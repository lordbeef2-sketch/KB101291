# JAVA OPENAPI: ModelVisitor (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/impl/ModelVisitor.html
- source_path: `com/nomagic/uml2/impl/ModelVisitor.html`
- source_sha256: `226b65d79723ae1c994441d5611d40b141c5f15e37b7fb486b6449a5f47ce0ce`
- captured_utc: `2026-07-14T16:59:02.523566+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.impl](package-summary.html)

## Interface ModelVisitor

All Superinterfaces:
`[AbstractVisitor](../../magicdraw/uml/AbstractVisitor.html)`

All Known Implementing Classes:
`[InheritanceVisitor](../../magicdraw/uml/InheritanceVisitor.html)`, `[ModelHierarchyVisitor](ModelHierarchyVisitor.html)`, `[ModelVisitorAdapter](ModelVisitorAdapter.html)`, `[Visitor](../../magicdraw/uml/Visitor.html)`

public interfaceModelVisitorextends [AbstractVisitor](../../magicdraw/uml/AbstractVisitor.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[visitAbstraction](#visitAbstraction(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Abstraction](../ext/magicdraw/classes/mddependencies/Abstraction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Abstraction`](../ext/magicdraw/classes/mddependencies/Abstraction.html).
`void`
`[visitAcceptCallAction](#visitAcceptCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([AcceptCallAction](../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`AcceptCallAction`](../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html).
`void`
`[visitAcceptEventAction](#visitAcceptEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([AcceptEventAction](../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`AcceptEventAction`](../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html).
`void`
`[visitAction](#visitAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Action](../ext/magicdraw/actions/mdbasicactions/Action.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Action`](../ext/magicdraw/actions/mdbasicactions/Action.html).
`void`
`[visitActionExecutionSpecification](#visitActionExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ActionExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActionExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActionExecutionSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html).
`void`
`[visitActionInputPin](#visitActionInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActionInputPin](../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActionInputPin`](../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html).
`void`
`[visitActivity](#visitActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Activity](../ext/magicdraw/activities/mdfundamentalactivities/Activity.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Activity`](../ext/magicdraw/activities/mdfundamentalactivities/Activity.html).
`void`
`[visitActivityEdge](#visitActivityEdge(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActivityEdge](../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActivityEdge`](../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html).
`void`
`[visitActivityFinalNode](#visitActivityFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityFinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActivityFinalNode](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActivityFinalNode`](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html).
`void`
`[visitActivityGroup](#visitActivityGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActivityGroup](../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActivityGroup`](../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html).
`void`
`[visitActivityNode](#visitActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActivityNode](../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActivityNode`](../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html).
`void`
`[visitActivityParameterNode](#visitActivityParameterNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActivityParameterNode](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActivityParameterNode`](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
`void`
`[visitActivityPartition](#visitActivityPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ActivityPartition](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ActivityPartition`](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html).
`void`
`[visitActor](#visitActor(com.nomagic.uml2.ext.magicdraw.mdusecases.Actor,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Actor](../ext/magicdraw/mdusecases/Actor.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Actor`](../ext/magicdraw/mdusecases/Actor.html).
`void`
`[visitAddStructuralFeatureValueAction](#visitAddStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([AddStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`AddStructuralFeatureValueAction`](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html).
`void`
`[visitAddVariableValueAction](#visitAddVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([AddVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`AddVariableValueAction`](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html).
`void`
`[visitAnyReceiveEvent](#visitAnyReceiveEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.AnyReceiveEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([AnyReceiveEvent](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`AnyReceiveEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html).
`void`
`[visitArtifact](#visitArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Artifact](../ext/magicdraw/deployments/mdartifacts/Artifact.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Artifact`](../ext/magicdraw/deployments/mdartifacts/Artifact.html).
`void`
`[visitAssociation](#visitAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Association](../ext/magicdraw/classes/mdkernel/Association.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Association`](../ext/magicdraw/classes/mdkernel/Association.html).
`void`
`[visitAssociationClass](#visitAssociationClass(com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses.AssociationClass,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([AssociationClass](../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`AssociationClass`](../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html).
`void`
`[visitBehavior](#visitBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Behavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Behavior`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html).
`void`
`[visitBehavioralFeature](#visitBehavioralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([BehavioralFeature](../ext/magicdraw/classes/mdkernel/BehavioralFeature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`BehavioralFeature`](../ext/magicdraw/classes/mdkernel/BehavioralFeature.html).
`void`
`[visitBehavioredClassifier](#visitBehavioredClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([BehavioredClassifier](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`BehavioredClassifier`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html).
`void`
`[visitBehaviorExecutionSpecification](#visitBehaviorExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.BehaviorExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([BehaviorExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`BehaviorExecutionSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html).
`void`
`[visitBooleanTaggedValue](#visitBooleanTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BooleanTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([BooleanTaggedValue](../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`BooleanTaggedValue`](../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html).
`void`
`[visitBroadcastSignalAction](#visitBroadcastSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.BroadcastSignalAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([BroadcastSignalAction](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`BroadcastSignalAction`](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html).
`void`
`[visitCallAction](#visitCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CallAction](../ext/magicdraw/actions/mdbasicactions/CallAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CallAction`](../ext/magicdraw/actions/mdbasicactions/CallAction.html).
`void`
`[visitCallBehaviorAction](#visitCallBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CallBehaviorAction](../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CallBehaviorAction`](../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html).
`void`
`[visitCallEvent](#visitCallEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CallEvent](../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CallEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html).
`void`
`[visitCallOperationAction](#visitCallOperationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CallOperationAction](../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CallOperationAction`](../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html).
`void`
`[visitCentralBufferNode](#visitCentralBufferNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.CentralBufferNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CentralBufferNode](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CentralBufferNode`](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html).
`void`
`[visitChangeEvent](#visitChangeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ChangeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ChangeEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html).
`void`
`[visitClass](#visitClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Class](../ext/magicdraw/classes/mdkernel/Class.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Class`](../ext/magicdraw/classes/mdkernel/Class.html).
`void`
`[visitClassifier](#visitClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Classifier](../ext/magicdraw/classes/mdkernel/Classifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Classifier`](../ext/magicdraw/classes/mdkernel/Classifier.html).
`void`
`[visitClassifierTemplateParameter](#visitClassifierTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ClassifierTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ClassifierTemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html).
`void`
`[visitClause](#visitClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Clause](../ext/magicdraw/activities/mdstructuredactivities/Clause.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Clause`](../ext/magicdraw/activities/mdstructuredactivities/Clause.html).
`void`
`[visitClearAssociationAction](#visitClearAssociationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ClearAssociationAction](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ClearAssociationAction`](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html).
`void`
`[visitClearStructuralFeatureAction](#visitClearStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ClearStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ClearStructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html).
`void`
`[visitClearVariableAction](#visitClearVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ClearVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ClearVariableAction](../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ClearVariableAction`](../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html).
`void`
`[visitCollaboration](#visitCollaboration(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.Collaboration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Collaboration](../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Collaboration`](../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html).
`void`
`[visitCollaborationUse](#visitCollaborationUse(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CollaborationUse](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CollaborationUse`](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html).
`void`
`[visitCombinedFragment](#visitCombinedFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CombinedFragment](../ext/magicdraw/interactions/mdfragments/CombinedFragment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CombinedFragment`](../ext/magicdraw/interactions/mdfragments/CombinedFragment.html).
`void`
`[visitComment](#visitComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Comment](../ext/magicdraw/classes/mdkernel/Comment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Comment`](../ext/magicdraw/classes/mdkernel/Comment.html).
`void`
`[visitCommunicationPath](#visitCommunicationPath(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.CommunicationPath,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CommunicationPath](../ext/magicdraw/deployments/mdnodes/CommunicationPath.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CommunicationPath`](../ext/magicdraw/deployments/mdnodes/CommunicationPath.html).
`void`
`[visitComponent](#visitComponent(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Component](../ext/magicdraw/components/mdbasiccomponents/Component.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Component`](../ext/magicdraw/components/mdbasiccomponents/Component.html).
`void`
`[visitComponentRealization](#visitComponentRealization(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.ComponentRealization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ComponentRealization](../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ComponentRealization`](../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html).
`void`
`[visitConditionalNode](#visitConditionalNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ConditionalNode](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ConditionalNode`](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html).
`void`
`[visitConnectableElement](#visitConnectableElement(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ConnectableElement](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ConnectableElement`](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html).
`void`
`[visitConnectableElementTemplateParameter](#visitConnectableElementTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ConnectableElementTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ConnectableElementTemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html).
`void`
`[visitConnectionPointReference](#visitConnectionPointReference(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.ConnectionPointReference,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ConnectionPointReference](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ConnectionPointReference`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html).
`void`
`[visitConnector](#visitConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Connector](../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Connector`](../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html).
`void`
`[visitConnectorEnd](#visitConnectorEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ConnectorEnd](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ConnectorEnd`](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html).
`void`
`[visitConsiderIgnoreFragment](#visitConsiderIgnoreFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.ConsiderIgnoreFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ConsiderIgnoreFragment](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ConsiderIgnoreFragment`](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html).
`void`
`[visitConstraint](#visitConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Constraint](../ext/magicdraw/classes/mdkernel/Constraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Constraint`](../ext/magicdraw/classes/mdkernel/Constraint.html).
`void`
`[visitContinuation](#visitContinuation(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Continuation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Continuation](../ext/magicdraw/interactions/mdfragments/Continuation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Continuation`](../ext/magicdraw/interactions/mdfragments/Continuation.html).
`void`
`[visitControlFlow](#visitControlFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ControlFlow](../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ControlFlow`](../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html).
`void`
`[visitControlNode](#visitControlNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ControlNode](../ext/magicdraw/activities/mdbasicactivities/ControlNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ControlNode`](../ext/magicdraw/activities/mdbasicactivities/ControlNode.html).
`void`
`[visitCreateLinkAction](#visitCreateLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CreateLinkAction](../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CreateLinkAction`](../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html).
`void`
`[visitCreateLinkObjectAction](#visitCreateLinkObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CreateLinkObjectAction](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CreateLinkObjectAction`](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html).
`void`
`[visitCreateObjectAction](#visitCreateObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([CreateObjectAction](../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`CreateObjectAction`](../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html).
`void`
`[visitDataStoreNode](#visitDataStoreNode(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.DataStoreNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DataStoreNode](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DataStoreNode`](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html).
`void`
`[visitDataType](#visitDataType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DataType](../ext/magicdraw/classes/mdkernel/DataType.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DataType`](../ext/magicdraw/classes/mdkernel/DataType.html).
`void`
`[visitDecisionNode](#visitDecisionNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.DecisionNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DecisionNode](../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DecisionNode`](../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html).
`void`
`[visitDependency](#visitDependency(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Dependency](../ext/magicdraw/classes/mddependencies/Dependency.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Dependency`](../ext/magicdraw/classes/mddependencies/Dependency.html).
`void`
`[visitDeployedArtifact](#visitDeployedArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DeployedArtifact](../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DeployedArtifact`](../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html).
`void`
`[visitDeployment](#visitDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Deployment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Deployment](../ext/magicdraw/deployments/mdnodes/Deployment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Deployment`](../ext/magicdraw/deployments/mdnodes/Deployment.html).
`void`
`[visitDeploymentSpecification](#visitDeploymentSpecification(com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments.DeploymentSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DeploymentSpecification](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DeploymentSpecification`](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html).
`void`
`[visitDeploymentTarget](#visitDeploymentTarget(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DeploymentTarget](../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DeploymentTarget`](../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html).
`void`
`[visitDestroyLinkAction](#visitDestroyLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DestroyLinkAction](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DestroyLinkAction`](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html).
`void`
`[visitDestroyObjectAction](#visitDestroyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DestroyObjectAction](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DestroyObjectAction`](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html).
`void`
`[visitDestructionOccurrenceSpecification](#visitDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.DestructionOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DestructionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DestructionOccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html).
`void`
`[visitDevice](#visitDevice(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Device,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Device](../ext/magicdraw/deployments/mdnodes/Device.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Device`](../ext/magicdraw/deployments/mdnodes/Device.html).
`void`
`[visitDiagram](#visitDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Diagram](../ext/magicdraw/classes/mdkernel/Diagram.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Diagram`](../ext/magicdraw/classes/mdkernel/Diagram.html).
`void`
`[visitDirectedRelationship](#visitDirectedRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DirectedRelationship](../ext/magicdraw/classes/mdkernel/DirectedRelationship.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DirectedRelationship`](../ext/magicdraw/classes/mdkernel/DirectedRelationship.html).
`void`
`[visitDuration](#visitDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Duration](../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Duration`](../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html).
`void`
`[visitDurationConstraint](#visitDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DurationConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DurationConstraint`](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html).
`void`
`[visitDurationInterval](#visitDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DurationInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DurationInterval`](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html).
`void`
`[visitDurationObservation](#visitDurationObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationObservation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([DurationObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`DurationObservation`](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html).
`void`
`[visitElement](#visitElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Element](../ext/magicdraw/classes/mdkernel/Element.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Element`](../ext/magicdraw/classes/mdkernel/Element.html).
`void`
`[visitElementImport](#visitElementImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementImport,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ElementImport](../ext/magicdraw/classes/mdkernel/ElementImport.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ElementImport`](../ext/magicdraw/classes/mdkernel/ElementImport.html).
`void`
`[visitElementTaggedValue](#visitElementTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ElementTaggedValue](../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ElementTaggedValue`](../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html).
`void`
`[visitElementValue](#visitElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ElementValue](../ext/magicdraw/classes/mdkernel/ElementValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ElementValue`](../ext/magicdraw/classes/mdkernel/ElementValue.html).
`void`
`[visitEncapsulatedClassifier](#visitEncapsulatedClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([EncapsulatedClassifier](../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`EncapsulatedClassifier`](../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html).
`void`
`[visitEnumeration](#visitEnumeration(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Enumeration](../ext/magicdraw/classes/mdkernel/Enumeration.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Enumeration`](../ext/magicdraw/classes/mdkernel/Enumeration.html).
`void`
`[visitEnumerationLiteral](#visitEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([EnumerationLiteral](../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`EnumerationLiteral`](../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html).
`void`
`[visitEvent](#visitEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Event](../ext/magicdraw/commonbehaviors/mdcommunications/Event.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Event`](../ext/magicdraw/commonbehaviors/mdcommunications/Event.html).
`void`
`[visitExceptionHandler](#visitExceptionHandler(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExceptionHandler,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExceptionHandler](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExceptionHandler`](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html).
`void`
`[visitExecutableNode](#visitExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExecutableNode](../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExecutableNode`](../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html).
`void`
`[visitExecutionEnvironment](#visitExecutionEnvironment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.ExecutionEnvironment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExecutionEnvironment](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExecutionEnvironment`](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html).
`void`
`[visitExecutionOccurrenceSpecification](#visitExecutionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExecutionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExecutionOccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html).
`void`
`[visitExecutionSpecification](#visitExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExecutionSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html).
`void`
`[visitExpansionNode](#visitExpansionNode(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExpansionNode](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExpansionNode`](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html).
`void`
`[visitExpansionRegion](#visitExpansionRegion(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionRegion,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExpansionRegion](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExpansionRegion`](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html).
`void`
`[visitExpression](#visitExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Expression](../ext/magicdraw/classes/mdkernel/Expression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Expression`](../ext/magicdraw/classes/mdkernel/Expression.html).
`void`
`[visitExtend](#visitExtend(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Extend](../ext/magicdraw/mdusecases/Extend.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Extend`](../ext/magicdraw/mdusecases/Extend.html).
`void`
`[visitExtension](#visitExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Extension](../ext/magicdraw/mdprofiles/Extension.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Extension`](../ext/magicdraw/mdprofiles/Extension.html).
`void`
`[visitExtensionEnd](#visitExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.ExtensionEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExtensionEnd](../ext/magicdraw/mdprofiles/ExtensionEnd.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExtensionEnd`](../ext/magicdraw/mdprofiles/ExtensionEnd.html).
`void`
`[visitExtensionPoint](#visitExtensionPoint(com.nomagic.uml2.ext.magicdraw.mdusecases.ExtensionPoint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ExtensionPoint](../ext/magicdraw/mdusecases/ExtensionPoint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ExtensionPoint`](../ext/magicdraw/mdusecases/ExtensionPoint.html).
`void`
`[visitFeature](#visitFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Feature](../ext/magicdraw/classes/mdkernel/Feature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Feature`](../ext/magicdraw/classes/mdkernel/Feature.html).
`void`
`[visitFinalNode](#visitFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([FinalNode](../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`FinalNode`](../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html).
`void`
`[visitFinalState](#visitFinalState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.FinalState,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([FinalState](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`FinalState`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html).
`void`
`[visitFlowFinalNode](#visitFlowFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FlowFinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([FlowFinalNode](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`FlowFinalNode`](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html).
`void`
`[visitForkNode](#visitForkNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ForkNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ForkNode](../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ForkNode`](../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html).
`void`
`[visitFunctionBehavior](#visitFunctionBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.FunctionBehavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([FunctionBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`FunctionBehavior`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html).
`void`
`[visitGate](#visitGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Gate](../ext/magicdraw/interactions/mdfragments/Gate.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Gate`](../ext/magicdraw/interactions/mdfragments/Gate.html).
`void`
`[visitGeneralization](#visitGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Generalization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Generalization](../ext/magicdraw/classes/mdkernel/Generalization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Generalization`](../ext/magicdraw/classes/mdkernel/Generalization.html).
`void`
`[visitGeneralizationSet](#visitGeneralizationSet(com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes.GeneralizationSet,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([GeneralizationSet](../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`GeneralizationSet`](../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html).
`void`
`[visitGeneralOrdering](#visitGeneralOrdering(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.GeneralOrdering,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([GeneralOrdering](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`GeneralOrdering`](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html).
`void`
`[visitImage](#visitImage(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Image](../ext/magicdraw/mdprofiles/Image.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Image`](../ext/magicdraw/mdprofiles/Image.html).
`void`
`[visitInclude](#visitInclude(com.nomagic.uml2.ext.magicdraw.mdusecases.Include,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Include](../ext/magicdraw/mdusecases/Include.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Include`](../ext/magicdraw/mdusecases/Include.html).
`void`
`[visitInformationFlow](#visitInformationFlow(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InformationFlow](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InformationFlow`](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html).
`void`
`[visitInformationItem](#visitInformationItem(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationItem,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InformationItem](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InformationItem`](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html).
`void`
`[visitInitialNode](#visitInitialNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.InitialNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InitialNode](../ext/magicdraw/activities/mdbasicactivities/InitialNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InitialNode`](../ext/magicdraw/activities/mdbasicactivities/InitialNode.html).
`void`
`[visitInputPin](#visitInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InputPin](../ext/magicdraw/actions/mdbasicactions/InputPin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InputPin`](../ext/magicdraw/actions/mdbasicactions/InputPin.html).
`void`
`[visitInstanceSpecification](#visitInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InstanceSpecification](../ext/magicdraw/classes/mdkernel/InstanceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InstanceSpecification`](../ext/magicdraw/classes/mdkernel/InstanceSpecification.html).
`void`
`[visitInstanceValue](#visitInstanceValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InstanceValue](../ext/magicdraw/classes/mdkernel/InstanceValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InstanceValue`](../ext/magicdraw/classes/mdkernel/InstanceValue.html).
`void`
`[visitIntegerTaggedValue](#visitIntegerTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.IntegerTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([IntegerTaggedValue](../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`IntegerTaggedValue`](../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html).
`void`
`[visitInteraction](#visitInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Interaction](../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Interaction`](../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html).
`void`
`[visitInteractionConstraint](#visitInteractionConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InteractionConstraint](../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InteractionConstraint`](../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html).
`void`
`[visitInteractionFragment](#visitInteractionFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InteractionFragment](../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InteractionFragment`](../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html).
`void`
`[visitInteractionOperand](#visitInteractionOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InteractionOperand](../ext/magicdraw/interactions/mdfragments/InteractionOperand.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InteractionOperand`](../ext/magicdraw/interactions/mdfragments/InteractionOperand.html).
`void`
`[visitInteractionUse](#visitInteractionUse(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InteractionUse](../ext/magicdraw/interactions/mdfragments/InteractionUse.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InteractionUse`](../ext/magicdraw/interactions/mdfragments/InteractionUse.html).
`void`
`[visitInterface](#visitInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Interface](../ext/magicdraw/classes/mdinterfaces/Interface.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Interface`](../ext/magicdraw/classes/mdinterfaces/Interface.html).
`void`
`[visitInterfaceRealization](#visitInterfaceRealization(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.InterfaceRealization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InterfaceRealization](../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InterfaceRealization`](../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html).
`void`
`[visitInterruptibleActivityRegion](#visitInterruptibleActivityRegion(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InterruptibleActivityRegion](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InterruptibleActivityRegion`](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html).
`void`
`[visitInterval](#visitInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Interval](../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Interval`](../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html).
`void`
`[visitIntervalConstraint](#visitIntervalConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([IntervalConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`IntervalConstraint`](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html).
`void`
`[visitInvocationAction](#visitInvocationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([InvocationAction](../ext/magicdraw/actions/mdbasicactions/InvocationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`InvocationAction`](../ext/magicdraw/actions/mdbasicactions/InvocationAction.html).
`void`
`[visitJoinNode](#visitJoinNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([JoinNode](../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`JoinNode`](../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html).
`void`
`[visitLifeline](#visitLifeline(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Lifeline](../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Lifeline`](../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html).
`void`
`[visitLinkAction](#visitLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LinkAction](../ext/magicdraw/actions/mdintermediateactions/LinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LinkAction`](../ext/magicdraw/actions/mdintermediateactions/LinkAction.html).
`void`
`[visitLinkEndCreationData](#visitLinkEndCreationData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LinkEndCreationData](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LinkEndCreationData`](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html).
`void`
`[visitLinkEndData](#visitLinkEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LinkEndData](../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LinkEndData`](../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html).
`void`
`[visitLinkEndDestructionData](#visitLinkEndDestructionData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LinkEndDestructionData](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LinkEndDestructionData`](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html).
`void`
`[visitLiteralBoolean](#visitLiteralBoolean(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralBoolean,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralBoolean](../ext/magicdraw/classes/mdkernel/LiteralBoolean.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralBoolean`](../ext/magicdraw/classes/mdkernel/LiteralBoolean.html).
`void`
`[visitLiteralInteger](#visitLiteralInteger(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralInteger,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralInteger](../ext/magicdraw/classes/mdkernel/LiteralInteger.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralInteger`](../ext/magicdraw/classes/mdkernel/LiteralInteger.html).
`void`
`[visitLiteralNull](#visitLiteralNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralNull,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralNull](../ext/magicdraw/classes/mdkernel/LiteralNull.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralNull`](../ext/magicdraw/classes/mdkernel/LiteralNull.html).
`void`
`[visitLiteralReal](#visitLiteralReal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralReal,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralReal](../ext/magicdraw/classes/mdkernel/LiteralReal.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralReal`](../ext/magicdraw/classes/mdkernel/LiteralReal.html).
`void`
`[visitLiteralSpecification](#visitLiteralSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralSpecification](../ext/magicdraw/classes/mdkernel/LiteralSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralSpecification`](../ext/magicdraw/classes/mdkernel/LiteralSpecification.html).
`void`
`[visitLiteralString](#visitLiteralString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralString,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralString](../ext/magicdraw/classes/mdkernel/LiteralString.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralString`](../ext/magicdraw/classes/mdkernel/LiteralString.html).
`void`
`[visitLiteralUnlimitedNatural](#visitLiteralUnlimitedNatural(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralUnlimitedNatural,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LiteralUnlimitedNatural](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LiteralUnlimitedNatural`](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html).
`void`
`[visitLoopNode](#visitLoopNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([LoopNode](../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`LoopNode`](../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html).
`void`
`[visitManifestation](#visitManifestation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Manifestation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Manifestation](../ext/magicdraw/deployments/mdartifacts/Manifestation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Manifestation`](../ext/magicdraw/deployments/mdartifacts/Manifestation.html).
`void`
`[visitMergeNode](#visitMergeNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.MergeNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([MergeNode](../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`MergeNode`](../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html).
`void`
`[visitMessage](#visitMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Message](../ext/magicdraw/interactions/mdbasicinteractions/Message.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Message`](../ext/magicdraw/interactions/mdbasicinteractions/Message.html).
`void`
`[visitMessageEnd](#visitMessageEnd(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([MessageEnd](../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`MessageEnd`](../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html).
`void`
`[visitMessageEvent](#visitMessageEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.MessageEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([MessageEvent](../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`MessageEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html).
`void`
`[visitMessageOccurrenceSpecification](#visitMessageOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([MessageOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`MessageOccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html).
`void`
`[visitModel](#visitModel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Model](../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Model`](../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html).
`void`
`[visitMultiplicityElement](#visitMultiplicityElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([MultiplicityElement](../ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`MultiplicityElement`](../ext/magicdraw/classes/mdkernel/MultiplicityElement.html).
`void`
`[visitNamedElement](#visitNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([NamedElement](../ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`NamedElement`](../ext/magicdraw/classes/mdkernel/NamedElement.html).
`void`
`[visitNamespace](#visitNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Namespace](../ext/magicdraw/classes/mdkernel/Namespace.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Namespace`](../ext/magicdraw/classes/mdkernel/Namespace.html).
`void`
`[visitNode](#visitNode(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Node,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Node](../ext/magicdraw/deployments/mdnodes/Node.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Node`](../ext/magicdraw/deployments/mdnodes/Node.html).
`void`
`[visitObjectFlow](#visitObjectFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ObjectFlow](../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ObjectFlow`](../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html).
`void`
`[visitObjectNode](#visitObjectNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ObjectNode](../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ObjectNode`](../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html).
`void`
`[visitObservation](#visitObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Observation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Observation](../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Observation`](../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html).
`void`
`[visitOccurrenceSpecification](#visitOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.OccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([OccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`OccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html).
`void`
`[visitOpaqueAction](#visitOpaqueAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([OpaqueAction](../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`OpaqueAction`](../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html).
`void`
`[visitOpaqueBehavior](#visitOpaqueBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.OpaqueBehavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([OpaqueBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`OpaqueBehavior`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html).
`void`
`[visitOpaqueExpression](#visitOpaqueExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([OpaqueExpression](../ext/magicdraw/classes/mdkernel/OpaqueExpression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`OpaqueExpression`](../ext/magicdraw/classes/mdkernel/OpaqueExpression.html).
`void`
`[visitOperation](#visitOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Operation](../ext/magicdraw/classes/mdkernel/Operation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Operation`](../ext/magicdraw/classes/mdkernel/Operation.html).
`void`
`[visitOperationTemplateParameter](#visitOperationTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([OperationTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`OperationTemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html).
`void`
`[visitOutputPin](#visitOutputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([OutputPin](../ext/magicdraw/actions/mdbasicactions/OutputPin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`OutputPin`](../ext/magicdraw/actions/mdbasicactions/OutputPin.html).
`void`
`[visitPackage](#visitPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Package](../ext/magicdraw/classes/mdkernel/Package.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Package`](../ext/magicdraw/classes/mdkernel/Package.html).
`void`
`[visitPackageableElement](#visitPackageableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([PackageableElement](../ext/magicdraw/classes/mdkernel/PackageableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`PackageableElement`](../ext/magicdraw/classes/mdkernel/PackageableElement.html).
`void`
`[visitPackageImport](#visitPackageImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageImport,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([PackageImport](../ext/magicdraw/classes/mdkernel/PackageImport.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`PackageImport`](../ext/magicdraw/classes/mdkernel/PackageImport.html).
`void`
`[visitPackageMerge](#visitPackageMerge(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageMerge,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([PackageMerge](../ext/magicdraw/classes/mdkernel/PackageMerge.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`PackageMerge`](../ext/magicdraw/classes/mdkernel/PackageMerge.html).
`void`
`[visitParameter](#visitParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Parameter](../ext/magicdraw/classes/mdkernel/Parameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Parameter`](../ext/magicdraw/classes/mdkernel/Parameter.html).
`void`
`[visitParameterableElement](#visitParameterableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ParameterableElement](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ParameterableElement`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html).
`void`
`[visitParameterSet](#visitParameterSet(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ParameterSet](../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ParameterSet`](../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html).
`void`
`[visitPartDecomposition](#visitPartDecomposition(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([PartDecomposition](../ext/magicdraw/interactions/mdfragments/PartDecomposition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`PartDecomposition`](../ext/magicdraw/interactions/mdfragments/PartDecomposition.html).
`void`
`[visitPin](#visitPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Pin](../ext/magicdraw/actions/mdbasicactions/Pin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Pin`](../ext/magicdraw/actions/mdbasicactions/Pin.html).
`void`
`[visitPort](#visitPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Port](../ext/magicdraw/compositestructures/mdports/Port.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Port`](../ext/magicdraw/compositestructures/mdports/Port.html).
`void`
`[visitPrimitiveType](#visitPrimitiveType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PrimitiveType,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([PrimitiveType](../ext/magicdraw/classes/mdkernel/PrimitiveType.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`PrimitiveType`](../ext/magicdraw/classes/mdkernel/PrimitiveType.html).
`void`
`[visitProfile](#visitProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Profile](../ext/magicdraw/mdprofiles/Profile.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Profile`](../ext/magicdraw/mdprofiles/Profile.html).
`void`
`[visitProfileApplication](#visitProfileApplication(com.nomagic.uml2.ext.magicdraw.mdprofiles.ProfileApplication,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ProfileApplication](../ext/magicdraw/mdprofiles/ProfileApplication.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ProfileApplication`](../ext/magicdraw/mdprofiles/ProfileApplication.html).
`void`
`[visitProperty](#visitProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Property](../ext/magicdraw/classes/mdkernel/Property.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Property`](../ext/magicdraw/classes/mdkernel/Property.html).
`void`
`[visitProtocolConformance](#visitProtocolConformance(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolConformance,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ProtocolConformance](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ProtocolConformance`](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html).
`void`
`[visitProtocolStateMachine](#visitProtocolStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ProtocolStateMachine](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ProtocolStateMachine`](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html).
`void`
`[visitProtocolTransition](#visitProtocolTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ProtocolTransition](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ProtocolTransition`](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html).
`void`
`[visitPseudostate](#visitPseudostate(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Pseudostate,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Pseudostate](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Pseudostate`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html).
`void`
`[visitQualifierValue](#visitQualifierValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([QualifierValue](../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`QualifierValue`](../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html).
`void`
`[visitRaiseExceptionAction](#visitRaiseExceptionAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([RaiseExceptionAction](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`RaiseExceptionAction`](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html).
`void`
`[visitReadExtentAction](#visitReadExtentAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadExtentAction](../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadExtentAction`](../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html).
`void`
`[visitReadIsClassifiedObjectAction](#visitReadIsClassifiedObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadIsClassifiedObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadIsClassifiedObjectAction`](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html).
`void`
`[visitReadLinkAction](#visitReadLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadLinkAction](../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadLinkAction`](../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html).
`void`
`[visitReadLinkObjectEndAction](#visitReadLinkObjectEndAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadLinkObjectEndAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadLinkObjectEndAction`](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html).
`void`
`[visitReadLinkObjectEndQualifierAction](#visitReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadLinkObjectEndQualifierAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadLinkObjectEndQualifierAction`](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html).
`void`
`[visitReadSelfAction](#visitReadSelfAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadSelfAction](../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadSelfAction`](../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html).
`void`
`[visitReadStructuralFeatureAction](#visitReadStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadStructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html).
`void`
`[visitReadVariableAction](#visitReadVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReadVariableAction](../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReadVariableAction`](../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html).
`void`
`[visitRealization](#visitRealization(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Realization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Realization](../ext/magicdraw/classes/mddependencies/Realization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Realization`](../ext/magicdraw/classes/mddependencies/Realization.html).
`void`
`[visitRealTaggedValue](#visitRealTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RealTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([RealTaggedValue](../ext/magicdraw/classes/mdkernel/RealTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`RealTaggedValue`](../ext/magicdraw/classes/mdkernel/RealTaggedValue.html).
`void`
`[visitReception](#visitReception(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Reception](../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Reception`](../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html).
`void`
`[visitReclassifyObjectAction](#visitReclassifyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReclassifyObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReclassifyObjectAction`](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html).
`void`
`[visitRedefinableElement](#visitRedefinableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([RedefinableElement](../ext/magicdraw/classes/mdkernel/RedefinableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`RedefinableElement`](../ext/magicdraw/classes/mdkernel/RedefinableElement.html).
`void`
`[visitRedefinableTemplateSignature](#visitRedefinableTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([RedefinableTemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`RedefinableTemplateSignature`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html).
`void`
`[visitReduceAction](#visitReduceAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReduceAction](../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReduceAction`](../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html).
`void`
`[visitRegion](#visitRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Region](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Region`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html).
`void`
`[visitRelationship](#visitRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Relationship](../ext/magicdraw/classes/mdkernel/Relationship.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Relationship`](../ext/magicdraw/classes/mdkernel/Relationship.html).
`void`
`[visitRemoveStructuralFeatureValueAction](#visitRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([RemoveStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`RemoveStructuralFeatureValueAction`](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html).
`void`
`[visitRemoveVariableValueAction](#visitRemoveVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([RemoveVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`RemoveVariableValueAction`](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html).
`void`
`[visitReplyAction](#visitReplyAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ReplyAction](../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ReplyAction`](../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html).
`void`
`[visitSendObjectAction](#visitSendObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([SendObjectAction](../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`SendObjectAction`](../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html).
`void`
`[visitSendSignalAction](#visitSendSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([SendSignalAction](../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`SendSignalAction`](../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html).
`void`
`[visitSequenceNode](#visitSequenceNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([SequenceNode](../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`SequenceNode`](../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html).
`void`
`[visitSignal](#visitSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Signal](../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Signal`](../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html).
`void`
`[visitSignalEvent](#visitSignalEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.SignalEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([SignalEvent](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`SignalEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html).
`void`
`[visitSlot](#visitSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Slot](../ext/magicdraw/classes/mdkernel/Slot.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Slot`](../ext/magicdraw/classes/mdkernel/Slot.html).
`void`
`[visitStartClassifierBehaviorAction](#visitStartClassifierBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StartClassifierBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StartClassifierBehaviorAction`](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html).
`void`
`[visitStartObjectBehaviorAction](#visitStartObjectBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StartObjectBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StartObjectBehaviorAction`](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html).
`void`
`[visitState](#visitState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([State](../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`State`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html).
`void`
`[visitStateInvariant](#visitStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StateInvariant](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StateInvariant`](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html).
`void`
`[visitStateMachine](#visitStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StateMachine](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StateMachine`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html).
`void`
`[visitStereotype](#visitStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Stereotype](../ext/magicdraw/mdprofiles/Stereotype.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Stereotype`](../ext/magicdraw/mdprofiles/Stereotype.html).
`void`
`[visitStringExpression](#visitStringExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StringExpression](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StringExpression`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html).
`void`
`[visitStringTaggedValue](#visitStringTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StringTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StringTaggedValue](../ext/magicdraw/classes/mdkernel/StringTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StringTaggedValue`](../ext/magicdraw/classes/mdkernel/StringTaggedValue.html).
`void`
`[visitStructuralFeature](#visitStructuralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StructuralFeature](../ext/magicdraw/classes/mdkernel/StructuralFeature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StructuralFeature`](../ext/magicdraw/classes/mdkernel/StructuralFeature.html).
`void`
`[visitStructuralFeatureAction](#visitStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html).
`void`
`[visitStructuredActivityNode](#visitStructuredActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StructuredActivityNode](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StructuredActivityNode`](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html).
`void`
`[visitStructuredClassifier](#visitStructuredClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([StructuredClassifier](../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`StructuredClassifier`](../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html).
`void`
`[visitSubstitution](#visitSubstitution(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Substitution,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Substitution](../ext/magicdraw/classes/mddependencies/Substitution.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Substitution`](../ext/magicdraw/classes/mddependencies/Substitution.html).
`void`
`[visitTaggedValue](#visitTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TaggedValue](../ext/magicdraw/classes/mdkernel/TaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TaggedValue`](../ext/magicdraw/classes/mdkernel/TaggedValue.html).
`void`
`[visitTemplateableElement](#visitTemplateableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TemplateableElement](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TemplateableElement`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html).
`void`
`[visitTemplateBinding](#visitTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TemplateBinding](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TemplateBinding`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html).
`void`
`[visitTemplateParameter](#visitTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html).
`void`
`[visitTemplateParameterSubstitution](#visitTemplateParameterSubstitution(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TemplateParameterSubstitution](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TemplateParameterSubstitution`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html).
`void`
`[visitTemplateSignature](#visitTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TemplateSignature`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html).
`void`
`[visitTestIdentityAction](#visitTestIdentityAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TestIdentityAction](../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TestIdentityAction`](../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html).
`void`
`[visitTimeConstraint](#visitTimeConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TimeConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TimeConstraint`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html).
`void`
`[visitTimeEvent](#visitTimeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.TimeEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TimeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TimeEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html).
`void`
`[visitTimeExpression](#visitTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TimeExpression](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TimeExpression`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html).
`void`
`[visitTimeInterval](#visitTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TimeInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TimeInterval`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html).
`void`
`[visitTimeObservation](#visitTimeObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeObservation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TimeObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TimeObservation`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html).
`void`
`[visitTransition](#visitTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Transition](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Transition`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html).
`void`
`[visitTrigger](#visitTrigger(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Trigger](../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Trigger`](../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html).
`void`
`[visitType](#visitType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Type](../ext/magicdraw/classes/mdkernel/Type.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Type`](../ext/magicdraw/classes/mdkernel/Type.html).
`void`
`[visitTypedElement](#visitTypedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([TypedElement](../ext/magicdraw/classes/mdkernel/TypedElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`TypedElement`](../ext/magicdraw/classes/mdkernel/TypedElement.html).
`void`
`[visitUnmarshallAction](#visitUnmarshallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([UnmarshallAction](../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`UnmarshallAction`](../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html).
`void`
`[visitUsage](#visitUsage(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Usage,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Usage](../ext/magicdraw/classes/mddependencies/Usage.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Usage`](../ext/magicdraw/classes/mddependencies/Usage.html).
`void`
`[visitUseCase](#visitUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([UseCase](../ext/magicdraw/mdusecases/UseCase.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`UseCase`](../ext/magicdraw/mdusecases/UseCase.html).
`void`
`[visitValuePin](#visitValuePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ValuePin](../ext/magicdraw/actions/mdbasicactions/ValuePin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ValuePin`](../ext/magicdraw/actions/mdbasicactions/ValuePin.html).
`void`
`[visitValueSpecification](#visitValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ValueSpecification](../ext/magicdraw/classes/mdkernel/ValueSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ValueSpecification`](../ext/magicdraw/classes/mdkernel/ValueSpecification.html).
`void`
`[visitValueSpecificationAction](#visitValueSpecificationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([ValueSpecificationAction](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`ValueSpecificationAction`](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html).
`void`
`[visitVariable](#visitVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Variable,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Variable](../ext/magicdraw/activities/mdstructuredactivities/Variable.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Variable`](../ext/magicdraw/activities/mdstructuredactivities/Variable.html).
`void`
`[visitVariableAction](#visitVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.VariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([VariableAction](../ext/magicdraw/actions/mdstructuredactions/VariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`VariableAction`](../ext/magicdraw/actions/mdstructuredactions/VariableAction.html).
`void`
`[visitVertex](#visitVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([Vertex](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`Vertex`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html).
`void`
`[visitWriteLinkAction](#visitWriteLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([WriteLinkAction](../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`WriteLinkAction`](../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html).
`void`
`[visitWriteStructuralFeatureAction](#visitWriteStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([WriteStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`WriteStructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html).
`void`
`[visitWriteVariableAction](#visitWriteVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext))([WriteVariableAction](../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)`
Visitor method for [`WriteVariableAction`](../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html).

============ METHOD DETAIL ========== 
Method Details
visitAbstraction
void visitAbstraction([Abstraction](../ext/magicdraw/classes/mddependencies/Abstraction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Abstraction`](../ext/magicdraw/classes/mddependencies/Abstraction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAcceptCallAction
void visitAcceptCallAction([AcceptCallAction](../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`AcceptCallAction`](../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAcceptEventAction
void visitAcceptEventAction([AcceptEventAction](../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`AcceptEventAction`](../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAction
void visitAction([Action](../ext/magicdraw/actions/mdbasicactions/Action.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Action`](../ext/magicdraw/actions/mdbasicactions/Action.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActionExecutionSpecification
void visitActionExecutionSpecification([ActionExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActionExecutionSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActionInputPin
void visitActionInputPin([ActionInputPin](../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActionInputPin`](../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivity
void visitActivity([Activity](../ext/magicdraw/activities/mdfundamentalactivities/Activity.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Activity`](../ext/magicdraw/activities/mdfundamentalactivities/Activity.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivityEdge
void visitActivityEdge([ActivityEdge](../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActivityEdge`](../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivityFinalNode
void visitActivityFinalNode([ActivityFinalNode](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActivityFinalNode`](../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivityGroup
void visitActivityGroup([ActivityGroup](../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActivityGroup`](../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivityNode
void visitActivityNode([ActivityNode](../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActivityNode`](../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivityParameterNode
void visitActivityParameterNode([ActivityParameterNode](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActivityParameterNode`](../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActivityPartition
void visitActivityPartition([ActivityPartition](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ActivityPartition`](../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitActor
void visitActor([Actor](../ext/magicdraw/mdusecases/Actor.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Actor`](../ext/magicdraw/mdusecases/Actor.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAddStructuralFeatureValueAction
void visitAddStructuralFeatureValueAction([AddStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`AddStructuralFeatureValueAction`](../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAddVariableValueAction
void visitAddVariableValueAction([AddVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`AddVariableValueAction`](../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAnyReceiveEvent
void visitAnyReceiveEvent([AnyReceiveEvent](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`AnyReceiveEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitArtifact
void visitArtifact([Artifact](../ext/magicdraw/deployments/mdartifacts/Artifact.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Artifact`](../ext/magicdraw/deployments/mdartifacts/Artifact.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAssociation
void visitAssociation([Association](../ext/magicdraw/classes/mdkernel/Association.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Association`](../ext/magicdraw/classes/mdkernel/Association.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitAssociationClass
void visitAssociationClass([AssociationClass](../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`AssociationClass`](../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitBehavior
void visitBehavior([Behavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Behavior`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitBehaviorExecutionSpecification
void visitBehaviorExecutionSpecification([BehaviorExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`BehaviorExecutionSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitBehavioralFeature
void visitBehavioralFeature([BehavioralFeature](../ext/magicdraw/classes/mdkernel/BehavioralFeature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`BehavioralFeature`](../ext/magicdraw/classes/mdkernel/BehavioralFeature.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitBehavioredClassifier
void visitBehavioredClassifier([BehavioredClassifier](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`BehavioredClassifier`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitBroadcastSignalAction
void visitBroadcastSignalAction([BroadcastSignalAction](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`BroadcastSignalAction`](../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCallAction
void visitCallAction([CallAction](../ext/magicdraw/actions/mdbasicactions/CallAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CallAction`](../ext/magicdraw/actions/mdbasicactions/CallAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCallBehaviorAction
void visitCallBehaviorAction([CallBehaviorAction](../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CallBehaviorAction`](../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCallEvent
void visitCallEvent([CallEvent](../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CallEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCallOperationAction
void visitCallOperationAction([CallOperationAction](../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CallOperationAction`](../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCentralBufferNode
void visitCentralBufferNode([CentralBufferNode](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CentralBufferNode`](../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitChangeEvent
void visitChangeEvent([ChangeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ChangeEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClass
void visitClass([Class](../ext/magicdraw/classes/mdkernel/Class.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Class`](../ext/magicdraw/classes/mdkernel/Class.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClassifier
void visitClassifier([Classifier](../ext/magicdraw/classes/mdkernel/Classifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Classifier`](../ext/magicdraw/classes/mdkernel/Classifier.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClassifierTemplateParameter
void visitClassifierTemplateParameter([ClassifierTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ClassifierTemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClause
void visitClause([Clause](../ext/magicdraw/activities/mdstructuredactivities/Clause.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Clause`](../ext/magicdraw/activities/mdstructuredactivities/Clause.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClearAssociationAction
void visitClearAssociationAction([ClearAssociationAction](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ClearAssociationAction`](../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClearStructuralFeatureAction
void visitClearStructuralFeatureAction([ClearStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ClearStructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitClearVariableAction
void visitClearVariableAction([ClearVariableAction](../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ClearVariableAction`](../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCollaboration
void visitCollaboration([Collaboration](../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Collaboration`](../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCollaborationUse
void visitCollaborationUse([CollaborationUse](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CollaborationUse`](../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCombinedFragment
void visitCombinedFragment([CombinedFragment](../ext/magicdraw/interactions/mdfragments/CombinedFragment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CombinedFragment`](../ext/magicdraw/interactions/mdfragments/CombinedFragment.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitComment
void visitComment([Comment](../ext/magicdraw/classes/mdkernel/Comment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Comment`](../ext/magicdraw/classes/mdkernel/Comment.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCommunicationPath
void visitCommunicationPath([CommunicationPath](../ext/magicdraw/deployments/mdnodes/CommunicationPath.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CommunicationPath`](../ext/magicdraw/deployments/mdnodes/CommunicationPath.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitComponent
void visitComponent([Component](../ext/magicdraw/components/mdbasiccomponents/Component.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Component`](../ext/magicdraw/components/mdbasiccomponents/Component.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitComponentRealization
void visitComponentRealization([ComponentRealization](../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ComponentRealization`](../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConditionalNode
void visitConditionalNode([ConditionalNode](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ConditionalNode`](../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConnectableElement
void visitConnectableElement([ConnectableElement](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ConnectableElement`](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConnectableElementTemplateParameter
void visitConnectableElementTemplateParameter([ConnectableElementTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ConnectableElementTemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConnectionPointReference
void visitConnectionPointReference([ConnectionPointReference](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ConnectionPointReference`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConnector
void visitConnector([Connector](../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Connector`](../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConnectorEnd
void visitConnectorEnd([ConnectorEnd](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ConnectorEnd`](../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConsiderIgnoreFragment
void visitConsiderIgnoreFragment([ConsiderIgnoreFragment](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ConsiderIgnoreFragment`](../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitConstraint
void visitConstraint([Constraint](../ext/magicdraw/classes/mdkernel/Constraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Constraint`](../ext/magicdraw/classes/mdkernel/Constraint.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitContinuation
void visitContinuation([Continuation](../ext/magicdraw/interactions/mdfragments/Continuation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Continuation`](../ext/magicdraw/interactions/mdfragments/Continuation.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitControlFlow
void visitControlFlow([ControlFlow](../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ControlFlow`](../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitControlNode
void visitControlNode([ControlNode](../ext/magicdraw/activities/mdbasicactivities/ControlNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ControlNode`](../ext/magicdraw/activities/mdbasicactivities/ControlNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCreateLinkAction
void visitCreateLinkAction([CreateLinkAction](../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CreateLinkAction`](../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCreateLinkObjectAction
void visitCreateLinkObjectAction([CreateLinkObjectAction](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CreateLinkObjectAction`](../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitCreateObjectAction
void visitCreateObjectAction([CreateObjectAction](../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`CreateObjectAction`](../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDataStoreNode
void visitDataStoreNode([DataStoreNode](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DataStoreNode`](../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDataType
void visitDataType([DataType](../ext/magicdraw/classes/mdkernel/DataType.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DataType`](../ext/magicdraw/classes/mdkernel/DataType.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDecisionNode
void visitDecisionNode([DecisionNode](../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DecisionNode`](../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDependency
void visitDependency([Dependency](../ext/magicdraw/classes/mddependencies/Dependency.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Dependency`](../ext/magicdraw/classes/mddependencies/Dependency.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDeployedArtifact
void visitDeployedArtifact([DeployedArtifact](../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DeployedArtifact`](../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDeployment
void visitDeployment([Deployment](../ext/magicdraw/deployments/mdnodes/Deployment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Deployment`](../ext/magicdraw/deployments/mdnodes/Deployment.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDeploymentSpecification
void visitDeploymentSpecification([DeploymentSpecification](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DeploymentSpecification`](../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDeploymentTarget
void visitDeploymentTarget([DeploymentTarget](../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DeploymentTarget`](../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDestroyLinkAction
void visitDestroyLinkAction([DestroyLinkAction](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DestroyLinkAction`](../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDestroyObjectAction
void visitDestroyObjectAction([DestroyObjectAction](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DestroyObjectAction`](../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDestructionOccurrenceSpecification
void visitDestructionOccurrenceSpecification([DestructionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DestructionOccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDevice
void visitDevice([Device](../ext/magicdraw/deployments/mdnodes/Device.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Device`](../ext/magicdraw/deployments/mdnodes/Device.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDiagram
void visitDiagram([Diagram](../ext/magicdraw/classes/mdkernel/Diagram.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Diagram`](../ext/magicdraw/classes/mdkernel/Diagram.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDirectedRelationship
void visitDirectedRelationship([DirectedRelationship](../ext/magicdraw/classes/mdkernel/DirectedRelationship.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DirectedRelationship`](../ext/magicdraw/classes/mdkernel/DirectedRelationship.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDuration
void visitDuration([Duration](../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Duration`](../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDurationConstraint
void visitDurationConstraint([DurationConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DurationConstraint`](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDurationInterval
void visitDurationInterval([DurationInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DurationInterval`](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitDurationObservation
void visitDurationObservation([DurationObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`DurationObservation`](../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitElement
void visitElement([Element](../ext/magicdraw/classes/mdkernel/Element.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Element`](../ext/magicdraw/classes/mdkernel/Element.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitElementImport
void visitElementImport([ElementImport](../ext/magicdraw/classes/mdkernel/ElementImport.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ElementImport`](../ext/magicdraw/classes/mdkernel/ElementImport.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitElementValue
void visitElementValue([ElementValue](../ext/magicdraw/classes/mdkernel/ElementValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ElementValue`](../ext/magicdraw/classes/mdkernel/ElementValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitEncapsulatedClassifier
void visitEncapsulatedClassifier([EncapsulatedClassifier](../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`EncapsulatedClassifier`](../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitEnumeration
void visitEnumeration([Enumeration](../ext/magicdraw/classes/mdkernel/Enumeration.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Enumeration`](../ext/magicdraw/classes/mdkernel/Enumeration.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitEnumerationLiteral
void visitEnumerationLiteral([EnumerationLiteral](../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`EnumerationLiteral`](../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitEvent
void visitEvent([Event](../ext/magicdraw/commonbehaviors/mdcommunications/Event.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Event`](../ext/magicdraw/commonbehaviors/mdcommunications/Event.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExceptionHandler
void visitExceptionHandler([ExceptionHandler](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExceptionHandler`](../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExecutableNode
void visitExecutableNode([ExecutableNode](../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExecutableNode`](../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExecutionEnvironment
void visitExecutionEnvironment([ExecutionEnvironment](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExecutionEnvironment`](../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExecutionOccurrenceSpecification
void visitExecutionOccurrenceSpecification([ExecutionOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExecutionOccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExecutionSpecification
void visitExecutionSpecification([ExecutionSpecification](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExecutionSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExpansionNode
void visitExpansionNode([ExpansionNode](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExpansionNode`](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExpansionRegion
void visitExpansionRegion([ExpansionRegion](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExpansionRegion`](../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExpression
void visitExpression([Expression](../ext/magicdraw/classes/mdkernel/Expression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Expression`](../ext/magicdraw/classes/mdkernel/Expression.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExtend
void visitExtend([Extend](../ext/magicdraw/mdusecases/Extend.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Extend`](../ext/magicdraw/mdusecases/Extend.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExtension
void visitExtension([Extension](../ext/magicdraw/mdprofiles/Extension.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Extension`](../ext/magicdraw/mdprofiles/Extension.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExtensionEnd
void visitExtensionEnd([ExtensionEnd](../ext/magicdraw/mdprofiles/ExtensionEnd.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExtensionEnd`](../ext/magicdraw/mdprofiles/ExtensionEnd.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitExtensionPoint
void visitExtensionPoint([ExtensionPoint](../ext/magicdraw/mdusecases/ExtensionPoint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ExtensionPoint`](../ext/magicdraw/mdusecases/ExtensionPoint.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitFeature
void visitFeature([Feature](../ext/magicdraw/classes/mdkernel/Feature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Feature`](../ext/magicdraw/classes/mdkernel/Feature.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitFinalNode
void visitFinalNode([FinalNode](../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`FinalNode`](../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitFinalState
void visitFinalState([FinalState](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`FinalState`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitFlowFinalNode
void visitFlowFinalNode([FlowFinalNode](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`FlowFinalNode`](../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitForkNode
void visitForkNode([ForkNode](../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ForkNode`](../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitFunctionBehavior
void visitFunctionBehavior([FunctionBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`FunctionBehavior`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitGate
void visitGate([Gate](../ext/magicdraw/interactions/mdfragments/Gate.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Gate`](../ext/magicdraw/interactions/mdfragments/Gate.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitGeneralOrdering
void visitGeneralOrdering([GeneralOrdering](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`GeneralOrdering`](../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitGeneralization
void visitGeneralization([Generalization](../ext/magicdraw/classes/mdkernel/Generalization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Generalization`](../ext/magicdraw/classes/mdkernel/Generalization.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitGeneralizationSet
void visitGeneralizationSet([GeneralizationSet](../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`GeneralizationSet`](../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitImage
void visitImage([Image](../ext/magicdraw/mdprofiles/Image.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Image`](../ext/magicdraw/mdprofiles/Image.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInclude
void visitInclude([Include](../ext/magicdraw/mdusecases/Include.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Include`](../ext/magicdraw/mdusecases/Include.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInformationFlow
void visitInformationFlow([InformationFlow](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InformationFlow`](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInformationItem
void visitInformationItem([InformationItem](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InformationItem`](../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInitialNode
void visitInitialNode([InitialNode](../ext/magicdraw/activities/mdbasicactivities/InitialNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InitialNode`](../ext/magicdraw/activities/mdbasicactivities/InitialNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInputPin
void visitInputPin([InputPin](../ext/magicdraw/actions/mdbasicactions/InputPin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InputPin`](../ext/magicdraw/actions/mdbasicactions/InputPin.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInstanceSpecification
void visitInstanceSpecification([InstanceSpecification](../ext/magicdraw/classes/mdkernel/InstanceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InstanceSpecification`](../ext/magicdraw/classes/mdkernel/InstanceSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInstanceValue
void visitInstanceValue([InstanceValue](../ext/magicdraw/classes/mdkernel/InstanceValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InstanceValue`](../ext/magicdraw/classes/mdkernel/InstanceValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInteraction
void visitInteraction([Interaction](../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Interaction`](../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInteractionConstraint
void visitInteractionConstraint([InteractionConstraint](../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InteractionConstraint`](../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInteractionFragment
void visitInteractionFragment([InteractionFragment](../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InteractionFragment`](../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInteractionOperand
void visitInteractionOperand([InteractionOperand](../ext/magicdraw/interactions/mdfragments/InteractionOperand.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InteractionOperand`](../ext/magicdraw/interactions/mdfragments/InteractionOperand.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInteractionUse
void visitInteractionUse([InteractionUse](../ext/magicdraw/interactions/mdfragments/InteractionUse.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InteractionUse`](../ext/magicdraw/interactions/mdfragments/InteractionUse.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInterface
void visitInterface([Interface](../ext/magicdraw/classes/mdinterfaces/Interface.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Interface`](../ext/magicdraw/classes/mdinterfaces/Interface.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInterfaceRealization
void visitInterfaceRealization([InterfaceRealization](../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InterfaceRealization`](../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInterruptibleActivityRegion
void visitInterruptibleActivityRegion([InterruptibleActivityRegion](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InterruptibleActivityRegion`](../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInterval
void visitInterval([Interval](../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Interval`](../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitIntervalConstraint
void visitIntervalConstraint([IntervalConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`IntervalConstraint`](../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitInvocationAction
void visitInvocationAction([InvocationAction](../ext/magicdraw/actions/mdbasicactions/InvocationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`InvocationAction`](../ext/magicdraw/actions/mdbasicactions/InvocationAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitJoinNode
void visitJoinNode([JoinNode](../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`JoinNode`](../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLifeline
void visitLifeline([Lifeline](../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Lifeline`](../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLinkAction
void visitLinkAction([LinkAction](../ext/magicdraw/actions/mdintermediateactions/LinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LinkAction`](../ext/magicdraw/actions/mdintermediateactions/LinkAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLinkEndCreationData
void visitLinkEndCreationData([LinkEndCreationData](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LinkEndCreationData`](../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLinkEndData
void visitLinkEndData([LinkEndData](../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LinkEndData`](../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLinkEndDestructionData
void visitLinkEndDestructionData([LinkEndDestructionData](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LinkEndDestructionData`](../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralBoolean
void visitLiteralBoolean([LiteralBoolean](../ext/magicdraw/classes/mdkernel/LiteralBoolean.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralBoolean`](../ext/magicdraw/classes/mdkernel/LiteralBoolean.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralInteger
void visitLiteralInteger([LiteralInteger](../ext/magicdraw/classes/mdkernel/LiteralInteger.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralInteger`](../ext/magicdraw/classes/mdkernel/LiteralInteger.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralNull
void visitLiteralNull([LiteralNull](../ext/magicdraw/classes/mdkernel/LiteralNull.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralNull`](../ext/magicdraw/classes/mdkernel/LiteralNull.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralReal
void visitLiteralReal([LiteralReal](../ext/magicdraw/classes/mdkernel/LiteralReal.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralReal`](../ext/magicdraw/classes/mdkernel/LiteralReal.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralSpecification
void visitLiteralSpecification([LiteralSpecification](../ext/magicdraw/classes/mdkernel/LiteralSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralSpecification`](../ext/magicdraw/classes/mdkernel/LiteralSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralString
void visitLiteralString([LiteralString](../ext/magicdraw/classes/mdkernel/LiteralString.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralString`](../ext/magicdraw/classes/mdkernel/LiteralString.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLiteralUnlimitedNatural
void visitLiteralUnlimitedNatural([LiteralUnlimitedNatural](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LiteralUnlimitedNatural`](../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitLoopNode
void visitLoopNode([LoopNode](../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`LoopNode`](../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitManifestation
void visitManifestation([Manifestation](../ext/magicdraw/deployments/mdartifacts/Manifestation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Manifestation`](../ext/magicdraw/deployments/mdartifacts/Manifestation.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitMergeNode
void visitMergeNode([MergeNode](../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`MergeNode`](../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitMessage
void visitMessage([Message](../ext/magicdraw/interactions/mdbasicinteractions/Message.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Message`](../ext/magicdraw/interactions/mdbasicinteractions/Message.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitMessageEnd
void visitMessageEnd([MessageEnd](../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`MessageEnd`](../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitMessageEvent
void visitMessageEvent([MessageEvent](../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`MessageEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitMessageOccurrenceSpecification
void visitMessageOccurrenceSpecification([MessageOccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`MessageOccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitModel
void visitModel([Model](../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Model`](../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitMultiplicityElement
void visitMultiplicityElement([MultiplicityElement](../ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`MultiplicityElement`](../ext/magicdraw/classes/mdkernel/MultiplicityElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitNamedElement
void visitNamedElement([NamedElement](../ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`NamedElement`](../ext/magicdraw/classes/mdkernel/NamedElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitNamespace
void visitNamespace([Namespace](../ext/magicdraw/classes/mdkernel/Namespace.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Namespace`](../ext/magicdraw/classes/mdkernel/Namespace.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitNode
void visitNode([Node](../ext/magicdraw/deployments/mdnodes/Node.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Node`](../ext/magicdraw/deployments/mdnodes/Node.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitObjectFlow
void visitObjectFlow([ObjectFlow](../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ObjectFlow`](../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitObjectNode
void visitObjectNode([ObjectNode](../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ObjectNode`](../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitObservation
void visitObservation([Observation](../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Observation`](../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOccurrenceSpecification
void visitOccurrenceSpecification([OccurrenceSpecification](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`OccurrenceSpecification`](../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOpaqueAction
void visitOpaqueAction([OpaqueAction](../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`OpaqueAction`](../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOpaqueBehavior
void visitOpaqueBehavior([OpaqueBehavior](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`OpaqueBehavior`](../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOpaqueExpression
void visitOpaqueExpression([OpaqueExpression](../ext/magicdraw/classes/mdkernel/OpaqueExpression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`OpaqueExpression`](../ext/magicdraw/classes/mdkernel/OpaqueExpression.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOperation
void visitOperation([Operation](../ext/magicdraw/classes/mdkernel/Operation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Operation`](../ext/magicdraw/classes/mdkernel/Operation.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOperationTemplateParameter
void visitOperationTemplateParameter([OperationTemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`OperationTemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitOutputPin
void visitOutputPin([OutputPin](../ext/magicdraw/actions/mdbasicactions/OutputPin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`OutputPin`](../ext/magicdraw/actions/mdbasicactions/OutputPin.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPackage
void visitPackage([Package](../ext/magicdraw/classes/mdkernel/Package.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Package`](../ext/magicdraw/classes/mdkernel/Package.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPackageImport
void visitPackageImport([PackageImport](../ext/magicdraw/classes/mdkernel/PackageImport.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`PackageImport`](../ext/magicdraw/classes/mdkernel/PackageImport.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPackageMerge
void visitPackageMerge([PackageMerge](../ext/magicdraw/classes/mdkernel/PackageMerge.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`PackageMerge`](../ext/magicdraw/classes/mdkernel/PackageMerge.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPackageableElement
void visitPackageableElement([PackageableElement](../ext/magicdraw/classes/mdkernel/PackageableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`PackageableElement`](../ext/magicdraw/classes/mdkernel/PackageableElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitParameter
void visitParameter([Parameter](../ext/magicdraw/classes/mdkernel/Parameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Parameter`](../ext/magicdraw/classes/mdkernel/Parameter.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitParameterSet
void visitParameterSet([ParameterSet](../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ParameterSet`](../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitParameterableElement
void visitParameterableElement([ParameterableElement](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ParameterableElement`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPartDecomposition
void visitPartDecomposition([PartDecomposition](../ext/magicdraw/interactions/mdfragments/PartDecomposition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`PartDecomposition`](../ext/magicdraw/interactions/mdfragments/PartDecomposition.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPin
void visitPin([Pin](../ext/magicdraw/actions/mdbasicactions/Pin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Pin`](../ext/magicdraw/actions/mdbasicactions/Pin.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPort
void visitPort([Port](../ext/magicdraw/compositestructures/mdports/Port.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Port`](../ext/magicdraw/compositestructures/mdports/Port.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPrimitiveType
void visitPrimitiveType([PrimitiveType](../ext/magicdraw/classes/mdkernel/PrimitiveType.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`PrimitiveType`](../ext/magicdraw/classes/mdkernel/PrimitiveType.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitProfile
void visitProfile([Profile](../ext/magicdraw/mdprofiles/Profile.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Profile`](../ext/magicdraw/mdprofiles/Profile.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitProfileApplication
void visitProfileApplication([ProfileApplication](../ext/magicdraw/mdprofiles/ProfileApplication.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ProfileApplication`](../ext/magicdraw/mdprofiles/ProfileApplication.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitProperty
void visitProperty([Property](../ext/magicdraw/classes/mdkernel/Property.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Property`](../ext/magicdraw/classes/mdkernel/Property.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitProtocolConformance
void visitProtocolConformance([ProtocolConformance](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ProtocolConformance`](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitProtocolStateMachine
void visitProtocolStateMachine([ProtocolStateMachine](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ProtocolStateMachine`](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitProtocolTransition
void visitProtocolTransition([ProtocolTransition](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ProtocolTransition`](../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitPseudostate
void visitPseudostate([Pseudostate](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Pseudostate`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitQualifierValue
void visitQualifierValue([QualifierValue](../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`QualifierValue`](../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRaiseExceptionAction
void visitRaiseExceptionAction([RaiseExceptionAction](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`RaiseExceptionAction`](../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadExtentAction
void visitReadExtentAction([ReadExtentAction](../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadExtentAction`](../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadIsClassifiedObjectAction
void visitReadIsClassifiedObjectAction([ReadIsClassifiedObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadIsClassifiedObjectAction`](../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadLinkAction
void visitReadLinkAction([ReadLinkAction](../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadLinkAction`](../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadLinkObjectEndAction
void visitReadLinkObjectEndAction([ReadLinkObjectEndAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadLinkObjectEndAction`](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadLinkObjectEndQualifierAction
void visitReadLinkObjectEndQualifierAction([ReadLinkObjectEndQualifierAction](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadLinkObjectEndQualifierAction`](../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadSelfAction
void visitReadSelfAction([ReadSelfAction](../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadSelfAction`](../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadStructuralFeatureAction
void visitReadStructuralFeatureAction([ReadStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadStructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReadVariableAction
void visitReadVariableAction([ReadVariableAction](../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReadVariableAction`](../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRealization
void visitRealization([Realization](../ext/magicdraw/classes/mddependencies/Realization.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Realization`](../ext/magicdraw/classes/mddependencies/Realization.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReception
void visitReception([Reception](../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Reception`](../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReclassifyObjectAction
void visitReclassifyObjectAction([ReclassifyObjectAction](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReclassifyObjectAction`](../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRedefinableElement
void visitRedefinableElement([RedefinableElement](../ext/magicdraw/classes/mdkernel/RedefinableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`RedefinableElement`](../ext/magicdraw/classes/mdkernel/RedefinableElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRedefinableTemplateSignature
void visitRedefinableTemplateSignature([RedefinableTemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`RedefinableTemplateSignature`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReduceAction
void visitReduceAction([ReduceAction](../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReduceAction`](../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRegion
void visitRegion([Region](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Region`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRelationship
void visitRelationship([Relationship](../ext/magicdraw/classes/mdkernel/Relationship.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Relationship`](../ext/magicdraw/classes/mdkernel/Relationship.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRemoveStructuralFeatureValueAction
void visitRemoveStructuralFeatureValueAction([RemoveStructuralFeatureValueAction](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`RemoveStructuralFeatureValueAction`](../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRemoveVariableValueAction
void visitRemoveVariableValueAction([RemoveVariableValueAction](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`RemoveVariableValueAction`](../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitReplyAction
void visitReplyAction([ReplyAction](../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ReplyAction`](../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSendObjectAction
void visitSendObjectAction([SendObjectAction](../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`SendObjectAction`](../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSendSignalAction
void visitSendSignalAction([SendSignalAction](../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`SendSignalAction`](../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSequenceNode
void visitSequenceNode([SequenceNode](../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`SequenceNode`](../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSignal
void visitSignal([Signal](../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Signal`](../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSignalEvent
void visitSignalEvent([SignalEvent](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`SignalEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSlot
void visitSlot([Slot](../ext/magicdraw/classes/mdkernel/Slot.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Slot`](../ext/magicdraw/classes/mdkernel/Slot.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStartClassifierBehaviorAction
void visitStartClassifierBehaviorAction([StartClassifierBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StartClassifierBehaviorAction`](../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStartObjectBehaviorAction
void visitStartObjectBehaviorAction([StartObjectBehaviorAction](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StartObjectBehaviorAction`](../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitState
void visitState([State](../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`State`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStateInvariant
void visitStateInvariant([StateInvariant](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StateInvariant`](../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStateMachine
void visitStateMachine([StateMachine](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StateMachine`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStereotype
void visitStereotype([Stereotype](../ext/magicdraw/mdprofiles/Stereotype.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Stereotype`](../ext/magicdraw/mdprofiles/Stereotype.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStringExpression
void visitStringExpression([StringExpression](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StringExpression`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStructuralFeature
void visitStructuralFeature([StructuralFeature](../ext/magicdraw/classes/mdkernel/StructuralFeature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StructuralFeature`](../ext/magicdraw/classes/mdkernel/StructuralFeature.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStructuralFeatureAction
void visitStructuralFeatureAction([StructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStructuredActivityNode
void visitStructuredActivityNode([StructuredActivityNode](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StructuredActivityNode`](../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStructuredClassifier
void visitStructuredClassifier([StructuredClassifier](../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StructuredClassifier`](../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitSubstitution
void visitSubstitution([Substitution](../ext/magicdraw/classes/mddependencies/Substitution.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Substitution`](../ext/magicdraw/classes/mddependencies/Substitution.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTemplateBinding
void visitTemplateBinding([TemplateBinding](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TemplateBinding`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTemplateParameter
void visitTemplateParameter([TemplateParameter](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TemplateParameter`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTemplateParameterSubstitution
void visitTemplateParameterSubstitution([TemplateParameterSubstitution](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TemplateParameterSubstitution`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTemplateSignature
void visitTemplateSignature([TemplateSignature](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TemplateSignature`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTemplateableElement
void visitTemplateableElement([TemplateableElement](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TemplateableElement`](../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTestIdentityAction
void visitTestIdentityAction([TestIdentityAction](../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TestIdentityAction`](../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTimeConstraint
void visitTimeConstraint([TimeConstraint](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TimeConstraint`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTimeEvent
void visitTimeEvent([TimeEvent](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TimeEvent`](../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTimeExpression
void visitTimeExpression([TimeExpression](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TimeExpression`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTimeInterval
void visitTimeInterval([TimeInterval](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TimeInterval`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTimeObservation
void visitTimeObservation([TimeObservation](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TimeObservation`](../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTransition
void visitTransition([Transition](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Transition`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTrigger
void visitTrigger([Trigger](../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Trigger`](../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitType
void visitType([Type](../ext/magicdraw/classes/mdkernel/Type.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Type`](../ext/magicdraw/classes/mdkernel/Type.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTypedElement
void visitTypedElement([TypedElement](../ext/magicdraw/classes/mdkernel/TypedElement.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TypedElement`](../ext/magicdraw/classes/mdkernel/TypedElement.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitUnmarshallAction
void visitUnmarshallAction([UnmarshallAction](../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`UnmarshallAction`](../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitUsage
void visitUsage([Usage](../ext/magicdraw/classes/mddependencies/Usage.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Usage`](../ext/magicdraw/classes/mddependencies/Usage.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitUseCase
void visitUseCase([UseCase](../ext/magicdraw/mdusecases/UseCase.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`UseCase`](../ext/magicdraw/mdusecases/UseCase.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitValuePin
void visitValuePin([ValuePin](../ext/magicdraw/actions/mdbasicactions/ValuePin.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ValuePin`](../ext/magicdraw/actions/mdbasicactions/ValuePin.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitValueSpecification
void visitValueSpecification([ValueSpecification](../ext/magicdraw/classes/mdkernel/ValueSpecification.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ValueSpecification`](../ext/magicdraw/classes/mdkernel/ValueSpecification.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitValueSpecificationAction
void visitValueSpecificationAction([ValueSpecificationAction](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ValueSpecificationAction`](../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitVariable
void visitVariable([Variable](../ext/magicdraw/activities/mdstructuredactivities/Variable.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Variable`](../ext/magicdraw/activities/mdstructuredactivities/Variable.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitVariableAction
void visitVariableAction([VariableAction](../ext/magicdraw/actions/mdstructuredactions/VariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`VariableAction`](../ext/magicdraw/actions/mdstructuredactions/VariableAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitVertex
void visitVertex([Vertex](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`Vertex`](../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitWriteLinkAction
void visitWriteLinkAction([WriteLinkAction](../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`WriteLinkAction`](../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitWriteStructuralFeatureAction
void visitWriteStructuralFeatureAction([WriteStructuralFeatureAction](../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`WriteStructuralFeatureAction`](../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitWriteVariableAction
void visitWriteVariableAction([WriteVariableAction](../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`WriteVariableAction`](../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitTaggedValue
void visitTaggedValue([TaggedValue](../ext/magicdraw/classes/mdkernel/TaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`TaggedValue`](../ext/magicdraw/classes/mdkernel/TaggedValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitStringTaggedValue
void visitStringTaggedValue([StringTaggedValue](../ext/magicdraw/classes/mdkernel/StringTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`StringTaggedValue`](../ext/magicdraw/classes/mdkernel/StringTaggedValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitBooleanTaggedValue
void visitBooleanTaggedValue([BooleanTaggedValue](../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`BooleanTaggedValue`](../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitElementTaggedValue
void visitElementTaggedValue([ElementTaggedValue](../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`ElementTaggedValue`](../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitRealTaggedValue
void visitRealTaggedValue([RealTaggedValue](../ext/magicdraw/classes/mdkernel/RealTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`RealTaggedValue`](../ext/magicdraw/classes/mdkernel/RealTaggedValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.
visitIntegerTaggedValue
void visitIntegerTaggedValue([IntegerTaggedValue](../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html) element,
 [VisitorContext](../ext/jmi/reflect/VisitorContext.html) context)
Visitor method for [`IntegerTaggedValue`](../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html).
Parameters:
`element` - that should be visited.
`context` - visitor's context.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.impl</a></div>
<h1 class="title" title="Interface ModelVisitor">Interface ModelVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../magicdraw/uml/InheritanceVisitor.html" title="class in com.nomagic.magicdraw.uml">InheritanceVisitor</a></code>, <code><a href="ModelHierarchyVisitor.html" title="class in com.nomagic.uml2.impl">ModelHierarchyVisitor</a></code>, <code><a href="ModelVisitorAdapter.html" title="class in com.nomagic.uml2.impl">ModelVisitorAdapter</a></code>, <code><a href="../../magicdraw/uml/Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelVisitor</span><span class="extends-implements">
extends <a href="../../magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAbstraction(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAbstraction</a><wbr/>(<a href="../ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Abstraction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAcceptCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAcceptCallAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptCallAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAcceptEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAcceptEventAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptEventAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Action</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActionExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ActionExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActionExecutionSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ActionExecutionSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActionInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActionInputPin</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ActionInputPin</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivity</a><wbr/>(<a href="../ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>Activity</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivityEdge(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityEdge</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivityFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityFinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityFinalNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityFinalNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivityGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityGroup</a><wbr/>(<a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivityParameterNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityParameterNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActivityPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActivityPartition</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitActor(com.nomagic.uml2.ext.magicdraw.mdusecases.Actor,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitActor</a><wbr/>(<a href="../ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Actor</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAddStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAddStructuralFeatureValueAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>AddStructuralFeatureValueAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAddVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAddVariableValueAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>AddVariableValueAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAnyReceiveEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.AnyReceiveEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAnyReceiveEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>AnyReceiveEvent</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitArtifact</a><wbr/>(<a href="../ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Artifact</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAssociation</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAssociationClass(com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses.AssociationClass,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitAssociationClass</a><wbr/>(<a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code>AssociationClass</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehavior</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBehavioralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehavioralFeature</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BehavioralFeature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBehavioredClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehavioredClassifier</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>BehavioredClassifier</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBehaviorExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.BehaviorExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBehaviorExecutionSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>BehaviorExecutionSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBooleanTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BooleanTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBooleanTaggedValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BooleanTaggedValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBroadcastSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.BroadcastSignalAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitBroadcastSignalAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>BroadcastSignalAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCallBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallBehaviorAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCallEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>CallEvent</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCallOperationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCallOperationAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallOperationAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCentralBufferNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.CentralBufferNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCentralBufferNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>CentralBufferNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitChangeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitChangeEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>ChangeEvent</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClass</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClassifier</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClassifierTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClassifierTemplateParameter</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ClassifierTemplateParameter</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClause</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClearAssociationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClearAssociationAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearAssociationAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClearStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClearStructuralFeatureAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearStructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClearVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ClearVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitClearVariableAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ClearVariableAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCollaboration(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.Collaboration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCollaboration</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>Collaboration</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCollaborationUse(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCollaborationUse</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>CollaborationUse</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCombinedFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCombinedFragment</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitComment</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCommunicationPath(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.CommunicationPath,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCommunicationPath</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>CommunicationPath</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitComponent(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitComponent</a><wbr/>(<a href="../ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>Component</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitComponentRealization(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.ComponentRealization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitComponentRealization</a><wbr/>(<a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConditionalNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConditionalNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ConditionalNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectableElement(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectableElement</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectableElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectableElementTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectableElementTemplateParameter</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ConnectableElementTemplateParameter</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectionPointReference(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.ConnectionPointReference,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectionPointReference</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>ConnectionPointReference</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnector</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnectorEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConnectorEnd</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConsiderIgnoreFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.ConsiderIgnoreFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConsiderIgnoreFragment</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>ConsiderIgnoreFragment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitConstraint</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitContinuation(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Continuation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitContinuation</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Continuation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitControlFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitControlFlow</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlFlow</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitControlNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitControlNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCreateLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCreateLinkAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateLinkAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCreateLinkObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCreateLinkObjectAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>CreateLinkObjectAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCreateObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitCreateObjectAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateObjectAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDataStoreNode(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.DataStoreNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDataStoreNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>DataStoreNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDataType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDataType</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DataType</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDecisionNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.DecisionNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDecisionNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>DecisionNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDependency(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDependency</a><wbr/>(<a href="../ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDeployedArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeployedArtifact</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeployedArtifact</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Deployment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeployment</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Deployment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDeploymentSpecification(com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments.DeploymentSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeploymentSpecification</a><wbr/>(<a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code>DeploymentSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDeploymentTarget(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDeploymentTarget</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeploymentTarget</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDestroyLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDestroyLinkAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyLinkAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDestroyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDestroyObjectAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyObjectAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.DestructionOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDestructionOccurrenceSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>DestructionOccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDevice(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Device,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDevice</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Device</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDiagram</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDirectedRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDirectedRelationship</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDuration</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Duration</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDurationConstraint</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationConstraint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDurationInterval</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationInterval</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDurationObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationObservation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitDurationObservation</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationObservation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElement</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitElementImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementImport,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElementImport</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitElementTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElementTaggedValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementTaggedValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitElementValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementValue</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEncapsulatedClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEncapsulatedClassifier</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>EncapsulatedClassifier</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEnumeration(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEnumeration</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Enumeration</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEnumerationLiteral</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExceptionHandler(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExceptionHandler,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExceptionHandler</a><wbr/>(<a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutableNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExecutionEnvironment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.ExecutionEnvironment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutionEnvironment</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>ExecutionEnvironment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExecutionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutionOccurrenceSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionOccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExecutionSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExpansionNode(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExpansionNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExpansionRegion(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionRegion,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExpansionRegion</a><wbr/>(<a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionRegion</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExpression</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Expression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExtend(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtend</a><wbr/>(<a href="../ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Extend</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtension</a><wbr/>(<a href="../ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Extension</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.ExtensionEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtensionEnd</a><wbr/>(<a href="../ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ExtensionEnd</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExtensionPoint(com.nomagic.uml2.ext.magicdraw.mdusecases.ExtensionPoint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitExtensionPoint</a><wbr/>(<a href="../ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>ExtensionPoint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFeature</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Feature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFinalNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FinalNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFinalState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.FinalState,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFinalState</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>FinalState</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFlowFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FlowFinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFlowFinalNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FlowFinalNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitForkNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ForkNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitForkNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ForkNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFunctionBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.FunctionBehavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitFunctionBehavior</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>FunctionBehavior</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGate</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Gate</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Generalization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGeneralization</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitGeneralizationSet(com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes.GeneralizationSet,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGeneralizationSet</a><wbr/>(<a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code>GeneralizationSet</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitGeneralOrdering(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.GeneralOrdering,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitGeneralOrdering</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>GeneralOrdering</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitImage(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitImage</a><wbr/>(<a href="../ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Image</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInclude(com.nomagic.uml2.ext.magicdraw.mdusecases.Include,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInclude</a><wbr/>(<a href="../ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Include</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInformationFlow(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInformationFlow</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInformationItem(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationItem,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInformationItem</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationItem</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInitialNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.InitialNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInitialNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>InitialNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInputPin</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInstanceSpecification</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInstanceValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInstanceValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceValue</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitIntegerTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.IntegerTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitIntegerTaggedValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>IntegerTaggedValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteraction</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Interaction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInteractionConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionConstraint</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionConstraint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInteractionFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionFragment</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInteractionOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionOperand</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInteractionUse(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInteractionUse</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterface</a><wbr/>(<a href="../ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInterfaceRealization(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.InterfaceRealization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterfaceRealization</a><wbr/>(<a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>InterfaceRealization</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInterruptibleActivityRegion(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterruptibleActivityRegion</a><wbr/>(<a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>InterruptibleActivityRegion</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInterval</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitIntervalConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitIntervalConstraint</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>IntervalConstraint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInvocationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitInvocationAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InvocationAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitJoinNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitJoinNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>JoinNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLifeline(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLifeline</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Lifeline</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLinkEndCreationData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkEndCreationData</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndCreationData</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLinkEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkEndData</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndData</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLinkEndDestructionData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLinkEndDestructionData</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndDestructionData</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralBoolean(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralBoolean,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralBoolean</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralBoolean</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralInteger(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralInteger,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralInteger</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralInteger</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralNull,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralNull</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralNull</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralReal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralReal,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralReal</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralReal</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralSpecification</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralString,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralString</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralString</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralUnlimitedNatural(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralUnlimitedNatural,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLiteralUnlimitedNatural</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralUnlimitedNatural</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLoopNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitLoopNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>LoopNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitManifestation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Manifestation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitManifestation</a><wbr/>(<a href="../ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Manifestation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMergeNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.MergeNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMergeNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>MergeNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessage</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMessageEnd(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessageEnd</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageEnd</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMessageEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.MessageEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessageEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>MessageEvent</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMessageOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMessageOccurrenceSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageOccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitModel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitModel</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code>Model</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMultiplicityElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitMultiplicityElement</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitNamedElement</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitNamespace</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Namespace</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNode(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Node,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitNode</a><wbr/>(<a href="../ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Node</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitObjectFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitObjectFlow</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitObjectNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitObjectNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Observation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitObservation</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Observation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.OccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOccurrenceSpecification</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>OccurrenceSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOpaqueAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOpaqueAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OpaqueAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOpaqueBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.OpaqueBehavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOpaqueBehavior</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>OpaqueBehavior</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOpaqueExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOpaqueExpression</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>OpaqueExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOperation</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOperationTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOperationTemplateParameter</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>OperationTemplateParameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOutputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitOutputPin</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackage</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Package</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPackageableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackageableElement</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPackageImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageImport,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackageImport</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPackageMerge(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageMerge,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPackageMerge</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageMerge</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitParameter</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitParameterableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitParameterableElement</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ParameterableElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitParameterSet(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitParameterSet</a><wbr/>(<a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPartDecomposition(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPartDecomposition</a><wbr/>(<a href="../ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>PartDecomposition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPin</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPort</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPrimitiveType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PrimitiveType,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPrimitiveType</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PrimitiveType</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProfile</a><wbr/>(<a href="../ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Profile</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitProfileApplication(com.nomagic.uml2.ext.magicdraw.mdprofiles.ProfileApplication,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProfileApplication</a><wbr/>(<a href="../ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ProfileApplication</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProperty</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitProtocolConformance(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolConformance,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProtocolConformance</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolConformance</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitProtocolStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProtocolStateMachine</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolStateMachine</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitProtocolTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitProtocolTransition</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPseudostate(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Pseudostate,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitPseudostate</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Pseudostate</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitQualifierValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitQualifierValue</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRaiseExceptionAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRaiseExceptionAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RaiseExceptionAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadExtentAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadExtentAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadExtentAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadIsClassifiedObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadIsClassifiedObjectAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadIsClassifiedObjectAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadLinkAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadLinkAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadLinkObjectEndAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadLinkObjectEndAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadLinkObjectEndQualifierAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndQualifierAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadSelfAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadSelfAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadSelfAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadStructuralFeatureAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadStructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReadVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReadVariableAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ReadVariableAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRealization(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Realization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRealization</a><wbr/>(<a href="../ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Realization</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRealTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RealTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRealTaggedValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RealTaggedValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReception(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReception</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReclassifyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReclassifyObjectAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRedefinableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRedefinableElement</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRedefinableTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRedefinableTemplateSignature</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>RedefinableTemplateSignature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReduceAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReduceAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReduceAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRegion</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRelationship</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRemoveStructuralFeatureValueAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>RemoveStructuralFeatureValueAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRemoveVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitRemoveVariableValueAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RemoveVariableValueAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReplyAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitReplyAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReplyAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSendObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSendObjectAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>SendObjectAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSendSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSendSignalAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>SendSignalAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSequenceNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSequenceNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>SequenceNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSignal</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Signal</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSignalEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.SignalEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSignalEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>SignalEvent</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSlot</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Slot</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStartClassifierBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStartClassifierBehaviorAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartClassifierBehaviorAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStartObjectBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStartObjectBehaviorAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartObjectBehaviorAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitState</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStateInvariant</a><wbr/>(<a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>StateInvariant</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStateMachine</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>StateMachine</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStereotype</a><wbr/>(<a href="../ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStringExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStringExpression</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>StringExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStringTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StringTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStringTaggedValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StringTaggedValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStructuralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuralFeature</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StructuralFeature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuralFeatureAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>StructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStructuredActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuredActivityNode</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>StructuredActivityNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStructuredClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitStructuredClassifier</a><wbr/>(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>StructuredClassifier</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSubstitution(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Substitution,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitSubstitution</a><wbr/>(<a href="../ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTaggedValue</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TaggedValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTemplateableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateableElement</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateableElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateBinding</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateParameter</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTemplateParameterSubstitution(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateParameterSubstitution</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTemplateSignature</a><wbr/>(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateSignature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTestIdentityAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTestIdentityAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>TestIdentityAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTimeConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeConstraint</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeConstraint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTimeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.TimeEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeEvent</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>TimeEvent</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeExpression</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeInterval</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeInterval</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTimeObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeObservation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTimeObservation</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeObservation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTransition</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTrigger(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTrigger</a><wbr/>(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitType</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTypedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitTypedElement</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUnmarshallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitUnmarshallAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>UnmarshallAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUsage(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Usage,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitUsage</a><wbr/>(<a href="../ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Usage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitUseCase</a><wbr/>(<a href="../ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitValuePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitValuePin</a><wbr/>(<a href="../ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>ValuePin</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitValueSpecification</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitValueSpecificationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitValueSpecificationAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ValueSpecificationAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Variable,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitVariable</a><wbr/>(<a href="../ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.VariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitVariableAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>VariableAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitVertex</a><wbr/>(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Vertex</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitWriteLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitWriteLinkAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteLinkAction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitWriteStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitWriteStructuralFeatureAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteStructuralFeatureAction</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitWriteVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">visitWriteVariableAction</a><wbr/>(<a href="../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>WriteVariableAction</code></a>.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="visitAbstraction(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAbstraction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAbstraction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Abstraction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAcceptCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAcceptCallAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAcceptCallAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptCallAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAcceptEventAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAcceptEventAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAcceptEventAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>AcceptEventAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Action</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ActionExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActionExecutionSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActionExecutionSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ActionExecutionSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActionInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActionInputPin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActionInputPin</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ActionInputPin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivity</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>Activity</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityEdge(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityEdge</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivityEdge</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityFinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityFinalNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivityFinalNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityFinalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityGroup</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivityGroup</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivityNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityParameterNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityParameterNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivityParameterNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActivityPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActivityPartition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActivityPartition</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitActor(com.nomagic.uml2.ext.magicdraw.mdusecases.Actor,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitActor</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitActor</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Actor</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAddStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAddStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAddStructuralFeatureValueAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>AddStructuralFeatureValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAddVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAddVariableValueAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAddVariableValueAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>AddVariableValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnyReceiveEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.AnyReceiveEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAnyReceiveEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAnyReceiveEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>AnyReceiveEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitArtifact</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitArtifact</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Artifact</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAssociation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAssociation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationClass(com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses.AssociationClass,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitAssociationClass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAssociationClass</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses"><code>AssociationClass</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBehavior</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehaviorExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.BehaviorExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehaviorExecutionSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBehaviorExecutionSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>BehaviorExecutionSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavioralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehavioralFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBehavioralFeature</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BehavioralFeature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavioredClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBehavioredClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBehavioredClassifier</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>BehavioredClassifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBroadcastSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.BroadcastSignalAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBroadcastSignalAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBroadcastSignalAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>BroadcastSignalAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCallAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallBehaviorAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCallBehaviorAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCallEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>CallEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCallOperationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCallOperationAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCallOperationAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallOperationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCentralBufferNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.CentralBufferNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCentralBufferNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCentralBufferNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>CentralBufferNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitChangeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitChangeEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitChangeEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>ChangeEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClass</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClassifier</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifierTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClassifierTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClassifierTemplateParameter</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ClassifierTemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClause</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClause</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClearAssociationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClearAssociationAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClearAssociationAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearAssociationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClearStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClearStructuralFeatureAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClearStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearStructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClearVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ClearVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitClearVariableAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClearVariableAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ClearVariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaboration(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.Collaboration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCollaboration</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCollaboration</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>Collaboration</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollaborationUse(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCollaborationUse</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCollaborationUse</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>CollaborationUse</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCombinedFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCombinedFragment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCombinedFragment</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitComment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitComment</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCommunicationPath(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.CommunicationPath,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCommunicationPath</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCommunicationPath</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>CommunicationPath</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComponent(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitComponent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitComponent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>Component</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComponentRealization(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.ComponentRealization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitComponentRealization</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitComponentRealization</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConditionalNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConditionalNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConditionalNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ConditionalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectableElement(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectableElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectableElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectableElementTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectableElementTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectableElementTemplateParameter</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ConnectableElementTemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectionPointReference(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.ConnectionPointReference,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectionPointReference</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectionPointReference</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>ConnectionPointReference</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnector</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnectorEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConnectorEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnectorEnd</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConsiderIgnoreFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.ConsiderIgnoreFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConsiderIgnoreFragment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConsiderIgnoreFragment</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>ConsiderIgnoreFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitConstraint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConstraint</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitContinuation(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Continuation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitContinuation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitContinuation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Continuation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitControlFlow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitControlFlow</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitControlNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ControlNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitControlNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitControlNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ControlNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCreateLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCreateLinkAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCreateLinkAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCreateLinkObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCreateLinkObjectAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCreateLinkObjectAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>CreateLinkObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCreateObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitCreateObjectAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCreateObjectAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataStoreNode(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.DataStoreNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDataStoreNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDataStoreNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>DataStoreNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDataType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDataType</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DataType</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDecisionNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.DecisionNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDecisionNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDecisionNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>DecisionNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDependency(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDependency</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDependency</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeployedArtifact(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeployedArtifact</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDeployedArtifact</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeployedArtifact</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Deployment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeployment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDeployment</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Deployment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeploymentSpecification(com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments.DeploymentSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeploymentSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDeploymentSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments"><code>DeploymentSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDeploymentTarget(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDeploymentTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDeploymentTarget</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>DeploymentTarget</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDestroyLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDestroyLinkAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDestroyLinkAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDestroyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDestroyObjectAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDestroyObjectAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>DestroyObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.DestructionOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDestructionOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDestructionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>DestructionOccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDevice(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Device,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDevice</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDevice</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Device</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDiagram</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDiagram</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDirectedRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDirectedRelationship</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDirectedRelationship</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDuration</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDuration</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Duration</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDurationConstraint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDurationConstraint</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDurationInterval</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDurationInterval</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationInterval</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDurationObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationObservation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitDurationObservation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDurationObservation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationObservation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementImport,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElementImport</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitElementImport</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElementValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitElementValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEncapsulatedClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEncapsulatedClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEncapsulatedClassifier</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>EncapsulatedClassifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumeration(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEnumeration</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEnumeration</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Enumeration</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEnumerationLiteral(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEnumerationLiteral</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEnumerationLiteral</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExceptionHandler(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExceptionHandler,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExceptionHandler</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExceptionHandler</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutableNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExecutableNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutionEnvironment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.ExecutionEnvironment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutionEnvironment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExecutionEnvironment</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>ExecutionEnvironment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutionOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExecutionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionOccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExecutionSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.ExecutionSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExecutionSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExecutionSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ExecutionSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpansionNode(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExpansionNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExpansionNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpansionRegion(com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities.ExpansionRegion,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExpansionRegion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExpansionRegion</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExpansionRegion</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExpression</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Expression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtend(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtend</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExtend</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Extend</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtension</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExtension</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Extension</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.ExtensionEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtensionEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExtensionEnd</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ExtensionEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExtensionPoint(com.nomagic.uml2.ext.magicdraw.mdusecases.ExtensionPoint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitExtensionPoint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExtensionPoint</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>ExtensionPoint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeature</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Feature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFinalNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFinalNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FinalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFinalState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.FinalState,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFinalState</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFinalState</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>FinalState</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowFinalNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.FlowFinalNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFlowFinalNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFlowFinalNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>FlowFinalNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitForkNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ForkNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitForkNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitForkNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ForkNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFunctionBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.FunctionBehavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitFunctionBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFunctionBehavior</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>FunctionBehavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitGate</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Gate</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralOrdering(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.GeneralOrdering,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGeneralOrdering</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitGeneralOrdering</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>GeneralOrdering</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Generalization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGeneralization</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitGeneralization</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitGeneralizationSet(com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes.GeneralizationSet,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitGeneralizationSet</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitGeneralizationSet</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code>GeneralizationSet</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImage(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitImage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitImage</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Image</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInclude(com.nomagic.uml2.ext.magicdraw.mdusecases.Include,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInclude</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInclude</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Include</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationFlow(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInformationFlow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInformationFlow</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInformationItem(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows.InformationItem,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInformationItem</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInformationItem</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationItem</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInitialNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.InitialNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInitialNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInitialNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>InitialNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInputPin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInputPin</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInstanceSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInstanceSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstanceValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInstanceValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInstanceValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteraction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInteraction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Interaction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionConstraint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInteractionConstraint</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionFragment(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionFragment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInteractionFragment</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionOperand</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInteractionOperand</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteractionUse(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInteractionUse</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInteractionUse</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterface</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInterface</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterfaceRealization(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.InterfaceRealization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterfaceRealization</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInterfaceRealization</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>InterfaceRealization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterruptibleActivityRegion(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterruptibleActivityRegion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInterruptibleActivityRegion</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>InterruptibleActivityRegion</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInterval</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInterval</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIntervalConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitIntervalConstraint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitIntervalConstraint</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>IntervalConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInvocationAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitInvocationAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInvocationAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InvocationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitJoinNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitJoinNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitJoinNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>JoinNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLifeline(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLifeline</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLifeline</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Lifeline</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLinkAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndCreationData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkEndCreationData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLinkEndCreationData</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndCreationData</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkEndData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLinkEndData</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndData</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLinkEndDestructionData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLinkEndDestructionData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLinkEndDestructionData</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndDestructionData</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralBoolean(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralBoolean,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralBoolean</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralBoolean</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralBoolean</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralInteger(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralInteger,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralInteger</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralInteger</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralInteger</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralNull,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralNull</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralNull</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralNull</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralReal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralReal,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralReal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralReal</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralReal</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralString,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralString</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralString</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralString</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralUnlimitedNatural(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.LiteralUnlimitedNatural,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLiteralUnlimitedNatural</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralUnlimitedNatural</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>LiteralUnlimitedNatural</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLoopNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitLoopNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLoopNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>LoopNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitManifestation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Manifestation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitManifestation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitManifestation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts"><code>Manifestation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMergeNode(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.MergeNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMergeNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMergeNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>MergeNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMessage</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageEnd(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessageEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMessageEnd</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.MessageEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessageEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMessageEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>MessageEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMessageOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageOccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMessageOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMessageOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageOccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitModel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitModel</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitModel</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels"><code>Model</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMultiplicityElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitMultiplicityElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMultiplicityElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitNamedElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNamedElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNamespace</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Namespace</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNode(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.Node,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes"><code>Node</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectFlow(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectFlow,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitObjectFlow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitObjectFlow</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObjectNode(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitObjectNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitObjectNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Observation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitObservation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitObservation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Observation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.OccurrenceSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOccurrenceSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>OccurrenceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOpaqueAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOpaqueAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OpaqueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.OpaqueBehavior,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOpaqueBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOpaqueBehavior</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>OpaqueBehavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOpaqueExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOpaqueExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOpaqueExpression</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>OpaqueExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOperation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOperation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperationTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOperationTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOperationTemplateParameter</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>OperationTemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOutputPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitOutputPin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOutputPin</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPackage</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Package</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageImport(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageImport,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackageImport</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPackageImport</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageMerge(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageMerge,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackageMerge</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPackageMerge</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageMerge</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackageableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPackageableElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPackageableElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitParameter</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameterSet(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitParameterSet</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitParameterSet</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameterableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitParameterableElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitParameterableElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ParameterableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPartDecomposition(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPartDecomposition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPartDecomposition</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>PartDecomposition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPin</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPort</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPort</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPrimitiveType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PrimitiveType,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPrimitiveType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPrimitiveType</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PrimitiveType</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProfile</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitProfile</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Profile</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProfileApplication(com.nomagic.uml2.ext.magicdraw.mdprofiles.ProfileApplication,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProfileApplication</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitProfileApplication</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ProfileApplication</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProperty</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitProperty</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProtocolConformance(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolConformance,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProtocolConformance</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitProtocolConformance</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolConformance</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProtocolStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProtocolStateMachine</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitProtocolStateMachine</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolStateMachine</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitProtocolTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitProtocolTransition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitProtocolTransition</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPseudostate(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Pseudostate,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitPseudostate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPseudostate</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Pseudostate</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitQualifierValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitQualifierValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitQualifierValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRaiseExceptionAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRaiseExceptionAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRaiseExceptionAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RaiseExceptionAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadExtentAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadExtentAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadExtentAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadExtentAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadIsClassifiedObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadIsClassifiedObjectAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadIsClassifiedObjectAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadIsClassifiedObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadLinkAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadLinkAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadLinkObjectEndAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadLinkObjectEndAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadLinkObjectEndAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadLinkObjectEndQualifierAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadLinkObjectEndQualifierAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadLinkObjectEndQualifierAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndQualifierAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadSelfAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadSelfAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadSelfAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadSelfAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadStructuralFeatureAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ReadStructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReadVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReadVariableAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReadVariableAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>ReadVariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRealization(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Realization,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRealization</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRealization</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Realization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReception(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReception</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReception</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReclassifyObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReclassifyObjectAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReclassifyObjectAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRedefinableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRedefinableElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRedefinableElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRedefinableTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRedefinableTemplateSignature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRedefinableTemplateSignature</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>RedefinableTemplateSignature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReduceAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReduceAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReduceAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReduceAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRegion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRegion</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRelationship</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRelationship</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRemoveStructuralFeatureValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRemoveStructuralFeatureValueAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRemoveStructuralFeatureValueAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>RemoveStructuralFeatureValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRemoveVariableValueAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRemoveVariableValueAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRemoveVariableValueAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>RemoveVariableValueAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReplyAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitReplyAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReplyAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReplyAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSendObjectAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSendObjectAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSendObjectAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>SendObjectAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSendSignalAction(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSendSignalAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSendSignalAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>SendSignalAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSequenceNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSequenceNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSequenceNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>SequenceNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSignal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSignal</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Signal</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSignalEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.SignalEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSignalEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSignalEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>SignalEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSlot</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSlot</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Slot</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStartClassifierBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStartClassifierBehaviorAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStartClassifierBehaviorAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartClassifierBehaviorAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStartObjectBehaviorAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStartObjectBehaviorAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStartObjectBehaviorAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>StartObjectBehaviorAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitState</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitState</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStateInvariant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStateInvariant</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>StateInvariant</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStateMachine</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStateMachine</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>StateMachine</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStereotype</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStereotype</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStringExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStringExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStringExpression</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>StringExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuralFeature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuralFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStructuralFeature</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StructuralFeature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuralFeatureAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>StructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuredActivityNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuredActivityNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStructuredActivityNode</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>StructuredActivityNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructuredClassifier(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStructuredClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStructuredClassifier</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>StructuredClassifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubstitution(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Substitution,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitSubstitution</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSubstitution</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateBinding</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTemplateBinding</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTemplateParameter</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateParameterSubstitution(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateParameterSubstitution</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTemplateParameterSubstitution</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateSignature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTemplateSignature</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateSignature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTemplateableElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTemplateableElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTemplateableElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateableElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTestIdentityAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTestIdentityAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTestIdentityAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>TestIdentityAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeConstraint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTimeConstraint</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeConstraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.TimeEvent,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTimeEvent</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>TimeEvent</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTimeExpression</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeInterval</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTimeInterval</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeInterval</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTimeObservation(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeObservation,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTimeObservation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTimeObservation</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeObservation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTransition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTransition</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTrigger(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTrigger</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTrigger</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitType</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTypedElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTypedElement</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUnmarshallAction(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitUnmarshallAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUnmarshallAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>UnmarshallAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUsage(com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Usage,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitUsage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUsage</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Usage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitUseCase</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUseCase</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitValuePin(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitValuePin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitValuePin</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>ValuePin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitValueSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitValueSpecification</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitValueSpecificationAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitValueSpecificationAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitValueSpecificationAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ValueSpecificationAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Variable,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitVariable</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitVariable</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.VariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitVariableAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitVariableAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>VariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitVertex</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitVertex</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Vertex</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWriteLinkAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteLinkAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitWriteLinkAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitWriteLinkAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteLinkAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWriteStructuralFeatureAction(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitWriteStructuralFeatureAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitWriteStructuralFeatureAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>WriteStructuralFeatureAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitWriteVariableAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitWriteVariableAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitWriteVariableAction</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions"><code>WriteVariableAction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitTaggedValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTaggedValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TaggedValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStringTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StringTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitStringTaggedValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStringTaggedValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>StringTaggedValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBooleanTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BooleanTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitBooleanTaggedValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBooleanTaggedValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>BooleanTaggedValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ElementTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitElementTaggedValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitElementTaggedValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementTaggedValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRealTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RealTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitRealTaggedValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRealTaggedValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RealTaggedValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIntegerTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.IntegerTaggedValue,com.nomagic.uml2.ext.jmi.reflect.VisitorContext)">
<h3>visitIntegerTaggedValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitIntegerTaggedValue</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a> element,
 <a href="../ext/jmi/reflect/VisitorContext.html" title="class in com.nomagic.uml2.ext.jmi.reflect">VisitorContext</a> context)</span></div>
<div class="block">Visitor method for <a href="../ext/magicdraw/classes/mdkernel/IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>IntegerTaggedValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - that should be visited.</dd>
<dd><code>context</code> - visitor's context.</dd>
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
