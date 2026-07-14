# JAVA OPENAPI: InteractionHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/jmi/helpers/InteractionHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/InteractionHelper.html`
- source_sha256: `56f65a15380d7411fedd4d027b72b0e70caa4c9632b278f167a8f892497156f7`
- captured_utc: `2026-07-14T16:56:08.882607+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class InteractionHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.helpers.InteractionHelper

@OpenApiAllpublic classInteractionHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Helper methods for dealing with model in interactions (sequence).

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[KEEP_ALL_OPERATION](#KEEP_ALL_OPERATION)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[InteractionHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html)`
`[addParameterForOperation](#addParameterForOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String,boolean))([Operation](../../magicdraw/classes/mdkernel/Operation.html) operation,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean generateName)`

`static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html)`
`[addParameterForOperation](#addParameterForOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind))([Operation](../../magicdraw/classes/mdkernel/Operation.html) operation,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean generateName,
 [ParameterDirectionKind](../../magicdraw/classes/mdkernel/ParameterDirectionKind.html) directionKind)`
Adds a parameter to an operation with a given name.
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[addPropertyForSignal](#addPropertyForSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,java.lang.String,boolean))([Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean generateName)`

`static boolean`
`[canChangeMessageType](#canChangeMessageType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if this message can change its type.
`static void`
`[changeSynchForMessage](#changeSynchForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Change synch for message.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructMessageText](#constructMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 boolean showParameters)`
Deprecated.
use [`ModelTextCreator.createMessageText(Message, MessageTextParams, Supplier)`](../../../../magicdraw/uml/text/ModelTextCreator.html#createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier))
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createArgumentForMessage](#createArgumentForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Type](../../magicdraw/classes/mdkernel/Type.html) type)`
Creates an argument for a message.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createArgumentForMessage](#createArgumentForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Type](../../magicdraw/classes/mdkernel/Type.html) type,
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) defaultValue)`
Creates an argument for a message.
`static void`
`[createArgumentsForCallMessage](#createArgumentsForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Creates the arguments for call message.
`static [Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html)`
`[createDuration](#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint))([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) dc)`
Deprecated.
use [`createDuration(DurationInterval, boolean)`](#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean))
`static [Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html)`
`[createDuration](#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean))([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) interval,
 boolean createObservation)`
Create duration for duration interval min or max.
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[createProperty](#createProperty(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [Interaction](../../magicdraw/interactions/mdbasicinteractions/Interaction.html) inter)`
Creates property into interaction for the lifeline use.
`static [MessageOccurrenceSpecification](../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html)`
`[createReceiveEventByMessageSort](#createReceiveEventByMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Creates receive event occurrence according message sort
`static [TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html)`
`[createTimeExpression](#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint))([TimeConstraint](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) tc)`
Deprecated.
use [`createTimeExpression(TimeInterval, boolean)`](#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean))
`static [TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html)`
`[createTimeExpression](#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean))([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) timeInterval,
 boolean createObservation)`
Creates time expression for give time interval min or max.
`static void`
`[disposeMessageArguments](#disposeMessageArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Dispose message arguments.
`static void`
`[enableExecutionSpecificationModeling](#enableExecutionSpecificationModeling(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](../../../../magicdraw/uml/symbols/DiagramPresentationElement.html) diagramPresentationElement)`
Enable ExecutionSpecification modeling in given Sequence diagram.
`static boolean`
`[ensureDestructionOccurrence](#ensureDestructionOccurrence(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,boolean))([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline,
 boolean destruct)`
Ensures that a proper destruction occurrence is in the model on this lifeline.
`static void`
`[ensureFragmentsAreInFragmentCollection](#ensureFragmentsAreInFragmentCollection(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)> collection,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)> fragments)`
Ensures that fragments are in given fragment collection.
`static [Operation](../../magicdraw/classes/mdkernel/Operation.html)`
`[findCallOperation](#findCallOperation(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.List,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> preferredOperations,
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Find call operation.
`static [Operation](../../magicdraw/classes/mdkernel/Operation.html)`
`[findCallOperationWithArguments](#findCallOperationWithArguments(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.List,int,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> preferredOperations,
 int paramCount,
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Find call operation, which has closest parameter count.
`static [Interaction](../../magicdraw/interactions/mdbasicinteractions/Interaction.html)`
`[findInteraction](#findInteraction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) interactionElement)`
Finds interaction for a given interaction element.
`static [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[findSignalForMessage](#findSignalForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Find signal for message.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[getArgumentSupportedValueSpecifications](#getArgumentSupportedValueSpecifications())()`
Get argument supported value specification classes.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)>`
`[getAvailableOperationsForCallMessage](#getAvailableOperationsForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets operations which are available to select for a call message.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html)>`
`[getAvailableSignals](#getAvailableSignals(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets all available signals to select for a message.
`static [DestructionOccurrenceSpecification](../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`
`[getDestructionOccurrenceSpecification](#getDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)`
Gets destruction occurrence specification from a given lifeline.
`static [DestructionOccurrenceSpecification](../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html)`
`[getDestructionOccurrenceSpecification](#getDestructionOccurrenceSpecification(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)> collection)`
Gets destruction occurrence specification from a given lifeline.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[getIntervalMinMax](#getIntervalMinMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint))([IntervalConstraint](../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) interval)`
Returns min and max values.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[]`
`[getIntervalMinMaxValues](#getIntervalMinMaxValues(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint))([IntervalConstraint](../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) interval)`
Returns min and max values.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html)>`
`[getLifelines](#getLifelines(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Returns lifelines that are covered by given message
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getLifelineType](#getLifelineType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)`
Gets the lifeline type.
`static [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getMessage](#getMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate))([Gate](../../magicdraw/interactions/mdfragments/Gate.html) gate)`
Returns message, to which this gate is connected.
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getMessageEndClassifier](#getMessageEndClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 boolean client)`
Returns classifier - receiver of message.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Message](../../magicdraw/interactions/mdbasicinteractions/Message.html)>`
`[getMessages](#getMessages(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)`
Return all connected messages from given lifeline.
`static [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getMessageSubstitute](#getMessageSubstitute(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Returns message substitute for given message or the given message, if no substitution found.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getNestedNumberAsString](#getNestedNumberAsString(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) number)`
Gets the nested number as string.
`static [Operation](../../magicdraw/classes/mdkernel/Operation.html)`
`[getOperationOfCallMessage](#getOperationOfCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets the operation of call message.
`static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html)`
`[getOperationParameterByName](#getOperationParameterByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String))([Operation](../../magicdraw/classes/mdkernel/Operation.html) op,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Finds parameter from the operation by given name
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)>`
`[getOperations](#getOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Returns all operations for call actions
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)>`
`[getOperationsForCallAction](#getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)>`
`[getOperationsForCallAction](#getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
`static [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Gate](../../magicdraw/interactions/mdfragments/Gate.html)>`
`[getPairableGate](#getPairableGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,boolean))([CombinedFragment](../../magicdraw/interactions/mdfragments/CombinedFragment.html) fragment,
 boolean replayMessage)`
Gets iterator of Gates, which can be used to be formal pair of the gate.
`static [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Gate](../../magicdraw/interactions/mdfragments/Gate.html)>`
`[getPairableGate](#getPairableGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean))([InteractionUse](../../magicdraw/interactions/mdfragments/InteractionUse.html) use,
 boolean replayMessage)`
Gets iterator of Gates, which can be used to be formal pair of the gate.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getReceiveElement](#getReceiveElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets the receive element.
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getReceiverClassifier](#getReceiverClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Returns classifier - receiver of message.
`static [ConnectableElement](../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html)`
`[getRemovableConnectableElement](#getRemovableConnectableElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)`
Check if the represents can be removed along with lifeline.
`static [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getReplyMessage](#getReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Return receive event holder of the given message.
`static int`
`[getReturnParameterPosition](#getReturnParameterPosition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](../../magicdraw/classes/mdkernel/Operation.html) operation)`
Gets the return parameter position.
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getSendClassifier](#getSendClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Returns classifier - receiver of message.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getSendElement](#getSendElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Return send event holder of the given message.
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[getSignalAttributeByName](#getSignalAttributeByName(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,java.lang.String))([Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[getSignalAttributeForArgument](#getSignalAttributeForArgument(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) argument)`
Gets signal attribute if it exists for a given message argument.
`static [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[getSignalOfMessage](#getSignalOfMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Gets the signal of message.
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getStateInvariantClassifier](#getStateInvariantClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant))([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant)`
Gets classifier which is related to a given state invariant through a lifeline.
`static [Constraint](../../magicdraw/classes/mdkernel/Constraint.html)`
`[getStateInvariantConstraint](#getStateInvariantConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,boolean))([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant,
 boolean create)`
Gets state invariant constraint from state invariant.
`static [State](../../magicdraw/statemachines/mdbehaviorstatemachines/State.html)`
`[getStateInvariantState](#getStateInvariantState(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant))([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant)`
Retrieves state which is set to a given state invariant.
`static void`
`[initCoveredInfo](#initCoveredInfo(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html) fragment,
 [Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)`
Initializes the covered info.
`static void`
`[initMessage](#initMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Element](../../magicdraw/classes/mdkernel/Element.html) source,
 [Element](../../magicdraw/classes/mdkernel/Element.html) target)`
Initializes message by the given source and target.
`static void`
`[initMessage](#initMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) source,
 [Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) target)`
Initializes the message.
`static void`
`[initOperationForCallMessage](#initOperationForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation)`
Init the operation for call message.
`static boolean`
`[isCallMessage](#isCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if message is a call message.
`static boolean`
`[isCreateMessage](#isCreateMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if is creates the message.
`static boolean`
`[isDestroyMessage](#isDestroyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if is destroy message.
`static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isFirstEvent](#isFirstEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) constraint,
 [Element](../../magicdraw/classes/mdkernel/Element.html) constrainedElement)`
Returns firstEvent value for a given constrained element by index.
`static boolean`
`[isFoundMessage](#isFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if given message is a found message.
`static boolean`
`[isInsideMessage](#isInsideMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [CombinedFragment](../../magicdraw/interactions/mdfragments/CombinedFragment.html) fragment)`
Checks if given message is inside the fragment.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[isLifelinePort](#isLifelinePort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if lifeline from message supplier is port and exists in lifeline context.
`static boolean`
`[isLostMessage](#isLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if given message is a lost message.
`static boolean`
`[isNotGate](#isNotGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if message send end is Gate (Message send from diagram border)
`static boolean`
`[isReplyMessage](#isReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Indicates if this message is a reply message.
`static boolean`
`[isSendMessage](#isSendMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if is send message.
`static boolean`
`[isSynchMessage](#isSynchMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Checks if is synch message.
`static void`
`[makeFoundMessage](#makeFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Turns a message to a found message by removing its sending end
 and setting necessary properties.
`static void`
`[makeLostMessage](#makeLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
Turns a message to a lost message by removing its receiving end
 and setting necessary properties.
`static void`
`[makeMessageOperationCallable](#makeMessageOperationCallable(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)`
If message is not call, makes it call.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[parseArgumentName](#parseArgumentName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Parses argument from parameter=argument tuple.
`static void`
`[parseArguments](#parseArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Parses arguments from string and sets them as message arguments.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[parseParameterName](#parseParameterName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Parses parameter from parameter=argument tuple.
`static int`
`[removeReturnParameter](#removeReturnParameter(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) parameters)`
Removes the return parameter.
`static void`
`[setDurationInterval](#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,java.lang.String))([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) durationConstraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax)`
Sets duration interval data.
`static void`
`[setDurationInterval](#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,java.lang.String,java.lang.String))([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) dc,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue)`
Sets duration interval.
`static void`
`[setDurationInterval](#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,java.lang.String,boolean))([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) durationInterval,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax,
 boolean createObservation)`
Sets duration interval value.
`static void`
`[setDurationInterval](#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,java.lang.String,java.lang.String,boolean))([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) interval,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue,
 boolean createObservation)`
Sets duration interval.
`static void`
`[setDurationOwner](#setDurationOwner(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html) duration,
 [Element](../../magicdraw/classes/mdkernel/Element.html) findParentFrom)`
Sets the duration owner.
`static void`
`[setEventForDuration](#setEventForDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement))([Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html) duration,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event1,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event2)`
Sets events for first DurationObservation referenced by given Duration.
`static void`
`[setEventForDurationInterval](#setEventForDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean))([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) interval,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event1,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event2,
 boolean createObservations)`
Sets events for DurationInterval min and max durations.
`static void`
`[setEventForTimeExpression](#setEventForTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement))([TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) timeExpression,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event)`
Sets event for first time observation referenced by a given time expression.
`static void`
`[setEventForTimeInterval](#setEventForTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean))([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) interval,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event,
 boolean createObservation)`
Sets event for Time Interval min and max expressions.
`static void`
`[setFirstEvent](#setFirstEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) constraint,
 [Element](../../magicdraw/classes/mdkernel/Element.html) constrainedElement,
 boolean value)`
Sets firstEvent value for a given constrained element
 Does nothing if given element is not a constrained element or firstEvent list size is out of sync with constrainedElement list size.
`static void`
`[setGuard](#setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) guard)`
Sets the guard.
`static void`
`[setLifelineType](#setLifelineType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline,
 [Type](../../magicdraw/classes/mdkernel/Type.html) type)`
Sets the lifeline type.
`static void`
`[setMessageArguments](#setMessageArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.List))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> arguments)`
Sets the message arguments.
`static void`
`[setMessageSort](#setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [MessageSort](../../magicdraw/interactions/mdbasicinteractions/MessageSort.html) sort)`
Changes message sort by the given one.
`static void`
`[setOperationForMessage](#setOperationForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation,
 boolean createArguments)`
Sets the operation for message.
`static void`
`[setReturnValue](#setReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the return value.
`static void`
`[setReturnValueForMessage](#setReturnValueForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the return value for message.
`static void`
`[setSignalForMessage](#setSignalForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal)`
Sets the signal for message.
`static void`
`[setStateForStateInvariant](#setStateForStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,boolean))([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant,
 [State](../../magicdraw/statemachines/mdbehaviorstatemachines/State.html) state,
 boolean createConstraintIfNecessary)`
Sets state for state invariant to represent.
`static void`
`[setTarget](#setTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String))([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) target)`
Sets the target.
`static void`
`[setTimeExpressionOwner](#setTimeExpressionOwner(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) timeExpression,
 [Element](../../magicdraw/classes/mdkernel/Element.html) findParentFrom)`
Sets the time expression owner.
`static void`
`[setTimeInterval](#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,java.lang.String))([TimeConstraint](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) timeConstraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax)`
Sets time interval for a time constraint.
`static void`
`[setTimeInterval](#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,java.lang.String,java.lang.String))([TimeConstraint](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) timeConstraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue)`
Sets time interval for a given time constraint.
`static void`
`[setTimeInterval](#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,java.lang.String,boolean))([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) timeInterval,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax,
 boolean createObservation)`
Sets time interval data.
`static void`
`[setTimeInterval](#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,java.lang.String,java.lang.String,boolean))([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) timeInterval,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue,
 boolean createObservation)`
Sets time interval data.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
KEEP_ALL_OPERATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) KEEP_ALL_OPERATION
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.InteractionHelper.KEEP_ALL_OPERATION)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
InteractionHelper
public InteractionHelper()
 ============ METHOD DETAIL ========== 
Method Details
isLostMessage
public static boolean isLostMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if given message is a lost message.
Parameters:
`message` - message to check.
Returns:
true if given message is a lost message, false otherwise.
isFoundMessage
public static boolean isFoundMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if given message is a found message.
Parameters:
`message` - message to check.
Returns:
true if given message is a found message, false otherwise.
isSendMessage
public static boolean isSendMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if is send message.
Parameters:
`message` - the message
Returns:
true, if is send message
isSynchMessage
public static boolean isSynchMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if is synch message.
Parameters:
`message` - the message
Returns:
true, if is synch message
isDestroyMessage
public static boolean isDestroyMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if is destroy message.
Parameters:
`message` - the message
Returns:
true, if is destroy message
isReplyMessage
public static boolean isReplyMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if this message is a reply message.
Parameters:
`message` - - message to check.
Returns:
true if this is a reply message, false otherwise.
isCallMessage
public static boolean isCallMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Indicates if message is a call message.
Parameters:
`message` - - message to check.
Returns:
true if this message is a call message, false otherwise.
isCreateMessage
public static boolean isCreateMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if is creates the message.
Parameters:
`message` - the message
Returns:
true, if is creates the message
canChangeMessageType
public static boolean canChangeMessageType([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if this message can change its type. This is not possible if message does not have receive event.
Parameters:
`message` - message to check.
Returns:
true if message can change type, false otherwise.
getReceiverClassifier
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getReceiverClassifier([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Returns classifier - receiver of message.
Parameters:
`message` - message
Returns:
classifier
getSendClassifier
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getSendClassifier([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Returns classifier - receiver of message.
Parameters:
`message` - message
Returns:
classifier
getMessageEndClassifier
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getMessageEndClassifier([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 boolean client)
Returns classifier - receiver of message.
Parameters:
`message` - message
`client` - the client
Returns:
classifier
makeMessageOperationCallable
public static void makeMessageOperationCallable([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
If message is not call, makes it call.
Parameters:
`message` - message to check.
changeSynchForMessage
public static void changeSynchForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Change synch for message.
Parameters:
`message` - the message
setMessageSort
public static void setMessageSort([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [MessageSort](../../magicdraw/interactions/mdbasicinteractions/MessageSort.html) sort)
Changes message sort by the given one.
 
**NOTE** Message must have parent
Parameters:
`message` - Given message, to change sort
`sort` - Given sort kind, one from MessageSortEnum
See Also:
[`MessageSortEnum`](../../magicdraw/interactions/mdbasicinteractions/MessageSortEnum.html)
initMessage
public static void initMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) source,
 [Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) target)
Initializes the message.
Parameters:
`message` - the message
`source` - the source
`target` - the target
createReceiveEventByMessageSort
public static [MessageOccurrenceSpecification](../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html) createReceiveEventByMessageSort([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Creates receive event occurrence according message sort
Parameters:
`message` - message
Returns:
MessageOccurrenceSpecification
initCoveredInfo
public static void initCoveredInfo([InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html) fragment,
 [Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)
Initializes the covered info.
Parameters:
`fragment` - the fragment
`lifeline` - the lifeline
findInteraction
@CheckForNullpublic static [Interaction](../../magicdraw/interactions/mdbasicinteractions/Interaction.html) findInteraction(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) interactionElement)
Finds interaction for a given interaction element.
Parameters:
`interactionElement` - an element in an interaction.
Returns:
interaction to which a given interaction element is related.
initMessage
public static void initMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) source,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) target)
Initializes message by the given source and target.
 If source or target is of type Lifeline, then is created additionally MessageOccurrenceSpecification and covered by Lifeline
 If source or target is of type CombinedFragment, InteractionUse or Interaction,
 then is created additionally Gate as MessageEnd. Gate is not covered by any lifeline
Parameters:
`message` - message
`source` - source
`target` - target
makeLostMessage
public static void makeLostMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Turns a message to a lost message by removing its receiving end
 and setting necessary properties.
Parameters:
`message` - message to turn into a lost message.
makeFoundMessage
public static void makeFoundMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Turns a message to a found message by removing its sending end
 and setting necessary properties.
Parameters:
`message` - message to turn into a found message.
constructMessageText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructMessageText([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 boolean showParameters)
Deprecated.
use [`ModelTextCreator.createMessageText(Message, MessageTextParams, Supplier)`](../../../../magicdraw/uml/text/ModelTextCreator.html#createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier))
getMessageSubstitute
public static [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) getMessageSubstitute([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Returns message substitute for given message or the given message, if no substitution found. Message substitution
 is message found by the formal gate.
Parameters:
`message` - message, for which substitution will be searched
Returns:
given message if no substitution found
getOperationOfCallMessage
@CheckForNullpublic static [Operation](../../magicdraw/classes/mdkernel/Operation.html) getOperationOfCallMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets the operation of call message.
Parameters:
`message` - the message
Returns:
the operation of call message
getSignalOfMessage
@CheckForNullpublic static [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) getSignalOfMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets the signal of message.
Parameters:
`message` - the message
Returns:
the signal of message
getSignalAttributeForArgument
@CheckForNullpublic static [Property](../../magicdraw/classes/mdkernel/Property.html) getSignalAttributeForArgument([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) argument)
Gets signal attribute if it exists for a given message argument.
Parameters:
`argument` - argument for which to retrieve signal attribute.
Returns:
signal attribute related to the given argument if found, null otherwise.
setOperationForMessage
public static void setOperationForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation,
 boolean createArguments)
Sets the operation for message.
Parameters:
`message` - the message
`operation` - the operation
`createArguments` - the create arguments
setSignalForMessage
public static void setSignalForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal)
Sets the signal for message.
Parameters:
`message` - the message
`signal` - the signal
findSignalForMessage
@CheckForNullpublic static [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) findSignalForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Find signal for message.
Parameters:
`message` - the message
`name` - the name
Returns:
the signal
getAvailableOperationsForCallMessage
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> getAvailableOperationsForCallMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets operations which are available to select for a call message.
Parameters:
`message` - message for which to get available operations for selection.
Returns:
available operations.
getOperationsForCallAction
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> getOperationsForCallAction(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
Parameters:
`classifier` - classifier
Returns:
classifiers
getOperationsForCallAction
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> getOperationsForCallAction(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 @CheckForNull
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
Parameters:
`classifier` - classifier
`message` - call message
Returns:
classifiers
getOperations
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> getOperations(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 @CheckForNull
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Returns all operations for call actions
Parameters:
`classifier` - classifier from which we select operations
Returns:
operation set
isNotGate
public static boolean isNotGate(@CheckForNull
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if message send end is Gate (Message send from diagram border)
Parameters:
`message` - message
Returns:
true if is not Gate, else false
isLifelinePort
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) isLifelinePort(@CheckForNull
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Checks if lifeline from message supplier is port and exists in lifeline context.
Parameters:
`message` - message
Returns:
true if is port else false
getLifelines
@CheckForNullpublic static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html)> getLifelines(@CheckForNull
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Returns lifelines that are covered by given message
Parameters:
`message` - message
Returns:
lifelines that are covered by given message, null if no lifeline is covered
findCallOperationWithArguments
@CheckForNullpublic static [Operation](../../magicdraw/classes/mdkernel/Operation.html) findCallOperationWithArguments([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> preferredOperations,
 int paramCount,
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Find call operation, which has closest parameter count. Sometimes there are few operations with same names,
 but different parameter count - this function returns operation by name and closest match by paramCount.
Parameters:
`name` - the name
`classifier` - the classifier
`preferredOperations` - list of preferred operations
`paramCount` - preferred parameter count
`message` - call message
Returns:
the operation
findCallOperation
@CheckForNullpublic static [Operation](../../magicdraw/classes/mdkernel/Operation.html) findCallOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> preferredOperations,
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Find call operation.
Parameters:
`name` - the name
`classifier` - the classifier
`preferredOperations` - the preferred operations
`message` - call message
Returns:
the operation
createArgumentsForCallMessage
public static void createArgumentsForCallMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Creates the arguments for call message.
Parameters:
`message` - the message
createArgumentForMessage
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createArgumentForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Type](../../magicdraw/classes/mdkernel/Type.html) type)
Creates an argument for a message.
Parameters:
`message` - message for which to create an argument.
`type` - type of the argument.
Returns:
created argument for message.
createArgumentForMessage
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createArgumentForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) type,
 @CheckForNull
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) defaultValue)
Creates an argument for a message.
 Uses the passed default value to initialize the argument.
Parameters:
`message` - message for which to create an argument.
`type` - type of the argument.
`defaultValue` - default value for the argument.
Returns:
created argument for message.
getArgumentSupportedValueSpecifications
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> getArgumentSupportedValueSpecifications()
Get argument supported value specification classes.
Returns:
value specification classes.
getNestedNumberAsString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getNestedNumberAsString([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) number)
Gets the nested number as string.
Parameters:
`number` - the number
Returns:
the nested number as string
createProperty
public static [Property](../../magicdraw/classes/mdkernel/Property.html) createProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [Interaction](../../magicdraw/interactions/mdbasicinteractions/Interaction.html) inter)
Creates property into interaction for the lifeline use.
Parameters:
`propertyName` - name
`type` - type
`inter` - interaction
Returns:
created property
disposeMessageArguments
public static void disposeMessageArguments([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Dispose message arguments.
Parameters:
`message` - the message
setMessageArguments
public static void setMessageArguments([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> arguments)
 throws [ParseException](../../../../magicdraw/utils/parsers/ParseException.html)
Sets the message arguments.
Parameters:
`message` - the message
`arguments` - the arguments
Throws:
`[ParseException](../../../../magicdraw/utils/parsers/ParseException.html)` - the parse exception
removeReturnParameter
public static int removeReturnParameter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) parameters)
Removes the return parameter.
Parameters:
`parameters` - the parameters
Returns:
the int
setTarget
public static void setTarget([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) target)
Sets the target.
Parameters:
`message` - the message
`target` - the target
setGuard
public static void setGuard([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) guard)
Sets the guard.
Parameters:
`message` - the message
`guard` - the guard
getReceiveElement
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getReceiveElement([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets the receive element.
Parameters:
`message` - the message
Returns:
the receive element
getSendElement
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getSendElement([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Return send event holder of the given message.
 It can be:
 covered lifeline
 gate owner (Interaction, CombinedFragment, InteractionUse)
Parameters:
`message` - Given message, which will be analysed
Returns:
One of Lifeline, Interaction, CombinedFragment, InteractionUse.
 Can return null, if message has no send event
getReplyMessage
public static [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) getReplyMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Return receive event holder of the given message.
 It can be:
 covered lifeline
 gate owner (Interaction, CombinedFragment, InteractionUse)
Parameters:
`message` - Given message, which will be analysed
Returns:
One of Lifeline, Interaction, CombinedFragment, InteractionUse.
 Can return null, if message has no receive event
setReturnValue
public static void setReturnValue([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the return value.
Parameters:
`message` - the message
`value` - the value
getReturnParameterPosition
public static int getReturnParameterPosition(@CheckForNull
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation)
Gets the return parameter position.
Parameters:
`operation` - the operation
Returns:
the return parameter position
setReturnValueForMessage
public static void setReturnValueForMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the return value for message.
Parameters:
`message` - the message
`value` - the value
parseArguments
public static void parseArguments([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Parses arguments from string and sets them as message arguments.
Parameters:
`message` - message
`s` - string to parse
initOperationForCallMessage
public static void initOperationForCallMessage([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 @CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 @CheckForNull
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation)
Init the operation for call message.
Parameters:
`message` - the message
`classifier` - the classifier
`operation` - the op
setLifelineType
public static void setLifelineType([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) type)
Sets the lifeline type.
Parameters:
`lifeline` - the lifeline
`type` - the type
getStateInvariantClassifier
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getStateInvariantClassifier([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant)
Gets classifier which is related to a given state invariant through a lifeline.
Parameters:
`stateInvariant` - state invariant for which classifier should found.
Returns:
classifier if found, null otherwise.
getLifelineType
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getLifelineType([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)
Gets the lifeline type.
Parameters:
`lifeline` - the lifeline
Returns:
the lifeline type
getRemovableConnectableElement
@CheckForNullpublic static [ConnectableElement](../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html) getRemovableConnectableElement([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)
Check if the represents can be removed along with lifeline.
Parameters:
`lifeline` - lifeline
Returns:
connectible element that should be disposed
setTimeInterval
public static void setTimeInterval([TimeConstraint](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) timeConstraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue)
Sets time interval for a given time constraint.
Parameters:
`timeConstraint` - time constraint to modify.
`minValue` - min value.
`maxValue` - max value.
setTimeInterval
public static void setTimeInterval([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) timeInterval,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue,
 boolean createObservation)
Sets time interval data.
Parameters:
`timeInterval` - time interval to modify.
`minValue` - min value.
`maxValue` - max value.
`createObservation` - indicates if observation should be created.
setTimeInterval
public static void setTimeInterval([TimeConstraint](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) timeConstraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax)
Sets time interval for a time constraint.
 String is of type lower..higher values.
Parameters:
`timeConstraint` - constraint constraint for which to set time interval.
`minMax` - min..max format value.
setTimeInterval
public static void setTimeInterval([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) timeInterval,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax,
 boolean createObservation)
Sets time interval data.
 String is of type lower..higher values.
Parameters:
`timeInterval` - time interval to modify.
`minMax` - min..max format value.
`createObservation` - indicates if observation should be created.
setDurationInterval
public static void setDurationInterval([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) durationConstraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax)
Sets duration interval data.
 String is of type lower..higher values.
Parameters:
`durationConstraint` - duration constraint to set.
`minMax` - min..max format value.
setDurationInterval
public static void setDurationInterval([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) durationInterval,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minMax,
 boolean createObservation)
Sets duration interval value.
 String is of type lower..higher values.
Parameters:
`durationInterval` - duration interval to modify.
`minMax` - min..max format value.
`createObservation` - indicates if observation should be created.
createTimeExpression
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) createTimeExpression([TimeConstraint](../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) tc)
Deprecated.
use [`createTimeExpression(TimeInterval, boolean)`](#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean))
Creates time expression.
Parameters:
`tc` - constraint
Returns:
expression
createTimeExpression
public static [TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) createTimeExpression([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) timeInterval,
 boolean createObservation)
Creates time expression for give time interval min or max.
Parameters:
`timeInterval` - interval
`createObservation` - create observation
Returns:
expression
setTimeExpressionOwner
public static void setTimeExpressionOwner([TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) timeExpression,
 [Element](../../magicdraw/classes/mdkernel/Element.html) findParentFrom)
Sets the time expression owner.
Parameters:
`timeExpression` - the time expression
`findParentFrom` - the find parent from
getIntervalMinMax
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] getIntervalMinMax([IntervalConstraint](../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) interval)
Returns min and max values. If not exist - can be null
Parameters:
`interval` - interval
Returns:
min max values
getIntervalMinMaxValues
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] getIntervalMinMaxValues([IntervalConstraint](../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html) interval)
Returns min and max values. If not exist - can be null
Parameters:
`interval` - interval
Returns:
min max values
createDuration
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html) createDuration([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) dc)
Deprecated.
use [`createDuration(DurationInterval, boolean)`](#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean))
Creates duration with appropriate DurationObservationAction and min and max values.
Parameters:
`dc` - constraint
Returns:
constraint
createDuration
public static [Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html) createDuration([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) interval,
 boolean createObservation)
Create duration for duration interval min or max.
Parameters:
`interval` - interval
`createObservation` - create observation
Returns:
duration
setDurationOwner
public static void setDurationOwner([Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html) duration,
 [Element](../../magicdraw/classes/mdkernel/Element.html) findParentFrom)
Sets the duration owner.
Parameters:
`duration` - the duration
`findParentFrom` - the find parent from
setDurationInterval
public static void setDurationInterval([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) dc,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue)
Sets duration interval.
Parameters:
`dc` - constraint
`minValue` - min value
`maxValue` - max value
setDurationInterval
public static void setDurationInterval([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) interval,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) minValue,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) maxValue,
 boolean createObservation)
Sets duration interval.
Parameters:
`interval` - interval
`minValue` - min value
`maxValue` - max value
`createObservation` - create observation
isInsideMessage
public static boolean isInsideMessage(@CheckForNull
 [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [CombinedFragment](../../magicdraw/interactions/mdfragments/CombinedFragment.html) fragment)
Checks if given message is inside the fragment. Check
 - if given message has one end with the same covered lifeline as `fragment` does
 - if given message has one end to the nested fragment
 
 Message is expected to have one end connected to `fragment`
Parameters:
`message` - Message to check if ii is inside
`fragment` - Check if given message is inside THIS fragment
Returns:
true if given message is inside the given fragment
getMessage
@CheckForNullpublic static [Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) getMessage([Gate](../../magicdraw/interactions/mdfragments/Gate.html) gate)
Returns message, to which this gate is connected.
Parameters:
`gate` - given gate to check message
Returns:
Message, which is connected to the gate
getPairableGate
public static [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Gate](../../magicdraw/interactions/mdfragments/Gate.html)> getPairableGate([InteractionUse](../../magicdraw/interactions/mdfragments/InteractionUse.html) use,
 boolean replayMessage)
Gets iterator of Gates, which can be used to be formal pair of the gate.
Parameters:
`use` - given interaction use
`replayMessage` - if true, than all messages will be returned which are pairable for replay message kind
Returns:
Iterator of gates. Not null.
getPairableGate
public static [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Gate](../../magicdraw/interactions/mdfragments/Gate.html)> getPairableGate([CombinedFragment](../../magicdraw/interactions/mdfragments/CombinedFragment.html) fragment,
 boolean replayMessage)
Gets iterator of Gates, which can be used to be formal pair of the gate. The are : all gates, which are originated
 by inside messages of given fragment. Inside message must have at least one end which would cover lifeline,
 covered by given fragment
Parameters:
`fragment` - given interaction fragment
`replayMessage` - if true, than all messages will be returned which are pairable for replay message kind
Returns:
Iterator of gates. Not null.
setEventForTimeExpression
public static void setEventForTimeExpression([TimeExpression](../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html) timeExpression,
 @CheckForNull
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event)
Sets event for first time observation referenced by a given time expression.
 If time expression does not reference any time observation, call is ignored.
Parameters:
`timeExpression` - time expression to modify.
`event` - event to set.
setEventForTimeInterval
public static void setEventForTimeInterval([TimeInterval](../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html) interval,
 @CheckForNull
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event,
 boolean createObservation)
Sets event for Time Interval min and max expressions. Creates min and max expressions if needed.
Parameters:
`interval` - time interval
`event` - event
`createObservation` - if true create TimeObservation if min and max expressions are created
setEventForDuration
public static void setEventForDuration([Duration](../../magicdraw/commonbehaviors/mdsimpletime/Duration.html) duration,
 @CheckForNull
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event1,
 @CheckForNull
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event2)
Sets events for first DurationObservation referenced by given Duration. If Duration do no reference any DurationObservation, call is ignored.
Parameters:
`duration` - duration
`event1` - event or null
`event2` - event or null
setEventForDurationInterval
public static void setEventForDurationInterval([DurationInterval](../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html) interval,
 @CheckForNull
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event1,
 @CheckForNull
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) event2,
 boolean createObservations)
Sets events for DurationInterval min and max durations. Creates min and max durations if needed
Parameters:
`interval` - duration interval
`event1` - event or null
`event2` - event or null
`createObservations` - if true create DurationObservation if min and max durations are created
setStateForStateInvariant
public static void setStateForStateInvariant([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant,
 [State](../../magicdraw/statemachines/mdbehaviorstatemachines/State.html) state,
 boolean createConstraintIfNecessary)
Sets state for state invariant to represent.
Parameters:
`stateInvariant` - state invariant for which state should be set.
`state` - state which should be set to state invariant.
`createConstraintIfNecessary` - creates constraint if constraint doesn't exist in a state invariant.
getStateInvariantConstraint
@CheckForNullpublic static [Constraint](../../magicdraw/classes/mdkernel/Constraint.html) getStateInvariantConstraint([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant,
 boolean create)
Gets state invariant constraint from state invariant.
Parameters:
`stateInvariant` - state invariant from which to get state invariant constraint.
`create` - true if a new constraint should be created when no constraints are found.
Returns:
invariant constraint if found or new created, null if no constraint found.
getStateInvariantState
@CheckForNullpublic static [State](../../magicdraw/statemachines/mdbehaviorstatemachines/State.html) getStateInvariantState([StateInvariant](../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html) stateInvariant)
Retrieves state which is set to a given state invariant.
Parameters:
`stateInvariant` - state invariant for which state should be retrieved.
Returns:
state if found, null otherwise.
getMessages
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Message](../../magicdraw/interactions/mdbasicinteractions/Message.html)> getMessages([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)
Return all connected messages from given lifeline.
Parameters:
`lifeline` - lifeline
Returns:
all messages connected to this lifeline.
parseParameterName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parseParameterName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Parses parameter from parameter=argument tuple.
Parameters:
`text` - text to parse.
Returns:
parsed parameter name.
parseArgumentName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parseArgumentName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Parses argument from parameter=argument tuple.
Parameters:
`text` - text to parse.
Returns:
parsed argument name.
addParameterForOperation
@CheckForNullpublic static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html) addParameterForOperation([Operation](../../magicdraw/classes/mdkernel/Operation.html) operation,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean generateName)
addParameterForOperation
@CheckForNullpublic static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html) addParameterForOperation([Operation](../../magicdraw/classes/mdkernel/Operation.html) operation,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean generateName,
 [ParameterDirectionKind](../../magicdraw/classes/mdkernel/ParameterDirectionKind.html) directionKind)
Adds a parameter to an operation with a given name.
Parameters:
`operation` - operation for which to add a parameter.
`name` - name to set.
`generateName` - indicates whether name should be generated if given name is empty.
`directionKind` - parameter direction
Returns:
created parameter.
addPropertyForSignal
@CheckForNullpublic static [Property](../../magicdraw/classes/mdkernel/Property.html) addPropertyForSignal([Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean generateName)
getOperationParameterByName
@CheckForNullpublic static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html) getOperationParameterByName([Operation](../../magicdraw/classes/mdkernel/Operation.html) op,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Finds parameter from the operation by given name
Parameters:
`op` - provided operation
`name` - name for the parameter
Returns:
parameter or null
getSignalAttributeByName
@CheckForNullpublic static [Property](../../magicdraw/classes/mdkernel/Property.html) getSignalAttributeByName([Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
ensureFragmentsAreInFragmentCollection
public static void ensureFragmentsAreInFragmentCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)> collection,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)> fragments)
Ensures that fragments are in given fragment collection.
Parameters:
`collection` - collection to check.
`fragments` - fragments to add to the fragment collection.
getAvailableSignals
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html)> getAvailableSignals([Message](../../magicdraw/interactions/mdbasicinteractions/Message.html) message)
Gets all available signals to select for a message.
Parameters:
`message` - message for which to retrieve all available signals.
Returns:
available signals for a message.
getDestructionOccurrenceSpecification
@CheckForNullpublic static [DestructionOccurrenceSpecification](../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) getDestructionOccurrenceSpecification([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline)
Gets destruction occurrence specification from a given lifeline.
Parameters:
`lifeline` - lifeline for which to get destruction occurrence specification.
Returns:
destruction occurrence specification if found any, null otherwise.
getDestructionOccurrenceSpecification
@CheckForNullpublic static [DestructionOccurrenceSpecification](../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html) getDestructionOccurrenceSpecification([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html)> collection)
Gets destruction occurrence specification from a given lifeline.
Parameters:
`collection` - collection in which to search for destruction occurrence.
Returns:
destruction occurrence specification if found any, null otherwise.
ensureDestructionOccurrence
public static boolean ensureDestructionOccurrence([Lifeline](../../magicdraw/interactions/mdbasicinteractions/Lifeline.html) lifeline,
 boolean destruct)
Ensures that a proper destruction occurrence is in the model on this lifeline.
Parameters:
`lifeline` - lifeline for which to ensure destruction occurrence.
`destruct` - indicates whether lifeline is destructed or not.
Returns:
true if destruction event was changed
enableExecutionSpecificationModeling
public static void enableExecutionSpecificationModeling([DiagramPresentationElement](../../../../magicdraw/uml/symbols/DiagramPresentationElement.html) diagramPresentationElement)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html),
[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Enable ExecutionSpecification modeling in given Sequence diagram.
Parameters:
`diagramPresentationElement` - sequence diagram.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if diagram is not sequence diagram.
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created at the current moment, or diagram is not loaded.
setFirstEvent
public static void setFirstEvent([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) constraint,
 [Element](../../magicdraw/classes/mdkernel/Element.html) constrainedElement,
 boolean value)
Sets firstEvent value for a given constrained element
 Does nothing if given element is not a constrained element or firstEvent list size is out of sync with constrainedElement list size.
Parameters:
`constraint` - constraint
`constrainedElement` - constrained element
`value` - firstEvent value
isFirstEvent
@CheckForNullpublic static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isFirstEvent([DurationConstraint](../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) constraint,
 [Element](../../magicdraw/classes/mdkernel/Element.html) constrainedElement)
Returns firstEvent value for a given constrained element by index.
Parameters:
`constraint` - constraint
`constrainedElement` - constrained element
Returns:
value or null if given element is not a constrained element or firstEvent list size is out of the sync with constrainedElement list size

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class InteractionHelper">Class InteractionHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.InteractionHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">InteractionHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helper methods for dealing with model in interactions (sequence).</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#KEEP_ALL_OPERATION">KEEP_ALL_OPERATION</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">InteractionHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addParameterForOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String,boolean)">addParameterForOperation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean generateName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addParameterForOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind)">addParameterForOperation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean generateName,
 <a href="../../magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> directionKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds a parameter to an operation with a given name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyForSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,java.lang.String,boolean)">addPropertyForSignal</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean generateName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeMessageType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">canChangeMessageType</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if this message can change its type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#changeSynchForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">changeSynchForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Change synch for message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#constructMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean)">constructMessageText</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 boolean showParameters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../magicdraw/uml/text/ModelTextCreator.html#createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createMessageText(Message, MessageTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createArgumentForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">createArgumentForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an argument for a message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createArgumentForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">createArgumentForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> defaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an argument for a message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createArgumentsForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">createArgumentsForCallMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the arguments for call message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint)">createDuration</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> dc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean)"><code>createDuration(DurationInterval, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean)">createDuration</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> interval,
 boolean createObservation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create duration for duration interval min or max.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createProperty(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">createProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> inter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates property into interaction for the lifeline use.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createReceiveEventByMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">createReceiveEventByMessageSort</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates receive event occurrence according message sort</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)">createTimeExpression</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> tc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean)"><code>createTimeExpression(TimeInterval, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean)">createTimeExpression</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> timeInterval,
 boolean createObservation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates time expression for give time interval min or max.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeMessageArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">disposeMessageArguments</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dispose message arguments.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#enableExecutionSpecificationModeling(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">enableExecutionSpecificationModeling</a><wbr/>(<a href="../../../../magicdraw/uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Enable ExecutionSpecification modeling in given Sequence diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureDestructionOccurrence(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,boolean)">ensureDestructionOccurrence</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline,
 boolean destruct)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Ensures that a proper destruction occurrence is in the model on this lifeline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureFragmentsAreInFragmentCollection(java.util.Collection,java.util.Collection)">ensureFragmentsAreInFragmentCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt; fragments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Ensures that fragments are in given fragment collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findCallOperation(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.List,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">findCallOperation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt; preferredOperations,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find call operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findCallOperationWithArguments(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.List,int,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">findCallOperationWithArguments</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt; preferredOperations,
 int paramCount,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find call operation, which has closest parameter count.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findInteraction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findInteraction</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> interactionElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds interaction for a given interaction element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findSignalForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">findSignalForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find signal for message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getArgumentSupportedValueSpecifications()">getArgumentSupportedValueSpecifications</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get argument supported value specification classes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAvailableOperationsForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getAvailableOperationsForCallMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets operations which are available to select for a call message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAvailableSignals(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getAvailableSignals</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets all available signals to select for a message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">getDestructionOccurrenceSpecification</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets destruction occurrence specification from a given lifeline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDestructionOccurrenceSpecification(java.util.Collection)">getDestructionOccurrenceSpecification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets destruction occurrence specification from a given lifeline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntervalMinMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">getIntervalMinMax</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> interval)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns min and max values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntervalMinMaxValues(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">getIntervalMinMaxValues</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> interval)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns min and max values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLifelines(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getLifelines</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns lifelines that are covered by given message</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLifelineType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">getLifelineType</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the lifeline type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)">getMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> gate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns message, to which this gate is connected.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageEndClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean)">getMessageEndClassifier</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 boolean client)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns classifier - receiver of message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessages(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">getMessages</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return all connected messages from given lifeline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageSubstitute(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getMessageSubstitute</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns message substitute for given message or the given message, if no substitution found.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNestedNumberAsString(java.util.List)">getNestedNumberAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> number)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the nested number as string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationOfCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getOperationOfCallMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the operation of call message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationParameterByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String)">getOperationParameterByName</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> op,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds parameter from the operation by given name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getOperations</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all operations for call actions</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getOperationsForCallAction</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getOperationsForCallAction</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPairableGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,boolean)">getPairableGate</a><wbr/>(<a href="../../magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> fragment,
 boolean replayMessage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets iterator of Gates, which can be used to be formal pair of the gate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPairableGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean)">getPairableGate</a><wbr/>(<a href="../../magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> use,
 boolean replayMessage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets iterator of Gates, which can be used to be formal pair of the gate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReceiveElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getReceiveElement</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the receive element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReceiverClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getReceiverClassifier</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns classifier - receiver of message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemovableConnectableElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">getRemovableConnectableElement</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if the represents can be removed along with lifeline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getReplyMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return receive event holder of the given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReturnParameterPosition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">getReturnParameterPosition</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the return parameter position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSendClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getSendClassifier</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns classifier - receiver of message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSendElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getSendElement</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return send event holder of the given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalAttributeByName(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,java.lang.String)">getSignalAttributeByName</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalAttributeForArgument(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getSignalAttributeForArgument</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> argument)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets signal attribute if it exists for a given message argument.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalOfMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">getSignalOfMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the signal of message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateInvariantClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">getStateInvariantClassifier</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets classifier which is related to a given state invariant through a lifeline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateInvariantConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,boolean)">getStateInvariantConstraint</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant,
 boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets state invariant constraint from state invariant.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateInvariantState(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">getStateInvariantState</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves state which is set to a given state invariant.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initCoveredInfo(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">initCoveredInfo</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a> fragment,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes the covered info.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">initMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes message by the given source and target.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">initMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> source,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes the message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initOperationForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">initOperationForCallMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Init the operation for call message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isCallMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if message is a call message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isCreateMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is creates the message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDestroyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isDestroyMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is destroy message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFirstEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFirstEvent</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> constraint,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> constrainedElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns firstEvent value for a given constrained element by index.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isFoundMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if given message is a found message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInsideMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">isInsideMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> fragment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given message is inside the fragment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLifelinePort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isLifelinePort</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if lifeline from message supplier is port and exists in lifeline context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isLostMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if given message is a lost message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNotGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isNotGate</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if message send end is Gate (Message send from diagram border)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isReplyMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if this message is a reply message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSendMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isSendMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is send message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSynchMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">isSynchMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if is synch message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#makeFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">makeFoundMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Turns a message to a found message by removing its sending end
 and setting necessary properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#makeLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">makeLostMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Turns a message to a lost message by removing its receiving end
 and setting necessary properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#makeMessageOperationCallable(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">makeMessageOperationCallable</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If message is not call, makes it call.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseArgumentName(java.lang.String)">parseArgumentName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses argument from parameter=argument tuple.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">parseArguments</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses arguments from string and sets them as message arguments.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseParameterName(java.lang.String)">parseParameterName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses parameter from parameter=argument tuple.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeReturnParameter(java.util.List)">removeReturnParameter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> parameters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the return parameter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,java.lang.String)">setDurationInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> durationConstraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets duration interval data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,java.lang.String,java.lang.String)">setDurationInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> dc,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets duration interval.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,java.lang.String,boolean)">setDurationInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> durationInterval,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax,
 boolean createObservation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets duration interval value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,java.lang.String,java.lang.String,boolean)">setDurationInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> interval,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue,
 boolean createObservation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets duration interval.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setDurationOwner(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setDurationOwner</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> duration,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> findParentFrom)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the duration owner.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEventForDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">setEventForDuration</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> duration,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event1,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets events for first DurationObservation referenced by given Duration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEventForDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">setEventForDurationInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> interval,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event1,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event2,
 boolean createObservations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets events for DurationInterval min and max durations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEventForTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">setEventForTimeExpression</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> timeExpression,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets event for first time observation referenced by a given time expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEventForTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">setEventForTimeInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> interval,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event,
 boolean createObservation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets event for Time Interval min and max expressions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFirstEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">setFirstEvent</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> constraint,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> constrainedElement,
 boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets firstEvent value for a given constrained element
 Does nothing if given element is not a constrained element or firstEvent list size is out of sync with constrainedElement list size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">setGuard</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> guard)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the guard.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLifelineType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setLifelineType</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the lifeline type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMessageArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.List)">setMessageArguments</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; arguments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the message arguments.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)">setMessageSort</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/interactions/mdbasicinteractions/MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> sort)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Changes message sort by the given one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOperationForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean)">setOperationForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean createArguments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the operation for message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">setReturnValue</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the return value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReturnValueForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">setReturnValueForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the return value for message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSignalForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">setSignalForMessage</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the signal for message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStateForStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,boolean)">setStateForStateInvariant</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant,
 <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> state,
 boolean createConstraintIfNecessary)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets state for state invariant to represent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">setTarget</a><wbr/>(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the target.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeExpressionOwner(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setTimeExpressionOwner</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> timeExpression,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> findParentFrom)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the time expression owner.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,java.lang.String)">setTimeInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> timeConstraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets time interval for a time constraint.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,java.lang.String,java.lang.String)">setTimeInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> timeConstraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets time interval for a given time constraint.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,java.lang.String,boolean)">setTimeInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> timeInterval,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax,
 boolean createObservation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets time interval data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,java.lang.String,java.lang.String,boolean)">setTimeInterval</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> timeInterval,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue,
 boolean createObservation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets time interval data.</div>
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
<section class="detail" id="KEEP_ALL_OPERATION">
<h3>KEEP_ALL_OPERATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">KEEP_ALL_OPERATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.InteractionHelper.KEEP_ALL_OPERATION">Constant Field Values</a></li>
</ul>
</dd>
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
<h3>InteractionHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">InteractionHelper</span>()</div>
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
<section class="detail" id="isLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isLostMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLostMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if given message is a lost message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to check.</dd>
<dt>Returns:</dt>
<dd>true if given message is a lost message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isFoundMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFoundMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if given message is a found message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to check.</dd>
<dt>Returns:</dt>
<dd>true if given message is a found message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSendMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isSendMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSendMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if is send message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>true, if is send message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSynchMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isSynchMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSynchMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if is synch message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>true, if is synch message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDestroyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isDestroyMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDestroyMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if is destroy message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>true, if is destroy message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isReplyMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isReplyMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if this message is a reply message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - - message to check.</dd>
<dt>Returns:</dt>
<dd>true if this is a reply message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isCallMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCallMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Indicates if message is a call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - - message to check.</dd>
<dt>Returns:</dt>
<dd>true if this message is a call message, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isCreateMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreateMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if is creates the message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>true, if is creates the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeMessageType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>canChangeMessageType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canChangeMessageType</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if this message can change its type. This is not possible if message does not have receive event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to check.</dd>
<dt>Returns:</dt>
<dd>true if message can change type, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReceiverClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getReceiverClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getReceiverClassifier</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Returns classifier - receiver of message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dt>Returns:</dt>
<dd>classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getSendClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getSendClassifier</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Returns classifier - receiver of message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dt>Returns:</dt>
<dd>classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageEndClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean)">
<h3>getMessageEndClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getMessageEndClassifier</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 boolean client)</span></div>
<div class="block">Returns classifier - receiver of message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dd><code>client</code> - the client</dd>
<dt>Returns:</dt>
<dd>classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeMessageOperationCallable(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>makeMessageOperationCallable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">makeMessageOperationCallable</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">If message is not call, makes it call.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to check.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeSynchForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>changeSynchForMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">changeSynchForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Change synch for message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)">
<h3>setMessageSort</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMessageSort</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/interactions/mdbasicinteractions/MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> sort)</span></div>
<div class="block">Changes message sort by the given one.
 <p></p>
<b>NOTE</b> Message must have parent</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Given message, to change sort</dd>
<dd><code>sort</code> - Given sort kind, one from MessageSortEnum</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../magicdraw/interactions/mdbasicinteractions/MessageSortEnum.html" title="class in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageSortEnum</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>initMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> source,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> target)</span></div>
<div class="block">Initializes the message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>source</code> - the source</dd>
<dd><code>target</code> - the target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceiveEventByMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>createReceiveEventByMessageSort</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/MessageOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageOccurrenceSpecification</a></span> <span class="element-name">createReceiveEventByMessageSort</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Creates receive event occurrence according message sort</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dt>Returns:</dt>
<dd>MessageOccurrenceSpecification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initCoveredInfo(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>initCoveredInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initCoveredInfo</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a> fragment,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</span></div>
<div class="block">Initializes the covered info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fragment</code> - the fragment</dd>
<dd><code>lifeline</code> - the lifeline</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findInteraction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>findInteraction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">findInteraction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> interactionElement)</span></div>
<div class="block">Finds interaction for a given interaction element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interactionElement</code> - an element in an interaction.</dd>
<dt>Returns:</dt>
<dd>interaction to which a given interaction element is related.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>initMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target)</span></div>
<div class="block">Initializes message by the given source and target.
 <ul>
<li> If source or target is of type Lifeline, then is created additionally MessageOccurrenceSpecification and covered by Lifeline
 <li> If source or target is of type CombinedFragment, InteractionUse or Interaction,
 then is created additionally Gate as MessageEnd. Gate is not covered by any lifeline</li></li></ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dd><code>source</code> - source</dd>
<dd><code>target</code> - target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>makeLostMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">makeLostMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Turns a message to a lost message by removing its receiving end
 and setting necessary properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to turn into a lost message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>makeFoundMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">makeFoundMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Turns a message to a found message by removing its sending end
 and setting necessary properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to turn into a found message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean)">
<h3>constructMessageText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructMessageText</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 boolean showParameters)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../magicdraw/uml/text/ModelTextCreator.html#createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createMessageText(Message, MessageTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getMessageSubstitute(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getMessageSubstitute</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getMessageSubstitute</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Returns message substitute for given message or the given message, if no substitution found. Message substitution
 is message found by the formal gate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message, for which substitution will be searched</dd>
<dt>Returns:</dt>
<dd>given message if no substitution found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationOfCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getOperationOfCallMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getOperationOfCallMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets the operation of call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>the operation of call message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalOfMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getSignalOfMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">getSignalOfMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets the signal of message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>the signal of message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalAttributeForArgument(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>getSignalAttributeForArgument</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSignalAttributeForArgument</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> argument)</span></div>
<div class="block">Gets signal attribute if it exists for a given message argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>argument</code> - argument for which to retrieve signal attribute.</dd>
<dt>Returns:</dt>
<dd>signal attribute related to the given argument if found, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOperationForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean)">
<h3>setOperationForMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOperationForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean createArguments)</span></div>
<div class="block">Sets the operation for message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>operation</code> - the operation</dd>
<dd><code>createArguments</code> - the create arguments</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSignalForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">
<h3>setSignalForMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSignalForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal)</span></div>
<div class="block">Sets the signal for message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>signal</code> - the signal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findSignalForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">
<h3>findSignalForMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">findSignalForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Find signal for message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>name</code> - the name</dd>
<dt>Returns:</dt>
<dd>the signal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAvailableOperationsForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getAvailableOperationsForCallMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getAvailableOperationsForCallMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets operations which are available to select for a call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message for which to get available operations for selection.</dd>
<dt>Returns:</dt>
<dd>available operations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getOperationsForCallAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getOperationsForCallAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getOperationsForCallAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getOperationsForCallAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 @CheckForNull
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>message</code> - call message</dd>
<dt>Returns:</dt>
<dd>classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getOperations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getOperations</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 @CheckForNull
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Returns all operations for call actions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier from which we select operations</dd>
<dt>Returns:</dt>
<dd>operation set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNotGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isNotGate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNotGate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if message send end is Gate (Message send from diagram border)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dt>Returns:</dt>
<dd>true if is not Gate, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLifelinePort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>isLifelinePort</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">isLifelinePort</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Checks if lifeline from message supplier is port and exists in lifeline context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dt>Returns:</dt>
<dd>true if is port else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLifelines(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getLifelines</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a>&gt;</span> <span class="element-name">getLifelines</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Returns lifelines that are covered by given message</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dt>Returns:</dt>
<dd>lifelines that are covered by given message, null if no lifeline is covered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findCallOperationWithArguments(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.List,int,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>findCallOperationWithArguments</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">findCallOperationWithArguments</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt; preferredOperations,
 int paramCount,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Find call operation, which has closest parameter count. Sometimes there are few operations with same names,
 but different parameter count - this function returns operation by name and closest match by paramCount.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name</dd>
<dd><code>classifier</code> - the classifier</dd>
<dd><code>preferredOperations</code> - list of preferred operations</dd>
<dd><code>paramCount</code> - preferred parameter count</dd>
<dd><code>message</code> - call message</dd>
<dt>Returns:</dt>
<dd>the operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findCallOperation(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.List,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>findCallOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">findCallOperation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt; preferredOperations,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Find call operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name</dd>
<dd><code>classifier</code> - the classifier</dd>
<dd><code>preferredOperations</code> - the preferred operations</dd>
<dd><code>message</code> - call message</dd>
<dt>Returns:</dt>
<dd>the operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createArgumentsForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>createArgumentsForCallMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createArgumentsForCallMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Creates the arguments for call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createArgumentForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>createArgumentForMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createArgumentForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="block">Creates an argument for a message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message for which to create an argument.</dd>
<dd><code>type</code> - type of the argument.</dd>
<dt>Returns:</dt>
<dd>created argument for message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createArgumentForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>createArgumentForMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createArgumentForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> defaultValue)</span></div>
<div class="block">Creates an argument for a message.
 Uses the passed default value to initialize the argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message for which to create an argument.</dd>
<dd><code>type</code> - type of the argument.</dd>
<dd><code>defaultValue</code> - default value for the argument.</dd>
<dt>Returns:</dt>
<dd>created argument for message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getArgumentSupportedValueSpecifications()">
<h3>getArgumentSupportedValueSpecifications</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">getArgumentSupportedValueSpecifications</span>()</div>
<div class="block">Get argument supported value specification classes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value specification classes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedNumberAsString(java.util.List)">
<h3>getNestedNumberAsString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNestedNumberAsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> number)</span></div>
<div class="block">Gets the nested number as string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>number</code> - the number</dd>
<dt>Returns:</dt>
<dd>the nested number as string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProperty(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">
<h3>createProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">createProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../magicdraw/interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> inter)</span></div>
<div class="block">Creates property into interaction for the lifeline use.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - name</dd>
<dd><code>type</code> - type</dd>
<dd><code>inter</code> - interaction</dd>
<dt>Returns:</dt>
<dd>created property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeMessageArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>disposeMessageArguments</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disposeMessageArguments</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Dispose message arguments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMessageArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.List)">
<h3>setMessageArguments</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMessageArguments</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; arguments)</span>
                                throws <span class="exceptions"><a href="../../../../magicdraw/utils/parsers/ParseException.html" title="class in com.nomagic.magicdraw.utils.parsers">ParseException</a></span></div>
<div class="block">Sets the message arguments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>arguments</code> - the arguments</dd>
<dt>Throws:</dt>
<dd><code><a href="../../../../magicdraw/utils/parsers/ParseException.html" title="class in com.nomagic.magicdraw.utils.parsers">ParseException</a></code> - the parse exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeReturnParameter(java.util.List)">
<h3>removeReturnParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">removeReturnParameter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> parameters)</span></div>
<div class="block">Removes the return parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameters</code> - the parameters</dd>
<dt>Returns:</dt>
<dd>the int</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">
<h3>setTarget</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTarget</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> target)</span></div>
<div class="block">Sets the target.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>target</code> - the target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">
<h3>setGuard</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setGuard</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> guard)</span></div>
<div class="block">Sets the guard.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>guard</code> - the guard</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReceiveElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getReceiveElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getReceiveElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets the receive element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dt>Returns:</dt>
<dd>the receive element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getSendElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSendElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Return send event holder of the given message.
 <p>It can be:
 <ul>
<li> covered lifeline
 <li> gate owner (Interaction, CombinedFragment, InteractionUse)</li></li></ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Given message, which will be analysed</dd>
<dt>Returns:</dt>
<dd>One of Lifeline, Interaction, CombinedFragment, InteractionUse.
 Can return null, if message has no send event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getReplyMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getReplyMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Return receive event holder of the given message.
 <p>It can be:
 <ul>
<li> covered lifeline
 <li> gate owner (Interaction, CombinedFragment, InteractionUse)</li></li></ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Given message, which will be analysed</dd>
<dt>Returns:</dt>
<dd>One of Lifeline, Interaction, CombinedFragment, InteractionUse.
 Can return null, if message has no receive event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">
<h3>setReturnValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReturnValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the return value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>value</code> - the value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReturnParameterPosition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>getReturnParameterPosition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getReturnParameterPosition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation)</span></div>
<div class="block">Gets the return parameter position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - the operation</dd>
<dt>Returns:</dt>
<dd>the return parameter position</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReturnValueForMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">
<h3>setReturnValueForMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReturnValueForMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the return value for message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>value</code> - the value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseArguments(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.lang.String)">
<h3>parseArguments</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">parseArguments</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Parses arguments from string and sets them as message arguments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dd><code>s</code> - string to parse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initOperationForCallMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>initOperationForCallMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initOperationForCallMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation)</span></div>
<div class="block">Init the operation for call message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message</dd>
<dd><code>classifier</code> - the classifier</dd>
<dd><code>operation</code> - the op</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLifelineType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>setLifelineType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLifelineType</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="block">Sets the lifeline type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - the lifeline</dd>
<dd><code>type</code> - the type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateInvariantClassifier(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">
<h3>getStateInvariantClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getStateInvariantClassifier</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant)</span></div>
<div class="block">Gets classifier which is related to a given state invariant through a lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateInvariant</code> - state invariant for which classifier should found.</dd>
<dt>Returns:</dt>
<dd>classifier if found, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLifelineType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>getLifelineType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getLifelineType</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</span></div>
<div class="block">Gets the lifeline type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - the lifeline</dd>
<dt>Returns:</dt>
<dd>the lifeline type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemovableConnectableElement(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>getRemovableConnectableElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></span> <span class="element-name">getRemovableConnectableElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</span></div>
<div class="block">Check if the represents can be removed along with lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - lifeline</dd>
<dt>Returns:</dt>
<dd>connectible element that should be disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,java.lang.String,java.lang.String)">
<h3>setTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTimeInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> timeConstraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue)</span></div>
<div class="block">Sets time interval for a given time constraint.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeConstraint</code> - time constraint to modify.</dd>
<dd><code>minValue</code> - min value.</dd>
<dd><code>maxValue</code> - max value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,java.lang.String,java.lang.String,boolean)">
<h3>setTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTimeInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> timeInterval,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue,
 boolean createObservation)</span></div>
<div class="block">Sets time interval data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeInterval</code> - time interval to modify.</dd>
<dd><code>minValue</code> - min value.</dd>
<dd><code>maxValue</code> - max value.</dd>
<dd><code>createObservation</code> - indicates if observation should be created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint,java.lang.String)">
<h3>setTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTimeInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> timeConstraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax)</span></div>
<div class="block">Sets time interval for a time constraint.
 String is of type lower..higher values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeConstraint</code> - constraint constraint for which to set time interval.</dd>
<dd><code>minMax</code> - min..max format value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,java.lang.String,boolean)">
<h3>setTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTimeInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> timeInterval,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax,
 boolean createObservation)</span></div>
<div class="block">Sets time interval data.
 String is of type lower..higher values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeInterval</code> - time interval to modify.</dd>
<dd><code>minMax</code> - min..max format value.</dd>
<dd><code>createObservation</code> - indicates if observation should be created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,java.lang.String)">
<h3>setDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setDurationInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> durationConstraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax)</span></div>
<div class="block">Sets duration interval data.
 String is of type lower..higher values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>durationConstraint</code> - duration constraint to set.</dd>
<dd><code>minMax</code> - min..max format value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,java.lang.String,boolean)">
<h3>setDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setDurationInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> durationInterval,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minMax,
 boolean createObservation)</span></div>
<div class="block">Sets duration interval value.
 String is of type lower..higher values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>durationInterval</code> - duration interval to modify.</dd>
<dd><code>minMax</code> - min..max format value.</dd>
<dd><code>createObservation</code> - indicates if observation should be created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)">
<h3>createTimeExpression</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">createTimeExpression</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> tc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean)"><code>createTimeExpression(TimeInterval, boolean)</code></a></div>
</div>
<div class="block">Creates time expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tc</code> - constraint</dd>
<dt>Returns:</dt>
<dd>expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,boolean)">
<h3>createTimeExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">createTimeExpression</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> timeInterval,
 boolean createObservation)</span></div>
<div class="block">Creates time expression for give time interval min or max.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeInterval</code> - interval</dd>
<dd><code>createObservation</code> - create observation</dd>
<dt>Returns:</dt>
<dd>expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeExpressionOwner(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setTimeExpressionOwner</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTimeExpressionOwner</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> timeExpression,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> findParentFrom)</span></div>
<div class="block">Sets the time expression owner.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeExpression</code> - the time expression</dd>
<dd><code>findParentFrom</code> - the find parent from</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntervalMinMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">
<h3>getIntervalMinMax</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">getIntervalMinMax</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> interval)</span></div>
<div class="block">Returns min and max values. If not exist - can be null</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interval</code> - interval</dd>
<dt>Returns:</dt>
<dd>min max values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntervalMinMaxValues(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">
<h3>getIntervalMinMaxValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[]</span> <span class="element-name">getIntervalMinMaxValues</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a> interval)</span></div>
<div class="block">Returns min and max values. If not exist - can be null</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interval</code> - interval</dd>
<dt>Returns:</dt>
<dd>min max values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint)">
<h3>createDuration</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></span> <span class="element-name">createDuration</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> dc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean)"><code>createDuration(DurationInterval, boolean)</code></a></div>
</div>
<div class="block">Creates duration with appropriate DurationObservationAction and min and max values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dc</code> - constraint</dd>
<dt>Returns:</dt>
<dd>constraint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,boolean)">
<h3>createDuration</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></span> <span class="element-name">createDuration</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> interval,
 boolean createObservation)</span></div>
<div class="block">Create duration for duration interval min or max.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interval</code> - interval</dd>
<dd><code>createObservation</code> - create observation</dd>
<dt>Returns:</dt>
<dd>duration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDurationOwner(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setDurationOwner</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setDurationOwner</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> duration,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> findParentFrom)</span></div>
<div class="block">Sets the duration owner.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>duration</code> - the duration</dd>
<dd><code>findParentFrom</code> - the find parent from</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,java.lang.String,java.lang.String)">
<h3>setDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setDurationInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> dc,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue)</span></div>
<div class="block">Sets duration interval.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dc</code> - constraint</dd>
<dd><code>minValue</code> - min value</dd>
<dd><code>maxValue</code> - max value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,java.lang.String,java.lang.String,boolean)">
<h3>setDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setDurationInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> interval,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> minValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maxValue,
 boolean createObservation)</span></div>
<div class="block">Sets duration interval.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interval</code> - interval</dd>
<dd><code>minValue</code> - min value</dd>
<dd><code>maxValue</code> - max value</dd>
<dd><code>createObservation</code> - create observation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInsideMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">
<h3>isInsideMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInsideMessage</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> fragment)</span></div>
<div class="block">Checks if given message is inside the fragment. Check
 - if given message has one end with the same covered lifeline as  <code>fragment</code> does
 - if given message has one end to the nested fragment
 <p></p>
 Message is expected to have one end connected to <code>fragment</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Message to check if ii is inside</dd>
<dd><code>fragment</code> - Check if given message is inside THIS fragment</dd>
<dt>Returns:</dt>
<dd>true if given message is inside the given fragment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)">
<h3>getMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getMessage</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> gate)</span></div>
<div class="block">Returns message, to which this gate is connected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>gate</code> - given gate to check message</dd>
<dt>Returns:</dt>
<dd>Message, which is connected to the gate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPairableGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean)">
<h3>getPairableGate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a>&gt;</span> <span class="element-name">getPairableGate</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> use,
 boolean replayMessage)</span></div>
<div class="block">Gets iterator of Gates, which can be used to be formal pair of the gate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>use</code> - given interaction use</dd>
<dd><code>replayMessage</code> - if true, than all messages will be returned which are pairable for replay message kind</dd>
<dt>Returns:</dt>
<dd>Iterator of gates. Not null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPairableGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,boolean)">
<h3>getPairableGate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/interactions/mdfragments/Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a>&gt;</span> <span class="element-name">getPairableGate</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> fragment,
 boolean replayMessage)</span></div>
<div class="block">Gets iterator of Gates, which can be used to be formal pair of the gate. The are : all gates, which are originated
 by inside messages of given fragment. Inside message must have at least one end which would cover lifeline,
 covered by given fragment</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fragment</code> - given interaction fragment</dd>
<dd><code>replayMessage</code> - if true, than all messages will be returned which are pairable for replay message kind</dd>
<dt>Returns:</dt>
<dd>Iterator of gates. Not null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventForTimeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">
<h3>setEventForTimeExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setEventForTimeExpression</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> timeExpression,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event)</span></div>
<div class="block">Sets event for first time observation referenced by a given time expression.
 If time expression does not reference any time observation, call is ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeExpression</code> - time expression to modify.</dd>
<dd><code>event</code> - event to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventForTimeInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeInterval,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">
<h3>setEventForTimeInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setEventForTimeInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a> interval,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event,
 boolean createObservation)</span></div>
<div class="block">Sets event for Time Interval min and max expressions. Creates min and max expressions if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interval</code> - time interval</dd>
<dd><code>event</code> - event</dd>
<dd><code>createObservation</code> - if true create TimeObservation if min and max expressions are created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventForDuration(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">
<h3>setEventForDuration</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setEventForDuration</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> duration,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event1,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event2)</span></div>
<div class="block">Sets events for first DurationObservation referenced by given Duration. If Duration do no reference any DurationObservation, call is ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>duration</code> - duration</dd>
<dd><code>event1</code> - event or null</dd>
<dd><code>event2</code> - event or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventForDurationInterval(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationInterval,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">
<h3>setEventForDurationInterval</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setEventForDurationInterval</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a> interval,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event1,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> event2,
 boolean createObservations)</span></div>
<div class="block">Sets events for DurationInterval min and max durations. Creates min and max durations if needed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interval</code> - duration interval</dd>
<dd><code>event1</code> - event or null</dd>
<dd><code>event2</code> - event or null</dd>
<dd><code>createObservations</code> - if true create DurationObservation if min and max durations are created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStateForStateInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,boolean)">
<h3>setStateForStateInvariant</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStateForStateInvariant</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant,
 <a href="../../magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> state,
 boolean createConstraintIfNecessary)</span></div>
<div class="block">Sets state for state invariant to represent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateInvariant</code> - state invariant for which state should be set.</dd>
<dd><code>state</code> - state which should be set to state invariant.</dd>
<dd><code>createConstraintIfNecessary</code> - creates constraint if constraint doesn't exist in a state invariant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateInvariantConstraint(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant,boolean)">
<h3>getStateInvariantConstraint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getStateInvariantConstraint</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant,
 boolean create)</span></div>
<div class="block">Gets state invariant constraint from state invariant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateInvariant</code> - state invariant from which to get state invariant constraint.</dd>
<dd><code>create</code> - true if a new constraint should be created when no constraints are found.</dd>
<dt>Returns:</dt>
<dd>invariant constraint if found or new created, null if no constraint found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateInvariantState(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">
<h3>getStateInvariantState</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">getStateInvariantState</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> stateInvariant)</span></div>
<div class="block">Retrieves state which is set to a given state invariant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateInvariant</code> - state invariant for which state should be retrieved.</dd>
<dt>Returns:</dt>
<dd>state if found, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessages(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>getMessages</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</span> <span class="element-name">getMessages</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</span></div>
<div class="block">Return all connected messages from given lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - lifeline</dd>
<dt>Returns:</dt>
<dd>all messages connected to this lifeline.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseParameterName(java.lang.String)">
<h3>parseParameterName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">parseParameterName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Parses parameter from parameter=argument tuple.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to parse.</dd>
<dt>Returns:</dt>
<dd>parsed parameter name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseArgumentName(java.lang.String)">
<h3>parseArgumentName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">parseArgumentName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Parses argument from parameter=argument tuple.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to parse.</dd>
<dt>Returns:</dt>
<dd>parsed argument name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addParameterForOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String,boolean)">
<h3>addParameterForOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">addParameterForOperation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean generateName)</span></div>
</section>
</li>
<li>
<section class="detail" id="addParameterForOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind)">
<h3>addParameterForOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">addParameterForOperation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean generateName,
 <a href="../../magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> directionKind)</span></div>
<div class="block">Adds a parameter to an operation with a given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - operation for which to add a parameter.</dd>
<dd><code>name</code> - name to set.</dd>
<dd><code>generateName</code> - indicates whether name should be generated if given name is empty.</dd>
<dd><code>directionKind</code> - parameter direction</dd>
<dt>Returns:</dt>
<dd>created parameter.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyForSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,java.lang.String,boolean)">
<h3>addPropertyForSignal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">addPropertyForSignal</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean generateName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOperationParameterByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.lang.String)">
<h3>getOperationParameterByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">getOperationParameterByName</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> op,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Finds parameter from the operation by given name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>op</code> - provided operation</dd>
<dd><code>name</code> - name for the parameter</dd>
<dt>Returns:</dt>
<dd>parameter or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalAttributeByName(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,java.lang.String)">
<h3>getSignalAttributeByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSignalAttributeByName</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="ensureFragmentsAreInFragmentCollection(java.util.Collection,java.util.Collection)">
<h3>ensureFragmentsAreInFragmentCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">ensureFragmentsAreInFragmentCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt; fragments)</span></div>
<div class="block">Ensures that fragments are in given fragment collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to check.</dd>
<dd><code>fragments</code> - fragments to add to the fragment collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAvailableSignals(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>getAvailableSignals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</span> <span class="element-name">getAvailableSignals</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message)</span></div>
<div class="block">Gets all available signals to select for a message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message for which to retrieve all available signals.</dd>
<dt>Returns:</dt>
<dd>available signals for a message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestructionOccurrenceSpecification(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>getDestructionOccurrenceSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></span> <span class="element-name">getDestructionOccurrenceSpecification</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline)</span></div>
<div class="block">Gets destruction occurrence specification from a given lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - lifeline for which to get destruction occurrence specification.</dd>
<dt>Returns:</dt>
<dd>destruction occurrence specification if found any, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestructionOccurrenceSpecification(java.util.Collection)">
<h3>getDestructionOccurrenceSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/interactions/mdbasicinteractions/DestructionOccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">DestructionOccurrenceSpecification</a></span> <span class="element-name">getDestructionOccurrenceSpecification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/interactions/mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt; collection)</span></div>
<div class="block">Gets destruction occurrence specification from a given lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection in which to search for destruction occurrence.</dd>
<dt>Returns:</dt>
<dd>destruction occurrence specification if found any, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureDestructionOccurrence(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline,boolean)">
<h3>ensureDestructionOccurrence</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">ensureDestructionOccurrence</span><wbr/><span class="parameters">(<a href="../../magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> lifeline,
 boolean destruct)</span></div>
<div class="block">Ensures that a proper destruction occurrence is in the model on this lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifeline</code> - lifeline for which to ensure destruction occurrence.</dd>
<dd><code>destruct</code> - indicates whether lifeline is destructed or not.</dd>
<dt>Returns:</dt>
<dd>true if destruction event was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enableExecutionSpecificationModeling(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>enableExecutionSpecificationModeling</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">enableExecutionSpecificationModeling</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement)</span>
                                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Enable ExecutionSpecification modeling in given Sequence diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramPresentationElement</code> - sequence diagram.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if diagram is not sequence diagram.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created at the current moment, or diagram is not loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFirstEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>setFirstEvent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setFirstEvent</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> constraint,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> constrainedElement,
 boolean value)</span></div>
<div class="block">Sets firstEvent value for a given constrained element
 Does nothing if given element is not a constrained element or firstEvent list size is out of sync with constrainedElement list size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint</dd>
<dd><code>constrainedElement</code> - constrained element</dd>
<dd><code>value</code> - firstEvent value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFirstEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFirstEvent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isFirstEvent</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> constraint,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> constrainedElement)</span></div>
<div class="block">Returns firstEvent value for a given constrained element by index.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint</dd>
<dd><code>constrainedElement</code> - constrained element</dd>
<dt>Returns:</dt>
<dd>value or null if given element is not a constrained element or firstEvent list size is out of the sync with constrainedElement list size</dd>
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
