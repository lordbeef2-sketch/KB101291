# JAVA OPENAPI: PresentationElementsManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/openapi/uml/PresentationElementsManager.html
- source_path: `com/nomagic/magicdraw/openapi/uml/PresentationElementsManager.html`
- source_sha256: `338d6650b5b4fae727ac067b4fd04525b080b6d37875c53ca5847fa5b48e6b47`
- captured_utc: `2026-07-14T16:55:24.905115+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.openapi.uml](package-summary.html)

## Class PresentationElementsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.openapi.uml.PresentationElementsManager

@OpenApiAllpublic classPresentationElementsManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

The utility class for ShapesElements and PathElement creating, moving and properties changing.
 Works together with `SessionManager`.
 This manager can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.

See Also:
[`SessionManager`](SessionManager.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[PresentationElementsManager](#%3Cinit%3E())()`
Private constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[changePathBreakPoints](#changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List))([PathElement](../../uml/symbols/paths/PathElement.html) element,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) newBreakPoints)`
Changes the break points of the given PathElement.
`void`
`[changePathPoints](#changePathPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.awt.Point,java.awt.Point,java.util.List))([PathElement](../../uml/symbols/paths/PathElement.html) element,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newBreakPoints)`
Changes the points of the given PathElement.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[connectComment](#connectComment(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) comment,
 [PresentationElement](../../uml/symbols/PresentationElement.html) target)`
Connects given comment with note anchor to the given presentation element.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[connectNote](#connectNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) noteOrComment,
 [PresentationElement](../../uml/symbols/PresentationElement.html) target)`
Connects given note or comment shape with an anchor to the given presentation element.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[createContainmentLink](#createContainmentLink(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) parentView,
 [PresentationElement](../../uml/symbols/PresentationElement.html) childView)`
Connects given parent and child elements with a containment link.
`[ContentShape](../../uml/symbols/shapes/ContentShape.html)`
`[createContentShape](#createContentShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) pack)`
Creates a ContentShape in the given parent.
`[DurationConstraintView](../../uml/symbols/paths/DurationConstraintView.html)`
`[createDurationConstraint](#createDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement))([DurationConstraint](../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) durationConstraint,
 [PathElement](../../uml/symbols/paths/PathElement.html) firstConstrainedView,
 [PathElement](../../uml/symbols/paths/PathElement.html) secondConstrainedView)`
Creates DurationConstraint presentation element between the given two end views, that can be either
 SeqMessageView or ActivationView
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[createFoundMessage](#createFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int))([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) from,
 [Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) insertAfter,
 int verticalGap)`
Creates a found message symbol for a given message from the given shape element.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createGenericView](#createGenericView(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) identifier)`
Creates Generic view
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createImageShape](#createImageShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.io.File))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) imageFile)`
Creates an image shape in the given parent.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createImageShape](#createImageShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.io.File,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) imageFile,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates an image shape in the given parent.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[createLostMessage](#createLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int))([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) from,
 [Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) insertAfter,
 int verticalGap)`
Creates a lost message symbol for a given message from the given shape element.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createNote](#createNote(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) parent)`
Creates a note in the given parent.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createNote](#createNote(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates a note in the given parent.
`[PartView](../../uml/symbols/shapes/PartView.html)`
`[createPartShape](#createPartShape(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,boolean,java.awt.Point))([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) part,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> nestedPath,
 boolean createRelationships,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates part shape on the diagram at a given coordinate.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[createPathElement](#createPathElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [PresentationElement](../../uml/symbols/PresentationElement.html) client,
 [PresentationElement](../../uml/symbols/PresentationElement.html) supplier)`
Creates a PathElement for given relationship between given client and supplier PresentationElements.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createPathToSelfShapeElement](#createPathToSelfShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [PresentationElement](../../uml/symbols/PresentationElement.html) client)`

`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createRectangularShape](#createRectangularShape(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) parent)`
Creates a rectangular shape in the given parent.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createRectangularShape](#createRectangularShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates a rectangular shape in the given parent.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createSeparator](#createSeparator(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) parent)`
Creates a separator shape in the given parent.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createSeparator](#createSeparator(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates a separator shape in the parent.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[createSequenceMessage](#createSequenceMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean,int,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int))([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [MessageSort](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html) sort,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) from,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) to,
 boolean recursive,
 int diagonal,
 [Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) insertAfter,
 int verticalGap)`
Creates a PathElement for given message between given client (from) and supplier (to) PresentationElements.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createShapeElement](#createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent)`
Creates a ShapeElement for given ModelElement in the given diagram.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createShapeElement](#createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 boolean createRelationships)`
Creates a ShapeElement for given ModelElement in the given diagram.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createShapeElement](#createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.awt.Point))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 boolean createRelationships,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates a ShapeElement for given ModelElement in the given diagram.
`[SwimlaneView](../../uml/symbols/shapes/SwimlaneView.html)`
`[createSwimlane](#createSwimlane(java.util.List,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [ActivityPartition](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html)> horizontal,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [ActivityPartition](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html)> vertical,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)`
Creates a swimlane in a given diagram.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createTextBox](#createTextBox(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) parent)`
Creates a text box in the given parent.
`[ShapeElement](../../uml/symbols/shapes/ShapeElement.html)`
`[createTextBox](#createTextBox(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Creates a text box in the given parent.
`[PathElement](../../uml/symbols/paths/PathElement.html)`
`[createVirtualRelation](#createVirtualRelation(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([PresentationElement](../../uml/symbols/PresentationElement.html) clientView,
 [PresentationElement](../../uml/symbols/PresentationElement.html) supplierView,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ruleKey)`
Creates Virtual Relation view
`void`
`[deletePresentationElement](#deletePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) element)`
Removes given element from the diagram.
`static [PresentationElementsManager](PresentationElementsManager.html)`
`[getInstance](#getInstance())()`
Returns an instance of this manager.
`protected boolean`
`[isPresentationElementEditable](#isPresentationElementEditable(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) element)`

`void`
`[movePresentationElement](#movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Moves a presentation element to the given parent and the specified location.
`void`
`[movePresentationElement](#movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,boolean))([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 boolean canChangeElementOwner)`
Moves a presentation element to the given parent and the specified location.
`void`
`[movePresentationElement](#movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Moves a presentation element to the specified location.
`void`
`[movePresentationElements](#movePresentationElements(java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> views,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Moves a list of presentation elements to the given parent and the specified location.
`void`
`[movePresentationElements](#movePresentationElements(java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,boolean))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> views,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 boolean canChangeElementOwner)`
Moves a list of presentation elements to the given parent and the specified location.
`void`
`[movePresentationElements](#movePresentationElements(java.util.List,java.awt.Point))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> views,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Moves a list of presentation elements to the specified location.
`void`
`[resetLabelPositions](#resetLabelPositions(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../../uml/symbols/paths/PathElement.html) element)`
Moves all given PathElement's labels to the default positions (for example, the default position for name label is the middle of the path).
`void`
`[reshapeShapeElement](#reshapeShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle))([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) element,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) newBounds)`
Reshapes given ShapeElement.
`void`
`[setConstraintForNote](#setConstraintForNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) note,
 [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Shows given constraint in the given note.
`void`
`[setPresentationElementProperties](#setPresentationElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.PropertyManager))([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [PropertyManager](../../properties/PropertyManager.html) propertyManager)`
Changes symbol properties of a given presentation element.
`void`
`[setText](#setText(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.lang.String))([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) shape,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Sets text for given symbol.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PresentationElementsManager
protected PresentationElementsManager()
Private constructor. Do not allow creating instance outside this class.
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [PresentationElementsManager](PresentationElementsManager.html) getInstance()
Returns an instance of this manager.
Returns:
instance of this manager.
createShapeElement
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createShapeElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a ShapeElement for given ModelElement in the given diagram.
 The created shape location is (0,0). The relationships to other symbols are not created.
Parameters:
`element` - the given ModelElement to create ShapeElement for.
`parent` - presentation element in which symbol should be created. Method can produce unpredictable results in case created symbol is illegal in such a parent. Valid combination is such as package in package, class in package, etc.
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createShapeElement
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createShapeElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 boolean createRelationships,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a ShapeElement for given ModelElement in the given diagram.
 The created shape location is (0,0).
Parameters:
`element` - the given ModelElement to create ShapeElement for.
`createRelationships` - create relationships to other symbols or not.
`parent` - presentation element in which symbol should be created. Method can produce unpredictable results in case created symbol is illegal in such a parent. Valid combination is such as package in package, class in package, etc.
`location` - the location where the new symbol is placed
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createShapeElement
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createShapeElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 boolean createRelationships)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a ShapeElement for given ModelElement in the given diagram.
 The created shape location is (0,0).
Parameters:
`element` - the given ModelElement to create ShapeElement for.
`createRelationships` - create relationships to other symbols or not.
`parent` - presentation element in which symbol should be created. Method can produce unpredictable results in case created symbol is illegal in such a parent. Valid combination is such as package in package, class in package, etc.
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createPathElement
public [PathElement](../../uml/symbols/paths/PathElement.html) createPathElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [PresentationElement](../../uml/symbols/PresentationElement.html) client,
 [PresentationElement](../../uml/symbols/PresentationElement.html) supplier)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a PathElement for given relationship between given client and supplier PresentationElements.
 The PathElement will be created in the same diagram as client's and supplier's PresentationElements are. 

 ModelElement of a client must be equal to relationship's client. 

 ModelElement of supplier must be equal to relationship's supplier.
Parameters:
`relationship` - the given relationship.
`client` - a PresentationElement of relationship client.
`supplier` - a PresentationElement of relationship supplier.
Returns:
created PathElement for given a relationship.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createPathToSelfShapeElement
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createPathToSelfShapeElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [PresentationElement](../../uml/symbols/PresentationElement.html) client)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)`
deletePresentationElement
public void deletePresentationElement([PresentationElement](../../uml/symbols/PresentationElement.html) element)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Removes given element from the diagram.
Parameters:
`element` - the element to remove.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
isPresentationElementEditable
protected boolean isPresentationElementEditable([PresentationElement](../../uml/symbols/PresentationElement.html) element)
movePresentationElement
public void movePresentationElement([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves a presentation element to the given parent and the specified location.
 During this operation parent of the symbol can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.
Parameters:
`view` - presentation element to move.
`parent` - parent to move into.
`location` - location to move to.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
movePresentationElement
public void movePresentationElement([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 boolean canChangeElementOwner)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves a presentation element to the given parent and the specified location.
 During this operation parent of the symbol can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.
Parameters:
`view` - presentation element to move.
`parent` - parent to move into.
`location` - location to move to.
`canChangeElementOwner` - allow changing an Element owner if needed by symbols structure
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
movePresentationElement
public void movePresentationElement([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves a presentation element to the specified location.
 During this operation, the parent of the symbol does not change, only geometrical position changes.
Parameters:
`view` - symbol to move.
`location` - location to move to.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
movePresentationElements
public void movePresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> views,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves a list of presentation elements to the given parent and the specified location.
 During this operation parent of symbols can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.
Parameters:
`views` - presentation elements to move.
`parent` - parent to move into.
`location` - location to move to.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
movePresentationElements
public void movePresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> views,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 boolean canChangeElementOwner)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves a list of presentation elements to the given parent and the specified location.
 During this operation parent of symbols can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.
Parameters:
`views` - presentation elements to move.
`parent` - parent to move into.
`location` - location to move to.
`canChangeElementOwner` - allow changing an Element owner if needed by symbols structure
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
movePresentationElements
public void movePresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> views,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves a list of presentation elements to the specified location.
 During this operation parent of symbols does not change.
Parameters:
`views` - presentation elements to move.
`location` - location to move to.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
reshapeShapeElement
public void reshapeShapeElement([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) element,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) newBounds)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Reshapes given ShapeElement.
Parameters:
`element` - the ShapeElement to reshape.
`newBounds` - a new bounds of the element.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if an element is read-only.
changePathBreakPoints
public void changePathBreakPoints([PathElement](../../uml/symbols/paths/PathElement.html) element,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) newBreakPoints)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Changes the break points of the given PathElement.
 The order of break points is from supplier to client.
Parameters:
`element` - the given PathElement.
`newBreakPoints` - a list of new PathElement break points
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is read-only and can't edit.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if a given element is null or if given breakpoints are null
changePathPoints
public void changePathPoints([PathElement](../../uml/symbols/paths/PathElement.html) element,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newBreakPoints)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Changes the points of the given PathElement.
 The order of break points is from supplier to client.
Parameters:
`element` - the given PathElement.
`supplierPoint` - new supplier
`clientPoint` - new client point
`newBreakPoints` - a list of new PathElement break points
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is read-only and can't edit
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if a given element is null or if given breakpoints are null
resetLabelPositions
public void resetLabelPositions([PathElement](../../uml/symbols/paths/PathElement.html) element)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves all given PathElement's labels to the default positions (for example, the default position for name label is the middle of the path).
Parameters:
`element` - the given PathElement to reset labels for.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if a given element is null.
setPresentationElementProperties
public void setPresentationElementProperties([PresentationElement](../../uml/symbols/PresentationElement.html) view,
 [PropertyManager](../../properties/PropertyManager.html) propertyManager)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Changes symbol properties of a given presentation element.
 Make sure to pass the newly created or cloned property manager, not the old one.
 Example:
PresentationElement view = // some view
 ChoiceProperty property = (ChoiceProperty) view.getProperty(PropertyID.TAGGED_VALUES_DISPLAY_MODE);
 // important to create a new property or clone the old one!
 Property clonedProperty = property.clone();
 clonedProperty.setValue(ClassifierView.IN_COMPARTMENT);
 // important to create a new property manager or clone the old one!
 PropertyManager properties = new PropertyManager();
 properties.addProperty(clonedProperty);
 PresentationElementsManager.getInstance().setPresentationElementProperties(view, properties);
Parameters:
`view` - symbol for which to change the property manager.
`propertyManager` - a newly created or cloned manager with new properties. Do not reuse the old property manager
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if a given element is null and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if a given element and properties is null and the element's type can't have properties
createNote
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createNote([PresentationElement](../../uml/symbols/PresentationElement.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a note in the given parent.
 The created shape location is (0,0).
Parameters:
`parent` - the parent to create ShapeElement in
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot edit
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createNote
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createNote([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a note in the given parent.
Parameters:
`parent` - the parent to create Note in
`location` - location of created Note
Returns:
created Note
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if parent is null
createTextBox
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createTextBox([PresentationElement](../../uml/symbols/PresentationElement.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a text box in the given parent.
 The created shape location is (0,0).
Parameters:
`parent` - the parent to create ShapeElement in.
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot edit
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createImageShape
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createImageShape([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) imageFile,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates an image shape in the given parent.
Parameters:
`parent` - the parent to create Image Shape in
`imageFile` - image file
`location` - location of created Image Shape
Returns:
created Image Shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if parent is null
createImageShape
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createImageShape([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) imageFile)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates an image shape in the given parent.
 The created shape location is (0,0).
Parameters:
`parent` - the parent to create Image Shape in
`imageFile` - image file
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if a parent is read-only and cannot edit
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createTextBox
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createTextBox([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a text box in the given parent.
Parameters:
`parent` - the parent to create TextBox in
`location` - location of TextBox
Returns:
created TextBox
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createContentShape
public [ContentShape](../../uml/symbols/shapes/ContentShape.html) createContentShape([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) pack)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a ContentShape in the given parent.
Parameters:
`parent` - the parent to create ContentShape in
`location` - location of shape
`pack` - content shape root content
Returns:
created TextBox
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createSeparator
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createSeparator([PresentationElement](../../uml/symbols/PresentationElement.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a separator shape in the given parent.
 The created shape location is (0,0).
Parameters:
`parent` - the parent to create ShapeElement in
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot edit
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createSeparator
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createSeparator([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a separator shape in the parent.
Parameters:
`parent` - the parent to create Separator in
`location` - location of Separator
Returns:
created Separator
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createRectangularShape
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createRectangularShape([PresentationElement](../../uml/symbols/PresentationElement.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a rectangular shape in the given parent.
 The created shape location is (0,0).
Parameters:
`parent` - the parent to create ShapeElement in
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot edit
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
createRectangularShape
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createRectangularShape([PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a rectangular shape in the given parent.
Parameters:
`parent` - the parent to create Rectangular Shape in
`location` - location of shape
Returns:
created shaped
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only and cannot be edited
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given parent is null
connectNote
public [PathElement](../../uml/symbols/paths/PathElement.html) connectNote([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) noteOrComment,
 [PresentationElement](../../uml/symbols/PresentationElement.html) target)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Connects given note or comment shape with an anchor to the given presentation element.
Parameters:
`noteOrComment` - the given note or comment shape.
`target` - the presentation element to connect note (or comment) to.
Returns:
created anchor.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if note (or comment) is read-only and cannot edit.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given note is not instance of NoteView or comment is not instance of CommentView.
connectComment
public [PathElement](../../uml/symbols/paths/PathElement.html) connectComment([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) comment,
 [PresentationElement](../../uml/symbols/PresentationElement.html) target)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Connects given comment with note anchor to the given presentation element.
Parameters:
`comment` - comment to connect.
`target` - the presentation element to connect comment to.
Returns:
created shape
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if comment is read-only and not editable.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given comment is not an instance of CommentView.
setText
public void setText([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) shape,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Sets text for given symbol. Given symbol can be note, text box or separator.
Parameters:
`shape` - the given symbol.
`text` - a new text for a given symbol.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given node is not an instance of NoteView, TextBoxView, SeparatorView
setConstraintForNote
public void setConstraintForNote([ShapeElement](../../uml/symbols/shapes/ShapeElement.html) note,
 [Constraint](../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Shows given constraint in the given note.
 Constraint must be added into a model already.
 Constraint must be assigned to ModelElement of symbol connected to the given note.
 If these conditions are not true, constraint may not be shown inside the note.
Parameters:
`note` - the given note.
`constraint` - the given constraint.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if note is read-only and cannot edit.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given node is not an instance of NoteView.
createSwimlane
public [SwimlaneView](../../uml/symbols/shapes/SwimlaneView.html) createSwimlane([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [ActivityPartition](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html)> horizontal,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [ActivityPartition](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html)> vertical,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a swimlane in a given diagram.
 Adds horizontal and vertical partitions to the created swimlane.
Parameters:
`horizontal` - list of horizontal partitions
`vertical` - list of vertical partitions
`diagram` - parent for swimlane
Returns:
created swimlane
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given diagram is read-only and cannot edit.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given diagram is null.
createContainmentLink
public [PathElement](../../uml/symbols/paths/PathElement.html) createContainmentLink([PresentationElement](../../uml/symbols/PresentationElement.html) parentView,
 [PresentationElement](../../uml/symbols/PresentationElement.html) childView)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Connects given parent and child elements with a containment link.
Parameters:
`parentView` - the presentation element of the parent element.
`childView` - the presentation element of the child element.
Returns:
created link.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if parent element does not contain child element.
createLostMessage
public [PathElement](../../uml/symbols/paths/PathElement.html) createLostMessage([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) from,
 @CheckForNull
 [Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) insertAfter,
 int verticalGap)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a lost message symbol for a given message from the given shape element.
 The given message is initialized (message ends are created and set, message sort is assigned) in this method.
Parameters:
`message` - the given message
`from` - a ShapeElement of message client lifeline
`insertAfter` - the new message is inserted after this message, or null to insert before all messages
`verticalGap` - vertical gap before the new message
Returns:
created symbol for a given message
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only
createFoundMessage
public [PathElement](../../uml/symbols/paths/PathElement.html) createFoundMessage([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) from,
 @CheckForNull
 [Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) insertAfter,
 int verticalGap)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a found message symbol for a given message from the given shape element.
 The given message is initialized (message ends are created and set, message sort is assigned) in this method.
Parameters:
`message` - the given message
`from` - a ShapeElement of message client lifeline
`insertAfter` - the new message is inserted after this message, or null to insert before all messages
`verticalGap` - vertical gap before the new message
Returns:
created symbol for a given message
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only
createSequenceMessage
public [PathElement](../../uml/symbols/paths/PathElement.html) createSequenceMessage([Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 [MessageSort](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html) sort,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) from,
 [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) to,
 boolean recursive,
 int diagonal,
 @CheckForNull
 [Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) insertAfter,
 int verticalGap)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates a PathElement for given message between given client (from) and supplier (to) PresentationElements.
 The given message is initialized (message ends are created and set, message sort is assigned) in this method.
 The diagram should be opened to make the messages' layout correctly.
Parameters:
`message` - the given message.
`sort` - message sort.
`from` - a ShapeElement of message client lifeline.
`to` - a ShapeElement of message supplier lifeline.
`recursive` - true if a message is recursive (a recursive message can be only when from == to).
`diagonal` - vertical size of a diagonal message, or 0 if the message is not diagonal.
`insertAfter` - the new message is inserted after this message, or null to insert before all messages.
`verticalGap` - vertical gap before the new message.
Returns:
created PathElement for a given message.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createDurationConstraint
@CheckForNullpublic [DurationConstraintView](../../uml/symbols/paths/DurationConstraintView.html) createDurationConstraint([DurationConstraint](../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html) durationConstraint,
 [PathElement](../../uml/symbols/paths/PathElement.html) firstConstrainedView,
 [PathElement](../../uml/symbols/paths/PathElement.html) secondConstrainedView)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates DurationConstraint presentation element between the given two end views, that can be either
 SeqMessageView or ActivationView
Parameters:
`durationConstraint` - model element for the DurationConstraintView
`firstConstrainedView` - first end
`secondConstrainedView` - second end
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is not editable
createPartShape
@CheckForNullpublic [PartView](../../uml/symbols/shapes/PartView.html) createPartShape([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) part,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> nestedPath,
 boolean createRelationships,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates part shape on the diagram at a given coordinate.
 Parent symbol can be specified.
 If a nested parts path is specified, nesting level is displayed in dot notation.
 It can be specified whether to create connected relationships.
Parameters:
`part` - part for which to create a shape.
`parent` - parent symbol in which to add the part.
`nestedPath` - a list of nested parts in which to nest the given part symbol.
`createRelationships` - controls whether to display connected paths.
`location` - location on the diagram where to move the part.
Returns:
created part symbol or null if it was not possible to create it.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createVirtualRelation
@CheckForNullpublic [PathElement](../../uml/symbols/paths/PathElement.html) createVirtualRelation([PresentationElement](../../uml/symbols/PresentationElement.html) clientView,
 [PresentationElement](../../uml/symbols/PresentationElement.html) supplierView,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ruleKey)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates Virtual Relation view
Parameters:
`clientView` - relation client view
`supplierView` - relation supplier view
`ruleKey` - Virtual relation rule key
Returns:
created virtual relation symbol or null if it was not possible to create it.
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.
createGenericView
public [ShapeElement](../../uml/symbols/shapes/ShapeElement.html) createGenericView([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PresentationElement](../../uml/symbols/PresentationElement.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) identifier)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates Generic view
Parameters:
`element` - element for which the generic view is created
`parent` - container
`identifier` - Generic view unique identifier, you can have different Generic views for the same element when the identifier is different
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if diagram is read-only.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.openapi.uml</a></div>
<h1 class="title" title="Class PresentationElementsManager">Class PresentationElementsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.openapi.uml.PresentationElementsManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PresentationElementsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The utility class for ShapesElements and PathElement creating, moving and properties changing.
 Works together with <code>SessionManager</code>.
 <p>
 This manager can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PresentationElementsManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Private constructor.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List)">changePathBreakPoints</a><wbr/>(<a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> newBreakPoints)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changes the break points of the given PathElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changePathPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.awt.Point,java.awt.Point,java.util.List)">changePathPoints</a><wbr/>(<a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newBreakPoints)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changes the points of the given PathElement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#connectComment(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">connectComment</a><wbr/>(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> comment,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Connects given comment with note anchor to the given presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#connectNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">connectNote</a><wbr/>(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> noteOrComment,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Connects given note or comment shape with an anchor to the given presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createContainmentLink(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">createContainmentLink</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parentView,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> childView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Connects given parent and child elements with a containment link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ContentShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ContentShape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createContentShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createContentShape</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> pack)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a ContentShape in the given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/DurationConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DurationConstraintView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">createDurationConstraint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> durationConstraint,
 <a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> firstConstrainedView,
 <a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> secondConstrainedView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates DurationConstraint presentation element between the given two end views, that can be either
 SeqMessageView or ActivationView</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int)">createFoundMessage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> from,
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> insertAfter,
 int verticalGap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a found message symbol for a given message from the given shape element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGenericView(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">createGenericView</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> identifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates Generic view</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.io.File)">createImageShape</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates an image shape in the given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.io.File,java.awt.Point)">createImageShape</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates an image shape in the given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int)">createLostMessage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> from,
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> insertAfter,
 int verticalGap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a lost message symbol for a given message from the given shape element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNote(com.nomagic.magicdraw.uml.symbols.PresentationElement)">createNote</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a note in the given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNote(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">createNote</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a note in the given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPartShape(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,boolean,java.awt.Point)">createPartShape</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> part,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; nestedPath,
 boolean createRelationships,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates part shape on the diagram at a given coordinate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPathElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">createPathElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a PathElement for given relationship between given client and supplier PresentationElements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPathToSelfShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement)">createPathToSelfShapeElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRectangularShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">createRectangularShape</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a rectangular shape in the given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRectangularShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">createRectangularShape</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a rectangular shape in the given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSeparator(com.nomagic.magicdraw.uml.symbols.PresentationElement)">createSeparator</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a separator shape in the given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSeparator(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">createSeparator</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a separator shape in the parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSequenceMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean,int,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int)">createSequenceMessage</a><wbr/>(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> sort,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> from,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> to,
 boolean recursive,
 int diagonal,
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> insertAfter,
 int verticalGap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a PathElement for given message between given client (from) and supplier (to) PresentationElements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement)">createShapeElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a ShapeElement for given ModelElement in the given diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">createShapeElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 boolean createRelationships)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a ShapeElement for given ModelElement in the given diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.awt.Point)">createShapeElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 boolean createRelationships,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a ShapeElement for given ModelElement in the given diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/SwimlaneView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSwimlane(java.util.List,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">createSwimlane</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt; horizontal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt; vertical,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a swimlane in a given diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTextBox(com.nomagic.magicdraw.uml.symbols.PresentationElement)">createTextBox</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a text box in the given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTextBox(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">createTextBox</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a text box in the given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createVirtualRelation(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">createVirtualRelation</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> clientView,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplierView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> ruleKey)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates Virtual Relation view</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deletePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">deletePresentationElement</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given element from the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PresentationElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml">PresentationElementsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an instance of this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPresentationElementEditable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isPresentationElementEditable</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">movePresentationElement</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves a presentation element to the given parent and the specified location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,boolean)">movePresentationElement</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 boolean canChangeElementOwner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves a presentation element to the given parent and the specified location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">movePresentationElement</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves a presentation element to the specified location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePresentationElements(java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">movePresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; views,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves a list of presentation elements to the given parent and the specified location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePresentationElements(java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,boolean)">movePresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; views,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 boolean canChangeElementOwner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves a list of presentation elements to the given parent and the specified location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePresentationElements(java.util.List,java.awt.Point)">movePresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; views,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves a list of presentation elements to the specified location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetLabelPositions(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">resetLabelPositions</a><wbr/>(<a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves all given PathElement's labels to the default positions (for example, the default position for name label is the middle of the path).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reshapeShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">reshapeShapeElement</a><wbr/>(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> newBounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reshapes given ShapeElement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConstraintForNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setConstraintForNote</a><wbr/>(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> note,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows given constraint in the given note.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPresentationElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.PropertyManager)">setPresentationElementProperties</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changes symbol properties of a given presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.lang.String)">setText</a><wbr/>(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets text for given symbol.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>PresentationElementsManager</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">PresentationElementsManager</span>()</div>
<div class="block">Private constructor. Do not allow creating instance outside this class.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="PresentationElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml">PresentationElementsManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns an instance of this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createShapeElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span>
                                throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a ShapeElement for given ModelElement in the given diagram.
 The created shape location is (0,0). The relationships to other symbols are not created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement to create ShapeElement for.</dd>
<dd><code>parent</code> - presentation element in which symbol should be created. Method can produce unpredictable results in case created symbol is illegal in such a parent. Valid combination is such as package in package, class in package, etc.</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.awt.Point)">
<h3>createShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createShapeElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 boolean createRelationships,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                                throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a ShapeElement for given ModelElement in the given diagram.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement to create ShapeElement for.</dd>
<dd><code>createRelationships</code> - create relationships to other symbols or not.</dd>
<dd><code>parent</code> - presentation element in which symbol should be created. Method can produce unpredictable results in case created symbol is illegal in such a parent. Valid combination is such as package in package, class in package, etc.</dd>
<dd><code>location</code> - the location where the new symbol is placed</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">
<h3>createShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createShapeElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 boolean createRelationships)</span>
                                throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a ShapeElement for given ModelElement in the given diagram.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement to create ShapeElement for.</dd>
<dd><code>createRelationships</code> - create relationships to other symbols or not.</dd>
<dd><code>parent</code> - presentation element in which symbol should be created. Method can produce unpredictable results in case created symbol is illegal in such a parent. Valid combination is such as package in package, class in package, etc.</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPathElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">createPathElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a PathElement for given relationship between given client and supplier PresentationElements.
 The PathElement will be created in the same diagram as client's and supplier's PresentationElements are.<br/>
 ModelElement of a client must be equal to relationship's client.<br/>
 ModelElement of supplier must be equal to relationship's supplier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the given relationship.</dd>
<dd><code>client</code> - a PresentationElement of relationship client.</dd>
<dd><code>supplier</code> - a PresentationElement of relationship supplier.</dd>
<dt>Returns:</dt>
<dd>created PathElement for given a relationship.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPathToSelfShapeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createPathToSelfShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createPathToSelfShapeElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</span>
                                          throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deletePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>deletePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deletePresentationElement</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span>
                               throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Removes given element from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to remove.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPresentationElementEditable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isPresentationElementEditable</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isPresentationElementEditable</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>movePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePresentationElement</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                             throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves a presentation element to the given parent and the specified location.
 During this operation parent of the symbol can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - presentation element to move.</dd>
<dd><code>parent</code> - parent to move into.</dd>
<dd><code>location</code> - location to move to.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,boolean)">
<h3>movePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePresentationElement</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 boolean canChangeElementOwner)</span>
                             throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves a presentation element to the given parent and the specified location.
 During this operation parent of the symbol can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - presentation element to move.</dd>
<dd><code>parent</code> - parent to move into.</dd>
<dd><code>location</code> - location to move to.</dd>
<dd><code>canChangeElementOwner</code> - allow changing an Element owner if needed by symbols structure</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>movePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePresentationElement</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                             throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves a presentation element to the specified location.
 During this operation, the parent of the symbol does not change, only geometrical position changes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol to move.</dd>
<dd><code>location</code> - location to move to.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePresentationElements(java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>movePresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; views,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves a list of presentation elements to the given parent and the specified location.
 During this operation parent of symbols can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>views</code> - presentation elements to move.</dd>
<dd><code>parent</code> - parent to move into.</dd>
<dd><code>location</code> - location to move to.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePresentationElements(java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,boolean)">
<h3>movePresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; views,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 boolean canChangeElementOwner)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves a list of presentation elements to the given parent and the specified location.
 During this operation parent of symbols can change both at the symbols and at the model level.
 If a model is read-only, model element parent does not change, only symbol coordinates change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>views</code> - presentation elements to move.</dd>
<dd><code>parent</code> - parent to move into.</dd>
<dd><code>location</code> - location to move to.</dd>
<dd><code>canChangeElementOwner</code> - allow changing an Element owner if needed by symbols structure</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePresentationElements(java.util.List,java.awt.Point)">
<h3>movePresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; views,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves a list of presentation elements to the specified location.
 During this operation parent of symbols does not change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>views</code> - presentation elements to move.</dd>
<dd><code>location</code> - location to move to.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reshapeShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">
<h3>reshapeShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reshapeShapeElement</span><wbr/><span class="parameters">(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> newBounds)</span>
                         throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Reshapes given ShapeElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the ShapeElement to reshape.</dd>
<dd><code>newBounds</code> - a new bounds of the element.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if an element is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List)">
<h3>changePathBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">changePathBreakPoints</span><wbr/><span class="parameters">(<a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> newBreakPoints)</span>
                           throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Changes the break points of the given PathElement.
 The order of break points is from supplier to client.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given PathElement.</dd>
<dd><code>newBreakPoints</code> - a list of new PathElement break points</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is read-only and can't edit.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if a given element is null or if given breakpoints are null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changePathPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.awt.Point,java.awt.Point,java.util.List)">
<h3>changePathPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">changePathPoints</span><wbr/><span class="parameters">(<a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newBreakPoints)</span>
                      throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Changes the points of the given PathElement.
 The order of break points is from supplier to client.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given PathElement.</dd>
<dd><code>supplierPoint</code> - new supplier</dd>
<dd><code>clientPoint</code> - new client point</dd>
<dd><code>newBreakPoints</code> - a list of new PathElement break points</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is read-only and can't edit</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if a given element is null or if given breakpoints are null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetLabelPositions(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>resetLabelPositions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetLabelPositions</span><wbr/><span class="parameters">(<a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</span>
                         throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves all given PathElement's labels to the default positions (for example, the default position for name label is the middle of the path).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given PathElement to reset labels for.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if a given element is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPresentationElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setPresentationElementProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPresentationElementProperties</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</span>
                                      throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Changes symbol properties of a given presentation element.
 Make sure to pass the newly created or cloned property manager, not the old one.
 <p>
<h4>Example:</h4>
<pre>
 PresentationElement view =  // some view
 ChoiceProperty property = (ChoiceProperty) view.getProperty(PropertyID.TAGGED_VALUES_DISPLAY_MODE);
 // important to create a new property or clone the old one!
 Property clonedProperty = property.clone();
 clonedProperty.setValue(ClassifierView.IN_COMPARTMENT);
 // important to create a new property manager or clone the old one!
 PropertyManager properties = new PropertyManager();
 properties.addProperty(clonedProperty);
 PresentationElementsManager.getInstance().setPresentationElementProperties(view, properties);
 </pre></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol for which to change the property manager.</dd>
<dd><code>propertyManager</code> - a newly created or cloned manager with new properties. Do not reuse the old property manager</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if a given element is null and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if a given element and properties is null and the element's type can't have properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNote(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createNote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createNote</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span>
                        throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a note in the given parent.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create ShapeElement in</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot edit</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNote(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>createNote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createNote</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                        throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a note in the given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create Note in</dd>
<dd><code>location</code> - location of created Note</dd>
<dt>Returns:</dt>
<dd>created Note</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTextBox(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createTextBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createTextBox</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span>
                           throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a text box in the given parent.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create ShapeElement in.</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot edit</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.io.File,java.awt.Point)">
<h3>createImageShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createImageShape</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates an image shape in the given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create Image Shape in</dd>
<dd><code>imageFile</code> - image file</dd>
<dd><code>location</code> - location of created Image Shape</dd>
<dt>Returns:</dt>
<dd>created Image Shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.io.File)">
<h3>createImageShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createImageShape</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates an image shape in the given parent.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create Image Shape in</dd>
<dd><code>imageFile</code> - image file</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if a parent is read-only and cannot edit</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTextBox(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>createTextBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createTextBox</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                           throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a text box in the given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create TextBox in</dd>
<dd><code>location</code> - location of TextBox</dd>
<dt>Returns:</dt>
<dd>created TextBox</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContentShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createContentShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ContentShape.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ContentShape</a></span> <span class="element-name">createContentShape</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> pack)</span>
                                throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a ContentShape in the given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create ContentShape in</dd>
<dd><code>location</code> - location of shape</dd>
<dd><code>pack</code> - content shape root content</dd>
<dt>Returns:</dt>
<dd>created TextBox</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSeparator(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createSeparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createSeparator</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span>
                             throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a separator shape in the given parent.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create ShapeElement in</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot edit</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSeparator(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>createSeparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createSeparator</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                             throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a separator shape in the parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create Separator in</dd>
<dd><code>location</code> - location of Separator</dd>
<dt>Returns:</dt>
<dd>created Separator</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRectangularShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createRectangularShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createRectangularShape</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span>
                                    throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a rectangular shape in the given parent.
 The created shape location is (0,0).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create ShapeElement in</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot edit</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRectangularShape(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Point)">
<h3>createRectangularShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createRectangularShape</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                                    throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a rectangular shape in the given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent to create Rectangular Shape in</dd>
<dd><code>location</code> - location of shape</dd>
<dt>Returns:</dt>
<dd>created shaped</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only and cannot be edited</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given parent is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="connectNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>connectNote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">connectNote</span><wbr/><span class="parameters">(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> noteOrComment,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</span>
                        throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Connects given note or comment shape with an anchor to the given presentation element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>noteOrComment</code> - the given note or comment shape.</dd>
<dd><code>target</code> - the presentation element to connect note (or comment) to.</dd>
<dt>Returns:</dt>
<dd>created anchor.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if note (or comment) is read-only and cannot edit.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given note is not instance of NoteView or comment is not instance of CommentView.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="connectComment(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>connectComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">connectComment</span><wbr/><span class="parameters">(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> comment,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</span>
                           throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Connects given comment with note anchor to the given presentation element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>comment</code> - comment to connect.</dd>
<dd><code>target</code> - the presentation element to connect comment to.</dd>
<dt>Returns:</dt>
<dd>created shape</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if comment is read-only and not editable.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given comment is not an instance of CommentView.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.lang.String)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span>
             throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Sets text for given symbol. Given symbol can be note, text box or separator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - the given symbol.</dd>
<dd><code>text</code> - a new text for a given symbol.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given node is not an instance of NoteView, TextBoxView, SeparatorView</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConstraintForNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setConstraintForNote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConstraintForNote</span><wbr/><span class="parameters">(<a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> note,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span>
                          throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Shows given constraint in the given note.
 Constraint must be added into a model already.
 Constraint must be assigned to ModelElement of symbol connected to the given note.
 If these conditions are not true, constraint may not be shown inside the note.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>note</code> - the given note.</dd>
<dd><code>constraint</code> - the given constraint.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if note is read-only and cannot edit.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given node is not an instance of NoteView.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSwimlane(java.util.List,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>createSwimlane</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/SwimlaneView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneView</a></span> <span class="element-name">createSwimlane</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt; horizontal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt; vertical,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span>
                            throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a swimlane in a given diagram.
 Adds horizontal and vertical partitions to the created swimlane.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>horizontal</code> - list of horizontal partitions</dd>
<dd><code>vertical</code> - list of vertical partitions</dd>
<dd><code>diagram</code> - parent for swimlane</dd>
<dt>Returns:</dt>
<dd>created swimlane</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given diagram is read-only and cannot edit.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given diagram is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContainmentLink(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createContainmentLink</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">createContainmentLink</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parentView,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> childView)</span>
                                  throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Connects given parent and child elements with a containment link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentView</code> - the presentation element of the parent element.</dd>
<dd><code>childView</code> - the presentation element of the child element.</dd>
<dt>Returns:</dt>
<dd>created link.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if parent element does not contain child element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLostMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int)">
<h3>createLostMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">createLostMessage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> from,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> insertAfter,
 int verticalGap)</span>
                              throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a lost message symbol for a given message from the given shape element.
 The given message is initialized (message ends are created and set, message sort is assigned) in this method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the given message</dd>
<dd><code>from</code> - a ShapeElement of message client lifeline</dd>
<dd><code>insertAfter</code> - the new message is inserted after this message, or null to insert before all messages</dd>
<dd><code>verticalGap</code> - vertical gap before the new message</dd>
<dt>Returns:</dt>
<dd>created symbol for a given message</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFoundMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int)">
<h3>createFoundMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">createFoundMessage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> from,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> insertAfter,
 int verticalGap)</span>
                               throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a found message symbol for a given message from the given shape element.
 The given message is initialized (message ends are created and set, message sort is assigned) in this method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the given message</dd>
<dd><code>from</code> - a ShapeElement of message client lifeline</dd>
<dd><code>insertAfter</code> - the new message is inserted after this message, or null to insert before all messages</dd>
<dd><code>verticalGap</code> - vertical gap before the new message</dd>
<dt>Returns:</dt>
<dd>created symbol for a given message</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSequenceMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean,int,com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,int)">
<h3>createSequenceMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">createSequenceMessage</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> sort,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> from,
 <a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> to,
 boolean recursive,
 int diagonal,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> insertAfter,
 int verticalGap)</span>
                                  throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates a PathElement for given message between given client (from) and supplier (to) PresentationElements.
 The given message is initialized (message ends are created and set, message sort is assigned) in this method.
 The diagram should be opened to make the messages' layout correctly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the given message.</dd>
<dd><code>sort</code> - message sort.</dd>
<dd><code>from</code> - a ShapeElement of message client lifeline.</dd>
<dd><code>to</code> - a ShapeElement of message supplier lifeline.</dd>
<dd><code>recursive</code> - true if a message is recursive (a recursive message can be only when from == to).</dd>
<dd><code>diagonal</code> - vertical size of a diagonal message, or 0 if the message is not diagonal.</dd>
<dd><code>insertAfter</code> - the new message is inserted after this message, or null to insert before all messages.</dd>
<dd><code>verticalGap</code> - vertical gap before the new message.</dd>
<dt>Returns:</dt>
<dd>created PathElement for a given message.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDurationConstraint(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.DurationConstraint,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>createDurationConstraint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/DurationConstraintView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">DurationConstraintView</a></span> <span class="element-name">createDurationConstraint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a> durationConstraint,
 <a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> firstConstrainedView,
 <a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> secondConstrainedView)</span>
                                                throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates DurationConstraint presentation element between the given two end views, that can be either
 SeqMessageView or ActivationView</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>durationConstraint</code> - model element for the DurationConstraintView</dd>
<dd><code>firstConstrainedView</code> - first end</dd>
<dd><code>secondConstrainedView</code> - second end</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is not editable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPartShape(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,boolean,java.awt.Point)">
<h3>createPartShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></span> <span class="element-name">createPartShape</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> part,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; nestedPath,
 boolean createRelationships,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span>
                         throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates part shape on the diagram at a given coordinate.
 Parent symbol can be specified.
 If a nested parts path is specified, nesting level is displayed in dot notation.
 It can be specified whether to create connected relationships.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>part</code> - part for which to create a shape.</dd>
<dd><code>parent</code> - parent symbol in which to add the part.</dd>
<dd><code>nestedPath</code> - a list of nested parts in which to nest the given part symbol.</dd>
<dd><code>createRelationships</code> - controls whether to display connected paths.</dd>
<dd><code>location</code> - location on the diagram where to move the part.</dd>
<dt>Returns:</dt>
<dd>created part symbol or null if it was not possible to create it.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVirtualRelation(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>createVirtualRelation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">createVirtualRelation</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> clientView,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplierView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> ruleKey)</span>
                                  throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates Virtual Relation view</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clientView</code> - relation client view</dd>
<dd><code>supplierView</code> - relation supplier view</dd>
<dd><code>ruleKey</code> - Virtual relation rule key</dd>
<dt>Returns:</dt>
<dd>created virtual relation symbol or null if it was not possible to create it.</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGenericView(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>createGenericView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">createGenericView</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> identifier)</span>
                               throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates Generic view</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which the generic view is created</dd>
<dd><code>parent</code> - container</dd>
<dd><code>identifier</code> - Generic view unique identifier, you can have different Generic views for the same element when the identifier is different</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if diagram is read-only.</dd>
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
