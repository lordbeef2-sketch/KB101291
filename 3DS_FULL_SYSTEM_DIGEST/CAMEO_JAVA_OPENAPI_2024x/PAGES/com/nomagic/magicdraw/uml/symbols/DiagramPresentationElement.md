# JAVA OPENAPI: DiagramPresentationElement (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/DiagramPresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DiagramPresentationElement.html`
- source_sha256: `7e0b3f58053c14c7c4b8a3d1aebd7c869e8d88b7c79fd58ae0f98d7e279247e5`
- captured_utc: `2026-07-14T16:52:11.606875+00:00`

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
`com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer`, `[BaseElement](../BaseElement.html)`, `[MDElement](../MDElement.html)`, `[ModelElementProvider](../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner`, `[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classDiagramPresentationElement
extends [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)
implements com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner, [StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html), com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer

Class for representing UML diagram. Diagram purpose is to contain set of presentation elements. 

 For diagram creation use [`ModelElementsManager`](../../openapi/uml/ModelElementsManager.html) class. 

 For working with diagram presentation elements use
 [`PresentationElementsManager`](../../openapi/uml/PresentationElementsManager.html) class.

See Also:
[`ModelElementsManager`](../../openapi/uml/ModelElementsManager.html)
[`PresentationElementsManager`](../../openapi/uml/PresentationElementsManager.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[DASHED_STROKE](PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](shapes/StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramPresentationElement](#%3Cinit%3E())()`
Constructs new empty diagram.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../Visitor.html) visitor)`
Method accepts visitor, and calls method visit<class name>(this) of visitor .
`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getDiagram](#getDiagram())()`
Returns Diagram model element of this presentation element.
`[DiagramFrameView](shapes/DiagramFrameView.html)`
`[getDiagramFrame](#getDiagramFrame())()`
Get the frame of the diagram.
`[DiagramType](../DiagramType.html)`
`[getDiagramType](#getDiagramType())()`
Returns the type of the diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements())()`
Returns collection of model elements that have views in this diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements(boolean))(boolean checkOnlyPersistent)`
Deprecated.
checkOnlyPersistent parameter is ignored.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUsedModelElements](#getUsedModelElements(com.nomagic.magicdraw.core.diagram.UsedElementPolicy))([UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)`
Returns collection of model elements that are used in this diagram.
`boolean`
`[isElementInDiagram](#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks if given element exist in any diagram.
`boolean`
`[isElementInDiagram](#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.core.diagram.UsedElementPolicy))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [UsedElementPolicy](../../core/diagram/UsedElementPolicy.html) usedElementPolicy)`
Checks if given element exist in any diagram.
`boolean`
`[isInitialFrameSizeSet](#isInitialFrameSizeSet())()`

`void`
`[setDiagramType](#setDiagramType(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](../DiagramType.html) type)`
Sets the type of the diagram and fires
 the property change event with name ExtendedPropertyNames.EDIT_DIAGRAM_TYPE .
`void`
`[setInitialFrameSizeSet](#setInitialFrameSizeSet(boolean))(boolean value)`
Set a flag that diagram frame size should not be recalculated on opening.
`void`
`[sSetDiagramType](#sSetDiagramType(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](../DiagramType.html) type)`
Sets the type of the diagram.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)
`[addContentPropertyChangeListener](AbstractDiagramPresentationElement.html#addContentPropertyChangeListener(java.beans.PropertyChangeListener)), [close](AbstractDiagramPresentationElement.html#close()), [collectPresentationElementsRecursively](AbstractDiagramPresentationElement.html#collectPresentationElementsRecursively()), [collectShowingManipulatedElementsRecursively](AbstractDiagramPresentationElement.html#collectShowingManipulatedElementsRecursively()), [collectShowingPresentationElementsRecursively](AbstractDiagramPresentationElement.html#collectShowingPresentationElementsRecursively()), [ensureLoaded](AbstractDiagramPresentationElement.html#ensureLoaded()), [findPresentationElement](AbstractDiagramPresentationElement.html#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)), [findPresentationElement](AbstractDiagramPresentationElement.html#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findPresentationElementForPathConnecting](AbstractDiagramPresentationElement.html#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)), [findPresentationElementsForPathConnecting](AbstractDiagramPresentationElement.html#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [isLoaded](AbstractDiagramPresentationElement.html#isLoaded()), [isSymbolDiagram](AbstractDiagramPresentationElement.html#isSymbolDiagram()), [layout](AbstractDiagramPresentationElement.html#layout(boolean)), [layout](AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)), [layout](AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [open](AbstractDiagramPresentationElement.html#open()), [open](AbstractDiagramPresentationElement.html#open(boolean)), [openInActiveTab](AbstractDiagramPresentationElement.html#openInActiveTab(boolean)), [removeContentPropertyChangeListener](AbstractDiagramPresentationElement.html#removeContentPropertyChangeListener(java.beans.PropertyChangeListener))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[addProperty](PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [collectSubManipulatedElements](PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [getBoundsShape](PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getDiagramPresentationElement](PresentationElement.html#getDiagramPresentationElement()), [getManipulatedParent](PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](PresentationElement.html#getManipulatedPresentationElements()), [getMiddlePoint](PresentationElement.html#getMiddlePoint()), [getObjectParent](PresentationElement.html#getObjectParent()), [getParent](PresentationElement.html#getParent()), [getPreferredDimension](PresentationElement.html#getPreferredDimension()), [getPreferredSize](PresentationElement.html#getPreferredSize()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke(int)), [getPropertyManager](PresentationElement.html#getPropertyManager()), [getSelected](PresentationElement.html#getSelected()), [getStroke](PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](PresentationElement.html#getStroke(int)), [getStroke](PresentationElement.html#getStroke(int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int,int)), [getStroke](PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](PresentationElement.html#isSelected()), [onFind](PresentationElement.html#onFind()), [onFind](PresentationElement.html#onFind(boolean)), [setAllSelected](PresentationElement.html#setAllSelected(boolean)), [setSelected](PresentationElement.html#setSelected(boolean)), [setSelected](PresentationElement.html#setSelected(java.util.List))`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getCommandForAppending, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramPresentationElement
@OpenApipublic DiagramPresentationElement()
Constructs new empty diagram.
 Do not use this constructor to create a diagram explicitly.
 Open API provides method for diagrams creation.
See Also:
[`ModelElementsManager.createDiagram(String, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)`](../../openapi/uml/ModelElementsManager.html#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))
 ============ METHOD DETAIL ========== 
Method Details
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
getDiagramType
@OpenApipublic [DiagramType](../DiagramType.html) getDiagramType()
Returns the type of the diagram.
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
getDiagram
@OpenApipublic [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getDiagram()
Returns Diagram model element of this presentation element.
Returns:
Diagram object of this element.
See Also:
[`getElement()`](#getElement())
accept
@OpenApipublic void accept([Visitor](../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts visitor, and calls method visit<class name>(this) of visitor .
 See Visitor pattern for more details.
Specified by:
`[accept](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../MDElement.html)`
Overrides:
`[accept](AbstractDiagramPresentationElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in class `[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
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
getDiagramFrame
@OpenApi
@CheckForNullpublic [DiagramFrameView](shapes/DiagramFrameView.html) getDiagramFrame()
Get the frame of the diagram.
Returns:
frame of the diagram.
isInitialFrameSizeSet
@OpenApipublic boolean isInitialFrameSizeSet()
Returns:
false if diagram frame size should not be recalculated on opening.
setInitialFrameSizeSet
@OpenApipublic void setInitialFrameSizeSet(boolean value)
Set a flag that diagram frame size should not be recalculated on opening.
Parameters:
`value` - new value

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
<dd><code>com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</code>, <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner</code>, <code><a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramPresentationElement</span>
<span class="extends-implements">extends <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>
implements com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderOwner, <a href="shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a>, com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</span></div>
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
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
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
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts visitor, and calls method visit&lt;class name&gt;(this) of visitor .</div>
</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType()">getDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type of the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedModelElements()">getUsedModelElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns collection of model elements that have views in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getUsedModelElements(boolean)">getUsedModelElements</a><wbr/>(boolean checkOnlyPersistent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">checkOnlyPersistent parameter is ignored.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedModelElements(com.nomagic.magicdraw.core.diagram.UsedElementPolicy)">getUsedModelElements</a><wbr/>(<a href="../../core/diagram/UsedElementPolicy.html" title="enum class in com.nomagic.magicdraw.core.diagram">UsedElementPolicy</a> usedElementPolicy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns collection of model elements that are used in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isElementInDiagram</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDiagramType(com.nomagic.magicdraw.uml.DiagramType)">setDiagramType</a><wbr/>(<a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the type of the diagram and fires
 the property change event with name ExtendedPropertyNames.EDIT_DIAGRAM_TYPE .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitialFrameSizeSet(boolean)">setInitialFrameSizeSet</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a flag that diagram frame size should not be recalculated on opening.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetDiagramType(com.nomagic.magicdraw.uml.DiagramType)">sSetDiagramType</a><wbr/>(<a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the type of the diagram.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></h3>
<code><a href="AbstractDiagramPresentationElement.html#addContentPropertyChangeListener(java.beans.PropertyChangeListener)">addContentPropertyChangeListener</a>, <a href="AbstractDiagramPresentationElement.html#close()">close</a>, <a href="AbstractDiagramPresentationElement.html#collectPresentationElementsRecursively()">collectPresentationElementsRecursively</a>, <a href="AbstractDiagramPresentationElement.html#collectShowingManipulatedElementsRecursively()">collectShowingManipulatedElementsRecursively</a>, <a href="AbstractDiagramPresentationElement.html#collectShowingPresentationElementsRecursively()">collectShowingPresentationElementsRecursively</a>, <a href="AbstractDiagramPresentationElement.html#ensureLoaded()">ensureLoaded</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">findPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElement</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">findPresentationElementForPathConnecting</a>, <a href="AbstractDiagramPresentationElement.html#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElementsForPathConnecting</a>, <a href="AbstractDiagramPresentationElement.html#isLoaded()">isLoaded</a>, <a href="AbstractDiagramPresentationElement.html#isSymbolDiagram()">isSymbolDiagram</a>, <a href="AbstractDiagramPresentationElement.html#layout(boolean)">layout</a>, <a href="AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">layout</a>, <a href="AbstractDiagramPresentationElement.html#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">layout</a>, <a href="AbstractDiagramPresentationElement.html#open()">open</a>, <a href="AbstractDiagramPresentationElement.html#open(boolean)">open</a>, <a href="AbstractDiagramPresentationElement.html#openInActiveTab(boolean)">openInActiveTab</a>, <a href="AbstractDiagramPresentationElement.html#removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">removeContentPropertyChangeListener</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="PresentationElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="PresentationElement.html#getParent()">getParent</a>, <a href="PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="PresentationElement.html#getSelected()">getSelected</a>, <a href="PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="PresentationElement.html#getStroke(int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="PresentationElement.html#isSelected()">isSelected</a>, <a href="PresentationElement.html#onFind()">onFind</a>, <a href="PresentationElement.html#onFind(boolean)">onFind</a>, <a href="PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="PresentationElement.html#setSelected(java.util.List)">setSelected</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getCommandForAppending, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a></code></div>
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
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
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
<section class="detail" id="getDiagramType()">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">getDiagramType</span>()</div>
<div class="block">Returns the type of the diagram.</div>
<dl class="notes">
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
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts visitor, and calls method visit&lt;class name&gt;(this) of visitor .
 See Visitor pattern for more details.</div>
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
<section class="detail" id="getDiagramFrame()">
<h3>getDiagramFrame</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="shapes/DiagramFrameView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">DiagramFrameView</a></span> <span class="element-name">getDiagramFrame</span>()</div>
<div class="block">Get the frame of the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>frame of the diagram.</dd>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
