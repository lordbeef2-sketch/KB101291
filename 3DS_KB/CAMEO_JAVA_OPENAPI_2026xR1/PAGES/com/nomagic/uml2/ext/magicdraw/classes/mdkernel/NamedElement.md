# JAVA OPENAPI: NamedElement (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/NamedElement.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/NamedElement.html`
- source_sha256: `22e69b6fa3c4de7685ecdce6f3dcc338fa2ef9954989e969c9fb9bf951811842`
- captured_utc: `2026-07-14T16:46:29.354191+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface NamedElement

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[Abstraction](../mddependencies/Abstraction.html)`, `[AcceptCallAction](../../actions/mdcompleteactions/AcceptCallAction.html)`, `[AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html)`, `[Action](../../actions/mdbasicactions/Action.html)`, `[ActionExecutionSpecification](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html)`, `[ActionInputPin](../../actions/mdstructuredactions/ActionInputPin.html)`, `[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html)`, `[ActivityFinalNode](../../activities/mdbasicactivities/ActivityFinalNode.html)`, `[ActivityGroup](../../activities/mdfundamentalactivities/ActivityGroup.html)`, `[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[ActivityParameterNode](../../activities/mdbasicactivities/ActivityParameterNode.html)`, `[ActivityPartition](../../activities/mdintermediateactivities/ActivityPartition.html)`, `[Actor](../../mdusecases/Actor.html)`, `[AddStructuralFeatureValueAction](../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`, `[AddVariableValueAction](../../actions/mdstructuredactions/AddVariableValueAction.html)`, `[AnyReceiveEvent](../../commonbehaviors/mdcommunications/AnyReceiveEvent.html)`, `[Artifact](../../deployments/mdartifacts/Artifact.html)`, `[Association](Association.html)`, `[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioralFeature](BehavioralFeature.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[BehaviorExecutionSpecification](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)`, `[BroadcastSignalAction](../../actions/mdintermediateactions/BroadcastSignalAction.html)`, `[CallAction](../../actions/mdbasicactions/CallAction.html)`, `[CallBehaviorAction](../../actions/mdbasicactions/CallBehaviorAction.html)`, `[CallEvent](../../commonbehaviors/mdcommunications/CallEvent.html)`, `[CallOperationAction](../../actions/mdbasicactions/CallOperationAction.html)`, `[CentralBufferNode](../../activities/mdintermediateactivities/CentralBufferNode.html)`, `[ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[ClearAssociationAction](../../actions/mdintermediateactions/ClearAssociationAction.html)`, `[ClearStructuralFeatureAction](../../actions/mdintermediateactions/ClearStructuralFeatureAction.html)`, `[ClearVariableAction](../../actions/mdstructuredactions/ClearVariableAction.html)`, `[Collaboration](../../compositestructures/mdcollaborations/Collaboration.html)`, `[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html)`, `[CombinedFragment](../../interactions/mdfragments/CombinedFragment.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[ComponentRealization](../../components/mdbasiccomponents/ComponentRealization.html)`, `[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html)`, `[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)`, `[ConnectionPointReference](../../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)`, `[Connector](../../compositestructures/mdinternalstructures/Connector.html)`, `[ConsiderIgnoreFragment](../../interactions/mdfragments/ConsiderIgnoreFragment.html)`, `[Constraint](Constraint.html)`, `[Continuation](../../interactions/mdfragments/Continuation.html)`, `[ControlFlow](../../activities/mdbasicactivities/ControlFlow.html)`, `[ControlNode](../../activities/mdbasicactivities/ControlNode.html)`, `[CreateLinkAction](../../actions/mdintermediateactions/CreateLinkAction.html)`, `[CreateLinkObjectAction](../../actions/mdcompleteactions/CreateLinkObjectAction.html)`, `[CreateObjectAction](../../actions/mdintermediateactions/CreateObjectAction.html)`, `[DataStoreNode](../../activities/mdcompleteactivities/DataStoreNode.html)`, `[DataType](DataType.html)`, `[DecisionNode](../../activities/mdintermediateactivities/DecisionNode.html)`, `[Dependency](../mddependencies/Dependency.html)`, `[DeployedArtifact](../../deployments/mdnodes/DeployedArtifact.html)`, `[Deployment](../../deployments/mdnodes/Deployment.html)`, `[DeploymentSpecification](../../deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)`, `[DestroyLinkAction](../../actions/mdintermediateactions/DestroyLinkAction.html)`, `[DestroyObjectAction](../../actions/mdintermediateactions/DestroyObjectAction.html)`, `[DestructionOccurrenceSpecification](../../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[Diagram](Diagram.html)`, `[Duration](../../commonbehaviors/mdsimpletime/Duration.html)`, `[DurationConstraint](../../commonbehaviors/mdsimpletime/DurationConstraint.html)`, `[DurationInterval](../../commonbehaviors/mdsimpletime/DurationInterval.html)`, `[DurationObservation](../../commonbehaviors/mdsimpletime/DurationObservation.html)`, `[ElementValue](ElementValue.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](Enumeration.html)`, `[EnumerationLiteral](EnumerationLiteral.html)`, `[Event](../../commonbehaviors/mdcommunications/Event.html)`, `[ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[ExecutionOccurrenceSpecification](../../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html)`, `[ExecutionSpecification](../../interactions/mdbasicinteractions/ExecutionSpecification.html)`, `[ExpansionNode](../../activities/mdextrastructuredactivities/ExpansionNode.html)`, `[ExpansionRegion](../../activities/mdextrastructuredactivities/ExpansionRegion.html)`, `[Expression](Expression.html)`, `[Extend](../../mdusecases/Extend.html)`, `[Extension](../../mdprofiles/Extension.html)`, `[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[ExtensionPoint](../../mdusecases/ExtensionPoint.html)`, `[Feature](Feature.html)`, `[FinalNode](../../activities/mdintermediateactivities/FinalNode.html)`, `[FinalState](../../statemachines/mdbehaviorstatemachines/FinalState.html)`, `[FlowFinalNode](../../activities/mdintermediateactivities/FlowFinalNode.html)`, `[ForkNode](../../activities/mdintermediateactivities/ForkNode.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[Gate](../../interactions/mdfragments/Gate.html)`, `[GeneralizationSet](../mdpowertypes/GeneralizationSet.html)`, `[GeneralOrdering](../../interactions/mdbasicinteractions/GeneralOrdering.html)`, `[Include](../../mdusecases/Include.html)`, `[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)`, `[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)`, `[InitialNode](../../activities/mdbasicactivities/InitialNode.html)`, `[InputPin](../../actions/mdbasicactions/InputPin.html)`, `[InstanceSpecification](InstanceSpecification.html)`, `[InstanceValue](InstanceValue.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html)`, `[InteractionFragment](../../interactions/mdbasicinteractions/InteractionFragment.html)`, `[InteractionOperand](../../interactions/mdfragments/InteractionOperand.html)`, `[InteractionUse](../../interactions/mdfragments/InteractionUse.html)`, `[Interface](../mdinterfaces/Interface.html)`, `[InterfaceRealization](../mdinterfaces/InterfaceRealization.html)`, `[InterruptibleActivityRegion](../../activities/mdcompleteactivities/InterruptibleActivityRegion.html)`, `[Interval](../../commonbehaviors/mdsimpletime/Interval.html)`, `[IntervalConstraint](../../commonbehaviors/mdsimpletime/IntervalConstraint.html)`, `[InvocationAction](../../actions/mdbasicactions/InvocationAction.html)`, `[JoinNode](../../activities/mdintermediateactivities/JoinNode.html)`, `[Lifeline](../../interactions/mdbasicinteractions/Lifeline.html)`, `[LinkAction](../../actions/mdintermediateactions/LinkAction.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralNull](LiteralNull.html)`, `[LiteralReal](LiteralReal.html)`, `[LiteralSpecification](LiteralSpecification.html)`, `[LiteralString](LiteralString.html)`, `[LiteralUnlimitedNatural](LiteralUnlimitedNatural.html)`, `[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`, `[Manifestation](../../deployments/mdartifacts/Manifestation.html)`, `[MergeNode](../../activities/mdintermediateactivities/MergeNode.html)`, `[Message](../../interactions/mdbasicinteractions/Message.html)`, `[MessageEnd](../../interactions/mdbasicinteractions/MessageEnd.html)`, `[MessageEvent](../../commonbehaviors/mdcommunications/MessageEvent.html)`, `[MessageOccurrenceSpecification](../../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)`, `[Model](../../auxiliaryconstructs/mdmodels/Model.html)`, `[Namespace](Namespace.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)`, `[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)`, `[Observation](../../commonbehaviors/mdsimpletime/Observation.html)`, `[OccurrenceSpecification](../../interactions/mdbasicinteractions/OccurrenceSpecification.html)`, `[OpaqueAction](../../actions/mdbasicactions/OpaqueAction.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[OpaqueExpression](OpaqueExpression.html)`, `[Operation](Operation.html)`, `[OutputPin](../../actions/mdbasicactions/OutputPin.html)`, `[Package](Package.html)`, `[PackageableElement](PackageableElement.html)`, `[Parameter](Parameter.html)`, `[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)`, `[PartDecomposition](../../interactions/mdfragments/PartDecomposition.html)`, `[Pin](../../actions/mdbasicactions/Pin.html)`, `[Port](../../compositestructures/mdports/Port.html)`, `[PrimitiveType](PrimitiveType.html)`, `[Profile](../../mdprofiles/Profile.html)`, `[Property](Property.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`, `[Pseudostate](../../statemachines/mdbehaviorstatemachines/Pseudostate.html)`, `[RaiseExceptionAction](../../actions/mdstructuredactions/RaiseExceptionAction.html)`, `[ReadExtentAction](../../actions/mdcompleteactions/ReadExtentAction.html)`, `[ReadIsClassifiedObjectAction](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`, `[ReadLinkAction](../../actions/mdintermediateactions/ReadLinkAction.html)`, `[ReadLinkObjectEndAction](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html)`, `[ReadLinkObjectEndQualifierAction](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`, `[ReadSelfAction](../../actions/mdintermediateactions/ReadSelfAction.html)`, `[ReadStructuralFeatureAction](../../actions/mdintermediateactions/ReadStructuralFeatureAction.html)`, `[ReadVariableAction](../../actions/mdstructuredactions/ReadVariableAction.html)`, `[Realization](../mddependencies/Realization.html)`, `[Reception](../../commonbehaviors/mdcommunications/Reception.html)`, `[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)`, `[RedefinableElement](RedefinableElement.html)`, `[RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`, `[ReduceAction](../../actions/mdcompleteactions/ReduceAction.html)`, `[Region](../../statemachines/mdbehaviorstatemachines/Region.html)`, `[RemoveStructuralFeatureValueAction](../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`, `[RemoveVariableValueAction](../../actions/mdstructuredactions/RemoveVariableValueAction.html)`, `[ReplyAction](../../actions/mdcompleteactions/ReplyAction.html)`, `[SendObjectAction](../../actions/mdintermediateactions/SendObjectAction.html)`, `[SendSignalAction](../../actions/mdbasicactions/SendSignalAction.html)`, `[SequenceNode](../../activities/mdstructuredactivities/SequenceNode.html)`, `[Signal](../../commonbehaviors/mdcommunications/Signal.html)`, `[SignalEvent](../../commonbehaviors/mdcommunications/SignalEvent.html)`, `[StartClassifierBehaviorAction](../../actions/mdcompleteactions/StartClassifierBehaviorAction.html)`, `[StartObjectBehaviorAction](../../actions/mdcompleteactions/StartObjectBehaviorAction.html)`, `[State](../../statemachines/mdbehaviorstatemachines/State.html)`, `[StateInvariant](../../interactions/mdbasicinteractions/StateInvariant.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`, `[StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html)`, `[StructuralFeature](StructuralFeature.html)`, `[StructuralFeatureAction](../../actions/mdintermediateactions/StructuralFeatureAction.html)`, `[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[Substitution](../mddependencies/Substitution.html)`, `[TestIdentityAction](../../actions/mdintermediateactions/TestIdentityAction.html)`, `[TimeConstraint](../../commonbehaviors/mdsimpletime/TimeConstraint.html)`, `[TimeEvent](../../commonbehaviors/mdcommunications/TimeEvent.html)`, `[TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html)`, `[TimeInterval](../../commonbehaviors/mdsimpletime/TimeInterval.html)`, `[TimeObservation](../../commonbehaviors/mdsimpletime/TimeObservation.html)`, `[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`, `[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)`, `[Type](Type.html)`, `[TypedElement](TypedElement.html)`, `[UnmarshallAction](../../actions/mdcompleteactions/UnmarshallAction.html)`, `[Usage](../mddependencies/Usage.html)`, `[UseCase](../../mdusecases/UseCase.html)`, `[ValuePin](../../actions/mdbasicactions/ValuePin.html)`, `[ValueSpecification](ValueSpecification.html)`, `[ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html)`, `[Variable](../../activities/mdstructuredactivities/Variable.html)`, `[VariableAction](../../actions/mdstructuredactions/VariableAction.html)`, `[Vertex](../../statemachines/mdbehaviorstatemachines/Vertex.html)`, `[WriteLinkAction](../../actions/mdintermediateactions/WriteLinkAction.html)`, `[WriteStructuralFeatureAction](../../actions/mdintermediateactions/WriteStructuralFeatureAction.html)`, `[WriteVariableAction](../../actions/mdstructuredactions/WriteVariableAction.html)`

public interfaceNamedElementextends [Element](Element.html)

begin-user-doc 
 A representation of the model object '***Named Element***'.
 end-user-doc 
begin-model-doc 
 A NamedElement is an Element in a model that may have a name. The name may be given directly and/or via the use of a StringExpression.
 end-model-doc 
The following features are supported:
 [`*message Of Signature*`](#get_messageOfSignature())
[`*Client Dependency*`](#getClientDependency())
[`*Supplier Dependency*`](#getSupplierDependency())
[`*namespace Of Member*`](#get_namespaceOfMember())
[`*Namespace*`](#getNamespace())
[`*information Flow Of Information Source*`](#get_informationFlowOfInformationSource())
[`*information Flow Of Information Target*`](#get_informationFlowOfInformationTarget())
[`*Name*`](#getName())
[`*Name Expression*`](#getNameExpression())
[`*Qualified Name*`](#getQualifiedName())
[`*Visibility*`](#getVisibility())
[`*consider Ignore Fragment Of Message*`](#get_considerIgnoreFragmentOfMessage())
[`*time Observation Of Event*`](#get_timeObservationOfEvent())
[`*duration Observation Of Event*`](#get_durationObservationOfEvent())

See Also:
[`UMLPackage.getNamedElement()`](../../metadata/UMLPackage.html#getNamedElement())
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
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ConsiderIgnoreFragment](../../interactions/mdfragments/ConsiderIgnoreFragment.html)>`
`[get_considerIgnoreFragmentOfMessage](#get_considerIgnoreFragmentOfMessage())()`
Returns the value of the '***consider Ignore Fragment Of Message***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DurationObservation](../../commonbehaviors/mdsimpletime/DurationObservation.html)>`
`[get_durationObservationOfEvent](#get_durationObservationOfEvent())()`
Returns the value of the '***duration Observation Of Event***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)>`
`[get_informationFlowOfInformationSource](#get_informationFlowOfInformationSource())()`
Returns the value of the '***information Flow Of Information Source***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)>`
`[get_informationFlowOfInformationTarget](#get_informationFlowOfInformationTarget())()`
Returns the value of the '***information Flow Of Information Target***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Message](../../interactions/mdbasicinteractions/Message.html)>`
`[get_messageOfSignature](#get_messageOfSignature())()`
Returns the value of the '***message Of Signature***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Namespace](Namespace.html)>`
`[get_namespaceOfMember](#get_namespaceOfMember())()`
Returns the value of the '***namespace Of Member***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TimeObservation](../../commonbehaviors/mdsimpletime/TimeObservation.html)>`
`[get_timeObservationOfEvent](#get_timeObservationOfEvent())()`
Returns the value of the '***time Observation Of Event***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Dependency](../mddependencies/Dependency.html)>`
`[getClientDependency](#getClientDependency())()`
Returns the value of the '***Client Dependency***' reference list.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns the value of the '***Name***' attribute.
`[StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html)`
`[getNameExpression](#getNameExpression())()`
Returns the value of the '***Name Expression***' containment reference.
`[Namespace](Namespace.html)`
`[getNamespace](#getNamespace())()`
Returns the value of the '***Namespace***' reference.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQualifiedName](#getQualifiedName())()`
Returns the value of the '***Qualified Name***' attribute.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Dependency](../mddependencies/Dependency.html)>`
`[getSupplierDependency](#getSupplierDependency())()`
Returns the value of the '***Supplier Dependency***' reference list.
`[VisibilityKind](VisibilityKind.html)`
`[getVisibility](#getVisibility())()`
Returns the value of the '***Visibility***' attribute.
`boolean`
`[has_considerIgnoreFragmentOfMessage](#has_considerIgnoreFragmentOfMessage())()`

`boolean`
`[has_durationObservationOfEvent](#has_durationObservationOfEvent())()`

`boolean`
`[has_informationFlowOfInformationSource](#has_informationFlowOfInformationSource())()`

`boolean`
`[has_informationFlowOfInformationTarget](#has_informationFlowOfInformationTarget())()`

`boolean`
`[has_messageOfSignature](#has_messageOfSignature())()`

`boolean`
`[has_namespaceOfMember](#has_namespaceOfMember())()`

`boolean`
`[has_timeObservationOfEvent](#has_timeObservationOfEvent())()`

`boolean`
`[hasClientDependency](#hasClientDependency())()`
Returns the value of the '***Qualified Name***' attribute.
`boolean`
`[hasSupplierDependency](#hasSupplierDependency())()`

`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Name*`](#getName())' attribute.
`void`
`[setNameExpression](#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression))([StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html) value)`
Sets the value of the '[`*Name Expression*`](#getNameExpression())' containment reference.
`void`
`[setNamespace](#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Namespace](Namespace.html) value)`
Sets the value of the '[`*Namespace*`](#getNamespace())' reference.
`void`
`[setVisibility](#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))([VisibilityKind](VisibilityKind.html) value)`
Sets the value of the '[`*Visibility*`](#getVisibility())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
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
getClientDependency
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Dependency](../mddependencies/Dependency.html)> getClientDependency()
Returns the value of the '***Client Dependency***' reference list.
 The list contents are of type [`Dependency`](../mddependencies/Dependency.html).
 It is bidirectional and its opposite is '[`*Client*`](../mddependencies/Dependency.html#getClient())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates the Dependencies that reference this NamedElement as a client.
 end-model-doc
Returns:
the value of the '*Client Dependency*' reference list.
See Also:
[`UMLPackage.getNamedElement_ClientDependency()`](../../metadata/UMLPackage.html#getNamedElement_ClientDependency())
[`Dependency.getClient()`](../mddependencies/Dependency.html#getClient())
Model:
opposite="client" ordered="false"
Generated:
getSupplierDependency
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Dependency](../mddependencies/Dependency.html)> getSupplierDependency()
Returns the value of the '***Supplier Dependency***' reference list.
 The list contents are of type [`Dependency`](../mddependencies/Dependency.html).
 It is bidirectional and its opposite is '[`*Supplier*`](../mddependencies/Dependency.html#getSupplier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates the dependencies that reference the supplier.
 end-model-doc
Returns:
the value of the '*Supplier Dependency*' reference list.
See Also:
[`UMLPackage.getNamedElement_SupplierDependency()`](../../metadata/UMLPackage.html#getNamedElement_SupplierDependency())
[`Dependency.getSupplier()`](../mddependencies/Dependency.html#getSupplier())
Model:
opposite="supplier" ordered="false"
Generated:
get_informationFlowOfInformationSource
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)> get_informationFlowOfInformationSource()
Returns the value of the '***information Flow Of Information Source***' reference list.
 The list contents are of type [`InformationFlow`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html).
 It is bidirectional and its opposite is
 '[`*Information Source*`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationSource())'.
 begin-user-doc 
If the meaning of the '*information Flow Of Information Source*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Flow Of Information Source*' reference list.
See Also:
[`UMLPackage.getNamedElement__informationFlowOfInformationSource()`](../../metadata/UMLPackage.html#getNamedElement__informationFlowOfInformationSource())
[`InformationFlow.getInformationSource()`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationSource())
Model:
opposite="informationSource" ordered="false"
Generated:
get_informationFlowOfInformationTarget
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)> get_informationFlowOfInformationTarget()
Returns the value of the '***information Flow Of Information Target***' reference list.
 The list contents are of type [`InformationFlow`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html).
 It is bidirectional and its opposite is
 '[`*Information Target*`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationTarget())'.
 begin-user-doc 
If the meaning of the '*information Flow Of Information Target*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Flow Of Information Target*' reference list.
See Also:
[`UMLPackage.getNamedElement__informationFlowOfInformationTarget()`](../../metadata/UMLPackage.html#getNamedElement__informationFlowOfInformationTarget())
[`InformationFlow.getInformationTarget()`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationTarget())
Model:
opposite="informationTarget" ordered="false"
Generated:
get_messageOfSignature
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Message](../../interactions/mdbasicinteractions/Message.html)> get_messageOfSignature()
Returns the value of the '***message Of Signature***' reference list.
 The list contents are of type [`Message`](../../interactions/mdbasicinteractions/Message.html).
 It is bidirectional and its opposite is '[`*Signature*`](../../interactions/mdbasicinteractions/Message.html#getSignature())'.
 begin-user-doc 
If the meaning of the '*message Of Signature*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message Of Signature*' reference list.
See Also:
[`UMLPackage.getNamedElement__messageOfSignature()`](../../metadata/UMLPackage.html#getNamedElement__messageOfSignature())
[`Message.getSignature()`](../../interactions/mdbasicinteractions/Message.html#getSignature())
Model:
opposite="signature" ordered="false"
Generated:
get_namespaceOfMember
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Namespace](Namespace.html)> get_namespaceOfMember()
Returns the value of the '***namespace Of Member***' reference list.
 The list contents are of type [`Namespace`](Namespace.html).
 It is bidirectional and its opposite is '[`*Member*`](Namespace.html#getMember())'.
 begin-user-doc 
If the meaning of the '*namespace Of Member*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*namespace Of Member*' reference list.
See Also:
[`UMLPackage.getNamedElement__namespaceOfMember()`](../../metadata/UMLPackage.html#getNamedElement__namespaceOfMember())
[`Namespace.getMember()`](Namespace.html#getMember())
Model:
opposite="member" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getNamespace
@CheckForNull[Namespace](Namespace.html) getNamespace()
Returns the value of the '***Namespace***' reference.
 It is bidirectional and its opposite is '[`*Owned Member*`](Namespace.html#getOwnedMember())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the Namespace that owns the NamedElement.
 end-model-doc
Returns:
the value of the '*Namespace*' reference.
See Also:
[`setNamespace(Namespace)`](#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))
[`UMLPackage.getNamedElement_Namespace()`](../../metadata/UMLPackage.html#getNamedElement_Namespace())
[`Namespace.getOwnedMember()`](Namespace.html#getOwnedMember())
Model:
opposite="ownedMember" transient="true" volatile="true" derived="true" ordered="false"
Generated:
setNamespace
void setNamespace(@CheckForNull
 [Namespace](Namespace.html) value)
Sets the value of the '[`*Namespace*`](#getNamespace())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Namespace*' reference.
See Also:
[`getNamespace()`](#getNamespace())
Generated:
getName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Returns the value of the '***Name***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The name of the NamedElement.
 end-model-doc
Returns:
the value of the '*Name*' attribute.
See Also:
[`setName(String)`](#setName(java.lang.String))
[`UMLPackage.getNamedElement_Name()`](../../metadata/UMLPackage.html#getNamedElement_Name())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"
Generated:
setName
void setName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Name*`](#getName())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Name*' attribute.
See Also:
[`getName()`](#getName())
Generated:
getNameExpression
@CheckForNull[StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html) getNameExpression()
Returns the value of the '***Name Expression***' containment reference.
 It is bidirectional and its opposite is '[`*named Element Of Name Expression*`](../../auxiliaryconstructs/mdtemplates/StringExpression.html#get_namedElementOfNameExpression())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The StringExpression used to define the name of this NamedElement.
 end-model-doc
Returns:
the value of the '*Name Expression*' containment reference.
See Also:
[`setNameExpression(StringExpression)`](#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression))
[`UMLPackage.getNamedElement_NameExpression()`](../../metadata/UMLPackage.html#getNamedElement_NameExpression())
[`StringExpression.get_namedElementOfNameExpression()`](../../auxiliaryconstructs/mdtemplates/StringExpression.html#get_namedElementOfNameExpression())
Model:
opposite="_namedElementOfNameExpression" containment="true" resolveProxies="true" ordered="false"
Generated:
setNameExpression
void setNameExpression(@CheckForNull
 [StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html) value)
Sets the value of the '[`*Name Expression*`](#getNameExpression())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Name Expression*' containment reference.
See Also:
[`getNameExpression()`](#getNameExpression())
Generated:
getQualifiedName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQualifiedName()
Returns the value of the '***Qualified Name***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A name that allows the NamedElement to be identified within a hierarchy of nested Namespaces. It is constructed from the names of the containing Namespaces
 starting at the root of the hierarchy and ending with the name of the NamedElement itself.
 end-model-doc
Returns:
the value of the '*Qualified Name*' attribute.
See Also:
[`UMLPackage.getNamedElement_QualifiedName()`](../../metadata/UMLPackage.html#getNamedElement_QualifiedName())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getVisibility
@CheckForNull[VisibilityKind](VisibilityKind.html) getVisibility()
Returns the value of the '***Visibility***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Determines whether and how the NamedElement is visible outside its owning Namespace.
 end-model-doc
Returns:
the value of the '*Visibility*' attribute.
See Also:
[`setVisibility(VisibilityKind)`](#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))
[`UMLPackage.getNamedElement_Visibility()`](../../metadata/UMLPackage.html#getNamedElement_Visibility())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.NamedElementVisibilityKind" ordered="false"
Generated:
setVisibility
void setVisibility(@CheckForNull
 [VisibilityKind](VisibilityKind.html) value)
Sets the value of the '[`*Visibility*`](#getVisibility())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Visibility*' attribute.
See Also:
[`getVisibility()`](#getVisibility())
Generated:
get_durationObservationOfEvent
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DurationObservation](../../commonbehaviors/mdsimpletime/DurationObservation.html)> get_durationObservationOfEvent()
Returns the value of the '***duration Observation Of Event***' reference list.
 The list contents are of type [`DurationObservation`](../../commonbehaviors/mdsimpletime/DurationObservation.html).
 It is bidirectional and its opposite is '[`*Event*`](../../commonbehaviors/mdsimpletime/DurationObservation.html#getEvent())'.
 begin-user-doc 
If the meaning of the '*duration Observation Of Event*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*duration Observation Of Event*' reference list.
See Also:
[`UMLPackage.getNamedElement__durationObservationOfEvent()`](../../metadata/UMLPackage.html#getNamedElement__durationObservationOfEvent())
[`DurationObservation.getEvent()`](../../commonbehaviors/mdsimpletime/DurationObservation.html#getEvent())
Model:
opposite="event" ordered="false"
Generated:
get_timeObservationOfEvent
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TimeObservation](../../commonbehaviors/mdsimpletime/TimeObservation.html)> get_timeObservationOfEvent()
Returns the value of the '***time Observation Of Event***' reference list.
 The list contents are of type [`TimeObservation`](../../commonbehaviors/mdsimpletime/TimeObservation.html).
 It is bidirectional and its opposite is '[`*Event*`](../../commonbehaviors/mdsimpletime/TimeObservation.html#getEvent())'.
 begin-user-doc 
If the meaning of the '*time Observation Of Event*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*time Observation Of Event*' reference list.
See Also:
[`UMLPackage.getNamedElement__timeObservationOfEvent()`](../../metadata/UMLPackage.html#getNamedElement__timeObservationOfEvent())
[`TimeObservation.getEvent()`](../../commonbehaviors/mdsimpletime/TimeObservation.html#getEvent())
Model:
opposite="event" ordered="false"
Generated:
get_considerIgnoreFragmentOfMessage
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ConsiderIgnoreFragment](../../interactions/mdfragments/ConsiderIgnoreFragment.html)> get_considerIgnoreFragmentOfMessage()
Returns the value of the '***consider Ignore Fragment Of Message***' reference list.
 The list contents are of type [`ConsiderIgnoreFragment`](../../interactions/mdfragments/ConsiderIgnoreFragment.html).
 It is bidirectional and its opposite is '[`*Message*`](../../interactions/mdfragments/ConsiderIgnoreFragment.html#getMessage())'.
 begin-user-doc 
If the meaning of the '*consider Ignore Fragment Of Message*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*consider Ignore Fragment Of Message*' reference list.
See Also:
[`UMLPackage.getNamedElement__considerIgnoreFragmentOfMessage()`](../../metadata/UMLPackage.html#getNamedElement__considerIgnoreFragmentOfMessage())
[`ConsiderIgnoreFragment.getMessage()`](../../interactions/mdfragments/ConsiderIgnoreFragment.html#getMessage())
Model:
opposite="message" ordered="false"
Generated:
hasClientDependency
boolean hasClientDependency()
 throws javax.jmi.reflect.JmiException
Returns the value of the '***Qualified Name***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A name that allows the NamedElement to be identified within a hierarchy of nested Namespaces. It is constructed from the names of the containing Namespaces
 starting at the root of the hierarchy and ending with the name of the NamedElement itself.
 end-model-doc
Returns:
the value of the '*Qualified Name*' attribute.
Throws:
`javax.jmi.reflect.JmiException`
See Also:
[`UMLPackage.getNamedElement_QualifiedName()`](../../metadata/UMLPackage.html#getNamedElement_QualifiedName())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
hasSupplierDependency
boolean hasSupplierDependency()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationFlowOfInformationSource
boolean has_informationFlowOfInformationSource()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationFlowOfInformationTarget
boolean has_informationFlowOfInformationTarget()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_messageOfSignature
boolean has_messageOfSignature()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_namespaceOfMember
boolean has_namespaceOfMember()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_durationObservationOfEvent
boolean has_durationObservationOfEvent()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_timeObservationOfEvent
boolean has_timeObservationOfEvent()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_considerIgnoreFragmentOfMessage
boolean has_considerIgnoreFragmentOfMessage()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface NamedElement">Interface NamedElement</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code>, <code><a href="../../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code>, <code><a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code>, <code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a></code>, <code><a href="../../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></code>, <code><a href="../../activities/mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></code>, <code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code>, <code><a href="../../activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></code>, <code><a href="../../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code>, <code><a href="../../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></code>, <code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a></code>, <code><a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code>, <code><a href="../../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code>, <code><a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code>, <code><a href="../../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></code>, <code><a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code>, <code><a href="../../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code>, <code><a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code>, <code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code>, <code><a href="../../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code>, <code><a href="../../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code>, <code><a href="../../interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code>, <code><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></code>, <code><a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code>, <code><a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a></code>, <code><a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code>, <code><a href="../../interactions/mdfragments/Continuation.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Continuation</a></code>, <code><a href="../../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code>, <code><a href="../../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a></code>, <code><a href="../../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code>, <code><a href="../../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code>, <code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code>, <code><a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code>, <code><a href="../../deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a></code>, <code><a href="../../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code>, <code><a href="../../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code>, <code><a href="../../interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></code>, <code><a href="ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code>, <code><a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../interactions/mdbasicinteractions/ExecutionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionOccurrenceSpecification</a></code>, <code><a href="../../interactions/mdbasicinteractions/ExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ExecutionSpecification</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code>, <code><a href="../../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></code>, <code><a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code>, <code><a href="../../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></code>, <code><a href="../../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></code>, <code><a href="../mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></code>, <code><a href="../../interactions/mdbasicinteractions/GeneralOrdering.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">GeneralOrdering</a></code>, <code><a href="../../mdusecases/Include.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Include</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></code>, <code><a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code>, <code><a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code>, <code><a href="InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code>, <code><a href="../../interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a></code>, <code><a href="../../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></code>, <code><a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code>, <code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code>, <code><a href="../../activities/mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code>, <code><a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code>, <code><a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code>, <code><a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code>, <code><a href="../../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code>, <code><a href="LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code>, <code><a href="LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code>, <code><a href="LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code>, <code><a href="LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></code>, <code><a href="LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code>, <code><a href="LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code>, <code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="../../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code>, <code><a href="../../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code>, <code><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code>, <code><a href="../../interactions/mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></code>, <code><a href="../../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a></code>, <code><a href="../../interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></code>, <code><a href="../../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code>, <code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code>, <code><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a></code>, <code><a href="../../interactions/mdbasicinteractions/OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a></code>, <code><a href="../../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code>, <code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code>, <code><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code>, <code><a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code>, <code><a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></code>, <code><a href="../../interactions/mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></code>, <code><a href="../../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code>, <code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></code>, <code><a href="../../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code>, <code><a href="../mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code>, <code><a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code>, <code><a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code>, <code><a href="../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code>, <code><a href="../../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code>, <code><a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code>, <code><a href="../../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code>, <code><a href="../../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code>, <code><a href="../../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code>, <code><a href="../../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code>, <code><a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code>, <code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code>, <code><a href="../../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code>, <code><a href="../../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></code>, <code><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code>, <code><a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code>, <code><a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code>, <code><a href="../mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code>, <code><a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code>, <code><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code>, <code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code>, <code><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code>, <code><a href="../../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code>, <code><a href="../../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code>, <code><a href="../../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">NamedElement</span><span class="extends-implements">
extends <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Named Element</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A NamedElement is an Element in a model that may have a name. The name may be given directly and/or via the use of a StringExpression.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_messageOfSignature()"><code><em>message Of Signature</em></code></a></li>
<li><a href="#getClientDependency()"><code><em>Client Dependency</em></code></a></li>
<li><a href="#getSupplierDependency()"><code><em>Supplier Dependency</em></code></a></li>
<li><a href="#get_namespaceOfMember()"><code><em>namespace Of Member</em></code></a></li>
<li><a href="#getNamespace()"><code><em>Namespace</em></code></a></li>
<li><a href="#get_informationFlowOfInformationSource()"><code><em>information Flow Of Information Source</em></code></a></li>
<li><a href="#get_informationFlowOfInformationTarget()"><code><em>information Flow Of Information Target</em></code></a></li>
<li><a href="#getName()"><code><em>Name</em></code></a></li>
<li><a href="#getNameExpression()"><code><em>Name Expression</em></code></a></li>
<li><a href="#getQualifiedName()"><code><em>Qualified Name</em></code></a></li>
<li><a href="#getVisibility()"><code><em>Visibility</em></code></a></li>
<li><a href="#get_considerIgnoreFragmentOfMessage()"><code><em>consider Ignore Fragment Of Message</em></code></a></li>
<li><a href="#get_timeObservationOfEvent()"><code><em>time Observation Of Event</em></code></a></li>
<li><a href="#get_durationObservationOfEvent()"><code><em>duration Observation Of Event</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getNamedElement()"><code>UMLPackage.getNamedElement()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>consider Ignore Fragment Of Message</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>duration Observation Of Event</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Flow Of Information Source</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Flow Of Information Target</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageOfSignature()">get_messageOfSignature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message Of Signature</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_namespaceOfMember()">get_namespaceOfMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>namespace Of Member</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>time Observation Of Event</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClientDependency()">getClientDependency</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Client Dependency</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNameExpression()">getNameExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Name Expression</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNamespace()">getNamespace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Namespace</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getQualifiedName()">getQualifiedName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Qualified Name</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSupplierDependency()">getSupplierDependency</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Supplier Dependency</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVisibility()">getVisibility</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Visibility</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_messageOfSignature()">has_messageOfSignature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_namespaceOfMember()">has_namespaceOfMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasClientDependency()">hasClientDependency</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Qualified Name</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSupplierDependency()">hasSupplierDependency</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getName()"><code><em>Name</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a><wbr/>(<a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getNameExpression()"><code><em>Name Expression</em></code></a>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a><wbr/>(<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getNamespace()"><code><em>Namespace</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a><wbr/>(<a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getVisibility()"><code><em>Visibility</em></code></a>' attribute.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
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
<section class="detail" id="getClientDependency()">
<h3>getClientDependency</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt;</span> <span class="element-name">getClientDependency</span>()</div>
<div class="block">Returns the value of the '<em><b>Client Dependency</b></em>' reference list.
 The list contents are of type <a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a>.
 It is bidirectional and its opposite is '<a href="../mddependencies/Dependency.html#getClient()"><code><em>Client</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates the Dependencies that reference this NamedElement as a client.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Client Dependency</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement_ClientDependency()"><code>UMLPackage.getNamedElement_ClientDependency()</code></a></li>
<li><a href="../mddependencies/Dependency.html#getClient()"><code>Dependency.getClient()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="client" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierDependency()">
<h3>getSupplierDependency</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt;</span> <span class="element-name">getSupplierDependency</span>()</div>
<div class="block">Returns the value of the '<em><b>Supplier Dependency</b></em>' reference list.
 The list contents are of type <a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Dependency</code></a>.
 It is bidirectional and its opposite is '<a href="../mddependencies/Dependency.html#getSupplier()"><code><em>Supplier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates the dependencies that reference the supplier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Supplier Dependency</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement_SupplierDependency()"><code>UMLPackage.getNamedElement_SupplierDependency()</code></a></li>
<li><a href="../mddependencies/Dependency.html#getSupplier()"><code>Dependency.getSupplier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="supplier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationFlowOfInformationSource()">
<h3>get_informationFlowOfInformationSource</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</span> <span class="element-name">get_informationFlowOfInformationSource</span>()</div>
<div class="block">Returns the value of the '<em><b>information Flow Of Information Source</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationSource()"><code><em>Information Source</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Flow Of Information Source</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Flow Of Information Source</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__informationFlowOfInformationSource()"><code>UMLPackage.getNamedElement__informationFlowOfInformationSource()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationSource()"><code>InformationFlow.getInformationSource()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="informationSource" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationFlowOfInformationTarget()">
<h3>get_informationFlowOfInformationTarget</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</span> <span class="element-name">get_informationFlowOfInformationTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>information Flow Of Information Target</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationTarget()"><code><em>Information Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Flow Of Information Target</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Flow Of Information Target</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__informationFlowOfInformationTarget()"><code>UMLPackage.getNamedElement__informationFlowOfInformationTarget()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getInformationTarget()"><code>InformationFlow.getInformationTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="informationTarget" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageOfSignature()">
<h3>get_messageOfSignature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</span> <span class="element-name">get_messageOfSignature</span>()</div>
<div class="block">Returns the value of the '<em><b>message Of Signature</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Message.html#getSignature()"><code><em>Signature</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message Of Signature</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message Of Signature</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__messageOfSignature()"><code>UMLPackage.getNamedElement__messageOfSignature()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Message.html#getSignature()"><code>Message.getSignature()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="signature" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_namespaceOfMember()">
<h3>get_namespaceOfMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt;</span> <span class="element-name">get_namespaceOfMember</span>()</div>
<div class="block">Returns the value of the '<em><b>namespace Of Member</b></em>' reference list.
 The list contents are of type <a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Namespace</code></a>.
 It is bidirectional and its opposite is '<a href="Namespace.html#getMember()"><code><em>Member</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>namespace Of Member</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>namespace Of Member</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__namespaceOfMember()"><code>UMLPackage.getNamedElement__namespaceOfMember()</code></a></li>
<li><a href="Namespace.html#getMember()"><code>Namespace.getMember()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="member" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNamespace()">
<h3>getNamespace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></span> <span class="element-name">getNamespace</span>()</div>
<div class="block">Returns the value of the '<em><b>Namespace</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Namespace.html#getOwnedMember()"><code><em>Owned Member</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the Namespace that owns the NamedElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Namespace</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)"><code>setNamespace(Namespace)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getNamedElement_Namespace()"><code>UMLPackage.getNamedElement_Namespace()</code></a></li>
<li><a href="Namespace.html#getOwnedMember()"><code>Namespace.getOwnedMember()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedMember" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>setNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setNamespace</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getNamespace()"><code><em>Namespace</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Namespace</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getNamespace()"><code>getNamespace()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns the value of the '<em><b>Name</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The name of the NamedElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setName(java.lang.String)"><code>setName(String)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getNamedElement_Name()"><code>UMLPackage.getNamedElement_Name()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getName()"><code><em>Name</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getName()"><code>getName()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameExpression()">
<h3>getNameExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></span> <span class="element-name">getNameExpression</span>()</div>
<div class="block">Returns the value of the '<em><b>Name Expression</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html#get_namedElementOfNameExpression()"><code><em>named Element Of Name Expression</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The StringExpression used to define the name of this NamedElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Name Expression</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)"><code>setNameExpression(StringExpression)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getNamedElement_NameExpression()"><code>UMLPackage.getNamedElement_NameExpression()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html#get_namedElementOfNameExpression()"><code>StringExpression.get_namedElementOfNameExpression()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_namedElementOfNameExpression" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">
<h3>setNameExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setNameExpression</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getNameExpression()"><code><em>Name Expression</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Name Expression</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getNameExpression()"><code>getNameExpression()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedName()">
<h3>getQualifiedName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedName</span>()</div>
<div class="block">Returns the value of the '<em><b>Qualified Name</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A name that allows the NamedElement to be identified within a hierarchy of nested Namespaces. It is constructed from the names of the containing Namespaces
 starting at the root of the hierarchy and ending with the name of the NamedElement itself.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Qualified Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement_QualifiedName()"><code>UMLPackage.getNamedElement_QualifiedName()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibility()">
<h3>getVisibility</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a></span> <span class="element-name">getVisibility</span>()</div>
<div class="block">Returns the value of the '<em><b>Visibility</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Determines whether and how the NamedElement is visible outside its owning Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Visibility</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)"><code>setVisibility(VisibilityKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getNamedElement_Visibility()"><code>UMLPackage.getNamedElement_Visibility()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.NamedElementVisibilityKind" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">
<h3>setVisibility</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setVisibility</span><wbr/><span class="parameters">(@CheckForNull
 <a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getVisibility()"><code><em>Visibility</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Visibility</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getVisibility()"><code>getVisibility()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_durationObservationOfEvent()">
<h3>get_durationObservationOfEvent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a>&gt;</span> <span class="element-name">get_durationObservationOfEvent</span>()</div>
<div class="block">Returns the value of the '<em><b>duration Observation Of Event</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>DurationObservation</code></a>.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdsimpletime/DurationObservation.html#getEvent()"><code><em>Event</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>duration Observation Of Event</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>duration Observation Of Event</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__durationObservationOfEvent()"><code>UMLPackage.getNamedElement__durationObservationOfEvent()</code></a></li>
<li><a href="../../commonbehaviors/mdsimpletime/DurationObservation.html#getEvent()"><code>DurationObservation.getEvent()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="event" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_timeObservationOfEvent()">
<h3>get_timeObservationOfEvent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a>&gt;</span> <span class="element-name">get_timeObservationOfEvent</span>()</div>
<div class="block">Returns the value of the '<em><b>time Observation Of Event</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>TimeObservation</code></a>.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdsimpletime/TimeObservation.html#getEvent()"><code><em>Event</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>time Observation Of Event</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>time Observation Of Event</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__timeObservationOfEvent()"><code>UMLPackage.getNamedElement__timeObservationOfEvent()</code></a></li>
<li><a href="../../commonbehaviors/mdsimpletime/TimeObservation.html#getEvent()"><code>TimeObservation.getEvent()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="event" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_considerIgnoreFragmentOfMessage()">
<h3>get_considerIgnoreFragmentOfMessage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">ConsiderIgnoreFragment</a>&gt;</span> <span class="element-name">get_considerIgnoreFragmentOfMessage</span>()</div>
<div class="block">Returns the value of the '<em><b>consider Ignore Fragment Of Message</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>ConsiderIgnoreFragment</code></a>.
 It is bidirectional and its opposite is '<a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html#getMessage()"><code><em>Message</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>consider Ignore Fragment Of Message</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>consider Ignore Fragment Of Message</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement__considerIgnoreFragmentOfMessage()"><code>UMLPackage.getNamedElement__considerIgnoreFragmentOfMessage()</code></a></li>
<li><a href="../../interactions/mdfragments/ConsiderIgnoreFragment.html#getMessage()"><code>ConsiderIgnoreFragment.getMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="message" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasClientDependency()">
<h3>hasClientDependency</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasClientDependency</span>()
                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<div class="block">Returns the value of the '<em><b>Qualified Name</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A name that allows the NamedElement to be identified within a hierarchy of nested Namespaces. It is constructed from the names of the containing Namespaces
 starting at the root of the hierarchy and ending with the name of the NamedElement itself.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Qualified Name</em>' attribute.</dd>
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamedElement_QualifiedName()"><code>UMLPackage.getNamedElement_QualifiedName()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSupplierDependency()">
<h3>hasSupplierDependency</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSupplierDependency</span>()
                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationFlowOfInformationSource()">
<h3>has_informationFlowOfInformationSource</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationFlowOfInformationSource</span>()
                                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationFlowOfInformationTarget()">
<h3>has_informationFlowOfInformationTarget</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationFlowOfInformationTarget</span>()
                                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_messageOfSignature()">
<h3>has_messageOfSignature</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_messageOfSignature</span>()
                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_namespaceOfMember()">
<h3>has_namespaceOfMember</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_namespaceOfMember</span>()
                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_durationObservationOfEvent()">
<h3>has_durationObservationOfEvent</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_durationObservationOfEvent</span>()
                                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_timeObservationOfEvent()">
<h3>has_timeObservationOfEvent</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_timeObservationOfEvent</span>()
                            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_considerIgnoreFragmentOfMessage()">
<h3>has_considerIgnoreFragmentOfMessage</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_considerIgnoreFragmentOfMessage</span>()
                                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
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
