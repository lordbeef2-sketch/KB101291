# JAVA OPENAPI: RepresentationTextCreator (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/RepresentationTextCreator.html
- source_path: `com/nomagic/magicdraw/uml/RepresentationTextCreator.html`
- source_sha256: `e99fc4adbbaa1fc2b98ad1e92492e45c4b306bed17a36575c413f7e9741127a9`
- captured_utc: `2026-07-14T16:55:55.573459+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class RepresentationTextCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator](DeprecatedRepresentationTextCreator.html)
com.nomagic.magicdraw.uml.RepresentationTextCreator

@OpenApiAllpublic classRepresentationTextCreator
extends [DeprecatedRepresentationTextCreator](DeprecatedRepresentationTextCreator.html)
Class for creating text of BaseElements represented in various UI components (tree nodes, text labels and etc).

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html)`
Representation text provider extension point.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.[DeprecatedRepresentationTextCreator](DeprecatedRepresentationTextCreator.html)
`[COLOR_POSTFIX](DeprecatedRepresentationTextCreator.html#COLOR_POSTFIX), [COLOR_PREFIX](DeprecatedRepresentationTextCreator.html#COLOR_PREFIX), [EMPTY_NAME_NOTATION](DeprecatedRepresentationTextCreator.html#EMPTY_NAME_NOTATION), [GRAY_COLOR_STRING](DeprecatedRepresentationTextCreator.html#GRAY_COLOR_STRING)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RepresentationTextCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addProvider](#addProvider(com.nomagic.magicdraw.uml.RepresentationTextCreator.RepresentationTextProvider))([RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html) provider)`
Registers a given representation text provider.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createDefaultRepresentationText](#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)`
Gets default (not extended) representation text.
`static [Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[BaseElement](BaseElement.html)>`
`[createRepresentationTextComparator](#createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams))([RepresentationTextParams](RepresentationTextParams.html) params)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAbsoluteUMLPathToRoot](#getAbsoluteUMLPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Method returns string representing path from root element to the given element.
`static boolean`
`[getFullName](#getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean checkTopStereotype)`
Get Element full name.
`static boolean`
`[getFullName](#getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean checkTopStereotype,
 boolean checkTopModelElement)`
Get Element full name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFullUMLName](#getFullUMLName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Method returns full UML name of element given element
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFullUMLName](#getFullUMLName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean doNotAddTopLevels)`
Get full UML Name of the given element
`static [RepresentationTextCreator](RepresentationTextCreator.html)`
`[getInstance](#getInstance())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModelElementNameWithParentPath](#getModelElementNameWithParentPath(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean))([NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 boolean addColor)`
Get element name with parent path.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModelElementParentPath](#getModelElementParentPath(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean addBrackets)`
Get element name with parent path.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPathToRoot](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get path of the given element to the root of element.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPathToRoot](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean checkTop)`
Get path of the given element to the root of element.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPathToRoot](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean relativeToLibrary,
 boolean compactMode)`
Calculates qualified name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPathToRoot](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean relativeToLibrary,
 boolean relativeToModel,
 boolean compactMode)`
Calculates qualified name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPathToRoot](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean toModelLibrary,
 boolean toModel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Get path to root.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPathToRoot](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean checkTop,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Get path to root.
`static [RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html)`
`[getProviderFor](#getProviderFor(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) element)`
Looks for a provider for a given element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRelationshipFromToPart](#getRelationshipFromToPart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.RepresentationTextParams))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) clientModelElement,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplierModelElement,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRelationshipFromToPart](#getRelationshipFromToPart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship,com.nomagic.magicdraw.uml.RepresentationTextParams))([Relationship](../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html) relationship,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) element)`
Returns representation text for the provided element
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)`
Returns representation text for the provided element
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean))([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams,
 boolean noCache)`
Returns representation text for the provided element
`boolean`
`[isCreateBoundElementName](#isCreateBoundElementName())()`

`static void`
`[removeProvider](#removeProvider(com.nomagic.magicdraw.uml.RepresentationTextCreator.RepresentationTextProvider))([RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html) provider)`
Unregisters a given representation text provider.
`void`
`[resetAutoIdRepresentations](#resetAutoIdRepresentations(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Clear the text cache for all elements that are part of the given project and have element numbers
`void`
`[setCreateBoundElementName](#setCreateBoundElementName(boolean))(boolean createBoundElementName)`
Methods inherited from class com.nomagic.magicdraw.uml.[DeprecatedRepresentationTextCreator](DeprecatedRepresentationTextCreator.html)
`[appendColor](DeprecatedRepresentationTextCreator.html#appendColor(java.lang.StringBuffer,java.awt.Color)), [appendColor](DeprecatedRepresentationTextCreator.html#appendColor(java.lang.String,java.awt.Color)), [appendGrayColor](DeprecatedRepresentationTextCreator.html#appendGrayColor(java.lang.String)), [appendGrayColor](DeprecatedRepresentationTextCreator.html#appendGrayColor(java.lang.StringBuffer)), [constructActivityEdgeText](DeprecatedRepresentationTextCreator.html#constructActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean)), [constructCombinedFragmentOperatorText](DeprecatedRepresentationTextCreator.html#constructCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)), [createActivityParameterNodeText](DeprecatedRepresentationTextCreator.html#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean)), [createAssociationText](DeprecatedRepresentationTextCreator.html#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [createBehaviorText](DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)), [createBehaviorText](DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createBehaviorText](DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createBehaviorText](DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createClassifierName](DeprecatedRepresentationTextCreator.html#createClassifierName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean,boolean)), [createClassifiersRepresentation](DeprecatedRepresentationTextCreator.html#createClassifiersRepresentation(java.util.Collection,boolean,boolean)), [createConstraintsText](DeprecatedRepresentationTextCreator.html#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean,boolean,boolean)), [createConstraintsText](DeprecatedRepresentationTextCreator.html#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean)), [createConstraintsText](DeprecatedRepresentationTextCreator.html#createConstraintsText(java.util.Collection,java.lang.String,boolean,boolean,boolean)), [createDefaultRepresentationText](DeprecatedRepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)), [createDefaultRepresentationText](DeprecatedRepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)), [createDefaultRepresentationText](DeprecatedRepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool)), [createElementNameText](DeprecatedRepresentationTextCreator.html#createElementNameText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [createEnumerationLiteralText](DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean)), [createEnumerationLiteralText](DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean)), [createEnumerationLiteralText](DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean)), [createEnumerationLiteralText](DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createEventText](DeprecatedRepresentationTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)), [createEventText](DeprecatedRepresentationTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,boolean,boolean)), [createGuardText](DeprecatedRepresentationTextCreator.html#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [createId](DeprecatedRepresentationTextCreator.html#createId(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [createInstanceSpecificationText](DeprecatedRepresentationTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean)), [createInstanceSpecificationText](DeprecatedRepresentationTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean,boolean)), [createInteractionUseText](DeprecatedRepresentationTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction)), [createInteractionUseText](DeprecatedRepresentationTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean,boolean)), [createMultiplicityRangeText](DeprecatedRepresentationTextCreator.html#createMultiplicityRangeText(java.lang.Integer)), [createMultiplicityText](DeprecatedRepresentationTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,boolean,boolean,boolean)), [createMultiplicityText](DeprecatedRepresentationTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer)), [createMultiplicityText](DeprecatedRepresentationTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,boolean)), [createMultiplicityText](DeprecatedRepresentationTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,boolean)), [createNamedElementListText](DeprecatedRepresentationTextCreator.html#createNamedElementListText(java.util.List)), [createOperandGuardText](DeprecatedRepresentationTextCreator.html#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)), [createOperationText](DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createOperationText](DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createOperationText](DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createOperationText](DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createParameterDirectionText](DeprecatedRepresentationTextCreator.html#createParameterDirectionText(com.nomagic.magicdraw.core.Project,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,boolean,boolean,boolean)), [createParametersText](DeprecatedRepresentationTextCreator.html#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean)), [createParametersText](DeprecatedRepresentationTextCreator.html#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean,boolean)), [createParameterText](DeprecatedRepresentationTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean)), [createParameterText](DeprecatedRepresentationTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean)), [createParameterText](DeprecatedRepresentationTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean,boolean,boolean)), [createPinText](DeprecatedRepresentationTextCreator.html#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,boolean,boolean,boolean,boolean,boolean,boolean)), [createPortText](DeprecatedRepresentationTextCreator.html#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean)), [createPortText](DeprecatedRepresentationTextCreator.html#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean)), [createPortText](DeprecatedRepresentationTextCreator.html#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createPropertyPropertyStringText](DeprecatedRepresentationTextCreator.html#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer)), [createPropertyPropertyStringText](DeprecatedRepresentationTextCreator.html#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer,java.lang.String)), [createPropertyText](DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createPropertyText](DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createPropertyText](DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createPropertyText](DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createPropertyText](DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createProtocolTransitionText](DeprecatedRepresentationTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)), [createProtocolTransitionText](DeprecatedRepresentationTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean)), [createProtocolTransitionText](DeprecatedRepresentationTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean,boolean,boolean)), [createPureSlotsString](DeprecatedRepresentationTextCreator.html#createPureSlotsString(java.util.Collection,java.lang.String,boolean,boolean)), [createReceptionText](DeprecatedRepresentationTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createReceptionText](DeprecatedRepresentationTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createReceptionText](DeprecatedRepresentationTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createRepresentationTextComparator](DeprecatedRepresentationTextCreator.html#createRepresentationTextComparator(boolean,boolean)), [createSlotsText](DeprecatedRepresentationTextCreator.html#createSlotsText(java.util.Collection,java.lang.String,boolean,boolean)), [createSlotText](DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createSlotText](DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createSlotText](DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createSlotText](DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)), [createStateText](DeprecatedRepresentationTextCreator.html#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)), [createStereotypesText](DeprecatedRepresentationTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char)), [createStereotypesText](DeprecatedRepresentationTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char,boolean,boolean)), [createStereotypesText](DeprecatedRepresentationTextCreator.html#createStereotypesText(java.util.Collection,char)), [createStereotypesText](DeprecatedRepresentationTextCreator.html#createStereotypesText(java.util.Collection,char,boolean,boolean)), [createStereotypeText](DeprecatedRepresentationTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [createStereotypeText](DeprecatedRepresentationTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)), [createStereotypeText](DeprecatedRepresentationTextCreator.html#createStereotypeText(java.lang.String)), [createTemplateBindingText](DeprecatedRepresentationTextCreator.html#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)), [createTemplateBindingText](DeprecatedRepresentationTextCreator.html#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean)), [createTemplateParametersText](DeprecatedRepresentationTextCreator.html#createTemplateParametersText(java.util.Collection,java.lang.String)), [createTemplateParameterSubstitutionText](DeprecatedRepresentationTextCreator.html#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean)), [createTemplateParameterText](DeprecatedRepresentationTextCreator.html#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [createTransitionText](DeprecatedRepresentationTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean)), [createTransitionText](DeprecatedRepresentationTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean)), [createTransitionText](DeprecatedRepresentationTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean,boolean,boolean)), [createTriggersText](DeprecatedRepresentationTextCreator.html#createTriggersText(java.util.Collection)), [createTriggersText](DeprecatedRepresentationTextCreator.html#createTriggersText(java.util.Collection,boolean)), [createTriggersText](DeprecatedRepresentationTextCreator.html#createTriggersText(java.util.Collection,boolean,boolean,boolean)), [createTriggerText](DeprecatedRepresentationTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger)), [createTriggerText](DeprecatedRepresentationTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean)), [createTriggerText](DeprecatedRepresentationTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean,boolean,boolean)), [createTypedElementText](DeprecatedRepresentationTextCreator.html#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,boolean,boolean,boolean,boolean,boolean)), [createTypeName](DeprecatedRepresentationTextCreator.html#createTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean)), [createValueSpecificationText](DeprecatedRepresentationTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [createVisibilityText](DeprecatedRepresentationTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)), [endColorHtmlTag](DeprecatedRepresentationTextCreator.html#endColorHtmlTag(java.lang.String)), [endColorHtmlTag](DeprecatedRepresentationTextCreator.html#endColorHtmlTag(java.lang.StringBuilder)), [getLocationInTool](DeprecatedRepresentationTextCreator.html#getLocationInTool()), [getPureTextFromColoredText](DeprecatedRepresentationTextCreator.html#getPureTextFromColoredText(java.lang.String)), [getRelationshipFromToRepresentation](DeprecatedRepresentationTextCreator.html#getRelationshipFromToRepresentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,boolean)), [getRepresentedText](DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean)), [getRepresentedText](DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)), [getRepresentedText](DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)), [getRepresentedText](DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean)), [getRepresentedText](DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool,boolean)), [isAddColor](DeprecatedRepresentationTextCreator.html#isAddColor()), [isShowFullType](DeprecatedRepresentationTextCreator.html#isShowFullType()), [resetColor](DeprecatedRepresentationTextCreator.html#resetColor(java.lang.String)), [resetColor](DeprecatedRepresentationTextCreator.html#resetColor(java.lang.StringBuffer)), [setAddColor](DeprecatedRepresentationTextCreator.html#setAddColor(boolean)), [setLocationInTool](DeprecatedRepresentationTextCreator.html#setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool)), [setShowFullType](DeprecatedRepresentationTextCreator.html#setShowFullType(boolean)), [startColorHtmlTag](DeprecatedRepresentationTextCreator.html#startColorHtmlTag(java.lang.StringBuilder,java.awt.Color)), [startColorHtmlTag](DeprecatedRepresentationTextCreator.html#startColorHtmlTag(java.lang.String,java.awt.Color))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RepresentationTextCreator
public RepresentationTextCreator()
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [RepresentationTextCreator](RepresentationTextCreator.html) getInstance()
Returns:
thread local specific instance
getRepresentedText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) element)
Returns representation text for the provided element
Parameters:
`element` - element which representation text will be created.
Returns:
representation text for the given element.
getRepresentedText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)
Returns representation text for the provided element
Parameters:
`element` - element which representation text will be created.
`textParams` - parameters describing how to construct the text, what to include
Returns:
representation text for the given element.
getRepresentedText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams,
 boolean noCache)
Returns representation text for the provided element
Parameters:
`element` - element which representation text will be created.
`textParams` - parameters describing how to construct the text, what to include
`noCache` - if false, cached text value (that was calculated earlier) can be returned
 if true, cache will not be used and representation text will be constructed
Returns:
representation text for the given element.
createDefaultRepresentationText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createDefaultRepresentationText([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)
Gets default (not extended) representation text.
 Representation text can be extended by adding a [`RepresentationTextCreator.RepresentationTextProvider`](RepresentationTextCreator.RepresentationTextProvider.html)
Parameters:
`element` - element for which to retrieve representation text.
`textParams` - parameters describing how to construct the text, what to include
getModelElementParentPath
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModelElementParentPath([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean addBrackets)
Get element name with parent path.
Parameters:
`element` - the given name element
`addBrackets` - true for add brackets to the string
Returns:
parent path
getModelElementNameWithParentPath
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModelElementNameWithParentPath([NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 boolean addColor)
Get element name with parent path.
Parameters:
`element` - the given name element
`addColor` - add color flag
Returns:
element name with parent path
getFullUMLName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFullUMLName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Method returns full UML name of element given element
Parameters:
`element` - element
Returns:
full element name with path to root
getFullUMLName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFullUMLName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean doNotAddTopLevels)
Get full UML Name of the given element
Parameters:
`element` - the given element
`doNotAddTopLevels` - do not add to top level
Returns:
full UML Name
getAbsoluteUMLPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAbsoluteUMLPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Method returns string representing path from root element to the given element.
Parameters:
`element` - element
Returns:
path from the the root element to the given one
getPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get path of the given element to the root of element.
Parameters:
`element` - the given element
Returns:
the path to root element element
getPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean checkTop)
Get path of the given element to the root of element.
Parameters:
`element` - the given element
`checkTop` - true for check the root
Returns:
the path to root element element
getPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean relativeToLibrary,
 boolean compactMode)
Calculates qualified name. It can generate string using standard UML notation (using double colon for separator) or in the old MagicDraw style (surrounded with parentheses).
 For more options see [`getPathToRoot(Element, boolean, boolean, boolean)`](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean))
Parameters:
`element` - model element used to calculate qualified name
`relativeToLibrary` - if true, then qualified name is calculated from "model library" element, otherwise qualified name is calculated from root.
`compactMode` - if true, then old MagicDraw notation is used, otherwise uses standard UML notation
Returns:
string containing "name space" qualified name part.
getPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean relativeToLibrary,
 boolean relativeToModel,
 boolean compactMode)
Calculates qualified name. It can generate string using standard UML notation (using double colon for separator) or in the old MagicDraw style (surrounded with parentheses).
Parameters:
`element` - model element used to calculate qualified name
`relativeToLibrary` - if true, then qualified name is calculated from "model library" element, otherwise qualified name is calculated from root.
`relativeToModel` - if true, then qualified name is calculated from nearest "model" element, otherwise qualified name is calculated from root.
`compactMode` - if true, then old MagicDraw notation is used, otherwise uses standard UML notation
Returns:
string containing "name space" qualified name part.
getPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean checkTop,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Get path to root. For More options see [`getPathToRoot(Element, boolean, boolean, String)`](#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,java.lang.String))
Parameters:
`element` - the given element
`checkTop` - true for check the root
`separator` - separator to use to create a path
Returns:
string
getPathToRoot
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPathToRoot([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean toModelLibrary,
 boolean toModel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Get path to root.
Parameters:
`element` - the given element
`toModelLibrary` - if true, stops at model library
`toModel` - if true, stops at mode element
`separator` - separator to use to create a path
Returns:
string
getFullName
public static boolean getFullName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean checkTopStereotype)
Get Element full name. For more options see [`getFullName(Element, StringBuffer, String, boolean, boolean)`](#getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean,boolean)).
Parameters:
`element` - the given element
`path` - Path of element
`separator` - the separator
`checkTopStereotype` - is check top stereotype
Returns:
true if element is NamedElement, otherwise false.
getFullName
public static boolean getFullName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [StringBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html) path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 boolean checkTopStereotype,
 boolean checkTopModelElement)
Get Element full name.
Parameters:
`element` - The NameElement.
`path` - Path of NameElement.
`separator` - The separator.
`checkTopStereotype` - Is check to stereotype?
`checkTopModelElement` - indicates Model model element check
Returns:
true if element is NamedElement, otherwise false.
addProvider
public static void addProvider([RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html) provider)
Registers a given representation text provider.
Parameters:
`provider` - provider
removeProvider
public static void removeProvider([RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html) provider)
Unregisters a given representation text provider.
Parameters:
`provider` - provider
getProviderFor
@CheckForNullpublic static [RepresentationTextCreator.RepresentationTextProvider](RepresentationTextCreator.RepresentationTextProvider.html) getProviderFor([BaseElement](BaseElement.html) element)
Looks for a provider for a given element.
Parameters:
`element` - given element
Returns:
found provider or null
getRelationshipFromToPart
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRelationshipFromToPart([Relationship](../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html) relationship,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)
getRelationshipFromToPart
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRelationshipFromToPart([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) clientModelElement,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplierModelElement,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)
isCreateBoundElementName
public boolean isCreateBoundElementName()
setCreateBoundElementName
public void setCreateBoundElementName(boolean createBoundElementName)
resetAutoIdRepresentations
public void resetAutoIdRepresentations([Project](../core/Project.html) project)
Clear the text cache for all elements that are part of the given project and have element numbers
Parameters:
`project` - project
createRepresentationTextComparator
public static [Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[BaseElement](BaseElement.html)> createRepresentationTextComparator([RepresentationTextParams](RepresentationTextParams.html) params)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class RepresentationTextCreator">Class RepresentationTextCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="DeprecatedRepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator</a>
<div class="inheritance">com.nomagic.magicdraw.uml.RepresentationTextCreator</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RepresentationTextCreator</span>
<span class="extends-implements">extends <a href="DeprecatedRepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">DeprecatedRepresentationTextCreator</a></span></div>
<div class="block">Class for creating text of BaseElements represented in various UI components (tree nodes, text labels and etc).</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a></code></div>
<div class="col-last even-row-color">
<div class="block">Representation text provider extension point.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator">Fields inherited from class com.nomagic.magicdraw.uml.<a href="DeprecatedRepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">DeprecatedRepresentationTextCreator</a></h3>
<code><a href="DeprecatedRepresentationTextCreator.html#COLOR_POSTFIX">COLOR_POSTFIX</a>, <a href="DeprecatedRepresentationTextCreator.html#COLOR_PREFIX">COLOR_PREFIX</a>, <a href="DeprecatedRepresentationTextCreator.html#EMPTY_NAME_NOTATION">EMPTY_NAME_NOTATION</a>, <a href="DeprecatedRepresentationTextCreator.html#GRAY_COLOR_STRING">GRAY_COLOR_STRING</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RepresentationTextCreator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addProvider(com.nomagic.magicdraw.uml.RepresentationTextCreator.RepresentationTextProvider)">addProvider</a><wbr/>(<a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers a given representation text provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)">createDefaultRepresentationText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets default (not extended) representation text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams)">createRepresentationTextComparator</a><wbr/>(<a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> params)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbsoluteUMLPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAbsoluteUMLPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method returns string representing path from root element to the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean)">getFullName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean checkTopStereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Element full name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean,boolean)">getFullName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean checkTopStereotype,
 boolean checkTopModelElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Element full name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFullUMLName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getFullUMLName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method returns full UML name of element given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFullUMLName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getFullUMLName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean doNotAddTopLevels)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get full UML Name of the given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextCreator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElementNameWithParentPath(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">getModelElementNameWithParentPath</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 boolean addColor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get element name with parent path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElementParentPath(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getModelElementParentPath</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean addBrackets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get element name with parent path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get path of the given element to the root of element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean checkTop)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get path of the given element to the root of element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">getPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean relativeToLibrary,
 boolean compactMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)">getPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean relativeToLibrary,
 boolean relativeToModel,
 boolean compactMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,java.lang.String)">getPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean toModelLibrary,
 boolean toModel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get path to root.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,java.lang.String)">getPathToRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean checkTop,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get path to root.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProviderFor(com.nomagic.magicdraw.uml.BaseElement)">getProviderFor</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a provider for a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipFromToPart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.RepresentationTextParams)">getRelationshipFromToPart</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientModelElement,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierModelElement,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipFromToPart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship,com.nomagic.magicdraw.uml.RepresentationTextParams)">getRelationshipFromToPart</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a> relationship,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns representation text for the provided element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns representation text for the provided element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams,
 boolean noCache)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns representation text for the provided element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateBoundElementName()">isCreateBoundElementName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProvider(com.nomagic.magicdraw.uml.RepresentationTextCreator.RepresentationTextProvider)">removeProvider</a><wbr/>(<a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregisters a given representation text provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetAutoIdRepresentations(com.nomagic.magicdraw.core.Project)">resetAutoIdRepresentations</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear the text cache for all elements that are part of the given project and have element numbers</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateBoundElementName(boolean)">setCreateBoundElementName</a><wbr/>(boolean createBoundElementName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.DeprecatedRepresentationTextCreator">Methods inherited from class com.nomagic.magicdraw.uml.<a href="DeprecatedRepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">DeprecatedRepresentationTextCreator</a></h3>
<code><a href="DeprecatedRepresentationTextCreator.html#appendColor(java.lang.StringBuffer,java.awt.Color)">appendColor</a>, <a href="DeprecatedRepresentationTextCreator.html#appendColor(java.lang.String,java.awt.Color)">appendColor</a>, <a href="DeprecatedRepresentationTextCreator.html#appendGrayColor(java.lang.String)">appendGrayColor</a>, <a href="DeprecatedRepresentationTextCreator.html#appendGrayColor(java.lang.StringBuffer)">appendGrayColor</a>, <a href="DeprecatedRepresentationTextCreator.html#constructActivityEdgeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge,boolean)">constructActivityEdgeText</a>, <a href="DeprecatedRepresentationTextCreator.html#constructCombinedFragmentOperatorText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">constructCombinedFragmentOperatorText</a>, <a href="DeprecatedRepresentationTextCreator.html#createActivityParameterNodeText(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityParameterNode,boolean,boolean)">createActivityParameterNodeText</a>, <a href="DeprecatedRepresentationTextCreator.html#createAssociationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">createAssociationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">createBehaviorText</a>, <a href="DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createBehaviorText</a>, <a href="DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createBehaviorText</a>, <a href="DeprecatedRepresentationTextCreator.html#createBehaviorText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createBehaviorText</a>, <a href="DeprecatedRepresentationTextCreator.html#createClassifierName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean,boolean)">createClassifierName</a>, <a href="DeprecatedRepresentationTextCreator.html#createClassifiersRepresentation(java.util.Collection,boolean,boolean)">createClassifiersRepresentation</a>, <a href="DeprecatedRepresentationTextCreator.html#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,boolean,boolean,boolean)">createConstraintsText</a>, <a href="DeprecatedRepresentationTextCreator.html#createConstraintsText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean)">createConstraintsText</a>, <a href="DeprecatedRepresentationTextCreator.html#createConstraintsText(java.util.Collection,java.lang.String,boolean,boolean,boolean)">createConstraintsText</a>, <a href="DeprecatedRepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">createDefaultRepresentationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">createDefaultRepresentationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool)">createDefaultRepresentationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createElementNameText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createElementNameText</a>, <a href="DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a>, <a href="DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a>, <a href="DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a>, <a href="DeprecatedRepresentationTextCreator.html#createEnumerationLiteralText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createEnumerationLiteralText</a>, <a href="DeprecatedRepresentationTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">createEventText</a>, <a href="DeprecatedRepresentationTextCreator.html#createEventText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event,boolean,boolean)">createEventText</a>, <a href="DeprecatedRepresentationTextCreator.html#createGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">createGuardText</a>, <a href="DeprecatedRepresentationTextCreator.html#createId(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">createId</a>, <a href="DeprecatedRepresentationTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean)">createInstanceSpecificationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createInstanceSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean,boolean,boolean,boolean)">createInstanceSpecificationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallBehaviorAction)">createInteractionUseText</a>, <a href="DeprecatedRepresentationTextCreator.html#createInteractionUseText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse,boolean,boolean)">createInteractionUseText</a>, <a href="DeprecatedRepresentationTextCreator.html#createMultiplicityRangeText(java.lang.Integer)">createMultiplicityRangeText</a>, <a href="DeprecatedRepresentationTextCreator.html#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,boolean,boolean,boolean)">createMultiplicityText</a>, <a href="DeprecatedRepresentationTextCreator.html#createMultiplicityText(java.lang.Integer,java.lang.Integer)">createMultiplicityText</a>, <a href="DeprecatedRepresentationTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,boolean)">createMultiplicityText</a>, <a href="DeprecatedRepresentationTextCreator.html#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,boolean)">createMultiplicityText</a>, <a href="DeprecatedRepresentationTextCreator.html#createNamedElementListText(java.util.List)">createNamedElementListText</a>, <a href="DeprecatedRepresentationTextCreator.html#createOperandGuardText(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)">createOperandGuardText</a>, <a href="DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createOperationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createOperationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createParameterDirectionText(com.nomagic.magicdraw.core.Project,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,boolean,boolean,boolean)">createParameterDirectionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean)">createParametersText</a>, <a href="DeprecatedRepresentationTextCreator.html#createParametersText(java.util.Collection,boolean,boolean,boolean,boolean,boolean)">createParametersText</a>, <a href="DeprecatedRepresentationTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean)">createParameterText</a>, <a href="DeprecatedRepresentationTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean)">createParameterText</a>, <a href="DeprecatedRepresentationTextCreator.html#createParameterText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,boolean,boolean,boolean,boolean,boolean,boolean)">createParameterText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPinText(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin,boolean,boolean,boolean,boolean,boolean,boolean)">createPinText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean)">createPortText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean)">createPortText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPortText(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPortText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer)">createPropertyPropertyStringText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyPropertyStringText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.StringBuffer,java.lang.String)">createPropertyPropertyStringText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPropertyText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createPropertyText</a>, <a href="DeprecatedRepresentationTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">createProtocolTransitionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean)">createProtocolTransitionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createProtocolTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition,boolean,boolean,boolean)">createProtocolTransitionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createPureSlotsString(java.util.Collection,java.lang.String,boolean,boolean)">createPureSlotsString</a>, <a href="DeprecatedRepresentationTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createReceptionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createReceptionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createReceptionText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Reception,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createReceptionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createRepresentationTextComparator(boolean,boolean)">createRepresentationTextComparator</a>, <a href="DeprecatedRepresentationTextCreator.html#createSlotsText(java.util.Collection,java.lang.String,boolean,boolean)">createSlotsText</a>, <a href="DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a>, <a href="DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a>, <a href="DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a>, <a href="DeprecatedRepresentationTextCreator.html#createSlotText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">createSlotText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStateText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">createStateText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char)">createStereotypesText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,char,boolean,boolean)">createStereotypesText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypesText(java.util.Collection,char)">createStereotypesText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypesText(java.util.Collection,char,boolean,boolean)">createStereotypesText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">createStereotypeText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">createStereotypeText</a>, <a href="DeprecatedRepresentationTextCreator.html#createStereotypeText(java.lang.String)">createStereotypeText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">createTemplateBindingText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTemplateBindingText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding,boolean)">createTemplateBindingText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTemplateParametersText(java.util.Collection,java.lang.String)">createTemplateParametersText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTemplateParameterSubstitutionText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution,boolean)">createTemplateParameterSubstitutionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTemplateParameterText(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">createTemplateParameterText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean)">createTransitionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean)">createTransitionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTransitionText(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,boolean,boolean,boolean,boolean,boolean)">createTransitionText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTriggersText(java.util.Collection)">createTriggersText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTriggersText(java.util.Collection,boolean)">createTriggersText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTriggersText(java.util.Collection,boolean,boolean,boolean)">createTriggersText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger)">createTriggerText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean)">createTriggerText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTriggerText(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Trigger,boolean,boolean,boolean)">createTriggerText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTypedElementText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,boolean,boolean,boolean,boolean,boolean)">createTypedElementText</a>, <a href="DeprecatedRepresentationTextCreator.html#createTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,boolean)">createTypeName</a>, <a href="DeprecatedRepresentationTextCreator.html#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">createValueSpecificationText</a>, <a href="DeprecatedRepresentationTextCreator.html#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">createVisibilityText</a>, <a href="DeprecatedRepresentationTextCreator.html#endColorHtmlTag(java.lang.String)">endColorHtmlTag</a>, <a href="DeprecatedRepresentationTextCreator.html#endColorHtmlTag(java.lang.StringBuilder)">endColorHtmlTag</a>, <a href="DeprecatedRepresentationTextCreator.html#getLocationInTool()">getLocationInTool</a>, <a href="DeprecatedRepresentationTextCreator.html#getPureTextFromColoredText(java.lang.String)">getPureTextFromColoredText</a>, <a href="DeprecatedRepresentationTextCreator.html#getRelationshipFromToRepresentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean,boolean)">getRelationshipFromToRepresentation</a>, <a href="DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean)">getRepresentedText</a>, <a href="DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">getRepresentedText</a>, <a href="DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean)">getRepresentedText</a>, <a href="DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,boolean)">getRepresentedText</a>, <a href="DeprecatedRepresentationTextCreator.html#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,boolean,boolean,boolean,com.nomagic.magicdraw.ui.LocationInTool,boolean)">getRepresentedText</a>, <a href="DeprecatedRepresentationTextCreator.html#isAddColor()">isAddColor</a>, <a href="DeprecatedRepresentationTextCreator.html#isShowFullType()">isShowFullType</a>, <a href="DeprecatedRepresentationTextCreator.html#resetColor(java.lang.String)">resetColor</a>, <a href="DeprecatedRepresentationTextCreator.html#resetColor(java.lang.StringBuffer)">resetColor</a>, <a href="DeprecatedRepresentationTextCreator.html#setAddColor(boolean)">setAddColor</a>, <a href="DeprecatedRepresentationTextCreator.html#setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool)">setLocationInTool</a>, <a href="DeprecatedRepresentationTextCreator.html#setShowFullType(boolean)">setShowFullType</a>, <a href="DeprecatedRepresentationTextCreator.html#startColorHtmlTag(java.lang.StringBuilder,java.awt.Color)">startColorHtmlTag</a>, <a href="DeprecatedRepresentationTextCreator.html#startColorHtmlTag(java.lang.String,java.awt.Color)">startColorHtmlTag</a></code></div>
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
<h3>RepresentationTextCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RepresentationTextCreator</span>()</div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="RepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextCreator</a></span> <span class="element-name">getInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>thread local specific instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns representation text for the provided element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which representation text will be created.</dd>
<dt>Returns:</dt>
<dd>representation text for the given element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</span></div>
<div class="block">Returns representation text for the provided element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which representation text will be created.</dd>
<dd><code>textParams</code> - parameters describing how to construct the text, what to include</dd>
<dt>Returns:</dt>
<dd>representation text for the given element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams,boolean)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams,
 boolean noCache)</span></div>
<div class="block">Returns representation text for the provided element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which representation text will be created.</dd>
<dd><code>textParams</code> - parameters describing how to construct the text, what to include</dd>
<dd><code>noCache</code> - if false, cached text value (that was calculated earlier) can be returned
                   if true, cache will not be used and representation text will be constructed</dd>
<dt>Returns:</dt>
<dd>representation text for the given element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultRepresentationText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)">
<h3>createDefaultRepresentationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createDefaultRepresentationText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</span></div>
<div class="block">Gets default (not extended) representation text.
 Representation text can be extended by adding a <a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml"><code>RepresentationTextCreator.RepresentationTextProvider</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which to retrieve representation text.</dd>
<dd><code>textParams</code> - parameters describing how to construct the text, what to include</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelElementParentPath(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getModelElementParentPath</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModelElementParentPath</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean addBrackets)</span></div>
<div class="block">Get element name with parent path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given name element</dd>
<dd><code>addBrackets</code> - true for add brackets to the string</dd>
<dt>Returns:</dt>
<dd>parent path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelElementNameWithParentPath(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">
<h3>getModelElementNameWithParentPath</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModelElementNameWithParentPath</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 boolean addColor)</span></div>
<div class="block">Get element name with parent path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given name element</dd>
<dd><code>addColor</code> - add color flag</dd>
<dt>Returns:</dt>
<dd>element name with parent path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFullUMLName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getFullUMLName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFullUMLName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Method returns full UML name of element given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>full element name with path to root</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFullUMLName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getFullUMLName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFullUMLName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean doNotAddTopLevels)</span></div>
<div class="block">Get full UML Name of the given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>doNotAddTopLevels</code> - do not add to top level</dd>
<dt>Returns:</dt>
<dd>full UML Name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbsoluteUMLPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAbsoluteUMLPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAbsoluteUMLPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Method returns string representing path from root element to the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>path from the the root element to the given one</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get path of the given element to the root of element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dt>Returns:</dt>
<dd>the path to root element element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean checkTop)</span></div>
<div class="block">Get path of the given element to the root of element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>checkTop</code> - true for check the root</dd>
<dt>Returns:</dt>
<dd>the path to root element element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">
<h3>getPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean relativeToLibrary,
 boolean compactMode)</span></div>
<div class="block">Calculates qualified name. It can generate string using standard UML notation (using double colon for separator) or in the old MagicDraw style (surrounded with parentheses).
 For more options see <a href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)"><code>getPathToRoot(Element, boolean, boolean, boolean)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element used to calculate qualified name</dd>
<dd><code>relativeToLibrary</code> - if true, then qualified name is calculated from "model library" element, otherwise qualified name is calculated from root.</dd>
<dd><code>compactMode</code> - if true, then old MagicDraw notation is used, otherwise uses standard UML notation</dd>
<dt>Returns:</dt>
<dd>string containing "name space" qualified name part.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)">
<h3>getPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean relativeToLibrary,
 boolean relativeToModel,
 boolean compactMode)</span></div>
<div class="block">Calculates qualified name. It can generate string using standard UML notation (using double colon for separator) or in the old MagicDraw style (surrounded with parentheses).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element used to calculate qualified name</dd>
<dd><code>relativeToLibrary</code> - if true, then qualified name is calculated from "model library" element, otherwise qualified name is calculated from root.</dd>
<dd><code>relativeToModel</code> - if true, then qualified name is calculated from nearest "model" element, otherwise qualified name is calculated from root.</dd>
<dd><code>compactMode</code> - if true, then old MagicDraw notation is used, otherwise uses standard UML notation</dd>
<dt>Returns:</dt>
<dd>string containing "name space" qualified name part.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,java.lang.String)">
<h3>getPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean checkTop,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Get path to root. For More options see <a href="#getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,java.lang.String)"><code>getPathToRoot(Element, boolean, boolean, String)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>checkTop</code> - true for check the root</dd>
<dd><code>separator</code> - separator to use to create a path</dd>
<dt>Returns:</dt>
<dd>string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathToRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,java.lang.String)">
<h3>getPathToRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPathToRoot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean toModelLibrary,
 boolean toModel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Get path to root.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>toModelLibrary</code> - if true, stops at model library</dd>
<dd><code>toModel</code> - if true, stops at mode element</dd>
<dd><code>separator</code> - separator to use to create a path</dd>
<dt>Returns:</dt>
<dd>string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean)">
<h3>getFullName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">getFullName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean checkTopStereotype)</span></div>
<div class="block">Get Element full name. For more options see <a href="#getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean,boolean)"><code>getFullName(Element, StringBuffer, String, boolean, boolean)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>path</code> - Path of element</dd>
<dd><code>separator</code> - the separator</dd>
<dd><code>checkTopStereotype</code> - is check top stereotype</dd>
<dt>Returns:</dt>
<dd>true if element is NamedElement, otherwise false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFullName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.StringBuffer,java.lang.String,boolean,boolean)">
<h3>getFullName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">getFullName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 boolean checkTopStereotype,
 boolean checkTopModelElement)</span></div>
<div class="block">Get Element full name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - The NameElement.</dd>
<dd><code>path</code> - Path of NameElement.</dd>
<dd><code>separator</code> - The separator.</dd>
<dd><code>checkTopStereotype</code> - Is check to stereotype?</dd>
<dd><code>checkTopModelElement</code> - indicates Model model element check</dd>
<dt>Returns:</dt>
<dd>true if element is NamedElement, otherwise false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProvider(com.nomagic.magicdraw.uml.RepresentationTextCreator.RepresentationTextProvider)">
<h3>addProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addProvider</span><wbr/><span class="parameters">(<a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a> provider)</span></div>
<div class="block">Registers a given representation text provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProvider(com.nomagic.magicdraw.uml.RepresentationTextCreator.RepresentationTextProvider)">
<h3>removeProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeProvider</span><wbr/><span class="parameters">(<a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a> provider)</span></div>
<div class="block">Unregisters a given representation text provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProviderFor(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getProviderFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a></span> <span class="element-name">getProviderFor</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Looks for a provider for a given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>found provider or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationshipFromToPart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship,com.nomagic.magicdraw.uml.RepresentationTextParams)">
<h3>getRelationshipFromToPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRelationshipFromToPart</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a> relationship,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRelationshipFromToPart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.RepresentationTextParams)">
<h3>getRelationshipFromToPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRelationshipFromToPart</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientModelElement,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierModelElement,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCreateBoundElementName()">
<h3>isCreateBoundElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateBoundElementName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCreateBoundElementName(boolean)">
<h3>setCreateBoundElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateBoundElementName</span><wbr/><span class="parameters">(boolean createBoundElementName)</span></div>
</section>
</li>
<li>
<section class="detail" id="resetAutoIdRepresentations(com.nomagic.magicdraw.core.Project)">
<h3>resetAutoIdRepresentations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetAutoIdRepresentations</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Clear the text cache for all elements that are part of the given project and have element numbers</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRepresentationTextComparator(com.nomagic.magicdraw.uml.RepresentationTextParams)">
<h3>createRepresentationTextComparator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">createRepresentationTextComparator</span><wbr/><span class="parameters">(<a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> params)</span></div>
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
