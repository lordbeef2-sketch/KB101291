# JAVA OPENAPI: ClassifierView (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/shapes/ClassifierView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/ClassifierView.html`
- source_sha256: `788360ad0dff3fb2969ef0eb822ccfaef7d447104c3156bf9a768bc45e81a73c`
- captured_utc: `2026-07-14T16:56:03.229545+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class ClassifierView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `com.nomagic.magicdraw.uml.CompartmentSupport`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.CompartmentContainer`, `com.nomagic.magicdraw.uml.symbols.CompartmentOwner`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `com.nomagic.magicdraw.uml.symbols.shapes.PortOwner`, `com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner`, `[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `com.nomagic.magicdraw.uml.symbols.Wrapable`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[ActorView](ActorView.html)`, `[ArtifactView](ArtifactView.html)`, `[ClassView](ClassView.html)`, `[DataTypeView](DataTypeView.html)`, `[EnumerationView](EnumerationView.html)`, `[InformationItemView](InformationItemView.html)`, `[InterfaceView](InterfaceView.html)`, `[PrimitiveTypeView](PrimitiveTypeView.html)`, `[SignalView](SignalView.html)`, `[StereotypeView](StereotypeView.html)`

@OpenApipublic abstract classClassifierView
extends com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
implements com.nomagic.magicdraw.uml.symbols.shapes.PortOwner, com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ALL](#ALL)`
Members display options - display all members.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[ASSOCIATION_ENDS_DISPLAY_MODES](#ASSOCIATION_ENDS_DISPLAY_MODES)`
List of available association ends display in attribute compartment mode.
`static final [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[DEFAULT_SIZE](#DEFAULT_SIZE)`

`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[MEMBERS_DISPLAY_MODES](#MEMBERS_DISPLAY_MODES)`
List of available members display options.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NOT_PRIVATE](#NOT_PRIVATE)`
Members display options - not private members.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ONLY_PUBLIC](#ONLY_PUBLIC)`
Members display options - display only public members.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[WITHOUT_ASSOCIATION](#WITHOUT_ASSOCIATION)`
Association ends display options - display association end if association symbol is not drawn in the diagram.
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
`SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_IMAGE_AND_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODES`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[BORDER_ELEMENT_MARGIN_ALL](ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL), [BORDER_ELEMENT_MARGIN_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM), [BORDER_ELEMENT_MARGIN_LEFT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT), [BORDER_ELEMENT_MARGIN_LEFT_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT), [BORDER_ELEMENT_MARGIN_MODES](ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES), [BORDER_ELEMENT_MARGIN_NONE](ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE), [BORDER_ELEMENT_MARGIN_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT), [BORDER_ELEMENT_MARGIN_TOP](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP), [BORDER_ELEMENT_MARGIN_TOP_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM), [BOTTOM_EDGE](ShapeElement.html#BOTTOM_EDGE), [INSIDE_EDGE_POSITION](ShapeElement.html#INSIDE_EDGE_POSITION), [LEFT_EDGE](ShapeElement.html#LEFT_EDGE), [NEED_AUTOSIZE_FULL](ShapeElement.html#NEED_AUTOSIZE_FULL), [NEED_AUTOSIZE_LAYOUT](ShapeElement.html#NEED_AUTOSIZE_LAYOUT), [NEED_AUTOSIZE_NONE](ShapeElement.html#NEED_AUTOSIZE_NONE), [NO_EDGE](ShapeElement.html#NO_EDGE), [NULL_INSETS](ShapeElement.html#NULL_INSETS), [ON_EDGE_POSITION](ShapeElement.html#ON_EDGE_POSITION), [OUTSIDE_EDGE_POSITION](ShapeElement.html#OUTSIDE_EDGE_POSITION), [RIGHT_EDGE](ShapeElement.html#RIGHT_EDGE), [SPACE](ShapeElement.html#SPACE), [SPACE_INSETS](ShapeElement.html#SPACE_INSETS), [SPACE_INSETS_EMPTY_TOP_BOTTOM](ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM), [TOP_EDGE](ShapeElement.html#TOP_EDGE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[showsProxy](../paths/PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner
`QNAME_DISPLAY_MODE_ABOVE_NAME, QNAME_DISPLAY_MODE_BELOW_NAME, QNAME_DISPLAY_MODE_DO_NOT_DISPLAY, QNAME_DISPLAY_MODE_MERGE_WITH_NAME, QNAME_DISPLAY_MODES`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner
`DO_NOT_DISPLAY, IN_COMPARTMENT, ON_SHAPE, TAGGED_VALUES_DISPLAY_MODES`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
``
`[ClassifierView](#%3Cinit%3E())()`

``
`[ClassifierView](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`

`protected`
`[ClassifierView](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView,boolean))([PresentationElement](../PresentationElement.html) parent,
 com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView header,
 boolean canDisplayStructure)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`boolean`
`[addConnectedPathElement](#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) element)`
Adds a new path element, and recalculates its position.
`void`
`[addPresentationElement](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean))([PresentationElement](../PresentationElement.html) element,
 int index,
 boolean resize)`
If a specified object not inserted in this container then adds a new object view to the container.
`void`
`[atInsert](#atInsert())()`
Invalidates object at insert
`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Check of given symbol can be added as child into this symbol.
`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Object view has no children.
`boolean`
`[canStereotypeIconGrow](#canStereotypeIconGrow())()`

`[ClassifierView](ClassifierView.html)`
`[clone](#clone())()`

`[ContainerShape](../../../../awt/ContainerShape.html)`
`[createBoundsShape](#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))([PathElement](../paths/PathElement.html) path,
 [BoundsTransformation](../BoundsTransformation.html) transformation)`
Creates bounding shape for intersection calculation.
`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[createStateForUpdateOperation](#createStateForUpdateOperation())()`
Create collection of any properties used to distinguish during shape update if movePathElements should be called
`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`protected void`
`[drawShadow](#drawShadow(java.awt.Graphics))([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g)`

`protected com.nomagic.ui.UnmodifiableInsets`
`[getAdditionalCompartmentInsets](#getAdditionalCompartmentInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel))(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel level)`

`protected int`
`[getAdditionalHeaderHeightForPreferredBounds](#getAdditionalHeaderHeightForPreferredBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) headerBounds)`

`com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentHelper`
`[getAttributesCompartmentHelper](#getAttributesCompartmentHelper())()`

`protected [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView>`
`[getBaseMembersCompartmentViewStream](#getBaseMembersCompartmentViewStream())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoxBounds](#getBoxBounds())()`

`com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView`
`[getClassifierHeaderView](#getClassifierHeaderView())()`
Deprecated.
use [`getHeaderView()`](#getHeaderView())
`com.nomagic.magicdraw.uml.symbols.shapes.CompartmentHelper`
`[getCompartmentHelper](#getCompartmentHelper(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) modelElement)`

`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getDefaultDimension](#getDefaultDimension())()`

`[Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[PresentationElement](../PresentationElement.html)>`
`[getDrawComparator](#getDrawComparator())()`

`[Classifier](../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`[EncapsulatedClassifier](../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html)`
`[getEncapsulatedClassifier](#getEncapsulatedClassifier())()`

`[TypedElement](../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html)`
`[getEncapsulatedClassifierProvider](#getEncapsulatedClassifierProvider())()`

`com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView`
`[getHeaderView](#getHeaderView())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMembersDisplayMode](#getMembersDisplayMode())()`
Gets members display mode.
`com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentHelper`
`[getOperationsCompartmentHelper](#getOperationsCompartmentHelper())()`

`protected [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](../PresentationElement.html)>`
`[getProxyPresentationElementsStream](#getProxyPresentationElementsStream())()`

`com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentHelper`
`[getStructureCompartmentHelper](#getStructureCompartmentHelper())()`

`com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView`
`[getStructureCompartmentView](#getStructureCompartmentView())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTaggedValuesDisplayMode](#getTaggedValuesDisplayMode())()`

`[Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html)`
`[getTemplateSignatureExtent](#getTemplateSignatureExtent(boolean))(boolean calculatePrefSize)`

`com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView`
`[getTemplateSignatureView](#getTemplateSignatureView())()`

`void`
`[initialize](#initialize())()`
Initialize symbol and its children state.
`void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`protected com.nomagic.ui.UnmodifiableInsets`
`[internalGetHeaderInsets](#internalGetHeaderInsets())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement>`
`[internalGetModelElementsForRelationshipConnecting](#internalGetModelElementsForRelationshipConnecting())()`
Returns all possible element that can be used for some relationship connecting.
`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[internalGetModelElementToConnectRelationship](#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean))(com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)`
Returns element that should be used for given relationship connecting.
`protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[internalGetSelfManipulationPreferredSize](#internalGetSelfManipulationPreferredSize())()`

`boolean`
`[internalIsSuitableToConnectRelationship](#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd))(com.dassault_systemes.modeler.foundation.model.RelationshipEnd<?> end)`

`void`
`[internalLayoutChildren](#internalLayoutChildren(boolean))(boolean calculatePrefSize)`

`void`
`[internalSilentApply](#internalSilentApply())()`
Silently applies all properties after initialization
`protected void`
`[internalSpecificUpdate](#internalSpecificUpdate())()`
Specific to every shape and model element update operation.
`boolean`
`[isChildLayoutable](#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) child)`
Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.
`boolean`
`[isCutMemberNames](#isCutMemberNames())()`

`boolean`
`[isShowFullType](#isShowFullType())()`
Returns show full type
`boolean`
`[isShowInherited](#isShowInherited())()`

`boolean`
`[isShowQualifiedNameInTaggedValues](#isShowQualifiedNameInTaggedValues())()`

`boolean`
`[isShowTaggedValuesStereotypes](#isShowTaggedValuesStereotypes())()`

`boolean`
`[isShowUML_2_0_Notation](#isShowUML_2_0_Notation())()`

`boolean`
`[isSuppressAttributes](#isSuppressAttributes())()`

`boolean`
`[isSuppressed](#isSuppressed(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) modelElement)`

`boolean`
`[isSuppressMethods](#isSuppressMethods())()`

`boolean`
`[isSuppressStructure](#isSuppressStructure())()`

`boolean`
`[isTemplateSignatureVisible](#isTemplateSignatureVisible())()`

`boolean`
`[isUseAdvancedColoring](#isUseAdvancedColoring())()`
Returns use advanced coloring flag value
`protected void`
`[preferredSizeIgnoringOrientation](#preferredSizeIgnoringOrientation(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`boolean`
`[removeConnectedPathElement](#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) link)`
Removes path element.
`void`
`[removePresentationElement](#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean))([PresentationElement](../PresentationElement.html) element,
 boolean resizeParent)`
Removes object view from container.
`protected void`
`[reshapeToPreferred](#reshapeToPreferred())()`

`void`
`[sAddPresentationElement](#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))([PresentationElement](../PresentationElement.html) element,
 int index)`
Add given child to this symbol at given index
`protected void`
`[selfSpecificHeaderShapeDraw](#selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`void`
`[setCutMemberNames](#setCutMemberNames(boolean))(boolean cut)`

`void`
`[setMembersDisplayMode](#setMembersDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) membersDisplayMode)`
Sets members display mode.
`void`
`[setShowFullType](#setShowFullType(boolean))(boolean show)`
Sets show full type for members
`void`
`[setShowInherited](#setShowInherited(boolean))(boolean showInherited)`
Show inherited members in compartments
`void`
`[setShowQualifiedNameInTaggedValues](#setShowQualifiedNameInTaggedValues(boolean))(boolean show)`

`void`
`[setShowTaggedValuesStereotypes](#setShowTaggedValuesStereotypes(boolean))(boolean show)`

`void`
`[setShowUML_2_0_Notation](#setShowUML_2_0_Notation(boolean))(boolean show)`

`void`
`[setTaggedValuesDisplayMode](#setTaggedValuesDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[setUseAdvancedColoring](#setUseAdvancedColoring(boolean))(boolean use)`
Sets use advanced coloring
`void`
`[sRemovePresentationElement](#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) element)`
Removes given child
`void`
`[sSetCutMemberNames](#sSetCutMemberNames(boolean))(boolean cut)`

`void`
`[sSetMembersDisplayMode](#sSetMembersDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) membersDisplayMode)`
Sets members display mode.
`void`
`[sSetShowFullType](#sSetShowFullType(boolean))(boolean show)`
Sets show full type for members
`void`
`[sSetShowInherited](#sSetShowInherited(boolean))(boolean showInherited)`
Show inherited members in compartments
`void`
`[sSetShowQualifiedNameInTaggedValues](#sSetShowQualifiedNameInTaggedValues(boolean))(boolean show)`

`void`
`[sSetShowTaggedValuesStereotypes](#sSetShowTaggedValuesStereotypes(boolean))(boolean show)`

`void`
`[sSetShowUML_2_0_Notation](#sSetShowUML_2_0_Notation(boolean))(boolean b)`

`void`
`[sSetTaggedValuesDisplayMode](#sSetTaggedValuesDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[sSetUseAdvancedColoring](#sSetUseAdvancedColoring(boolean))(boolean use)`
Sets use advanced coloring
`void`
`[updateChildrenVisibility](#updateChildrenVisibility())()`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
`canSuppressContent, getBooleanCompartmentPropertyValue, getConstraintAndTaggedValueAlignment, getConstraintTextMode, getDefaultElementStereotypeToHeader, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesCompartmentView, getMiddlePointByIcon, getQNameDisplayMode, getSecondaryImageAndStereotypeDisplayMode, getStereotypeLabel, getStereotypesDisplayMode, internalBeforeUpdate, isShowDerivedSign, isShowElementProperties, isShowIcon, isShowNumberTagName, isShowRakeIcon, isShowRakeSymbol, isShowTaggedValues, isShowType, propertyChange, recursiveAutosize, setConstraintAndTaggedValueAlignment, setConstraints, setConstraintTextMode, setDSLStereotypesDisplayMode, setElementNumberDisplayMode, setQNameDisplayMode, setSecondaryImageAndStereotypeDisplayMode, setShowConstraints, setShowDerivedSign, setShowElementProperties, setShowIcon, setShowNumberTagName, setShowTaggedValues, setShowType, setStereotype, setStereotypesDisplayMode, setTaggedValues, sSetConstraintAndTaggedValueAlignment, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElement, sSetElementNumberDisplayMode, sSetQNameDisplayMode, sSetSecondaryImageAndStereotypeDisplayMode, sSetShowConstraints, sSetShowDerivedSign, sSetShowElementProperties, sSetShowIcon, sSetShowNumberTagName, sSetShowTaggedValues, sSetShowType, sSetStereotypesDisplayMode, updateBorderVisibility, updateName`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView
`addCompartment, addCompartment, applyCompartmentsStyle, areBoxCompartmentsSuppressed, askDeleteDataConfirmation, asPresentationElement, autosizeShapesOnEdge, canChangeParent, canHideBorder, childrenBoundsForReshape, createCompartmentElements, doInternalLayoutAdditionCompartment, doInternalLayoutChildren, getAdditionalCompartment, getAdditionalCompartmentContainer, getAdditionalCompartmentDescriptor, getAdditionalCompartmentToLayout, getAdditionalRenderersToNotifyOnPropertiesChange, getChildrenBoundsForPreferredBounds, getChildrenInsets, getCollections, getCompartmentByID, getCompartmentIDs, getCompartments, getCompartmentsIDs, getCompartmentStyleDelegate, getConfiguredPreferredSizeForAutosize, getHeaderMaxYForShrinkableShape, getHeaderVerticalPositionForLayout, getLastHeaderShapeElementBottom, getMainCompartmentContainer, getName, getPreferredDimensionForAutosize, hasManipulatedChildrenIncludingIndirect, hasSharedModelElement, internalAddIndirectManipulatedChildrenRect, internalGetIndirectManipulatedChildrenRect, internalPostSpecificUpdate, internalSetCollections, isBorderVisible, isChildMovable, isMakePreferredSizeAfterPropertiesChange, isWrapEnabled, iterateCompartmentDelegates, makePreferredSizeAfterPropertiesChange, makePreferredSizeAfterPropertiesChange, onChildEdgeChange, paintSelf, removeCompartment, removeCompartment, setCollections, setCompartmentSuppressed, setHeaderObject, setMakePreferredSizeAfterPropertiesChange, setReshapeMode, setVisibleElements, setWrapEnabled, sSetCompartmentSuppressed, sSetName, sSetWrapEnabled, updateCompartmentsVisibility`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
`addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, coversPoint, editName, getHeaderBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderObject, getHeaderVerticalPosition, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalPostUpdatePresentationElement, internalPreSpecificUpdate, internalUpdatePresentationElement, invalidate, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, minimumSizeIgnoringOrientation, paintChildren, preferredDimension, setHeaderVerticalPosition, setName, setTextEditable, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canMoveChildOutside, checkShowsProxy, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAppendChildRect, internalGetChildAt, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, removePresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[addBreakPoints](ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [adjustBounds](ShapeElement.html#adjustBounds(java.awt.Rectangle)), [adjustOnEdge](ShapeElement.html#adjustOnEdge()), [adjustOnEdge](ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)), [adjustOnEdgeChildren](ShapeElement.html#adjustOnEdgeChildren()), [autosize](ShapeElement.html#autosize()), [calculateAdjustOnEdgeLocation](ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)), [calculateAndGetMinimumShrinkingDimension](ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)), [calculateAndGetPreferredDimension](ShapeElement.html#calculateAndGetPreferredDimension()), [calculateEdge](ShapeElement.html#calculateEdge()), [calculateMinimumDimension](ShapeElement.html#calculateMinimumDimension()), [calculateOnEdgeBounds](ShapeElement.html#calculateOnEdgeBounds()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension(int,int)), [canBeAutosized](ShapeElement.html#canBeAutosized()), [canHavePaths](ShapeElement.html#canHavePaths()), [clearOldRect](ShapeElement.html#clearOldRect()), [edgeChanged](ShapeElement.html#edgeChanged()), [ensureDimension](ShapeElement.html#ensureDimension(boolean)), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable()), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)), [findFreePlaceForShapeOnBorder](ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)), [getBorderElementMargin](ShapeElement.html#getBorderElementMargin()), [getBounds](ShapeElement.html#getBounds()), [getCenterlineableInnerParts](ShapeElement.html#getCenterlineableInnerParts(int)), [getDimensionForShrinking](ShapeElement.html#getDimensionForShrinking(int,int)), [getEdgeLine](ShapeElement.html#getEdgeLine(int)), [getFixedConnectionPoints](ShapeElement.html#getFixedConnectionPoints()), [getHeaderInsetReduce](ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)), [getInsetsForOnEdgeShapes](ShapeElement.html#getInsetsForOnEdgeShapes()), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)), [getIntersection](ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLoadedDimension](ShapeElement.html#getLoadedDimension()), [getMiddlePoint](ShapeElement.html#getMiddlePoint()), [getMiddlePoint](ShapeElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](ShapeElement.html#getMiddlePointX()), [getMiddlePointX](ShapeElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](ShapeElement.html#getMiddlePointY()), [getMiddlePointY](ShapeElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](ShapeElement.html#getMinimumDimension()), [getNearestEdge](ShapeElement.html#getNearestEdge(int,int)), [getNearestEdge](ShapeElement.html#getNearestEdge(java.awt.Rectangle)), [getNeedAutosizeFlag](ShapeElement.html#getNeedAutosizeFlag()), [getNotCopyBounds](ShapeElement.html#getNotCopyBounds()), [getOnEdge](ShapeElement.html#getOnEdge()), [getOnEdgeCornerDistance](ShapeElement.html#getOnEdgeCornerDistance()), [getOnEdgePosition](ShapeElement.html#getOnEdgePosition()), [getPreferredDimension](ShapeElement.html#getPreferredDimension()), [getReshapeMode](ShapeElement.html#getReshapeMode()), [getSizeForDrawing](ShapeElement.html#getSizeForDrawing()), [getSuspendShapeAutoResizeMode](ShapeElement.html#getSuspendShapeAutoResizeMode()), [hasManipulator](ShapeElement.html#hasManipulator()), [internalGetBoundsShape](ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [intersects](ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [isAutosized](ShapeElement.html#isAutosized()), [isCenterlineInner](ShapeElement.html#isCenterlineInner()), [isHorizontalCenterlineProvider](ShapeElement.html#isHorizontalCenterlineProvider()), [isOnEdge](ShapeElement.html#isOnEdge()), [isShapeOnEdge](ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isShrinkable](ShapeElement.html#isShrinkable()), [isSnapShapesOnBorderToGrid](ShapeElement.html#isSnapShapesOnBorderToGrid()), [isSnapToGrid](ShapeElement.html#isSnapToGrid()), [isUseFixedConnectionPoints](ShapeElement.html#isUseFixedConnectionPoints()), [isVerticalCenterlineProvider](ShapeElement.html#isVerticalCenterlineProvider()), [layoutChildren](ShapeElement.html#layoutChildren()), [maximumDimension](ShapeElement.html#maximumDimension(java.awt.Dimension)), [minimumOrMinimumShrinkableDimension](ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)), [moveLinksToSelf](ShapeElement.html#moveLinksToSelf()), [movePathElement](ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)), [movePathElements](ShapeElement.html#movePathElements()), [needAdjustToMaximumDimension](ShapeElement.html#needAdjustToMaximumDimension()), [prepareForShadowDrawing](ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [providesHorizontalCenterline](ShapeElement.html#providesHorizontalCenterline()), [providesVerticalCenterline](ShapeElement.html#providesVerticalCenterline()), [resetCalculatePreferredRegardingChildren](ShapeElement.html#resetCalculatePreferredRegardingChildren()), [setAutosize](ShapeElement.html#setAutosize(boolean)), [setBorderElementMargin](ShapeElement.html#setBorderElementMargin(java.lang.String)), [setCalculatePreferredRegardingChildren](ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)), [setLoadedDimension](ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)), [setMinimumDimension](ShapeElement.html#setMinimumDimension(int,int)), [setNeedAutosizeFlag](ShapeElement.html#setNeedAutosizeFlag(byte)), [setOldRect](ShapeElement.html#setOldRect(java.awt.Rectangle)), [setOnEdge](ShapeElement.html#setOnEdge(int)), [setPreferredDimension](ShapeElement.html#setPreferredDimension(int,int)), [setSnapShapesOnBorderToGrid](ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)), [setSuspendShapeAutoResizeMode](ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)), [setUseFixedConnectionPoints](ShapeElement.html#setUseFixedConnectionPoints(boolean)), [shouldDrawShadow](ShapeElement.html#shouldDrawShadow()), [simpleSetBounds](ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)), [simpleSetBounds](ShapeElement.html#simpleSetBounds(java.awt.Rectangle)), [snapsToCenterlines](ShapeElement.html#snapsToCenterlines()), [sSetBorderElementMargin](ShapeElement.html#sSetBorderElementMargin(java.lang.String)), [sSetBounds](ShapeElement.html#sSetBounds(java.awt.Rectangle)), [sSetSuspendShapeAutoResizeMode](ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)), [sSetVisibility](ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [toString](ShapeElement.html#toString()), [updateLater](ShapeElement.html#updateLater())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[disposeConnectedPaths](../paths/PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](../paths/PathConnector.html#getPreferredArrowLength()), [isShowsProxy](../paths/PathConnector.html#isShowsProxy()), [movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [sAddConnectedPathElement](../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](../paths/PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](../PresentationElement.html#mustShowContextMenu()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [resizeParent](../PresentationElement.html#resizeParent()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties()), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape
`getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.uml.CompartmentSupport
`setVisibleElements`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, asPresentationElement, getProperty, getPropertyManager`

============ FIELD DETAIL =========== 
Field Details
ALL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ALL
Members display options - display all members.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.ALL)
ONLY_PUBLIC
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ONLY_PUBLIC
Members display options - display only public members.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.ONLY_PUBLIC)
NOT_PRIVATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NOT_PRIVATE
Members display options - not private members.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.NOT_PRIVATE)
MEMBERS_DISPLAY_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) MEMBERS_DISPLAY_MODES
List of available members display options.
See Also:
[`ALL`](#ALL)
[`ONLY_PUBLIC`](#ONLY_PUBLIC)
[`NOT_PRIVATE`](#NOT_PRIVATE)
WITHOUT_ASSOCIATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) WITHOUT_ASSOCIATION
Association ends display options - display association end if association symbol is not drawn in the diagram.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.WITHOUT_ASSOCIATION)
ASSOCIATION_ENDS_DISPLAY_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) ASSOCIATION_ENDS_DISPLAY_MODES
List of available association ends display in attribute compartment mode.
See Also:
[`ALL`](#ALL)
[`WITHOUT_ASSOCIATION`](#WITHOUT_ASSOCIATION)
`TaggedValuesDisplayModeOwner.DO_NOT_DISPLAY`
DEFAULT_SIZE
public static final [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) DEFAULT_SIZE
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ClassifierView
public ClassifierView()
ClassifierView
public ClassifierView(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
ClassifierView
protected ClassifierView(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent,
 com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView header,
 boolean canDisplayStructure)
 ============ METHOD DETAIL ========== 
Method Details
getDefaultDimension
public [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getDefaultDimension()
Overrides:
`[getDefaultDimension](ShapeElement.html#getDefaultDimension())` in class `[ShapeElement](ShapeElement.html)`
getTemplateSignatureView
public com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView getTemplateSignatureView()
Returns:
TemplateSignatureView symbol
getStructureCompartmentView
public com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView getStructureCompartmentView()
Returns:
StructureCompartment symbol
sSetShowFullType
public void sSetShowFullType(boolean show)
Sets show full type for members
Parameters:
`show` - show full type
setShowFullType
public void setShowFullType(boolean show)
Sets show full type for members
Parameters:
`show` - show full type
isShowFullType
public boolean isShowFullType()
Returns show full type
Returns:
show full type
sSetUseAdvancedColoring
public void sSetUseAdvancedColoring(boolean use)
Sets use advanced coloring
Parameters:
`use` - use advanced coloring flag
setUseAdvancedColoring
public void setUseAdvancedColoring(boolean use)
Sets use advanced coloring
Parameters:
`use` - use advanced coloring flag
isUseAdvancedColoring
public boolean isUseAdvancedColoring()
Returns use advanced coloring flag value
Returns:
advanced coloring value
clone
public [ClassifierView](ClassifierView.html) clone()
Specified by:
`[clone](../../BaseElement.html#clone())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`clone` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
preferredSizeIgnoringOrientation
protected void preferredSizeIgnoringOrientation([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
Overrides:
`preferredSizeIgnoringOrientation` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
internalLayoutChildren
public void internalLayoutChildren(boolean calculatePrefSize)
Overrides:
`internalLayoutChildren` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
getTemplateSignatureExtent
@CheckForNullpublic [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) getTemplateSignatureExtent(boolean calculatePrefSize)
getAdditionalHeaderHeightForPreferredBounds
protected int getAdditionalHeaderHeightForPreferredBounds(@CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) headerBounds)
Overrides:
`getAdditionalHeaderHeightForPreferredBounds` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
createStateForUpdateOperation
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> createStateForUpdateOperation()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Create collection of any properties used to distinguish during shape update if movePathElements should be called
Overrides:
`createStateForUpdateOperation` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Returns:
state
internalSpecificUpdate
protected void internalSpecificUpdate()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Specific to every shape and model element update operation. Must be overridden in subclasses if you need to do specific tasks.
 !!! Important - all resizing, paths moving and so on is done in updatePresentationElement and should not be done in specific update.
Overrides:
`internalSpecificUpdate` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
See Also:
`AbstractHeaderShapeView.internalUpdatePresentationElement()`
atInsert
public void atInsert()
Description copied from class: `[PresentationElement](../PresentationElement.html#atInsert())`
Invalidates object at insert
Specified by:
`[atInsert](../../BaseElement.html#atInsert())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`atInsert` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
dispose
public void dispose()
Description copied from class: `[PresentationElement](../PresentationElement.html#dispose())`
disposes ends of links when link is deleted
Specified by:
`[dispose](../../BaseElement.html#dispose())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`dispose` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
updateChildrenVisibility
public void updateChildrenVisibility()
Overrides:
`updateChildrenVisibility` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
isSuppressAttributes
public boolean isSuppressAttributes()
isSuppressMethods
public boolean isSuppressMethods()
isSuppressed
public boolean isSuppressed([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) modelElement)
isSuppressStructure
public boolean isSuppressStructure()
accept
public void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
initialize
public void initialize()
Description copied from class: `[PresentationElement](../PresentationElement.html#initialize())`
Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.
Overrides:
`[initialize](ShapeElement.html#initialize())` in class `[ShapeElement](ShapeElement.html)`
canAddInstance
public boolean canAddInstance([PresentationElement](../PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Object view has no children.
Overrides:
`canAddInstance` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
canAddChild
public boolean canAddChild([PresentationElement](../PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Check of given symbol can be added as child into this symbol.
Overrides:
`canAddChild` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Parameters:
`symbol` - symbol
Returns:
true if symbol can be added
canStereotypeIconGrow
public boolean canStereotypeIconGrow()
Returns:
true if stereotype icon forces shape growing into all directions on resize
createBoundsShape
public [ContainerShape](../../../../awt/ContainerShape.html) createBoundsShape([PathElement](../paths/PathElement.html) path,
 [BoundsTransformation](../BoundsTransformation.html) transformation)
Description copied from class: `[ShapeElement](ShapeElement.html#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))`
Creates bounding shape for intersection calculation.
Overrides:
`createBoundsShape` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Parameters:
`path` - path
`transformation` - transformation
Returns:
shape
addPresentationElement
public void addPresentationElement([PresentationElement](../PresentationElement.html) element,
 int index,
 boolean resize)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
If a specified object not inserted in this container then adds a new object view to the container.
Overrides:
`addPresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Parameters:
`element` - new PresentationElement object
`index` - index to add at
`resize` - resize parent
sAddPresentationElement
public void sAddPresentationElement([PresentationElement](../PresentationElement.html) element,
 int index)
Description copied from class: `[PresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))`
Add given child to this symbol at given index
Overrides:
`sAddPresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`element` - child to add
`index` - index to add at. Can be -1
removePresentationElement
public void removePresentationElement([PresentationElement](../PresentationElement.html) element,
 boolean resizeParent)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Removes object view from container.
Overrides:
`removePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Parameters:
`element` - object to remove
`resizeParent` - resize parent
sRemovePresentationElement
public void sRemovePresentationElement([PresentationElement](../PresentationElement.html) element)
Description copied from class: `[PresentationElement](../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Removes given child
Overrides:
`sRemovePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`element` - child
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Description copied from class: `[PresentationElement](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))`
Applies properties from given property manager
Overrides:
`internalApplyProperties` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
Parameters:
`changer` - new properties
internalSilentApply
public void internalSilentApply()
Description copied from class: `[PresentationElement](../PresentationElement.html#internalSilentApply())`
Silently applies all properties after initialization
Overrides:
`internalSilentApply` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
sSetTaggedValuesDisplayMode
public void sSetTaggedValuesDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Specified by:
`sSetTaggedValuesDisplayMode` in interface `com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner`
setTaggedValuesDisplayMode
public void setTaggedValuesDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Specified by:
`setTaggedValuesDisplayMode` in interface `com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner`
isShowTaggedValuesStereotypes
public boolean isShowTaggedValuesStereotypes()
sSetShowTaggedValuesStereotypes
public void sSetShowTaggedValuesStereotypes(boolean show)
setShowTaggedValuesStereotypes
public void setShowTaggedValuesStereotypes(boolean show)
isShowQualifiedNameInTaggedValues
public boolean isShowQualifiedNameInTaggedValues()
sSetShowQualifiedNameInTaggedValues
public void sSetShowQualifiedNameInTaggedValues(boolean show)
setShowQualifiedNameInTaggedValues
public void setShowQualifiedNameInTaggedValues(boolean show)
setCutMemberNames
public void setCutMemberNames(boolean cut)
sSetCutMemberNames
public void sSetCutMemberNames(boolean cut)
isCutMemberNames
public boolean isCutMemberNames()
getTaggedValuesDisplayMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTaggedValuesDisplayMode()
Specified by:
`getTaggedValuesDisplayMode` in interface `com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner`
getDrawComparator
public [Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[PresentationElement](../PresentationElement.html)> getDrawComparator()
Overrides:
`[getDrawComparator](../PresentationElement.html#getDrawComparator())` in class `[PresentationElement](../PresentationElement.html)`
sSetShowUML_2_0_Notation
public void sSetShowUML_2_0_Notation(boolean b)
isShowUML_2_0_Notation
public boolean isShowUML_2_0_Notation()
addConnectedPathElement
public boolean addConnectedPathElement([PathElement](../paths/PathElement.html) element)
Description copied from class: `[PathConnector](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))`
Adds a new path element, and recalculates its position.
Overrides:
`[addConnectedPathElement](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))` in class `[PathConnector](../paths/PathConnector.html)`
Parameters:
`element` - element to be added.
Returns:
true if an element was added
reshapeToPreferred
protected void reshapeToPreferred()
removeConnectedPathElement
public boolean removeConnectedPathElement([PathElement](../paths/PathElement.html) link)
Description copied from class: `[PathConnector](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))`
Removes path element.
Overrides:
`[removeConnectedPathElement](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))` in class `[PathConnector](../paths/PathConnector.html)`
Parameters:
`link` - element to remove.
Returns:
true if an element was removed
setShowUML_2_0_Notation
public void setShowUML_2_0_Notation(boolean show)
isTemplateSignatureVisible
public boolean isTemplateSignatureVisible()
getAttributesCompartmentHelper
public com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentHelper getAttributesCompartmentHelper()
getOperationsCompartmentHelper
public com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentHelper getOperationsCompartmentHelper()
getCompartmentHelper
public com.nomagic.magicdraw.uml.symbols.shapes.CompartmentHelper getCompartmentHelper([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) modelElement)
getStructureCompartmentHelper
public com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentHelper getStructureCompartmentHelper()
internalGetModelElementToConnectRelationship
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement internalGetModelElementToConnectRelationship(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)
Description copied from class: `[PresentationElement](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean))`
Returns element that should be used for given relationship connecting.
 All possible elements are returned by method [`PresentationElement.getModelElementsForRelationshipConnecting()`](../PresentationElement.html#getModelElementsForRelationshipConnecting()).
Overrides:
`[internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean))` in class `[PresentationElement](../PresentationElement.html)`
Returns:
all possible elements
See Also:
[`PresentationElement.getModelElementsForRelationshipConnecting()`](../PresentationElement.html#getModelElementsForRelationshipConnecting())
internalIsSuitableToConnectRelationship
public boolean internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd<?> end)
Overrides:
`[internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd))` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if given possible elements (end of relationship) is suitable to connect given relationship to this symbol
internalGetModelElementsForRelationshipConnecting
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement> internalGetModelElementsForRelationshipConnecting()
Description copied from class: `[PresentationElement](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting())`
Returns all possible element that can be used for some relationship connecting.
Overrides:
`[internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
all possible elements
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`createSmartListenerConfig` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
internalGetHeaderInsets
protected com.nomagic.ui.UnmodifiableInsets internalGetHeaderInsets()
Overrides:
`internalGetHeaderInsets` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
getAdditionalCompartmentInsets
protected com.nomagic.ui.UnmodifiableInsets getAdditionalCompartmentInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel level)
Overrides:
`getAdditionalCompartmentInsets` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
getProxyPresentationElementsStream
protected [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](../PresentationElement.html)> getProxyPresentationElementsStream()
Overrides:
`getProxyPresentationElementsStream` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
internalGetSelfManipulationPreferredSize
protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) internalGetSelfManipulationPreferredSize()
Overrides:
`internalGetSelfManipulationPreferredSize` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Returns:
size for manipulation which does not take into account the size of children on some specific conditions (for example, in case if wrapped text)
getEncapsulatedClassifier
public [EncapsulatedClassifier](../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) getEncapsulatedClassifier()
Specified by:
`getEncapsulatedClassifier` in interface `com.nomagic.magicdraw.uml.symbols.shapes.PortOwner`
getEncapsulatedClassifierProvider
public [TypedElement](../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) getEncapsulatedClassifierProvider()
Specified by:
`getEncapsulatedClassifierProvider` in interface `com.nomagic.magicdraw.uml.symbols.shapes.PortOwner`
getBoxBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoxBounds()
selfSpecificHeaderShapeDraw
protected void selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Overrides:
`selfSpecificHeaderShapeDraw` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
drawShadow
protected void drawShadow([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g)
getMembersDisplayMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMembersDisplayMode()
Gets members display mode.
Returns:
mode
See Also:
[`setMembersDisplayMode(String)`](#setMembersDisplayMode(java.lang.String))
[`ALL`](#ALL)
[`NOT_PRIVATE`](#NOT_PRIVATE)
[`ONLY_PUBLIC`](#ONLY_PUBLIC)
sSetMembersDisplayMode
public void sSetMembersDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) membersDisplayMode)
Sets members display mode. Does not update classifier symbol.
Parameters:
`membersDisplayMode` - display mode
See Also:
[`setMembersDisplayMode(String)`](#setMembersDisplayMode(java.lang.String))
[`ALL`](#ALL)
[`NOT_PRIVATE`](#NOT_PRIVATE)
[`ONLY_PUBLIC`](#ONLY_PUBLIC)
setMembersDisplayMode
public void setMembersDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) membersDisplayMode)
Sets members display mode.
Parameters:
`membersDisplayMode` - display mode
See Also:
[`setMembersDisplayMode(String)`](#setMembersDisplayMode(java.lang.String))
[`ALL`](#ALL)
[`NOT_PRIVATE`](#NOT_PRIVATE)
[`ONLY_PUBLIC`](#ONLY_PUBLIC)
isShowInherited
public boolean isShowInherited()
Returns:
true if inherited members are shown in compartments
sSetShowInherited
public void sSetShowInherited(boolean showInherited)
Show inherited members in compartments
Parameters:
`showInherited` - show
setShowInherited
public void setShowInherited(boolean showInherited)
Show inherited members in compartments
Parameters:
`showInherited` - show
isChildLayoutable
public boolean isChildLayoutable([PresentationElement](../PresentationElement.html) child)
Description copied from class: `[ShapeElement](ShapeElement.html#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.
 Not "layoutable" children are just moved together with parents, but layoutChildren() do not control their location.
Overrides:
`isChildLayoutable` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
Parameters:
`child` - child
Returns:
true, if given child is layed-out inside autosize method of this shape. False here
getElement
public [Classifier](../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) getElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#getElement())`
Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.
Specified by:
`[getElement](../../ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../../ModelElementProvider.html)`
Overrides:
`[getElement](../PresentationElement.html#getElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
model element of this presentation element.
getBaseMembersCompartmentViewStream
protected [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView> getBaseMembersCompartmentViewStream()
getHeaderView
public com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView getHeaderView()
Overrides:
`getHeaderView` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
getClassifierHeaderView
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView getClassifierHeaderView()
Deprecated.
use [`getHeaderView()`](#getHeaderView())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class ClassifierView">Class ClassifierView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code>com.nomagic.magicdraw.uml.CompartmentSupport</code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.CompartmentContainer</code>, <code>com.nomagic.magicdraw.uml.symbols.CompartmentOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.PortOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner</code>, <code><a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code>com.nomagic.magicdraw.uml.symbols.Wrapable</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ActorView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActorView</a></code>, <code><a href="ArtifactView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ArtifactView</a></code>, <code><a href="ClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassView</a></code>, <code><a href="DataTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DataTypeView</a></code>, <code><a href="EnumerationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">EnumerationView</a></code>, <code><a href="InformationItemView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InformationItemView</a></code>, <code><a href="InterfaceView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">InterfaceView</a></code>, <code><a href="PrimitiveTypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PrimitiveTypeView</a></code>, <code><a href="SignalView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SignalView</a></code>, <code><a href="StereotypeView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StereotypeView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ClassifierView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
implements com.nomagic.magicdraw.uml.symbols.shapes.PortOwner, com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner</span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALL">ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Members display options - display all members.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASSOCIATION_ENDS_DISPLAY_MODES">ASSOCIATION_ENDS_DISPLAY_MODES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of available association ends display in attribute compartment mode.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_SIZE">DEFAULT_SIZE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MEMBERS_DISPLAY_MODES">MEMBERS_DISPLAY_MODES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of available members display options.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NOT_PRIVATE">NOT_PRIVATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Members display options - not private members.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ONLY_PUBLIC">ONLY_PUBLIC</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Members display options - display only public members.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WITHOUT_ASSOCIATION">WITHOUT_ASSOCIATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Association ends display options - display association end if association symbol is not drawn in the diagram.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</h3>
<code>SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_IMAGE_AND_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODES</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL">BORDER_ELEMENT_MARGIN_ALL</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM">BORDER_ELEMENT_MARGIN_BOTTOM</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT">BORDER_ELEMENT_MARGIN_LEFT</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT">BORDER_ELEMENT_MARGIN_LEFT_RIGHT</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES">BORDER_ELEMENT_MARGIN_MODES</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE">BORDER_ELEMENT_MARGIN_NONE</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT">BORDER_ELEMENT_MARGIN_RIGHT</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP">BORDER_ELEMENT_MARGIN_TOP</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM">BORDER_ELEMENT_MARGIN_TOP_BOTTOM</a>, <a href="ShapeElement.html#BOTTOM_EDGE">BOTTOM_EDGE</a>, <a href="ShapeElement.html#INSIDE_EDGE_POSITION">INSIDE_EDGE_POSITION</a>, <a href="ShapeElement.html#LEFT_EDGE">LEFT_EDGE</a>, <a href="ShapeElement.html#NEED_AUTOSIZE_FULL">NEED_AUTOSIZE_FULL</a>, <a href="ShapeElement.html#NEED_AUTOSIZE_LAYOUT">NEED_AUTOSIZE_LAYOUT</a>, <a href="ShapeElement.html#NEED_AUTOSIZE_NONE">NEED_AUTOSIZE_NONE</a>, <a href="ShapeElement.html#NO_EDGE">NO_EDGE</a>, <a href="ShapeElement.html#NULL_INSETS">NULL_INSETS</a>, <a href="ShapeElement.html#ON_EDGE_POSITION">ON_EDGE_POSITION</a>, <a href="ShapeElement.html#OUTSIDE_EDGE_POSITION">OUTSIDE_EDGE_POSITION</a>, <a href="ShapeElement.html#RIGHT_EDGE">RIGHT_EDGE</a>, <a href="ShapeElement.html#SPACE">SPACE</a>, <a href="ShapeElement.html#SPACE_INSETS">SPACE_INSETS</a>, <a href="ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM">SPACE_INSETS_EMPTY_TOP_BOTTOM</a>, <a href="ShapeElement.html#TOP_EDGE">TOP_EDGE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#showsProxy">showsProxy</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DEFAULT_LINE_WIDTH">DEFAULT_LINE_WIDTH</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#HANDLE_SIZE">HANDLE_SIZE</a>, <a href="../PresentationElement.html#MAX_LINE_WIDTH">MAX_LINE_WIDTH</a>, <a href="../PresentationElement.html#MIN_LINE_WIDTH">MIN_LINE_WIDTH</a>, <a href="../PresentationElement.html#peStyle">peStyle</a>, <a href="../PresentationElement.html#SHADOW_WIDTH">SHADOW_WIDTH</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner</h3>
<code>QNAME_DISPLAY_MODE_ABOVE_NAME, QNAME_DISPLAY_MODE_BELOW_NAME, QNAME_DISPLAY_MODE_DO_NOT_DISPLAY, QNAME_DISPLAY_MODE_MERGE_WITH_NAME, QNAME_DISPLAY_MODES</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.StereotypesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.<a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></h3>
<code><a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL">DSL_STEREOTYPE_DISPLAY_MODE_ALL</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST">DSL_STEREOTYPE_DISPLAY_MODE_LAST</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE">DSL_STEREOTYPE_DISPLAY_MODE_NONE</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES">DSL_STEREOTYPE_DISPLAY_MODES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES">STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON">STEREOTYPE_DISPLAY_MODE_ICON</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT">STEREOTYPE_DISPLAY_MODE_TEXT</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON">STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES">STEREOTYPES_DISPLAY_MODES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE">STEREOTYPES_DISPLAY_MODES_SIMPLE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner</h3>
<code>DO_NOT_DISPLAY, IN_COMPARTMENT, ON_SHAPE, TAGGED_VALUES_DISPLAY_MODES</code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code> </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ClassifierView</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code> </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">ClassifierView</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView,boolean)">ClassifierView</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView header,
 boolean canDisplayStructure)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new path element, and recalculates its position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean)">addPresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index,
 boolean resize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If a specified object not inserted in this container then adds a new object view to the container.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates object at insert</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check of given symbol can be added as child into this symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Object view has no children.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canStereotypeIconGrow()">canStereotypeIconGrow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ClassifierView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassifierView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">createBoundsShape</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates bounding shape for intersection calculation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateForUpdateOperation()">createStateForUpdateOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create collection of any properties used to distinguish during shape update if movePathElements should be called</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">disposes ends of links when link is deleted</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#drawShadow(java.awt.Graphics)">drawShadow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalCompartmentInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">getAdditionalCompartmentInsets</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel level)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalHeaderHeightForPreferredBounds(java.awt.Rectangle)">getAdditionalHeaderHeightForPreferredBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> headerBounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttributesCompartmentHelper()">getAttributesCompartmentHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseMembersCompartmentViewStream()">getBaseMembersCompartmentViewStream</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoxBounds()">getBoxBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getClassifierHeaderView()">getClassifierHeaderView</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getHeaderView()"><code>getHeaderView()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.CompartmentHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompartmentHelper(java.lang.Class)">getCompartmentHelper</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> modelElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultDimension()">getDefaultDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawComparator()">getDrawComparator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEncapsulatedClassifier()">getEncapsulatedClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEncapsulatedClassifierProvider()">getEncapsulatedClassifierProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeaderView()">getHeaderView</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMembersDisplayMode()">getMembersDisplayMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets members display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationsCompartmentHelper()">getOperationsCompartmentHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProxyPresentationElementsStream()">getProxyPresentationElementsStream</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStructureCompartmentHelper()">getStructureCompartmentHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStructureCompartmentView()">getStructureCompartmentView</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValuesDisplayMode()">getTaggedValuesDisplayMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateSignatureExtent(boolean)">getTemplateSignatureExtent</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateSignatureView()">getTemplateSignatureView</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize symbol and its children state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetHeaderInsets()">internalGetHeaderInsets</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all possible element that can be used for some relationship connecting.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns element that should be used for given relationship connecting.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetSelfManipulationPreferredSize()">internalGetSelfManipulationPreferredSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a><wbr/>(com.dassault_systemes.modeler.foundation.model.RelationshipEnd&lt;?&gt; end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalLayoutChildren(boolean)">internalLayoutChildren</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSilentApply()">internalSilentApply</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSpecificUpdate()">internalSpecificUpdate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specific to every shape and model element update operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildLayoutable</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCutMemberNames()">isCutMemberNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowFullType()">isShowFullType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns show full type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowInherited()">isShowInherited</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowQualifiedNameInTaggedValues()">isShowQualifiedNameInTaggedValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowTaggedValuesStereotypes()">isShowTaggedValuesStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowUML_2_0_Notation()">isShowUML_2_0_Notation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuppressAttributes()">isSuppressAttributes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuppressed(java.lang.Class)">isSuppressed</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> modelElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuppressMethods()">isSuppressMethods</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuppressStructure()">isSuppressStructure</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTemplateSignatureVisible()">isTemplateSignatureVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseAdvancedColoring()">isUseAdvancedColoring</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns use advanced coloring flag value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferredSizeIgnoringOrientation(java.awt.Dimension,int,int)">preferredSizeIgnoringOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">removePresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 boolean resizeParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes object view from container.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reshapeToPreferred()">reshapeToPreferred</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol at given index</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">selfSpecificHeaderShapeDraw</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCutMemberNames(boolean)">setCutMemberNames</a><wbr/>(boolean cut)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMembersDisplayMode(java.lang.String)">setMembersDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> membersDisplayMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets members display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowFullType(boolean)">setShowFullType</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets show full type for members</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowInherited(boolean)">setShowInherited</a><wbr/>(boolean showInherited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show inherited members in compartments</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowQualifiedNameInTaggedValues(boolean)">setShowQualifiedNameInTaggedValues</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowTaggedValuesStereotypes(boolean)">setShowTaggedValuesStereotypes</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowUML_2_0_Notation(boolean)">setShowUML_2_0_Notation</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTaggedValuesDisplayMode(java.lang.String)">setTaggedValuesDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseAdvancedColoring(boolean)">setUseAdvancedColoring</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets use advanced coloring</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given child</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetCutMemberNames(boolean)">sSetCutMemberNames</a><wbr/>(boolean cut)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetMembersDisplayMode(java.lang.String)">sSetMembersDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> membersDisplayMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets members display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowFullType(boolean)">sSetShowFullType</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets show full type for members</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowInherited(boolean)">sSetShowInherited</a><wbr/>(boolean showInherited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show inherited members in compartments</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowQualifiedNameInTaggedValues(boolean)">sSetShowQualifiedNameInTaggedValues</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowTaggedValuesStereotypes(boolean)">sSetShowTaggedValuesStereotypes</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowUML_2_0_Notation(boolean)">sSetShowUML_2_0_Notation</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetTaggedValuesDisplayMode(java.lang.String)">sSetTaggedValuesDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetUseAdvancedColoring(boolean)">sSetUseAdvancedColoring</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets use advanced coloring</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateChildrenVisibility()">updateChildrenVisibility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</h3>
<code>canSuppressContent, getBooleanCompartmentPropertyValue, getConstraintAndTaggedValueAlignment, getConstraintTextMode, getDefaultElementStereotypeToHeader, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesCompartmentView, getMiddlePointByIcon, getQNameDisplayMode, getSecondaryImageAndStereotypeDisplayMode, getStereotypeLabel, getStereotypesDisplayMode, internalBeforeUpdate, isShowDerivedSign, isShowElementProperties, isShowIcon, isShowNumberTagName, isShowRakeIcon, isShowRakeSymbol, isShowTaggedValues, isShowType, propertyChange, recursiveAutosize, setConstraintAndTaggedValueAlignment, setConstraints, setConstraintTextMode, setDSLStereotypesDisplayMode, setElementNumberDisplayMode, setQNameDisplayMode, setSecondaryImageAndStereotypeDisplayMode, setShowConstraints, setShowDerivedSign, setShowElementProperties, setShowIcon, setShowNumberTagName, setShowTaggedValues, setShowType, setStereotype, setStereotypesDisplayMode, setTaggedValues, sSetConstraintAndTaggedValueAlignment, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElement, sSetElementNumberDisplayMode, sSetQNameDisplayMode, sSetSecondaryImageAndStereotypeDisplayMode, sSetShowConstraints, sSetShowDerivedSign, sSetShowElementProperties, sSetShowIcon, sSetShowNumberTagName, sSetShowTaggedValues, sSetShowType, sSetStereotypesDisplayMode, updateBorderVisibility, updateName</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</h3>
<code>addCompartment, addCompartment, applyCompartmentsStyle, areBoxCompartmentsSuppressed, askDeleteDataConfirmation, asPresentationElement, autosizeShapesOnEdge, canChangeParent, canHideBorder, childrenBoundsForReshape, createCompartmentElements, doInternalLayoutAdditionCompartment, doInternalLayoutChildren, getAdditionalCompartment, getAdditionalCompartmentContainer, getAdditionalCompartmentDescriptor, getAdditionalCompartmentToLayout, getAdditionalRenderersToNotifyOnPropertiesChange, getChildrenBoundsForPreferredBounds, getChildrenInsets, getCollections, getCompartmentByID, getCompartmentIDs, getCompartments, getCompartmentsIDs, getCompartmentStyleDelegate, getConfiguredPreferredSizeForAutosize, getHeaderMaxYForShrinkableShape, getHeaderVerticalPositionForLayout, getLastHeaderShapeElementBottom, getMainCompartmentContainer, getName, getPreferredDimensionForAutosize, hasManipulatedChildrenIncludingIndirect, hasSharedModelElement, internalAddIndirectManipulatedChildrenRect, internalGetIndirectManipulatedChildrenRect, internalPostSpecificUpdate, internalSetCollections, isBorderVisible, isChildMovable, isMakePreferredSizeAfterPropertiesChange, isWrapEnabled, iterateCompartmentDelegates, makePreferredSizeAfterPropertiesChange, makePreferredSizeAfterPropertiesChange, onChildEdgeChange, paintSelf, removeCompartment, removeCompartment, setCollections, setCompartmentSuppressed, setHeaderObject, setMakePreferredSizeAfterPropertiesChange, setReshapeMode, setVisibleElements, setWrapEnabled, sSetCompartmentSuppressed, sSetName, sSetWrapEnabled, updateCompartmentsVisibility</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</h3>
<code>addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, coversPoint, editName, getHeaderBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderObject, getHeaderVerticalPosition, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalPostUpdatePresentationElement, internalPreSpecificUpdate, internalUpdatePresentationElement, invalidate, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, minimumSizeIgnoringOrientation, paintChildren, preferredDimension, setHeaderVerticalPosition, setName, setTextEditable, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canMoveChildOutside, checkShowsProxy, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAppendChildRect, internalGetChildAt, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, removePresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a>, <a href="ShapeElement.html#adjustBounds(java.awt.Rectangle)">adjustBounds</a>, <a href="ShapeElement.html#adjustOnEdge()">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>, <a href="ShapeElement.html#autosize()">autosize</a>, <a href="ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a>, <a href="ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a>, <a href="ShapeElement.html#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>, <a href="ShapeElement.html#calculateEdge()">calculateEdge</a>, <a href="ShapeElement.html#calculateMinimumDimension()">calculateMinimumDimension</a>, <a href="ShapeElement.html#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>, <a href="ShapeElement.html#calculatePreferredDimension()">calculatePreferredDimension</a>, <a href="ShapeElement.html#calculatePreferredDimension(int,int)">calculatePreferredDimension</a>, <a href="ShapeElement.html#canBeAutosized()">canBeAutosized</a>, <a href="ShapeElement.html#canHavePaths()">canHavePaths</a>, <a href="ShapeElement.html#clearOldRect()">clearOldRect</a>, <a href="ShapeElement.html#edgeChanged()">edgeChanged</a>, <a href="ShapeElement.html#ensureDimension(boolean)">ensureDimension</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a>, <a href="ShapeElement.html#getBorderElementMargin()">getBorderElementMargin</a>, <a href="ShapeElement.html#getBounds()">getBounds</a>, <a href="ShapeElement.html#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a>, <a href="ShapeElement.html#getDimensionForShrinking(int,int)">getDimensionForShrinking</a>, <a href="ShapeElement.html#getEdgeLine(int)">getEdgeLine</a>, <a href="ShapeElement.html#getFixedConnectionPoints()">getFixedConnectionPoints</a>, <a href="ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a>, <a href="ShapeElement.html#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getLoadedDimension()">getLoadedDimension</a>, <a href="ShapeElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="ShapeElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="ShapeElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="ShapeElement.html#getNearestEdge(int,int)">getNearestEdge</a>, <a href="ShapeElement.html#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a>, <a href="ShapeElement.html#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>, <a href="ShapeElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="ShapeElement.html#getOnEdge()">getOnEdge</a>, <a href="ShapeElement.html#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>, <a href="ShapeElement.html#getOnEdgePosition()">getOnEdgePosition</a>, <a href="ShapeElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="ShapeElement.html#getReshapeMode()">getReshapeMode</a>, <a href="ShapeElement.html#getSizeForDrawing()">getSizeForDrawing</a>, <a href="ShapeElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#hasManipulator()">hasManipulator</a>, <a href="ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a>, <a href="ShapeElement.html#isAutosized()">isAutosized</a>, <a href="ShapeElement.html#isCenterlineInner()">isCenterlineInner</a>, <a href="ShapeElement.html#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>, <a href="ShapeElement.html#isOnEdge()">isOnEdge</a>, <a href="ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a>, <a href="ShapeElement.html#isShrinkable()">isShrinkable</a>, <a href="ShapeElement.html#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="ShapeElement.html#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>, <a href="ShapeElement.html#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>, <a href="ShapeElement.html#layoutChildren()">layoutChildren</a>, <a href="ShapeElement.html#maximumDimension(java.awt.Dimension)">maximumDimension</a>, <a href="ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a>, <a href="ShapeElement.html#moveLinksToSelf()">moveLinksToSelf</a>, <a href="ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a>, <a href="ShapeElement.html#movePathElements()">movePathElements</a>, <a href="ShapeElement.html#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>, <a href="ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="ShapeElement.html#providesHorizontalCenterline()">providesHorizontalCenterline</a>, <a href="ShapeElement.html#providesVerticalCenterline()">providesVerticalCenterline</a>, <a href="ShapeElement.html#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setAutosize(boolean)">setAutosize</a>, <a href="ShapeElement.html#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a>, <a href="ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a>, <a href="ShapeElement.html#setMinimumDimension(int,int)">setMinimumDimension</a>, <a href="ShapeElement.html#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a>, <a href="ShapeElement.html#setOldRect(java.awt.Rectangle)">setOldRect</a>, <a href="ShapeElement.html#setOnEdge(int)">setOnEdge</a>, <a href="ShapeElement.html#setPreferredDimension(int,int)">setPreferredDimension</a>, <a href="ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a>, <a href="ShapeElement.html#shouldDrawShadow()">shouldDrawShadow</a>, <a href="ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a>, <a href="ShapeElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="ShapeElement.html#snapsToCenterlines()">snapsToCenterlines</a>, <a href="ShapeElement.html#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a>, <a href="ShapeElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="ShapeElement.html#toString()">toString</a>, <a href="ShapeElement.html#updateLater()">updateLater</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="../paths/PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="../paths/PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#resizeParent()">resizeParent</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</h3>
<code>getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.CompartmentSupport">Methods inherited from interface com.nomagic.magicdraw.uml.CompartmentSupport</h3>
<code>setVisibleElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../../MDElement.html#getProject()">getProject</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</h3>
<code>addProperty, asPresentationElement, getProperty, getPropertyManager</code></div>
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
<section class="detail" id="ALL">
<h3>ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALL</span></div>
<div class="block">Members display options - display all members.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ONLY_PUBLIC">
<h3>ONLY_PUBLIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ONLY_PUBLIC</span></div>
<div class="block">Members display options - display only public members.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.ONLY_PUBLIC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NOT_PRIVATE">
<h3>NOT_PRIVATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NOT_PRIVATE</span></div>
<div class="block">Members display options - not private members.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.NOT_PRIVATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MEMBERS_DISPLAY_MODES">
<h3>MEMBERS_DISPLAY_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">MEMBERS_DISPLAY_MODES</span></div>
<div class="block">List of available members display options.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#ALL"><code>ALL</code></a></li>
<li><a href="#ONLY_PUBLIC"><code>ONLY_PUBLIC</code></a></li>
<li><a href="#NOT_PRIVATE"><code>NOT_PRIVATE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WITHOUT_ASSOCIATION">
<h3>WITHOUT_ASSOCIATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">WITHOUT_ASSOCIATION</span></div>
<div class="block">Association ends display options - display association end if association symbol is not drawn in the diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ClassifierView.WITHOUT_ASSOCIATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSOCIATION_ENDS_DISPLAY_MODES">
<h3>ASSOCIATION_ENDS_DISPLAY_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">ASSOCIATION_ENDS_DISPLAY_MODES</span></div>
<div class="block">List of available association ends display in attribute compartment mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#ALL"><code>ALL</code></a></li>
<li><a href="#WITHOUT_ASSOCIATION"><code>WITHOUT_ASSOCIATION</code></a></li>
<li><code>TaggedValuesDisplayModeOwner.DO_NOT_DISPLAY</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_SIZE">
<h3>DEFAULT_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">DEFAULT_SIZE</span></div>
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
<h3>ClassifierView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassifierView</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>ClassifierView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassifierView</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView,boolean)">
<h3>ClassifierView</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ClassifierView</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView header,
 boolean canDisplayStructure)</span></div>
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
<section class="detail" id="getDefaultDimension()">
<h3>getDefaultDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getDefaultDimension</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#getDefaultDimension()">getDefaultDimension</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateSignatureView()">
<h3>getTemplateSignatureView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.TemplateSignatureView</span> <span class="element-name">getTemplateSignatureView</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>TemplateSignatureView symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructureCompartmentView()">
<h3>getStructureCompartmentView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentView</span> <span class="element-name">getStructureCompartmentView</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>StructureCompartment symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowFullType(boolean)">
<h3>sSetShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowFullType</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Sets show full type for members</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - show full type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowFullType(boolean)">
<h3>setShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowFullType</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Sets show full type for members</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - show full type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowFullType()">
<h3>isShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowFullType</span>()</div>
<div class="block">Returns show full type</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>show full type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetUseAdvancedColoring(boolean)">
<h3>sSetUseAdvancedColoring</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetUseAdvancedColoring</span><wbr/><span class="parameters">(boolean use)</span></div>
<div class="block">Sets use advanced coloring</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>use</code> - use advanced coloring flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseAdvancedColoring(boolean)">
<h3>setUseAdvancedColoring</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseAdvancedColoring</span><wbr/><span class="parameters">(boolean use)</span></div>
<div class="block">Sets use advanced coloring</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>use</code> - use advanced coloring flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseAdvancedColoring()">
<h3>isUseAdvancedColoring</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseAdvancedColoring</span>()</div>
<div class="block">Returns use advanced coloring flag value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>advanced coloring value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ClassifierView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ClassifierView</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>clone</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preferredSizeIgnoringOrientation(java.awt.Dimension,int,int)">
<h3>preferredSizeIgnoringOrientation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preferredSizeIgnoringOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>preferredSizeIgnoringOrientation</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalLayoutChildren(boolean)">
<h3>internalLayoutChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalLayoutChildren</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalLayoutChildren</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateSignatureExtent(boolean)">
<h3>getTemplateSignatureExtent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></span> <span class="element-name">getTemplateSignatureExtent</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAdditionalHeaderHeightForPreferredBounds(java.awt.Rectangle)">
<h3>getAdditionalHeaderHeightForPreferredBounds</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getAdditionalHeaderHeightForPreferredBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> headerBounds)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getAdditionalHeaderHeightForPreferredBounds</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateForUpdateOperation()">
<h3>createStateForUpdateOperation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">createStateForUpdateOperation</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></span></div>
<div class="block">Create collection of any properties used to distinguish during shape update if movePathElements should be called</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createStateForUpdateOperation</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Returns:</dt>
<dd>state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalSpecificUpdate()">
<h3>internalSpecificUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalSpecificUpdate</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></span></div>
<div class="block">Specific to every shape and model element update operation. Must be overridden in subclasses if you need to do specific tasks.
 !!! Important - all resizing, paths moving and so on is done in updatePresentationElement and should not be done in specific update.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalSpecificUpdate</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>AbstractHeaderShapeView.internalUpdatePresentationElement()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#atInsert()">PresentationElement</a></code></span></div>
<div class="block">Invalidates object at insert</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#atInsert()">atInsert</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>atInsert</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#dispose()">PresentationElement</a></code></span></div>
<div class="block">disposes ends of links when link is deleted</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#dispose()">dispose</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>dispose</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateChildrenVisibility()">
<h3>updateChildrenVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateChildrenVisibility</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>updateChildrenVisibility</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSuppressAttributes()">
<h3>isSuppressAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuppressAttributes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSuppressMethods()">
<h3>isSuppressMethods</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuppressMethods</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSuppressed(java.lang.Class)">
<h3>isSuppressed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuppressed</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> modelElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSuppressStructure()">
<h3>isSuppressStructure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuppressStructure</span>()</div>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.
 See "Visitor" pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initialize()">
<h3>initialize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initialize</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#initialize()">PresentationElement</a></code></span></div>
<div class="block">Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#initialize()">initialize</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Object view has no children.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>canAddInstance</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Check of given symbol can be added as child into this symbol.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>canAddChild</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>symbol</code> - symbol</dd>
<dt>Returns:</dt>
<dd>true if symbol can be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canStereotypeIconGrow()">
<h3>canStereotypeIconGrow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canStereotypeIconGrow</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if stereotype icon forces shape growing into all directions on resize</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">
<h3>createBoundsShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createBoundsShape</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">ShapeElement</a></code></span></div>
<div class="block">Creates bounding shape for intersection calculation.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createBoundsShape</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>path</code> - path</dd>
<dd><code>transformation</code> - transformation</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean)">
<h3>addPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index,
 boolean resize)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">If a specified object not inserted in this container then adds a new object view to the container.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addPresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - new PresentationElement object</dd>
<dd><code>index</code> - index to add at</dd>
<dd><code>resize</code> - resize parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">
<h3>sAddPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sAddPresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">PresentationElement</a></code></span></div>
<div class="block">Add given child to this symbol at given index</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>sAddPresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
<dd><code>index</code> - index to add at. Can be -1</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">
<h3>removePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 boolean resizeParent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">Removes object view from container.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - object to remove</dd>
<dd><code>resizeParent</code> - resize parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sRemovePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sRemovePresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Removes given child</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>sRemovePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>internalApplyProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalApplyProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">PresentationElement</a></code></span></div>
<div class="block">Applies properties from given property manager</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalApplyProperties</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalSilentApply()">
<h3>internalSilentApply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalSilentApply</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalSilentApply()">PresentationElement</a></code></span></div>
<div class="block">Silently applies all properties after initialization</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalSilentApply</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetTaggedValuesDisplayMode(java.lang.String)">
<h3>sSetTaggedValuesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetTaggedValuesDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>sSetTaggedValuesDisplayMode</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTaggedValuesDisplayMode(java.lang.String)">
<h3>setTaggedValuesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTaggedValuesDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setTaggedValuesDisplayMode</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowTaggedValuesStereotypes()">
<h3>isShowTaggedValuesStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowTaggedValuesStereotypes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetShowTaggedValuesStereotypes(boolean)">
<h3>sSetShowTaggedValuesStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowTaggedValuesStereotypes</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowTaggedValuesStereotypes(boolean)">
<h3>setShowTaggedValuesStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowTaggedValuesStereotypes</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowQualifiedNameInTaggedValues()">
<h3>isShowQualifiedNameInTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowQualifiedNameInTaggedValues</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetShowQualifiedNameInTaggedValues(boolean)">
<h3>sSetShowQualifiedNameInTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowQualifiedNameInTaggedValues</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowQualifiedNameInTaggedValues(boolean)">
<h3>setShowQualifiedNameInTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowQualifiedNameInTaggedValues</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setCutMemberNames(boolean)">
<h3>setCutMemberNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCutMemberNames</span><wbr/><span class="parameters">(boolean cut)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetCutMemberNames(boolean)">
<h3>sSetCutMemberNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetCutMemberNames</span><wbr/><span class="parameters">(boolean cut)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCutMemberNames()">
<h3>isCutMemberNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCutMemberNames</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTaggedValuesDisplayMode()">
<h3>getTaggedValuesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTaggedValuesDisplayMode</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getTaggedValuesDisplayMode</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.TaggedValuesDisplayModeOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawComparator()">
<h3>getDrawComparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getDrawComparator</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowUML_2_0_Notation(boolean)">
<h3>sSetShowUML_2_0_Notation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowUML_2_0_Notation</span><wbr/><span class="parameters">(boolean b)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowUML_2_0_Notation()">
<h3>isShowUML_2_0_Notation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowUML_2_0_Notation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>addConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addConnectedPathElement</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">PathConnector</a></code></span></div>
<div class="block">Adds a new path element, and recalculates its position.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element to be added.</dd>
<dt>Returns:</dt>
<dd>true if an element was added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reshapeToPreferred()">
<h3>reshapeToPreferred</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">reshapeToPreferred</span>()</div>
</section>
</li>
<li>
<section class="detail" id="removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>removeConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeConnectedPathElement</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">PathConnector</a></code></span></div>
<div class="block">Removes path element.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>link</code> - element to remove.</dd>
<dt>Returns:</dt>
<dd>true if an element was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowUML_2_0_Notation(boolean)">
<h3>setShowUML_2_0_Notation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowUML_2_0_Notation</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTemplateSignatureVisible()">
<h3>isTemplateSignatureVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTemplateSignatureVisible</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAttributesCompartmentHelper()">
<h3>getAttributesCompartmentHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.AttributesCompartmentHelper</span> <span class="element-name">getAttributesCompartmentHelper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOperationsCompartmentHelper()">
<h3>getOperationsCompartmentHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.OperationsCompartmentHelper</span> <span class="element-name">getOperationsCompartmentHelper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCompartmentHelper(java.lang.Class)">
<h3>getCompartmentHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.CompartmentHelper</span> <span class="element-name">getCompartmentHelper</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> modelElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStructureCompartmentHelper()">
<h3>getStructureCompartmentHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.StructureCompartmentHelper</span> <span class="element-name">getStructureCompartmentHelper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">
<h3>internalGetModelElementToConnectRelationship</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">internalGetModelElementToConnectRelationship</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">PresentationElement</a></code></span></div>
<div class="block">Returns element that should be used for given relationship connecting.
 All possible elements are returned by method <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()"><code>PresentationElement.getModelElementsForRelationshipConnecting()</code></a>.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>all possible elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()"><code>PresentationElement.getModelElementsForRelationshipConnecting()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">
<h3>internalIsSuitableToConnectRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">internalIsSuitableToConnectRelationship</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.RelationshipEnd&lt;?&gt; end)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if given possible elements (end of relationship) is suitable to connect given relationship to this symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetModelElementsForRelationshipConnecting()">
<h3>internalGetModelElementsForRelationshipConnecting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</span> <span class="element-name">internalGetModelElementsForRelationshipConnecting</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">PresentationElement</a></code></span></div>
<div class="block">Returns all possible element that can be used for some relationship connecting.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>all possible elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createSmartListenerConfig</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetHeaderInsets()">
<h3>internalGetHeaderInsets</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">internalGetHeaderInsets</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalGetHeaderInsets</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalCompartmentInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">
<h3>getAdditionalCompartmentInsets</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">getAdditionalCompartmentInsets</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel level)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getAdditionalCompartmentInsets</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProxyPresentationElementsStream()">
<h3>getProxyPresentationElementsStream</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getProxyPresentationElementsStream</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getProxyPresentationElementsStream</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetSelfManipulationPreferredSize()">
<h3>internalGetSelfManipulationPreferredSize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">internalGetSelfManipulationPreferredSize</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalGetSelfManipulationPreferredSize</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Returns:</dt>
<dd>size for manipulation which does not take into account the size of children on some specific conditions (for example, in case if wrapped text)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEncapsulatedClassifier()">
<h3>getEncapsulatedClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></span> <span class="element-name">getEncapsulatedClassifier</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getEncapsulatedClassifier</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.PortOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEncapsulatedClassifierProvider()">
<h3>getEncapsulatedClassifierProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></span> <span class="element-name">getEncapsulatedClassifierProvider</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getEncapsulatedClassifierProvider</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.PortOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoxBounds()">
<h3>getBoxBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBoxBounds</span>()</div>
</section>
</li>
<li>
<section class="detail" id="selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>selfSpecificHeaderShapeDraw</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">selfSpecificHeaderShapeDraw</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>selfSpecificHeaderShapeDraw</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawShadow(java.awt.Graphics)">
<h3>drawShadow</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">drawShadow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g)</span></div>
</section>
</li>
<li>
<section class="detail" id="getMembersDisplayMode()">
<h3>getMembersDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMembersDisplayMode</span>()</div>
<div class="block">Gets members display mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>mode</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setMembersDisplayMode(java.lang.String)"><code>setMembersDisplayMode(String)</code></a></li>
<li><a href="#ALL"><code>ALL</code></a></li>
<li><a href="#NOT_PRIVATE"><code>NOT_PRIVATE</code></a></li>
<li><a href="#ONLY_PUBLIC"><code>ONLY_PUBLIC</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetMembersDisplayMode(java.lang.String)">
<h3>sSetMembersDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetMembersDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> membersDisplayMode)</span></div>
<div class="block">Sets members display mode. Does not update classifier symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membersDisplayMode</code> - display mode</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setMembersDisplayMode(java.lang.String)"><code>setMembersDisplayMode(String)</code></a></li>
<li><a href="#ALL"><code>ALL</code></a></li>
<li><a href="#NOT_PRIVATE"><code>NOT_PRIVATE</code></a></li>
<li><a href="#ONLY_PUBLIC"><code>ONLY_PUBLIC</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMembersDisplayMode(java.lang.String)">
<h3>setMembersDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMembersDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> membersDisplayMode)</span></div>
<div class="block">Sets members display mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membersDisplayMode</code> - display mode</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setMembersDisplayMode(java.lang.String)"><code>setMembersDisplayMode(String)</code></a></li>
<li><a href="#ALL"><code>ALL</code></a></li>
<li><a href="#NOT_PRIVATE"><code>NOT_PRIVATE</code></a></li>
<li><a href="#ONLY_PUBLIC"><code>ONLY_PUBLIC</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowInherited()">
<h3>isShowInherited</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowInherited</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if inherited members are shown in compartments</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowInherited(boolean)">
<h3>sSetShowInherited</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowInherited</span><wbr/><span class="parameters">(boolean showInherited)</span></div>
<div class="block">Show inherited members in compartments</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showInherited</code> - show</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowInherited(boolean)">
<h3>setShowInherited</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowInherited</span><wbr/><span class="parameters">(boolean showInherited)</span></div>
<div class="block">Show inherited members in compartments</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showInherited</code> - show</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isChildLayoutable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChildLayoutable</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">ShapeElement</a></code></span></div>
<div class="block">Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.
 Not "layoutable" children are just moved together with parents, but layoutChildren() do not control their location.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>isChildLayoutable</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>child</code> - child</dd>
<dt>Returns:</dt>
<dd>true, if given child is layed-out inside autosize method of this shape. False here</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getElement()">PresentationElement</a></code></span></div>
<div class="block">Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../ModelElementProvider.html#getElement()">getElement</a></code> in interface <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getElement()">getElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>model element of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseMembersCompartmentViewStream()">
<h3>getBaseMembersCompartmentViewStream</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.BaseMembersCompartmentView&gt;</span> <span class="element-name">getBaseMembersCompartmentViewStream</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHeaderView()">
<h3>getHeaderView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView</span> <span class="element-name">getHeaderView</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getHeaderView</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifierHeaderView()">
<h3>getClassifierHeaderView</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.ClassifierHeaderView</span> <span class="element-name">getClassifierHeaderView</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getHeaderView()"><code>getHeaderView()</code></a></div>
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
