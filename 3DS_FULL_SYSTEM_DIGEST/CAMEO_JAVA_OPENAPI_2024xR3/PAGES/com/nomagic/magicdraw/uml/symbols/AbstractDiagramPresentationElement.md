# JAVA OPENAPI: AbstractDiagramPresentationElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html`
- source_sha256: `d4c3898a3f28ee110f479efda7a8e540128d8d7497d1afa8409ad9facfdedae7`
- captured_utc: `2026-07-14T16:55:58.020487+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class AbstractDiagramPresentationElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](PresentationElement.html)
com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement

All Implemented Interfaces:
`com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer`, `[BaseElement](../BaseElement.html)`, `[MDElement](../MDElement.html)`, `[ModelElementProvider](../ModelElementProvider.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[DiagramPresentationElement](DiagramPresentationElement.html)`

@OpenApipublic abstract classAbstractDiagramPresentationElement
extends [PresentationElement](PresentationElement.html)
implements com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[CANVAS_SIZE](#CANVAS_SIZE)`

`static final int`
`[DEFAULT_GRID_SIZE](#DEFAULT_GRID_SIZE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_CONTENT_LOADED_PROPERTY](#DIAGRAM_CONTENT_LOADED_PROPERTY)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ORIENTATION_HORIZONTAL](#DIAGRAM_ORIENTATION_HORIZONTAL)`
Horizontal diagram orientation mode.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[DIAGRAM_ORIENTATION_MODES](#DIAGRAM_ORIENTATION_MODES)`
Diagram orientation modes.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ORIENTATION_VERTICAL](#DIAGRAM_ORIENTATION_VERTICAL)`
Vertical diagram orientation mode.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FORCE_CONTENT_SAVE_PROPERTY](#FORCE_CONTENT_SAVE_PROPERTY)`

`static final int`
`[MAX_GRID_SIZE](#MAX_GRID_SIZE)`

`static final int`
`[MIN_GRID_SIZE](#MIN_GRID_SIZE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[DASHED_STROKE](PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](PresentationElement.html#MIN_LINE_WIDTH), [peStyle](PresentationElement.html#peStyle), [SHADOW_WIDTH](PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](PresentationElement.html#SOLID_STROKE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractDiagramPresentationElement](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`boolean`
`[addContentPropertyChangeListener](#addContentPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Registers the listener for changes in all symbols contained in the diagram.
`final void`
`[addDynamicRepresentationProvider](#addDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider))(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)`

`final void`
`[addDynamicStyleProvider](#addDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider))(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)`

`void`
`[addPresentationElement](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))([PresentationElement](PresentationElement.html) element,
 int index)`
Add given child to this symbol at given index
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) l)`
Just hack, registers the same listener to the container
`static void`
`[adjustInitialDiagramFrameBounds](#adjustInitialDiagramFrameBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Adjust initial diagram frame bounds.
`abstract void`
`[applyForcedProperties](#applyForcedProperties())()`

`void`
`[atInsert](#atInsert())()`
Invalidates object at insert
`void`
`[autosizeSuspendedSymbolsWithHiddenContent](#autosizeSuspendedSymbolsWithHiddenContent())()`

`protected [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[calculateInitialDiagramFrameBounds](#calculateInitialDiagramFrameBounds())()`
Gets bounds which should be set for the diagram's frame.
`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`
Check of given symbol can be added as child into this symbol.
`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`
Object view has no children.
`boolean`
`[canDeleteChild](#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) obj)`
Checks if given element can be deleted from this element.
`void`
`[cleanupAfterLoad](#cleanupAfterLoad())()`

`protected void`
`[clearCaches](#clearCaches())()`

`[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
`[clone](#clone())()`

`final void`
`[close](#close())()`
Closes diagram window.
`void`
`[close](#close(boolean))(boolean closeWindow)`
Closes opened diagram
 If closeWindow is 'false' and there is a possibility to back to the previous diagram in that window, when the previous diagram is opened
 Otherwise, diagram window is closed
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectPresentationElementsRecursively](#collectPresentationElementsRecursively())()`
Collects all elements in this diagram recursively.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectShowingManipulatedElementsRecursively](#collectShowingManipulatedElementsRecursively())()`
Collects all visible manipulated elements in this diagram recursively.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectShowingPresentationElementsRecursively](#collectShowingPresentationElementsRecursively())()`
Collects all visible elements in this diagram recursively.
`boolean`
`[coversPoint](#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks if object covers provided point
`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`void`
`[ensureLoaded](#ensureLoaded())()`
Ensures that the diagram is loaded.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds a presentation element for a given model element of the given symbol type in this diagram.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds a presentation element for a given model element of a given symbol type in this diagram.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElementForPathConnecting](#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class))([BaseElement](../BaseElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.
`final <S extends [PresentationElement](PresentationElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<S>`
`[findPresentationElements](#findPresentationElements(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<S> classType)`
Finds manipulated presentation elements matching given class type.
`final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[findPresentationElements](#findPresentationElements(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[PresentationElement](PresentationElement.html)> predicate)`
Finds manipulated presentation elements matching given predicate.
`final [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](PresentationElement.html)>`
`[findPresentationElementsForPathConnecting](#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.
`protected void`
`[fireContentPropertyChange](#fireContentPropertyChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.lang.Object,java.lang.Object))([PresentationElement](PresentationElement.html) source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
`[getAbstractDiagramPresentationElement](#getAbstractDiagramPresentationElement())()`
Returns diagram of this presentation element.
`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getBackgroundColor](#getBackgroundColor())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Delegate bounds request to its container.
`com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineManager`
`[getCenterlineManager](#getCenterlineManager())()`
Gets centerline manager for this diagram.
`com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer`
`[getContainer](#getContainer())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getContentHash](#getContentHash())()`

`final com.nomagic.magicdraw.uml.symbols.DiagramContentState`
`[getContentState](#getContentState())()`

`abstract [DiagramLayouter](layout/DiagramLayouter.html)`
`[getDefaultDiagramLayouter](#getDefaultDiagramLayouter())()`

`abstract com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
`[getDiagramFrame](#getDiagramFrame())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramOrientationMode](#getDiagramOrientationMode())()`
Gets diagram orientation mode.
`abstract [AbstractDiagramType](../AbstractDiagramType.html)`
`[getDiagramType](#getDiagramType())()`

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramTypeAsString](#getDiagramTypeAsString())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider>`
`[getDynamicRepresentationProviders](#getDynamicRepresentationProviders())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider>`
`[getDynamicStyleProviders](#getDynamicStyleProviders())()`

`int`
`[getGridSize](#getGridSize())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns the ID of the `Element`.
`com.nomagic.magicdraw.uml.symbols.LineJumpPlace`
`[getLineJumpPlace](#getLineJumpPlace())()`
Returns current line jump place value of the diagram.
`[PresentationElement](PresentationElement.html)`
`[getManipulatedElementAt](#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)`
Gets manipulate object view at specified point pt.
`[PresentationElement](PresentationElement.html)`
`[getManipulatedElementAt](#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)`
Gets manipulate symbol at specified point pt.
`com.dassault_systemes.modeler.magic.diagram.SortManager`
`[getManipulationSortManager](#getManipulationSortManager())()`
Returns manipulation sort manager for this diagram view.
`com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator`
`[getOpenConfigurator](#getOpenConfigurator())()`

`com.dassault_systemes.modeler.foundation.diagram.style.DiagramStylePropertyDelegate`
`[getOwnStyleDelegate](#getOwnStyleDelegate())()`

`float`
`[getPathGridSize](#getPathGridSize())()`

`com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.PathToMoveCache`
`[getPathToMoveCache](#getPathToMoveCache())()`

`[PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Searches and returns symbol that covers given point.
`[PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Gets object view at point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElements](#getPresentationElements())()`
Returns all children of this element
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Searches and returns all symbols that covers given point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)`
Gets object view at point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Gets object view at point.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRealType](#getRealType())()`
Returns real diagram type.
`com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject`
`[getRepresentation](#getRepresentation())()`

`abstract com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject`
`[getRepresentationFromModelElement](#getRepresentationFromModelElement())()`

`com.dassault_systemes.modeler.magic.diagram.SortManager`
`[getSortManager](#getSortManager())()`
Returns sort manager for this diagram view.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.dassault_systemes.modeler.magic.diagram.SortManager>`
`[getSortManagers](#getSortManagers(boolean))(boolean create)`
Gets sort managers registered for this diagram.
`final com.dassault_systemes.modeler.magic.diagram.DiagramSurfaces`
`[getSurfaces](#getSurfaces())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuspendShapeAutoResizeMode](#getSuspendShapeAutoResizeMode())()`

`<T> T`
`[getValue](#getValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) key)`

`<T> T`
`[getValueOrCompute](#getValueOrCompute(java.lang.Object,java.util.function.Supplier))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) key,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> valueSupplier)`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getVisibleBounds](#getVisibleBounds())()`
Returns user visible bounds of the diagram.
`float`
`[getZoom](#getZoom())()`

`protected boolean`
`[hasManipulationSortManager](#hasManipulationSortManager())()`

`protected boolean`
`[hasNoRegisteredRealTypeDescriptor](#hasNoRegisteredRealTypeDescriptor())()`

`boolean`
`[hasSelectableSymbols](#hasSelectableSymbols())()`

`boolean`
`[hasVerticalOrientation](#hasVerticalOrientation())()`
Returns true if diagram has vertical orientation.
`void`
`[initialize](#initialize())()`
Initialize symbol and its children state.
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

`protected abstract void`
`[internalSetDiagramType](#internalSetDiagramType(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) umlType)`

`void`
`[internalSilentApply](#internalSilentApply())()`
Silently applies all properties after initialization
`boolean`
`[intersects](#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks whether object intersects with given rectangle
`boolean`
`[isDummyMode](#isDummyMode())()`

`boolean`
`[isEmpty](#isEmpty())()`

`boolean`
`[isForceStoreContentOnSave](#isForceStoreContentOnSave())()`

`boolean`
`[isLabelsAutoDisplaySuspended](#isLabelsAutoDisplaySuspended())()`

`boolean`
`[isLoaded](#isLoaded())()`
Check if the diagram is loaded.
`boolean`
`[isModified](#isModified())()`

`boolean`
`[isOpening](#isOpening())()`

`boolean`
`[isShapesAutoResizeSuspended](#isShapesAutoResizeSuspended())()`

`boolean`
`[isShowDiagramFrame](#isShowDiagramFrame())()`

`boolean`
`[isShowGrid](#isShowGrid())()`

`boolean`
`[isSnapToGridPaths](#isSnapToGridPaths())()`

`boolean`
`[isSnapToGridShapes](#isSnapToGridShapes())()`

`boolean`
`[isSymbolDiagram](#isSymbolDiagram())()`
Checks if diagram displays symbols as its contents.
`boolean`
`[isUseFlowLayoutLogic](#isUseFlowLayoutLogic())()`

`boolean`
`[isUseGradientForFill](#isUseGradientForFill())()`
Do we need to use gradient for fill color? Returns value of fill gradient property.
`final boolean`
`[layout](#layout(boolean))(boolean useCommands)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Layouting.layout(AbstractDiagramPresentationElement)`](layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)) or `com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement)`
`abstract boolean`
`[layout](#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) layouter)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Layouting.layout(AbstractDiagramPresentationElement, String)`](layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String)) or `com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String)`
`boolean`
`[layout](#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) diagramLayouter,
 [AbstractDiagramLayouterOptionsGroup](../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Layouting.layout(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)`](layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)) or `com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)`
`void`
`[loadContents](#loadContents(com.nomagic.task.ProgressStatus))([ProgressStatus](../../../task/ProgressStatus.html) status)`
Loads diagram to memory.
`void`
`[open](#open())()`
Open the diagram
`void`
`[open](#open(boolean))(boolean showProgress)`
Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open
`void`
`[open](#open(boolean,boolean))(boolean loadContent,
 boolean showProgress)`
Open the diagram.
`void`
`[open](#open(boolean,boolean,boolean))(boolean loadContent,
 boolean showProgress,
 boolean inActiveTab)`
Open the diagram.
`void`
`[openInActiveTab](#openInActiveTab(boolean))(boolean showProgress)`
Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab
`void`
`[paintChildren](#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`void`
`[paintSelf](#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`void`
`[postOpenFromCommand](#postOpenFromCommand())()`

`void`
`[preferredSize](#preferredSize(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) dim)`

`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
Listens for property change it can be: data was edited text box was edited
`void`
`[recalculateInternalDataRequired](#recalculateInternalDataRequired())()`

`void`
`[recursiveAutosize](#recursiveAutosize())()`
Resize recursively all symbols.
`void`
`[registerInProject](#registerInProject())()`

`boolean`
`[removeContentPropertyChangeListener](#removeContentPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Unregister the given listener from the diagram.
`final void`
`[removeDynamicRepresentationProvider](#removeDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider))(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)`

`final void`
`[removeDynamicStyleProvider](#removeDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider))(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)`

`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) l)`
Just hack, unregister the same listener from the container
`void`
`[resetContainer](#resetContainer())()`
In case diagram type changes in way `AbstractDiagramPresentationElementContainer` needs to be changed it should be reset and
 new one will be created on [`getContainer()`](#getContainer()) first call.
`void`
`[sAddPresentationElement](#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))([PresentationElement](PresentationElement.html) element,
 int index)`
Add given child to this symbol at given index
`void`
`[setBounds](#setBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
sets bounds of this object view
`void`
`[setContentHash](#setContentHash(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) contentHash)`
Sets identifier of contents.
`void`
`[setDiagramRepresentationObject](#setDiagramRepresentationObject(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject))(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)`
Initializes all persistent data from it's `DiagramRepresentationObject` except for diagram contents.
`void`
`[setDummyMode](#setDummyMode(boolean))(boolean dummyMode)`

`void`
`[setForceStoreContentOnSave](#setForceStoreContentOnSave(boolean))(boolean forceStoreContentOnSave)`

`void`
`[setGridSize](#setGridSize(int))(int grid)`
Sets grid size.
`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets the specified ID to the `Element`.
`void`
`[setInitialDiagramFrameBounds](#setInitialDiagramFrameBounds())()`
Sets initial diagram frame bounds for this diagram's frame.
`void`
`[setInitializer](#setInitializer(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer))(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer initializer)`
Sets custom diagram presentation element initializer.
`void`
`[setLabelsAutoDisplaySuspended](#setLabelsAutoDisplaySuspended(boolean))(boolean enabled)`

`void`
`[setModified](#setModified(boolean))(boolean modified)`

`void`
`[setOpenConfigurator](#setOpenConfigurator(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator))(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator openConfigurator)`
Sets open configurator.
`void`
`[setPresentationElements](#setPresentationElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)`
Sets children of this element
`void`
`[setShapesAutoResizeSuspended](#setShapesAutoResizeSuspended(boolean))(boolean enabled)`

`void`
`[setShowGrid](#setShowGrid(boolean))(boolean showGrid)`
Sets grid flag
`void`
`[setSnapToGridPaths](#setSnapToGridPaths(boolean))(boolean snap)`

`void`
`[setSnapToGridShapes](#setSnapToGridShapes(boolean))(boolean snap)`
Snaps symbols to grid.
`void`
`[setSuspendShapeAutoResizeMode](#setSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[setUseGradientForFill](#setUseGradientForFill(boolean))(boolean use)`
Sets elements gradient fill option.
`<T> void`
`[setValue](#setValue(java.lang.Object,T))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) key,
 T value)`

`static void`
`[setZoomProvider](#setZoomProvider(java.util.function.Function))([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html),[Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html)> provider)`

`void`
`[snapViewToGrid](#snapViewToGrid(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) el)`
Snaps given symbol to grid
`void`
`[sSetBounds](#sSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Sets bounds of this object view only.
`void`
`[sSetDiagramFrame](#sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView))(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView symbol)`

`protected void`
`[sSetForceStoreContentOnSave](#sSetForceStoreContentOnSave(boolean))(boolean forceStoreContentOnSave)`

`void`
`[sSetGridSize](#sSetGridSize(int))(int grid)`
Sets grid size.
`void`
`[sSetLabelsAutoDisplaySuspended](#sSetLabelsAutoDisplaySuspended(boolean))(boolean enabled)`

`void`
`[sSetLineJumpPlace](#sSetLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace))(com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)`
Sets value of line jump place.
`void`
`[sSetPresentationElements](#sSetPresentationElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)`
Sets children of this element
`void`
`[sSetShapesAutoResizeSuspended](#sSetShapesAutoResizeSuspended(boolean))(boolean enabled)`

`void`
`[sSetShowGrid](#sSetShowGrid(boolean))(boolean showGrid)`
Sets grid flag
`void`
`[sSetSnapToGridPaths](#sSetSnapToGridPaths(boolean))(boolean snap)`

`void`
`[sSetSnapToGridShapes](#sSetSnapToGridShapes(boolean))(boolean snap)`
Snaps symbols to grid.
`void`
`[sSetSuspendShapeAutoResizeMode](#sSetSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[unloadDiagram](#unloadDiagram())()`
Disposes all symbols and creates not loaded data.
`void`
`[unregisterFromProject](#unregisterFromProject())()`

`void`
`[updateFrameSize](#updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`

`boolean`
`[useParentStyle](#useParentStyle())()`
Does this element uses parent style or has it's own?
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[addPresentationElement](PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addPresentationElementWithoutResize](PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustBoundsBeforeChange](PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)), [adjustChildBounds](PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [adjustChildBoundsForMoving](PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](PresentationElement.html#alwaysShowTooltip()), [applyProperties](PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](PresentationElement.html#askDeleteDataConfirmation()), [atInsertChildren](PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](PresentationElement.html#autosizeAndResizeManipulatedParent()), [autosizeAndResizeParent](PresentationElement.html#autosizeAndResizeParent()), [beforeDelete](PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](PresentationElement.html#boundsChanged()), [boundsChanged](PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)), [canChangeParent](PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](PresentationElement.html#canFill()), [canHavePaths](PresentationElement.html#canHavePaths()), [changeProperties](PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [checkShowsProxy](PresentationElement.html#checkShowsProxy()), [childrenForMoving](PresentationElement.html#childrenForMoving()), [clearShowsProxy](PresentationElement.html#clearShowsProxy()), [collectSubManipulatedElements](PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](PresentationElement.html#coversPoint(int,int)), [createFillStrategy](PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](PresentationElement.html#createPropertyChangeListener()), [createSmartListenerConfig](PresentationElement.html#createSmartListenerConfig(java.util.List)), [disposeChildren](PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](PresentationElement.html#disposePropertyChangeListener()), [draw](PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](PresentationElement.html#dynamicFillColor()), [dynamicLineColor](PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](PresentationElement.html#dynamicStroke()), [dynamicStroke](PresentationElement.html#dynamicStroke(int)), [dynamicStroke](PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](PresentationElement.html#dynamicTextColor()), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [findOwnerForChildElement](PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [generateID](PresentationElement.html#generateID()), [getActualElement](PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](PresentationElement.html#getDiagramSurface()), [getDrawComparator](PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](PresentationElement.html#getEffectiveStyleOwner()), [getElement](PresentationElement.html#getElement()), [getElementsForRelationshipConnecting](PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](PresentationElement.html#getFillColor()), [getFont](PresentationElement.html#getFont()), [getFontHeight](PresentationElement.html#getFontHeight()), [getFontRenderContext](PresentationElement.html#getFontRenderContext()), [getHumanName](PresentationElement.html#getHumanName()), [getHumanType](PresentationElement.html#getHumanType()), [getIntersection](PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLineColor](PresentationElement.html#getLineColor()), [getLineWidth](PresentationElement.html#getLineWidth()), [getManipulatedElementAt](PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](PresentationElement.html#getManipulationBounds(java.awt.Point)), [getManipulationPreferredDimension](PresentationElement.html#getManipulationPreferredDimension()), [getMiddlePoint](PresentationElement.html#getMiddlePoint()), [getMiddlePoint](PresentationElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](PresentationElement.html#getMiddlePointX()), [getMiddlePointX](PresentationElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](PresentationElement.html#getMiddlePointY()), [getMiddlePointY](PresentationElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](PresentationElement.html#getMinimumDimension()), [getModelElement](PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](PresentationElement.html#getModelElementToMove()), [getNotCopyBounds](PresentationElement.html#getNotCopyBounds()), [getNotZoomedTolerance](PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](PresentationElement.html#getObjectParent()), [getParent](PresentationElement.html#getParent()), [getParentSymbolStyleOwner](PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredBounds](PresentationElement.html#getPreferredBounds()), [getPreferredDimension](PresentationElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](PresentationElement.html#getPreferredDimensionForAutosize()), [getPreferredSize](PresentationElement.html#getPreferredSize()), [getPresentationElementAt](PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementCount](PresentationElement.html#getPresentationElementCount()), [getPresentationElementIndex](PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getPresentationElementsAt](PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](PresentationElement.html#getProjectImpl()), [getProperty](PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](PresentationElement.html#getPropertyManager()), [getPropertyManagerName](PresentationElement.html#getPropertyManagerName()), [getRenderer](PresentationElement.html#getRenderer()), [getSelected](PresentationElement.html#getSelected()), [getStroke](PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](PresentationElement.html#getStroke(int)), [getStroke](PresentationElement.html#getStroke(int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int,int)), [getStroke](PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](PresentationElement.html#getStyle()), [getSymbolRenderer](PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](PresentationElement.html#getTextColor()), [getTolerance](PresentationElement.html#getTolerance()), [getVisibility](PresentationElement.html#getVisibility()), [getVisiblePresentationElements](PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](PresentationElement.html#hasManipulatedPresentationElements()), [hasManipulator](PresentationElement.html#hasManipulator()), [hasSharedModelElement](PresentationElement.html#hasSharedModelElement()), [initializeAndAutosize](PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetBoundsShape](PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [internalGetModelElementsForRelationshipConnecting](PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [internalUpdatePresentationElement](PresentationElement.html#internalUpdatePresentationElement()), [intersects](PresentationElement.html#intersects(int,int,int,int)), [invalidate](PresentationElement.html#invalidate()), [isCanChildrenChangeEdge](PresentationElement.html#isCanChildrenChangeEdge()), [isChildVisible](PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isContentHidden](PresentationElement.html#isContentHidden()), [isCreateElementListener](PresentationElement.html#isCreateElementListener()), [isDetectable](PresentationElement.html#isDetectable()), [isDisposed](PresentationElement.html#isDisposed()), [isLayouting](PresentationElement.html#isLayouting()), [isMovableByMoveManager](PresentationElement.html#isMovableByMoveManager()), [isNotNull](PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](PresentationElement.html#isShowElementTypeAsLabel()), [isShowsProxy](PresentationElement.html#isShowsProxy()), [isSnapToGrid](PresentationElement.html#isSnapToGrid()), [isSortable](PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](PresentationElement.html#isTextEditable()), [isUseFillColor](PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](PresentationElement.html#isUseFillColorByProperty()), [isVisible](PresentationElement.html#isVisible()), [isVisibleInDiagram](PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](PresentationElement.html#isVisibleOrShrunken()), [movePathElements](PresentationElement.html#movePathElements()), [movePathElementsRecursively](PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](PresentationElement.html#mustShowContextMenu()), [notifyCreated](PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](PresentationElement.html#onDiagramSurfaceSet()), [onFind](PresentationElement.html#onFind()), [onFind](PresentationElement.html#onFind(boolean)), [onFontChange](PresentationElement.html#onFontChange()), [onParentChange](PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenBackground](PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForShadowDrawing](PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [recreateListeners](PresentationElement.html#recreateListeners()), [registerInSortManager](PresentationElement.html#registerInSortManager()), [rememberBounds](PresentationElement.html#rememberBounds()), [rememberBounds](PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](PresentationElement.html#removeItSelfOnUpdate()), [removePresentationElement](PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [resizeParent](PresentationElement.html#resizeParent()), [sAddPresentationElement](PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](PresentationElement.html#selectObjectsForMoving()), [selectPathsForMoving](PresentationElement.html#selectPathsForMoving(java.util.List)), [setAllSelected](PresentationElement.html#setAllSelected(boolean)), [setBounds](PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](PresentationElement.html#setCreateElementListener(boolean)), [setDummyResizeMode](PresentationElement.html#setDummyResizeMode(boolean)), [setElement](PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFillColor](PresentationElement.html#setFillColor(java.awt.Color)), [setFont](PresentationElement.html#setFont(java.awt.Font)), [setLayouting](PresentationElement.html#setLayouting(boolean)), [setLineColor](PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](PresentationElement.html#setLocation(int,int)), [setLocation](PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](PresentationElement.html#setNeedRecreateListeners(boolean)), [setParent](PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setPropertyManagerName](PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](PresentationElement.html#setSelected(boolean)), [setSelected](PresentationElement.html#setSelected(java.util.List)), [setSize](PresentationElement.html#setSize(int,int)), [setSize](PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](PresentationElement.html#setTextColor(java.awt.Color)), [setTextEditable](PresentationElement.html#setTextEditable(boolean)), [setUseFillColor](PresentationElement.html#setUseFillColor(boolean)), [setVisibility](PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [setVisible](PresentationElement.html#setVisible(boolean)), [silentApply](PresentationElement.html#silentApply()), [silentApply](PresentationElement.html#silentApply(boolean)), [simpleSetBounds](PresentationElement.html#simpleSetBounds(int,int,int,int)), [simpleSetBounds](PresentationElement.html#simpleSetBounds(java.awt.Rectangle)), [snapToGrid](PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](PresentationElement.html#sortObjectsByY(java.util.List)), [sRemovePresentationElement](PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetBounds](PresentationElement.html#sSetBounds(int,int,int,int)), [sSetElement](PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [sSetLocation](PresentationElement.html#sSetLocation(int,int)), [sSetLocation](PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](PresentationElement.html#sSetSize(int,int)), [sSetSize](PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisibility](PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sSetVisible](PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](PresentationElement.html#update()), [updateAfterLoad](PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateLater](PresentationElement.html#updateLater()), [updateModelByView](PresentationElement.html#updateModelByView()), [updateModelByViewInternal](PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](PresentationElement.html#useParentProperties())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, setResourceIDProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../MDElement.html)
`[getProject](../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../utils/NameOwner.html)
`[getName](../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
DIAGRAM_ORIENTATION_VERTICAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ORIENTATION_VERTICAL
Vertical diagram orientation mode.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DIAGRAM_ORIENTATION_VERTICAL)
DIAGRAM_ORIENTATION_HORIZONTAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ORIENTATION_HORIZONTAL
Horizontal diagram orientation mode.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DIAGRAM_ORIENTATION_HORIZONTAL)
DIAGRAM_ORIENTATION_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> DIAGRAM_ORIENTATION_MODES
Diagram orientation modes.
FORCE_CONTENT_SAVE_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FORCE_CONTENT_SAVE_PROPERTY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.FORCE_CONTENT_SAVE_PROPERTY)
MIN_GRID_SIZE
public static final int MIN_GRID_SIZE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.MIN_GRID_SIZE)
MAX_GRID_SIZE
public static final int MAX_GRID_SIZE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.MAX_GRID_SIZE)
CANVAS_SIZE
public static final int CANVAS_SIZE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.CANVAS_SIZE)
DIAGRAM_CONTENT_LOADED_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_CONTENT_LOADED_PROPERTY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DIAGRAM_CONTENT_LOADED_PROPERTY)
DEFAULT_GRID_SIZE
public static final int DEFAULT_GRID_SIZE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DEFAULT_GRID_SIZE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractDiagramPresentationElement
public AbstractDiagramPresentationElement()
 ============ METHOD DETAIL ========== 
Method Details
setDiagramRepresentationObject
public void setDiagramRepresentationObject(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)
Initializes all persistent data from it's `DiagramRepresentationObject` except for diagram contents.
Parameters:
`repObject` - object
setID
public void setID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Description copied from interface: `[BaseElement](../BaseElement.html#setID(java.lang.String))`
Sets the specified ID to the `Element`.
Specified by:
`[setID](../BaseElement.html#setID(java.lang.String))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`setID` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`id` - the id to be set.
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Description copied from interface: `[BaseElement](../BaseElement.html#getID())`
Returns the ID of the `Element`.
 If the ID is `null`, new id for an element is generated.
 Element id is persistence and does not change during project save/load.
Specified by:
`[getID](../BaseElement.html#getID())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`getID` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
the ID of the `Element`.
internalAddToCache
protected void internalAddToCache([AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) oldType,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType)
internalRemoveFromCache
protected void internalRemoveFromCache([AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram)
hasNoRegisteredRealTypeDescriptor
protected boolean hasNoRegisteredRealTypeDescriptor()
internalSetDiagramType
protected abstract void internalSetDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) umlType)
getRepresentation
public com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject getRepresentation()
canAddInstance
public boolean canAddInstance([PresentationElement](PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Object view has no children.
Overrides:
`[canAddInstance](PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElement](PresentationElement.html)`
getAbstractDiagramPresentationElement
public [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) getAbstractDiagramPresentationElement()
Description copied from class: `[PresentationElement](PresentationElement.html#getAbstractDiagramPresentationElement())`
Returns diagram of this presentation element.
Overrides:
`[getAbstractDiagramPresentationElement](PresentationElement.html#getAbstractDiagramPresentationElement())` in class `[PresentationElement](PresentationElement.html)`
Returns:
diagram of this presentation element.
getCenterlineManager
public com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineManager getCenterlineManager()
Gets centerline manager for this diagram.
Returns:
centerline manager for this diagram.
getContainer
public com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer getContainer()
Returns:
diagram container
resetContainer
public void resetContainer()
In case diagram type changes in way `AbstractDiagramPresentationElementContainer` needs to be changed it should be reset and
 new one will be created on [`getContainer()`](#getContainer()) first call.
paintSelf
public void paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Specified by:
`[paintSelf](PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](PresentationElement.html)`
paintChildren
public void paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Specified by:
`[paintChildren](PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](PresentationElement.html)`
intersects
public boolean intersects(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
checks whether object intersects with given rectangle
Specified by:
`[intersects](PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Returns:
true if object and rectangle intersects
coversPoint
public boolean coversPoint(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
checks if object covers provided point
Specified by:
`[coversPoint](PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Returns:
true if object covers this point
sAddPresentationElement
public void sAddPresentationElement([PresentationElement](PresentationElement.html) element,
 int index)
Description copied from class: `[PresentationElement](PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))`
Add given child to this symbol at given index
Overrides:
`[sAddPresentationElement](PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`element` - child to add
`index` - index to add at. Can be -1
addPresentationElement
public void addPresentationElement([PresentationElement](PresentationElement.html) element,
 int index)
Description copied from class: `[PresentationElement](PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))`
Add given child to this symbol at given index
Overrides:
`[addPresentationElement](PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`element` - child to add
`index` - index to add at. Can be -1
isEmpty
public boolean isEmpty()
getPresentationElements
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElements()
Description copied from class: `[PresentationElement](PresentationElement.html#getPresentationElements())`
Returns all children of this element
Overrides:
`[getPresentationElements](PresentationElement.html#getPresentationElements())` in class `[PresentationElement](PresentationElement.html)`
Returns:
all children of this element. The collection is unmodifiable.
setPresentationElements
public void setPresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)
Description copied from class: `[PresentationElement](PresentationElement.html#setPresentationElements(java.util.List))`
Sets children of this element
Overrides:
`[setPresentationElements](PresentationElement.html#setPresentationElements(java.util.List))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`elements` - children
sSetPresentationElements
public void sSetPresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)
Description copied from class: `[PresentationElement](PresentationElement.html#sSetPresentationElements(java.util.List))`
Sets children of this element
Overrides:
`[sSetPresentationElements](PresentationElement.html#sSetPresentationElements(java.util.List))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`elements` - children
setBounds
public void setBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
Description copied from class: `[PresentationElement](PresentationElement.html#setBounds(java.awt.Rectangle))`
sets bounds of this object view
Specified by:
`[setBounds](PresentationElement.html#setBounds(java.awt.Rectangle))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`r` - rectangle of bounds
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)` - always
sSetBounds
public void sSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
Description copied from class: `[PresentationElement](PresentationElement.html#sSetBounds(java.awt.Rectangle))`
Sets bounds of this object view only.
Specified by:
`[sSetBounds](PresentationElement.html#sSetBounds(java.awt.Rectangle))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`r` - rectangle of bounds.
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)` - always
addPropertyChangeListener
public void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) l)
Just hack, registers the same listener to the container
Specified by:
`[addPropertyChangeListener](../BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`addPropertyChangeListener` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`l` - the `PropertyChangeListener` to be added.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removePropertyChangeListener
public void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) l)
Just hack, unregister the same listener from the container
Specified by:
`[removePropertyChangeListener](../BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`removePropertyChangeListener` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`l` - the PropertyChangeListener to be removed.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
getGridSize
public int getGridSize()
Returns:
grid size
setGridSize
public void setGridSize(int grid)
Sets grid size.
Parameters:
`grid` - grid size
snapViewToGrid
public void snapViewToGrid([PresentationElement](PresentationElement.html) el)
Snaps given symbol to grid
Parameters:
`el` - symbol
getPathGridSize
public float getPathGridSize()
Returns:
path grid size
sSetGridSize
public void sSetGridSize(int grid)
Sets grid size.
Parameters:
`grid` - grid size
setShowGrid
public void setShowGrid(boolean showGrid)
Sets grid flag
Parameters:
`showGrid` - show grid
sSetShowGrid
public void sSetShowGrid(boolean showGrid)
Sets grid flag
Parameters:
`showGrid` - show grid value
isShowGrid
public boolean isShowGrid()
Returns:
grid flag
setSnapToGridPaths
public void setSnapToGridPaths(boolean snap)
sSetSnapToGridPaths
public void sSetSnapToGridPaths(boolean snap)
isSnapToGridPaths
public boolean isSnapToGridPaths()
setSnapToGridShapes
public void setSnapToGridShapes(boolean snap)
Snaps symbols to grid.
Parameters:
`snap` - snap value
sSetSnapToGridShapes
public void sSetSnapToGridShapes(boolean snap)
Snaps symbols to grid.
Parameters:
`snap` - snap value
isSnapToGridShapes
public boolean isSnapToGridShapes()
Returns:
snap to grid value
getDynamicStyleProviders
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider> getDynamicStyleProviders()
addDynamicStyleProvider
public final void addDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)
removeDynamicStyleProvider
public final void removeDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)
addDynamicRepresentationProvider
public final void addDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)
removeDynamicRepresentationProvider
public final void removeDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)
getDynamicRepresentationProviders
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider> getDynamicRepresentationProviders()
getSortManagers
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.dassault_systemes.modeler.magic.diagram.SortManager> getSortManagers(boolean create)
Gets sort managers registered for this diagram.
Parameters:
`create` - indicates if sort managers should be created if they aren't created yet.
Returns:
sort managers registered for this diagram.
getSortManager
public com.dassault_systemes.modeler.magic.diagram.SortManager getSortManager()
Returns sort manager for this diagram view.
Returns:
symbol sort manager.
getManipulationSortManager
public com.dassault_systemes.modeler.magic.diagram.SortManager getManipulationSortManager()
Returns manipulation sort manager for this diagram view.
Returns:
manipulation symbol sort manager.
hasManipulationSortManager
protected boolean hasManipulationSortManager()
getPresentationElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
Gets object view at point.
Overrides:
`[getPresentationElementAt](PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
`kind` - intersection kind to check for
Returns:
object view at this point.
getPresentationElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Searches and returns symbol that covers given point.
Overrides:
`[getPresentationElementAt](PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`relativePoint` - point where searching for symbol
`kind` - intersection kind to check for
Returns:
symbol that covers given point, null if no objects found
getPresentationElementsAt
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Searches and returns all symbols that covers given point.
Overrides:
`[getPresentationElementsAt](PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`pt` - point where searching for symbol
`kind` - intersection kind to check for
Returns:
object that covers given point, null if no objects found
getPresentationElementsAt
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)
Description copied from class: `[PresentationElement](PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))`
Gets object view at point.
Overrides:
`[getPresentationElementsAt](PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
Returns:
object view at this point.
getPresentationElementsAt
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
Gets object view at point.
Overrides:
`[getPresentationElementsAt](PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
`kind` - intersection kind to check for
Returns:
object view at this point.
getManipulatedElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getManipulatedElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)
Description copied from class: `[PresentationElement](PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))`
Gets manipulate symbol at specified point pt.
Overrides:
`[getManipulatedElementAt](PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`relativePoint` - `Point`
`sortManagerProvider` - provides sort manager in which to search.
Returns:
manipulate symbol
getManipulatedElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getManipulatedElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)
Gets manipulate object view at specified point pt.
Overrides:
`[getManipulatedElementAt](PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`pt` - `Point`
`intersectionKind` - intersection kind to check for
Returns:
manipulate object view
hasSelectableSymbols
public boolean hasSelectableSymbols()
getVisibleBounds
@CheckForNullpublic [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getVisibleBounds()
Returns user visible bounds of the diagram.
Returns:
visible bounds or null if the diagram is not opened.
atInsert
public void atInsert()
Description copied from class: `[PresentationElement](PresentationElement.html#atInsert())`
Invalidates object at insert
Specified by:
`[atInsert](../BaseElement.html#atInsert())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`[atInsert](PresentationElement.html#atInsert())` in class `[PresentationElement](PresentationElement.html)`
dispose
public void dispose()
Description copied from class: `[PresentationElement](PresentationElement.html#dispose())`
disposes ends of links when link is deleted
Specified by:
`[dispose](../BaseElement.html#dispose())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`[dispose](PresentationElement.html#dispose())` in class `[PresentationElement](PresentationElement.html)`
firePropertyChange
public void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Description copied from interface: `[BaseElement](../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.
Specified by:
`[firePropertyChange](../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`[firePropertyChange](PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
fireContentPropertyChange
protected void fireContentPropertyChange([PresentationElement](PresentationElement.html) source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.
Parameters:
`source` - source element
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
clearCaches
protected void clearCaches()
collectShowingManipulatedElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectShowingManipulatedElementsRecursively()
Collects all visible manipulated elements in this diagram recursively.
Returns:
manipulated elements in this diagram
collectShowingPresentationElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectShowingPresentationElementsRecursively()
Collects all visible elements in this diagram recursively.
Returns:
visible elements in this diagram
collectPresentationElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectPresentationElementsRecursively()
Collects all elements in this diagram recursively.
Returns:
elements in this diagram
addContentPropertyChangeListener
@OpenApipublic boolean addContentPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Registers the listener for changes in all symbols contained in the diagram.
Parameters:
`listener` - the `PropertyChangeListener` to be added
Returns:
true if listener was added - it wasn't there yet, otherwise false
removeContentPropertyChangeListener
@OpenApipublic boolean removeContentPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Unregister the given listener from the diagram.
Parameters:
`listener` - the PropertyChangeListener to be removed
Returns:
true if listener was removed
clone
public [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) clone()
Specified by:
`[clone](../BaseElement.html#clone())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`[clone](PresentationElement.html#clone())` in class `[PresentationElement](PresentationElement.html)`
isDummyMode
public boolean isDummyMode()
setDummyMode
public void setDummyMode(boolean dummyMode)
canDeleteChild
public boolean canDeleteChild([BaseElement](../BaseElement.html) obj)
Description copied from interface: `[BaseElement](../BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))`
Checks if given element can be deleted from this element.
 Following rules must be true to have result true:
 1.this element must be editable.
 2.project must be editable.
 3.the type of given child must be valid for teamwork lock for edit operation
 (for example, class, package etc., not Attribute).
Specified by:
`[canDeleteChild](../BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`canDeleteChild` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`obj` - a given child
Returns:
true, if the given element can be deleted from the current element.
useParentStyle
public boolean useParentStyle()
Description copied from class: `[PresentationElement](PresentationElement.html#useParentStyle())`
Does this element uses parent style or has it's own?
Overrides:
`[useParentStyle](PresentationElement.html#useParentStyle())` in class `[PresentationElement](PresentationElement.html)`
Returns:
true, if element does not have style and uses parent's style.
getSurfaces
public final com.dassault_systemes.modeler.magic.diagram.DiagramSurfaces getSurfaces()
isSymbolDiagram
@OpenApipublic boolean isSymbolDiagram()
Checks if diagram displays symbols as its contents. Another type of diagrams may be tables, matrices.
Returns:
true if diagram displays symbols
accept
@OpenApipublic void accept([Visitor](../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
unloadDiagram
public void unloadDiagram()
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Disposes all symbols and creates not loaded data.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - in case of some error
internalClearOnUnload
protected void internalClearOnUnload()
recalculateInternalDataRequired
public void recalculateInternalDataRequired()
isLoaded
@OpenApipublic boolean isLoaded()
Check if the diagram is loaded.
Returns:
true if diagram contents is loaded
getContentState
public final com.nomagic.magicdraw.uml.symbols.DiagramContentState getContentState()
ensureLoaded
@OpenApipublic void ensureLoaded()
Ensures that the diagram is loaded.
 If the diagram is not loaded, load it.
 Make sure the project is active before invoking this method.
 Otherwise, the diagram may not be loaded.
loadContents
public void loadContents(@CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Loads diagram to memory.
 This method should be used only when the diagram is not loaded.
 Make sure the project is active before invoking this method.
 Otherwise, the diagram may not be loaded.
Parameters:
`status` - progress status.
cleanupAfterLoad
public void cleanupAfterLoad()
isForceStoreContentOnSave
public boolean isForceStoreContentOnSave()
setForceStoreContentOnSave
public void setForceStoreContentOnSave(boolean forceStoreContentOnSave)
sSetForceStoreContentOnSave
protected void sSetForceStoreContentOnSave(boolean forceStoreContentOnSave)
getDiagramTypeAsString
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramTypeAsString()
getRealType
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRealType()
Returns real diagram type. Real diagram type is a diagram type that is not registered but was persisted before.
Returns:
real type
isUseFlowLayoutLogic
public boolean isUseFlowLayoutLogic()
layout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public final boolean layout(boolean useCommands)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Layouting.layout(AbstractDiagramPresentationElement)`](layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)) or `com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement)`
Layout the diagram using default layouter.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List))} to select symbols in the diagram.
Parameters:
`useCommands` - true to create commands. If true, this command will be available in the project's command history.
Returns:
true if layout was performed.
layout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public abstract boolean layout(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) layouter)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Layouting.layout(AbstractDiagramPresentationElement, String)`](layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String)) or `com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String)`
Layouts the diagram with the specified layouter.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List))} to select symbols in the diagram.
Parameters:
`useCommands` - true to create commands. If true, this command will be available in the project's command history
`layouter` - layouter to be used for layouting
Returns:
true if layout was performed.
layout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public boolean layout(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) diagramLayouter,
 [AbstractDiagramLayouterOptionsGroup](../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Layouting.layout(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)`](layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)) or `com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)`
Layout the diagram.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List))} to select symbols in the diagram.
Parameters:
`useCommands` - true to create commands. If true, this command will be available in the project's command history
`diagramLayouter` - layouter to use
`options` - layout options
Returns:
true if layout was performed
getDefaultDiagramLayouter
public abstract [DiagramLayouter](layout/DiagramLayouter.html) getDefaultDiagramLayouter()
isShowDiagramFrame
public boolean isShowDiagramFrame()
getDiagramFrame
@CheckForNullpublic abstract com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView getDiagramFrame()
sSetDiagramFrame
public void sSetDiagramFrame(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView symbol)
updateFrameSize
public void updateFrameSize([PresentationElement](PresentationElement.html) element)
applyForcedProperties
public abstract void applyForcedProperties()
getRepresentationFromModelElement
public abstract com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject getRepresentationFromModelElement()
registerInProject
public void registerInProject()
unregisterFromProject
public void unregisterFromProject()
getDiagramType
public abstract [AbstractDiagramType](../AbstractDiagramType.html) getDiagramType()
postOpenFromCommand
public void postOpenFromCommand()
getZoom
public float getZoom()
getPathToMoveCache
public com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.PathToMoveCache getPathToMoveCache()
Returns:
paths to move cache
getContentHash
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getContentHash()
setContentHash
public void setContentHash(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) contentHash)
Sets identifier of contents.
Parameters:
`contentHash` - content hash
isShapesAutoResizeSuspended
public boolean isShapesAutoResizeSuspended()
sSetShapesAutoResizeSuspended
public void sSetShapesAutoResizeSuspended(boolean enabled)
setShapesAutoResizeSuspended
public void setShapesAutoResizeSuspended(boolean enabled)
autosizeSuspendedSymbolsWithHiddenContent
public void autosizeSuspendedSymbolsWithHiddenContent()
isLabelsAutoDisplaySuspended
public boolean isLabelsAutoDisplaySuspended()
sSetLabelsAutoDisplaySuspended
public void sSetLabelsAutoDisplaySuspended(boolean enabled)
setLabelsAutoDisplaySuspended
public void setLabelsAutoDisplaySuspended(boolean enabled)
getSuspendShapeAutoResizeMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuspendShapeAutoResizeMode()
sSetSuspendShapeAutoResizeMode
public void sSetSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
setSuspendShapeAutoResizeMode
public void setSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Description copied from class: `[PresentationElement](PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))`
Listens for property change it can be: data was edited text box was edited
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Overrides:
`[propertyChange](PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))` in class `[PresentationElement](PresentationElement.html)`
isModified
public boolean isModified()
setModified
public void setModified(boolean modified)
canAddChild
public boolean canAddChild([PresentationElement](PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Check of given symbol can be added as child into this symbol.
Overrides:
`[canAddChild](PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`symbol` - symbol
Returns:
true if symbol can be added
findPresentationElement
@OpenApi
@CheckForNullpublic final [PresentationElement](PresentationElement.html) findPresentationElement(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds a presentation element for a given model element of a given symbol type in this diagram.
 Does recursive search in the diagram.
Parameters:
`element` - the given ModelElement.
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElement
@OpenApi
@CheckForNullpublic final [PresentationElement](PresentationElement.html) findPresentationElement(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds a presentation element for a given model element of the given symbol type in this diagram. Does recursive search in the diagram.
Parameters:
`element` - the given ModelElement.
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElements
public final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> findPresentationElements([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[PresentationElement](PresentationElement.html)> predicate)
Finds manipulated presentation elements matching given predicate. Does recursive search in the diagram.
Parameters:
`predicate` - predicate
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElements
public final <S extends [PresentationElement](PresentationElement.html)>
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<S> findPresentationElements([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<S> classType)
Finds manipulated presentation elements matching given class type. Does recursive search in the diagram.
Parameters:
`classType` - class type
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElementForPathConnecting
@CheckForNull
@OpenApipublic final [PresentationElement](PresentationElement.html) findPresentationElementForPathConnecting([BaseElement](../BaseElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.
 Does recursive search.
Parameters:
`element` - the given ModelElement
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElementsForPathConnecting
@OpenApipublic final [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](PresentationElement.html)> findPresentationElementsForPathConnecting([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.
 Does recursive search.
Parameters:
`element` - the given ModelElement
`presentationElementClass` - the class of presentation element or null if any.
Returns:
a stream of presentation elements
getBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
Delegate bounds request to its container.
Overrides:
`[getBounds](PresentationElement.html#getBounds())` in class `[PresentationElement](PresentationElement.html)`
Returns:
bounds
See Also:
`PresentationElementsManager.reshapeShapeElement`
setOpenConfigurator
public void setOpenConfigurator(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator openConfigurator)
Sets open configurator.
Parameters:
`openConfigurator` - open configurator.
getOpenConfigurator
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator getOpenConfigurator()
initialize
public void initialize()
Description copied from class: `[PresentationElement](PresentationElement.html#initialize())`
Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.
Overrides:
`[initialize](PresentationElement.html#initialize())` in class `[PresentationElement](PresentationElement.html)`
setInitializer
public void setInitializer(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer initializer)
Sets custom diagram presentation element initializer.
Parameters:
`initializer` - custom diagram presentation element initializer.
open
@OpenApipublic void open()
Open the diagram
open
@OpenApipublic void open(boolean showProgress)
Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open
Parameters:
`showProgress` - show progress dialog
open
public void open(boolean loadContent,
 boolean showProgress)
Open the diagram.
Parameters:
`loadContent` - load diagram content
`showProgress` - show progress dialog
openInActiveTab
@OpenApipublic void openInActiveTab(boolean showProgress)
Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab
Parameters:
`showProgress` - show progress dialog
open
public void open(boolean loadContent,
 boolean showProgress,
 boolean inActiveTab)
Open the diagram.
Parameters:
`loadContent` - load diagram content
`showProgress` - show progress dialog
isOpening
public boolean isOpening()
Returns:
true if the diagram is in opening mode at the moment
close
@OpenApipublic final void close()
Closes diagram window.
close
public void close(boolean closeWindow)
Closes opened diagram
 If closeWindow is 'false' and there is a possibility to back to the previous diagram in that window, when the previous diagram is opened
 Otherwise, diagram window is closed
Parameters:
`closeWindow` - if a window should be closed
getLineJumpPlace
public com.nomagic.magicdraw.uml.symbols.LineJumpPlace getLineJumpPlace()
Returns current line jump place value of the diagram.
Returns:
line jump place mode
sSetLineJumpPlace
public void sSetLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)
Sets value of line jump place.
Parameters:
`lineJumpPlace` - line jump place mode
getDiagramOrientationMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramOrientationMode()
Gets diagram orientation mode.
Returns:
diagram orientation mode.
hasVerticalOrientation
public boolean hasVerticalOrientation()
Returns true if diagram has vertical orientation.
Returns:
true if the diagram has vertical orientation, false otherwise.
getBackgroundColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getBackgroundColor()
Returns:
background color
setUseGradientForFill
public void setUseGradientForFill(boolean use)
Sets elements gradient fill option. Will presentation element use gradient fill, or not for painting.
Parameters:
`use` - true to use.
isUseGradientForFill
public boolean isUseGradientForFill()
Do we need to use gradient for fill color? Returns value of fill gradient property.
Overrides:
`[isUseGradientForFill](PresentationElement.html#isUseGradientForFill())` in class `[PresentationElement](PresentationElement.html)`
Returns:
True, when use gradient fill property is true.
internalSilentApply
public void internalSilentApply()
Description copied from class: `[PresentationElement](PresentationElement.html#internalSilentApply())`
Silently applies all properties after initialization
Overrides:
`[internalSilentApply](PresentationElement.html#internalSilentApply())` in class `[PresentationElement](PresentationElement.html)`
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Description copied from class: `[PresentationElement](PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))`
Applies properties from given property manager
Overrides:
`[internalApplyProperties](PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))` in class `[PresentationElement](PresentationElement.html)`
Parameters:
`changer` - new properties
preferredSize
public void preferredSize([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) dim)
recursiveAutosize
public void recursiveAutosize()
Description copied from class: `[PresentationElement](PresentationElement.html#recursiveAutosize())`
Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy
Overrides:
`[recursiveAutosize](PresentationElement.html#recursiveAutosize())` in class `[PresentationElement](PresentationElement.html)`
calculateInitialDiagramFrameBounds
@CheckForNullprotected [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) calculateInitialDiagramFrameBounds()
Gets bounds which should be set for the diagram's frame.
adjustInitialDiagramFrameBounds
public static void adjustInitialDiagramFrameBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Adjust initial diagram frame bounds.
Parameters:
`bounds` - bounds
setInitialDiagramFrameBounds
public void setInitialDiagramFrameBounds()
Sets initial diagram frame bounds for this diagram's frame.
getOwnStyleDelegate
public com.dassault_systemes.modeler.foundation.diagram.style.DiagramStylePropertyDelegate getOwnStyleDelegate()
Overrides:
`[getOwnStyleDelegate](PresentationElement.html#getOwnStyleDelegate())` in class `[PresentationElement](PresentationElement.html)`
Returns:
the own style property delegate
setZoomProvider
public static void setZoomProvider([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html),[Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html)> provider)
setValue
public <T> void setValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) key,
 @CheckForNull
 T value)
getValue
@CheckForNullpublic <T> T getValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) key)
getValueOrCompute
public <T> T getValueOrCompute([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) key,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> valueSupplier)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class AbstractDiagramPresentationElement">Class AbstractDiagramPresentationElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</code>, <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractDiagramPresentationElement</span>
<span class="extends-implements">extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>
implements com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</span></div>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CANVAS_SIZE">CANVAS_SIZE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_GRID_SIZE">DEFAULT_GRID_SIZE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENT_LOADED_PROPERTY">DIAGRAM_CONTENT_LOADED_PROPERTY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_ORIENTATION_HORIZONTAL">DIAGRAM_ORIENTATION_HORIZONTAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Horizontal diagram orientation mode.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_ORIENTATION_MODES">DIAGRAM_ORIENTATION_MODES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Diagram orientation modes.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_ORIENTATION_VERTICAL">DIAGRAM_ORIENTATION_VERTICAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vertical diagram orientation mode.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FORCE_CONTENT_SAVE_PROPERTY">FORCE_CONTENT_SAVE_PROPERTY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MAX_GRID_SIZE">MAX_GRID_SIZE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MIN_GRID_SIZE">MIN_GRID_SIZE</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="PresentationElement.html#DEFAULT_LINE_WIDTH">DEFAULT_LINE_WIDTH</a>, <a href="PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="PresentationElement.html#HANDLE_SIZE">HANDLE_SIZE</a>, <a href="PresentationElement.html#MAX_LINE_WIDTH">MAX_LINE_WIDTH</a>, <a href="PresentationElement.html#MIN_LINE_WIDTH">MIN_LINE_WIDTH</a>, <a href="PresentationElement.html#peStyle">peStyle</a>, <a href="PresentationElement.html#SHADOW_WIDTH">SHADOW_WIDTH</a>, <a href="PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractDiagramPresentationElement</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContentPropertyChangeListener(java.beans.PropertyChangeListener)">addContentPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the listener for changes in all symbols contained in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)">addDynamicRepresentationProvider</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)">addDynamicStyleProvider</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol at given index</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> l)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Just hack, registers the same listener to the container</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustInitialDiagramFrameBounds(java.awt.Rectangle)">adjustInitialDiagramFrameBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adjust initial diagram frame bounds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#applyForcedProperties()">applyForcedProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates object at insert</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosizeSuspendedSymbolsWithHiddenContent()">autosizeSuspendedSymbolsWithHiddenContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateInitialDiagramFrameBounds()">calculateInitialDiagramFrameBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets bounds which should be set for the diagram's frame.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check of given symbol can be added as child into this symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Object view has no children.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element can be deleted from this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cleanupAfterLoad()">cleanupAfterLoad</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCaches()">clearCaches</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes diagram window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close(boolean)">close</a><wbr/>(boolean closeWindow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes opened diagram
 If closeWindow is 'false' and there is a possibility to back to the previous diagram in that window, when the previous diagram is opened
 Otherwise, diagram window is closed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectPresentationElementsRecursively()">collectPresentationElementsRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements in this diagram recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectShowingManipulatedElementsRecursively()">collectShowingManipulatedElementsRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible manipulated elements in this diagram recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectShowingPresentationElementsRecursively()">collectShowingPresentationElementsRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible elements in this diagram recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">disposes ends of links when link is deleted</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureLoaded()">ensureLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Ensures that the diagram is loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">findPresentationElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a presentation element for a given model element of the given symbol type in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a presentation element for a given model element of a given symbol type in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">findPresentationElementForPathConnecting</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final &lt;S extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;S&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElements(java.lang.Class)">findPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;S&gt; classType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds manipulated presentation elements matching given class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElements(java.util.function.Predicate)">findPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; predicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds manipulated presentation elements matching given predicate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElementsForPathConnecting</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireContentPropertyChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.lang.Object,java.lang.Object)">fireContentPropertyChange</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagram of this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBackgroundColor()">getBackgroundColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegate bounds request to its container.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenterlineManager()">getCenterlineManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets centerline manager for this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainer()">getContainer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentHash()">getContentHash</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.nomagic.magicdraw.uml.symbols.DiagramContentState</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentState()">getContentState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultDiagramLayouter()">getDefaultDiagramLayouter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramFrame()">getDiagramFrame</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramOrientationMode()">getDiagramOrientationMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets diagram orientation mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramType()">getDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramTypeAsString()">getDiagramTypeAsString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicRepresentationProviders()">getDynamicRepresentationProviders</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicStyleProviders()">getDynamicStyleProviders</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGridSize()">getGridSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the ID of the <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.LineJumpPlace</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineJumpPlace()">getLineJumpPlace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current line jump place value of the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulate object view at specified point pt.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulate symbol at specified point pt.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.magic.diagram.SortManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulationSortManager()">getManipulationSortManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns manipulation sort manager for this diagram view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpenConfigurator()">getOpenConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.style.DiagramStylePropertyDelegate</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnStyleDelegate()">getOwnStyleDelegate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>float</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathGridSize()">getPathGridSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.PathToMoveCache</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathToMoveCache()">getPathToMoveCache</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Searches and returns symbol that covers given point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElements()">getPresentationElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all children of this element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Searches and returns all symbols that covers given point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRealType()">getRealType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns real diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentation()">getRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresentationFromModelElement()">getRepresentationFromModelElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.magic.diagram.SortManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortManager()">getSortManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns sort manager for this diagram view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.dassault_systemes.modeler.magic.diagram.SortManager&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortManagers(boolean)">getSortManagers</a><wbr/>(boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets sort managers registered for this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.dassault_systemes.modeler.magic.diagram.DiagramSurfaces</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSurfaces()">getSurfaces</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.Object)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T&gt; T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueOrCompute(java.lang.Object,java.util.function.Supplier)">getValueOrCompute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; valueSupplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleBounds()">getVisibleBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns user visible bounds of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>float</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getZoom()">getZoom</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasManipulationSortManager()">hasManipulationSortManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasNoRegisteredRealTypeDescriptor()">hasNoRegisteredRealTypeDescriptor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasSelectableSymbols()">hasSelectableSymbols</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasVerticalOrientation()">hasVerticalOrientation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if diagram has vertical orientation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize symbol and its children state.</div>
</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#internalSetDiagramType(java.lang.String,java.lang.String)">internalSetDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSilentApply()">internalSilentApply</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a><wbr/>(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks whether object intersects with given rectangle</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDummyMode()">isDummyMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isForceStoreContentOnSave()">isForceStoreContentOnSave</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLabelsAutoDisplaySuspended()">isLabelsAutoDisplaySuspended</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded()">isLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if the diagram is loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isModified()">isModified</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOpening()">isOpening</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShapesAutoResizeSuspended()">isShapesAutoResizeSuspended</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDiagramFrame()">isShowDiagramFrame</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGrid()">isShowGrid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGridPaths()">isSnapToGridPaths</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGridShapes()">isSnapToGridShapes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSymbolDiagram()">isSymbolDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram displays symbols as its contents.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseFlowLayoutLogic()">isUseFlowLayoutLogic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseGradientForFill()">isUseGradientForFill</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do we need to use gradient for fill color? Returns value of fill gradient property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(boolean)">layout</a><wbr/>(boolean useCommands)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)"><code>Layouting.layout(AbstractDiagramPresentationElement)</code></a> or <code>com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement)</code></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">layout</a><wbr/>(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String)"><code>Layouting.layout(AbstractDiagramPresentationElement, String)</code></a> or <code>com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">layout</a><wbr/>(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> diagramLayouter,
 <a href="../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)"><code>Layouting.layout(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)</code></a> or <code>com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)</code></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadContents(com.nomagic.task.ProgressStatus)">loadContents</a><wbr/>(<a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads diagram to memory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open()">open</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(boolean)">open</a><wbr/>(boolean showProgress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(boolean,boolean)">open</a><wbr/>(boolean loadContent,
 boolean showProgress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(boolean,boolean,boolean)">open</a><wbr/>(boolean loadContent,
 boolean showProgress,
 boolean inActiveTab)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openInActiveTab(boolean)">openInActiveTab</a><wbr/>(boolean showProgress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#recalculateInternalDataRequired()">recalculateInternalDataRequired</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#recursiveAutosize()">recursiveAutosize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resize recursively all symbols.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerInProject()">registerInProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">removeContentPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the given listener from the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)">removeDynamicRepresentationProvider</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)">removeDynamicStyleProvider</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> l)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Just hack, unregister the same listener from the container</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetContainer()">resetContainer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">In case diagram type changes in way <code>AbstractDiagramPresentationElementContainer</code> needs to be changed it should be reset and
 new one will be created on <a href="#getContainer()"><code>getContainer()</code></a> first call.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol at given index</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBounds(java.awt.Rectangle)">setBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets bounds of this object view</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContentHash(java.lang.String)">setContentHash</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contentHash)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets identifier of contents.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramRepresentationObject(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject)">setDiagramRepresentationObject</a><wbr/>(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initializes all persistent data from it's <code>DiagramRepresentationObject</code> except for diagram contents.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDummyMode(boolean)">setDummyMode</a><wbr/>(boolean dummyMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setForceStoreContentOnSave(boolean)">setForceStoreContentOnSave</a><wbr/>(boolean forceStoreContentOnSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGridSize(int)">setGridSize</a><wbr/>(int grid)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets grid size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the specified ID to the <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitialDiagramFrameBounds()">setInitialDiagramFrameBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets initial diagram frame bounds for this diagram's frame.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitializer(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer)">setInitializer</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets custom diagram presentation element initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLabelsAutoDisplaySuspended(boolean)">setLabelsAutoDisplaySuspended</a><wbr/>(boolean enabled)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModified(boolean)">setModified</a><wbr/>(boolean modified)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOpenConfigurator(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator)">setOpenConfigurator</a><wbr/>(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator openConfigurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets open configurator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPresentationElements(java.util.List)">setPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets children of this element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShapesAutoResizeSuspended(boolean)">setShapesAutoResizeSuspended</a><wbr/>(boolean enabled)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGrid(boolean)">setShowGrid</a><wbr/>(boolean showGrid)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets grid flag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSnapToGridPaths(boolean)">setSnapToGridPaths</a><wbr/>(boolean snap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSnapToGridShapes(boolean)">setSnapToGridShapes</a><wbr/>(boolean snap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Snaps symbols to grid.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseGradientForFill(boolean)">setUseGradientForFill</a><wbr/>(boolean use)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets elements gradient fill option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object,T)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> key,
 T value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setZoomProvider(java.util.function.Function)">setZoomProvider</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a>&gt; provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapViewToGrid(com.nomagic.magicdraw.uml.symbols.PresentationElement)">snapViewToGrid</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> el)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Snaps given symbol to grid</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBounds(java.awt.Rectangle)">sSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bounds of this object view only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">sSetDiagramFrame</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetForceStoreContentOnSave(boolean)">sSetForceStoreContentOnSave</a><wbr/>(boolean forceStoreContentOnSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetGridSize(int)">sSetGridSize</a><wbr/>(int grid)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets grid size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetLabelsAutoDisplaySuspended(boolean)">sSetLabelsAutoDisplaySuspended</a><wbr/>(boolean enabled)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace)">sSetLineJumpPlace</a><wbr/>(com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value of line jump place.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetPresentationElements(java.util.List)">sSetPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets children of this element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShapesAutoResizeSuspended(boolean)">sSetShapesAutoResizeSuspended</a><wbr/>(boolean enabled)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowGrid(boolean)">sSetShowGrid</a><wbr/>(boolean showGrid)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets grid flag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSnapToGridPaths(boolean)">sSetSnapToGridPaths</a><wbr/>(boolean snap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSnapToGridShapes(boolean)">sSetSnapToGridShapes</a><wbr/>(boolean snap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Snaps symbols to grid.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unloadDiagram()">unloadDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disposes all symbols and creates not loaded data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterFromProject()">unregisterFromProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateFrameSize</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useParentStyle()">useParentStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does this element uses parent style or has it's own?</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElementWithoutResize</a>, <a href="PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a>, <a href="PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBoundsForMoving</a>, <a href="PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="PresentationElement.html#autosizeAndResizeParent()">autosizeAndResizeParent</a>, <a href="PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a>, <a href="PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="PresentationElement.html#canFill()">canFill</a>, <a href="PresentationElement.html#canHavePaths()">canHavePaths</a>, <a href="PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="PresentationElement.html#checkShowsProxy()">checkShowsProxy</a>, <a href="PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="PresentationElement.html#clearShowsProxy()">clearShowsProxy</a>, <a href="PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="PresentationElement.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a>, <a href="PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="PresentationElement.html#generateID()">generateID</a>, <a href="PresentationElement.html#getActualElement()">getActualElement</a>, <a href="PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="PresentationElement.html#getElement()">getElement</a>, <a href="PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="PresentationElement.html#getFillColor()">getFillColor</a>, <a href="PresentationElement.html#getFont()">getFont</a>, <a href="PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="PresentationElement.html#getHumanName()">getHumanName</a>, <a href="PresentationElement.html#getHumanType()">getHumanType</a>, <a href="PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="PresentationElement.html#getLineColor()">getLineColor</a>, <a href="PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="PresentationElement.html#getManipulationPreferredDimension()">getManipulationPreferredDimension</a>, <a href="PresentationElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="PresentationElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="PresentationElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="PresentationElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="PresentationElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="PresentationElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="PresentationElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="PresentationElement.html#getModelElement()">getModelElement</a>, <a href="PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="PresentationElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="PresentationElement.html#getParent()">getParent</a>, <a href="PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="PresentationElement.html#getPreferredBounds()">getPreferredBounds</a>, <a href="PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="PresentationElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementIndex</a>, <a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="PresentationElement.html#getRenderer()">getRenderer</a>, <a href="PresentationElement.html#getSelected()">getSelected</a>, <a href="PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="PresentationElement.html#getStroke(int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="PresentationElement.html#getStyle()">getStyle</a>, <a href="PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="PresentationElement.html#getTextColor()">getTextColor</a>, <a href="PresentationElement.html#getTolerance()">getTolerance</a>, <a href="PresentationElement.html#getVisibility()">getVisibility</a>, <a href="PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="PresentationElement.html#hasManipulator()">hasManipulator</a>, <a href="PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a>, <a href="PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="PresentationElement.html#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>, <a href="PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="PresentationElement.html#invalidate()">invalidate</a>, <a href="PresentationElement.html#isCanChildrenChangeEdge()">isCanChildrenChangeEdge</a>, <a href="PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="PresentationElement.html#isContentHidden()">isContentHidden</a>, <a href="PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="PresentationElement.html#isDetectable()">isDetectable</a>, <a href="PresentationElement.html#isDisposed()">isDisposed</a>, <a href="PresentationElement.html#isLayouting()">isLayouting</a>, <a href="PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="PresentationElement.html#isSelected()">isSelected</a>, <a href="PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="PresentationElement.html#isShowsProxy()">isShowsProxy</a>, <a href="PresentationElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="PresentationElement.html#isSortable()">isSortable</a>, <a href="PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="PresentationElement.html#isVisible()">isVisible</a>, <a href="PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="PresentationElement.html#movePathElements()">movePathElements</a>, <a href="PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="PresentationElement.html#onFind()">onFind</a>, <a href="PresentationElement.html#onFind(boolean)">onFind</a>, <a href="PresentationElement.html#onFontChange()">onFontChange</a>, <a href="PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenBackground</a>, <a href="PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a>, <a href="PresentationElement.html#resizeParent()">resizeParent</a>, <a href="PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="PresentationElement.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="PresentationElement.html#setDummyResizeMode(boolean)">setDummyResizeMode</a>, <a href="PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="PresentationElement.html#setFillColor(java.awt.Color)">setFillColor</a>, <a href="PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="PresentationElement.html#setSize(int,int)">setSize</a>, <a href="PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="PresentationElement.html#setTextEditable(boolean)">setTextEditable</a>, <a href="PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="PresentationElement.html#silentApply()">silentApply</a>, <a href="PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="PresentationElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a>, <a href="PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a>, <a href="PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="PresentationElement.html#update()">update</a>, <a href="PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="PresentationElement.html#updateLater()">updateLater</a>, <a href="PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="PresentationElement.html#useParentProperties()">useParentProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, setResourceIDProvider, sGetID, toString</code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../utils/NameOwner.html#getName()">getName</a></code></div>
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
<section class="detail" id="DIAGRAM_ORIENTATION_VERTICAL">
<h3>DIAGRAM_ORIENTATION_VERTICAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ORIENTATION_VERTICAL</span></div>
<div class="block">Vertical diagram orientation mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DIAGRAM_ORIENTATION_VERTICAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ORIENTATION_HORIZONTAL">
<h3>DIAGRAM_ORIENTATION_HORIZONTAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ORIENTATION_HORIZONTAL</span></div>
<div class="block">Horizontal diagram orientation mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DIAGRAM_ORIENTATION_HORIZONTAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ORIENTATION_MODES">
<h3>DIAGRAM_ORIENTATION_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">DIAGRAM_ORIENTATION_MODES</span></div>
<div class="block">Diagram orientation modes.</div>
</section>
</li>
<li>
<section class="detail" id="FORCE_CONTENT_SAVE_PROPERTY">
<h3>FORCE_CONTENT_SAVE_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FORCE_CONTENT_SAVE_PROPERTY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.FORCE_CONTENT_SAVE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MIN_GRID_SIZE">
<h3>MIN_GRID_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MIN_GRID_SIZE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.MIN_GRID_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAX_GRID_SIZE">
<h3>MAX_GRID_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MAX_GRID_SIZE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.MAX_GRID_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CANVAS_SIZE">
<h3>CANVAS_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CANVAS_SIZE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.CANVAS_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENT_LOADED_PROPERTY">
<h3>DIAGRAM_CONTENT_LOADED_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_CONTENT_LOADED_PROPERTY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DIAGRAM_CONTENT_LOADED_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_GRID_SIZE">
<h3>DEFAULT_GRID_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DEFAULT_GRID_SIZE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.DEFAULT_GRID_SIZE">Constant Field Values</a></li>
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
<h3>AbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractDiagramPresentationElement</span>()</div>
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
<section class="detail" id="setDiagramRepresentationObject(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject)">
<h3>setDiagramRepresentationObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDiagramRepresentationObject</span><wbr/><span class="parameters">(com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject repObject)</span></div>
<div class="block">Initializes all persistent data from it's <code>DiagramRepresentationObject</code> except for diagram contents.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>repObject</code> - object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#setID(java.lang.String)">BaseElement</a></code></span></div>
<div class="block">Sets the specified ID to the <code>Element</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#setID(java.lang.String)">setID</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>setID</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>id</code> - the id to be set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#getID()">BaseElement</a></code></span></div>
<div class="block">Returns the ID of the <code>Element</code>.
 If the ID is <code>null</code>, new id for an element is generated.
 Element id is persistence and does not change during project save/load.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#getID()">getID</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getID</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>the ID of the <code>Element</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalAddToCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,java.lang.String)">
<h3>internalAddToCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalAddToCache</span><wbr/><span class="parameters">(<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType)</span></div>
</section>
</li>
<li>
<section class="detail" id="internalRemoveFromCache(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>internalRemoveFromCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalRemoveFromCache</span><wbr/><span class="parameters">(<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasNoRegisteredRealTypeDescriptor()">
<h3>hasNoRegisteredRealTypeDescriptor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasNoRegisteredRealTypeDescriptor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="internalSetDiagramType(java.lang.String,java.lang.String)">
<h3>internalSetDiagramType</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">internalSetDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlType)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRepresentation()">
<h3>getRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject</span> <span class="element-name">getRepresentation</span>()</div>
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
<dd><code><a href="PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramPresentationElement()">
<h3>getAbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getAbstractDiagramPresentationElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getAbstractDiagramPresentationElement()">PresentationElement</a></code></span></div>
<div class="block">Returns diagram of this presentation element.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>diagram of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenterlineManager()">
<h3>getCenterlineManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineManager</span> <span class="element-name">getCenterlineManager</span>()</div>
<div class="block">Gets centerline manager for this diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>centerline manager for this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainer()">
<h3>getContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElementContainer</span> <span class="element-name">getContainer</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram container</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetContainer()">
<h3>resetContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetContainer</span>()</div>
<div class="block">In case diagram type changes in way <code>AbstractDiagramPresentationElementContainer</code> needs to be changed it should be reset and
 new one will be created on <a href="#getContainer()"><code>getContainer()</code></a> first call.</div>
</section>
</li>
<li>
<section class="detail" id="paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintSelf</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintChildren</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">checks whether object intersects with given rectangle</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object and rectangle intersects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>coversPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">coversPoint</span><wbr/><span class="parameters">(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">checks if object covers provided point</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object covers this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">
<h3>sAddPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sAddPresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">PresentationElement</a></code></span></div>
<div class="block">Add given child to this symbol at given index</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
<dd><code>index</code> - index to add at. Can be -1</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">
<h3>addPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">PresentationElement</a></code></span></div>
<div class="block">Add given child to this symbol at given index</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
<dd><code>index</code> - index to add at. Can be -1</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPresentationElements()">
<h3>getPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElements</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getPresentationElements()">PresentationElement</a></code></span></div>
<div class="block">Returns all children of this element</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getPresentationElements()">getPresentationElements</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>all children of this element. The collection is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPresentationElements(java.util.List)">
<h3>setPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#setPresentationElements(java.util.List)">PresentationElement</a></code></span></div>
<div class="block">Sets children of this element</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#setPresentationElements(java.util.List)">setPresentationElements</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>elements</code> - children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetPresentationElements(java.util.List)">
<h3>sSetPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#sSetPresentationElements(java.util.List)">PresentationElement</a></code></span></div>
<div class="block">Sets children of this element</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#sSetPresentationElements(java.util.List)">sSetPresentationElements</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>elements</code> - children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBounds(java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span>
               throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#setBounds(java.awt.Rectangle)">PresentationElement</a></code></span></div>
<div class="block">sets bounds of this object view</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PresentationElement.html#setBounds(java.awt.Rectangle)">setBounds</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>r</code> - rectangle of bounds</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code> - always</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetBounds(java.awt.Rectangle)">
<h3>sSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span>
                throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#sSetBounds(java.awt.Rectangle)">PresentationElement</a></code></span></div>
<div class="block">Sets bounds of this object view only.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PresentationElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>r</code> - rectangle of bounds.</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code> - always</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> l)</span></div>
<div class="block">Just hack, registers the same listener to the container</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>addPropertyChangeListener</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>l</code> - the <code>PropertyChangeListener</code> to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> l)</span></div>
<div class="block">Just hack, unregister the same listener from the container</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>removePropertyChangeListener</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>l</code> - the PropertyChangeListener to be removed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGridSize()">
<h3>getGridSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getGridSize</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>grid size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGridSize(int)">
<h3>setGridSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGridSize</span><wbr/><span class="parameters">(int grid)</span></div>
<div class="block">Sets grid size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>grid</code> - grid size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="snapViewToGrid(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>snapViewToGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">snapViewToGrid</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> el)</span></div>
<div class="block">Snaps given symbol to grid</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>el</code> - symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathGridSize()">
<h3>getPathGridSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">getPathGridSize</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>path grid size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetGridSize(int)">
<h3>sSetGridSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetGridSize</span><wbr/><span class="parameters">(int grid)</span></div>
<div class="block">Sets grid size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>grid</code> - grid size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowGrid(boolean)">
<h3>setShowGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGrid</span><wbr/><span class="parameters">(boolean showGrid)</span></div>
<div class="block">Sets grid flag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showGrid</code> - show grid</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowGrid(boolean)">
<h3>sSetShowGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowGrid</span><wbr/><span class="parameters">(boolean showGrid)</span></div>
<div class="block">Sets grid flag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showGrid</code> - show grid value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowGrid()">
<h3>isShowGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowGrid</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>grid flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSnapToGridPaths(boolean)">
<h3>setSnapToGridPaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSnapToGridPaths</span><wbr/><span class="parameters">(boolean snap)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetSnapToGridPaths(boolean)">
<h3>sSetSnapToGridPaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSnapToGridPaths</span><wbr/><span class="parameters">(boolean snap)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSnapToGridPaths()">
<h3>isSnapToGridPaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSnapToGridPaths</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSnapToGridShapes(boolean)">
<h3>setSnapToGridShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSnapToGridShapes</span><wbr/><span class="parameters">(boolean snap)</span></div>
<div class="block">Snaps symbols to grid.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>snap</code> - snap value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetSnapToGridShapes(boolean)">
<h3>sSetSnapToGridShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSnapToGridShapes</span><wbr/><span class="parameters">(boolean snap)</span></div>
<div class="block">Snaps symbols to grid.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>snap</code> - snap value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSnapToGridShapes()">
<h3>isSnapToGridShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSnapToGridShapes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>snap to grid value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDynamicStyleProviders()">
<h3>getDynamicStyleProviders</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider&gt;</span> <span class="element-name">getDynamicStyleProviders</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)">
<h3>addDynamicStyleProvider</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addDynamicStyleProvider</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeDynamicStyleProvider(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider)">
<h3>removeDynamicStyleProvider</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">removeDynamicStyleProvider</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.DynamicStyleProvider dynamicStyleProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="addDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)">
<h3>addDynamicRepresentationProvider</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addDynamicRepresentationProvider</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeDynamicRepresentationProvider(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider)">
<h3>removeDynamicRepresentationProvider</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">removeDynamicRepresentationProvider</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider dynamicRepresentationProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDynamicRepresentationProviders()">
<h3>getDynamicRepresentationProviders</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.uml.symbols.DynamicRepresentationProvider&gt;</span> <span class="element-name">getDynamicRepresentationProviders</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSortManagers(boolean)">
<h3>getSortManagers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.dassault_systemes.modeler.magic.diagram.SortManager&gt;</span> <span class="element-name">getSortManagers</span><wbr/><span class="parameters">(boolean create)</span></div>
<div class="block">Gets sort managers registered for this diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>create</code> - indicates if sort managers should be created if they aren't created yet.</dd>
<dt>Returns:</dt>
<dd>sort managers registered for this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortManager()">
<h3>getSortManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.magic.diagram.SortManager</span> <span class="element-name">getSortManager</span>()</div>
<div class="block">Returns sort manager for this diagram view.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>symbol sort manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulationSortManager()">
<h3>getManipulationSortManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.magic.diagram.SortManager</span> <span class="element-name">getManipulationSortManager</span>()</div>
<div class="block">Returns manipulation sort manager for this diagram view.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manipulation symbol sort manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasManipulationSortManager()">
<h3>hasManipulationSortManager</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasManipulationSortManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Searches and returns symbol that covers given point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - point where searching for symbol</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>symbol that covers given point, null if no objects found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Searches and returns all symbols that covers given point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>pt</code> - point where searching for symbol</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object that covers given point, null if no objects found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">PresentationElement</a></code></span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">
<h3>getManipulatedElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">PresentationElement</a></code></span></div>
<div class="block">Gets manipulate symbol at specified point pt.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - <code> Point </code></dd>
<dd><code>sortManagerProvider</code> - provides sort manager in which to search.</dd>
<dt>Returns:</dt>
<dd>manipulate symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getManipulatedElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)</span></div>
<div class="block">Gets manipulate object view at specified point pt.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>pt</code> - <code> Point </code></dd>
<dd><code>intersectionKind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>manipulate object view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSelectableSymbols()">
<h3>hasSelectableSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasSelectableSymbols</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getVisibleBounds()">
<h3>getVisibleBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getVisibleBounds</span>()</div>
<div class="block">Returns user visible bounds of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>visible bounds or null if the diagram is not opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#atInsert()">PresentationElement</a></code></span></div>
<div class="block">Invalidates object at insert</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#atInsert()">atInsert</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#atInsert()">atInsert</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#dispose()">PresentationElement</a></code></span></div>
<div class="block">disposes ends of links when link is deleted</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#dispose()">dispose</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#dispose()">dispose</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">BaseElement</a></code></span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireContentPropertyChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.lang.Object,java.lang.Object)">
<h3>fireContentPropertyChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">fireContentPropertyChange</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source element</dd>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCaches()">
<h3>clearCaches</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearCaches</span>()</div>
</section>
</li>
<li>
<section class="detail" id="collectShowingManipulatedElementsRecursively()">
<h3>collectShowingManipulatedElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectShowingManipulatedElementsRecursively</span>()</div>
<div class="block">Collects all visible manipulated elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manipulated elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectShowingPresentationElementsRecursively()">
<h3>collectShowingPresentationElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectShowingPresentationElementsRecursively</span>()</div>
<div class="block">Collects all visible elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>visible elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectPresentationElementsRecursively()">
<h3>collectPresentationElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectPresentationElementsRecursively</span>()</div>
<div class="block">Collects all elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContentPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addContentPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addContentPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Registers the listener for changes in all symbols contained in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added</dd>
<dt>Returns:</dt>
<dd>true if listener was added - it wasn't there yet, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removeContentPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeContentPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Unregister the given listener from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed</dd>
<dt>Returns:</dt>
<dd>true if listener was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#clone()">clone</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDummyMode()">
<h3>isDummyMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDummyMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDummyMode(boolean)">
<h3>setDummyMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDummyMode</span><wbr/><span class="parameters">(boolean dummyMode)</span></div>
</section>
</li>
<li>
<section class="detail" id="canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canDeleteChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDeleteChild</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Checks if given element can be deleted from this element.
 Following rules must be true to have result true:
 1.this element must be editable.
 2.project must be editable.
 3.the type of given child must be valid for teamwork lock for edit operation
 (for example, class, package etc., not Attribute).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>canDeleteChild</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - a given child</dd>
<dt>Returns:</dt>
<dd>true, if the given element can be deleted from the current element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useParentStyle()">
<h3>useParentStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">useParentStyle</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#useParentStyle()">PresentationElement</a></code></span></div>
<div class="block">Does this element uses parent style or has it's own?</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#useParentStyle()">useParentStyle</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true, if element does not have style and uses parent's style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSurfaces()">
<h3>getSurfaces</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">com.dassault_systemes.modeler.magic.diagram.DiagramSurfaces</span> <span class="element-name">getSurfaces</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSymbolDiagram()">
<h3>isSymbolDiagram</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSymbolDiagram</span>()</div>
<div class="block">Checks if diagram displays symbols as its contents. Another type of diagrams may be tables, matrices.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram displays symbols</dd>
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
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unloadDiagram()">
<h3>unloadDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unloadDiagram</span>()
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Disposes all symbols and creates not loaded data.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalClearOnUnload()">
<h3>internalClearOnUnload</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalClearOnUnload</span>()</div>
</section>
</li>
<li>
<section class="detail" id="recalculateInternalDataRequired()">
<h3>recalculateInternalDataRequired</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">recalculateInternalDataRequired</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isLoaded()">
<h3>isLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span>()</div>
<div class="block">Check if the diagram is loaded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram contents is loaded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentState()">
<h3>getContentState</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.DiagramContentState</span> <span class="element-name">getContentState</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ensureLoaded()">
<h3>ensureLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensureLoaded</span>()</div>
<div class="block">Ensures that the diagram is loaded.
 If the diagram is not loaded, load it.
 Make sure the project is active before invoking this method.
 Otherwise, the diagram may not be loaded.</div>
</section>
</li>
<li>
<section class="detail" id="loadContents(com.nomagic.task.ProgressStatus)">
<h3>loadContents</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadContents</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Loads diagram to memory.
 This method should be used only when the diagram is not loaded.
 Make sure the project is active before invoking this method.
 Otherwise, the diagram may not be loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - progress status.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cleanupAfterLoad()">
<h3>cleanupAfterLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cleanupAfterLoad</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isForceStoreContentOnSave()">
<h3>isForceStoreContentOnSave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isForceStoreContentOnSave</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setForceStoreContentOnSave(boolean)">
<h3>setForceStoreContentOnSave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setForceStoreContentOnSave</span><wbr/><span class="parameters">(boolean forceStoreContentOnSave)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetForceStoreContentOnSave(boolean)">
<h3>sSetForceStoreContentOnSave</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">sSetForceStoreContentOnSave</span><wbr/><span class="parameters">(boolean forceStoreContentOnSave)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDiagramTypeAsString()">
<h3>getDiagramTypeAsString</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramTypeAsString</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRealType()">
<h3>getRealType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRealType</span>()</div>
<div class="block">Returns real diagram type. Real diagram type is a diagram type that is not registered but was persisted before.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>real type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseFlowLayoutLogic()">
<h3>isUseFlowLayoutLogic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseFlowLayoutLogic</span>()</div>
</section>
</li>
<li>
<section class="detail" id="layout(boolean)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)"><code>Layouting.layout(AbstractDiagramPresentationElement)</code></a> or <code>com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement)</code></div>
</div>
<div class="block">Layout the diagram using default layouter.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a>} to select symbols in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in the project's command history.</dd>
<dt>Returns:</dt>
<dd>true if layout was performed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String)"><code>Layouting.layout(AbstractDiagramPresentationElement, String)</code></a> or <code>com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String)</code></div>
</div>
<div class="block">Layouts the diagram with the specified layouter.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a>} to select symbols in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in the project's command history</dd>
<dd><code>layouter</code> - layouter to be used for layouting</dd>
<dt>Returns:</dt>
<dd>true if layout was performed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> diagramLayouter,
 <a href="../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="layout/Layouting.html#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)"><code>Layouting.layout(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)</code></a> or <code>com.nomagic.magicdraw.uml.symbols.layout.Layouting#layoutNoSession(AbstractDiagramPresentationElement, String, AbstractDiagramLayouterOptionsGroup)</code></div>
</div>
<div class="block">Layout the diagram.
 Only selected symbols in the diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a>} to select symbols in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in the project's command history</dd>
<dd><code>diagramLayouter</code> - layouter to use</dd>
<dd><code>options</code> - layout options</dd>
<dt>Returns:</dt>
<dd>true if layout was performed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultDiagramLayouter()">
<h3>getDefaultDiagramLayouter</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></span> <span class="element-name">getDefaultDiagramLayouter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowDiagramFrame()">
<h3>isShowDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDiagramFrame</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramFrame()">
<h3>getDiagramFrame</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public abstract</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</span> <span class="element-name">getDiagramFrame</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetDiagramFrame(com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView)">
<h3>sSetDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetDiagramFrame</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView symbol)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateFrameSize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>updateFrameSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateFrameSize</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="applyForcedProperties()">
<h3>applyForcedProperties</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">applyForcedProperties</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentationFromModelElement()">
<h3>getRepresentationFromModelElement</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">com.nomagic.magicdraw.core.diagram.DiagramRepresentationObject</span> <span class="element-name">getRepresentationFromModelElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="registerInProject()">
<h3>registerInProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerInProject</span>()</div>
</section>
</li>
<li>
<section class="detail" id="unregisterFromProject()">
<h3>unregisterFromProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unregisterFromProject</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramType()">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a href="../AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></span> <span class="element-name">getDiagramType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="postOpenFromCommand()">
<h3>postOpenFromCommand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">postOpenFromCommand</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getZoom()">
<h3>getZoom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">getZoom</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPathToMoveCache()">
<h3>getPathToMoveCache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.PathToMoveCache</span> <span class="element-name">getPathToMoveCache</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>paths to move cache</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentHash()">
<h3>getContentHash</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getContentHash</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setContentHash(java.lang.String)">
<h3>setContentHash</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContentHash</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contentHash)</span></div>
<div class="block">Sets identifier of contents.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contentHash</code> - content hash</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShapesAutoResizeSuspended()">
<h3>isShapesAutoResizeSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShapesAutoResizeSuspended</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetShapesAutoResizeSuspended(boolean)">
<h3>sSetShapesAutoResizeSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShapesAutoResizeSuspended</span><wbr/><span class="parameters">(boolean enabled)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShapesAutoResizeSuspended(boolean)">
<h3>setShapesAutoResizeSuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShapesAutoResizeSuspended</span><wbr/><span class="parameters">(boolean enabled)</span></div>
</section>
</li>
<li>
<section class="detail" id="autosizeSuspendedSymbolsWithHiddenContent()">
<h3>autosizeSuspendedSymbolsWithHiddenContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosizeSuspendedSymbolsWithHiddenContent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isLabelsAutoDisplaySuspended()">
<h3>isLabelsAutoDisplaySuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLabelsAutoDisplaySuspended</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetLabelsAutoDisplaySuspended(boolean)">
<h3>sSetLabelsAutoDisplaySuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetLabelsAutoDisplaySuspended</span><wbr/><span class="parameters">(boolean enabled)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLabelsAutoDisplaySuspended(boolean)">
<h3>setLabelsAutoDisplaySuspended</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLabelsAutoDisplaySuspended</span><wbr/><span class="parameters">(boolean enabled)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSuspendShapeAutoResizeMode()">
<h3>getSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuspendShapeAutoResizeMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetSuspendShapeAutoResizeMode(java.lang.String)">
<h3>sSetSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSuspendShapeAutoResizeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSuspendShapeAutoResizeMode(java.lang.String)">
<h3>setSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuspendShapeAutoResizeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
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
<dd><code><a href="PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModified()">
<h3>isModified</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isModified</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setModified(boolean)">
<h3>setModified</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModified</span><wbr/><span class="parameters">(boolean modified)</span></div>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Check of given symbol can be added as child into this symbol.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>symbol</code> - symbol</dd>
<dt>Returns:</dt>
<dd>true if symbol can be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds a presentation element for a given model element of a given symbol type in this diagram.
 Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement.</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds a presentation element for a given model element of the given symbol type in this diagram. Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement.</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElements(java.util.function.Predicate)">
<h3>findPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">findPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; predicate)</span></div>
<div class="block">Finds manipulated presentation elements matching given predicate. Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>predicate</code> - predicate</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElements(java.lang.Class)">
<h3>findPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="type-parameters">&lt;S extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span>
<span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;S&gt;</span> <span class="element-name">findPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;S&gt; classType)</span></div>
<div class="block">Finds manipulated presentation elements matching given class type. Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classType</code> - class type</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">
<h3>findPresentationElementForPathConnecting</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElementForPathConnecting</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.
 Does recursive search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findPresentationElementsForPathConnecting</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">findPresentationElementsForPathConnecting</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.
 Does recursive search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>a stream of presentation elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()</div>
<div class="block">Delegate bounds request to its container.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getBounds()">getBounds</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>bounds</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>PresentationElementsManager.reshapeShapeElement</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOpenConfigurator(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator)">
<h3>setOpenConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpenConfigurator</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator openConfigurator)</span></div>
<div class="block">Sets open configurator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>openConfigurator</code> - open configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpenConfigurator()">
<h3>getOpenConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement.OpenConfigurator</span> <span class="element-name">getOpenConfigurator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="initialize()">
<h3>initialize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initialize</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#initialize()">PresentationElement</a></code></span></div>
<div class="block">Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#initialize()">initialize</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitializer(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer)">
<h3>setInitializer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitializer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElementInitializer initializer)</span></div>
<div class="block">Sets custom diagram presentation element initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - custom diagram presentation element initializer.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open()">
<h3>open</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span>()</div>
<div class="block">Open the diagram</div>
</section>
</li>
<li>
<section class="detail" id="open(boolean)">
<h3>open</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span><wbr/><span class="parameters">(boolean showProgress)</span></div>
<div class="block">Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open(boolean,boolean)">
<h3>open</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span><wbr/><span class="parameters">(boolean loadContent,
 boolean showProgress)</span></div>
<div class="block">Open the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>loadContent</code> - load diagram content</dd>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openInActiveTab(boolean)">
<h3>openInActiveTab</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openInActiveTab</span><wbr/><span class="parameters">(boolean showProgress)</span></div>
<div class="block">Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open(boolean,boolean,boolean)">
<h3>open</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span><wbr/><span class="parameters">(boolean loadContent,
 boolean showProgress,
 boolean inActiveTab)</span></div>
<div class="block">Open the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>loadContent</code> - load diagram content</dd>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOpening()">
<h3>isOpening</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOpening</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the diagram is in opening mode at the moment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">close</span>()</div>
<div class="block">Closes diagram window.</div>
</section>
</li>
<li>
<section class="detail" id="close(boolean)">
<h3>close</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">close</span><wbr/><span class="parameters">(boolean closeWindow)</span></div>
<div class="block">Closes opened diagram
 If closeWindow is 'false' and there is a possibility to back to the previous diagram in that window, when the previous diagram is opened
 Otherwise, diagram window is closed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>closeWindow</code> - if a window should be closed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLineJumpPlace()">
<h3>getLineJumpPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.LineJumpPlace</span> <span class="element-name">getLineJumpPlace</span>()</div>
<div class="block">Returns current line jump place value of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>line jump place mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace)">
<h3>sSetLineJumpPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetLineJumpPlace</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)</span></div>
<div class="block">Sets value of line jump place.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineJumpPlace</code> - line jump place mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramOrientationMode()">
<h3>getDiagramOrientationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramOrientationMode</span>()</div>
<div class="block">Gets diagram orientation mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram orientation mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasVerticalOrientation()">
<h3>hasVerticalOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasVerticalOrientation</span>()</div>
<div class="block">Returns true if diagram has vertical orientation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the diagram has vertical orientation, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBackgroundColor()">
<h3>getBackgroundColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getBackgroundColor</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>background color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseGradientForFill(boolean)">
<h3>setUseGradientForFill</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseGradientForFill</span><wbr/><span class="parameters">(boolean use)</span></div>
<div class="block">Sets elements gradient fill option. Will presentation element use gradient fill, or not for painting.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>use</code> - true to use.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseGradientForFill()">
<h3>isUseGradientForFill</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseGradientForFill</span>()</div>
<div class="block">Do we need to use gradient for fill color? Returns value of fill gradient property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>True, when use gradient fill property is true.</dd>
</dl>
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
<dd><code><a href="PresentationElement.html#internalSilentApply()">internalSilentApply</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
<dd><code><a href="PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preferredSize(java.awt.Dimension)">
<h3>preferredSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">preferredSize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dim)</span></div>
</section>
</li>
<li>
<section class="detail" id="recursiveAutosize()">
<h3>recursiveAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">recursiveAutosize</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="PresentationElement.html#recursiveAutosize()">PresentationElement</a></code></span></div>
<div class="block">Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#recursiveAutosize()">recursiveAutosize</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateInitialDiagramFrameBounds()">
<h3>calculateInitialDiagramFrameBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">calculateInitialDiagramFrameBounds</span>()</div>
<div class="block">Gets bounds which should be set for the diagram's frame.</div>
</section>
</li>
<li>
<section class="detail" id="adjustInitialDiagramFrameBounds(java.awt.Rectangle)">
<h3>adjustInitialDiagramFrameBounds</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">adjustInitialDiagramFrameBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Adjust initial diagram frame bounds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitialDiagramFrameBounds()">
<h3>setInitialDiagramFrameBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitialDiagramFrameBounds</span>()</div>
<div class="block">Sets initial diagram frame bounds for this diagram's frame.</div>
</section>
</li>
<li>
<section class="detail" id="getOwnStyleDelegate()">
<h3>getOwnStyleDelegate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.DiagramStylePropertyDelegate</span> <span class="element-name">getOwnStyleDelegate</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a></code> in class <code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>the own style property delegate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setZoomProvider(java.util.function.Function)">
<h3>setZoomProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setZoomProvider</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a>&gt; provider)</span></div>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object,T)">
<h3 id="setValue(java.lang.Object,java.lang.Object)">setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> key,
 @CheckForNull
 T value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getValue(java.lang.Object)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> key)</span></div>
</section>
</li>
<li>
<section class="detail" id="getValueOrCompute(java.lang.Object,java.util.function.Supplier)">
<h3>getValueOrCompute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">getValueOrCompute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; valueSupplier)</span></div>
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
