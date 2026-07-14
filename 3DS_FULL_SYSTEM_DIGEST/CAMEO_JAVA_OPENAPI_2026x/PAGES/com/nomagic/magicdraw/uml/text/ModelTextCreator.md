# JAVA OPENAPI: ModelTextCreator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/text/ModelTextCreator.html
- source_path: `com/nomagic/magicdraw/uml/text/ModelTextCreator.html`
- source_sha256: `32012d1cdea7645d713bd920354b4d29db777d8d388ff5223f3cd8ef7558cefc`
- captured_utc: `2026-07-14T16:58:33.202237+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.text](package-summary.html)

## Class ModelTextCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.text.CoreTextCreator](CoreTextCreator.html)
com.nomagic.magicdraw.uml.text.ModelTextCreator

@OpenApiAllpublic classModelTextCreator
extends [CoreTextCreator](CoreTextCreator.html)
Contains methods to create representation text for various model elements

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ELEMENTS_PROPERTY_KEY](#ELEMENTS_PROPERTY_KEY)`
Fields inherited from class com.nomagic.magicdraw.uml.text.[CoreTextCreator](CoreTextCreator.html)
`[NEW_LINE_SEPARATOR](CoreTextCreator.html#NEW_LINE_SEPARATOR), [TYPE_SEPARATOR](CoreTextCreator.html#TYPE_SEPARATOR), [VALUE_SEPARATOR](CoreTextCreator.html#VALUE_SEPARATOR)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModelTextCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[appendAssociationEnd](#appendAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.text.builders.TextBuilder))([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [TextBuilder](../../../text/builders/TextBuilder.html) builder)`

`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createActivityEdgeText](#createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier))([ActivityEdge](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html) activityEdge,
 boolean showWeight,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`ActivityEdge`](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createActivityParameterNodeText](#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean,java.util.function.Supplier))([ActivityParameterNode](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) parameterNode,
 boolean showFullType,
 boolean showTypePrefix,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`ActivityParameterNode`](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createActivityParameterNodeText](#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier))([ActivityParameterNode](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) parameterNode,
 boolean showFullType,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`ActivityParameterNode`](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createAssociationText](#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier))([Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Association`](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createBehaviorText](#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))([Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 [BehaviorTextParams](BehaviorTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Behavior`](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createCombinedFragmentOperatorText](#createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier))([CombinedFragment](../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html) combinedFragment,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`CombinedFragment`](../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createConstraintsText](#createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [ConstraintTextParams](ConstraintTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation for the given collection of [`Constraint`](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) elements.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createConstraintText](#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier))([Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [ConstraintTextParams](ConstraintTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Constraint`](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createEnumerationLiteralText](#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))([EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumerationLiteral,
 [MemberTextParams](MemberTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`EnumerationLiteral`](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createEventText](#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier))([Event](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event,
 [EventTextParams](EventTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Event`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createGuardText](#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier))([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the provided message's guard.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createInstanceSpecificationText](#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier))([InstanceSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [InstanceSpecificationTextParams](InstanceSpecificationTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`InstanceSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createInstanceSpecificationText](#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier,java.util.function.Predicate))([InstanceSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [InstanceSpecificationTextParams](InstanceSpecificationTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> classifierFilter)`
Creates string representation of the given [`InstanceSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createInteractionUseText](#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier))([CallBehaviorAction](../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) callBehaviorAction,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`CallBehaviorAction`](../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) that is displayed as InteractionUse.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createInteractionUseText](#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier))([InteractionUse](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html) interactionUse,
 [InteractionUseTextParams](InteractionUseTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`InteractionUse`](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createMessageText](#createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier))([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [MessageTextParams](MessageTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Message`](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createOperandGuardText](#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier))([InteractionOperand](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html) interactionOperand,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation for the guard of the given [`InteractionOperand`](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createOperationText](#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))([Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [OperationTextParams](OperationTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Operation`](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createParameterDirectionText](#createParameterDirectionText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,com.nomagic.uml2.project.ElementProject,com.nomagic.magicdraw.uml.text.ParameterDirectionTextParams,java.util.function.Supplier))([ParameterDirectionKind](../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html) parameterDirection,
 com.nomagic.uml2.project.ElementProject project,
 [ParameterDirectionTextParams](ParameterDirectionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`ParameterDirectionKind`](../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html)
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createParametersText](#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameters,
 [ParameterTextParams](ParameterTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation for the given collection of [`Parameter`](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) elements, separated by comma
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createParameterText](#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))([Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 [ParameterTextParams](ParameterTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Parameter`](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createPinText](#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier))([Pin](../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html) pin,
 [PinTextParams](PinTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Pin`](../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createPropertyText](#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [PropertyTextParams](PropertyTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Property`](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createProtocolTransitionText](#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))([ProtocolTransition](../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition,
 [TransitionTextParams](TransitionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`ProtocolTransition`](../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createReceptionText](#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))([Reception](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 [ReceptionTextParams](ReceptionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Reception`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createRelationshipFromToText](#createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) clientModelElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) clientName,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplierModelElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) supplierName,
 boolean addFullQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Create relation representation text part to represent from what element to what element relation is connected.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createSlotsText](#createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [SlotTextParams](SlotTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of given slots collection (without braces).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createSlotsTextWithBraces](#createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [SlotTextParams](SlotTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of given slots collection, wrapped between '{' and '}'.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createSlotText](#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))([Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 [SlotTextParams](SlotTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given slot.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createSlotText](#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier,com.nomagic.magicdraw.uml.text.RepTextContext))([Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 [SlotTextParams](SlotTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory,
 [RepTextContext](RepTextContext.html) context)`
Creates string representation of the given slot.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStateText](#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier))([State](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) state,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`State`](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTaggedValuesText](#createTaggedValuesText(java.util.Collection,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html)> taggedValues,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of given taggedValues collection (without braces).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTaggedValuesTextWithBraces](#createTaggedValuesTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html)> taggedValues,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of given taggedValues collection, wrapped between '{' and '}'.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTaggedValueText](#createTaggedValueText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.util.function.Supplier))([TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given taggedValue.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTaggedValueText](#createTaggedValueText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.util.function.Supplier,com.nomagic.magicdraw.uml.text.RepTextContext))([TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory,
 [RepTextContext](RepTextContext.html) context)`
Creates string representation of the given taggedValue.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTemplateBindingText](#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean,java.util.function.Supplier))([TemplateBinding](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) templateBinding,
 boolean showTemplateParameterInfo,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`TemplateBinding`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTemplateParametersText](#createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TemplateParameter](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html)> templateParameters,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation for the given collection of [`TemplateParameter`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) elements.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTemplateParameterSubstitutionText](#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier))([TemplateParameterSubstitution](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) parameterSubstitution,
 boolean showTemplateParameterInfo,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`TemplateParameterSubstitution`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTemplateParameterText](#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier))([TemplateParameter](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) templateParameter,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`TemplateParameter`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTransitionText](#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))([Transition](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 [TransitionTextParams](TransitionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given Transition.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTriggersText](#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> triggers,
 [TriggerTextParams](TriggerTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation for the given collection of [`Trigger`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) elements, separated by comma.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTriggerText](#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))([Trigger](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger,
 [TriggerTextParams](TriggerTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Trigger`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html).
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTypedElementText](#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier))([TypedElement](../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) typedElement,
 [TypedElementTextParams](TypedElementTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`TypedElement`](../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html).
Methods inherited from class com.nomagic.magicdraw.uml.text.[CoreTextCreator](CoreTextCreator.html)
`[appendPrefix](CoreTextCreator.html#appendPrefix(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.text.builders.TextBuilder)), [containsParentheses](CoreTextCreator.html#containsParentheses(java.lang.String)), [createElementNumberText](CoreTextCreator.html#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier)), [createMultiplicityRangeText](CoreTextCreator.html#createMultiplicityRangeText(java.lang.Integer)), [createMultiplicityText](CoreTextCreator.html#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)), [createMultiplicityText](CoreTextCreator.html#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)), [createMultiplicityText](CoreTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)), [createMultiplicityText](CoreTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer)), [createMultiplicityText](CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)), [createMultiplicityText](CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)), [createNamedElementListText](CoreTextCreator.html#createNamedElementListText(java.util.List,java.util.function.Supplier)), [createStereotypesText](CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)), [createStereotypesText](CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)), [createStereotypeText](CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)), [createStereotypeText](CoreTextCreator.html#createStereotypeText(java.lang.String)), [createStringCollectionText](CoreTextCreator.html#createStringCollectionText(java.util.Collection,java.lang.String,java.util.function.Supplier)), [createStyledTypeText](CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean,java.util.function.Supplier)), [createStyledTypeText](CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)), [createStyledTypeTextWithSeparator](CoreTextCreator.html#createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean,java.util.function.Supplier)), [createStyledTypeTextWithSeparator](CoreTextCreator.html#createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)), [createTypeText](CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean,java.util.function.Supplier)), [createTypeText](CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)), [createTypeText](CoreTextCreator.html#createTypeText(java.util.Collection,boolean,boolean,java.util.function.Supplier)), [createTypeText](CoreTextCreator.html#createTypeText(java.util.Collection,boolean,java.util.function.Supplier)), [createValueSpecificationText](CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier)), [createValueSpecificationText](CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier)), [createVisibilityText](CoreTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)), [isUseStandardStereotypeChar](CoreTextCreator.html#isUseStandardStereotypeChar()), [join](CoreTextCreator.html#join(com.nomagic.text.builders.TextBuilder,java.lang.String,java.util.stream.Stream,java.util.function.Function)), [setUseStandardStereotypeChar](CoreTextCreator.html#setUseStandardStereotypeChar(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ELEMENTS_PROPERTY_KEY
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ELEMENTS_PROPERTY_KEY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.ModelTextCreator.ELEMENTS_PROPERTY_KEY)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModelTextCreator
public ModelTextCreator()
 ============ METHOD DETAIL ========== 
Method Details
createActivityEdgeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createActivityEdgeText([ActivityEdge](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html) activityEdge,
 boolean showWeight,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`ActivityEdge`](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html).
Parameters:
`activityEdge` - element to create representation text for
`showWeight` - when true, weight information will be included to the text
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the activity edge's text appended
createConstraintsText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createConstraintsText([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [ConstraintTextParams](ConstraintTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation for the given collection of [`Constraint`](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) elements.
Parameters:
`constraints` - collection of constraint elements to create representation text for
`textParams` - configuration that defines what to include in the text of the constraint
`separator` - symbol(s) to separate each constraint's text with
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the constraints' text appended
See Also:
[`createConstraintText(Constraint, ConstraintTextParams, Supplier)`](#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier))
createConstraintText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createConstraintText(@CheckForNull
 [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [ConstraintTextParams](ConstraintTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Constraint`](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html).
Parameters:
`constraint` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the constraint
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the constraint's text appended
createPinText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createPinText([Pin](../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html) pin,
 [PinTextParams](PinTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Pin`](../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html).
Parameters:
`pin` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the pin
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the pin's text appended
createCombinedFragmentOperatorText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createCombinedFragmentOperatorText([CombinedFragment](../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html) combinedFragment,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`CombinedFragment`](../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html).
Parameters:
`combinedFragment` - element to create representation text for
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the combinedFragment's text appended
createOperandGuardText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createOperandGuardText([InteractionOperand](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html) interactionOperand,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation for the guard of the given [`InteractionOperand`](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html).
Parameters:
`interactionOperand` - element to create representation text for
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the guard's text appended
createTransitionText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTransitionText([Transition](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 [TransitionTextParams](TransitionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given Transition. Keep in mind that text is different for protocol transition. 

 Syntax of [`Transition`](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html): `trigger[guard]/effect`. 

 Syntax of [`ProtocolTransition`](../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html): `[precondition]trigger/[postcondition]`.
Parameters:
`transition` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the ?
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the transition's text appended
createProtocolTransitionText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createProtocolTransitionText([ProtocolTransition](../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition,
 [TransitionTextParams](TransitionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`ProtocolTransition`](../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html).
 Syntax: `[precondition]trigger/[postcondition]`.
Parameters:
`transition` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the ?
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the transition's text appended
createTriggersText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTriggersText([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> triggers,
 [TriggerTextParams](TriggerTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation for the given collection of [`Trigger`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) elements, separated by comma.
Parameters:
`triggers` - collection of trigger elements to create representation text for
`textParams` - configuration that defines what to include in the text of the trigger
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the trigger's text appended
See Also:
[`createTriggerText(Trigger, TriggerTextParams, Supplier)`](#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createTriggerText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTriggerText([Trigger](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger,
 [TriggerTextParams](TriggerTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Trigger`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html).
Parameters:
`trigger` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the trigger
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the trigger's text appended
createEventText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createEventText([Event](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event,
 [EventTextParams](EventTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Event`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html).
Parameters:
`event` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the event
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the event's text appended
createBehaviorText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createBehaviorText([Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 [BehaviorTextParams](BehaviorTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Behavior`](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html).
Parameters:
`behavior` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the behavior
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the behavior's text appended
createInteractionUseText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createInteractionUseText([InteractionUse](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html) interactionUse,
 [InteractionUseTextParams](InteractionUseTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`InteractionUse`](../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html).
Parameters:
`interactionUse` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the interactionUse
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the interactionUse's text appended
createInteractionUseText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createInteractionUseText([CallBehaviorAction](../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) callBehaviorAction,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`CallBehaviorAction`](../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) that is displayed as InteractionUse.
Parameters:
`callBehaviorAction` - element to create representation text for
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the action's text appended
createMessageText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createMessageText([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [MessageTextParams](MessageTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Message`](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html).
Parameters:
`message` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the message
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the message's text appended
createAssociationText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createAssociationText([Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Association`](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html).
Parameters:
`association` - element to create representation text for
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the association's text appended
createStateText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStateText([State](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) state,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`State`](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html).
Parameters:
`state` - element to create representation text for
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the state's text appended
createParametersText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createParametersText([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameters,
 [ParameterTextParams](ParameterTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation for the given collection of [`Parameter`](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) elements, separated by comma
Parameters:
`parameters` - collection of parameters to create representation text for
`textParams` - configuration that defines what to include in the text of each parameter
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the parameters' text appended
createParameterText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createParameterText([Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 [ParameterTextParams](ParameterTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Parameter`](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html).
Parameters:
`parameter` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the parameter
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the parameter's text appended
createParameterDirectionText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createParameterDirectionText(@CheckForNull
 [ParameterDirectionKind](../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html) parameterDirection,
 com.nomagic.uml2.project.ElementProject project,
 [ParameterDirectionTextParams](ParameterDirectionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`ParameterDirectionKind`](../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html)
Parameters:
`parameterDirection` - direction to create representation text for
`project` - project to which parameter belongs
`textParams` - configuration that defines what to include in the text of the parameter direction
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the parameter direction text appended
createOperationText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createOperationText([Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [OperationTextParams](OperationTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Operation`](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html).
Parameters:
`operation` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the operation
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the operation's text appended
createReceptionText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createReceptionText([Reception](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 [ReceptionTextParams](ReceptionTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Reception`](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html).
Parameters:
`reception` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the reception
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the reception's text appended
createPropertyText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createPropertyText([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [PropertyTextParams](PropertyTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Property`](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html).
Parameters:
`property` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the property
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the property's text appended
createActivityParameterNodeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createActivityParameterNodeText([ActivityParameterNode](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) parameterNode,
 boolean showFullType,
 boolean showTypePrefix,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`ActivityParameterNode`](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
Parameters:
`parameterNode` - element to create representation text for
`showFullType` - true if qualified name should be included in the text of node's type
`showTypePrefix` - true to include type's prefix
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the node's text appended
createActivityParameterNodeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createActivityParameterNodeText([ActivityParameterNode](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) parameterNode,
 boolean showFullType,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`ActivityParameterNode`](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html).
Parameters:
`parameterNode` - element to create representation text for
`showFullType` - true if qualified name should be included in the text of node's type
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the node's text appended
createGuardText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createGuardText([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the provided message's guard.
Parameters:
`message` - element for which guard representation text has to be created
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the guard's text appended
createEnumerationLiteralText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createEnumerationLiteralText([EnumerationLiteral](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumerationLiteral,
 [MemberTextParams](MemberTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`EnumerationLiteral`](../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html).
Parameters:
`enumerationLiteral` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the enumeration literal
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the enumeration literal's text appended
createTemplateParameterText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTemplateParameterText([TemplateParameter](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) templateParameter,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`TemplateParameter`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html).
Parameters:
`templateParameter` - element to create representation text for
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the template parameter's text appended
createTemplateParametersText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTemplateParametersText([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TemplateParameter](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html)> templateParameters,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation for the given collection of [`TemplateParameter`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) elements.
Parameters:
`templateParameters` - collection of template parameter elements to create representation text for
`separator` - symbol(s) to separate each parameter's text with
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the parameters' text appended
See Also:
[`createTemplateParameterText(TemplateParameter, Supplier)`](#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier))
createTemplateBindingText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTemplateBindingText([TemplateBinding](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) templateBinding,
 boolean showTemplateParameterInfo,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`TemplateBinding`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html).
Parameters:
`templateBinding` - element to create representation text for
`showTemplateParameterInfo` - indicates if full template parameter notation should be used.
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the template binding's text appended
createTemplateParameterSubstitutionText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTemplateParameterSubstitutionText([TemplateParameterSubstitution](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) parameterSubstitution,
 boolean showTemplateParameterInfo,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`TemplateParameterSubstitution`](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html).
Parameters:
`parameterSubstitution` - element to create representation text for
`showTemplateParameterInfo` - indicates if full template parameter notation should be used.
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the parameter substitution's text appended
createInstanceSpecificationText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createInstanceSpecificationText([InstanceSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [InstanceSpecificationTextParams](InstanceSpecificationTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`InstanceSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html).
Parameters:
`instance` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the instance
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the instance's text appended
createInstanceSpecificationText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createInstanceSpecificationText([InstanceSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [InstanceSpecificationTextParams](InstanceSpecificationTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> classifierFilter)
Creates string representation of the given [`InstanceSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html).
Parameters:
`instance` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the instance
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
`classifierFilter` - provides ability to filter classifiers.
Returns:
builder with the instance's text appended
createRelationshipFromToText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createRelationshipFromToText([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) clientModelElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) clientName,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplierModelElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) supplierName,
 boolean addFullQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Create relation representation text part to represent from what element to what element relation is connected.
 For example if we connect Connector to 2 properties a and b, that are Owned by class Class1. In Containment
 browser we would see "Connector[Class1::a - Class1::b]" so this method returns the part for the representation
 "[Class1::a - Class1::b]".
Parameters:
`relationship` - relationship for which we want the representation part
`clientModelElement` - first (from) element
`clientName` - name or custom text of first (from) element
`supplierModelElement` - second (to) element
`supplierName` - name or custom text of second (to) element
`addFullQualifiedName` - if true, full qualified name will be added to client and supplier names
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the relation text appended
appendAssociationEnd
public static void appendAssociationEnd([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [TextBuilder](../../../text/builders/TextBuilder.html) builder)
createTypedElementText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTypedElementText([TypedElement](../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) typedElement,
 [TypedElementTextParams](TypedElementTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`TypedElement`](../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html).
Parameters:
`typedElement` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the typed element
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the typed element's text appended
createSlotsTextWithBraces
public static [TextBuilder](../../../text/builders/TextBuilder.html) createSlotsTextWithBraces([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [SlotTextParams](SlotTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of given slots collection, wrapped between '{' and '}'.
Parameters:
`slots` - collection of slots
`textParams` - configuration that defines what to include in the text of a slot
`separator` - symbol(s) to separate each slot's text with
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the slots text appended
createSlotsText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createSlotsText([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [SlotTextParams](SlotTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of given slots collection (without braces).
Parameters:
`slots` - collection of slots
`textParams` - configuration that defines what to include in the text of a slot
`separator` - symbol(s) to separate each slot's text with
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the slots text appended
createSlotText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createSlotText([Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 [SlotTextParams](SlotTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given slot.
Parameters:
`slot` - element to create representation text for
`textParams` - configuration that defines what to include in the text of a slot
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the slot's text appended
createSlotText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createSlotText([Slot](../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 [SlotTextParams](SlotTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory,
 [RepTextContext](RepTextContext.html) context)
Creates string representation of the given slot.
Parameters:
`slot` - element to create representation text for
`textParams` - configuration that defines what to include in the text of a slot
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
`context` - representation text creator invoker
Returns:
builder with the slot's text appended
createTaggedValuesText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTaggedValuesText([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html)> taggedValues,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of given taggedValues collection (without braces).
Parameters:
`taggedValues` - collection of taggedValues
`textParams` - configuration that defines what to include in the text of a slot
`separator` - symbol(s) to separate each slot's text with
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the taggedValues text appended
createTaggedValueText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTaggedValueText([TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given taggedValue.
Parameters:
`taggedValue` - element to create representation text for
`textParams` - configuration that defines what to include in the text of a taggedValue
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the taggedValue's text appended
createTaggedValueText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTaggedValueText([TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory,
 [RepTextContext](RepTextContext.html) context)
Creates string representation of the given taggedValue.
Parameters:
`taggedValue` - element to create representation text for
`textParams` - configuration that defines what to include in the text of a taggedValue
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the taggedValue's text appended
createTaggedValuesTextWithBraces
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTaggedValuesTextWithBraces([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TaggedValue](../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html)> taggedValues,
 [TaggedValueTextParams](TaggedValueTextParams.html) textParams,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of given taggedValues collection, wrapped between '{' and '}'.
Parameters:
`taggedValues` - collection of taggedValues
`textParams` - configuration that defines what to include in the text of a slot
`separator` - symbol(s) to separate each slot's text with
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append created text to
Returns:
builder with the taggedValues text appended

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.text</a></div>
<h1 class="title" title="Class ModelTextCreator">Class ModelTextCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CoreTextCreator.html" title="class in com.nomagic.magicdraw.uml.text">com.nomagic.magicdraw.uml.text.CoreTextCreator</a>
<div class="inheritance">com.nomagic.magicdraw.uml.text.ModelTextCreator</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ModelTextCreator</span>
<span class="extends-implements">extends <a href="CoreTextCreator.html" title="class in com.nomagic.magicdraw.uml.text">CoreTextCreator</a></span></div>
<div class="block">Contains methods to create representation text for various model elements</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ELEMENTS_PROPERTY_KEY">ELEMENTS_PROPERTY_KEY</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.text.CoreTextCreator">Fields inherited from class com.nomagic.magicdraw.uml.text.<a href="CoreTextCreator.html" title="class in com.nomagic.magicdraw.uml.text">CoreTextCreator</a></h3>
<code><a href="CoreTextCreator.html#NEW_LINE_SEPARATOR">NEW_LINE_SEPARATOR</a>, <a href="CoreTextCreator.html#TYPE_SEPARATOR">TYPE_SEPARATOR</a>, <a href="CoreTextCreator.html#VALUE_SEPARATOR">VALUE_SEPARATOR</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ModelTextCreator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#appendAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.text.builders.TextBuilder)">appendAssociationEnd</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier)">createActivityEdgeText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> activityEdge,
 boolean showWeight,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean,java.util.function.Supplier)">createActivityParameterNodeText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> parameterNode,
 boolean showFullType,
 boolean showTypePrefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier)">createActivityParameterNodeText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> parameterNode,
 boolean showFullType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier)">createAssociationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)">createBehaviorText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 <a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier)">createCombinedFragmentOperatorText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> combinedFragment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier)">createConstraintsText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a href="ConstraintTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ConstraintTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a> elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier)">createConstraintText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a href="ConstraintTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ConstraintTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)">createEnumerationLiteralText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumerationLiteral,
 <a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier)">createEventText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event,
 <a href="EventTextParams.html" title="class in com.nomagic.magicdraw.uml.text">EventTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier)">createGuardText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the provided message's guard.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier)">createInstanceSpecificationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="InstanceSpecificationTextParams.html" title="class in com.nomagic.magicdraw.uml.text">InstanceSpecificationTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier,java.util.function.Predicate)">createInstanceSpecificationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="InstanceSpecificationTextParams.html" title="class in com.nomagic.magicdraw.uml.text">InstanceSpecificationTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; classifierFilter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier)">createInteractionUseText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> callBehaviorAction,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a> that is displayed as InteractionUse.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier)">createInteractionUseText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> interactionUse,
 <a href="InteractionUseTextParams.html" title="class in com.nomagic.magicdraw.uml.text">InteractionUseTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier)">createMessageText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="MessageTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MessageTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier)">createOperandGuardText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> interactionOperand,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation for the guard of the given <a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)">createOperationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a href="OperationTextParams.html" title="class in com.nomagic.magicdraw.uml.text">OperationTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterDirectionText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,com.nomagic.uml2.project.ElementProject,com.nomagic.magicdraw.uml.text.ParameterDirectionTextParams,java.util.function.Supplier)">createParameterDirectionText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> parameterDirection,
 com.nomagic.uml2.project.ElementProject project,
 <a href="ParameterDirectionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ParameterDirectionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ParameterDirectionKind</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)">createParametersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameters,
 <a href="ParameterTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ParameterTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a> elements, separated by comma</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)">createParameterText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 <a href="ParameterTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ParameterTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier)">createPinText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> pin,
 <a href="PinTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PinTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)">createPropertyText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)">createProtocolTransitionText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition,
 <a href="TransitionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TransitionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)">createReceptionText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 <a href="ReceptionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ReceptionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier)">createRelationshipFromToText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> clientName,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> supplierName,
 boolean addFullQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create relation representation text part to represent from what element to what element relation is connected.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)">createSlotsText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of given slots collection (without braces).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)">createSlotsTextWithBraces</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of given slots collection, wrapped between '{' and '}'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)">createSlotText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given slot.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier,com.nomagic.magicdraw.uml.text.RepTextContext)">createSlotText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory,
 <a href="RepTextContext.html" title="class in com.nomagic.magicdraw.uml.text">RepTextContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given slot.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier)">createStateText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> state,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTaggedValuesText(java.util.Collection,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.lang.String,java.util.function.Supplier)">createTaggedValuesText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt; taggedValues,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of given taggedValues collection (without braces).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTaggedValuesTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.lang.String,java.util.function.Supplier)">createTaggedValuesTextWithBraces</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt; taggedValues,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of given taggedValues collection, wrapped between '{' and '}'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTaggedValueText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.util.function.Supplier)">createTaggedValueText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given taggedValue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTaggedValueText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.util.function.Supplier,com.nomagic.magicdraw.uml.text.RepTextContext)">createTaggedValueText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory,
 <a href="RepTextContext.html" title="class in com.nomagic.magicdraw.uml.text">RepTextContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given taggedValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean,java.util.function.Supplier)">createTemplateBindingText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> templateBinding,
 boolean showTemplateParameterInfo,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier)">createTemplateParametersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a>&gt; templateParameters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a> elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier)">createTemplateParameterSubstitutionText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> parameterSubstitution,
 boolean showTemplateParameterInfo,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier)">createTemplateParameterText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> templateParameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)">createTransitionText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 <a href="TransitionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TransitionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given Transition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)">createTriggersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; triggers,
 <a href="TriggerTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TriggerTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a> elements, separated by comma.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)">createTriggerText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger,
 <a href="TriggerTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TriggerTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier)">createTypedElementText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> typedElement,
 <a href="TypedElementTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TypedElementTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.text.CoreTextCreator">Methods inherited from class com.nomagic.magicdraw.uml.text.<a href="CoreTextCreator.html" title="class in com.nomagic.magicdraw.uml.text">CoreTextCreator</a></h3>
<code><a href="CoreTextCreator.html#appendPrefix(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.text.builders.TextBuilder)">appendPrefix</a>, <a href="CoreTextCreator.html#containsParentheses(java.lang.String)">containsParentheses</a>, <a href="CoreTextCreator.html#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier)">createElementNumberText</a>, <a href="CoreTextCreator.html#createMultiplicityRangeText(java.lang.Integer)">createMultiplicityRangeText</a>, <a href="CoreTextCreator.html#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">createMultiplicityText</a>, <a href="CoreTextCreator.html#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">createMultiplicityText</a>, <a href="CoreTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">createMultiplicityText</a>, <a href="CoreTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer)">createMultiplicityText</a>, <a href="CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)">createMultiplicityText</a>, <a href="CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)">createMultiplicityText</a>, <a href="CoreTextCreator.html#createNamedElementListText(java.util.List,java.util.function.Supplier)">createNamedElementListText</a>, <a href="CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">createStereotypesText</a>, <a href="CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">createStereotypesText</a>, <a href="CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">createStereotypeText</a>, <a href="CoreTextCreator.html#createStereotypeText(java.lang.String)">createStereotypeText</a>, <a href="CoreTextCreator.html#createStringCollectionText(java.util.Collection,java.lang.String,java.util.function.Supplier)">createStringCollectionText</a>, <a href="CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean,java.util.function.Supplier)">createStyledTypeText</a>, <a href="CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">createStyledTypeText</a>, <a href="CoreTextCreator.html#createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean,java.util.function.Supplier)">createStyledTypeTextWithSeparator</a>, <a href="CoreTextCreator.html#createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">createStyledTypeTextWithSeparator</a>, <a href="CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean,java.util.function.Supplier)">createTypeText</a>, <a href="CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">createTypeText</a>, <a href="CoreTextCreator.html#createTypeText(java.util.Collection,boolean,boolean,java.util.function.Supplier)">createTypeText</a>, <a href="CoreTextCreator.html#createTypeText(java.util.Collection,boolean,java.util.function.Supplier)">createTypeText</a>, <a href="CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier)">createValueSpecificationText</a>, <a href="CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier)">createValueSpecificationText</a>, <a href="CoreTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">createVisibilityText</a>, <a href="CoreTextCreator.html#isUseStandardStereotypeChar()">isUseStandardStereotypeChar</a>, <a href="CoreTextCreator.html#join(com.nomagic.text.builders.TextBuilder,java.lang.String,java.util.stream.Stream,java.util.function.Function)">join</a>, <a href="CoreTextCreator.html#setUseStandardStereotypeChar(boolean)">setUseStandardStereotypeChar</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="ELEMENTS_PROPERTY_KEY">
<h3>ELEMENTS_PROPERTY_KEY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ELEMENTS_PROPERTY_KEY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.ModelTextCreator.ELEMENTS_PROPERTY_KEY">Constant Field Values</a></li>
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
<h3>ModelTextCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModelTextCreator</span>()</div>
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
<section class="detail" id="createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier)">
<h3>createActivityEdgeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createActivityEdgeText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> activityEdge,
 boolean showWeight,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activityEdge</code> - element to create representation text for</dd>
<dd><code>showWeight</code> - when true, weight information will be included to the text</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the activity edge's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier)">
<h3>createConstraintsText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createConstraintsText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a href="ConstraintTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ConstraintTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a> elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraints</code> - collection of constraint elements to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the constraint</dd>
<dd><code>separator</code> - symbol(s) to separate each constraint's text with</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the constraints' text appended</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier)"><code>createConstraintText(Constraint, ConstraintTextParams, Supplier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier)">
<h3>createConstraintText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createConstraintText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a href="ConstraintTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ConstraintTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the constraint</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the constraint's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier)">
<h3>createPinText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createPinText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> pin,
 <a href="PinTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PinTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>Pin</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pin</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the pin</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the pin's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier)">
<h3>createCombinedFragmentOperatorText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createCombinedFragmentOperatorText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> combinedFragment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>CombinedFragment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>combinedFragment</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the combinedFragment's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier)">
<h3>createOperandGuardText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createOperandGuardText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> interactionOperand,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation for the guard of the given <a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionOperand</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interactionOperand</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the guard's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)">
<h3>createTransitionText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTransitionText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 <a href="TransitionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TransitionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given Transition. Keep in mind that text is different for protocol transition.<br/>
 Syntax of <a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>: <code>trigger[guard]/effect</code>.<br/>
 Syntax of <a href="../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>: <code>[precondition]trigger/[postcondition]</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the ?</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the transition's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)">
<h3>createProtocolTransitionText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createProtocolTransitionText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition,
 <a href="TransitionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TransitionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines"><code>ProtocolTransition</code></a>.
 Syntax: <code>[precondition]trigger/[postcondition]</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the ?</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the transition's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)">
<h3>createTriggersText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTriggersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; triggers,
 <a href="TriggerTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TriggerTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a> elements, separated by comma.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>triggers</code> - collection of trigger elements to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the trigger</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the trigger's text appended</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)">
<h3>createTriggerText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTriggerText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger,
 <a href="TriggerTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TriggerTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>trigger</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the trigger</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the trigger's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier)">
<h3>createEventText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createEventText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event,
 <a href="EventTextParams.html" title="class in com.nomagic.magicdraw.uml.text">EventTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the event</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the event's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)">
<h3>createBehaviorText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createBehaviorText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 <a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the behavior</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the behavior's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier)">
<h3>createInteractionUseText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createInteractionUseText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> interactionUse,
 <a href="InteractionUseTextParams.html" title="class in com.nomagic.magicdraw.uml.text">InteractionUseTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>interactionUse</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the interactionUse</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the interactionUse's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier)">
<h3>createInteractionUseText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createInteractionUseText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> callBehaviorAction,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a> that is displayed as InteractionUse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callBehaviorAction</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the action's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.text.MessageTextParams,java.util.function.Supplier)">
<h3>createMessageText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createMessageText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="MessageTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MessageTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the message</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the message's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier)">
<h3>createAssociationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createAssociationText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the association's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier)">
<h3>createStateText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStateText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> state,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the state's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)">
<h3>createParametersText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createParametersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameters,
 <a href="ParameterTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ParameterTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a> elements, separated by comma</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameters</code> - collection of parameters to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of each parameter</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the parameters' text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)">
<h3>createParameterText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createParameterText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 <a href="ParameterTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ParameterTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameter</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the parameter</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the parameter's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterDirectionText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,com.nomagic.uml2.project.ElementProject,com.nomagic.magicdraw.uml.text.ParameterDirectionTextParams,java.util.function.Supplier)">
<h3>createParameterDirectionText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createParameterDirectionText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> parameterDirection,
 com.nomagic.uml2.project.ElementProject project,
 <a href="ParameterDirectionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ParameterDirectionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ParameterDirectionKind</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterDirection</code> - direction to create representation text for</dd>
<dd><code>project</code> - project to which parameter belongs</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the parameter direction</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the parameter direction text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)">
<h3>createOperationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createOperationText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a href="OperationTextParams.html" title="class in com.nomagic.magicdraw.uml.text">OperationTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the operation</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the operation's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)">
<h3>createReceptionText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createReceptionText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 <a href="ReceptionTextParams.html" title="class in com.nomagic.magicdraw.uml.text">ReceptionTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reception</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the reception</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the reception's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)">
<h3>createPropertyText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createPropertyText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the property</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the property's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean,java.util.function.Supplier)">
<h3>createActivityParameterNodeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createActivityParameterNodeText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> parameterNode,
 boolean showFullType,
 boolean showTypePrefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterNode</code> - element to create representation text for</dd>
<dd><code>showFullType</code> - true if qualified name should be included in the text of node's type</dd>
<dd><code>showTypePrefix</code> - true to include type's prefix</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the node's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier)">
<h3>createActivityParameterNodeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createActivityParameterNodeText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> parameterNode,
 boolean showFullType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterNode</code> - element to create representation text for</dd>
<dd><code>showFullType</code> - true if qualified name should be included in the text of node's type</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the node's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier)">
<h3>createGuardText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createGuardText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the provided message's guard.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - element for which guard representation text has to be created</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the guard's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)">
<h3>createEnumerationLiteralText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createEnumerationLiteralText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumerationLiteral,
 <a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>EnumerationLiteral</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumerationLiteral</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the enumeration literal</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the enumeration literal's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier)">
<h3>createTemplateParameterText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTemplateParameterText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> templateParameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateParameter</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the template parameter's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier)">
<h3>createTemplateParametersText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTemplateParametersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a>&gt; templateParameters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation for the given collection of <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a> elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateParameters</code> - collection of template parameter elements to create representation text for</dd>
<dd><code>separator</code> - symbol(s) to separate each parameter's text with</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the parameters' text appended</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier)"><code>createTemplateParameterText(TemplateParameter, Supplier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean,java.util.function.Supplier)">
<h3>createTemplateBindingText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTemplateBindingText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> templateBinding,
 boolean showTemplateParameterInfo,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateBinding</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBinding</code> - element to create representation text for</dd>
<dd><code>showTemplateParameterInfo</code> - indicates if full template parameter notation should be used.</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the template binding's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier)">
<h3>createTemplateParameterSubstitutionText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTemplateParameterSubstitutionText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> parameterSubstitution,
 boolean showTemplateParameterInfo,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterSubstitution</code> - element to create representation text for</dd>
<dd><code>showTemplateParameterInfo</code> - indicates if full template parameter notation should be used.</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the parameter substitution's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier)">
<h3>createInstanceSpecificationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createInstanceSpecificationText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="InstanceSpecificationTextParams.html" title="class in com.nomagic.magicdraw.uml.text">InstanceSpecificationTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the instance</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the instance's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier,java.util.function.Predicate)">
<h3>createInstanceSpecificationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createInstanceSpecificationText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="InstanceSpecificationTextParams.html" title="class in com.nomagic.magicdraw.uml.text">InstanceSpecificationTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; classifierFilter)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the instance</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dd><code>classifierFilter</code> - provides ability to filter classifiers.</dd>
<dt>Returns:</dt>
<dd>builder with the instance's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier)">
<h3>createRelationshipFromToText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createRelationshipFromToText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> clientName,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> supplierName,
 boolean addFullQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Create relation representation text part to represent from what element to what element relation is connected.
 For example if we connect Connector to 2 properties a and b, that are Owned by class Class1. In Containment
 browser we would see "Connector[Class1::a - Class1::b]" so this method returns the part for the representation
 "[Class1::a - Class1::b]".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship for which we want the representation part</dd>
<dd><code>clientModelElement</code> - first (from) element</dd>
<dd><code>clientName</code> - name or custom text of first (from) element</dd>
<dd><code>supplierModelElement</code> - second (to) element</dd>
<dd><code>supplierName</code> - name or custom text of second (to) element</dd>
<dd><code>addFullQualifiedName</code> - if true, full qualified name will be added to client and supplier names</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the relation text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.text.builders.TextBuilder)">
<h3>appendAssociationEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">appendAssociationEnd</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> builder)</span></div>
</section>
</li>
<li>
<section class="detail" id="createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier)">
<h3>createTypedElementText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTypedElementText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> typedElement,
 <a href="TypedElementTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TypedElementTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>typedElement</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the typed element</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the typed element's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)">
<h3>createSlotsTextWithBraces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createSlotsTextWithBraces</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of given slots collection, wrapped between '{' and '}'.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slots</code> - collection of slots</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a slot</dd>
<dd><code>separator</code> - symbol(s) to separate each slot's text with</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the slots text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)">
<h3>createSlotsText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createSlotsText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of given slots collection (without braces).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slots</code> - collection of slots</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a slot</dd>
<dd><code>separator</code> - symbol(s) to separate each slot's text with</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the slots text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)">
<h3>createSlotText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createSlotText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given slot.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a slot</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the slot's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier,com.nomagic.magicdraw.uml.text.RepTextContext)">
<h3>createSlotText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createSlotText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 <a href="SlotTextParams.html" title="class in com.nomagic.magicdraw.uml.text">SlotTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory,
 <a href="RepTextContext.html" title="class in com.nomagic.magicdraw.uml.text">RepTextContext</a> context)</span></div>
<div class="block">Creates string representation of the given slot.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a slot</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dd><code>context</code> - representation text creator invoker</dd>
<dt>Returns:</dt>
<dd>builder with the slot's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTaggedValuesText(java.util.Collection,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.lang.String,java.util.function.Supplier)">
<h3>createTaggedValuesText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTaggedValuesText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt; taggedValues,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of given taggedValues collection (without braces).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValues</code> - collection of taggedValues</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a slot</dd>
<dd><code>separator</code> - symbol(s) to separate each slot's text with</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the taggedValues text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTaggedValueText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.util.function.Supplier)">
<h3>createTaggedValueText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTaggedValueText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given taggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a taggedValue</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the taggedValue's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTaggedValueText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.util.function.Supplier,com.nomagic.magicdraw.uml.text.RepTextContext)">
<h3>createTaggedValueText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTaggedValueText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory,
 <a href="RepTextContext.html" title="class in com.nomagic.magicdraw.uml.text">RepTextContext</a> context)</span></div>
<div class="block">Creates string representation of the given taggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a taggedValue</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the taggedValue's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTaggedValuesTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.TaggedValueTextParams,java.lang.String,java.util.function.Supplier)">
<h3>createTaggedValuesTextWithBraces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTaggedValuesTextWithBraces</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt; taggedValues,
 <a href="TaggedValueTextParams.html" title="class in com.nomagic.magicdraw.uml.text">TaggedValueTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of given taggedValues collection, wrapped between '{' and '}'.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValues</code> - collection of taggedValues</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of a slot</dd>
<dd><code>separator</code> - symbol(s) to separate each slot's text with</dd>
<dd><code>builderFactory</code> - provides  <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append created text to</dd>
<dt>Returns:</dt>
<dd>builder with the taggedValues text appended</dd>
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
