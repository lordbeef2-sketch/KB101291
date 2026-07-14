# JAVA OPENAPI: DiagramPresentationElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/DiagramPresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DiagramPresentationElement.html`
- source_sha256: `50e1736f87a19032711a3a36574350f96686e98411f56c64560de45d4405ad55`
- captured_utc: `2026-07-14T16:55:56.312468+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class DiagramPresentationElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)
com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement

All Implemented Interfaces:
`com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer`, `[BaseElement](../BaseElement.html)`, `[MDElement](../MDElement.html)`, `[ModelElementProvider](../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`, `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classDiagramPresentationElement
extends [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)
implements com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner, [StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html), com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer, com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement

Class for representing UML diagram. Diagram purpose is to contain set of presentation elements. 

 For diagram creation use [`ModelElementsManager`](../../openapi/uml/ModelElementsManager.html) class. 

 For working with diagram presentation elements use
 [`PresentationElementsManager`](../../openapi/uml/PresentationElementsManager.html) class.

See Also:
[`ModelElementsManager`](../../openapi/uml/ModelElementsManager.html)
[`PresentationElementsManager`](../../openapi/uml/PresentationElementsManager.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[DIAGRAM_USE_STEREOTYPE_MODES](#DIAGRAM_USE_STEREOTYPE_MODES)`
Diagram use stereotype modes.
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)
`[CANVAS_SIZE](AbstractDiagramPresentationElement.html#CANVAS_SIZE), [DEFAULT_GRID_SIZE](AbstractDiagramPresentationElement.html#DEFAULT_GRID_SIZE), [DIAGRAM_CONTENT_LOADED_PROPERTY](AbstractDiagramPresentationElement.html#DIAGRAM_CONTENT_LOADED_PROPERTY), [DIAGRAM_ORIENTATION_HORIZONTAL](AbstractDiagramPresentationElement.html#DIAGRAM_ORIENTATION_HORIZONTAL), [DIAGRAM_ORIENTATION_MODES](AbstractDiagramPresentationElement.html#DIAGRAM_ORIENTATION_MODES), [DIAGRAM_ORIENTATION_VERTICAL](AbstractDiagramPresentationElement.html#DIAGRAM_ORIENTATION_VERTICAL), [FORCE_CONTENT_SAVE_PROPERTY](AbstractDiagramPresentationElement.html#FORCE_CONTENT_SAVE_PROPERTY), [MAX_GRID_SIZE](AbstractDiagramPresentationElement.html#MAX_GRID_SIZE), [MIN_GRID_SIZE](AbstractDiagramPresentationElement.html#MIN_GRID_SIZE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[DASHED_STROKE](PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](PresentationElement.html#MIN_LINE_WIDTH), [peStyle](PresentationElement.html#peStyle), [SHADOW_WIDTH](PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramPresentationElement](#%3Cinit%3E())()`
Constructs new empty diagram.
`[DiagramPresentationElement](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`

`[DiagramPresentationElement](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)`

`[DiagramPresentationElement](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.uml.DiagramType))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [DiagramType](../DiagramType.html) type)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`static void`
`[addDiagramCreationInfo](#addDiagramCreationInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`

`static void`
`[addDiagramCreationInfo](#addDiagramCreationInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 boolean overwrite)`

`void`
`[applyForcedProperties](#applyForcedProperties())()`
Applies properties stored in default style for diagram and marked as forced.
`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`
Object view has no children.
`protected void`
`[clearCaches](#clearCaches())()`

`[DiagramPresentationElement](DiagramPresentationElement.html)`
`[clone](#clone())()`

`void`
`[createDiagramInfoShape](#createDiagramInfoShape(boolean))(boolean simple)`

`static [DiagramPresentationElement](DiagramPresentationElement.html)`
`[get](#get(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`
Returns diagram of given presentation element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAspectRatioMode](#getAspectRatioMode())()`

`com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer`
`[getContainer](#getContainer())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCurrentDate](#getCurrentDate())()`

`[DiagramLayouter](layout/DiagramLayouter.html)`
`[getDefaultDiagramLayouter](#getDefaultDiagramLayouter())()`

`[Style](../../properties/Style.html)`
`[getDefaultStyleForDiagram](#getDefaultStyleForDiagram(com.nomagic.magicdraw.properties.StyleManager))([StyleManager](../../properties/StyleManager.html) styleManager)`
Finds style for this diagram
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDefaultStyleID](#getDefaultStyleID())()`

`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getDiagram](#getDiagram())()`
Returns Diagram model element of this presentation element.
`[DiagramFrameView](shapes/DiagramFrameView.html)`
`[getDiagramFrame](#getDiagramFrame())()`
Get the frame of the diagram.
`[DiagramPropertiesShape](shapes/DiagramPropertiesShape.html)`
`[getDiagramPropertiesShape](#getDiagramPropertiesShape())()`

`[DiagramType](../DiagramType.html)`
`[getDiagramType](#getDiagramType())()`
Returns the type of the diagram.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramTypeAsString](#getDiagramTypeAsString())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDSLStereotypesDisplayMode](#getDSLStereotypesDisplayMode())()`
Gets DSL stereotype display mode.
`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanType](#getHumanType())()`
Returns human representation of the data type
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Gets the name of this `DiagramPresentationElement` object.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRealType](#getRealType())()`
Returns real diagram type.
`com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject`
`[getRepresentationFromModelElement](#getRepresentationFromModelElement())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypesDisplayMode](#getStereotypesDisplayMode())()`
Gets setereotypes display mode.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements())()`
Returns collection of model elements that have views in this diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements(boolean))(boolean checkOnlyPersistent)`
Deprecated.
checkOnlyPersistent parameter is ignored.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements(boolean,boolean))(boolean checkOnlyPersistent,
 boolean checkOnlyFriendly)`
Deprecated.
checkOnlyPersistent and checkOnlyFriendly parameters are ignored.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements(com.nomagic.magicdraw.core.diagram.UsedElementPolicy))([UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)`
Returns collection of model elements that are used in this diagram.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUseStereotypeMode](#getUseStereotypeMode())()`
Gets diagram use stereotype mode.
`boolean`
`[hasHeavyWeightSymbols](#hasHeavyWeightSymbols())()`
Check is diagram has heavyweight symbols - symbols those can be painted correctly only if diagram is displayed in some JComponent
`protected boolean`
`[hasManipulationSortManager](#hasManipulationSortManager())()`

`boolean`
`[hasNoRegisteredRealTypeDescriptor](#hasNoRegisteredRealTypeDescriptor())()`

`protected void`
`[internalAddToCache](#internalAddToCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,java.lang.String))([AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) oldType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType)`

`void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`protected void`
`[internalClearOnUnload](#internalClearOnUnload())()`

`protected void`
`[internalRemoveFromCache](#internalRemoveFromCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram)`

`protected void`
`[internalSetDiagramType](#internalSetDiagramType(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramUmlType)`

`void`
`[internalSilentApply](#internalSilentApply())()`
Silently applies all properties after initialization
`boolean`
`[isAutosized](#isAutosized())()`

`boolean`
`[isElementInDiagram](#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks if given element exist in any diagram.
`boolean`
`[isElementInDiagram](#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.core.diagram.UsedElementPolicy))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean skipProxyCheck,
 [UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)`
Checks if given element exist in any diagram.
`boolean`
`[isElementInDiagram](#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.core.diagram.UsedElementPolicy))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)`
Checks if given element exist in any diagram.
`boolean`
`[isInitialFrameSizeSet](#isInitialFrameSizeSet())()`

`boolean`
`[isModificationTimeUpdateDisabled](#isModificationTimeUpdateDisabled())()`
Indicates if automatic diagram modification time update is disabled
`boolean`
`[isShowAbbreviatedDiagramType](#isShowAbbreviatedDiagramType())()`

`boolean`
`[isShowActivations](#isShowActivations())()`

`boolean`
`[isShowContextKind](#isShowContextKind())()`

`boolean`
`[isShowContextName](#isShowContextName())()`

`boolean`
`[isShowContextType](#isShowContextType())()`

`boolean`
`[isShowDiagramFrame](#isShowDiagramFrame())()`

`boolean`
`[isShowDiagramInfo](#isShowDiagramInfo())()`

`boolean`
`[isShowDiagramName](#isShowDiagramName())()`

`boolean`
`[isShowDiagramOwner](#isShowDiagramOwner())()`

`boolean`
`[isShowDiagramType](#isShowDiagramType())()`

`boolean`
`[isShowMessageNumbers](#isShowMessageNumbers())()`

`boolean`
`[isShowParameters](#isShowParameters())()`

`boolean`
`[isUseAdvancedNumbering](#isUseAdvancedNumbering())()`

`boolean`
`[isUseFlowLayoutLogic](#isUseFlowLayoutLogic())()`
Indicates if smart path/shape edit should be used in this diagram.
`boolean`
`[layout](#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) layouter)`
Deprecated, for removal: This API element is subject to removal in a future version.
`void`
`[onFontChange](#onFontChange())()`

`void`
`[positionDiagramInfoShapeOnFrame](#positionDiagramInfoShapeOnFrame(com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape))([DiagramPropertiesShape](shapes/DiagramPropertiesShape.html) shape)`

`void`
`[postOpenFromCommand](#postOpenFromCommand())()`

`void`
`[preferredSize](#preferredSize(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) dim)`

`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
Listens for property change it can be: data was edited text box was edited
`static void`
`[registerHeavyWeightSymbolsChecker](#registerHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker))(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)`

`void`
`[resetLastModificationUpdateTime](#resetLastModificationUpdateTime())()`
Reset cached last diagram modification time.
`void`
`[setAspectRatioMode](#setAspectRatioMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[setAutosize](#setAutosize(boolean))(boolean val)`

`void`
`[setDefaultStyleID](#setDefaultStyleID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets new diagram style id to representation object
`void`
`[setDiagramOrientationMode](#setDiagramOrientationMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Sets diagram orientation mode.
`void`
`[setDiagramType](#setDiagramType(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](../DiagramType.html) type)`
Sets the type of the diagram and fires
 the property change event with name ExtendedPropertyNames.EDIT_DIAGRAM_TYPE .
`void`
`[setDSLStereotypesDisplayMode](#setDSLStereotypesDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Sets DSL stereotype display mode value.
`void`
`[setInitialDiagramFrameBounds](#setInitialDiagramFrameBounds())()`
Sets initial diagram frame bounds for this diagram's frame.
`void`
`[setInitialFrameSizeSet](#setInitialFrameSizeSet(boolean))(boolean value)`
Set a flag that diagram frame size should not be recalculated on opening.
`void`
`[setModificationTimeUpdateDisabled](#setModificationTimeUpdateDisabled(boolean))(boolean modificationTimeUpdateDisabled)`
Disables automatic diagram modification time update.
`void`
`[setRealType](#setRealType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) realType)`
If diagram type is not registered then known type is set.
`void`
`[setShowAbbreviatedDiagramType](#setShowAbbreviatedDiagramType(boolean))(boolean show)`

`void`
`[setShowActivations](#setShowActivations(boolean))(boolean b)`

`void`
`[setShowContextKind](#setShowContextKind(boolean))(boolean show)`

`void`
`[setShowContextName](#setShowContextName(boolean))(boolean show)`

`void`
`[setShowContextType](#setShowContextType(boolean))(boolean show)`

`void`
`[setShowDiagramFrame](#setShowDiagramFrame(boolean))(boolean show)`

`void`
`[setShowDiagramInfo](#setShowDiagramInfo(boolean))(boolean showDiagramInfo)`

`void`
`[setShowDiagramName](#setShowDiagramName(boolean))(boolean show)`

`void`
`[setShowDiagramOwner](#setShowDiagramOwner(boolean))(boolean show)`

`void`
`[setShowDiagramType](#setShowDiagramType(boolean))(boolean show)`

`void`
`[setShowMessageNumbers](#setShowMessageNumbers(boolean))(boolean b)`

`void`
`[setShowParameters](#setShowParameters(boolean))(boolean show)`

`void`
`[setStereotypesDisplayMode](#setStereotypesDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Sets stereotype display mode value.
`void`
`[setSuspendShapeAutoResizeMode](#setSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[setUseAdvancedNumbering](#setUseAdvancedNumbering(boolean))(boolean b)`

`void`
`[setUseStereotypeMode](#setUseStereotypeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Sets diagram use stereotype mode.
`void`
`[sSetAspectRatioMode](#sSetAspectRatioMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[sSetAutosize](#sSetAutosize(boolean))(boolean val)`

`void`
`[sSetDiagramFrame](#sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView diagramFrame)`

`void`
`[sSetDiagramOrientationMode](#sSetDiagramOrientationMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Simple set for diagram orientation mode property
`void`
`[sSetDiagramType](#sSetDiagramType(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](../DiagramType.html) type)`
Sets the type of the diagram.
`void`
`[sSetDSLStereotypesDisplayMode](#sSetDSLStereotypesDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Simple sets (no updates) DSL stereotypes display mode.
`void`
`[sSetElement](#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Sets diagram element for this object.
`protected void`
`[sSetForceStoreContentOnSave](#sSetForceStoreContentOnSave(boolean))(boolean forceStoreContentOnSave)`

`void`
`[sSetShowAbbreviatedDiagramType](#sSetShowAbbreviatedDiagramType(boolean))(boolean show)`

`void`
`[sSetShowActivations](#sSetShowActivations(boolean))(boolean b)`

`void`
`[sSetShowContextKind](#sSetShowContextKind(boolean))(boolean show)`

`void`
`[sSetShowContextName](#sSetShowContextName(boolean))(boolean show)`

`void`
`[sSetShowContextType](#sSetShowContextType(boolean))(boolean show)`

`void`
`[sSetShowDiagramFrame](#sSetShowDiagramFrame(boolean))(boolean show)`

`void`
`[sSetShowDiagramInfo](#sSetShowDiagramInfo(boolean))(boolean b)`

`void`
`[sSetShowDiagramName](#sSetShowDiagramName(boolean))(boolean show)`

`void`
`[sSetShowDiagramOwner](#sSetShowDiagramOwner(boolean))(boolean show)`

`void`
`[sSetShowDiagramType](#sSetShowDiagramType(boolean))(boolean show)`

`void`
`[sSetShowParameters](#sSetShowParameters(boolean))(boolean show)`

`void`
`[sSetStereotypesDisplayMode](#sSetStereotypesDisplayMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Simple sets (no updates) stereotypes display mode.
`void`
`[sSetSuspendShapeAutoResizeMode](#sSetSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[sSetUseStereotypeMode](#sSetUseStereotypeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`
Simple set for diagram use stereotype mode property
`static void`
`[unRegisterHeavyWeightSymbolsChecker](#unRegisterHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker))(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)`

`void`
`[updateDiagramPropertiesShapeModificationTime](#updateDiagramPropertiesShapeModificationTime())()`

`void`
`[updateFrameSize](#updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)
`[addContentPropertyChangeListener](AbstractDiagramPresentationElement.html#addContentPropertyChangeListener(java.beans.PropertyChangeListener)), [addDynamicRepresentationProvider](AbstractDiagramPresentationElement.html#addDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)), [addDynamicStyleProvider](AbstractDiagramPresentationElement.html#addDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)), [addPresentationElement](AbstractDiagramPresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [addPropertyChangeListener](AbstractDiagramPresentationElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [adjustInitialDiagramFrameBounds](AbstractDiagramPresentationElement.html#adjustInitialDiagramFrameBounds(java.awt.Rectangle)), [atInsert](AbstractDiagramPresentationElement.html#atInsert()), [autosizeSuspendedSymbolsWithHiddenContent](AbstractDiagramPresentationElement.html#autosizeSuspendedSymbolsWithHiddenContent()), [calculateInitialDiagramFrameBounds](AbstractDiagramPresentationElement.html#calculateInitialDiagramFrameBounds()), [canAddChild](AbstractDiagramPresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canDeleteChild](AbstractDiagramPresentationElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [cleanupAfterLoad](AbstractDiagramPresentationElement.html#cleanupAfterLoad()), [close](AbstractDiagramPresentationElement.html#close()), [close](AbstractDiagramPresentationElement.html#close(boolean)), [collectPresentationElementsRecursively](AbstractDiagramPresentationElement.html#collectPresentationElementsRecursively()), [collectShowingManipulatedElementsRecursively](AbstractDiagramPresentationElement.html#collectShowingManipulatedElementsRecursively()), [collectShowingPresentationElementsRecursively](AbstractDiagramPresentationElement.html#collectShowingPresentationElementsRecursively()), [coversPoint](AbstractDiagramPresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [dispose](AbstractDiagramPresentationElement.html#dispose()), [ensureLoaded](AbstractDiagramPresentationElement.html#ensureLoaded()), [findPresentationElement](AbstractDiagramPresentationElement.html#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)), [findPresentationElement](AbstractDiagramPresentationElement.html#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findPresentationElementForPathConnecting](AbstractDiagramPresentationElement.html#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)), [findPresentationElements](AbstractDiagramPresentationElement.html#findPresentationElements(java.lang.Class)), [findPresentationElements](AbstractDiagramPresentationElement.html#findPresentationElements(java.util.function.Predicate)), [findPresentationElementsForPathConnecting](AbstractDiagramPresentationElement.html#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [fireContentPropertyChange](AbstractDiagramPresentationElement.html#fireContentPropertyChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.lang.Object,java.lang.Object)), [firePropertyChange](AbstractDiagramPresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getAbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html#getAbstractDiagramPresentationElement()), [getBackgroundColor](AbstractDiagramPresentationElement.html#getBackgroundColor()), [getBounds](AbstractDiagramPresentationElement.html#getBounds()), [getCenterlineManager](AbstractDiagramPresentationElement.html#getCenterlineManager()), [getContentHash](AbstractDiagramPresentationElement.html#getContentHash()), [getContentState](AbstractDiagramPresentationElement.html#getContentState()), [getDiagramOrientationMode](AbstractDiagramPresentationElement.html#getDiagramOrientationMode()), [getDynamicRepresentationProviders](AbstractDiagramPresentationElement.html#getDynamicRepresentationProviders()), [getDynamicStyleProviders](AbstractDiagramPresentationElement.html#getDynamicStyleProviders()), [getGridSize](AbstractDiagramPresentationElement.html#getGridSize()), [getID](AbstractDiagramPresentationElement.html#getID()), [getLineJumpPlace](AbstractDiagramPresentationElement.html#getLineJumpPlace()), [getManipulatedElementAt](AbstractDiagramPresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedElementAt](AbstractDiagramPresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulationSortManager](AbstractDiagramPresentationElement.html#getManipulationSortManager()), [getOpenConfigurator](AbstractDiagramPresentationElement.html#getOpenConfigurator()), [getOwnStyleDelegate](AbstractDiagramPresentationElement.html#getOwnStyleDelegate()), [getPathGridSize](AbstractDiagramPresentationElement.html#getPathGridSize()), [getPathToMoveCache](AbstractDiagramPresentationElement.html#getPathToMoveCache()), [getPresentationElementAt](AbstractDiagramPresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementAt](AbstractDiagramPresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElements](AbstractDiagramPresentationElement.html#getPresentationElements()), [getPresentationElementsAt](AbstractDiagramPresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](AbstractDiagramPresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](AbstractDiagramPresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getRepresentation](AbstractDiagramPresentationElement.html#getRepresentation()), [getSortManager](AbstractDiagramPresentationElement.html#getSortManager()), [getSortManagers](AbstractDiagramPresentationElement.html#getSortManagers(boolean)), [getSurfaces](AbstractDiagramPresentationElement.html#getSurfaces()), [getSuspendShapeAutoResizeMode](AbstractDiagramPresentationElement.html#getSuspendShapeAutoResizeMode()), [getValue](AbstractDiagramPresentationElement.html#getValue(java.lang.Object)), [getValueOrCompute](AbstractDiagramPresentationElement.html#getValueOrCompute(java.lang.Object,java.util.function.Supplier)), [getVisibleBounds](AbstractDiagramPresentationElement.html#getVisibleBounds()), [getZoom](AbstractDiagramPresentationElement.html#getZoom()), [hasSelectableSymbols](AbstractDiagramPresentationElement.html#hasSelectableSymbols()), [hasVerticalOrientation](AbstractDiagramPresentationElement.html#hasVerticalOrientation()), [initialize](AbstractDiagramPresentationElement.html#initialize()), [intersects](AbstractDiagramPresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [isDummyMode](AbstractDiagramPresentationElement.html#isDummyMode()), [isEmpty](AbstractDiagramPresentationElement.html#isEmpty()), [isForceStoreContentOnSave](AbstractDiagramPresentationElement.html#isForceStoreContentOnSave()), [isLabelsAutoDisplaySuspended](AbstractDiagramPresentationElement.html#isLabelsAutoDisplaySuspended()), [isLoaded](AbstractDiagramPresentationElement.html#isLoaded()), [isModified](AbstractDiagramPresentationElement.html#isModified()), [isOpening](AbstractDiagramPresentationElement.html#isOpening()), [isShapesAutoResizeSuspended](AbstractDiagramPresentationElement.html#isShapesAutoResizeSuspended()), [isShowGrid](AbstractDiagramPresentationElement.html#isShowGrid()), [isSnapToGridPaths](AbstractDiagramPresentationElement.html#isSnapToGridPaths()), [isSnapToGridShapes](AbstractDiagramPresentationElement.html#isSnapToGridShapes()), [isSymbolDiagram](AbstractDiagramPresentationElement.html#isSymbolDiagram()), [isUseGradientForFill](AbstractDiagramPresentationElement.html#isUseGradientForFill()), [layout](AbstractDiagramPresentationElement.html#layout(boolean)), [layout](AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [loadContents](AbstractDiagramPresentationElement.html#loadContents(com.nomagic.task.ProgressStatus)), [open](AbstractDiagramPresentationElement.html#open()), [open](AbstractDiagramPresentationElement.html#open(boolean)), [open](AbstractDiagramPresentationElement.html#open(boolean,boolean)), [open](AbstractDiagramPresentationElement.html#open(boolean,boolean,boolean)), [openInActiveTab](AbstractDiagramPresentationElement.html#openInActiveTab(boolean)), [paintChildren](AbstractDiagramPresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelf](AbstractDiagramPresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [recalculateInternalDataRequired](AbstractDiagramPresentationElement.html#recalculateInternalDataRequired()), [recursiveAutosize](AbstractDiagramPresentationElement.html#recursiveAutosize()), [registerInProject](AbstractDiagramPresentationElement.html#registerInProject()), [removeContentPropertyChangeListener](AbstractDiagramPresentationElement.html#removeContentPropertyChangeListener(java.beans.PropertyChangeListener)), [removeDynamicRepresentationProvider](AbstractDiagramPresentationElement.html#removeDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)), [removeDynamicStyleProvider](AbstractDiagramPresentationElement.html#removeDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)), [removePropertyChangeListener](AbstractDiagramPresentationElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [resetContainer](AbstractDiagramPresentationElement.html#resetContainer()), [sAddPresentationElement](AbstractDiagramPresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [setBounds](AbstractDiagramPresentationElement.html#setBounds(java.awt.Rectangle)), [setContentHash](AbstractDiagramPresentationElement.html#setContentHash(java.lang.String)), [setDiagramRepresentationObject](AbstractDiagramPresentationElement.html#setDiagramRepresentationObject(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject)), [setDummyMode](AbstractDiagramPresentationElement.html#setDummyMode(boolean)), [setForceStoreContentOnSave](AbstractDiagramPresentationElement.html#setForceStoreContentOnSave(boolean)), [setGridSize](AbstractDiagramPresentationElement.html#setGridSize(int)), [setID](AbstractDiagramPresentationElement.html#setID(java.lang.String)), [setInitializer](AbstractDiagramPresentationElement.html#setInitializer(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer)), [setLabelsAutoDisplaySuspended](AbstractDiagramPresentationElement.html#setLabelsAutoDisplaySuspended(boolean)), [setModified](AbstractDiagramPresentationElement.html#setModified(boolean)), [setOpenConfigurator](AbstractDiagramPresentationElement.html#setOpenConfigurator(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator)), [setPresentationElements](AbstractDiagramPresentationElement.html#setPresentationElements(java.util.List)), [setShapesAutoResizeSuspended](AbstractDiagramPresentationElement.html#setShapesAutoResizeSuspended(boolean)), [setShowGrid](AbstractDiagramPresentationElement.html#setShowGrid(boolean)), [setSnapToGridPaths](AbstractDiagramPresentationElement.html#setSnapToGridPaths(boolean)), [setSnapToGridShapes](AbstractDiagramPresentationElement.html#setSnapToGridShapes(boolean)), [setUseGradientForFill](AbstractDiagramPresentationElement.html#setUseGradientForFill(boolean)), [setValue](AbstractDiagramPresentationElement.html#setValue(java.lang.Object,T)), [setZoomProvider](AbstractDiagramPresentationElement.html#setZoomProvider(java.util.function.Function)), [snapViewToGrid](AbstractDiagramPresentationElement.html#snapViewToGrid(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetBounds](AbstractDiagramPresentationElement.html#sSetBounds(java.awt.Rectangle)), [sSetGridSize](AbstractDiagramPresentationElement.html#sSetGridSize(int)), [sSetLabelsAutoDisplaySuspended](AbstractDiagramPresentationElement.html#sSetLabelsAutoDisplaySuspended(boolean)), [sSetLineJumpPlace](AbstractDiagramPresentationElement.html#sSetLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace)), [sSetPresentationElements](AbstractDiagramPresentationElement.html#sSetPresentationElements(java.util.List)), [sSetShapesAutoResizeSuspended](AbstractDiagramPresentationElement.html#sSetShapesAutoResizeSuspended(boolean)), [sSetShowGrid](AbstractDiagramPresentationElement.html#sSetShowGrid(boolean)), [sSetSnapToGridPaths](AbstractDiagramPresentationElement.html#sSetSnapToGridPaths(boolean)), [sSetSnapToGridShapes](AbstractDiagramPresentationElement.html#sSetSnapToGridShapes(boolean)), [unloadDiagram](AbstractDiagramPresentationElement.html#unloadDiagram()), [unregisterFromProject](AbstractDiagramPresentationElement.html#unregisterFromProject()), [useParentStyle](AbstractDiagramPresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[addPresentationElement](PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addPresentationElementWithoutResize](PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustBoundsBeforeChange](PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)), [adjustChildBounds](PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [adjustChildBoundsForMoving](PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](PresentationElement.html#alwaysShowTooltip()), [applyProperties](PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](PresentationElement.html#askDeleteDataConfirmation()), [atInsertChildren](PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](PresentationElement.html#autosizeAndResizeManipulatedParent()), [autosizeAndResizeParent](PresentationElement.html#autosizeAndResizeParent()), [beforeDelete](PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](PresentationElement.html#boundsChanged()), [boundsChanged](PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)), [canChangeParent](PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](PresentationElement.html#canFill()), [canHavePaths](PresentationElement.html#canHavePaths()), [changeProperties](PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [checkShowsProxy](PresentationElement.html#checkShowsProxy()), [childrenForMoving](PresentationElement.html#childrenForMoving()), [clearShowsProxy](PresentationElement.html#clearShowsProxy()), [collectSubManipulatedElements](PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](PresentationElement.html#coversPoint(int,int)), [createFillStrategy](PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](PresentationElement.html#createPropertyChangeListener()), [createSmartListenerConfig](PresentationElement.html#createSmartListenerConfig(java.util.List)), [disposeChildren](PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](PresentationElement.html#disposePropertyChangeListener()), [draw](PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](PresentationElement.html#dynamicFillColor()), [dynamicLineColor](PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](PresentationElement.html#dynamicStroke()), [dynamicStroke](PresentationElement.html#dynamicStroke(int)), [dynamicStroke](PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](PresentationElement.html#dynamicTextColor()), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [findOwnerForChildElement](PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [generateID](PresentationElement.html#generateID()), [getActualElement](PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](PresentationElement.html#getDiagramSurface()), [getDrawComparator](PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](PresentationElement.html#getFillColor()), [getFont](PresentationElement.html#getFont()), [getFontHeight](PresentationElement.html#getFontHeight()), [getFontRenderContext](PresentationElement.html#getFontRenderContext()), [getHumanName](PresentationElement.html#getHumanName()), [getIntersection](PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLineColor](PresentationElement.html#getLineColor()), [getLineWidth](PresentationElement.html#getLineWidth()), [getManipulatedElementAt](PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](PresentationElement.html#getManipulationBounds(java.awt.Point)), [getManipulationPreferredDimension](PresentationElement.html#getManipulationPreferredDimension()), [getMiddlePoint](PresentationElement.html#getMiddlePoint()), [getMiddlePoint](PresentationElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](PresentationElement.html#getMiddlePointX()), [getMiddlePointX](PresentationElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](PresentationElement.html#getMiddlePointY()), [getMiddlePointY](PresentationElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](PresentationElement.html#getMinimumDimension()), [getModelElement](PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](PresentationElement.html#getModelElementToMove()), [getNotCopyBounds](PresentationElement.html#getNotCopyBounds()), [getNotZoomedTolerance](PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](PresentationElement.html#getObjectParent()), [getParent](PresentationElement.html#getParent()), [getParentSymbolStyleOwner](PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredBounds](PresentationElement.html#getPreferredBounds()), [getPreferredDimension](PresentationElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](PresentationElement.html#getPreferredDimensionForAutosize()), [getPreferredSize](PresentationElement.html#getPreferredSize()), [getPresentationElementAt](PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementCount](PresentationElement.html#getPresentationElementCount()), [getPresentationElementIndex](PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getPresentationElementsAt](PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](PresentationElement.html#getProjectImpl()), [getProperty](PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](PresentationElement.html#getPropertyManager()), [getPropertyManagerName](PresentationElement.html#getPropertyManagerName()), [getRenderer](PresentationElement.html#getRenderer()), [getSelected](PresentationElement.html#getSelected()), [getStroke](PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](PresentationElement.html#getStroke(int)), [getStroke](PresentationElement.html#getStroke(int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int,int)), [getStroke](PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](PresentationElement.html#getStyle()), [getSymbolRenderer](PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](PresentationElement.html#getTextColor()), [getTolerance](PresentationElement.html#getTolerance()), [getVisibility](PresentationElement.html#getVisibility()), [getVisiblePresentationElements](PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](PresentationElement.html#hasManipulatedPresentationElements()), [hasManipulator](PresentationElement.html#hasManipulator()), [hasSharedModelElement](PresentationElement.html#hasSharedModelElement()), [initializeAndAutosize](PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetBoundsShape](PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [internalGetModelElementsForRelationshipConnecting](PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [internalUpdatePresentationElement](PresentationElement.html#internalUpdatePresentationElement()), [intersects](PresentationElement.html#intersects(int,int,int,int)), [invalidate](PresentationElement.html#invalidate()), [isCanChildrenChangeEdge](PresentationElement.html#isCanChildrenChangeEdge()), [isChildVisible](PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isContentHidden](PresentationElement.html#isContentHidden()), [isCreateElementListener](PresentationElement.html#isCreateElementListener()), [isDetectable](PresentationElement.html#isDetectable()), [isDisposed](PresentationElement.html#isDisposed()), [isLayouting](PresentationElement.html#isLayouting()), [isMovableByMoveManager](PresentationElement.html#isMovableByMoveManager()), [isNotNull](PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](PresentationElement.html#isShowElementTypeAsLabel()), [isShowsProxy](PresentationElement.html#isShowsProxy()), [isSnapToGrid](PresentationElement.html#isSnapToGrid()), [isSortable](PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](PresentationElement.html#isTextEditable()), [isUseFillColor](PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](PresentationElement.html#isUseFillColorByProperty()), [isVisible](PresentationElement.html#isVisible()), [isVisibleInDiagram](PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](PresentationElement.html#isVisibleOrShrunken()), [movePathElements](PresentationElement.html#movePathElements()), [movePathElementsRecursively](PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](PresentationElement.html#mustShowContextMenu()), [notifyCreated](PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](PresentationElement.html#onDiagramSurfaceSet()), [onFind](PresentationElement.html#onFind()), [onFind](PresentationElement.html#onFind(boolean)), [onParentChange](PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenBackground](PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForShadowDrawing](PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [recreateListeners](PresentationElement.html#recreateListeners()), [registerInSortManager](PresentationElement.html#registerInSortManager()), [rememberBounds](PresentationElement.html#rememberBounds()), [rememberBounds](PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](PresentationElement.html#removeItSelfOnUpdate()), [removePresentationElement](PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [resizeParent](PresentationElement.html#resizeParent()), [sAddPresentationElement](PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](PresentationElement.html#selectObjectsForMoving()), [selectPathsForMoving](PresentationElement.html#selectPathsForMoving(java.util.List)), [setAllSelected](PresentationElement.html#setAllSelected(boolean)), [setBounds](PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](PresentationElement.html#setCreateElementListener(boolean)), [setDummyResizeMode](PresentationElement.html#setDummyResizeMode(boolean)), [setElement](PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFillColor](PresentationElement.html#setFillColor(java.awt.Color)), [setFont](PresentationElement.html#setFont(java.awt.Font)), [setLayouting](PresentationElement.html#setLayouting(boolean)), [setLineColor](PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](PresentationElement.html#setLocation(int,int)), [setLocation](PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](PresentationElement.html#setNeedRecreateListeners(boolean)), [setParent](PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setPropertyManagerName](PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](PresentationElement.html#setSelected(boolean)), [setSelected](PresentationElement.html#setSelected(java.util.List)), [setSize](PresentationElement.html#setSize(int,int)), [setSize](PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](PresentationElement.html#setTextColor(java.awt.Color)), [setTextEditable](PresentationElement.html#setTextEditable(boolean)), [setUseFillColor](PresentationElement.html#setUseFillColor(boolean)), [setVisibility](PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [setVisible](PresentationElement.html#setVisible(boolean)), [silentApply](PresentationElement.html#silentApply()), [silentApply](PresentationElement.html#silentApply(boolean)), [simpleSetBounds](PresentationElement.html#simpleSetBounds(int,int,int,int)), [simpleSetBounds](PresentationElement.html#simpleSetBounds(java.awt.Rectangle)), [snapToGrid](PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](PresentationElement.html#sortObjectsByY(java.util.List)), [sRemovePresentationElement](PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetBounds](PresentationElement.html#sSetBounds(int,int,int,int)), [sSetLocation](PresentationElement.html#sSetLocation(int,int)), [sSetLocation](PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](PresentationElement.html#sSetSize(int,int)), [sSetSize](PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisibility](PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sSetVisible](PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](PresentationElement.html#update()), [updateAfterLoad](PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateLater](PresentationElement.html#updateLater()), [updateModelByView](PresentationElement.html#updateModelByView()), [updateModelByViewInternal](PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](PresentationElement.html#useParentProperties())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, setResourceIDProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../MDElement.html)
`[getProject](../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, asPresentationElement, getProperty, getPropertyManager`

============ FIELD DETAIL =========== 
Field Details
DIAGRAM_USE_STEREOTYPE_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> DIAGRAM_USE_STEREOTYPE_MODES
Diagram use stereotype modes.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramPresentationElement
@OpenApipublic DiagramPresentationElement()
Constructs new empty diagram.
 Do not use this constructor to create a diagram explicitly.
 Open API provides method for diagrams creation.
See Also:
[`ModelElementsManager.createDiagram(String, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)`](../../openapi/uml/ModelElementsManager.html#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))
DiagramPresentationElement
public DiagramPresentationElement(@CheckForNull
 [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
DiagramPresentationElement
public DiagramPresentationElement(@CheckForNull
 [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 @CheckForNull
 [DiagramType](../DiagramType.html) type)
DiagramPresentationElement
public DiagramPresentationElement(@CheckForNull
 [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 @CheckForNull
 com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)
 ============ METHOD DETAIL ========== 
Method Details
internalAddToCache
protected void internalAddToCache([AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) oldType,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType)
Overrides:
`[internalAddToCache](AbstractDiagramPresentationElement.html#internalAddToCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,java.lang.String))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
internalRemoveFromCache
protected void internalRemoveFromCache([AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram)
Overrides:
`[internalRemoveFromCache](AbstractDiagramPresentationElement.html#internalRemoveFromCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
hasNoRegisteredRealTypeDescriptor
public boolean hasNoRegisteredRealTypeDescriptor()
Overrides:
`[hasNoRegisteredRealTypeDescriptor](AbstractDiagramPresentationElement.html#hasNoRegisteredRealTypeDescriptor())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
sSetDiagramType
@OpenApipublic void sSetDiagramType(@CheckForNull
 [DiagramType](../DiagramType.html) type)
Sets the type of the diagram.
Parameters:
`type` - the type of the diagram
setDiagramType
@OpenApipublic void setDiagramType([DiagramType](../DiagramType.html) type)
Sets the type of the diagram and fires
 the property change event with name ExtendedPropertyNames.EDIT_DIAGRAM_TYPE .
Parameters:
`type` - the type of the diagram
See Also:
[`ExtendedPropertyNames.EDIT_DIAGRAM_TYPE`](../ExtendedPropertyNames.html#EDIT_DIAGRAM_TYPE)
[`Project`](../../core/Project.html)
internalSetDiagramType
protected void internalSetDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramUmlType)
Specified by:
`[internalSetDiagramType](AbstractDiagramPresentationElement.html#internalSetDiagramType(java.lang.String,java.lang.String))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getDiagramType
@OpenApipublic [DiagramType](../DiagramType.html) getDiagramType()
Returns the type of the diagram.
Specified by:
`[getDiagramType](AbstractDiagramPresentationElement.html#getDiagramType())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Returns:
the type of the diagram
See Also:
[`DiagramTypes.UML_CLASS_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM)
[`DiagramTypes.UML_USECASE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM)
[`DiagramTypes.UML_COMMUNICATION_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM)
[`DiagramTypes.UML_SEQUENCE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM)
[`DiagramTypes.UML_STATECHART_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM)
[`DiagramTypes.UML_PROTOCOL_STATE_MACHINE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM)
[`DiagramTypes.UML_ACTIVITY_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM)
[`DiagramTypes.UML_COMPOSITE_STRUCTURE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM)
[`DiagramTypes.UML_OBJECT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM)
[`DiagramTypes.UML_PACKAGE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM)
[`DiagramTypes.UML_COMPONENT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM)
[`DiagramTypes.UML_DEPLOYMENT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM)
[`DiagramTypes.UML_PROFILE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM)
getHumanType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanType()
Returns human representation of the data type
Specified by:
`[getHumanType](../BaseElement.html#getHumanType())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`[getHumanType](PresentationElement.html#getHumanType())` in class `[PresentationElement](PresentationElement.html)`
Returns:
the name of the data
clone
public [DiagramPresentationElement](DiagramPresentationElement.html) clone()
Specified by:
`[clone](../BaseElement.html#clone())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`[clone](AbstractDiagramPresentationElement.html#clone())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getDiagram
@OpenApipublic [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getDiagram()
Returns Diagram model element of this presentation element.
Returns:
Diagram object of this element.
See Also:
[`getElement()`](#getElement())
getElement
public [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getElement()
Description copied from class: `[PresentationElement](PresentationElement.html#getElement())`
Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.
Specified by:
`[getElement](../ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../ModelElementProvider.html)`
Overrides:
`[getElement](PresentationElement.html#getElement())` in class `[PresentationElement](PresentationElement.html)`
Returns:
model element of this presentation element.
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Description copied from class: `[PresentationElement](PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))`
Listens for property change it can be: data was edited text box was edited
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Overrides:
`[propertyChange](AbstractDiagramPresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
accept
@OpenApipublic void accept([Visitor](../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../MDElement.html)`
Overrides:
`[accept](AbstractDiagramPresentationElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getDiagramTypeAsString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramTypeAsString()
Specified by:
`[getDiagramTypeAsString](AbstractDiagramPresentationElement.html#getDiagramTypeAsString())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Gets the name of this `DiagramPresentationElement` object.
Specified by:
`[getName](../MDElement.html#getName())` in interface `[MDElement](../MDElement.html)`
Specified by:
`[getName](../../utils/NameOwner.html#getName())` in interface `[NameOwner](../../utils/NameOwner.html)`
Overrides:
`getName` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
name of this object
sSetShowDiagramOwner
public void sSetShowDiagramOwner(boolean show)
sSetShowAbbreviatedDiagramType
public void sSetShowAbbreviatedDiagramType(boolean show)
sSetShowDiagramName
public void sSetShowDiagramName(boolean show)
sSetShowParameters
public void sSetShowParameters(boolean show)
sSetShowContextName
public void sSetShowContextName(boolean show)
sSetShowContextType
public void sSetShowContextType(boolean show)
sSetShowDiagramType
public void sSetShowDiagramType(boolean show)
sSetShowContextKind
public void sSetShowContextKind(boolean show)
setShowAbbreviatedDiagramType
public void setShowAbbreviatedDiagramType(boolean show)
setShowDiagramName
public void setShowDiagramName(boolean show)
setShowParameters
public void setShowParameters(boolean show)
setShowContextName
public void setShowContextName(boolean show)
setShowContextType
public void setShowContextType(boolean show)
setShowDiagramType
public void setShowDiagramType(boolean show)
setShowContextKind
public void setShowContextKind(boolean show)
isShowAbbreviatedDiagramType
public boolean isShowAbbreviatedDiagramType()
Specified by:
`isShowAbbreviatedDiagramType` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
isShowDiagramName
public boolean isShowDiagramName()
Specified by:
`isShowDiagramName` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
isShowParameters
public boolean isShowParameters()
Specified by:
`isShowParameters` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
isShowContextName
public boolean isShowContextName()
Specified by:
`isShowContextName` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
isShowContextType
public boolean isShowContextType()
Specified by:
`isShowContextType` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
isShowDiagramType
public boolean isShowDiagramType()
Specified by:
`isShowDiagramType` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
isShowContextKind
public boolean isShowContextKind()
Specified by:
`isShowContextKind` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
sSetShowDiagramFrame
public void sSetShowDiagramFrame(boolean show)
isShowDiagramOwner
public boolean isShowDiagramOwner()
isShowDiagramFrame
public boolean isShowDiagramFrame()
Overrides:
`[isShowDiagramFrame](AbstractDiagramPresentationElement.html#isShowDiagramFrame())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
setShowDiagramOwner
public void setShowDiagramOwner(boolean show)
setShowDiagramFrame
public void setShowDiagramFrame(boolean show)
sSetElement
public void sSetElement(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Sets diagram element for this object.
Overrides:
`[sSetElement](PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))` in class `[PresentationElement](PresentationElement.html)`
canAddInstance
public boolean canAddInstance([PresentationElement](PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Object view has no children.
Overrides:
`[canAddInstance](AbstractDiagramPresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
hasManipulationSortManager
protected boolean hasManipulationSortManager()
Overrides:
`[hasManipulationSortManager](AbstractDiagramPresentationElement.html#hasManipulationSortManager())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
onFontChange
public void onFontChange()
Overrides:
`[onFontChange](PresentationElement.html#onFontChange())` in class `[PresentationElement](PresentationElement.html)`
setShowMessageNumbers
public void setShowMessageNumbers(boolean b)
setUseAdvancedNumbering
public void setUseAdvancedNumbering(boolean b)
isShowMessageNumbers
public boolean isShowMessageNumbers()
isUseAdvancedNumbering
public boolean isUseAdvancedNumbering()
isShowDiagramInfo
public boolean isShowDiagramInfo()
sSetShowDiagramInfo
public void sSetShowDiagramInfo(boolean b)
resetLastModificationUpdateTime
public void resetLastModificationUpdateTime()
Reset cached last diagram modification time.
getDiagramPropertiesShape
@CheckForNullpublic [DiagramPropertiesShape](shapes/DiagramPropertiesShape.html) getDiagramPropertiesShape()
setShowDiagramInfo
public void setShowDiagramInfo(boolean showDiagramInfo)
createDiagramInfoShape
public void createDiagramInfoShape(boolean simple)
positionDiagramInfoShapeOnFrame
public void positionDiagramInfoShapeOnFrame([DiagramPropertiesShape](shapes/DiagramPropertiesShape.html) shape)
addDiagramCreationInfo
public static void addDiagramCreationInfo([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
addDiagramCreationInfo
public static void addDiagramCreationInfo([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 boolean overwrite)
sSetShowActivations
public void sSetShowActivations(boolean b)
setShowActivations
public void setShowActivations(boolean b)
isShowActivations
public boolean isShowActivations()
sSetDiagramOrientationMode
public void sSetDiagramOrientationMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Simple set for diagram orientation mode property
Parameters:
`mode` - - diagram orientation mode.
setDiagramOrientationMode
public void setDiagramOrientationMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Sets diagram orientation mode.
Parameters:
`mode` - - diagram orientation mode.
sSetUseStereotypeMode
public void sSetUseStereotypeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Simple set for diagram use stereotype mode property
Parameters:
`mode` - - diagram orientation mode.
setUseStereotypeMode
public void setUseStereotypeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Sets diagram use stereotype mode.
Parameters:
`mode` - - diagram orientation mode.
getUseStereotypeMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUseStereotypeMode()
Gets diagram use stereotype mode.
Specified by:
`getUseStereotypeMode` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
Returns:
diagram orientation mode.
getAspectRatioMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAspectRatioMode()
setAspectRatioMode
public void setAspectRatioMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
sSetAspectRatioMode
public void sSetAspectRatioMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
internalSilentApply
public void internalSilentApply()
Description copied from class: `[PresentationElement](PresentationElement.html#internalSilentApply())`
Silently applies all properties after initialization
Overrides:
`[internalSilentApply](AbstractDiagramPresentationElement.html#internalSilentApply())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Description copied from class: `[PresentationElement](PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))`
Applies properties from given property manager
Overrides:
`[internalApplyProperties](AbstractDiagramPresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Parameters:
`changer` - new properties
preferredSize
public void preferredSize([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) dim)
Overrides:
`[preferredSize](AbstractDiagramPresentationElement.html#preferredSize(java.awt.Dimension))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
isModificationTimeUpdateDisabled
public boolean isModificationTimeUpdateDisabled()
Indicates if automatic diagram modification time update is disabled
Returns:
true when diagram modification time update is disabled
setModificationTimeUpdateDisabled
public void setModificationTimeUpdateDisabled(boolean modificationTimeUpdateDisabled)
Disables automatic diagram modification time update.
Parameters:
`modificationTimeUpdateDisabled` - true to disable automatic diagram modification time update.
updateDiagramPropertiesShapeModificationTime
public void updateDiagramPropertiesShapeModificationTime()
applyForcedProperties
public void applyForcedProperties()
Applies properties stored in default style for diagram and marked as forced.
 They can be marked as forced using "apply" from styles dialog.
Specified by:
`[applyForcedProperties](AbstractDiagramPresentationElement.html#applyForcedProperties())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getUsedModelElements
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUsedModelElements(boolean checkOnlyPersistent)
Deprecated.
checkOnlyPersistent parameter is ignored. Use [`getUsedModelElements()`](#getUsedModelElements())
Returns collection of model elements that are drawn in this diagram.
Parameters:
`checkOnlyPersistent` - if true, result includes elements for symbols which are saved to XMI and not created at run-time. If false, includes all elements.
Returns:
collection of model elements.
getUsedModelElements
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUsedModelElements(boolean checkOnlyPersistent,
 boolean checkOnlyFriendly)
Deprecated.
checkOnlyPersistent and checkOnlyFriendly parameters are ignored. Use [`getUsedModelElements()`](#getUsedModelElements())
Returns collection of model elements that are drawn in this diagram.
Parameters:
`checkOnlyPersistent` - if true, result includes elements for symbols which are saved to XMI and not created at run-time. If false, includes all elements.
`checkOnlyFriendly` - check only "friendly" symbols
Returns:
collection of model elements.
getUsedModelElements
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUsedModelElements()
Returns collection of model elements that have views in this diagram.
Returns:
collection of model elements.
getUsedModelElements
@OpenApipublic [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUsedModelElements([UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)
Returns collection of model elements that are used in this diagram.
Parameters:
`usedElementPolicy` - used element policy
Returns:
collection of model elements.
isElementInDiagram
@OpenApipublic boolean isElementInDiagram([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Checks if given element exist in any diagram.
Parameters:
`element` - element
Returns:
true if element exist in any diagram otherwise false
isElementInDiagram
@OpenApipublic boolean isElementInDiagram([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)
Checks if given element exist in any diagram.
Parameters:
`element` - element
Returns:
true if element exist in any diagram otherwise false
isElementInDiagram
public boolean isElementInDiagram([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean skipProxyCheck,
 [UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)
Checks if given element exist in any diagram.
Parameters:
`element` - element
`skipProxyCheck` - enables to skip if diagram's actual element is proxy
Returns:
true if element exist in any diagram otherwise false
setDefaultStyleID
public void setDefaultStyleID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Sets new diagram style id to representation object
Parameters:
`id` - new id
getDefaultStyleID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDefaultStyleID()
Returns:
Returns the defaultStyleForDiagramID, can be null if default style is equal to diagram style, or diagram is loaded.
getDefaultStyleForDiagram
@CheckForNullpublic [Style](../../properties/Style.html) getDefaultStyleForDiagram([StyleManager](../../properties/StyleManager.html) styleManager)
Finds style for this diagram
Parameters:
`styleManager` - manager to find in.
Returns:
found style, null if no style is created.
getRealType
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRealType()
Returns real diagram type. Real diagram type is diagram type which is not registered but loaded from project file.
Overrides:
`[getRealType](AbstractDiagramPresentationElement.html#getRealType())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Returns:
real type. Can be null.
setRealType
public void setRealType(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) realType)
If diagram type is not registered then known type is set. Real type is preserved for saving.
Parameters:
`realType` - real diagram type.
getCurrentDate
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCurrentDate()
sSetDiagramFrame
public void sSetDiagramFrame(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView diagramFrame)
Overrides:
`[sSetDiagramFrame](AbstractDiagramPresentationElement.html#sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getDiagramFrame
@OpenApi
@CheckForNullpublic [DiagramFrameView](shapes/DiagramFrameView.html) getDiagramFrame()
Get the frame of the diagram.
Specified by:
`[getDiagramFrame](AbstractDiagramPresentationElement.html#getDiagramFrame())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Returns:
frame of the diagram.
getContainer
public com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer getContainer()
Overrides:
`[getContainer](AbstractDiagramPresentationElement.html#getContainer())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Returns:
diagram container
setInitialDiagramFrameBounds
public void setInitialDiagramFrameBounds()
Sets initial diagram frame bounds for this diagram's frame.
Overrides:
`[setInitialDiagramFrameBounds](AbstractDiagramPresentationElement.html#setInitialDiagramFrameBounds())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getStereotypesDisplayMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypesDisplayMode()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
Gets setereotypes display mode.
Specified by:
`getStereotypesDisplayMode` in interface `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`
Specified by:
`[getStereotypesDisplayMode](shapes/StereotypesDisplayModeOwner.html#getStereotypesDisplayMode())` in interface `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`
Returns:
stereotypes display mode.
sSetStereotypesDisplayMode
public void sSetStereotypesDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Description copied from interface: `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html#sSetStereotypesDisplayMode(java.lang.String))`
Simple sets (no updates) stereotypes display mode.
Specified by:
`[sSetStereotypesDisplayMode](shapes/StereotypesDisplayModeOwner.html#sSetStereotypesDisplayMode(java.lang.String))` in interface `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`
Parameters:
`mode` - stereotypes display mode value.
setStereotypesDisplayMode
public void setStereotypesDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Description copied from interface: `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html#setStereotypesDisplayMode(java.lang.String))`
Sets stereotype display mode value.
Specified by:
`[setStereotypesDisplayMode](shapes/StereotypesDisplayModeOwner.html#setStereotypesDisplayMode(java.lang.String))` in interface `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`
Parameters:
`mode` - stereotype display mode.
getDSLStereotypesDisplayMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDSLStereotypesDisplayMode()
Description copied from interface: `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html#getDSLStereotypesDisplayMode())`
Gets DSL stereotype display mode.
Specified by:
`[getDSLStereotypesDisplayMode](shapes/StereotypesDisplayModeOwner.html#getDSLStereotypesDisplayMode())` in interface `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`
Returns:
stereotype display mode.
sSetDSLStereotypesDisplayMode
public void sSetDSLStereotypesDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Description copied from interface: `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html#sSetDSLStereotypesDisplayMode(java.lang.String))`
Simple sets (no updates) DSL stereotypes display mode.
Specified by:
`[sSetDSLStereotypesDisplayMode](shapes/StereotypesDisplayModeOwner.html#sSetDSLStereotypesDisplayMode(java.lang.String))` in interface `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`
Parameters:
`mode` - stereotypes display mode value.
setDSLStereotypesDisplayMode
public void setDSLStereotypesDisplayMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Description copied from interface: `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html#setDSLStereotypesDisplayMode(java.lang.String))`
Sets DSL stereotype display mode value.
Specified by:
`[setDSLStereotypesDisplayMode](shapes/StereotypesDisplayModeOwner.html#setDSLStereotypesDisplayMode(java.lang.String))` in interface `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`
Parameters:
`mode` - stereotype display mode.
isAutosized
public boolean isAutosized()
sSetAutosize
public void sSetAutosize(boolean val)
setAutosize
public void setAutosize(boolean val)
updateFrameSize
public void updateFrameSize([PresentationElement](PresentationElement.html) element)
Overrides:
`[updateFrameSize](AbstractDiagramPresentationElement.html#updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
isUseFlowLayoutLogic
public boolean isUseFlowLayoutLogic()
Indicates if smart path/shape edit should be used in this diagram.
Overrides:
`[isUseFlowLayoutLogic](AbstractDiagramPresentationElement.html#isUseFlowLayoutLogic())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Returns:
true if smart symbol editing should be used, false otherwise.
clearCaches
protected void clearCaches()
Overrides:
`[clearCaches](AbstractDiagramPresentationElement.html#clearCaches())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
isInitialFrameSizeSet
@OpenApipublic boolean isInitialFrameSizeSet()
Returns:
false if diagram frame size should not be recalculated on opening.
setInitialFrameSizeSet
@OpenApipublic void setInitialFrameSizeSet(boolean value)
Set a flag that diagram frame size should not be recalculated on opening.
Parameters:
`value` - new value
hasHeavyWeightSymbols
public boolean hasHeavyWeightSymbols()
Check is diagram has heavyweight symbols - symbols those can be painted correctly only if diagram is displayed in some JComponent
Returns:
true if heavyweight symbols exists in the diagram
registerHeavyWeightSymbolsChecker
public static void registerHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)
unRegisterHeavyWeightSymbolsChecker
public static void unRegisterHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)
sSetSuspendShapeAutoResizeMode
public void sSetSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Overrides:
`[sSetSuspendShapeAutoResizeMode](AbstractDiagramPresentationElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
setSuspendShapeAutoResizeMode
public void setSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
Overrides:
`[setSuspendShapeAutoResizeMode](AbstractDiagramPresentationElement.html#setSuspendShapeAutoResizeMode(java.lang.String))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
internalClearOnUnload
protected void internalClearOnUnload()
Overrides:
`[internalClearOnUnload](AbstractDiagramPresentationElement.html#internalClearOnUnload())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
getRepresentationFromModelElement
public com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject getRepresentationFromModelElement()
Specified by:
`[getRepresentationFromModelElement](AbstractDiagramPresentationElement.html#getRepresentationFromModelElement())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
postOpenFromCommand
public void postOpenFromCommand()
Overrides:
`[postOpenFromCommand](AbstractDiagramPresentationElement.html#postOpenFromCommand())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
sSetForceStoreContentOnSave
protected void sSetForceStoreContentOnSave(boolean forceStoreContentOnSave)
Overrides:
`[sSetForceStoreContentOnSave](AbstractDiagramPresentationElement.html#sSetForceStoreContentOnSave(boolean))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
get
@OpenApipublic static [DiagramPresentationElement](DiagramPresentationElement.html) get([PresentationElement](PresentationElement.html) symbol)
Returns diagram of given presentation element.
Returns:
diagram of given presentation element.
layout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public boolean layout(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) layouter)
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))`
Layouts the diagram with the specified layouter.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List))} to select symbols in the diagram.
Specified by:
`[layout](AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Parameters:
`useCommands` - true to create commands. If true, this command will be available in the project's command history
`layouter` - layouter to be used for layouting
Returns:
true if layout was performed.
getDefaultDiagramLayouter
public [DiagramLayouter](layout/DiagramLayouter.html) getDefaultDiagramLayouter()
Specified by:
`[getDefaultDiagramLayouter](AbstractDiagramPresentationElement.html#getDefaultDiagramLayouter())` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class DiagramPresentationElement">Class DiagramPresentationElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</code>, <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code>, <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramPresentationElement</span>
<span class="extends-implements">extends <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>
implements com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner, <a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a>, com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer, com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</span></div>
<div class="block">Class for representing UML diagram. Diagram purpose is to contain set of presentation elements.<br/>
 For diagram creation use <a href="../../openapi/uml/ModelElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>ModelElementsManager</code></a> class.<br/>
 For working with diagram presentation elements use
 <a href="../../openapi/uml/PresentationElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>PresentationElementsManager</code></a> class.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../openapi/uml/ModelElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>ModelElementsManager</code></a></li>
<li><a href="../../openapi/uml/PresentationElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>PresentationElementsManager</code></a></li>
</ul>
</dd>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_USE_STEREOTYPE_MODES">DIAGRAM_USE_STEREOTYPE_MODES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Diagram use stereotype modes.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></h3>
<code><a href="AbstractDiagramPresentationElement.html#CANVAS_SIZE">CANVAS_SIZE</a>, <a href="AbstractDiagramPresentationElement.html#DEFAULT_GRID_SIZE">DEFAULT_GRID_SIZE</a>, <a href="AbstractDiagramPresentationElement.html#DIAGRAM_CONTENT_LOADED_PROPERTY">DIAGRAM_CONTENT_LOADED_PROPERTY</a>, <a href="AbstractDiagramPresentationElement.html#DIAGRAM_ORIENTATION_HORIZONTAL">DIAGRAM_ORIENTATION_HORIZONTAL</a>, <a href="AbstractDiagramPresentationElement.html#DIAGRAM_ORIENTATION_MODES">DIAGRAM_ORIENTATION_MODES</a>, <a href="AbstractDiagramPresentationElement.html#DIAGRAM_ORIENTATION_VERTICAL">DIAGRAM_ORIENTATION_VERTICAL</a>, <a href="AbstractDiagramPresentationElement.html#FORCE_CONTENT_SAVE_PROPERTY">FORCE_CONTENT_SAVE_PROPERTY</a>, <a href="AbstractDiagramPresentationElement.html#MAX_GRID_SIZE">MAX_GRID_SIZE</a>, <a href="AbstractDiagramPresentationElement.html#MIN_GRID_SIZE">MIN_GRID_SIZE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="PresentationElement.html#DEFAULT_LINE_WIDTH">DEFAULT_LINE_WIDTH</a>, <a href="PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="PresentationElement.html#HANDLE_SIZE">HANDLE_SIZE</a>, <a href="PresentationElement.html#MAX_LINE_WIDTH">MAX_LINE_WIDTH</a>, <a href="PresentationElement.html#MIN_LINE_WIDTH">MIN_LINE_WIDTH</a>, <a href="PresentationElement.html#peStyle">peStyle</a>, <a href="PresentationElement.html#SHADOW_WIDTH">SHADOW_WIDTH</a>, <a href="PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.StereotypesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.<a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></h3>
<code><a href="shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL">DSL_STEREOTYPE_DISPLAY_MODE_ALL</a>, <a href="shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST">DSL_STEREOTYPE_DISPLAY_MODE_LAST</a>, <a href="shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE">DSL_STEREOTYPE_DISPLAY_MODE_NONE</a>, <a href="shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES">DSL_STEREOTYPE_DISPLAY_MODES</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES">STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON">STEREOTYPE_DISPLAY_MODE_ICON</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT">STEREOTYPE_DISPLAY_MODE_TEXT</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON">STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES">STEREOTYPES_DISPLAY_MODES</a>, <a href="shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE">STEREOTYPES_DISPLAY_MODES_SIMPLE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramPresentationElement</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new empty diagram.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">DiagramPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject)">DiagramPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.uml.DiagramType)">DiagramPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramCreationInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">addDiagramCreationInfo</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addDiagramCreationInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean)">addDiagramCreationInfo</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 boolean overwrite)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#applyForcedProperties()">applyForcedProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties stored in default style for diagram and marked as forced.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Object view has no children.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCaches()">clearCaches</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagramInfoShape(boolean)">createDiagramInfoShape</a><wbr/>(boolean simple)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get(com.nomagic.magicdraw.uml.symbols.PresentationElement)">get</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns diagram of given presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAspectRatioMode()">getAspectRatioMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainer()">getContainer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentDate()">getCurrentDate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultDiagramLayouter()">getDefaultDiagramLayouter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultStyleForDiagram(com.nomagic.magicdraw.properties.StyleManager)">getDefaultStyleForDiagram</a><wbr/>(<a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> styleManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds style for this diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultStyleID()">getDefaultStyleID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagram()">getDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Diagram model element of this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="shapes/DiagramFrameView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramFrameView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramFrame()">getDiagramFrame</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the frame of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramPropertiesShape()">getDiagramPropertiesShape</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType()">getDiagramType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramTypeAsString()">getDiagramTypeAsString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDSLStereotypesDisplayMode()">getDSLStereotypesDisplayMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets DSL stereotype display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanType()">getHumanType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns human representation of the data type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the name of this <code>DiagramPresentationElement</code> object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRealType()">getRealType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns real diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationFromModelElement()">getRepresentationFromModelElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypesDisplayMode()">getStereotypesDisplayMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets setereotypes display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedModelElements()">getUsedModelElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns collection of model elements that have views in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getUsedModelElements(boolean)">getUsedModelElements</a><wbr/>(boolean checkOnlyPersistent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">checkOnlyPersistent parameter is ignored.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getUsedModelElements(boolean,boolean)">getUsedModelElements</a><wbr/>(boolean checkOnlyPersistent,
 boolean checkOnlyFriendly)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">checkOnlyPersistent and checkOnlyFriendly parameters are ignored.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedModelElements(com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">getUsedModelElements</a><wbr/>(<a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns collection of model elements that are used in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseStereotypeMode()">getUseStereotypeMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram use stereotype mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasHeavyWeightSymbols()">hasHeavyWeightSymbols</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check is diagram has heavyweight symbols - symbols those can be painted correctly only if diagram is displayed in some JComponent</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasManipulationSortManager()">hasManipulationSortManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasNoRegisteredRealTypeDescriptor()">hasNoRegisteredRealTypeDescriptor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalAddToCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,java.lang.String)">internalAddToCache</a><wbr/>(<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalClearOnUnload()">internalClearOnUnload</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalRemoveFromCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">internalRemoveFromCache</a><wbr/>(<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSetDiagramType(java.lang.String,java.lang.String)">internalSetDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramUmlType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSilentApply()">internalSilentApply</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutosized()">isAutosized</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isElementInDiagram</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element exist in any diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">isElementInDiagram</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean skipProxyCheck,
 <a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element exist in any diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">isElementInDiagram</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element exist in any diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInitialFrameSizeSet()">isInitialFrameSizeSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isModificationTimeUpdateDisabled()">isModificationTimeUpdateDisabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if automatic diagram modification time update is disabled</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowAbbreviatedDiagramType()">isShowAbbreviatedDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowActivations()">isShowActivations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowContextKind()">isShowContextKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowContextName()">isShowContextName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowContextType()">isShowContextType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramFrame()">isShowDiagramFrame</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramInfo()">isShowDiagramInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramName()">isShowDiagramName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramOwner()">isShowDiagramOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramType()">isShowDiagramType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowMessageNumbers()">isShowMessageNumbers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowParameters()">isShowParameters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseAdvancedNumbering()">isUseAdvancedNumbering</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseFlowLayoutLogic()">isUseFlowLayoutLogic</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if smart path/shape edit should be used in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">layout</a><wbr/>(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onFontChange()">onFontChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#positionDiagramInfoShapeOnFrame(com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape)">positionDiagramInfoShapeOnFrame</a><wbr/>(<a href="shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a> shape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#postOpenFromCommand()">postOpenFromCommand</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferredSize(java.awt.Dimension)">preferredSize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dim)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker)">registerHeavyWeightSymbolsChecker</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetLastModificationUpdateTime()">resetLastModificationUpdateTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reset cached last diagram modification time.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAspectRatioMode(java.lang.String)">setAspectRatioMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutosize(boolean)">setAutosize</a><wbr/>(boolean val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultStyleID(java.lang.String)">setDefaultStyleID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new diagram style id to representation object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramOrientationMode(java.lang.String)">setDiagramOrientationMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram orientation mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramType(com.nomagic.magicdraw.uml.DiagramType)">setDiagramType</a><wbr/>(<a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the type of the diagram and fires
 the property change event with name ExtendedPropertyNames.EDIT_DIAGRAM_TYPE .</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDSLStereotypesDisplayMode(java.lang.String)">setDSLStereotypesDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets DSL stereotype display mode value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitialDiagramFrameBounds()">setInitialDiagramFrameBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets initial diagram frame bounds for this diagram's frame.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitialFrameSizeSet(boolean)">setInitialFrameSizeSet</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a flag that diagram frame size should not be recalculated on opening.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModificationTimeUpdateDisabled(boolean)">setModificationTimeUpdateDisabled</a><wbr/>(boolean modificationTimeUpdateDisabled)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disables automatic diagram modification time update.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRealType(java.lang.String)">setRealType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> realType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If diagram type is not registered then known type is set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowAbbreviatedDiagramType(boolean)">setShowAbbreviatedDiagramType</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowActivations(boolean)">setShowActivations</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowContextKind(boolean)">setShowContextKind</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowContextName(boolean)">setShowContextName</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowContextType(boolean)">setShowContextType</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDiagramFrame(boolean)">setShowDiagramFrame</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDiagramInfo(boolean)">setShowDiagramInfo</a><wbr/>(boolean showDiagramInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDiagramName(boolean)">setShowDiagramName</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDiagramOwner(boolean)">setShowDiagramOwner</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDiagramType(boolean)">setShowDiagramType</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowMessageNumbers(boolean)">setShowMessageNumbers</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowParameters(boolean)">setShowParameters</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypesDisplayMode(java.lang.String)">setStereotypesDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets stereotype display mode value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseAdvancedNumbering(boolean)">setUseAdvancedNumbering</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseStereotypeMode(java.lang.String)">setUseStereotypeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram use stereotype mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetAspectRatioMode(java.lang.String)">sSetAspectRatioMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetAutosize(boolean)">sSetAutosize</a><wbr/>(boolean val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">sSetDiagramFrame</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView diagramFrame)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetDiagramOrientationMode(java.lang.String)">sSetDiagramOrientationMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Simple set for diagram orientation mode property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetDiagramType(com.nomagic.magicdraw.uml.DiagramType)">sSetDiagramType</a><wbr/>(<a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the type of the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetDSLStereotypesDisplayMode(java.lang.String)">sSetDSLStereotypesDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Simple sets (no updates) DSL stereotypes display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets diagram element for this object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetForceStoreContentOnSave(boolean)">sSetForceStoreContentOnSave</a><wbr/>(boolean forceStoreContentOnSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowAbbreviatedDiagramType(boolean)">sSetShowAbbreviatedDiagramType</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowActivations(boolean)">sSetShowActivations</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowContextKind(boolean)">sSetShowContextKind</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowContextName(boolean)">sSetShowContextName</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowContextType(boolean)">sSetShowContextType</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowDiagramFrame(boolean)">sSetShowDiagramFrame</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowDiagramInfo(boolean)">sSetShowDiagramInfo</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowDiagramName(boolean)">sSetShowDiagramName</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowDiagramOwner(boolean)">sSetShowDiagramOwner</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowDiagramType(boolean)">sSetShowDiagramType</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowParameters(boolean)">sSetShowParameters</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetStereotypesDisplayMode(java.lang.String)">sSetStereotypesDisplayMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Simple sets (no updates) stereotypes display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetUseStereotypeMode(java.lang.String)">sSetUseStereotypeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Simple set for diagram use stereotype mode property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unRegisterHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker)">unRegisterHeavyWeightSymbolsChecker</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateDiagramPropertiesShapeModificationTime()">updateDiagramPropertiesShapeModificationTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateFrameSize</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></h3>
<code><a href="AbstractDiagramPresentationElement.html#addContentPropertyChangeListener(java.beans.PropertyChangeListener)">addContentPropertyChangeListener</a>, <a href="AbstractDiagramPresentationElement.html#addDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)">addDynamicRepresentationProvider</a>, <a href="AbstractDiagramPresentationElement.html#addDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)">addDynamicStyleProvider</a>, <a href="AbstractDiagramPresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="AbstractDiagramPresentationElement.html#adjustInitialDiagramFrameBounds(java.awt.Rectangle)">adjustInitialDiagramFrameBounds</a>, <a href="AbstractDiagramPresentationElement.html#atInsert()">atInsert</a>, <a href="AbstractDiagramPresentationElement.html#autosizeSuspendedSymbolsWithHiddenContent()">autosizeSuspendedSymbolsWithHiddenContent</a>, <a href="AbstractDiagramPresentationElement.html#calculateInitialDiagramFrameBounds()">calculateInitialDiagramFrameBounds</a>, <a href="AbstractDiagramPresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a>, <a href="AbstractDiagramPresentationElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a>, <a href="AbstractDiagramPresentationElement.html#cleanupAfterLoad()">cleanupAfterLoad</a>, <a href="AbstractDiagramPresentationElement.html#close()">close</a>, <a href="AbstractDiagramPresentationElement.html#close(boolean)">close</a>, <a href="AbstractDiagramPresentationElement.html#collectPresentationElementsRecursively()">collectPresentationElementsRecursively</a>, <a href="AbstractDiagramPresentationElement.html#collectShowingManipulatedElementsRecursively()">collectShowingManipulatedElementsRecursively</a>, <a href="AbstractDiagramPresentationElement.html#collectShowingPresentationElementsRecursively()">collectShowingPresentationElementsRecursively</a>, <a href="AbstractDiagramPresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a>, <a href="AbstractDiagramPresentationElement.html#dispose()">dispose</a>, <a href="AbstractDiagramPresentationElement.html#ensureLoaded()">ensureLoaded</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">findPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">findPresentationElementForPathConnecting</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElements(java.lang.Class)">findPresentationElements</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElements(java.util.function.Predicate)">findPresentationElements</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElementsForPathConnecting</a>, <a href="AbstractDiagramPresentationElement.html#fireContentPropertyChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.lang.Object,java.lang.Object)">fireContentPropertyChange</a>, <a href="AbstractDiagramPresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="AbstractDiagramPresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#getBackgroundColor()">getBackgroundColor</a>, <a href="AbstractDiagramPresentationElement.html#getBounds()">getBounds</a>, <a href="AbstractDiagramPresentationElement.html#getCenterlineManager()">getCenterlineManager</a>, <a href="AbstractDiagramPresentationElement.html#getContentHash()">getContentHash</a>, <a href="AbstractDiagramPresentationElement.html#getContentState()">getContentState</a>, <a href="AbstractDiagramPresentationElement.html#getDiagramOrientationMode()">getDiagramOrientationMode</a>, <a href="AbstractDiagramPresentationElement.html#getDynamicRepresentationProviders()">getDynamicRepresentationProviders</a>, <a href="AbstractDiagramPresentationElement.html#getDynamicStyleProviders()">getDynamicStyleProviders</a>, <a href="AbstractDiagramPresentationElement.html#getGridSize()">getGridSize</a>, <a href="AbstractDiagramPresentationElement.html#getID()">getID</a>, <a href="AbstractDiagramPresentationElement.html#getLineJumpPlace()">getLineJumpPlace</a>, <a href="AbstractDiagramPresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a>, <a href="AbstractDiagramPresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="AbstractDiagramPresentationElement.html#getManipulationSortManager()">getManipulationSortManager</a>, <a href="AbstractDiagramPresentationElement.html#getOpenConfigurator()">getOpenConfigurator</a>, <a href="AbstractDiagramPresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="AbstractDiagramPresentationElement.html#getPathGridSize()">getPathGridSize</a>, <a href="AbstractDiagramPresentationElement.html#getPathToMoveCache()">getPathToMoveCache</a>, <a href="AbstractDiagramPresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="AbstractDiagramPresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="AbstractDiagramPresentationElement.html#getPresentationElements()">getPresentationElements</a>, <a href="AbstractDiagramPresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="AbstractDiagramPresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="AbstractDiagramPresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="AbstractDiagramPresentationElement.html#getRepresentation()">getRepresentation</a>, <a href="AbstractDiagramPresentationElement.html#getSortManager()">getSortManager</a>, <a href="AbstractDiagramPresentationElement.html#getSortManagers(boolean)">getSortManagers</a>, <a href="AbstractDiagramPresentationElement.html#getSurfaces()">getSurfaces</a>, <a href="AbstractDiagramPresentationElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="AbstractDiagramPresentationElement.html#getValue(java.lang.Object)">getValue</a>, <a href="AbstractDiagramPresentationElement.html#getValueOrCompute(java.lang.Object,java.util.function.Supplier)">getValueOrCompute</a>, <a href="AbstractDiagramPresentationElement.html#getVisibleBounds()">getVisibleBounds</a>, <a href="AbstractDiagramPresentationElement.html#getZoom()">getZoom</a>, <a href="AbstractDiagramPresentationElement.html#hasSelectableSymbols()">hasSelectableSymbols</a>, <a href="AbstractDiagramPresentationElement.html#hasVerticalOrientation()">hasVerticalOrientation</a>, <a href="AbstractDiagramPresentationElement.html#initialize()">initialize</a>, <a href="AbstractDiagramPresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a>, <a href="AbstractDiagramPresentationElement.html#isDummyMode()">isDummyMode</a>, <a href="AbstractDiagramPresentationElement.html#isEmpty()">isEmpty</a>, <a href="AbstractDiagramPresentationElement.html#isForceStoreContentOnSave()">isForceStoreContentOnSave</a>, <a href="AbstractDiagramPresentationElement.html#isLabelsAutoDisplaySuspended()">isLabelsAutoDisplaySuspended</a>, <a href="AbstractDiagramPresentationElement.html#isLoaded()">isLoaded</a>, <a href="AbstractDiagramPresentationElement.html#isModified()">isModified</a>, <a href="AbstractDiagramPresentationElement.html#isOpening()">isOpening</a>, <a href="AbstractDiagramPresentationElement.html#isShapesAutoResizeSuspended()">isShapesAutoResizeSuspended</a>, <a href="AbstractDiagramPresentationElement.html#isShowGrid()">isShowGrid</a>, <a href="AbstractDiagramPresentationElement.html#isSnapToGridPaths()">isSnapToGridPaths</a>, <a href="AbstractDiagramPresentationElement.html#isSnapToGridShapes()">isSnapToGridShapes</a>, <a href="AbstractDiagramPresentationElement.html#isSymbolDiagram()">isSymbolDiagram</a>, <a href="AbstractDiagramPresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="AbstractDiagramPresentationElement.html#layout(boolean)">layout</a>, <a href="AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">layout</a>, <a href="AbstractDiagramPresentationElement.html#loadContents(com.nomagic.task.ProgressStatus)">loadContents</a>, <a href="AbstractDiagramPresentationElement.html#open()">open</a>, <a href="AbstractDiagramPresentationElement.html#open(boolean)">open</a>, <a href="AbstractDiagramPresentationElement.html#open(boolean,boolean)">open</a>, <a href="AbstractDiagramPresentationElement.html#open(boolean,boolean,boolean)">open</a>, <a href="AbstractDiagramPresentationElement.html#openInActiveTab(boolean)">openInActiveTab</a>, <a href="AbstractDiagramPresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a>, <a href="AbstractDiagramPresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a>, <a href="AbstractDiagramPresentationElement.html#recalculateInternalDataRequired()">recalculateInternalDataRequired</a>, <a href="AbstractDiagramPresentationElement.html#recursiveAutosize()">recursiveAutosize</a>, <a href="AbstractDiagramPresentationElement.html#registerInProject()">registerInProject</a>, <a href="AbstractDiagramPresentationElement.html#removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">removeContentPropertyChangeListener</a>, <a href="AbstractDiagramPresentationElement.html#removeDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)">removeDynamicRepresentationProvider</a>, <a href="AbstractDiagramPresentationElement.html#removeDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)">removeDynamicStyleProvider</a>, <a href="AbstractDiagramPresentationElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="AbstractDiagramPresentationElement.html#resetContainer()">resetContainer</a>, <a href="AbstractDiagramPresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#setBounds(java.awt.Rectangle)">setBounds</a>, <a href="AbstractDiagramPresentationElement.html#setContentHash(java.lang.String)">setContentHash</a>, <a href="AbstractDiagramPresentationElement.html#setDiagramRepresentationObject(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject)">setDiagramRepresentationObject</a>, <a href="AbstractDiagramPresentationElement.html#setDummyMode(boolean)">setDummyMode</a>, <a href="AbstractDiagramPresentationElement.html#setForceStoreContentOnSave(boolean)">setForceStoreContentOnSave</a>, <a href="AbstractDiagramPresentationElement.html#setGridSize(int)">setGridSize</a>, <a href="AbstractDiagramPresentationElement.html#setID(java.lang.String)">setID</a>, <a href="AbstractDiagramPresentationElement.html#setInitializer(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer)">setInitializer</a>, <a href="AbstractDiagramPresentationElement.html#setLabelsAutoDisplaySuspended(boolean)">setLabelsAutoDisplaySuspended</a>, <a href="AbstractDiagramPresentationElement.html#setModified(boolean)">setModified</a>, <a href="AbstractDiagramPresentationElement.html#setOpenConfigurator(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator)">setOpenConfigurator</a>, <a href="AbstractDiagramPresentationElement.html#setPresentationElements(java.util.List)">setPresentationElements</a>, <a href="AbstractDiagramPresentationElement.html#setShapesAutoResizeSuspended(boolean)">setShapesAutoResizeSuspended</a>, <a href="AbstractDiagramPresentationElement.html#setShowGrid(boolean)">setShowGrid</a>, <a href="AbstractDiagramPresentationElement.html#setSnapToGridPaths(boolean)">setSnapToGridPaths</a>, <a href="AbstractDiagramPresentationElement.html#setSnapToGridShapes(boolean)">setSnapToGridShapes</a>, <a href="AbstractDiagramPresentationElement.html#setUseGradientForFill(boolean)">setUseGradientForFill</a>, <a href="AbstractDiagramPresentationElement.html#setValue(java.lang.Object,T)">setValue</a>, <a href="AbstractDiagramPresentationElement.html#setZoomProvider(java.util.function.Function)">setZoomProvider</a>, <a href="AbstractDiagramPresentationElement.html#snapViewToGrid(com.nomagic.magicdraw.uml.symbols.PresentationElement)">snapViewToGrid</a>, <a href="AbstractDiagramPresentationElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="AbstractDiagramPresentationElement.html#sSetGridSize(int)">sSetGridSize</a>, <a href="AbstractDiagramPresentationElement.html#sSetLabelsAutoDisplaySuspended(boolean)">sSetLabelsAutoDisplaySuspended</a>, <a href="AbstractDiagramPresentationElement.html#sSetLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace)">sSetLineJumpPlace</a>, <a href="AbstractDiagramPresentationElement.html#sSetPresentationElements(java.util.List)">sSetPresentationElements</a>, <a href="AbstractDiagramPresentationElement.html#sSetShapesAutoResizeSuspended(boolean)">sSetShapesAutoResizeSuspended</a>, <a href="AbstractDiagramPresentationElement.html#sSetShowGrid(boolean)">sSetShowGrid</a>, <a href="AbstractDiagramPresentationElement.html#sSetSnapToGridPaths(boolean)">sSetSnapToGridPaths</a>, <a href="AbstractDiagramPresentationElement.html#sSetSnapToGridShapes(boolean)">sSetSnapToGridShapes</a>, <a href="AbstractDiagramPresentationElement.html#unloadDiagram()">unloadDiagram</a>, <a href="AbstractDiagramPresentationElement.html#unregisterFromProject()">unregisterFromProject</a>, <a href="AbstractDiagramPresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElementWithoutResize</a>, <a href="PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a>, <a href="PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBoundsForMoving</a>, <a href="PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="PresentationElement.html#autosizeAndResizeParent()">autosizeAndResizeParent</a>, <a href="PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a>, <a href="PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="PresentationElement.html#canFill()">canFill</a>, <a href="PresentationElement.html#canHavePaths()">canHavePaths</a>, <a href="PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="PresentationElement.html#checkShowsProxy()">checkShowsProxy</a>, <a href="PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="PresentationElement.html#clearShowsProxy()">clearShowsProxy</a>, <a href="PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="PresentationElement.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a>, <a href="PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="PresentationElement.html#generateID()">generateID</a>, <a href="PresentationElement.html#getActualElement()">getActualElement</a>, <a href="PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="PresentationElement.html#getFillColor()">getFillColor</a>, <a href="PresentationElement.html#getFont()">getFont</a>, <a href="PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="PresentationElement.html#getHumanName()">getHumanName</a>, <a href="PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="PresentationElement.html#getLineColor()">getLineColor</a>, <a href="PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="PresentationElement.html#getManipulationPreferredDimension()">getManipulationPreferredDimension</a>, <a href="PresentationElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="PresentationElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="PresentationElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="PresentationElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="PresentationElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="PresentationElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="PresentationElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="PresentationElement.html#getModelElement()">getModelElement</a>, <a href="PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="PresentationElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="PresentationElement.html#getParent()">getParent</a>, <a href="PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="PresentationElement.html#getPreferredBounds()">getPreferredBounds</a>, <a href="PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="PresentationElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementIndex</a>, <a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="PresentationElement.html#getRenderer()">getRenderer</a>, <a href="PresentationElement.html#getSelected()">getSelected</a>, <a href="PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="PresentationElement.html#getStroke(int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="PresentationElement.html#getStyle()">getStyle</a>, <a href="PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="PresentationElement.html#getTextColor()">getTextColor</a>, <a href="PresentationElement.html#getTolerance()">getTolerance</a>, <a href="PresentationElement.html#getVisibility()">getVisibility</a>, <a href="PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="PresentationElement.html#hasManipulator()">hasManipulator</a>, <a href="PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a>, <a href="PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="PresentationElement.html#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>, <a href="PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="PresentationElement.html#invalidate()">invalidate</a>, <a href="PresentationElement.html#isCanChildrenChangeEdge()">isCanChildrenChangeEdge</a>, <a href="PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="PresentationElement.html#isContentHidden()">isContentHidden</a>, <a href="PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="PresentationElement.html#isDetectable()">isDetectable</a>, <a href="PresentationElement.html#isDisposed()">isDisposed</a>, <a href="PresentationElement.html#isLayouting()">isLayouting</a>, <a href="PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="PresentationElement.html#isSelected()">isSelected</a>, <a href="PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="PresentationElement.html#isShowsProxy()">isShowsProxy</a>, <a href="PresentationElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="PresentationElement.html#isSortable()">isSortable</a>, <a href="PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="PresentationElement.html#isVisible()">isVisible</a>, <a href="PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="PresentationElement.html#movePathElements()">movePathElements</a>, <a href="PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="PresentationElement.html#onFind()">onFind</a>, <a href="PresentationElement.html#onFind(boolean)">onFind</a>, <a href="PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenBackground</a>, <a href="PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a>, <a href="PresentationElement.html#resizeParent()">resizeParent</a>, <a href="PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="PresentationElement.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="PresentationElement.html#setDummyResizeMode(boolean)">setDummyResizeMode</a>, <a href="PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="PresentationElement.html#setFillColor(java.awt.Color)">setFillColor</a>, <a href="PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="PresentationElement.html#setSize(int,int)">setSize</a>, <a href="PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="PresentationElement.html#setTextEditable(boolean)">setTextEditable</a>, <a href="PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="PresentationElement.html#silentApply()">silentApply</a>, <a href="PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="PresentationElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a>, <a href="PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="PresentationElement.html#update()">update</a>, <a href="PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="PresentationElement.html#updateLater()">updateLater</a>, <a href="PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="PresentationElement.html#useParentProperties()">useParentProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, setResourceIDProvider, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../MDElement.html#getProject()">getProject</a></code></div>
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
<section class="detail" id="DIAGRAM_USE_STEREOTYPE_MODES">
<h3>DIAGRAM_USE_STEREOTYPE_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">DIAGRAM_USE_STEREOTYPE_MODES</span></div>
<div class="block">Diagram use stereotype modes.</div>
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
<h3>DiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DiagramPresentationElement</span>()</div>
<div class="block">Constructs new empty diagram.
 Do not use this constructor to create a diagram explicitly.
 Open API provides method for diagrams creation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../openapi/uml/ModelElementsManager.html#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)"><code>ModelElementsManager.createDiagram(String, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>DiagramPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.uml.DiagramType)">
<h3>DiagramPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 @CheckForNull
 <a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject)">
<h3>DiagramPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 @CheckForNull
 com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)</span></div>
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
<section class="detail" id="internalAddToCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,java.lang.String)">
<h3>internalAddToCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalAddToCache</span><wbr/><span class="parameters">(<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#internalAddToCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,java.lang.String)">internalAddToCache</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalRemoveFromCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>internalRemoveFromCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalRemoveFromCache</span><wbr/><span class="parameters">(<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#internalRemoveFromCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">internalRemoveFromCache</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNoRegisteredRealTypeDescriptor()">
<h3>hasNoRegisteredRealTypeDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasNoRegisteredRealTypeDescriptor</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#hasNoRegisteredRealTypeDescriptor()">hasNoRegisteredRealTypeDescriptor</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetDiagramType(com.nomagic.magicdraw.uml.DiagramType)">
<h3>sSetDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetDiagramType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
<div class="block">Sets the type of the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type of the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramType(com.nomagic.magicdraw.uml.DiagramType)">
<h3>setDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramType</span><wbr/><span class="parameters">(<a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
<div class="block">Sets the type of the diagram and fires
 the property change event with name ExtendedPropertyNames.EDIT_DIAGRAM_TYPE .</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type of the diagram</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../ExtendedPropertyNames.html#EDIT_DIAGRAM_TYPE"><code>ExtendedPropertyNames.EDIT_DIAGRAM_TYPE</code></a></li>
<li><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core"><code>Project</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalSetDiagramType(java.lang.String,java.lang.String)">
<h3>internalSetDiagramType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalSetDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramUmlType)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#internalSetDiagramType(java.lang.String,java.lang.String)">internalSetDiagramType</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramType()">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">getDiagramType</span>()</div>
<div class="block">Returns the type of the diagram.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getDiagramType()">getDiagramType</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>the type of the diagram</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM"><code>DiagramTypes.UML_CLASS_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM"><code>DiagramTypes.UML_USECASE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM"><code>DiagramTypes.UML_COMMUNICATION_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM"><code>DiagramTypes.UML_SEQUENCE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM"><code>DiagramTypes.UML_STATECHART_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM"><code>DiagramTypes.UML_PROTOCOL_STATE_MACHINE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM"><code>DiagramTypes.UML_ACTIVITY_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM"><code>DiagramTypes.UML_COMPOSITE_STRUCTURE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM"><code>DiagramTypes.UML_OBJECT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM"><code>DiagramTypes.UML_PACKAGE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM"><code>DiagramTypes.UML_COMPONENT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM"><code>DiagramTypes.UML_DEPLOYMENT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM"><code>DiagramTypes.UML_PROFILE_DIAGRAM</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanType()">
<h3>getHumanType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanType</span>()</div>
<div class="block">Returns human representation of the data type</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#getHumanType()">getHumanType</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getHumanType()">getHumanType</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>the name of the data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#clone()">clone</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagram()">
<h3>getDiagram</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">getDiagram</span>()</div>
<div class="block">Returns Diagram model element of this presentation element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Diagram object of this element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getElement()"><code>getElement()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">getElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getElement()">PresentationElement</a></code></span></div>
<div class="block">Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ModelElementProvider.html#getElement()">getElement</a></code> in interface <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getElement()">getElement</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>model element of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">PresentationElement</a></code></span></div>
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.
 See "Visitor" pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramTypeAsString()">
<h3>getDiagramTypeAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramTypeAsString</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getDiagramTypeAsString()">getDiagramTypeAsString</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Gets the name of this <code>DiagramPresentationElement</code> object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../MDElement.html#getName()">getName</a></code> in interface <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../utils/NameOwner.html#getName()">getName</a></code> in interface <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getName</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>name of this object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowDiagramOwner(boolean)">
<h3>sSetShowDiagramOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowDiagramOwner</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowAbbreviatedDiagramType(boolean)">
<h3>sSetShowAbbreviatedDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowAbbreviatedDiagramType</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowDiagramName(boolean)">
<h3>sSetShowDiagramName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowDiagramName</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowParameters(boolean)">
<h3>sSetShowParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowParameters</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowContextName(boolean)">
<h3>sSetShowContextName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowContextName</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowContextType(boolean)">
<h3>sSetShowContextType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowContextType</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowDiagramType(boolean)">
<h3>sSetShowDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowDiagramType</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowContextKind(boolean)">
<h3>sSetShowContextKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowContextKind</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowAbbreviatedDiagramType(boolean)">
<h3>setShowAbbreviatedDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowAbbreviatedDiagramType</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowDiagramName(boolean)">
<h3>setShowDiagramName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDiagramName</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowParameters(boolean)">
<h3>setShowParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowParameters</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowContextName(boolean)">
<h3>setShowContextName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowContextName</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowContextType(boolean)">
<h3>setShowContextType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowContextType</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowDiagramType(boolean)">
<h3>setShowDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDiagramType</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowContextKind(boolean)">
<h3>setShowContextKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowContextKind</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowAbbreviatedDiagramType()">
<h3>isShowAbbreviatedDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowAbbreviatedDiagramType</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowAbbreviatedDiagramType</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramName()">
<h3>isShowDiagramName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramName</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowDiagramName</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowParameters()">
<h3>isShowParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowParameters</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowParameters</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowContextName()">
<h3>isShowContextName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowContextName</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowContextName</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowContextType()">
<h3>isShowContextType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowContextType</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowContextType</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramType()">
<h3>isShowDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramType</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowDiagramType</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowContextKind()">
<h3>isShowContextKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowContextKind</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isShowContextKind</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowDiagramFrame(boolean)">
<h3>sSetShowDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowDiagramFrame</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramOwner()">
<h3>isShowDiagramOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramOwner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramFrame()">
<h3>isShowDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramFrame</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#isShowDiagramFrame()">isShowDiagramFrame</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowDiagramOwner(boolean)">
<h3>setShowDiagramOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDiagramOwner</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowDiagramFrame(boolean)">
<h3>setShowDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDiagramFrame</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>sSetElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Sets diagram element for this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Object view has no children.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasManipulationSortManager()">
<h3>hasManipulationSortManager</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasManipulationSortManager</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#hasManipulationSortManager()">hasManipulationSortManager</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onFontChange()">
<h3>onFontChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onFontChange</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#onFontChange()">onFontChange</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowMessageNumbers(boolean)">
<h3>setShowMessageNumbers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowMessageNumbers</span><wbr/><span class="parameters">(boolean b)</span></div>
</section>
</li>
<li>
<section class="detail" id="setUseAdvancedNumbering(boolean)">
<h3>setUseAdvancedNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseAdvancedNumbering</span><wbr/><span class="parameters">(boolean b)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowMessageNumbers()">
<h3>isShowMessageNumbers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowMessageNumbers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isUseAdvancedNumbering()">
<h3>isUseAdvancedNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseAdvancedNumbering</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramInfo()">
<h3>isShowDiagramInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramInfo</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetShowDiagramInfo(boolean)">
<h3>sSetShowDiagramInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowDiagramInfo</span><wbr/><span class="parameters">(boolean b)</span></div>
</section>
</li>
<li>
<section class="detail" id="resetLastModificationUpdateTime()">
<h3>resetLastModificationUpdateTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetLastModificationUpdateTime</span>()</div>
<div class="block">Reset cached last diagram modification time.</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramPropertiesShape()">
<h3>getDiagramPropertiesShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a></span> <span class="element-name">getDiagramPropertiesShape</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setShowDiagramInfo(boolean)">
<h3>setShowDiagramInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowDiagramInfo</span><wbr/><span class="parameters">(boolean showDiagramInfo)</span></div>
</section>
</li>
<li>
<section class="detail" id="createDiagramInfoShape(boolean)">
<h3>createDiagramInfoShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createDiagramInfoShape</span><wbr/><span class="parameters">(boolean simple)</span></div>
</section>
</li>
<li>
<section class="detail" id="positionDiagramInfoShapeOnFrame(com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape)">
<h3>positionDiagramInfoShapeOnFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">positionDiagramInfoShapeOnFrame</span><wbr/><span class="parameters">(<a href="shapes/DiagramPropertiesShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramPropertiesShape</a> shape)</span></div>
</section>
</li>
<li>
<section class="detail" id="addDiagramCreationInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>addDiagramCreationInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addDiagramCreationInfo</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="addDiagramCreationInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,boolean)">
<h3>addDiagramCreationInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addDiagramCreationInfo</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 boolean overwrite)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetShowActivations(boolean)">
<h3>sSetShowActivations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowActivations</span><wbr/><span class="parameters">(boolean b)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowActivations(boolean)">
<h3>setShowActivations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowActivations</span><wbr/><span class="parameters">(boolean b)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowActivations()">
<h3>isShowActivations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowActivations</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetDiagramOrientationMode(java.lang.String)">
<h3>sSetDiagramOrientationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetDiagramOrientationMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block">Simple set for diagram orientation mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mode</code> - - diagram orientation mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramOrientationMode(java.lang.String)">
<h3>setDiagramOrientationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramOrientationMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block">Sets diagram orientation mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mode</code> - - diagram orientation mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetUseStereotypeMode(java.lang.String)">
<h3>sSetUseStereotypeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetUseStereotypeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block">Simple set for diagram use stereotype mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mode</code> - - diagram orientation mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseStereotypeMode(java.lang.String)">
<h3>setUseStereotypeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseStereotypeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block">Sets diagram use stereotype mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mode</code> - - diagram orientation mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseStereotypeMode()">
<h3>getUseStereotypeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUseStereotypeMode</span>()</div>
<div class="block">Gets diagram use stereotype mode.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getUseStereotypeMode</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
<dt>Returns:</dt>
<dd>diagram orientation mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAspectRatioMode()">
<h3>getAspectRatioMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAspectRatioMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAspectRatioMode(java.lang.String)">
<h3>setAspectRatioMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAspectRatioMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetAspectRatioMode(java.lang.String)">
<h3>sSetAspectRatioMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetAspectRatioMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
</section>
</li>
<li>
<section class="detail" id="internalSilentApply()">
<h3>internalSilentApply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalSilentApply</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#internalSilentApply()">PresentationElement</a></code></span></div>
<div class="block">Silently applies all properties after initialization</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#internalSilentApply()">internalSilentApply</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>internalApplyProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalApplyProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">PresentationElement</a></code></span></div>
<div class="block">Applies properties from given property manager</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preferredSize(java.awt.Dimension)">
<h3>preferredSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">preferredSize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dim)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#preferredSize(java.awt.Dimension)">preferredSize</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModificationTimeUpdateDisabled()">
<h3>isModificationTimeUpdateDisabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isModificationTimeUpdateDisabled</span>()</div>
<div class="block">Indicates if automatic diagram modification time update is disabled</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true when diagram modification time update is disabled</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModificationTimeUpdateDisabled(boolean)">
<h3>setModificationTimeUpdateDisabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModificationTimeUpdateDisabled</span><wbr/><span class="parameters">(boolean modificationTimeUpdateDisabled)</span></div>
<div class="block">Disables automatic diagram modification time update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modificationTimeUpdateDisabled</code> - true to disable automatic diagram modification time update.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateDiagramPropertiesShapeModificationTime()">
<h3>updateDiagramPropertiesShapeModificationTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateDiagramPropertiesShapeModificationTime</span>()</div>
</section>
</li>
<li>
<section class="detail" id="applyForcedProperties()">
<h3>applyForcedProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">applyForcedProperties</span>()</div>
<div class="block">Applies properties stored in default style for diagram and marked as forced.
 They can be marked as forced using  "apply" from styles dialog.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#applyForcedProperties()">applyForcedProperties</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedModelElements(boolean)">
<h3>getUsedModelElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUsedModelElements</span><wbr/><span class="parameters">(boolean checkOnlyPersistent)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">checkOnlyPersistent parameter is ignored. Use <a href="#getUsedModelElements()"><code>getUsedModelElements()</code></a></div>
</div>
<div class="block">Returns collection of model elements that are drawn in this diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>checkOnlyPersistent</code> - if true, result includes elements for symbols which are saved to XMI and not created at run-time. If false, includes all elements.</dd>
<dt>Returns:</dt>
<dd>collection of model elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedModelElements(boolean,boolean)">
<h3>getUsedModelElements</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUsedModelElements</span><wbr/><span class="parameters">(boolean checkOnlyPersistent,
 boolean checkOnlyFriendly)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">checkOnlyPersistent and checkOnlyFriendly parameters are ignored. Use <a href="#getUsedModelElements()"><code>getUsedModelElements()</code></a></div>
</div>
<div class="block">Returns collection of model elements that are drawn in this diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>checkOnlyPersistent</code> - if true, result includes elements for symbols which are saved to XMI and not created at run-time. If false, includes all elements.</dd>
<dd><code>checkOnlyFriendly</code> - check only "friendly" symbols</dd>
<dt>Returns:</dt>
<dd>collection of model elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedModelElements()">
<h3>getUsedModelElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUsedModelElements</span>()</div>
<div class="block">Returns collection of model elements that have views in this diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of model elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedModelElements(com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">
<h3>getUsedModelElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUsedModelElements</span><wbr/><span class="parameters">(<a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</span></div>
<div class="block">Returns collection of model elements that are used in this diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usedElementPolicy</code> - used element policy</dd>
<dt>Returns:</dt>
<dd>collection of model elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isElementInDiagram</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementInDiagram</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Checks if given element exist in any diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element exist in any diagram otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">
<h3>isElementInDiagram</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementInDiagram</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</span></div>
<div class="block">Checks if given element exist in any diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element exist in any diagram otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">
<h3>isElementInDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementInDiagram</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean skipProxyCheck,
 <a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</span></div>
<div class="block">Checks if given element exist in any diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>skipProxyCheck</code> - enables to skip if diagram's actual element is proxy</dd>
<dt>Returns:</dt>
<dd>true if element exist in any diagram otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefaultStyleID(java.lang.String)">
<h3>setDefaultStyleID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultStyleID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets new diagram style id to representation object</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - new id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultStyleID()">
<h3>getDefaultStyleID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefaultStyleID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the defaultStyleForDiagramID, can be null if default style is equal to diagram style, or diagram is loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultStyleForDiagram(com.nomagic.magicdraw.properties.StyleManager)">
<h3>getDefaultStyleForDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getDefaultStyleForDiagram</span><wbr/><span class="parameters">(<a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> styleManager)</span></div>
<div class="block">Finds style for this diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>styleManager</code> - manager to find in.</dd>
<dt>Returns:</dt>
<dd>found style, null if no style is created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealType()">
<h3>getRealType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRealType</span>()</div>
<div class="block">Returns real diagram type. Real diagram type is diagram type which is not registered but loaded from project file.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getRealType()">getRealType</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>real type. Can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRealType(java.lang.String)">
<h3>setRealType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRealType</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> realType)</span></div>
<div class="block">If diagram type is not registered then known type is set. Real type is preserved for saving.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>realType</code> - real diagram type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentDate()">
<h3>getCurrentDate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCurrentDate</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">
<h3>sSetDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetDiagramFrame</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView diagramFrame)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">sSetDiagramFrame</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramFrame()">
<h3>getDiagramFrame</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="shapes/DiagramFrameView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramFrameView</a></span> <span class="element-name">getDiagramFrame</span>()</div>
<div class="block">Get the frame of the diagram.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getDiagramFrame()">getDiagramFrame</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>frame of the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainer()">
<h3>getContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.DiagramObjectViewContainer</span> <span class="element-name">getContainer</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getContainer()">getContainer</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>diagram container</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitialDiagramFrameBounds()">
<h3>setInitialDiagramFrameBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitialDiagramFrameBounds</span>()</div>
<div class="block">Sets initial diagram frame bounds for this diagram's frame.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#setInitialDiagramFrameBounds()">setInitialDiagramFrameBounds</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypesDisplayMode()">
<h3>getStereotypesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypesDisplayMode</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></span></div>
<div class="block">Gets setereotypes display mode.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getStereotypesDisplayMode</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code></dd>
<dt>Specified by:</dt>
<dd><code><a href="shapes/StereotypesDisplayModeOwner.html#getStereotypesDisplayMode()">getStereotypesDisplayMode</a></code> in interface <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code></dd>
<dt>Returns:</dt>
<dd>stereotypes display mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetStereotypesDisplayMode(java.lang.String)">
<h3>sSetStereotypesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetStereotypesDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="shapes/StereotypesDisplayModeOwner.html#sSetStereotypesDisplayMode(java.lang.String)">StereotypesDisplayModeOwner</a></code></span></div>
<div class="block">Simple sets (no updates) stereotypes display mode.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="shapes/StereotypesDisplayModeOwner.html#sSetStereotypesDisplayMode(java.lang.String)">sSetStereotypesDisplayMode</a></code> in interface <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code></dd>
<dt>Parameters:</dt>
<dd><code>mode</code> - stereotypes display mode value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypesDisplayMode(java.lang.String)">
<h3>setStereotypesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStereotypesDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="shapes/StereotypesDisplayModeOwner.html#setStereotypesDisplayMode(java.lang.String)">StereotypesDisplayModeOwner</a></code></span></div>
<div class="block">Sets stereotype display mode value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="shapes/StereotypesDisplayModeOwner.html#setStereotypesDisplayMode(java.lang.String)">setStereotypesDisplayMode</a></code> in interface <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code></dd>
<dt>Parameters:</dt>
<dd><code>mode</code> - stereotype display mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDSLStereotypesDisplayMode()">
<h3>getDSLStereotypesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDSLStereotypesDisplayMode</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="shapes/StereotypesDisplayModeOwner.html#getDSLStereotypesDisplayMode()">StereotypesDisplayModeOwner</a></code></span></div>
<div class="block">Gets DSL stereotype display mode.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="shapes/StereotypesDisplayModeOwner.html#getDSLStereotypesDisplayMode()">getDSLStereotypesDisplayMode</a></code> in interface <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype display mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetDSLStereotypesDisplayMode(java.lang.String)">
<h3>sSetDSLStereotypesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetDSLStereotypesDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="shapes/StereotypesDisplayModeOwner.html#sSetDSLStereotypesDisplayMode(java.lang.String)">StereotypesDisplayModeOwner</a></code></span></div>
<div class="block">Simple sets (no updates) DSL stereotypes display mode.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="shapes/StereotypesDisplayModeOwner.html#sSetDSLStereotypesDisplayMode(java.lang.String)">sSetDSLStereotypesDisplayMode</a></code> in interface <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code></dd>
<dt>Parameters:</dt>
<dd><code>mode</code> - stereotypes display mode value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDSLStereotypesDisplayMode(java.lang.String)">
<h3>setDSLStereotypesDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDSLStereotypesDisplayMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="shapes/StereotypesDisplayModeOwner.html#setDSLStereotypesDisplayMode(java.lang.String)">StereotypesDisplayModeOwner</a></code></span></div>
<div class="block">Sets DSL stereotype display mode value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="shapes/StereotypesDisplayModeOwner.html#setDSLStereotypesDisplayMode(java.lang.String)">setDSLStereotypesDisplayMode</a></code> in interface <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code></dd>
<dt>Parameters:</dt>
<dd><code>mode</code> - stereotype display mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutosized()">
<h3>isAutosized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutosized</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetAutosize(boolean)">
<h3>sSetAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetAutosize</span><wbr/><span class="parameters">(boolean val)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutosize(boolean)">
<h3>setAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutosize</span><wbr/><span class="parameters">(boolean val)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>updateFrameSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateFrameSize</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateFrameSize</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseFlowLayoutLogic()">
<h3>isUseFlowLayoutLogic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseFlowLayoutLogic</span>()</div>
<div class="block">Indicates if smart path/shape edit should be used in this diagram.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#isUseFlowLayoutLogic()">isUseFlowLayoutLogic</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if smart symbol editing should be used, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCaches()">
<h3>clearCaches</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearCaches</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#clearCaches()">clearCaches</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInitialFrameSizeSet()">
<h3>isInitialFrameSizeSet</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInitialFrameSizeSet</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>false if diagram frame size should not be recalculated on opening.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitialFrameSizeSet(boolean)">
<h3>setInitialFrameSizeSet</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitialFrameSizeSet</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set a flag that diagram frame size should not be recalculated on opening.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasHeavyWeightSymbols()">
<h3>hasHeavyWeightSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasHeavyWeightSymbols</span>()</div>
<div class="block">Check is diagram has heavyweight symbols - symbols those can be painted correctly only if diagram is displayed in some JComponent</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if heavyweight symbols exists in the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker)">
<h3>registerHeavyWeightSymbolsChecker</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerHeavyWeightSymbolsChecker</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)</span></div>
</section>
</li>
<li>
<section class="detail" id="unRegisterHeavyWeightSymbolsChecker(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker)">
<h3>unRegisterHeavyWeightSymbolsChecker</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unRegisterHeavyWeightSymbolsChecker</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement.HeavyWeightSymbolsChecker checker)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetSuspendShapeAutoResizeMode(java.lang.String)">
<h3>sSetSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSuspendShapeAutoResizeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSuspendShapeAutoResizeMode(java.lang.String)">
<h3>setSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuspendShapeAutoResizeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalClearOnUnload()">
<h3>internalClearOnUnload</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalClearOnUnload</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#internalClearOnUnload()">internalClearOnUnload</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationFromModelElement()">
<h3>getRepresentationFromModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject</span> <span class="element-name">getRepresentationFromModelElement</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getRepresentationFromModelElement()">getRepresentationFromModelElement</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postOpenFromCommand()">
<h3>postOpenFromCommand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">postOpenFromCommand</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#postOpenFromCommand()">postOpenFromCommand</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetForceStoreContentOnSave(boolean)">
<h3>sSetForceStoreContentOnSave</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">sSetForceStoreContentOnSave</span><wbr/><span class="parameters">(boolean forceStoreContentOnSave)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#sSetForceStoreContentOnSave(boolean)">sSetForceStoreContentOnSave</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>get</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Returns diagram of given presentation element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram of given presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">AbstractDiagramPresentationElement</a></code></span></div>
<div class="block">Layouts the diagram with the specified layouter.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a>} to select symbols in the diagram.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">layout</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in the project's command history</dd>
<dd><code>layouter</code> - layouter to be used for layouting</dd>
<dt>Returns:</dt>
<dd>true if layout was performed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultDiagramLayouter()">
<h3>getDefaultDiagramLayouter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></span> <span class="element-name">getDefaultDiagramLayouter</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html#getDefaultDiagramLayouter()">getDefaultDiagramLayouter</a></code> in class <code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></dd>
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
