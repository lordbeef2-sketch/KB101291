# JAVA OPENAPI: Element (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Element.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Element.html`
- source_sha256: `62b069cf739439e983b98f25a42d95e70f52757fe8e721102c1e5058913b7d3f`
- captured_utc: `2026-07-14T16:58:52.773457+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Element

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[Abstraction](../mddependencies/Abstraction.html)`, `[AcceptCallAction](../../actions/mdcompleteactions/AcceptCallAction.html)`, `[AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html)`, `[Action](../../actions/mdbasicactions/Action.html)`, `[ActionExecutionSpecification](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html)`, `[ActionInputPin](../../actions/mdstructuredactions/ActionInputPin.html)`, `[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html)`, `[ActivityFinalNode](../../activities/mdbasicactivities/ActivityFinalNode.html)`, `[ActivityGroup](../../activities/mdfundamentalactivities/ActivityGroup.html)`, `[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[ActivityParameterNode](../../activities/mdbasicactivities/ActivityParameterNode.html)`, `[ActivityPartition](../../activities/mdintermediateactivities/ActivityPartition.html)`, `[Actor](../../mdusecases/Actor.html)`, `[AddStructuralFeatureValueAction](../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`, `[AddVariableValueAction](../../actions/mdstructuredactions/AddVariableValueAction.html)`, `[AnyReceiveEvent](../../commonbehaviors/mdcommunications/AnyReceiveEvent.html)`, `[Artifact](../../deployments/mdartifacts/Artifact.html)`, `[Association](Association.html)`, `[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioralFeature](BehavioralFeature.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[BehaviorExecutionSpecification](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)`, `[BooleanTaggedValue](BooleanTaggedValue.html)`, `[BroadcastSignalAction](../../actions/mdintermediateactions/BroadcastSignalAction.html)`, `[CallAction](../../actions/mdbasicactions/CallAction.html)`, `[CallBehaviorAction](../../actions/mdbasicactions/CallBehaviorAction.html)`, `[CallEvent](../../commonbehaviors/mdcommunications/CallEvent.html)`, `[CallOperationAction](../../actions/mdbasicactions/CallOperationAction.html)`, `[CentralBufferNode](../../activities/mdintermediateactivities/CentralBufferNode.html)`, `[ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)`, `[Clause](../../activities/mdstructuredactivities/Clause.html)`, `[ClearAssociationAction](../../actions/mdintermediateactions/ClearAssociationAction.html)`, `[ClearStructuralFeatureAction](../../actions/mdintermediateactions/ClearStructuralFeatureAction.html)`, `[ClearVariableAction](../../actions/mdstructuredactions/ClearVariableAction.html)`, `[Collaboration](../../compositestructures/mdcollaborations/Collaboration.html)`, `[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html)`, `[CombinedFragment](../../interactions/mdfragments/CombinedFragment.html)`, `[Comment](Comment.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[ComponentRealization](../../components/mdbasiccomponents/ComponentRealization.html)`, `[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html)`, `[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)`, `[ConnectableElementTemplateParameter](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)`, `[ConnectionPointReference](../../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)`, `[Connector](../../compositestructures/mdinternalstructures/Connector.html)`, `[ConnectorEnd](../../compositestructures/mdinternalstructures/ConnectorEnd.html)`, `[ConsiderIgnoreFragment](../../interactions/mdfragments/ConsiderIgnoreFragment.html)`, `[Constraint](Constraint.html)`, `[Continuation](../../interactions/mdfragments/Continuation.html)`, `[ControlFlow](../../activities/mdbasicactivities/ControlFlow.html)`, `[ControlNode](../../activities/mdbasicactivities/ControlNode.html)`, `[CreateLinkAction](../../actions/mdintermediateactions/CreateLinkAction.html)`, `[CreateLinkObjectAction](../../actions/mdcompleteactions/CreateLinkObjectAction.html)`, `[CreateObjectAction](../../actions/mdintermediateactions/CreateObjectAction.html)`, `[DataStoreNode](../../activities/mdcompleteactivities/DataStoreNode.html)`, `[DataType](DataType.html)`, `[DecisionNode](../../activities/mdintermediateactivities/DecisionNode.html)`, `[Dependency](../mddependencies/Dependency.html)`, `[DeployedArtifact](../../deployments/mdnodes/DeployedArtifact.html)`, `[Deployment](../../deployments/mdnodes/Deployment.html)`, `[DeploymentSpecification](../../deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)`, `[DestroyLinkAction](../../actions/mdintermediateactions/DestroyLinkAction.html)`, `[DestroyObjectAction](../../actions/mdintermediateactions/DestroyObjectAction.html)`, `[DestructionOccurrenceSpecification](../../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[Diagram](Diagram.html)`, `[DirectedRelationship](DirectedRelationship.html)`, `[Duration](../../commonbehaviors/mdsimpletime/Duration.html)`, `[DurationConstraint](../../commonbehaviors/mdsimpletime/DurationConstraint.html)`, `[DurationInterval](../../commonbehaviors/mdsimpletime/DurationInterval.html)`, `[DurationObservation](../../commonbehaviors/mdsimpletime/DurationObservation.html)`, `[ElementImport](ElementImport.html)`, `[ElementTaggedValue](ElementTaggedValue.html)`, `[ElementValue](ElementValue.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](Enumeration.html)`, `[EnumerationLiteral](EnumerationLiteral.html)`, `[Event](../../commonbehaviors/mdcommunications/Event.html)`, `[ExceptionHandler](../../activities/mdextrastructuredactivities/ExceptionHandler.html)`, `[ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[ExecutionOccurrenceSpecification](../../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)`, `[ExecutionSpecification](../../interactions/mdbasicinteractions/ExecutionSpecification.html)`, `[ExpansionNode](../../activities/mdextrastructuredactivities/ExpansionNode.html)`, `[ExpansionRegion](../../activities/mdextrastructuredactivities/ExpansionRegion.html)`, `[Expression](Expression.html)`, `[Extend](../../mdusecases/Extend.html)`, `[Extension](../../mdprofiles/Extension.html)`, `[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[ExtensionPoint](../../mdusecases/ExtensionPoint.html)`, `[Feature](Feature.html)`, `[FinalNode](../../activities/mdintermediateactivities/FinalNode.html)`, `[FinalState](../../statemachines/mdbehaviorstatemachines/FinalState.html)`, `[FlowFinalNode](../../activities/mdintermediateactivities/FlowFinalNode.html)`, `[ForkNode](../../activities/mdintermediateactivities/ForkNode.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[Gate](../../interactions/mdfragments/Gate.html)`, `[Generalization](Generalization.html)`, `[GeneralizationSet](../mdpowertypes/GeneralizationSet.html)`, `[GeneralOrdering](../../interactions/mdbasicinteractions/GeneralOrdering.html)`, `[Image](../../mdprofiles/Image.html)`, `[Include](../../mdusecases/Include.html)`, `[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)`, `[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)`, `[InitialNode](../../activities/mdbasicactivities/InitialNode.html)`, `[InputPin](../../actions/mdbasicactions/InputPin.html)`, `[InstanceSpecification](InstanceSpecification.html)`, `[InstanceValue](InstanceValue.html)`, `[IntegerTaggedValue](IntegerTaggedValue.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html)`, `[InteractionFragment](../../interactions/mdbasicinteractions/InteractionFragment.html)`, `[InteractionOperand](../../interactions/mdfragments/InteractionOperand.html)`, `[InteractionUse](../../interactions/mdfragments/InteractionUse.html)`, `[Interface](../mdinterfaces/Interface.html)`, `[InterfaceRealization](../mdinterfaces/InterfaceRealization.html)`, `[InterruptibleActivityRegion](../../activities/mdcompleteactivities/InterruptibleActivityRegion.html)`, `[Interval](../../commonbehaviors/mdsimpletime/Interval.html)`, `[IntervalConstraint](../../commonbehaviors/mdsimpletime/IntervalConstraint.html)`, `[InvocationAction](../../actions/mdbasicactions/InvocationAction.html)`, `[JoinNode](../../activities/mdintermediateactivities/JoinNode.html)`, `[Lifeline](../../interactions/mdbasicinteractions/Lifeline.html)`, `[LinkAction](../../actions/mdintermediateactions/LinkAction.html)`, `[LinkEndCreationData](../../actions/mdintermediateactions/LinkEndCreationData.html)`, `[LinkEndData](../../actions/mdintermediateactions/LinkEndData.html)`, `[LinkEndDestructionData](../../actions/mdintermediateactions/LinkEndDestructionData.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralNull](LiteralNull.html)`, `[LiteralReal](LiteralReal.html)`, `[LiteralSpecification](LiteralSpecification.html)`, `[LiteralString](LiteralString.html)`, `[LiteralUnlimitedNatural](LiteralUnlimitedNatural.html)`, `[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`, `[Manifestation](../../deployments/mdartifacts/Manifestation.html)`, `[MergeNode](../../activities/mdintermediateactivities/MergeNode.html)`, `[Message](../../interactions/mdbasicinteractions/Message.html)`, `[MessageEnd](../../interactions/mdbasicinteractions/MessageEnd.html)`, `[MessageEvent](../../commonbehaviors/mdcommunications/MessageEvent.html)`, `[MessageOccurrenceSpecification](../../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)`, `[Model](../../auxiliaryconstructs/mdmodels/Model.html)`, `[MultiplicityElement](MultiplicityElement.html)`, `[NamedElement](NamedElement.html)`, `[Namespace](Namespace.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)`, `[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)`, `[Observation](../../commonbehaviors/mdsimpletime/Observation.html)`, `[OccurrenceSpecification](../../interactions/mdbasicinteractions/OccurrenceSpecification.html)`, `[OpaqueAction](../../actions/mdbasicactions/OpaqueAction.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[OpaqueExpression](OpaqueExpression.html)`, `[Operation](Operation.html)`, `[OperationTemplateParameter](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)`, `[OutputPin](../../actions/mdbasicactions/OutputPin.html)`, `[Package](Package.html)`, `[PackageableElement](PackageableElement.html)`, `[PackageImport](PackageImport.html)`, `[PackageMerge](PackageMerge.html)`, `[Parameter](Parameter.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)`, `[PartDecomposition](../../interactions/mdfragments/PartDecomposition.html)`, `[Pin](../../actions/mdbasicactions/Pin.html)`, `[Port](../../compositestructures/mdports/Port.html)`, `[PrimitiveType](PrimitiveType.html)`, `[Profile](../../mdprofiles/Profile.html)`, `[ProfileApplication](../../mdprofiles/ProfileApplication.html)`, `[Property](Property.html)`, `[ProtocolConformance](../../statemachines/mdprotocolstatemachines/ProtocolConformance.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`, `[Pseudostate](../../statemachines/mdbehaviorstatemachines/Pseudostate.html)`, `[QualifierValue](../../actions/mdcompleteactions/QualifierValue.html)`, `[RaiseExceptionAction](../../actions/mdstructuredactions/RaiseExceptionAction.html)`, `[ReadExtentAction](../../actions/mdcompleteactions/ReadExtentAction.html)`, `[ReadIsClassifiedObjectAction](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`, `[ReadLinkAction](../../actions/mdintermediateactions/ReadLinkAction.html)`, `[ReadLinkObjectEndAction](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html)`, `[ReadLinkObjectEndQualifierAction](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`, `[ReadSelfAction](../../actions/mdintermediateactions/ReadSelfAction.html)`, `[ReadStructuralFeatureAction](../../actions/mdintermediateactions/ReadStructuralFeatureAction.html)`, `[ReadVariableAction](../../actions/mdstructuredactions/ReadVariableAction.html)`, `[Realization](../mddependencies/Realization.html)`, `[RealTaggedValue](RealTaggedValue.html)`, `[Reception](../../commonbehaviors/mdcommunications/Reception.html)`, `[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)`, `[RedefinableElement](RedefinableElement.html)`, `[RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`, `[ReduceAction](../../actions/mdcompleteactions/ReduceAction.html)`, `[Region](../../statemachines/mdbehaviorstatemachines/Region.html)`, `[Relationship](Relationship.html)`, `[RemoveStructuralFeatureValueAction](../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`, `[RemoveVariableValueAction](../../actions/mdstructuredactions/RemoveVariableValueAction.html)`, `[ReplyAction](../../actions/mdcompleteactions/ReplyAction.html)`, `[SendObjectAction](../../actions/mdintermediateactions/SendObjectAction.html)`, `[SendSignalAction](../../actions/mdbasicactions/SendSignalAction.html)`, `[SequenceNode](../../activities/mdstructuredactivities/SequenceNode.html)`, `[Signal](../../commonbehaviors/mdcommunications/Signal.html)`, `[SignalEvent](../../commonbehaviors/mdcommunications/SignalEvent.html)`, `[Slot](Slot.html)`, `[StartClassifierBehaviorAction](../../actions/mdcompleteactions/StartClassifierBehaviorAction.html)`, `[StartObjectBehaviorAction](../../actions/mdcompleteactions/StartObjectBehaviorAction.html)`, `[State](../../statemachines/mdbehaviorstatemachines/State.html)`, `[StateInvariant](../../interactions/mdbasicinteractions/StateInvariant.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`, `[StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html)`, `[StringTaggedValue](StringTaggedValue.html)`, `[StructuralFeature](StructuralFeature.html)`, `[StructuralFeatureAction](../../actions/mdintermediateactions/StructuralFeatureAction.html)`, `[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[Substitution](../mddependencies/Substitution.html)`, `[TaggedValue](TaggedValue.html)`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[TemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateBinding.html)`, `[TemplateParameter](../../auxiliaryconstructs/mdtemplates/TemplateParameter.html)`, `[TemplateParameterSubstitution](../../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html)`, `[TemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateSignature.html)`, `[TestIdentityAction](../../actions/mdintermediateactions/TestIdentityAction.html)`, `[TimeConstraint](../../commonbehaviors/mdsimpletime/TimeConstraint.html)`, `[TimeEvent](../../commonbehaviors/mdcommunications/TimeEvent.html)`, `[TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html)`, `[TimeInterval](../../commonbehaviors/mdsimpletime/TimeInterval.html)`, `[TimeObservation](../../commonbehaviors/mdsimpletime/TimeObservation.html)`, `[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`, `[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)`, `[Type](Type.html)`, `[TypedElement](TypedElement.html)`, `[UnmarshallAction](../../actions/mdcompleteactions/UnmarshallAction.html)`, `[Usage](../mddependencies/Usage.html)`, `[UseCase](../../mdusecases/UseCase.html)`, `[ValuePin](../../actions/mdbasicactions/ValuePin.html)`, `[ValueSpecification](ValueSpecification.html)`, `[ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html)`, `[Variable](../../activities/mdstructuredactivities/Variable.html)`, `[VariableAction](../../actions/mdstructuredactions/VariableAction.html)`, `[Vertex](../../statemachines/mdbehaviorstatemachines/Vertex.html)`, `[WriteLinkAction](../../actions/mdintermediateactions/WriteLinkAction.html)`, `[WriteStructuralFeatureAction](../../actions/mdintermediateactions/WriteStructuralFeatureAction.html)`, `[WriteVariableAction](../../actions/mdstructuredactions/WriteVariableAction.html)`

public interfaceElementextends [ModelObject](../../base/ModelObject.html)

begin-user-doc 
 A representation of the model object '***Element***'.
 end-user-doc 
begin-model-doc 
 An Element is a constituent of a model. As such, it has the capability of owning other Elements.
 end-model-doc 
The following features are supported:
 [`*Owned Comment*`](#getOwnedComment())
[`*comment Of Annotated Element*`](#get_commentOfAnnotatedElement())
[`*Owned Element*`](#getOwnedElement())
[`*Owner*`](#getOwner())
[`*Sync Element*`](#getSyncElement())
[`*element Of Sync Element*`](#get_elementOfSyncElement())
[`*Applied Stereotype*`](#getAppliedStereotype())
[`*relationship Of Related Element*`](#get_relationshipOfRelatedElement())
[`*activity Partition Of Represents*`](#get_activityPartitionOfRepresents())
[`*constraint Of Constrained Element*`](#get_constraintOfConstrainedElement())
[`*diagram Of Context*`](#get_diagramOfContext())
[`*directed Relationship Of Source*`](#get_directedRelationshipOfSource())
[`*directed Relationship Of Target*`](#get_directedRelationshipOfTarget())
[`*element Value Of Element*`](#get_elementValueOfElement())

See Also:
[`UMLPackage.getElement()`](../../metadata/UMLPackage.html#getElement())
Model:
abstract="true"
 annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](../../activities/mdintermediateactivities/ActivityPartition.html)>`
`[get_activityPartitionOfRepresents](#get_activityPartitionOfRepresents())()`
Returns the value of the '***activity Partition Of Represents***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Comment](Comment.html)>`
`[get_commentOfAnnotatedElement](#get_commentOfAnnotatedElement())()`
Returns the value of the '***comment Of Annotated Element***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)>`
`[get_constraintOfConstrainedElement](#get_constraintOfConstrainedElement())()`
Returns the value of the '***constraint Of Constrained Element***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](Diagram.html)>`
`[get_diagramOfContext](#get_diagramOfContext())()`
Returns the value of the '***diagram Of Context***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DirectedRelationship](DirectedRelationship.html)>`
`[get_directedRelationshipOfSource](#get_directedRelationshipOfSource())()`
Returns the value of the '***directed Relationship Of Source***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DirectedRelationship](DirectedRelationship.html)>`
`[get_directedRelationshipOfTarget](#get_directedRelationshipOfTarget())()`
Returns the value of the '***directed Relationship Of Target***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](Element.html)>`
`[get_elementOfSyncElement](#get_elementOfSyncElement())()`
Returns the value of the '***element Of Sync Element***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementTaggedValue](ElementTaggedValue.html)>`
`[get_elementTaggedValue](#get_elementTaggedValue())()`
Returns the value of the '***Element Tagged Value***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ElementValue](ElementValue.html)>`
`[get_elementValueOfElement](#get_elementValueOfElement())()`
Returns the value of the '***element Value Of Element***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Relationship](Relationship.html)>`
`[get_relationshipOfRelatedElement](#get_relationshipOfRelatedElement())()`
Returns the value of the '***relationship Of Related Element***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Stereotype](../../mdprofiles/Stereotype.html)>`
`[getAppliedStereotype](#getAppliedStereotype())()`
Returns the value of the '***Applied Stereotype***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Comment](Comment.html)>`
`[getOwnedComment](#getOwnedComment())()`
Returns the value of the '***Owned Comment***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](Element.html)>`
`[getOwnedElement](#getOwnedElement())()`
Returns the value of the '***Owned Element***' reference list.
`[Element](Element.html)`
`[getOwner](#getOwner())()`
Returns the value of the '***Owner***' reference.
`[Element](Element.html)`
`[getSyncElement](#getSyncElement())()`
Returns the value of the '***Sync Element***' reference.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TaggedValue](TaggedValue.html)>`
`[getTaggedValue](#getTaggedValue())()`
Returns the value of the '***Tagged Value***' containment reference list.
`boolean`
`[has_activityPartitionOfRepresents](#has_activityPartitionOfRepresents())()`

`boolean`
`[has_commentOfAnnotatedElement](#has_commentOfAnnotatedElement())()`

`boolean`
`[has_constraintOfConstrainedElement](#has_constraintOfConstrainedElement())()`

`boolean`
`[has_diagramOfContext](#has_diagramOfContext())()`

`boolean`
`[has_directedRelationshipOfSource](#has_directedRelationshipOfSource())()`

`boolean`
`[has_directedRelationshipOfTarget](#has_directedRelationshipOfTarget())()`

`boolean`
`[has_elementOfSyncElement](#has_elementOfSyncElement())()`

`boolean`
`[has_elementValueOfElement](#has_elementValueOfElement())()`

`boolean`
`[has_relationshipOfRelatedElement](#has_relationshipOfRelatedElement())()`

`boolean`
`[hasAppliedStereotype](#hasAppliedStereotype())()`

`boolean`
`[hasElementTaggedValue](#hasElementTaggedValue())()`

`boolean`
`[hasOwnedComment](#hasOwnedComment())()`

`boolean`
`[hasOwnedElement](#hasOwnedElement())()`

`boolean`
`[hasTaggedValue](#hasTaggedValue())()`

`void`
`[setOwner](#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](Element.html) value)`
Sets the value of the '[`*Owner*`](#getOwner())' reference.
`void`
`[setSyncElement](#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](Element.html) value)`
Sets the value of the '[`*Sync Element*`](#getSyncElement())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getOwnedComment
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Comment](Comment.html)> getOwnedComment()
Returns the value of the '***Owned Comment***' containment reference list.
 The list contents are of type [`Comment`](Comment.html).
 It is bidirectional and its opposite is '[`*Owning Element*`](Comment.html#getOwningElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Comments owned by this Element.
 end-model-doc
Returns:
the value of the '*Owned Comment*' containment reference list.
See Also:
[`UMLPackage.getElement_OwnedComment()`](../../metadata/UMLPackage.html#getElement_OwnedComment())
[`Comment.getOwningElement()`](Comment.html#getOwningElement())
Model:
opposite="owningElement" containment="true" resolveProxies="true" ordered="false"
Generated:
get_commentOfAnnotatedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Comment](Comment.html)> get_commentOfAnnotatedElement()
Returns the value of the '***comment Of Annotated Element***' reference list.
 The list contents are of type [`Comment`](Comment.html).
 It is bidirectional and its opposite is '[`*Annotated Element*`](Comment.html#getAnnotatedElement())'.
 begin-user-doc 
If the meaning of the '*comment Of Annotated Element*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*comment Of Annotated Element*' reference list.
See Also:
[`UMLPackage.getElement__commentOfAnnotatedElement()`](../../metadata/UMLPackage.html#getElement__commentOfAnnotatedElement())
[`Comment.getAnnotatedElement()`](Comment.html#getAnnotatedElement())
Model:
opposite="annotatedElement" ordered="false"
Generated:
getOwnedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](Element.html)> getOwnedElement()
Returns the value of the '***Owned Element***' reference list.
 The list contents are of type [`Element`](Element.html).
 It is bidirectional and its opposite is '[`*Owner*`](#getOwner())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Elements owned by this Element.
 end-model-doc
Returns:
the value of the '*Owned Element*' reference list.
See Also:
[`UMLPackage.getElement_OwnedElement()`](../../metadata/UMLPackage.html#getElement_OwnedElement())
[`getOwner()`](#getOwner())
Model:
opposite="owner" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getOwner
@CheckForNull[Element](Element.html) getOwner()
Returns the value of the '***Owner***' reference.
 It is bidirectional and its opposite is '[`*Owned Element*`](#getOwnedElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Element that owns this Element.
 end-model-doc
Returns:
the value of the '*Owner*' reference.
See Also:
[`setOwner(Element)`](#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`UMLPackage.getElement_Owner()`](../../metadata/UMLPackage.html#getElement_Owner())
[`getOwnedElement()`](#getOwnedElement())
Model:
opposite="ownedElement" transient="true" volatile="true" derived="true" ordered="false"
Generated:
setOwner
void setOwner(@CheckForNull
 [Element](Element.html) value)
Sets the value of the '[`*Owner*`](#getOwner())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owner*' reference.
See Also:
[`getOwner()`](#getOwner())
Generated:
getSyncElement
@CheckForNull[Element](Element.html) getSyncElement()
Returns the value of the '***Sync Element***' reference.
 It is bidirectional and its opposite is
 '[`*element Of Sync Element*`](#get_elementOfSyncElement())'.
 begin-user-doc 
If the meaning of the '*Sync Element*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Sync Element*' reference.
See Also:
[`setSyncElement(Element)`](#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`UMLPackage.getElement_SyncElement()`](../../metadata/UMLPackage.html#getElement_SyncElement())
[`get_elementOfSyncElement()`](#get_elementOfSyncElement())
Model:
opposite="_elementOfSyncElement" ordered="false"
Generated:
setSyncElement
void setSyncElement(@CheckForNull
 [Element](Element.html) value)
Sets the value of the '[`*Sync Element*`](#getSyncElement())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Sync Element*' reference.
See Also:
[`getSyncElement()`](#getSyncElement())
Generated:
get_elementOfSyncElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](Element.html)> get_elementOfSyncElement()
Returns the value of the '***element Of Sync Element***' reference list.
 The list contents are of type [`Element`](Element.html).
 It is bidirectional and its opposite is '[`*Sync Element*`](#getSyncElement())'.
 begin-user-doc 
If the meaning of the '*element Of Sync Element*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*element Of Sync Element*' reference list.
See Also:
[`UMLPackage.getElement__elementOfSyncElement()`](../../metadata/UMLPackage.html#getElement__elementOfSyncElement())
[`getSyncElement()`](#getSyncElement())
Model:
opposite="syncElement" ordered="false"
Generated:
get_activityPartitionOfRepresents
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](../../activities/mdintermediateactivities/ActivityPartition.html)> get_activityPartitionOfRepresents()
Returns the value of the '***activity Partition Of Represents***' reference list.
 The list contents are of type [`ActivityPartition`](../../activities/mdintermediateactivities/ActivityPartition.html).
 It is bidirectional and its opposite is
 '[`*Represents*`](../../activities/mdintermediateactivities/ActivityPartition.html#getRepresents())'.
 begin-user-doc 
If the meaning of the '*activity Partition Of Represents*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*activity Partition Of Represents*' reference list.
See Also:
[`UMLPackage.getElement__activityPartitionOfRepresents()`](../../metadata/UMLPackage.html#getElement__activityPartitionOfRepresents())
[`ActivityPartition.getRepresents()`](../../activities/mdintermediateactivities/ActivityPartition.html#getRepresents())
Model:
opposite="represents" ordered="false"
Generated:
get_constraintOfConstrainedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)> get_constraintOfConstrainedElement()
Returns the value of the '***constraint Of Constrained Element***' reference list.
 The list contents are of type [`Constraint`](Constraint.html).
 It is bidirectional and its opposite is '[`*Constrained Element*`](Constraint.html#getConstrainedElement())'.
 begin-user-doc 
If the meaning of the '*constraint Of Constrained Element*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*constraint Of Constrained Element*' reference list.
See Also:
[`UMLPackage.getElement__constraintOfConstrainedElement()`](../../metadata/UMLPackage.html#getElement__constraintOfConstrainedElement())
[`Constraint.getConstrainedElement()`](Constraint.html#getConstrainedElement())
Model:
opposite="constrainedElement" ordered="false"
Generated:
get_diagramOfContext
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](Diagram.html)> get_diagramOfContext()
Returns the value of the '***diagram Of Context***' reference list.
 The list contents are of type [`Diagram`](Diagram.html).
 It is bidirectional and its opposite is '[`*Context*`](Diagram.html#getContext())'.
 begin-user-doc 
If the meaning of the '*diagram Of Context*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*diagram Of Context*' reference list.
See Also:
[`UMLPackage.getElement__diagramOfContext()`](../../metadata/UMLPackage.html#getElement__diagramOfContext())
[`Diagram.getContext()`](Diagram.html#getContext())
Model:
opposite="context" ordered="false"
Generated:
get_relationshipOfRelatedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Relationship](Relationship.html)> get_relationshipOfRelatedElement()
Returns the value of the '***relationship Of Related Element***' reference list.
 The list contents are of type [`Relationship`](Relationship.html).
 It is bidirectional and its opposite is '[`*Related Element*`](Relationship.html#getRelatedElement())'.
 begin-user-doc 
If the meaning of the '*relationship Of Related Element*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*relationship Of Related Element*' reference list.
See Also:
[`UMLPackage.getElement__relationshipOfRelatedElement()`](../../metadata/UMLPackage.html#getElement__relationshipOfRelatedElement())
[`Relationship.getRelatedElement()`](Relationship.html#getRelatedElement())
Model:
opposite="relatedElement" transient="true" volatile="true" derived="true" ordered="false"
Generated:
get_directedRelationshipOfSource
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DirectedRelationship](DirectedRelationship.html)> get_directedRelationshipOfSource()
Returns the value of the '***directed Relationship Of Source***' reference list.
 The list contents are of type [`DirectedRelationship`](DirectedRelationship.html).
 It is bidirectional and its opposite is '[`*Source*`](DirectedRelationship.html#getSource())'.
 begin-user-doc 
If the meaning of the '*directed Relationship Of Source*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*directed Relationship Of Source*' reference list.
See Also:
[`UMLPackage.getElement__directedRelationshipOfSource()`](../../metadata/UMLPackage.html#getElement__directedRelationshipOfSource())
[`DirectedRelationship.getSource()`](DirectedRelationship.html#getSource())
Model:
opposite="source" transient="true" volatile="true" derived="true" ordered="false"
Generated:
get_directedRelationshipOfTarget
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DirectedRelationship](DirectedRelationship.html)> get_directedRelationshipOfTarget()
Returns the value of the '***directed Relationship Of Target***' reference list.
 The list contents are of type [`DirectedRelationship`](DirectedRelationship.html).
 It is bidirectional and its opposite is '[`*Target*`](DirectedRelationship.html#getTarget())'.
 begin-user-doc 
If the meaning of the '*directed Relationship Of Target*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*directed Relationship Of Target*' reference list.
See Also:
[`UMLPackage.getElement__directedRelationshipOfTarget()`](../../metadata/UMLPackage.html#getElement__directedRelationshipOfTarget())
[`DirectedRelationship.getTarget()`](DirectedRelationship.html#getTarget())
Model:
opposite="target" transient="true" volatile="true" derived="true" ordered="false"
Generated:
get_elementValueOfElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ElementValue](ElementValue.html)> get_elementValueOfElement()
Returns the value of the '***element Value Of Element***' reference list.
 The list contents are of type [`ElementValue`](ElementValue.html).
 It is bidirectional and its opposite is '[`*Element*`](ElementValue.html#getElement())'.
 begin-user-doc 
If the meaning of the '*element Value Of Element*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*element Value Of Element*' reference list.
See Also:
[`UMLPackage.getElement__elementValueOfElement()`](../../metadata/UMLPackage.html#getElement__elementValueOfElement())
[`ElementValue.getElement()`](ElementValue.html#getElement())
Model:
opposite="element" ordered="false"
Generated:
hasOwnedComment
boolean hasOwnedComment()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_commentOfAnnotatedElement
boolean has_commentOfAnnotatedElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedElement
boolean hasOwnedElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_elementOfSyncElement
boolean has_elementOfSyncElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_activityPartitionOfRepresents
boolean has_activityPartitionOfRepresents()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_constraintOfConstrainedElement
boolean has_constraintOfConstrainedElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_diagramOfContext
boolean has_diagramOfContext()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_relationshipOfRelatedElement
boolean has_relationshipOfRelatedElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_directedRelationshipOfSource
boolean has_directedRelationshipOfSource()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_directedRelationshipOfTarget
boolean has_directedRelationshipOfTarget()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_elementValueOfElement
boolean has_elementValueOfElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
getTaggedValue
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TaggedValue](TaggedValue.html)> getTaggedValue()
Returns the value of the '***Tagged Value***' containment reference list.
 The list contents are of type [`TaggedValue`](TaggedValue.html).
 It is bidirectional and its opposite is '[`*Tagged Value Owner*`](TaggedValue.html#getTaggedValueOwner())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The TaggedValues of this element.
 end-model-doc
Returns:
the value of the '*Tagged Value*' containment reference list.
See Also:
[`UMLPackage.getElement_TaggedValue()`](../../metadata/UMLPackage.html#getElement_TaggedValue())
[`TaggedValue.getTaggedValueOwner()`](TaggedValue.html#getTaggedValueOwner())
Model:
opposite="taggedValueOwner" containment="true" resolveProxies="true"
Generated:
hasTaggedValue
boolean hasTaggedValue()
Generated:
getAppliedStereotype
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Stereotype](../../mdprofiles/Stereotype.html)> getAppliedStereotype()
Returns the value of the '***Applied Stereotype***' reference list.
 The list contents are of type [`Stereotype`](../../mdprofiles/Stereotype.html).
 It is bidirectional and its opposite is '[`*Stereotyped Element*`](../../mdprofiles/Stereotype.html#get_stereotypedElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Stereotypes applied to this element.
 end-model-doc
Returns:
the value of the '*Applied Stereotype*' reference list.
See Also:
[`UMLPackage.getElement_AppliedStereotype()`](../../metadata/UMLPackage.html#getElement_AppliedStereotype())
[`Stereotype.get_stereotypedElement()`](../../mdprofiles/Stereotype.html#get_stereotypedElement())
Model:
opposite="_stereotypedElement"
Generated:
hasAppliedStereotype
boolean hasAppliedStereotype()
Generated:
get_elementTaggedValue
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementTaggedValue](ElementTaggedValue.html)> get_elementTaggedValue()
Returns the value of the '***Element Tagged Value***' reference list.
 The list contents are of type [`ElementTaggedValue`](ElementTaggedValue.html).
 It is bidirectional and its opposite is '[`*Value*`](ElementTaggedValue.html#getValue())'.
 begin-user-doc 
 end-user-doc
Returns:
the value of the '*Element Tagged Value*' reference list.
See Also:
[`UMLPackage.getElement__elementTaggedValue()`](../../metadata/UMLPackage.html#getElement__elementTaggedValue())
[`ElementTaggedValue.getValue()`](ElementTaggedValue.html#getValue())
Model:
opposite="value"
Generated:
hasElementTaggedValue
boolean hasElementTaggedValue()
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface Element">Interface Element</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code>, <code><a href="../../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code>, <code><a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code>, <code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></code>, <code><a href="../../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></code>, <code><a href="../../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></code>, <code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code>, <code><a href="../../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></code>, <code><a href="../../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code>, <code><a href="../../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></code>, <code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></code>, <code><a href="BooleanTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BooleanTaggedValue</a></code>, <code><a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code>, <code><a href="../../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code>, <code><a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code>, <code><a href="../../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></code>, <code><a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code>, <code><a href="../../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code>, <code><a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code>, <code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></code>, <code><a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code>, <code><a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code>, <code><a href="../../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code>, <code><a href="../../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code>, <code><a href="../../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code>, <code><a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code>, <code><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></code>, <code><a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code>, <code><a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></code>, <code><a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code>, <code><a href="../../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></code>, <code><a href="../../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code>, <code><a href="../../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a></code>, <code><a href="../../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code>, <code><a href="../../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code>, <code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code>, <code><a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code>, <code><a href="../../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a></code>, <code><a href="../../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code>, <code><a href="../../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code>, <code><a href="../../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code>, <code><a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></code>, <code><a href="ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a></code>, <code><a href="ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a></code>, <code><a href="ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></code>, <code><a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></code>, <code><a href="../../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code>, <code><a href="../../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></code>, <code><a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code>, <code><a href="../../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></code>, <code><a href="../../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></code>, <code><a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></code>, <code><a href="../mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></code>, <code><a href="../../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></code>, <code><a href="../../mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code>, <code><a href="../../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></code>, <code><a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code>, <code><a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code>, <code><a href="InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code>, <code><a href="IntegerTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">IntegerTaggedValue</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code>, <code><a href="../../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a></code>, <code><a href="../../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></code>, <code><a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code>, <code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code>, <code><a href="../../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code>, <code><a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code>, <code><a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code>, <code><a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code>, <code><a href="../../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></code>, <code><a href="../../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></code>, <code><a href="../../actions/mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code>, <code><a href="LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code>, <code><a href="LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code>, <code><a href="LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code>, <code><a href="LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></code>, <code><a href="LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code>, <code><a href="LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code>, <code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="../../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code>, <code><a href="../../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code>, <code><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code>, <code><a href="../../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></code>, <code><a href="../../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a></code>, <code><a href="../../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></code>, <code><a href="../../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code>, <code><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code>, <code><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a></code>, <code><a href="../../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></code>, <code><a href="../../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code>, <code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></code>, <code><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code>, <code><a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a></code>, <code><a href="PackageMerge.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageMerge</a></code>, <code><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></code>, <code><a href="../../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></code>, <code><a href="../../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code>, <code><a href="../../mdprofiles/ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a></code>, <code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolConformance.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolConformance</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></code>, <code><a href="../../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></code>, <code><a href="../../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code>, <code><a href="../mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code>, <code><a href="RealTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RealTaggedValue</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code>, <code><a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code>, <code><a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code>, <code><a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code>, <code><a href="../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code>, <code><a href="../../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code>, <code><a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code>, <code><a href="../../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code>, <code><a href="Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code>, <code><a href="../../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code>, <code><a href="../../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code>, <code><a href="../../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code>, <code><a href="StringTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StringTaggedValue</a></code>, <code><a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code>, <code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code>, <code><a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></code>, <code><a href="../../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code>, <code><a href="../../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></code>, <code><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code>, <code><a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code>, <code><a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code>, <code><a href="../mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code>, <code><a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code>, <code><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code>, <code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code>, <code><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code>, <code><a href="../../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code>, <code><a href="../../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code>, <code><a href="../../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Element</span><span class="extends-implements">
extends <a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Element</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An Element is a constituent of a model. As such, it has the capability of owning other Elements.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getOwnedComment()"><code><em>Owned Comment</em></code></a></li>
<li><a href="#get_commentOfAnnotatedElement()"><code><em>comment Of Annotated Element</em></code></a></li>
<li><a href="#getOwnedElement()"><code><em>Owned Element</em></code></a></li>
<li><a href="#getOwner()"><code><em>Owner</em></code></a></li>
<li><a href="#getSyncElement()"><code><em>Sync Element</em></code></a></li>
<li><a href="#get_elementOfSyncElement()"><code><em>element Of Sync Element</em></code></a></li>
<li><a href="#getAppliedStereotype()"><code><em>Applied Stereotype</em></code></a></li>
<li><a href="#get_relationshipOfRelatedElement()"><code><em>relationship Of Related Element</em></code></a></li>
<li><a href="#get_activityPartitionOfRepresents()"><code><em>activity Partition Of Represents</em></code></a></li>
<li><a href="#get_constraintOfConstrainedElement()"><code><em>constraint Of Constrained Element</em></code></a></li>
<li><a href="#get_diagramOfContext()"><code><em>diagram Of Context</em></code></a></li>
<li><a href="#get_directedRelationshipOfSource()"><code><em>directed Relationship Of Source</em></code></a></li>
<li><a href="#get_directedRelationshipOfTarget()"><code><em>directed Relationship Of Target</em></code></a></li>
<li><a href="#get_elementValueOfElement()"><code><em>element Value Of Element</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getElement()"><code>UMLPackage.getElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='classes.mdkernel'"</dd>
<dt>Generated:</dt>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>activity Partition Of Represents</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>comment Of Annotated Element</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>constraint Of Constrained Element</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_diagramOfContext()">get_diagramOfContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>diagram Of Context</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>directed Relationship Of Source</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>directed Relationship Of Target</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_elementOfSyncElement()">get_elementOfSyncElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>element Of Sync Element</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_elementTaggedValue()">get_elementTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Element Tagged Value</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_elementValueOfElement()">get_elementValueOfElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>element Value Of Element</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>relationship Of Related Element</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAppliedStereotype()">getAppliedStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Applied Stereotype</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedComment()">getOwnedComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Comment</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedElement()">getOwnedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Element</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwner()">getOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owner</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSyncElement()">getSyncElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Sync Element</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTaggedValue()">getTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Tagged Value</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_diagramOfContext()">has_diagramOfContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_elementOfSyncElement()">has_elementOfSyncElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_elementValueOfElement()">has_elementValueOfElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasAppliedStereotype()">hasAppliedStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasElementTaggedValue()">hasElementTaggedValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedComment()">hasOwnedComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedElement()">hasOwnedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasTaggedValue()">hasTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a><wbr/>(<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwner()"><code><em>Owner</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a><wbr/>(<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSyncElement()"><code><em>Sync Element</em></code></a>' reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
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
<section class="detail" id="getOwnedComment()">
<h3>getOwnedComment</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt;</span> <span class="element-name">getOwnedComment</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Comment</b></em>' containment reference list.
 The list contents are of type <a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a>.
 It is bidirectional and its opposite is '<a href="Comment.html#getOwningElement()"><code><em>Owning Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Comments owned by this Element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Comment</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement_OwnedComment()"><code>UMLPackage.getElement_OwnedComment()</code></a></li>
<li><a href="Comment.html#getOwningElement()"><code>Comment.getOwningElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningElement" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_commentOfAnnotatedElement()">
<h3>get_commentOfAnnotatedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt;</span> <span class="element-name">get_commentOfAnnotatedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>comment Of Annotated Element</b></em>' reference list.
 The list contents are of type <a href="Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Comment</code></a>.
 It is bidirectional and its opposite is '<a href="Comment.html#getAnnotatedElement()"><code><em>Annotated Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>comment Of Annotated Element</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>comment Of Annotated Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__commentOfAnnotatedElement()"><code>UMLPackage.getElement__commentOfAnnotatedElement()</code></a></li>
<li><a href="Comment.html#getAnnotatedElement()"><code>Comment.getAnnotatedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="annotatedElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElement()">
<h3>getOwnedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOwnedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Element</b></em>' reference list.
 The list contents are of type <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.
 It is bidirectional and its opposite is '<a href="#getOwner()"><code><em>Owner</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Elements owned by this Element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement_OwnedElement()"><code>UMLPackage.getElement_OwnedElement()</code></a></li>
<li><a href="#getOwner()"><code>getOwner()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owner" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwner()">
<h3>getOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getOwner</span>()</div>
<div class="block">Returns the value of the '<em><b>Owner</b></em>' reference.
 It is bidirectional and its opposite is '<a href="#getOwnedElement()"><code><em>Owned Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Element that owns this Element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owner</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>setOwner(Element)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElement_Owner()"><code>UMLPackage.getElement_Owner()</code></a></li>
<li><a href="#getOwnedElement()"><code>getOwnedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedElement" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setOwner</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwner</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwner()"><code><em>Owner</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owner</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getOwner()"><code>getOwner()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSyncElement()">
<h3>getSyncElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSyncElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Sync Element</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="#get_elementOfSyncElement()"><code><em>element Of Sync Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Sync Element</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Sync Element</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>setSyncElement(Element)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElement_SyncElement()"><code>UMLPackage.getElement_SyncElement()</code></a></li>
<li><a href="#get_elementOfSyncElement()"><code>get_elementOfSyncElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_elementOfSyncElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setSyncElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSyncElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSyncElement()"><code><em>Sync Element</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Sync Element</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSyncElement()"><code>getSyncElement()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_elementOfSyncElement()">
<h3>get_elementOfSyncElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">get_elementOfSyncElement</span>()</div>
<div class="block">Returns the value of the '<em><b>element Of Sync Element</b></em>' reference list.
 The list contents are of type <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.
 It is bidirectional and its opposite is '<a href="#getSyncElement()"><code><em>Sync Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>element Of Sync Element</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>element Of Sync Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__elementOfSyncElement()"><code>UMLPackage.getElement__elementOfSyncElement()</code></a></li>
<li><a href="#getSyncElement()"><code>getSyncElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="syncElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_activityPartitionOfRepresents()">
<h3>get_activityPartitionOfRepresents</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</span> <span class="element-name">get_activityPartitionOfRepresents</span>()</div>
<div class="block">Returns the value of the '<em><b>activity Partition Of Represents</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdintermediateactivities/ActivityPartition.html#getRepresents()"><code><em>Represents</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>activity Partition Of Represents</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>activity Partition Of Represents</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__activityPartitionOfRepresents()"><code>UMLPackage.getElement__activityPartitionOfRepresents()</code></a></li>
<li><a href="../../activities/mdintermediateactivities/ActivityPartition.html#getRepresents()"><code>ActivityPartition.getRepresents()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="represents" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_constraintOfConstrainedElement()">
<h3>get_constraintOfConstrainedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">get_constraintOfConstrainedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>constraint Of Constrained Element</b></em>' reference list.
 The list contents are of type <a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is '<a href="Constraint.html#getConstrainedElement()"><code><em>Constrained Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>constraint Of Constrained Element</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>constraint Of Constrained Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__constraintOfConstrainedElement()"><code>UMLPackage.getElement__constraintOfConstrainedElement()</code></a></li>
<li><a href="Constraint.html#getConstrainedElement()"><code>Constraint.getConstrainedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="constrainedElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_diagramOfContext()">
<h3>get_diagramOfContext</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</span> <span class="element-name">get_diagramOfContext</span>()</div>
<div class="block">Returns the value of the '<em><b>diagram Of Context</b></em>' reference list.
 The list contents are of type <a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a>.
 It is bidirectional and its opposite is '<a href="Diagram.html#getContext()"><code><em>Context</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>diagram Of Context</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>diagram Of Context</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__diagramOfContext()"><code>UMLPackage.getElement__diagramOfContext()</code></a></li>
<li><a href="Diagram.html#getContext()"><code>Diagram.getContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="context" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_relationshipOfRelatedElement()">
<h3>get_relationshipOfRelatedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a>&gt;</span> <span class="element-name">get_relationshipOfRelatedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>relationship Of Related Element</b></em>' reference list.
 The list contents are of type <a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a>.
 It is bidirectional and its opposite is '<a href="Relationship.html#getRelatedElement()"><code><em>Related Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>relationship Of Related Element</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>relationship Of Related Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__relationshipOfRelatedElement()"><code>UMLPackage.getElement__relationshipOfRelatedElement()</code></a></li>
<li><a href="Relationship.html#getRelatedElement()"><code>Relationship.getRelatedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="relatedElement" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_directedRelationshipOfSource()">
<h3>get_directedRelationshipOfSource</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;</span> <span class="element-name">get_directedRelationshipOfSource</span>()</div>
<div class="block">Returns the value of the '<em><b>directed Relationship Of Source</b></em>' reference list.
 The list contents are of type <a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a>.
 It is bidirectional and its opposite is '<a href="DirectedRelationship.html#getSource()"><code><em>Source</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>directed Relationship Of Source</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>directed Relationship Of Source</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__directedRelationshipOfSource()"><code>UMLPackage.getElement__directedRelationshipOfSource()</code></a></li>
<li><a href="DirectedRelationship.html#getSource()"><code>DirectedRelationship.getSource()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="source" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_directedRelationshipOfTarget()">
<h3>get_directedRelationshipOfTarget</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;</span> <span class="element-name">get_directedRelationshipOfTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>directed Relationship Of Target</b></em>' reference list.
 The list contents are of type <a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>DirectedRelationship</code></a>.
 It is bidirectional and its opposite is '<a href="DirectedRelationship.html#getTarget()"><code><em>Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>directed Relationship Of Target</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>directed Relationship Of Target</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__directedRelationshipOfTarget()"><code>UMLPackage.getElement__directedRelationshipOfTarget()</code></a></li>
<li><a href="DirectedRelationship.html#getTarget()"><code>DirectedRelationship.getTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="target" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_elementValueOfElement()">
<h3>get_elementValueOfElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a>&gt;</span> <span class="element-name">get_elementValueOfElement</span>()</div>
<div class="block">Returns the value of the '<em><b>element Value Of Element</b></em>' reference list.
 The list contents are of type <a href="ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementValue</code></a>.
 It is bidirectional and its opposite is '<a href="ElementValue.html#getElement()"><code><em>Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>element Value Of Element</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>element Value Of Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__elementValueOfElement()"><code>UMLPackage.getElement__elementValueOfElement()</code></a></li>
<li><a href="ElementValue.html#getElement()"><code>ElementValue.getElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="element" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedComment()">
<h3>hasOwnedComment</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedComment</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_commentOfAnnotatedElement()">
<h3>has_commentOfAnnotatedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_commentOfAnnotatedElement</span>()
                               throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedElement()">
<h3>hasOwnedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedElement</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_elementOfSyncElement()">
<h3>has_elementOfSyncElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_elementOfSyncElement</span>()
                          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_activityPartitionOfRepresents()">
<h3>has_activityPartitionOfRepresents</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_activityPartitionOfRepresents</span>()
                                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_constraintOfConstrainedElement()">
<h3>has_constraintOfConstrainedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_constraintOfConstrainedElement</span>()
                                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_diagramOfContext()">
<h3>has_diagramOfContext</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_diagramOfContext</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_relationshipOfRelatedElement()">
<h3>has_relationshipOfRelatedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_relationshipOfRelatedElement</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_directedRelationshipOfSource()">
<h3>has_directedRelationshipOfSource</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_directedRelationshipOfSource</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_directedRelationshipOfTarget()">
<h3>has_directedRelationshipOfTarget</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_directedRelationshipOfTarget</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_elementValueOfElement()">
<h3>has_elementValueOfElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_elementValueOfElement</span>()
                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValue()">
<h3>getTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt;</span> <span class="element-name">getTaggedValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Tagged Value</b></em>' containment reference list.
 The list contents are of type <a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TaggedValue</code></a>.
 It is bidirectional and its opposite is '<a href="TaggedValue.html#getTaggedValueOwner()"><code><em>Tagged Value Owner</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The TaggedValues of this element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Tagged Value</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement_TaggedValue()"><code>UMLPackage.getElement_TaggedValue()</code></a></li>
<li><a href="TaggedValue.html#getTaggedValueOwner()"><code>TaggedValue.getTaggedValueOwner()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="taggedValueOwner" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasTaggedValue()">
<h3>hasTaggedValue</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasTaggedValue</span>()</div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedStereotype()">
<h3>getAppliedStereotype</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAppliedStereotype</span>()</div>
<div class="block">Returns the value of the '<em><b>Applied Stereotype</b></em>' reference list.
 The list contents are of type <a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.
 It is bidirectional and its opposite is '<a href="../../mdprofiles/Stereotype.html#get_stereotypedElement()"><code><em>Stereotyped Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Stereotypes applied to this element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Applied Stereotype</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement_AppliedStereotype()"><code>UMLPackage.getElement_AppliedStereotype()</code></a></li>
<li><a href="../../mdprofiles/Stereotype.html#get_stereotypedElement()"><code>Stereotype.get_stereotypedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_stereotypedElement"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasAppliedStereotype()">
<h3>hasAppliedStereotype</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasAppliedStereotype</span>()</div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_elementTaggedValue()">
<h3>get_elementTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementTaggedValue</a>&gt;</span> <span class="element-name">get_elementTaggedValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Element Tagged Value</b></em>' reference list.
 The list contents are of type <a href="ElementTaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementTaggedValue</code></a>.
 It is bidirectional and its opposite is '<a href="ElementTaggedValue.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Element Tagged Value</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getElement__elementTaggedValue()"><code>UMLPackage.getElement__elementTaggedValue()</code></a></li>
<li><a href="ElementTaggedValue.html#getValue()"><code>ElementTaggedValue.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasElementTaggedValue()">
<h3>hasElementTaggedValue</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasElementTaggedValue</span>()</div>
<dl class="notes">
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
