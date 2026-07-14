# JAVA OPENAPI: DeprecatedRepresentationTextCreator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/DeprecatedRepresentationTextCreator.html
- source_path: `com/nomagic/magicdraw/uml/DeprecatedRepresentationTextCreator.html`
- source_sha256: `a03a3d77c22354b26fdf1aadeadeb56b3cc8d983e09e35722bf20249f8a9ba96`
- captured_utc: `2026-07-14T16:55:53.907441+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class DeprecatedRepresentationTextCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator

Direct Known Subclasses:
`[RepresentationTextCreator](RepresentationTextCreator.html)`

@OpenApiAllpublic classDeprecatedRepresentationTextCreator
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Deprecated OpenApi methods of RepresentationTextCreator that should not be used any more

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COLOR_POSTFIX](#COLOR_POSTFIX)`
Deprecated.
use [`RichTextStringUtils.COLOR_POSTFIX`](../../text/rich/RichTextStringUtils.html#COLOR_POSTFIX)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COLOR_PREFIX](#COLOR_PREFIX)`
Deprecated.
use [`RichTextStringUtils.COLOR_PREFIX`](../../text/rich/RichTextStringUtils.html#COLOR_PREFIX)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EMPTY_NAME_NOTATION](#EMPTY_NAME_NOTATION)`
Deprecated.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[GRAY_COLOR_STRING](#GRAY_COLOR_STRING)`
Deprecated.
use [`RichTextStringUtils.GRAY_COLOR`](../../text/rich/RichTextStringUtils.html#GRAY_COLOR)
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DeprecatedRepresentationTextCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[appendColor](#appendColor(java.lang.StringBuffer,java.awt.Color))([StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`
Deprecated.
use [`RichTextStringUtils.startColor(StringBuffer, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuffer,java.awt.Color))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[appendColor](#appendColor(java.lang.String,java.awt.Color))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[appendGrayColor](#appendGrayColor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
`static void`
`[appendGrayColor](#appendGrayColor(java.lang.StringBuffer))([StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text)`
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructActivityEdgeText](#constructActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean))([ActivityEdge](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html) activityEdge,
 boolean showWeight)`
Deprecated.
use [`ModelTextCreator.createActivityEdgeText(ActivityEdge, boolean, Supplier)`](text/ModelTextCreator.html#createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructCombinedFragmentOperatorText](#constructCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))([CombinedFragment](../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html) combinedFragment)`
Deprecated.
use [`ModelTextCreator.createCombinedFragmentOperatorText(CombinedFragment, Supplier)`](text/ModelTextCreator.html#createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createActivityParameterNodeText](#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean))([ActivityParameterNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) parameter,
 boolean showFullType,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createActivityParameterNodeText(ActivityParameterNode, boolean, Supplier)`](text/ModelTextCreator.html#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAssociationText](#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
Deprecated.
use [`ModelTextCreator.createAssociationText(Association, Supplier)`](text/ModelTextCreator.html#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createBehaviorText](#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior)`
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createBehaviorText](#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind)`
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createBehaviorText](#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)`
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createBehaviorText](#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)`
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createClassifierName](#createClassifierName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean,boolean))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 boolean showFullType,
 boolean addColorInformation)`
Deprecated.
use [`CoreTextCreator.createTypeText(Type, boolean, Supplier)`](text/CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createClassifiersRepresentation](#createClassifiersRepresentation(java.util.Collection,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) classifiers,
 boolean showFullType,
 boolean addColorInformation)`
Deprecated.
use [`CoreTextCreator.createTypeText(Collection, boolean, Supplier)`](text/CoreTextCreator.html#createTypeText(java.util.Collection,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createConstraintsText](#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean,boolean,boolean))([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)`
Deprecated.
use [`ModelTextCreator.createConstraintText(Constraint, ConstraintTextParams, Supplier)`](text/ModelTextCreator.html#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createConstraintsText](#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean))([ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 boolean addBrackets)`
Deprecated.
use [`CoreTextCreator.createValueSpecificationText(ValueSpecification, boolean, Supplier)`](text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createConstraintsText](#createConstraintsText(java.util.Collection,java.lang.String,boolean,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)`
Deprecated.
use [`ModelTextCreator.createConstraintsText(Collection, ConstraintTextParams, String, Supplier)`](text/ModelTextCreator.html#createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createDefaultRepresentationText](#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean))([BaseElement](BaseElement.html) element,
 boolean addColor,
 boolean fullSignature)`
Deprecated.
use [`RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createDefaultRepresentationText](#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean))([BaseElement](BaseElement.html) element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId)`
Deprecated.
use [`RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createDefaultRepresentationText](#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool))([BaseElement](BaseElement.html) element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId,
 [LocationInTool](../ui/LocationInTool.html) locationInTool)`
Deprecated.
use [`RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createElementNameText](#createElementNameText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) o)`
Deprecated.
use [`NamedElement.getName()`](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html#getName())
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createEnumerationLiteralText](#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression)`
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createEnumerationLiteralText](#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)`
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createEnumerationLiteralText](#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)`
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createEnumerationLiteralText](#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createEventText](#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event))([Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event)`
Deprecated.
use [`ModelTextCreator.createEventText(Event, EventTextParams, Supplier)`](text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createEventText](#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,boolean,boolean))([Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)`
Deprecated.
use [`ModelTextCreator.createEventText(Event, EventTextParams, Supplier)`](text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createGuardText](#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)`
Deprecated.
use [`ModelTextCreator.createGuardText(Message, Supplier)`](text/ModelTextCreator.html#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createId](#createId(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e,
 boolean addColor)`
Deprecated.
use [`CoreTextCreator.createElementNumberText(Element, Supplier)`](text/CoreTextCreator.html#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createInstanceSpecificationText](#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor)`
Deprecated.
use [`ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)`](text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createInstanceSpecificationText](#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean,boolean))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor,
 boolean showAutoID)`
Deprecated.
use [`ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)`](text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createInteractionUseText](#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction))([CallBehaviorAction](../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) interactionUse)`
Deprecated.
use [`ModelTextCreator.createInteractionUseText(CallBehaviorAction, Supplier)`](text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createInteractionUseText](#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean,boolean))([InteractionUse](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html) interactionUse,
 boolean addReferTo,
 boolean addArguments)`
Deprecated.
use [`ModelTextCreator.createInteractionUseText(InteractionUse, InteractionUseTextParams, Supplier)`](text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityRangeText](#createMultiplicityRangeText(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) range)`
Deprecated.
use [`CoreTextCreator.createMultiplicityRangeText(Integer)`](text/CoreTextCreator.html#createMultiplicityRangeText(java.lang.Integer))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,boolean,boolean,boolean))([MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) multiplicity,
 boolean showOrder,
 boolean showUnique,
 boolean addBrackets)`
Deprecated.
use [`CoreTextCreator.createMultiplicityText(MultiplicityElement, MultiplicityTextParams, Supplier)`](text/CoreTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(java.lang.Integer,java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lower,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) upper)`
Deprecated.
use [`CoreTextCreator.createMultiplicityText(Integer, Integer)`](text/CoreTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 boolean ordered,
 boolean unique,
 boolean addBrackets)`
Deprecated.
use [`CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)`](text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) lowerValue,
 boolean unique,
 boolean ordered,
 boolean addBrackets)`
Deprecated.
use [`CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)`](text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createNamedElementListText](#createNamedElementListText(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> elements)`
Deprecated.
use [`CoreTextCreator.createNamedElementListText(java.util.List, Supplier)`](text/CoreTextCreator.html#createNamedElementListText(java.util.List,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createOperandGuardText](#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand))([InteractionOperand](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html) operand)`
Deprecated.
use [`ModelTextCreator.createOperandGuardText(InteractionOperand, Supplier)`](text/ModelTextCreator.html#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createOperationText](#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters)`
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createOperationText](#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue)`
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createOperationText](#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)`
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createOperationText](#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)`
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createParameterDirectionText](#createParameterDirectionText(com.nomagic.magicdraw.core.Project,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,boolean,boolean,boolean))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameterMetaType,
 [ParameterDirectionKind](../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html) parameterDirection,
 boolean skipDefaultValue,
 boolean showReturnDirection,
 boolean addColorInformation)`
Deprecated.
use `ModelTextCreator#createParameterDirectionText(ParameterDirectionKind, Project, ParameterDirectionTextParams, Supplier)`
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createParametersText](#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createParametersText](#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showParameterDefaultValue)`
Deprecated.
use [`ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createParameterText](#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean))([Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createParameterText(Parameter, ParameterTextParams, Supplier)`](text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createParameterText](#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean))([Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue)`
Deprecated.
use [`ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createParameterText](#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean,boolean,boolean))([Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue,
 boolean skipDefaultDirection,
 boolean showReturnDirection)`
Deprecated.
use [`ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPinText](#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,boolean,boolean,boolean,boolean,boolean,boolean))([Pin](../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html) pin,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor,
 boolean showSynchronizationInfo)`
Deprecated.
use [`ModelTextCreator.createPinText(Pin, PinTextParams, Supplier)`](text/ModelTextCreator.html#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPortText](#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean))([Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPortText](#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean))([Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showInheritedSign,
 boolean addColor)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPortText](#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean addColor)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static void`
`[createPropertyPropertyStringText](#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text)`
Deprecated.
use `ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder)`
`static void`
`[createPropertyPropertyStringText](#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer,java.lang.String))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Deprecated.
use `ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder, String)`
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPropertyText](#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraints,
 boolean showMultiplicity,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPropertyText](#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPropertyText](#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPropertyText](#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPropertyText](#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createProtocolTransitionText](#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition))([ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition)`
Deprecated.
use [`ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createProtocolTransitionText](#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean))([ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition,
 boolean showPort)`
Deprecated.
use [`ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createProtocolTransitionText](#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean,boolean,boolean))([ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)`
Deprecated.
use [`ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createPureSlotsString](#createPureSlotsString(java.util.Collection,java.lang.String,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean showHTML,
 boolean showEmptyValue)`
Deprecated.
use [`ModelTextCreator.createSlotsText(Collection, SlotTextParams, String, Supplier)`](text/ModelTextCreator.html#createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createReceptionText](#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)`](text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createReceptionText](#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)`](text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createReceptionText](#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)`
Deprecated.
use [`ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)`](text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))
`static [Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[BaseElement](BaseElement.html)>`
`[createRepresentationTextComparator](#createRepresentationTextComparator(boolean,boolean))(boolean addColor,
 boolean showAutoId)`
Deprecated.
use [`RepresentationTextCreator.createRepresentationTextComparator(RepresentationTextParams)`](RepresentationTextCreator.html#createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createSlotsText](#createSlotsText(java.util.Collection,java.lang.String,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean showHTML,
 boolean showEmptyValue)`
Deprecated.
use [`ModelTextCreator.createSlotsTextWithBraces(Collection, SlotTextParams, String, Supplier)`](text/ModelTextCreator.html#createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createSlotText](#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)`
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createSlotText](#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)`
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createSlotText](#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived)`
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createSlotText](#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived,
 boolean forEditing,
 boolean colorUnitSymbols,
 boolean colorTag)`
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStateText](#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) state)`
Deprecated.
use [`ModelTextCreator.createStateText(State, Supplier)`](text/ModelTextCreator.html#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypesText](#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 char separator)`
Deprecated.
use [`CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypesText](#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 char separator,
 boolean skipDSL,
 boolean useAlias)`
Deprecated.
use [`CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypesText](#createStereotypesText(java.util.Collection,char))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 char separator)`
Deprecated.
use [`CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypesText](#createStereotypesText(java.util.Collection,char,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 char separator,
 boolean skipDSL,
 boolean useAlias)`
Deprecated.
use [`CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypeText](#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Deprecated.
use [`CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypeText](#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean useAlias)`
Deprecated.
use [`CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypeText](#createStereotypeText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Deprecated.
use [`CoreTextCreator.createStereotypeText(String)`](text/CoreTextCreator.html#createStereotypeText(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTemplateBindingText](#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding))([TemplateBinding](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) binding)`
Constructs given binding element text.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTemplateBindingText](#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean))([TemplateBinding](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) binding,
 boolean attachTemplateParameterInfo)`
Constructs given binding element text.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTemplateParametersText](#createTemplateParametersText(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) templateParameters,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Deprecated.
use [`ModelTextCreator.createTemplateParametersText(Collection, String, Supplier)`](text/ModelTextCreator.html#createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTemplateParameterSubstitutionText](#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean))([TemplateParameterSubstitution](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) parameterSubstitution,
 boolean attachTemplateParameterInfo)`
Deprecated.
use [`ModelTextCreator.createTemplateParameterSubstitutionText(TemplateParameterSubstitution, boolean, Supplier)`](text/ModelTextCreator.html#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTemplateParameterText](#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))([TemplateParameter](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) tParameter)`
Deprecated.
use [`ModelTextCreator.createTemplateParameterText(TemplateParameter, Supplier)`](text/ModelTextCreator.html#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTransitionText](#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean))([Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 boolean showEffect)`
Deprecated.
use [`ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTransitionText](#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean))([Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody)`
Deprecated.
use [`ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTransitionText](#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean,boolean,boolean))([Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)`
Deprecated.
use [`ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTriggersText](#createTriggersText(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) triggers)`
Deprecated.
use [`ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTriggersText](#createTriggersText(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) triggers,
 boolean showPort)`
Deprecated.
use [`ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTriggersText](#createTriggersText(java.util.Collection,boolean,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) triggers,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)`
Deprecated.
use [`ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTriggerText](#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger))([Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger)`
Deprecated.
use [`ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTriggerText](#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean))([Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger,
 boolean showPort)`
Deprecated.
use [`ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTriggerText](#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean,boolean,boolean))([Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)`
Deprecated.
use [`ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTypedElementText](#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,boolean,boolean,boolean,boolean,boolean))([TypedElement](../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) typedElement,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)`
Deprecated.
use [`ModelTextCreator.createTypedElementText(TypedElement, TypedElementTextParams, Supplier)`](text/ModelTextCreator.html#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createTypeName](#createTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean))([Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showFullType,
 boolean addColorInformation)`
Deprecated.
use [`CoreTextCreator.createStyledTypeText(Type, boolean, Supplier)`](text/CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createValueSpecificationText](#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) specification)`
Deprecated.
use [`CoreTextCreator.createValueSpecificationText(ValueSpecification, Supplier)`](text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier))
`static char`
`[createVisibilityText](#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))([VisibilityKind](../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html) visibility)`
Deprecated.
use [`CoreTextCreator.createVisibilityText(VisibilityKind)`](text/CoreTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[endColorHtmlTag](#endColorHtmlTag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`RichTextStringUtils.closeColor(String)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String))
`static void`
`[endColorHtmlTag](#endColorHtmlTag(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html) text)`
Deprecated.
use [`RichTextStringUtils.closeColor(StringBuilder)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuilder))
`[LocationInTool](../ui/LocationInTool.html)`
`[getLocationInTool](#getLocationInTool())()`
Deprecated.
text creation parameters are now retrieved from [`RepresentationTextParams`](RepresentationTextParams.html) which is passed as argument for various methods
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPureTextFromColoredText](#getPureTextFromColoredText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) coloredText)`
Deprecated.
use [`TextUtils.toPlainText(String)`](../../text/TextUtils.html#toPlainText(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRelationshipFromToRepresentation](#getRelationshipFromToRepresentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) clientModelElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clientName,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplierModelElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) supplierName,
 boolean showFullType,
 boolean addColor)`
Deprecated.
use [`ModelTextCreator.createRelationshipFromToText(Element, Element, String, Element, String, boolean, Supplier)`](text/ModelTextCreator.html#createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](BaseElement.html) el,
 boolean addColor)`
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean))([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber)`
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean))([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature)`
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean))([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 boolean noCache)`
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool,boolean))([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 [LocationInTool](../ui/LocationInTool.html) locationInTool,
 boolean noCache)`
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean))
`boolean`
`[isAddColor](#isAddColor())()`
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
`boolean`
`[isShowFullType](#isShowFullType())()`
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[resetColor](#resetColor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`RichTextStringUtils.closeColor(String)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String))
`static void`
`[resetColor](#resetColor(java.lang.StringBuffer))([StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text)`
Deprecated.
use [`RichTextStringUtils.closeColor(StringBuffer)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuffer))
`void`
`[setAddColor](#setAddColor(boolean))(boolean addColor)`
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
`void`
`[setLocationInTool](#setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool))([LocationInTool](../ui/LocationInTool.html) locationInTool)`
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
`void`
`[setShowFullType](#setShowFullType(boolean))(boolean value)`
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
`static void`
`[startColorHtmlTag](#startColorHtmlTag(java.lang.StringBuilder,java.awt.Color))([StringBuilder](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`
Deprecated.
use [`RichTextStringUtils.startColor(StringBuilder, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuilder,java.awt.Color))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[startColorHtmlTag](#startColorHtmlTag(java.lang.String,java.awt.Color))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
EMPTY_NAME_NOTATION
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EMPTY_NAME_NOTATION
Deprecated.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator.EMPTY_NAME_NOTATION)
COLOR_PREFIX
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COLOR_PREFIX
Deprecated.
use [`RichTextStringUtils.COLOR_PREFIX`](../../text/rich/RichTextStringUtils.html#COLOR_PREFIX)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator.COLOR_PREFIX)
COLOR_POSTFIX
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COLOR_POSTFIX
Deprecated.
use [`RichTextStringUtils.COLOR_POSTFIX`](../../text/rich/RichTextStringUtils.html#COLOR_POSTFIX)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator.COLOR_POSTFIX)
GRAY_COLOR_STRING
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GRAY_COLOR_STRING
Deprecated.
use [`RichTextStringUtils.GRAY_COLOR`](../../text/rich/RichTextStringUtils.html#GRAY_COLOR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DeprecatedRepresentationTextCreator
public DeprecatedRepresentationTextCreator()
 ============ METHOD DETAIL ========== 
Method Details
createTransitionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTransitionText([Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 boolean showEffect)
Deprecated.
use [`ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
createTransitionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTransitionText([Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody)
Deprecated.
use [`ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
createTransitionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTransitionText([Transition](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)
Deprecated.
use [`ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
createProtocolTransitionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createProtocolTransitionText([ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition)
Deprecated.
use [`ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
createProtocolTransitionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createProtocolTransitionText([ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition,
 boolean showPort)
Deprecated.
use [`ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
createProtocolTransitionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createProtocolTransitionText([ProtocolTransition](../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html) transition,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)
Deprecated.
use [`ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)`](text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier))
createTriggersText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTriggersText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) triggers)
Deprecated.
use [`ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createTriggersText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTriggersText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) triggers,
 boolean showPort)
Deprecated.
use [`ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createTriggersText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTriggersText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) triggers,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)
Deprecated.
use [`ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createTriggerText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTriggerText([Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger)
Deprecated.
use [`ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createTriggerText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTriggerText([Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger,
 boolean showPort)
Deprecated.
use [`ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createTriggerText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTriggerText([Trigger](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html) trigger,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)
Deprecated.
use [`ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)`](text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier))
createEventText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createEventText([Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event)
Deprecated.
use [`ModelTextCreator.createEventText(Event, EventTextParams, Supplier)`](text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier))
createEventText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createEventText([Event](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html) event,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)
Deprecated.
use [`ModelTextCreator.createEventText(Event, EventTextParams, Supplier)`](text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier))
createSlotText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createSlotText([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
Returns string representation of given tag definition.
Parameters:
`slot` - The given slot.
`showName` - Is show name?
`ignoreTrueValues` - Is ignore true values?
`showHTML` - True for show htm
`showFeatureType` - Is show feature type?
`showFullType` - True for show full type.
`addColorInformation` - True for set color.
`showEmptyValue` - show empty value
`showQualifiedName` - show qualified name
Returns:
The created string.
createSlotText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createSlotText(@Nonnull
 [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
Returns string representation of given tag definition.
Parameters:
`slot` - The given slot.
`showName` - Is show name?
`ignoreTrueValues` - Is ignore true values?
`showHTML` - True for show htm
`showFeatureType` - Is show feature type?
`showFullType` - True for show full type.
`showFeatureTypeTaggedValues` - show feature type tagged values
`addColorInformation` - True for set color.
`showEmptyValue` - show empty value
`showQualifiedName` - show qualified name
Returns:
The created string.
createSlotText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createSlotText(@Nonnull
 [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived)
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
Returns string representation of given tag definition.
Parameters:
`slot` - The given slot.
`showName` - Is show name?
`ignoreTrueValues` - Is ignore true values?
`showHTML` - True for show htm
`showFeatureType` - Is show feature type?
`showFullType` - True for show full type.
`showFeatureTypeTaggedValues` - show feature type tagged values
`addColorInformation` - True for set color.
`showEmptyValue` - show empty value
`showQualifiedName` - show qualified name
`showDerived` - if true returned string will be calculated as derived if possible
Returns:
The created string.
createSlotText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createSlotText([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived,
 boolean forEditing,
 boolean colorUnitSymbols,
 boolean colorTag)
Deprecated.
use [`ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)`](text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier))
Returns string representation of given tag definition.
Parameters:
`slot` - The given slot.
`showName` - Is show name?
`ignoreTrueValues` - Is ignore true values?
`showHTML` - True for show htm
`showFeatureType` - Is show feature type?
`showFullType` - True for show full type.
`showFeatureTypeTaggedValues` - show feature type tagged values
`addColorInformation` - True for set color.
`showEmptyValue` - show empty value
`showQualifiedName` - show qualified name
`showDerived` - if true returned string will be calculated as derived if possible
`forEditing` - flag to indicate that we need text for editing, so no additional text providers will be used
`colorUnitSymbols` - flag to indicate if we need to use color for additional text providers, we can't use addColorInformation, as we use same
 provider for instances that don't have color information property
`colorTag` - indicates if we need color tag or font color tag if we use in additional text providers
Returns:
The created string.
createPureSlotsString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPureSlotsString([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean showHTML,
 boolean showEmptyValue)
Deprecated.
use [`ModelTextCreator.createSlotsText(Collection, SlotTextParams, String, Supplier)`](text/ModelTextCreator.html#createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier))
createSlotsText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createSlotsText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)> slots,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean showHTML,
 boolean showEmptyValue)
Deprecated.
use [`ModelTextCreator.createSlotsTextWithBraces(Collection, SlotTextParams, String, Supplier)`](text/ModelTextCreator.html#createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier))
createConstraintsText
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createConstraintsText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)
Deprecated.
use [`ModelTextCreator.createConstraintsText(Collection, ConstraintTextParams, String, Supplier)`](text/ModelTextCreator.html#createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier))
createConstraintsText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createConstraintsText([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)
Deprecated.
use [`ModelTextCreator.createConstraintText(Constraint, ConstraintTextParams, Supplier)`](text/ModelTextCreator.html#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier))
createConstraintsText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createConstraintsText([ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 boolean addBrackets)
Deprecated.
use [`CoreTextCreator.createValueSpecificationText(ValueSpecification, boolean, Supplier)`](text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier))
constructActivityEdgeText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructActivityEdgeText([ActivityEdge](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html) activityEdge,
 boolean showWeight)
Deprecated.
use [`ModelTextCreator.createActivityEdgeText(ActivityEdge, boolean, Supplier)`](text/ModelTextCreator.html#createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier))
createValueSpecificationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createValueSpecificationText(@CheckForNull
 [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) specification)
Deprecated.
use [`CoreTextCreator.createValueSpecificationText(ValueSpecification, Supplier)`](text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier))
createTypeName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTypeName([Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showFullType,
 boolean addColorInformation)
Deprecated.
use [`CoreTextCreator.createStyledTypeText(Type, boolean, Supplier)`](text/CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))
createMultiplicityText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lower,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) upper)
Deprecated.
use [`CoreTextCreator.createMultiplicityText(Integer, Integer)`](text/CoreTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer))
createMultiplicityRangeText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityRangeText(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) range)
Deprecated.
use [`CoreTextCreator.createMultiplicityRangeText(Integer)`](text/CoreTextCreator.html#createMultiplicityRangeText(java.lang.Integer))
createMultiplicityText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 boolean ordered,
 boolean unique,
 boolean addBrackets)
Deprecated.
use [`CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)`](text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams))
createMultiplicityText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText([MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) multiplicity,
 boolean showOrder,
 boolean showUnique,
 boolean addBrackets)
Deprecated.
use [`CoreTextCreator.createMultiplicityText(MultiplicityElement, MultiplicityTextParams, Supplier)`](text/CoreTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier))
createMultiplicityText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 @CheckForNull
 [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) lowerValue,
 boolean unique,
 boolean ordered,
 boolean addBrackets)
Deprecated.
use [`CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)`](text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams))
createPinText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPinText([Pin](../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html) pin,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor,
 boolean showSynchronizationInfo)
Deprecated.
use [`ModelTextCreator.createPinText(Pin, PinTextParams, Supplier)`](text/ModelTextCreator.html#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier))
createOperandGuardText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createOperandGuardText([InteractionOperand](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html) operand)
Deprecated.
use [`ModelTextCreator.createOperandGuardText(InteractionOperand, Supplier)`](text/ModelTextCreator.html#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier))
constructCombinedFragmentOperatorText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructCombinedFragmentOperatorText([CombinedFragment](../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html) combinedFragment)
Deprecated.
use [`ModelTextCreator.createCombinedFragmentOperatorText(CombinedFragment, Supplier)`](text/ModelTextCreator.html#createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier))
createClassifiersRepresentation
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createClassifiersRepresentation([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) classifiers,
 boolean showFullType,
 boolean addColorInformation)
Deprecated.
use [`CoreTextCreator.createTypeText(Collection, boolean, Supplier)`](text/CoreTextCreator.html#createTypeText(java.util.Collection,boolean,java.util.function.Supplier))
createClassifierName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createClassifierName([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 boolean showFullType,
 boolean addColorInformation)
Deprecated.
use [`CoreTextCreator.createTypeText(Type, boolean, Supplier)`](text/CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))
createInteractionUseText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createInteractionUseText([InteractionUse](../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html) interactionUse,
 boolean addReferTo,
 boolean addArguments)
Deprecated.
use [`ModelTextCreator.createInteractionUseText(InteractionUse, InteractionUseTextParams, Supplier)`](text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier))
createInteractionUseText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createInteractionUseText([CallBehaviorAction](../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) interactionUse)
Deprecated.
use [`ModelTextCreator.createInteractionUseText(CallBehaviorAction, Supplier)`](text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier))
createId
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createId([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e,
 boolean addColor)
Deprecated.
use [`CoreTextCreator.createElementNumberText(Element, Supplier)`](text/CoreTextCreator.html#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier))
Create the id (number) to be prepended to the text representation of the element
Parameters:
`e` - the element
`addColor` - if true wrap in grey color tags
Returns:
the auto id (with space at the end) or empty string if number is not available
createAssociationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAssociationText([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Deprecated.
use [`ModelTextCreator.createAssociationText(Association, Supplier)`](text/ModelTextCreator.html#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier))
Create Association text.
Parameters:
`association` - Text owner.
Returns:
The created string.
createBehaviorText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createBehaviorText([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior)
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
Creates behavior text.
Parameters:
`behavior` - behavior to represent.
Returns:
behavior text.
createBehaviorText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createBehaviorText([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind)
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
Creates behavior text.
Parameters:
`behavior` - behavior to represent.
`showStereotype` - indicates if stereotypes should be displayed.
`showProperties` - indicates if properties and tagged values should be displayed.
`showInheritedSign` - indicates if inherited sign should be displayed.
`showSignature` - indicates if behavior signature should be displayed.
`showFullType` - indicates if full qualified type name should be displayed.
`showConstraintName` - indicates if constraint name should be displayed.
`showConstraintExpression` - indicates if constraint expression should be displayed.
`addColorInformation` - indicates if color information should be added to the representation text.
`showParameterDirectionKind` - indicates if parameter direction kind should be displayed.
Returns:
behavior text.
createBehaviorText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createBehaviorText([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
Creates behavior text.
Parameters:
`behavior` - behavior to represent.
`showStereotype` - indicates if stereotypes should be displayed.
`showProperties` - indicates if properties and tagged values should be displayed.
`showInheritedSign` - indicates if inherited sign should be displayed.
`showSignature` - indicates if behavior signature should be displayed.
`showFullType` - indicates if full qualified type name should be displayed.
`showConstraintName` - indicates if constraint name should be displayed.
`showConstraintExpression` - indicates if constraint expression should be displayed.
`addColorInformation` - indicates if color information should be added to the representation text.
`showParameterDirectionKind` - indicates if parameter direction kind should be displayed.
`showOpaqueBehaviorBody` - indicates if opaque behavior body should be displayed
Returns:
behavior text.
createBehaviorText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createBehaviorText([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)
Deprecated.
use [`ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)`](text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier))
Creates behavior text.
Parameters:
`behavior` - behavior to represent.
`showStereotype` - indicates if stereotypes should be displayed.
`showProperties` - indicates if properties and tagged values should be displayed.
`showInheritedSign` - indicates if inherited sign should be displayed.
`showSignature` - indicates if behavior signature should be displayed.
`showFullType` - indicates if full qualified type name should be displayed.
`showConstraintName` - indicates if constraint name should be displayed.
`showConstraintExpression` - indicates if constraint expression should be displayed.
`addColorInformation` - indicates if color information should be added to the representation text.
`showParameterDirectionKind` - indicates if parameter direction kind should be displayed.
`showOpaqueBehaviorBody` - indicates if opaque behavior body should be displayed
Returns:
behavior text.
createStateText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStateText([State](../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) state)
Deprecated.
use [`ModelTextCreator.createStateText(State, Supplier)`](text/ModelTextCreator.html#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier))
Creates state name text. It appends SubMachine name if available.
Parameters:
`state` - the state to create text for.
Returns:
string containing state name ad SubMachine name
createStereotypeText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypeText([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Deprecated.
use [`CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
createStereotypesText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypesText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 char separator)
Deprecated.
use [`CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
Returns string representation of given.
Parameters:
`stereotypes` - the collection of stereotypes.
`separator` - the separator of stereotypes
Returns:
The created string.
createStereotypesText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypesText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 char separator,
 boolean skipDSL,
 boolean useAlias)
Deprecated.
use [`CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
Returns string representation of given.
Parameters:
`stereotypes` - the collection of stereotypes.
`separator` - the separator of stereotypes
`skipDSL` - skip DSL stereotypes or nor
`useAlias` - use DSL alias instead of name
Returns:
The created string.
createStereotypeText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypeText([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean useAlias)
Deprecated.
use [`CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
createStereotypeText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypeText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Deprecated.
use [`CoreTextCreator.createStereotypeText(String)`](text/CoreTextCreator.html#createStereotypeText(java.lang.String))
createStereotypesText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypesText([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 char separator)
Deprecated.
use [`CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
Create the representation text of element be assigned stereotype.
Parameters:
`element` - The given element.
`separator` - The separator string.
Returns:
The string representation.
createStereotypesText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypesText([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 char separator,
 boolean skipDSL,
 boolean useAlias)
Deprecated.
use [`CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)`](text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))
Create the representation text of element be assigned stereotype.
Parameters:
`element` - The given element.
`separator` - The separator string.
`skipDSL` - skip DSL stereotypes or nor
`useAlias` - use DSL alias instead of name
Returns:
The string representation.
createPropertyPropertyStringText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void createPropertyPropertyStringText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text)
Deprecated.
use `ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder)`
createPropertyPropertyStringText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void createPropertyPropertyStringText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Deprecated.
use `ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder, String)`
createOperationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createOperationText([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters)
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
Constructs operation representation text.
Parameters:
`operation` - operation which text will be created.
`showParameters` - flag indicates if operation parameters should be shown.
`showVisibility` - flag indicates if operation visibility should be shown.
`showFullType` - true for show full type
`showStereotype` - show stereotype
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction
`addColorInformation` - add color
`showTemplateParameters` -
Returns:
method text string.
createOperationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createOperationText([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue)
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
Constructs representation operation text.
Parameters:
`operation` - operation which text will be created.
`showSignature` - flag indicates if method parameters should be shown.
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showStereotype` - show stereotype
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction kind
`addColorInformation` - add color
`showTemplateParameters` - indicates if template parameters should be shown.
`showParameterDefaultValue` - indicates if parameter default values should be shown.
Returns:
method text string.
createOperationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createOperationText([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
Constructs representation operation text.
Parameters:
`operation` - operation which text will be created.
`showSignature` - flag indicates if method parameters should be shown.
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showStereotype` - show stereotype
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction kind
`addColorInformation` - add color
`showTemplateParameters` - indicates if template parameters should be shown.
`showParameterDefaultValue` - indicates if parameter default values should be shown.
`showInheritedSign` - show inherited sign
Returns:
method text string.
createOperationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createOperationText([Operation](../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)
Deprecated.
use [`ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)`](text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier))
Constructs operation representation text.
Parameters:
`operation` - operation which text will be created.
`showParameters` - flag indicates if operation parameters should be shown.
`showVisibility` - flag indicates if operation visibility should be shown.
`showFullType` - True for show full type.
`showStereotype` - show stereotype
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction kind
`addColorInformation` - add color
`showTemplateParameters` - indicates if template parameters should be shown.
`showParameterDefaultValue` - indicates if parameter default values should be shown.
`showInheritedSign` - show inherited sign
Returns:
method text string.
createParameterDirectionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createParameterDirectionText([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameterMetaType,
 @CheckForNull
 [ParameterDirectionKind](../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html) parameterDirection,
 boolean skipDefaultValue,
 boolean showReturnDirection,
 boolean addColorInformation)
Deprecated.
use `ModelTextCreator#createParameterDirectionText(ParameterDirectionKind, Project, ParameterDirectionTextParams, Supplier)`
createParameterText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createParameterText([Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createParameterText(Parameter, ParameterTextParams, Supplier)`](text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
Creates text which represents parameter. for example "param : java::lang::String"
Parameters:
`parameter` - parameter which text will be created.
`showFullType` - True for show full type.
`showParameterDirection` - show parameter direction
`addColorInformation` - add color
Returns:
Created text
createParameterText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createParameterText([Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue,
 boolean skipDefaultDirection,
 boolean showReturnDirection)
Deprecated.
use [`ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
createParameterText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createParameterText([Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue)
Deprecated.
use [`ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
createParametersText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createParametersText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showParameterDefaultValue)
Deprecated.
use [`ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
createParametersText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createParametersText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Parameter](../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)> parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier))
createActivityParameterNodeText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createActivityParameterNodeText([ActivityParameterNode](../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html) parameter,
 boolean showFullType,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createActivityParameterNodeText(ActivityParameterNode, boolean, Supplier)`](text/ModelTextCreator.html#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier))
Creates text which represents activity parameter node. for example "param : java::lang::String"
Parameters:
`parameter` - parameter which text will be created.
`showFullType` - True for show full type.
`addColorInformation` - indicates if color information should be added to the parameter text.
Returns:
Created text
createReceptionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createReceptionText([Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)`](text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))
Constructs reception representation text.
Parameters:
`reception` - reception which text will be created.
`showSignature` - flag indicates if method parameters should be shown.
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction
`addColorInformation` - add color
Returns:
reception representation text
createReceptionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createReceptionText([Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)`](text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))
Constructs reception representation text.
Parameters:
`reception` - reception which text will be created.
`showSignature` - flag indicates if method parameters should be shown.
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction
`showInheritedSign` - show inherited sign
`addColorInformation` - add color
Returns:
reception representation text
createReceptionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createReceptionText([Reception](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html) reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)`](text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier))
Constructs reception representation text.
Parameters:
`reception` - reception which text will be created.
`showSignature` - flag indicates if method parameters should be shown.
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showParameterDirection` - show parameter direction
`showInheritedSign` - show inherited sign
`addColorInformation` - add color
Returns:
reception representation text
createGuardText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createGuardText([Message](../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) msg)
Deprecated.
use [`ModelTextCreator.createGuardText(Message, Supplier)`](text/ModelTextCreator.html#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier))
Creates Message guard text.
Parameters:
`msg` - message
Returns:
text
createEnumerationLiteralText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createEnumerationLiteralText([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression)
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
Constructs enumeration literal text.
Parameters:
`enumLiteral` - EnumerationLiteral
`showStereotype` - True, for show stereotype
`showProperties` - True, for show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
Returns:
text
createEnumerationLiteralText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createEnumerationLiteralText([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
Constructs enumeration literal text.
Parameters:
`enumLiteral` - EnumerationLiteral
`showStereotype` - True, for show stereotype
`showProperties` - True, for show properties
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showInheritedSign` - show inherited sign
Returns:
text
createEnumerationLiteralText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createEnumerationLiteralText([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
Constructs enumeration literal text.
Parameters:
`enumLiteral` - EnumerationLiteral
`showStereotype` - True, for show stereotype
`showProperties` - True, for show properties
`showTaggedValues` - True, for show tagged values
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showInheritedSign` - show inherited sign
Returns:
text
createEnumerationLiteralText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createEnumerationLiteralText([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)`](text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier))
Constructs enumeration literal text.
Parameters:
`enumLiteral` - EnumerationLiteral
`showStereotype` - True, for show stereotype
`showProperties` - True, for show properties
`showTaggedValues` - True, for show tagged values
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showInheritedSign` - show inherited sign
Returns:
text
createTemplateParametersText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTemplateParametersText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) templateParameters,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Deprecated.
use [`ModelTextCreator.createTemplateParametersText(Collection, String, Supplier)`](text/ModelTextCreator.html#createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier))
Create the Template Parameters Text.
Parameters:
`templateParameters` - The given TemplateParameters.
`separator` - The text separator
createTemplateParameterText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTemplateParameterText([TemplateParameter](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html) tParameter)
Deprecated.
use [`ModelTextCreator.createTemplateParameterText(TemplateParameter, Supplier)`](text/ModelTextCreator.html#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier))
Creates TemplateParameter text.
Parameters:
`tParameter` - The given TemplateParameter
Returns:
The create string.
createTemplateBindingText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTemplateBindingText([TemplateBinding](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) binding)
Constructs given binding element text.
Parameters:
`binding` - The given binding.
Returns:
The created string.
createTemplateBindingText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTemplateBindingText([TemplateBinding](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html) binding,
 boolean attachTemplateParameterInfo)
Constructs given binding element text.
Parameters:
`binding` - The given binding.
`attachTemplateParameterInfo` - indicates if full template parameter notation should be used.
Returns:
The created string.
createTemplateParameterSubstitutionText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTemplateParameterSubstitutionText([TemplateParameterSubstitution](../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html) parameterSubstitution,
 boolean attachTemplateParameterInfo)
Deprecated.
use [`ModelTextCreator.createTemplateParameterSubstitutionText(TemplateParameterSubstitution, boolean, Supplier)`](text/ModelTextCreator.html#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier))
Create TemplateParameterSubstitution Text.
Parameters:
`parameterSubstitution` - The given ParameterSubstitution.
`attachTemplateParameterInfo` - indicates if full template parameter notation should be used.
Returns:
The created text.
createPropertyText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPropertyText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraints,
 boolean showMultiplicity,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
Constructs attribute view text.
Parameters:
`property` - attribute which text will be created.
`showName` - show name
`showType` - show type
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showInitValue` - indicates if initial value of attribute will be shown. @return attribute view text string.
`showStereotype` - show stereotype
`showProperties` - show properties
`showConstraints` - show constraints
`showMultiplicity` - show multiplicity
`addColorInformation` - add color
Returns:
property text
createPropertyText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPropertyText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
Constructs attribute view text.
Parameters:
`property` - attribute which text will be created.
`showName` - show name
`showType` - show type
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showInitValue` - indicates if initial value of attribute will be shown. @return attribute view text string.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showTypeTaggedValues` - show tagged values
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showMultiplicity` - show multiplicity
`addColorInformation` - add color
Returns:
text
createPropertyText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPropertyText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
Constructs attribute view text.
Parameters:
`property` - attribute which text will be created.
`showName` - show name
`showType` - show type
`showDerived` - show derived sign
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showInitValue` - indicates if initial value of attribute will be shown. @return attribute view text string.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showTypeTaggedValues` - show tagged values
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showMultiplicity` - show multiplicity
`addColorInformation` - add color
Returns:
text
createPropertyText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPropertyText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
Constructs attribute view text.
Parameters:
`property` - attribute which text will be created.
`showName` - show name
`showType` - show type
`showDerived` - show derived sign
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showInitValue` - indicates if initial value of attribute will be shown. @return attribute view text string.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showTypeTaggedValues` - show tagged values
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showMultiplicity` - show multiplicity
`showInheritedSign` - show inherited sign
`addColorInformation` - add color
Returns:
text
createPropertyText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPropertyText([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
Constructs attribute view text.
Parameters:
`property` - attribute which text will be created.
`showName` - show name
`showType` - show type
`showDerived` - show derived sign
`showVisibility` - flag indicates if method visibility should be shown.
`showFullType` - True for show full type.
`showInitValue` - indicates if initial value of attribute will be shown. @return attribute view text string.
`showStereotype` - show stereotypes
`showProperties` - show properties
`showTypeTaggedValues` - show tagged values
`showConstraintName` - show constraint name
`showConstraintExpression` - show constraint expression
`showMultiplicity` - show multiplicity
`showInheritedSign` - show inherited sign
`addColorInformation` - add color
Returns:
text
createPortText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPortText([Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
createPortText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPortText([Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean addColor)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
createPortText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createPortText([Port](../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showInheritedSign,
 boolean addColor)
Deprecated.
use [`ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)`](text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier))
createInstanceSpecificationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createInstanceSpecificationText([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor)
Deprecated.
use [`ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)`](text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier))
createInstanceSpecificationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createInstanceSpecificationText([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor,
 boolean showAutoID)
Deprecated.
use [`ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)`](text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier))
appendGrayColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) appendGrayColor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
appendGrayColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void appendGrayColor([StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text)
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
resetColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resetColor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`RichTextStringUtils.closeColor(String)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String))
resetColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void resetColor([StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text)
Deprecated.
use [`RichTextStringUtils.closeColor(StringBuffer)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuffer))
appendColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void appendColor([StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
Deprecated.
use [`RichTextStringUtils.startColor(StringBuffer, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuffer,java.awt.Color))
appendColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) appendColor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
getPureTextFromColoredText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPureTextFromColoredText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) coloredText)
Deprecated.
use [`TextUtils.toPlainText(String)`](../../text/TextUtils.html#toPlainText(java.lang.String))
startColorHtmlTag
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void startColorHtmlTag([StringBuilder](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
Deprecated.
use [`RichTextStringUtils.startColor(StringBuilder, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuilder,java.awt.Color))
startColorHtmlTag
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) startColorHtmlTag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
Deprecated.
use [`RichTextStringUtils.startColor(String, Color)`](../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color))
endColorHtmlTag
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void endColorHtmlTag([StringBuilder](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html) text)
Deprecated.
use [`RichTextStringUtils.closeColor(StringBuilder)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuilder))
createRepresentationTextComparator
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[BaseElement](BaseElement.html)> createRepresentationTextComparator(boolean addColor,
 boolean showAutoId)
Deprecated.
use [`RepresentationTextCreator.createRepresentationTextComparator(RepresentationTextParams)`](RepresentationTextCreator.html#createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams))
endColorHtmlTag
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) endColorHtmlTag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`RichTextStringUtils.closeColor(String)`](../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String))
getRepresentedText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) el,
 boolean addColor)
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
getRepresentedText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber)
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
getRepresentedText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature)
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
getRepresentedText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 boolean noCache)
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean))
getRepresentedText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 [LocationInTool](../ui/LocationInTool.html) locationInTool,
 boolean noCache)
Deprecated.
use [`RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)`](RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean))
createDefaultRepresentationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createDefaultRepresentationText([BaseElement](BaseElement.html) element,
 boolean addColor,
 boolean fullSignature)
Deprecated.
use [`RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
createDefaultRepresentationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createDefaultRepresentationText([BaseElement](BaseElement.html) element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId)
Deprecated.
use [`RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
createDefaultRepresentationText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createDefaultRepresentationText([BaseElement](BaseElement.html) element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId,
 [LocationInTool](../ui/LocationInTool.html) locationInTool)
Deprecated.
use [`RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)`](RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))
isAddColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean isAddColor()
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
Returns:
always returns false
setAddColor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setAddColor(boolean addColor)
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
Method has no impact, does not set the value
getLocationInTool
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [LocationInTool](../ui/LocationInTool.html) getLocationInTool()
Deprecated.
text creation parameters are now retrieved from [`RepresentationTextParams`](RepresentationTextParams.html) which is passed as argument for various methods
Returns:
always returns [`LocationInTool.unknown`](../ui/LocationInTool.html#unknown)
setLocationInTool
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setLocationInTool([LocationInTool](../ui/LocationInTool.html) locationInTool)
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
Method has no impact, does not set the value
isShowFullType
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean isShowFullType()
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
Returns:
always returns false
setShowFullType
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setShowFullType(boolean value)
Deprecated.
text creation parameters should now be set in [`RepresentationTextParams`](RepresentationTextParams.html) and passed as argument for methods when retrieving text
Method has no impact, does not set the value
getRelationshipFromToRepresentation
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRelationshipFromToRepresentation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) clientModelElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clientName,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplierModelElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) supplierName,
 boolean showFullType,
 boolean addColor)
Deprecated.
use [`ModelTextCreator.createRelationshipFromToText(Element, Element, String, Element, String, boolean, Supplier)`](text/ModelTextCreator.html#createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier))
createTypedElementText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createTypedElementText([TypedElement](../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) typedElement,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)
Deprecated.
use [`ModelTextCreator.createTypedElementText(TypedElement, TypedElementTextParams, Supplier)`](text/ModelTextCreator.html#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier))
createNamedElementListText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createNamedElementListText([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> elements)
Deprecated.
use [`CoreTextCreator.createNamedElementListText(java.util.List, Supplier)`](text/CoreTextCreator.html#createNamedElementListText(java.util.List,java.util.function.Supplier))
createVisibilityText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static char createVisibilityText(@CheckForNull
 [VisibilityKind](../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html) visibility)
Deprecated.
use [`CoreTextCreator.createVisibilityText(VisibilityKind)`](text/CoreTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))
createElementNameText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createElementNameText(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) o)
Deprecated.
use [`NamedElement.getName()`](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html#getName())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class DeprecatedRepresentationTextCreator">Class DeprecatedRepresentationTextCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="RepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextCreator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DeprecatedRepresentationTextCreator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Deprecated OpenApi methods of RepresentationTextCreator that should not be used any more</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLOR_POSTFIX">COLOR_POSTFIX</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#COLOR_POSTFIX"><code>RichTextStringUtils.COLOR_POSTFIX</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLOR_PREFIX">COLOR_PREFIX</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#COLOR_PREFIX"><code>RichTextStringUtils.COLOR_PREFIX</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY_NAME_NOTATION">EMPTY_NAME_NOTATION</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GRAY_COLOR_STRING">GRAY_COLOR_STRING</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#GRAY_COLOR"><code>RichTextStringUtils.GRAY_COLOR</code></a></div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DeprecatedRepresentationTextCreator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#appendColor(java.lang.StringBuffer,java.awt.Color)">appendColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuffer,java.awt.Color)"><code>RichTextStringUtils.startColor(StringBuffer, Color)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#appendColor(java.lang.String,java.awt.Color)">appendColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#appendGrayColor(java.lang.String)">appendGrayColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#appendGrayColor(java.lang.StringBuffer)">appendGrayColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#constructActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean)">constructActivityEdgeText</a><wbr/>(<a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> activityEdge,
 boolean showWeight)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createActivityEdgeText(ActivityEdge, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#constructCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">constructCombinedFragmentOperatorText</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> combinedFragment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier)"><code>ModelTextCreator.createCombinedFragmentOperatorText(CombinedFragment, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean)">createActivityParameterNodeText</a><wbr/>(<a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> parameter,
 boolean showFullType,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createActivityParameterNodeText(ActivityParameterNode, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">createAssociationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier)"><code>ModelTextCreator.createAssociationText(Association, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">createBehaviorText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createBehaviorText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createBehaviorText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createBehaviorText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createClassifierName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean,boolean)">createClassifierName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 boolean showFullType,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createTypeText(Type, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createClassifiersRepresentation(java.util.Collection,boolean,boolean)">createClassifiersRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> classifiers,
 boolean showFullType,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createTypeText(java.util.Collection,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createTypeText(Collection, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean,boolean,boolean)">createConstraintsText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createConstraintText(Constraint, ConstraintTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean)">createConstraintsText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 boolean addBrackets)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createValueSpecificationText(ValueSpecification, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createConstraintsText(java.util.Collection,java.lang.String,boolean,boolean,boolean)">createConstraintsText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createConstraintsText(Collection, ConstraintTextParams, String, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">createDefaultRepresentationText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean addColor,
 boolean fullSignature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">createDefaultRepresentationText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool)">createDefaultRepresentationText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId,
 <a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createElementNameText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createElementNameText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html#getName()"><code>NamedElement.getName()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">createEventText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEventText(Event, EventTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,boolean,boolean)">createEventText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEventText(Event, EventTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">createGuardText</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier)"><code>ModelTextCreator.createGuardText(Message, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createId(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">createId</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e,
 boolean addColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier)"><code>CoreTextCreator.createElementNumberText(Element, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean)">createInstanceSpecificationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean,boolean)">createInstanceSpecificationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor,
 boolean showAutoID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction)">createInteractionUseText</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> interactionUse)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier)"><code>ModelTextCreator.createInteractionUseText(CallBehaviorAction, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean,boolean)">createInteractionUseText</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> interactionUse,
 boolean addReferTo,
 boolean addArguments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createInteractionUseText(InteractionUse, InteractionUseTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createMultiplicityRangeText(java.lang.Integer)">createMultiplicityRangeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> range)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityRangeText(java.lang.Integer)"><code>CoreTextCreator.createMultiplicityRangeText(Integer)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,boolean,boolean,boolean)">createMultiplicityText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> multiplicity,
 boolean showOrder,
 boolean showUnique,
 boolean addBrackets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createMultiplicityText(MultiplicityElement, MultiplicityTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createMultiplicityText(java.lang.Integer,java.lang.Integer)">createMultiplicityText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> upper)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer)"><code>CoreTextCreator.createMultiplicityText(Integer, Integer)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,boolean)">createMultiplicityText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 boolean ordered,
 boolean unique,
 boolean addBrackets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)"><code>CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,boolean)">createMultiplicityText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> lowerValue,
 boolean unique,
 boolean ordered,
 boolean addBrackets)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)"><code>CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createNamedElementListText(java.util.List)">createNamedElementListText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createNamedElementListText(java.util.List,java.util.function.Supplier)"><code>CoreTextCreator.createNamedElementListText(java.util.List, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)">createOperandGuardText</a><wbr/>(<a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> operand)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier)"><code>ModelTextCreator.createOperandGuardText(InteractionOperand, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createParameterDirectionText(com.nomagic.magicdraw.core.Project,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,boolean,boolean,boolean)">createParameterDirectionText</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameterMetaType,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> parameterDirection,
 boolean skipDefaultValue,
 boolean showReturnDirection,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>ModelTextCreator#createParameterDirectionText(ParameterDirectionKind, Project, ParameterDirectionTextParams, Supplier)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean)">createParametersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean,boolean)">createParametersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showParameterDefaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean)">createParameterText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParameterText(Parameter, ParameterTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean)">createParameterText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean,boolean,boolean)">createParameterText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue,
 boolean skipDefaultDirection,
 boolean showReturnDirection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,boolean,boolean,boolean,boolean,boolean,boolean)">createPinText</a><wbr/>(<a href="../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> pin,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor,
 boolean showSynchronizationInfo)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPinText(Pin, PinTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean)">createPortText</a><wbr/>(<a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean)">createPortText</a><wbr/>(<a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showInheritedSign,
 boolean addColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPortText</a><wbr/>(<a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean addColor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer)">createPropertyPropertyStringText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer,java.lang.String)">createPropertyPropertyStringText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder, String)</code></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraints,
 boolean showMultiplicity,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">createProtocolTransitionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean)">createProtocolTransitionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition,
 boolean showPort)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean,boolean,boolean)">createProtocolTransitionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPureSlotsString(java.util.Collection,java.lang.String,boolean,boolean)">createPureSlotsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean showHTML,
 boolean showEmptyValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createSlotsText(Collection, SlotTextParams, String, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createReceptionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createReceptionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createReceptionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createRepresentationTextComparator(boolean,boolean)">createRepresentationTextComparator</a><wbr/>(boolean addColor,
 boolean showAutoId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createRepresentationTextComparator(RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createSlotsText(java.util.Collection,java.lang.String,boolean,boolean)">createSlotsText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean showHTML,
 boolean showEmptyValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createSlotsTextWithBraces(Collection, SlotTextParams, String, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived,
 boolean forEditing,
 boolean colorUnitSymbols,
 boolean colorTag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">createStateText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> state)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier)"><code>ModelTextCreator.createStateText(State, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char)">createStereotypesText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 char separator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char,boolean,boolean)">createStereotypesText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 char separator,
 boolean skipDSL,
 boolean useAlias)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypesText(java.util.Collection,char)">createStereotypesText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 char separator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypesText(java.util.Collection,char,boolean,boolean)">createStereotypesText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 char separator,
 boolean skipDSL,
 boolean useAlias)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">createStereotypeText</a><wbr/>(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">createStereotypeText</a><wbr/>(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean useAlias)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createStereotypeText(java.lang.String)">createStereotypeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypeText(java.lang.String)"><code>CoreTextCreator.createStereotypeText(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">createTemplateBindingText</a><wbr/>(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> binding)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs given binding element text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean)">createTemplateBindingText</a><wbr/>(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> binding,
 boolean attachTemplateParameterInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs given binding element text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTemplateParametersText(java.util.Collection,java.lang.String)">createTemplateParametersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> templateParameters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createTemplateParametersText(Collection, String, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean)">createTemplateParameterSubstitutionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> parameterSubstitution,
 boolean attachTemplateParameterInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createTemplateParameterSubstitutionText(TemplateParameterSubstitution, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">createTemplateParameterText</a><wbr/>(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> tParameter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier)"><code>ModelTextCreator.createTemplateParameterText(TemplateParameter, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean)">createTransitionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 boolean showEffect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean)">createTransitionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean,boolean,boolean)">createTransitionText</a><wbr/>(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTriggersText(java.util.Collection)">createTriggersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> triggers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTriggersText(java.util.Collection,boolean)">createTriggersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> triggers,
 boolean showPort)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTriggersText(java.util.Collection,boolean,boolean,boolean)">createTriggersText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> triggers,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger)">createTriggerText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean)">createTriggerText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger,
 boolean showPort)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean,boolean,boolean)">createTriggerText</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,boolean,boolean,boolean,boolean,boolean)">createTypedElementText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> typedElement,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTypedElementText(TypedElement, TypedElementTextParams, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean)">createTypeName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showFullType,
 boolean addColorInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createStyledTypeText(Type, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">createValueSpecificationText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> specification)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier)"><code>CoreTextCreator.createValueSpecificationText(ValueSpecification, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static char</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">createVisibilityText</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)"><code>CoreTextCreator.createVisibilityText(VisibilityKind)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#endColorHtmlTag(java.lang.String)">endColorHtmlTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String)"><code>RichTextStringUtils.closeColor(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#endColorHtmlTag(java.lang.StringBuilder)">endColorHtmlTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuilder)"><code>RichTextStringUtils.closeColor(StringBuilder)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLocationInTool()">getLocationInTool</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters are now retrieved from <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> which is passed as argument for various methods</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPureTextFromColoredText(java.lang.String)">getPureTextFromColoredText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> coloredText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/TextUtils.html#toPlainText(java.lang.String)"><code>TextUtils.toPlainText(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRelationshipFromToRepresentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,boolean)">getRelationshipFromToRepresentation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> clientName,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> supplierName,
 boolean showFullType,
 boolean addColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createRelationshipFromToText(Element, Element, String, Element, String, boolean, Supplier)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 boolean noCache)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool,boolean)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 <a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool,
 boolean noCache)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isAddColor()">isAddColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isShowFullType()">isShowFullType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resetColor(java.lang.String)">resetColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String)"><code>RichTextStringUtils.closeColor(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resetColor(java.lang.StringBuffer)">resetColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuffer)"><code>RichTextStringUtils.closeColor(StringBuffer)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setAddColor(boolean)">setAddColor</a><wbr/>(boolean addColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool)">setLocationInTool</a><wbr/>(<a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setShowFullType(boolean)">setShowFullType</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#startColorHtmlTag(java.lang.StringBuilder,java.awt.Color)">startColorHtmlTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuilder,java.awt.Color)"><code>RichTextStringUtils.startColor(StringBuilder, Color)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#startColorHtmlTag(java.lang.String,java.awt.Color)">startColorHtmlTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
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
<section class="detail" id="EMPTY_NAME_NOTATION">
<h3>EMPTY_NAME_NOTATION</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EMPTY_NAME_NOTATION</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator.EMPTY_NAME_NOTATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLOR_PREFIX">
<h3>COLOR_PREFIX</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLOR_PREFIX</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#COLOR_PREFIX"><code>RichTextStringUtils.COLOR_PREFIX</code></a></div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator.COLOR_PREFIX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLOR_POSTFIX">
<h3>COLOR_POSTFIX</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLOR_POSTFIX</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#COLOR_POSTFIX"><code>RichTextStringUtils.COLOR_POSTFIX</code></a></div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator.COLOR_POSTFIX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GRAY_COLOR_STRING">
<h3>GRAY_COLOR_STRING</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GRAY_COLOR_STRING</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#GRAY_COLOR"><code>RichTextStringUtils.GRAY_COLOR</code></a></div>
</div>
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
<h3>DeprecatedRepresentationTextCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DeprecatedRepresentationTextCreator</span>()</div>
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
<section class="detail" id="createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean)">
<h3>createTransitionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTransitionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 boolean showEffect)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean)">
<h3>createTransitionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTransitionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean,boolean,boolean)">
<h3>createTransitionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTransitionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 boolean showEffect,
 boolean showPort,
 boolean showOpaqueBehaviorBody,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTransitionText(Transition, TransitionTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">
<h3>createProtocolTransitionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createProtocolTransitionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean)">
<h3>createProtocolTransitionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createProtocolTransitionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition,
 boolean showPort)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean,boolean,boolean)">
<h3>createProtocolTransitionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createProtocolTransitionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> transition,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,com.nomagic.magicdraw.uml.text.TransitionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createProtocolTransitionText(ProtocolTransition, TransitionTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTriggersText(java.util.Collection)">
<h3>createTriggersText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTriggersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> triggers)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTriggersText(java.util.Collection,boolean)">
<h3>createTriggersText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTriggersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> triggers,
 boolean showPort)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTriggersText(java.util.Collection,boolean,boolean,boolean)">
<h3>createTriggersText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTriggersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> triggers,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggersText(java.util.Collection,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggersText(Collection, TriggerTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger)">
<h3>createTriggerText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTriggerText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean)">
<h3>createTriggerText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTriggerText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger,
 boolean showPort)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean,boolean,boolean)">
<h3>createTriggerText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTriggerText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a> trigger,
 boolean showPort,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,com.nomagic.magicdraw.uml.text.TriggerTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTriggerText(Trigger, TriggerTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">
<h3>createEventText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createEventText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEventText(Event, EventTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,boolean,boolean)">
<h3>createEventText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createEventText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event,
 boolean showOperationsSignature,
 boolean useAdvancedColoring)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,com.nomagic.magicdraw.uml.text.EventTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEventText(Event, EventTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createSlotText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createSlotText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
<div class="block">Returns string representation of given tag definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - The given slot.</dd>
<dd><code>showName</code> - Is show name?</dd>
<dd><code>ignoreTrueValues</code> - Is ignore true values?</dd>
<dd><code>showHTML</code> - True for show htm</dd>
<dd><code>showFeatureType</code> - Is show feature type?</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>addColorInformation</code> - True for set color.</dd>
<dd><code>showEmptyValue</code> - show empty value</dd>
<dd><code>showQualifiedName</code> - show qualified name</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createSlotText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createSlotText</span><wbr/><span class="parameters">(@Nonnull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
<div class="block">Returns string representation of given tag definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - The given slot.</dd>
<dd><code>showName</code> - Is show name?</dd>
<dd><code>ignoreTrueValues</code> - Is ignore true values?</dd>
<dd><code>showHTML</code> - True for show htm</dd>
<dd><code>showFeatureType</code> - Is show feature type?</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showFeatureTypeTaggedValues</code> - show feature type tagged values</dd>
<dd><code>addColorInformation</code> - True for set color.</dd>
<dd><code>showEmptyValue</code> - show empty value</dd>
<dd><code>showQualifiedName</code> - show qualified name</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createSlotText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createSlotText</span><wbr/><span class="parameters">(@Nonnull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
<div class="block">Returns string representation of given tag definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - The given slot.</dd>
<dd><code>showName</code> - Is show name?</dd>
<dd><code>ignoreTrueValues</code> - Is ignore true values?</dd>
<dd><code>showHTML</code> - True for show htm</dd>
<dd><code>showFeatureType</code> - Is show feature type?</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showFeatureTypeTaggedValues</code> - show feature type tagged values</dd>
<dd><code>addColorInformation</code> - True for set color.</dd>
<dd><code>showEmptyValue</code> - show empty value</dd>
<dd><code>showQualifiedName</code> - show qualified name</dd>
<dd><code>showDerived</code> - if true returned string will be calculated as derived if possible</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createSlotText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createSlotText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 boolean showName,
 boolean ignoreTrueValues,
 boolean showHTML,
 boolean showFeatureType,
 boolean showFullType,
 boolean showFeatureTypeTaggedValues,
 boolean addColorInformation,
 boolean showEmptyValue,
 boolean showQualifiedName,
 boolean showDerived,
 boolean forEditing,
 boolean colorUnitSymbols,
 boolean colorTag)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,com.nomagic.magicdraw.uml.text.SlotTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createSlotText(Slot, SlotTextParams, Supplier)</code></a></div>
</div>
<div class="block">Returns string representation of given tag definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - The given slot.</dd>
<dd><code>showName</code> - Is show name?</dd>
<dd><code>ignoreTrueValues</code> - Is ignore true values?</dd>
<dd><code>showHTML</code> - True for show htm</dd>
<dd><code>showFeatureType</code> - Is show feature type?</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showFeatureTypeTaggedValues</code> - show feature type tagged values</dd>
<dd><code>addColorInformation</code> - True for set color.</dd>
<dd><code>showEmptyValue</code> - show empty value</dd>
<dd><code>showQualifiedName</code> - show qualified name</dd>
<dd><code>showDerived</code> - if true returned string will be calculated as derived if possible</dd>
<dd><code>forEditing</code> - flag to indicate that we need text for editing, so no additional text providers will be used</dd>
<dd><code>colorUnitSymbols</code> - flag to indicate if we need to use color for additional text providers, we can't use addColorInformation, as we use same
                                    provider for instances that don't have color information property</dd>
<dd><code>colorTag</code> - indicates if we need color tag or font color tag if we use in additional text providers</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPureSlotsString(java.util.Collection,java.lang.String,boolean,boolean)">
<h3>createPureSlotsString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPureSlotsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean showHTML,
 boolean showEmptyValue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotsText(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createSlotsText(Collection, SlotTextParams, String, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createSlotsText(java.util.Collection,java.lang.String,boolean,boolean)">
<h3>createSlotsText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createSlotsText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a>&gt; slots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean showHTML,
 boolean showEmptyValue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createSlotsTextWithBraces(java.util.Collection,com.nomagic.magicdraw.uml.text.SlotTextParams,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createSlotsTextWithBraces(Collection, SlotTextParams, String, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createConstraintsText(java.util.Collection,java.lang.String,boolean,boolean,boolean)">
<h3>createConstraintsText</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createConstraintsText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createConstraintsText(java.util.Collection,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createConstraintsText(Collection, ConstraintTextParams, String, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean,boolean,boolean)">
<h3>createConstraintsText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createConstraintsText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 boolean useName,
 boolean useExpression,
 boolean addBrackets)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,com.nomagic.magicdraw.uml.text.ConstraintTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createConstraintText(Constraint, ConstraintTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean)">
<h3>createConstraintsText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createConstraintsText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 boolean addBrackets)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createValueSpecificationText(ValueSpecification, boolean, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="constructActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean)">
<h3>constructActivityEdgeText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructActivityEdgeText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> activityEdge,
 boolean showWeight)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createActivityEdgeText(ActivityEdge, boolean, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>createValueSpecificationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createValueSpecificationText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> specification)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier)"><code>CoreTextCreator.createValueSpecificationText(ValueSpecification, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean)">
<h3>createTypeName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTypeName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showFullType,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createStyledTypeText(Type, boolean, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(java.lang.Integer,java.lang.Integer)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> upper)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer)"><code>CoreTextCreator.createMultiplicityText(Integer, Integer)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityRangeText(java.lang.Integer)">
<h3>createMultiplicityRangeText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityRangeText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> range)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityRangeText(java.lang.Integer)"><code>CoreTextCreator.createMultiplicityRangeText(Integer)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,boolean)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 boolean ordered,
 boolean unique,
 boolean addBrackets)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)"><code>CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,boolean,boolean,boolean)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> multiplicity,
 boolean showOrder,
 boolean showUnique,
 boolean addBrackets)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createMultiplicityText(MultiplicityElement, MultiplicityTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,boolean)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> lowerValue,
 boolean unique,
 boolean ordered,
 boolean addBrackets)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)"><code>CoreTextCreator.createMultiplicityText(String, String, boolean, boolean, MultiplicityTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPinText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPinText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a> pin,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor,
 boolean showSynchronizationInfo)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,com.nomagic.magicdraw.uml.text.PinTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPinText(Pin, PinTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)">
<h3>createOperandGuardText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createOperandGuardText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a> operand)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand,java.util.function.Supplier)"><code>ModelTextCreator.createOperandGuardText(InteractionOperand, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="constructCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">
<h3>constructCombinedFragmentOperatorText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructCombinedFragmentOperatorText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdfragments/CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> combinedFragment)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment,java.util.function.Supplier)"><code>ModelTextCreator.createCombinedFragmentOperatorText(CombinedFragment, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createClassifiersRepresentation(java.util.Collection,boolean,boolean)">
<h3>createClassifiersRepresentation</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createClassifiersRepresentation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> classifiers,
 boolean showFullType,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createTypeText(java.util.Collection,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createTypeText(Collection, boolean, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createClassifierName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean,boolean)">
<h3>createClassifierName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createClassifierName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 boolean showFullType,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)"><code>CoreTextCreator.createTypeText(Type, boolean, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean,boolean)">
<h3>createInteractionUseText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createInteractionUseText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> interactionUse,
 boolean addReferTo,
 boolean addArguments)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,com.nomagic.magicdraw.uml.text.InteractionUseTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createInteractionUseText(InteractionUse, InteractionUseTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction)">
<h3>createInteractionUseText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createInteractionUseText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a> interactionUse)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction,java.util.function.Supplier)"><code>ModelTextCreator.createInteractionUseText(CallBehaviorAction, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createId(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>createId</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createId</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier)"><code>CoreTextCreator.createElementNumberText(Element, Supplier)</code></a></div>
</div>
<div class="block">Create the id (number) to be prepended to the text representation of the element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - the element</dd>
<dd><code>addColor</code> - if true wrap in grey color tags</dd>
<dt>Returns:</dt>
<dd>the auto id (with space at the end) or empty string if number is not available</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>createAssociationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAssociationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,java.util.function.Supplier)"><code>ModelTextCreator.createAssociationText(Association, Supplier)</code></a></div>
</div>
<div class="block">Create Association text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - Text owner.</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>createBehaviorText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createBehaviorText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
<div class="block">Creates behavior text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - behavior to represent.</dd>
<dt>Returns:</dt>
<dd>behavior text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createBehaviorText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createBehaviorText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
<div class="block">Creates behavior text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - behavior to represent.</dd>
<dd><code>showStereotype</code> - indicates if stereotypes should be displayed.</dd>
<dd><code>showProperties</code> - indicates if properties and tagged values should be displayed.</dd>
<dd><code>showInheritedSign</code> - indicates if inherited sign should be displayed.</dd>
<dd><code>showSignature</code> - indicates if behavior signature should be displayed.</dd>
<dd><code>showFullType</code> - indicates if full qualified type name should be displayed.</dd>
<dd><code>showConstraintName</code> - indicates if constraint name should be displayed.</dd>
<dd><code>showConstraintExpression</code> - indicates if constraint expression should be displayed.</dd>
<dd><code>addColorInformation</code> - indicates if color information should be added to the representation text.</dd>
<dd><code>showParameterDirectionKind</code> - indicates if parameter direction kind should be displayed.</dd>
<dt>Returns:</dt>
<dd>behavior text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createBehaviorText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createBehaviorText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
<div class="block">Creates behavior text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - behavior to represent.</dd>
<dd><code>showStereotype</code> - indicates if stereotypes should be displayed.</dd>
<dd><code>showProperties</code> - indicates if properties and tagged values should be displayed.</dd>
<dd><code>showInheritedSign</code> - indicates if inherited sign should be displayed.</dd>
<dd><code>showSignature</code> - indicates if behavior signature should be displayed.</dd>
<dd><code>showFullType</code> - indicates if full qualified type name should be displayed.</dd>
<dd><code>showConstraintName</code> - indicates if constraint name should be displayed.</dd>
<dd><code>showConstraintExpression</code> - indicates if constraint expression should be displayed.</dd>
<dd><code>addColorInformation</code> - indicates if color information should be added to the representation text.</dd>
<dd><code>showParameterDirectionKind</code> - indicates if parameter direction kind should be displayed.</dd>
<dd><code>showOpaqueBehaviorBody</code> - indicates if opaque behavior body should be displayed</dd>
<dt>Returns:</dt>
<dd>behavior text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createBehaviorText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createBehaviorText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean showSignature,
 boolean showFullType,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean addColorInformation,
 boolean showParameterDirectionKind,
 boolean showOpaqueBehaviorBody)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,com.nomagic.magicdraw.uml.text.BehaviorTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createBehaviorText(Behavior, BehaviorTextParams, Supplier)</code></a></div>
</div>
<div class="block">Creates behavior text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - behavior to represent.</dd>
<dd><code>showStereotype</code> - indicates if stereotypes should be displayed.</dd>
<dd><code>showProperties</code> - indicates if properties and tagged values should be displayed.</dd>
<dd><code>showInheritedSign</code> - indicates if inherited sign should be displayed.</dd>
<dd><code>showSignature</code> - indicates if behavior signature should be displayed.</dd>
<dd><code>showFullType</code> - indicates if full qualified type name should be displayed.</dd>
<dd><code>showConstraintName</code> - indicates if constraint name should be displayed.</dd>
<dd><code>showConstraintExpression</code> - indicates if constraint expression should be displayed.</dd>
<dd><code>addColorInformation</code> - indicates if color information should be added to the representation text.</dd>
<dd><code>showParameterDirectionKind</code> - indicates if parameter direction kind should be displayed.</dd>
<dd><code>showOpaqueBehaviorBody</code> - indicates if opaque behavior body should be displayed</dd>
<dt>Returns:</dt>
<dd>behavior text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>createStateText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStateText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> state)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State,java.util.function.Supplier)"><code>ModelTextCreator.createStateText(State, Supplier)</code></a></div>
</div>
<div class="block">Creates state name text. It appends SubMachine name if available.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - the state to create text for.</dd>
<dt>Returns:</dt>
<dd>string containing state name ad SubMachine name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>createStereotypeText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypeText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createStereotypesText(java.util.Collection,char)">
<h3>createStereotypesText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypesText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 char separator)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
<div class="block">Returns string representation of given.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - the collection of stereotypes.</dd>
<dd><code>separator</code> - the separator of stereotypes</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypesText(java.util.Collection,char,boolean,boolean)">
<h3>createStereotypesText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypesText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 char separator,
 boolean skipDSL,
 boolean useAlias)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Collection, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
<div class="block">Returns string representation of given.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - the collection of stereotypes.</dd>
<dd><code>separator</code> - the separator of stereotypes</dd>
<dd><code>skipDSL</code> - skip DSL stereotypes or nor</dd>
<dd><code>useAlias</code> - use DSL alias instead of name</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">
<h3>createStereotypeText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypeText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean useAlias)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypeText(Stereotype, StereotypeTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createStereotypeText(java.lang.String)">
<h3>createStereotypeText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypeText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypeText(java.lang.String)"><code>CoreTextCreator.createStereotypeText(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char)">
<h3>createStereotypesText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypesText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 char separator)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
<div class="block">Create the representation text of element be assigned stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - The given element.</dd>
<dd><code>separator</code> - The separator string.</dd>
<dt>Returns:</dt>
<dd>The string representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char,boolean,boolean)">
<h3>createStereotypesText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypesText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 char separator,
 boolean skipDSL,
 boolean useAlias)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)"><code>CoreTextCreator.createStereotypesText(Element, String, StereotypeTextParams, Supplier)</code></a></div>
</div>
<div class="block">Create the representation text of element be assigned stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - The given element.</dd>
<dd><code>separator</code> - The separator string.</dd>
<dd><code>skipDSL</code> - skip DSL stereotypes or nor</dd>
<dd><code>useAlias</code> - use DSL alias instead of name</dd>
<dt>Returns:</dt>
<dd>The string representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer)">
<h3>createPropertyPropertyStringText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createPropertyPropertyStringText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer,java.lang.String)">
<h3>createPropertyPropertyStringText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createPropertyPropertyStringText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>ModelTextCreatorUtils.appendPropertyPropertyStringText(Property, TextBuilder, String)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createOperationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createOperationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs operation representation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - operation which text will be created.</dd>
<dd><code>showParameters</code> - flag indicates if operation parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if operation visibility should be shown.</dd>
<dd><code>showFullType</code> - true for show full type</dd>
<dd><code>showStereotype</code> - show stereotype</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dd><code>showTemplateParameters</code> - </dd>
<dt>Returns:</dt>
<dd>method text string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createOperationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createOperationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs representation operation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - operation which text will be created.</dd>
<dd><code>showSignature</code> - flag indicates if method parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showStereotype</code> - show stereotype</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction kind</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dd><code>showTemplateParameters</code> - indicates if template parameters should be shown.</dd>
<dd><code>showParameterDefaultValue</code> - indicates if parameter default values should be shown.</dd>
<dt>Returns:</dt>
<dd>method text string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createOperationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createOperationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs representation operation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - operation which text will be created.</dd>
<dd><code>showSignature</code> - flag indicates if method parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showStereotype</code> - show stereotype</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction kind</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dd><code>showTemplateParameters</code> - indicates if template parameters should be shown.</dd>
<dd><code>showParameterDefaultValue</code> - indicates if parameter default values should be shown.</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dt>Returns:</dt>
<dd>method text string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createOperationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createOperationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 boolean showParameters,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showTemplateParameters,
 boolean showParameterDefaultValue,
 boolean showInheritedSign)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.magicdraw.uml.text.OperationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createOperationText(Operation, OperationTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs operation representation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - operation which text will be created.</dd>
<dd><code>showParameters</code> - flag indicates if operation parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if operation visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showStereotype</code> - show stereotype</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction kind</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dd><code>showTemplateParameters</code> - indicates if template parameters should be shown.</dd>
<dd><code>showParameterDefaultValue</code> - indicates if parameter default values should be shown.</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dt>Returns:</dt>
<dd>method text string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterDirectionText(com.nomagic.magicdraw.core.Project,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,boolean,boolean,boolean)">
<h3>createParameterDirectionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createParameterDirectionText</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameterMetaType,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> parameterDirection,
 boolean skipDefaultValue,
 boolean showReturnDirection,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>ModelTextCreator#createParameterDirectionText(ParameterDirectionKind, Project, ParameterDirectionTextParams, Supplier)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean)">
<h3>createParameterText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createParameterText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParameterText(Parameter, ParameterTextParams, Supplier)</code></a></div>
</div>
<div class="block">Creates text which represents parameter. for example "param : java::lang::String"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameter</code> - parameter which text will be created.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showParameterDirection</code> - show parameter direction</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>Created text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createParameterText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createParameterText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue,
 boolean skipDefaultDirection,
 boolean showReturnDirection)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean)">
<h3>createParameterText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createParameterText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showDefaultValue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParameterText(Parameter, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createParametersText(java.util.Collection,boolean,boolean,boolean,boolean,boolean)">
<h3>createParametersText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createParametersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation,
 boolean showParameterDefaultValue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createParametersText(java.util.Collection,boolean,boolean,boolean,boolean)">
<h3>createParametersText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createParametersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt; parameters,
 boolean showSignature,
 boolean showFullType,
 boolean showParameterDirection,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createParametersText(java.util.Collection,com.nomagic.magicdraw.uml.text.ParameterTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createParametersText(java.util.Collection, ParameterTextParams, java.util.function.Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean)">
<h3>createActivityParameterNodeText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createActivityParameterNodeText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a> parameter,
 boolean showFullType,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createActivityParameterNodeText(ActivityParameterNode, boolean, Supplier)</code></a></div>
</div>
<div class="block">Creates text which represents activity parameter node. for example "param : java::lang::String"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameter</code> - parameter which text will be created.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>addColorInformation</code> - indicates if color information should be added to the parameter text.</dd>
<dt>Returns:</dt>
<dd>Created text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createReceptionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createReceptionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs reception representation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reception</code> - reception which text will be created.</dd>
<dd><code>showSignature</code> - flag indicates if method parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>reception representation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createReceptionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createReceptionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs reception representation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reception</code> - reception which text will be created.</dd>
<dd><code>showSignature</code> - flag indicates if method parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>reception representation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createReceptionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createReceptionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a> reception,
 boolean showSignature,
 boolean showVisibility,
 boolean showFullType,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showParameterDirection,
 boolean showInheritedSign,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,com.nomagic.magicdraw.uml.text.ReceptionTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createReceptionText(Reception, ReceptionTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs reception representation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reception</code> - reception which text will be created.</dd>
<dd><code>showSignature</code> - flag indicates if method parameters should be shown.</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showParameterDirection</code> - show parameter direction</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>reception representation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>createGuardText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createGuardText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> msg)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,java.util.function.Supplier)"><code>ModelTextCreator.createGuardText(Message, Supplier)</code></a></div>
</div>
<div class="block">Creates Message guard text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>msg</code> - message</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean)">
<h3>createEnumerationLiteralText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createEnumerationLiteralText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs enumeration literal text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumLiteral</code> - EnumerationLiteral</dd>
<dd><code>showStereotype</code> - True, for show stereotype</dd>
<dd><code>showProperties</code> - True, for show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean)">
<h3>createEnumerationLiteralText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createEnumerationLiteralText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs enumeration literal text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumLiteral</code> - EnumerationLiteral</dd>
<dd><code>showStereotype</code> - True, for show stereotype</dd>
<dd><code>showProperties</code> - True, for show properties</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createEnumerationLiteralText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createEnumerationLiteralText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs enumeration literal text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumLiteral</code> - EnumerationLiteral</dd>
<dd><code>showStereotype</code> - True, for show stereotype</dd>
<dd><code>showProperties</code> - True, for show properties</dd>
<dd><code>showTaggedValues</code> - True, for show tagged values</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createEnumerationLiteralText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createEnumerationLiteralText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> enumLiteral,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showInheritedSign,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,com.nomagic.magicdraw.uml.text.MemberTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createEnumerationLiteralText(EnumerationLiteral, MemberTextParams, Supplier)</code></a></div>
</div>
<div class="block">Constructs enumeration literal text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumLiteral</code> - EnumerationLiteral</dd>
<dd><code>showStereotype</code> - True, for show stereotype</dd>
<dd><code>showProperties</code> - True, for show properties</dd>
<dd><code>showTaggedValues</code> - True, for show tagged values</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParametersText(java.util.Collection,java.lang.String)">
<h3>createTemplateParametersText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTemplateParametersText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> templateParameters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTemplateParametersText(java.util.Collection,java.lang.String,java.util.function.Supplier)"><code>ModelTextCreator.createTemplateParametersText(Collection, String, Supplier)</code></a></div>
</div>
<div class="block">Create the Template Parameters Text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateParameters</code> - The given TemplateParameters.</dd>
<dd><code>separator</code> - The text separator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">
<h3>createTemplateParameterText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTemplateParameterText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> tParameter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter,java.util.function.Supplier)"><code>ModelTextCreator.createTemplateParameterText(TemplateParameter, Supplier)</code></a></div>
</div>
<div class="block">Creates TemplateParameter text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tParameter</code> - The given TemplateParameter</dd>
<dt>Returns:</dt>
<dd>The create string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">
<h3>createTemplateBindingText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTemplateBindingText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> binding)</span></div>
<div class="block">Constructs given binding element text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>binding</code> - The given binding.</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean)">
<h3>createTemplateBindingText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTemplateBindingText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> binding,
 boolean attachTemplateParameterInfo)</span></div>
<div class="block">Constructs given binding element text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>binding</code> - The given binding.</dd>
<dd><code>attachTemplateParameterInfo</code> - indicates if full template parameter notation should be used.</dd>
<dt>Returns:</dt>
<dd>The created string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean)">
<h3>createTemplateParameterSubstitutionText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTemplateParameterSubstitutionText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> parameterSubstitution,
 boolean attachTemplateParameterInfo)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createTemplateParameterSubstitutionText(TemplateParameterSubstitution, boolean, Supplier)</code></a></div>
</div>
<div class="block">Create TemplateParameterSubstitution Text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterSubstitution</code> - The given ParameterSubstitution.</dd>
<dd><code>attachTemplateParameterInfo</code> - indicates if full template parameter notation should be used.</dd>
<dt>Returns:</dt>
<dd>The created text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPropertyText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPropertyText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showConstraints,
 boolean showMultiplicity,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
<div class="block">Constructs attribute view text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - attribute which text will be created.</dd>
<dd><code>showName</code> - show name</dd>
<dd><code>showType</code> - show type</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showInitValue</code> - indicates if initial value of attribute will be shown. @return attribute view text string.</dd>
<dd><code>showStereotype</code> - show stereotype</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showConstraints</code> - show constraints</dd>
<dd><code>showMultiplicity</code> - show multiplicity</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>property text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPropertyText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPropertyText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
<div class="block">Constructs attribute view text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - attribute which text will be created.</dd>
<dd><code>showName</code> - show name</dd>
<dd><code>showType</code> - show type</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showInitValue</code> - indicates if initial value of attribute will be shown. @return attribute view text string.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showTypeTaggedValues</code> - show tagged values</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showMultiplicity</code> - show multiplicity</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPropertyText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPropertyText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
<div class="block">Constructs attribute view text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - attribute which text will be created.</dd>
<dd><code>showName</code> - show name</dd>
<dd><code>showType</code> - show type</dd>
<dd><code>showDerived</code> - show derived sign</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showInitValue</code> - indicates if initial value of attribute will be shown. @return attribute view text string.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showTypeTaggedValues</code> - show tagged values</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showMultiplicity</code> - show multiplicity</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPropertyText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPropertyText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
<div class="block">Constructs attribute view text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - attribute which text will be created.</dd>
<dd><code>showName</code> - show name</dd>
<dd><code>showType</code> - show type</dd>
<dd><code>showDerived</code> - show derived sign</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showInitValue</code> - indicates if initial value of attribute will be shown. @return attribute view text string.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showTypeTaggedValues</code> - show tagged values</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showMultiplicity</code> - show multiplicity</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPropertyText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPropertyText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean showName,
 boolean showType,
 boolean showDerived,
 boolean showVisibility,
 boolean showFullType,
 boolean showInitValue,
 boolean showStereotype,
 boolean showProperties,
 boolean showTaggedValues,
 boolean showTypeTaggedValues,
 boolean showConstraintName,
 boolean showConstraintExpression,
 boolean showMultiplicity,
 boolean showInheritedSign,
 boolean addColorInformation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, java.util.function.Supplier)</code></a></div>
</div>
<div class="block">Constructs attribute view text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - attribute which text will be created.</dd>
<dd><code>showName</code> - show name</dd>
<dd><code>showType</code> - show type</dd>
<dd><code>showDerived</code> - show derived sign</dd>
<dd><code>showVisibility</code> - flag indicates if method visibility should be shown.</dd>
<dd><code>showFullType</code> - True for show full type.</dd>
<dd><code>showInitValue</code> - indicates if initial value of attribute will be shown. @return attribute view text string.</dd>
<dd><code>showStereotype</code> - show stereotypes</dd>
<dd><code>showProperties</code> - show properties</dd>
<dd><code>showTypeTaggedValues</code> - show tagged values</dd>
<dd><code>showConstraintName</code> - show constraint name</dd>
<dd><code>showConstraintExpression</code> - show constraint expression</dd>
<dd><code>showMultiplicity</code> - show multiplicity</dd>
<dd><code>showInheritedSign</code> - show inherited sign</dd>
<dd><code>addColorInformation</code> - add color</dd>
<dt>Returns:</dt>
<dd>text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean)">
<h3>createPortText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPortText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPortText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPortText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showTaggedValues,
 boolean showInheritedSign,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>createPortText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createPortText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean showInheritedSign,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.text.PropertyTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createPropertyText(Property, PropertyTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean)">
<h3>createInstanceSpecificationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createInstanceSpecificationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean,boolean)">
<h3>createInstanceSpecificationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createInstanceSpecificationText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean showClassifier,
 boolean showFullType,
 boolean addColor,
 boolean showAutoID)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.magicdraw.uml.text.InstanceSpecificationTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createInstanceSpecificationText(InstanceSpecification, InstanceSpecificationTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="appendGrayColor(java.lang.String)">
<h3>appendGrayColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">appendGrayColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="appendGrayColor(java.lang.StringBuffer)">
<h3>appendGrayColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">appendGrayColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="resetColor(java.lang.String)">
<h3>resetColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">resetColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String)"><code>RichTextStringUtils.closeColor(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="resetColor(java.lang.StringBuffer)">
<h3>resetColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuffer)"><code>RichTextStringUtils.closeColor(StringBuffer)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="appendColor(java.lang.StringBuffer,java.awt.Color)">
<h3>appendColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">appendColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuffer,java.awt.Color)"><code>RichTextStringUtils.startColor(StringBuffer, Color)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="appendColor(java.lang.String,java.awt.Color)">
<h3>appendColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">appendColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getPureTextFromColoredText(java.lang.String)">
<h3>getPureTextFromColoredText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPureTextFromColoredText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> coloredText)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/TextUtils.html#toPlainText(java.lang.String)"><code>TextUtils.toPlainText(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="startColorHtmlTag(java.lang.StringBuilder,java.awt.Color)">
<h3>startColorHtmlTag</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">startColorHtmlTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.StringBuilder,java.awt.Color)"><code>RichTextStringUtils.startColor(StringBuilder, Color)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="startColorHtmlTag(java.lang.String,java.awt.Color)">
<h3>startColorHtmlTag</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">startColorHtmlTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#startColor(java.lang.String,java.awt.Color)"><code>RichTextStringUtils.startColor(String, Color)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="endColorHtmlTag(java.lang.StringBuilder)">
<h3>endColorHtmlTag</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">endColorHtmlTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.StringBuilder)"><code>RichTextStringUtils.closeColor(StringBuilder)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createRepresentationTextComparator(boolean,boolean)">
<h3>createRepresentationTextComparator</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">createRepresentationTextComparator</span><wbr/><span class="parameters">(boolean addColor,
 boolean showAutoId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createRepresentationTextComparator(RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="endColorHtmlTag(java.lang.String)">
<h3>endColorHtmlTag</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">endColorHtmlTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../text/rich/RichTextStringUtils.html#closeColor(java.lang.String)"><code>RichTextStringUtils.closeColor(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 boolean noCache)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool,boolean)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> el,
 boolean addColor,
 boolean showElementNumber,
 boolean fullSignature,
 <a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool,
 boolean noCache)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean)"><code>RepresentationTextCreator.getRepresentedText(BaseElement, RepresentationTextParams, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">
<h3>createDefaultRepresentationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createDefaultRepresentationText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean addColor,
 boolean fullSignature)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">
<h3>createDefaultRepresentationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createDefaultRepresentationText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool)">
<h3>createDefaultRepresentationText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createDefaultRepresentationText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean addColor,
 boolean fullSignature,
 boolean showAutoId,
 <a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="RepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)"><code>RepresentationTextCreator.createDefaultRepresentationText(BaseElement, RepresentationTextParams)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="isAddColor()">
<h3>isAddColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAddColor</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>always returns false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAddColor(boolean)">
<h3>setAddColor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAddColor</span><wbr/><span class="parameters">(boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
<div class="block">Method has no impact, does not set the value</div>
</section>
</li>
<li>
<section class="detail" id="getLocationInTool()">
<h3>getLocationInTool</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">getLocationInTool</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters are now retrieved from <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> which is passed as argument for various methods</div>
</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>always returns <a href="../ui/LocationInTool.html#unknown"><code>LocationInTool.unknown</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool)">
<h3>setLocationInTool</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocationInTool</span><wbr/><span class="parameters">(<a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
<div class="block">Method has no impact, does not set the value</div>
</section>
</li>
<li>
<section class="detail" id="isShowFullType()">
<h3>isShowFullType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowFullType</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>always returns false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowFullType(boolean)">
<h3>setShowFullType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowFullType</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">text creation parameters should now be set in <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextParams</code></a> and passed as argument for methods when retrieving text</div>
</div>
<div class="block">Method has no impact, does not set the value</div>
</section>
</li>
<li>
<section class="detail" id="getRelationshipFromToRepresentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,boolean)">
<h3>getRelationshipFromToRepresentation</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRelationshipFromToRepresentation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> clientName,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierModelElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> supplierName,
 boolean showFullType,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createRelationshipFromToText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,java.util.function.Supplier)"><code>ModelTextCreator.createRelationshipFromToText(Element, Element, String, Element, String, boolean, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,boolean,boolean,boolean,boolean,boolean)">
<h3>createTypedElementText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createTypedElementText</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> typedElement,
 boolean showName,
 boolean showType,
 boolean showMultiplicity,
 boolean showFullType,
 boolean addColor)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/ModelTextCreator.html#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.magicdraw.uml.text.TypedElementTextParams,java.util.function.Supplier)"><code>ModelTextCreator.createTypedElementText(TypedElement, TypedElementTextParams, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createNamedElementListText(java.util.List)">
<h3>createNamedElementListText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createNamedElementListText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; elements)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createNamedElementListText(java.util.List,java.util.function.Supplier)"><code>CoreTextCreator.createNamedElementListText(java.util.List, Supplier)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">
<h3>createVisibilityText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">char</span> <span class="element-name">createVisibilityText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> visibility)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="text/CoreTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)"><code>CoreTextCreator.createVisibilityText(VisibilityKind)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createElementNameText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createElementNameText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createElementNameText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> o)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html#getName()"><code>NamedElement.getName()</code></a></div>
</div>
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
