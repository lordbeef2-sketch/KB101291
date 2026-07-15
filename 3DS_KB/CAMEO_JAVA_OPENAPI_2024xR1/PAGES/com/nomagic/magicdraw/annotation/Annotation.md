# JAVA OPENAPI: Annotation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/annotation/Annotation.html
- source_path: `com/nomagic/magicdraw/annotation/Annotation.html`
- source_sha256: `32964dd96a904fa08b33ab3223741b02b8969285cb9a86dfb55c68847daf42a4`
- captured_utc: `2026-07-14T16:51:01.567940+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation](package-summary.html)

## Class Annotation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.annotation.Annotation

@OpenApiAllpublic classAnnotation
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Annotation is additional information about particular model element or symbol (target) or any other object.
 In contrast with annotation target, annotations are not stored in the project. They are
 rather computed in runtime.
 This additional information is paint text only: description (text) and short name (kind).
 Annotations can come from various sources, e.g. from OCL or some custom validation. Therefore,
 many annotations can be bound to the same target. Importance of each annotation
 is denoted by severity level. See `AnnotationPriorityComparator` for details.
 Annotations provide ready to use action which user can make e.g. in order to fix some
 problem in the model.
 Annotation are identified by kind, target, severity and actions - see equals() method for details.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEBUG](#DEBUG)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ERROR](#ERROR)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FATAL](#FATAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INFO](#INFO)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[WARNING](#WARNING)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Annotation](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String))([BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List))([BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List,java.lang.String))([BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List))([BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List))([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,com.nomagic.magicdraw.uml.BaseElement))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [BaseElement](../uml/BaseElement.html) target)`
Creates annotation object without actions.
`[Annotation](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,com.nomagic.magicdraw.uml.BaseElement,java.util.List))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [BaseElement](../uml/BaseElement.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates annotation object with actions.
`[Annotation](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,java.lang.Object))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`
Creates annotation object without actions.
`[Annotation](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,java.lang.Object,java.util.List))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates annotation object with actions.
`[Annotation](#%3Cinit%3E(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates and initializes a new `Annotation` object from specified parameters.
`[Annotation](#%3Cinit%3E(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Creates and initializes a new `Annotation` object from specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addPainter](#addPainter(com.nomagic.magicdraw.annotation.painters.AnnotationPainter))([AnnotationPainter](painters/AnnotationPainter.html) painter)`
Add painter
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructText](#constructText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`

`void`
`[dispose](#dispose())()`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)>`
`[getActions](#getActions())()`
Returns annotation actions.
`[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)`
`[getConstraint](#getConstraint())()`
Returns constraint that represents validation rule.
`static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon(com.nomagic.magicdraw.annotation.Annotation))([Annotation](Annotation.html) annotation)`
Returns icon of this annotation
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getKind](#getKind())()`
Returns annotation kind (short annotation name)
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AnnotationPainter](painters/AnnotationPainter.html)>`
`[getPainters](#getPainters())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getParentObject](#getParentObject())()`
Returns parent object.
`int`
`[getPriority](#getPriority())()`

`[Project](../core/Project.html)`
`[getProject](#getProject())()`
Gets project that annotation belongs to.
`[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getSeverity](#getSeverity())()`
Returns annotation severity level - one of the SeverityKind enumeration.
`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getSeverityColor](#getSeverityColor())()`
Calculates severity level color.
`[Image](../../uml2/ext/magicdraw/mdprofiles/Image.html)`
`[getSeverityImageIcon](#getSeverityImageIcon())()`
Annotation icon by severity.
`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getSeverityLevel](#getSeverityLevel(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Searches for a severity level with a given name in a project.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)>`
`[getSeverityLevels](#getSeverityLevels(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
A utility method for accessing available in the project severity levels (they are mapped to Enumeration Literals).
`[BaseElement](../uml/BaseElement.html)`
`[getTarget](#getTarget())()`
Returns annotation target - the project entity to which the annotation is bound to.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getTargetObject](#getTargetObject())()`
Returns an object to which the annotation is bound.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`
Returns annotation message.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getToolTipText](#getToolTipText())()`
Returns annotation tool tip text.
`int`
`[hashCode](#hashCode())()`

`protected void`
`[initInternal](#initInternal(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
initializes actions, severity color/icon and scopes
`void`
`[removePainter](#removePainter(com.nomagic.magicdraw.annotation.painters.AnnotationPainter))([AnnotationPainter](painters/AnnotationPainter.html) painter)`
Remove painter
`protected [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[resolveSeverity](#resolveSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`

`protected void`
`[setActions](#setActions(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`

`void`
`[setParentObject](#setParentObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentObject)`
Sets parent object.
`protected final void`
`[setPriority](#setPriority(int))(int priority)`

`void`
`[setSeverityColor](#setSeverityColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) severityColor)`
Set severity color, The color may be used to draw decorations around the shape.
`void`
`[setSeverityIcon](#setSeverityIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image))([Image](../../uml2/ext/magicdraw/mdprofiles/Image.html) severityIcon)`
Set annotation icon by severity
`void`
`[setText](#setText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Sets annotation text.
`void`
`[setToolTipText](#setToolTipText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toolTipText)`
Sets annotation tool tip text.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ERROR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ERROR
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.ERROR)
INFO
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INFO
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.INFO)
WARNING
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) WARNING
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.WARNING)
FATAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FATAL
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.FATAL)
DEBUG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEBUG
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.DEBUG)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Annotation
public Annotation(@CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Creates and initializes a new `Annotation` object from specified parameters.
 Actions list will be empty.
Parameters:
`target` - model element or presentation element that annotation is assigned to.
`constraint` - constraint that is violated.
Annotation
public Annotation(@CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates and initializes a new `Annotation` object from specified parameters.
Parameters:
`target` - model element or presentation element that annotation is assigned to.
`constraint` - constraint that is violated.
`actions` - annotation actions, can be an empty list.
Annotation
public Annotation(@CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Creates and initializes a new `Annotation` object from specified parameters.
Parameters:
`target` - model element or presentation element that annotation is assigned to.
`constraint` - constraint that is violated.
`text` - annotation text
Annotation
public Annotation(@CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates and initializes a new `Annotation` object from specified parameters.
Parameters:
`target` - model element or presentation element that annotation is assigned to.
`constraint` - constraint that is violated.
`text` - annotation text
`actions` - annotation actions, can be an empty list.
Annotation
public Annotation(@CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind)
Creates and initializes a new `Annotation` object from specified parameters.
Parameters:
`target` - model element or presentation element that annotation is assigned to.
`constraint` - constraint that is violated.
`text` - annotation text
`actions` - annotation actions, can be an empty list.
`kind` - annotation kind (short annotation name)
Annotation
public Annotation([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [BaseElement](../uml/BaseElement.html) target)
Creates annotation object without actions. None of the can be null.
Parameters:
`severity` - - defines how important the annotation is, e.g. it may influence the
 display order of annotation if there are many for the same element
`kind` - short unique name
`text` - message, detailed description of the problem. It may be displayed in
 tooltips, tables etc..
`target` - model element or presentation element that annotation is assigned to.
See Also:
[`getSeverityLevels(com.nomagic.magicdraw.core.Project)`](#getSeverityLevels(com.nomagic.magicdraw.core.Project))
Annotation
public Annotation([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates annotation object with actions. None of them can be null.
Parameters:
`severity` - - defines how important the annotation is, e.g. it may influence the
 display order of annotation if there are many for the same element
`kind` - short unique name
`text` - message, detailed description of the problem. It may be displayed in
 tooltips, tables etc..
`target` - model element or presentation element that annotation is assigned to.
`actions` - annotation actions, can be an empty list.
See Also:
[`getSeverityLevels(com.nomagic.magicdraw.core.Project)`](#getSeverityLevels(com.nomagic.magicdraw.core.Project))
Annotation
public Annotation(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Creates and initializes a new `Annotation` object from specified parameters.
 Actions list will be empty.
Parameters:
`target` - model element or presentation element that annotation is assigned to.
`constraint` - constraint that is violated.
Annotation
public Annotation([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Creates and initializes a new `Annotation` object from specified parameters.
 Target is unspecified (null).
Parameters:
`constraint` - constraint that is violated.
Annotation
public Annotation([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates and initializes a new `Annotation` object from specified parameters.
 Target is unspecified (null).
Parameters:
`constraint` - constraint that is violated.
`actions` - annotation actions, can be an empty list.
Annotation
public Annotation(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates and initializes a new `Annotation` object from specified parameters.
Parameters:
`target` - model object that annotation is assigned to.
`constraint` - constraint that is violated.
`actions` - annotation actions, can be an empty list.
Annotation
public Annotation(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates and initializes a new `Annotation` object from specified parameters.
Parameters:
`target` - object that annotation is assigned to.
`constraint` - constraint that is violated.
`text` - annotation text
`actions` - annotation actions, can be an empty list.
Annotation
public Annotation([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
Creates annotation object without actions. None of the can be null.
Parameters:
`severity` - - defines how important the annotation is, e.g. it may influence the
 display order of annotation if there are many for the same element
`kind` - short unique name
`text` - message, detailed description of the problem. It may be displayed in
 tooltips, tables etc..
`target` - object that annotation is assigned to.
See Also:
[`getSeverityLevels(com.nomagic.magicdraw.core.Project)`](#getSeverityLevels(com.nomagic.magicdraw.core.Project))
Annotation
public Annotation([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) kind,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Creates annotation object with actions. None of them can be null.
Parameters:
`severity` - - defines how important the annotation is, e.g. it may influence the
 display order of annotation if there are many for the same element
`kind` - short unique name
`text` - message, detailed description of the problem. It may be displayed in
 tooltips, tables etc..
`target` - object that annotation is assigned to.
`actions` - annotation actions, can be an empty list.
See Also:
[`getSeverityLevels(com.nomagic.magicdraw.core.Project)`](#getSeverityLevels(com.nomagic.magicdraw.core.Project))
 ============ METHOD DETAIL ========== 
Method Details
dispose
public void dispose()
resolveSeverity
@CheckForNullprotected [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) resolveSeverity([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
constructText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructText(@CheckForNull
 [BaseElement](../uml/BaseElement.html) target,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
setText
public void setText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Sets annotation text.
Parameters:
`text` - text to set.
initInternal
protected void initInternal([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
initializes actions, severity color/icon and scopes
getKind
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getKind()
Returns annotation kind (short annotation name)
Returns:
annotation kind
getTarget
@CheckForNullpublic [BaseElement](../uml/BaseElement.html) getTarget()
Returns annotation target - the project entity to which the annotation is bound to. The method
 can return null if the annotation is bound to any other project but to a project entity.
Returns:
annotation target
getTargetObject
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getTargetObject()
Returns an object to which the annotation is bound.
Returns:
target object.
getProject
@CheckForNullpublic [Project](../core/Project.html) getProject()
Gets project that annotation belongs to.
Returns:
Project or null if the project was already disposed.
getText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText()
Returns annotation message.
Returns:
annotation message
getToolTipText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getToolTipText()
Returns annotation tool tip text.
Returns:
annotation tool tip text.
setToolTipText
public void setToolTipText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toolTipText)
Sets annotation tool tip text.
Parameters:
`toolTipText` - text to set.
getActions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> getActions()
Returns annotation actions.
Returns:
annotation actions
setActions
protected void setActions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
getSeverity
public [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getSeverity()
Returns annotation severity level - one of the SeverityKind enumeration.
 Usually it's either an error, warning, info or debug level.
Returns:
annotation severity
See Also:
[`getSeverityLevels(com.nomagic.magicdraw.core.Project)`](#getSeverityLevels(com.nomagic.magicdraw.core.Project))
getPriority
public int getPriority()
Returns:
Priority of this annotation. Higher severity annotations have higher priority
setPriority
protected final void setPriority(int priority)
getSeverityColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getSeverityColor()
Calculates severity level color. The color may be used
 to draw decorations around the shape.
Returns:
calculated severity level color
setSeverityColor
public void setSeverityColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) severityColor)
Set severity color, The color may be used to draw decorations around the shape.
Parameters:
`severityColor` - color
getSeverityImageIcon
@CheckForNullpublic [Image](../../uml2/ext/magicdraw/mdprofiles/Image.html) getSeverityImageIcon()
Annotation icon by severity.
Returns:
Image element of stereotype applied to the severity level.
getConstraint
@CheckForNullpublic [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) getConstraint()
Returns constraint that represents validation rule.
Returns:
constraint.
setSeverityIcon
public void setSeverityIcon([Image](../../uml2/ext/magicdraw/mdprofiles/Image.html) severityIcon)
Set annotation icon by severity
Parameters:
`severityIcon` - icon
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
getParentObject
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getParentObject()
Returns parent object.
Returns:
parent object.
setParentObject
public void setParentObject(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentObject)
Sets parent object.
Parameters:
`parentObject` - new parent object.
getIcon
@CheckForNullpublic static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon([Annotation](Annotation.html) annotation)
Returns icon of this annotation
Parameters:
`annotation` - annotation
Returns:
icon
getSeverityLevels
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)> getSeverityLevels([Project](../core/Project.html) project)
A utility method for accessing available in the project severity levels (they are mapped to Enumeration Literals).
Parameters:
`project` - an owner of Enumeration
Returns:
a list of EnumerationLiterals corresponding to severity levels. Literals are sorted by priority
 (first is highest)
getSeverityLevel
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getSeverityLevel([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Searches for a severity level with a given name in a project.
Parameters:
`project` - project
`name` - severity name
Returns:
return severity level with a given name or null
See Also:
[`getSeverityLevels(com.nomagic.magicdraw.core.Project)`](#getSeverityLevels(com.nomagic.magicdraw.core.Project))
[`ERROR`](#ERROR)
[`WARNING`](#WARNING)
[`INFO`](#INFO)
[`DEBUG`](#DEBUG)
[`FATAL`](#FATAL)
getPainters
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AnnotationPainter](painters/AnnotationPainter.html)> getPainters()
Returns:
painters
addPainter
public void addPainter([AnnotationPainter](painters/AnnotationPainter.html) painter)
Add painter
Parameters:
`painter` - painter
removePainter
public void removePainter([AnnotationPainter](painters/AnnotationPainter.html) painter)
Remove painter
Parameters:
`painter` - painter

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation</a></div>
<h1 class="title" title="Class Annotation">Class Annotation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.annotation.Annotation</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Annotation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Annotation is additional information about particular model element or symbol (target) or any other object.
 In contrast with annotation target, annotations are not stored in the project. They are
 rather computed in runtime.
 This additional information is paint text only: description (text) and short name (kind).
 Annotations can come from various sources, e.g. from OCL or some custom validation. Therefore,
 many annotations can be bound to the same target. Importance of each annotation
 is denoted by severity level. See <code>AnnotationPriorityComparator</code> for details.
 Annotations provide ready to use action which user can make e.g. in order to fix some
 problem in the model.
 Annotation are identified by kind, target, severity and actions - see equals() method for details.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEBUG">DEBUG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ERROR">ERROR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FATAL">FATAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INFO">INFO</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WARNING">WARNING</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">Annotation</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String)">Annotation</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List)">Annotation</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List,java.lang.String)">Annotation</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List)">Annotation</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">Annotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List)">Annotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,com.nomagic.magicdraw.uml.BaseElement)">Annotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates annotation object without actions.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,com.nomagic.magicdraw.uml.BaseElement,java.util.List)">Annotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates annotation object with actions.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,java.lang.Object)">Annotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates annotation object without actions.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,java.lang.Object,java.util.List)">Annotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates annotation object with actions.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">Annotation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List)">Annotation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List)">Annotation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPainter(com.nomagic.magicdraw.annotation.painters.AnnotationPainter)">addPainter</a><wbr/>(<a href="painters/AnnotationPainter.html" title="interface in com.nomagic.magicdraw.annotation.painters">AnnotationPainter</a> painter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add painter</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constructText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">constructText</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActions()">getActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns annotation actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstraint()">getConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns constraint that represents validation rule.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(com.nomagic.magicdraw.annotation.Annotation)">getIcon</a><wbr/>(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon of this annotation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns annotation kind (short annotation name)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="painters/AnnotationPainter.html" title="interface in com.nomagic.magicdraw.annotation.painters">AnnotationPainter</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPainters()">getPainters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentObject()">getParentObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets project that annotation belongs to.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverity()">getSeverity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns annotation severity level - one of the SeverityKind enumeration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverityColor()">getSeverityColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates severity level color.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverityImageIcon()">getSeverityImageIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Annotation icon by severity.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverityLevel(com.nomagic.magicdraw.core.Project,java.lang.String)">getSeverityLevel</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a severity level with a given name in a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)">getSeverityLevels</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A utility method for accessing available in the project severity levels (they are mapped to Enumeration Literals).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns annotation target - the project entity to which the annotation is bound to.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetObject()">getTargetObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an object to which the annotation is bound.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns annotation message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getToolTipText()">getToolTipText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns annotation tool tip text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initInternal(java.util.List)">initInternal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">initializes actions, severity color/icon and scopes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePainter(com.nomagic.magicdraw.annotation.painters.AnnotationPainter)">removePainter</a><wbr/>(<a href="painters/AnnotationPainter.html" title="interface in com.nomagic.magicdraw.annotation.painters">AnnotationPainter</a> painter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove painter</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resolveSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">resolveSeverity</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActions(java.util.List)">setActions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentObject(java.lang.Object)">setParentObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets parent object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPriority(int)">setPriority</a><wbr/>(int priority)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeverityColor(java.awt.Color)">setSeverityColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> severityColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set severity color, The color may be used to draw decorations around the shape.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeverityIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image)">setSeverityIcon</a><wbr/>(<a href="../../uml2/ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> severityIcon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set annotation icon by severity</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.String)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets annotation text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setToolTipText(java.lang.String)">setToolTipText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> toolTipText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets annotation tool tip text.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="ERROR">
<h3>ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ERROR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.ERROR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INFO">
<h3>INFO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INFO</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.INFO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WARNING">
<h3>WARNING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">WARNING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.WARNING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FATAL">
<h3>FATAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FATAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.FATAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEBUG">
<h3>DEBUG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEBUG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.annotation.Annotation.DEBUG">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.
 Actions list will be empty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>text</code> - annotation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>text</code> - annotation text</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List,java.lang.String)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>text</code> - annotation text</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
<dd><code>kind</code> - annotation kind (short annotation name)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,com.nomagic.magicdraw.uml.BaseElement)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target)</span></div>
<div class="block">Creates annotation object without actions. None of the can be null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severity</code> - - defines how important the annotation is, e.g. it may influence the
                 display order of annotation if there are many for the same element</dd>
<dd><code>kind</code> - short unique name</dd>
<dd><code>text</code> - message, detailed description of the problem. It may be displayed in
                 tooltips, tables etc..</dd>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)"><code>getSeverityLevels(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,com.nomagic.magicdraw.uml.BaseElement,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates annotation object with actions. None of them can be null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severity</code> - - defines how important the annotation is, e.g. it may influence the
                 display order of annotation if there are many for the same element</dd>
<dd><code>kind</code> - short unique name</dd>
<dd><code>text</code> - message, detailed description of the problem. It may be displayed in
                 tooltips, tables etc..</dd>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)"><code>getSeverityLevels(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.
 Actions list will be empty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model element or presentation element that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.
 Target is unspecified (null).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint that is violated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.
 Target is unspecified (null).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - model object that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates and initializes a new <code>Annotation</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - object that annotation is assigned to.</dd>
<dd><code>constraint</code> - constraint that is violated.</dd>
<dd><code>text</code> - annotation text</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,java.lang.Object)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
<div class="block">Creates annotation object without actions. None of the can be null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severity</code> - - defines how important the annotation is, e.g. it may influence the
                 display order of annotation if there are many for the same element</dd>
<dd><code>kind</code> - short unique name</dd>
<dd><code>text</code> - message, detailed description of the problem. It may be displayed in
                 tooltips, tables etc..</dd>
<dd><code>target</code> - object that annotation is assigned to.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)"><code>getSeverityLevels(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,java.lang.String,java.lang.String,java.lang.Object,java.util.List)">
<h3>Annotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> kind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Creates annotation object with actions. None of them can be null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severity</code> - - defines how important the annotation is, e.g. it may influence the
                 display order of annotation if there are many for the same element</dd>
<dd><code>kind</code> - short unique name</dd>
<dd><code>text</code> - message, detailed description of the problem. It may be displayed in
                 tooltips, tables etc..</dd>
<dd><code>target</code> - object that annotation is assigned to.</dd>
<dd><code>actions</code> - annotation actions, can be an empty list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)"><code>getSeverityLevels(com.nomagic.magicdraw.core.Project)</code></a></li>
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
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
</section>
</li>
<li>
<section class="detail" id="resolveSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>resolveSeverity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">resolveSeverity</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
</section>
</li>
<li>
<section class="detail" id="constructText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>constructText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.String)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Sets annotation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initInternal(java.util.List)">
<h3>initInternal</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initInternal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">initializes actions, severity color/icon and scopes</div>
</section>
</li>
<li>
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getKind</span>()</div>
<div class="block">Returns annotation kind (short annotation name)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTarget()">
<h3>getTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getTarget</span>()</div>
<div class="block">Returns annotation target - the project entity to which the annotation is bound to. The method
 can return null if the annotation is bound to any other project but to a project entity.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetObject()">
<h3>getTargetObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTargetObject</span>()</div>
<div class="block">Returns an object to which the annotation is bound.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Gets project that annotation belongs to.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Project or null if the project was already disposed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block">Returns annotation message.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getToolTipText()">
<h3>getToolTipText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getToolTipText</span>()</div>
<div class="block">Returns annotation tool tip text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation tool tip text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setToolTipText(java.lang.String)">
<h3>setToolTipText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setToolTipText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> toolTipText)</span></div>
<div class="block">Sets annotation tool tip text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>toolTipText</code> - text to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActions()">
<h3>getActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getActions</span>()</div>
<div class="block">Returns annotation actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActions(java.util.List)">
<h3>setActions</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setActions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSeverity()">
<h3>getSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getSeverity</span>()</div>
<div class="block">Returns annotation severity level - one of the SeverityKind enumeration.
 Usually it's either an error, warning, info or debug level.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>annotation severity</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)"><code>getSeverityLevels(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Priority of this annotation. Higher severity annotations have higher priority</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPriority(int)">
<h3>setPriority</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">setPriority</span><wbr/><span class="parameters">(int priority)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSeverityColor()">
<h3>getSeverityColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getSeverityColor</span>()</div>
<div class="block">Calculates severity level color. The color may be used
 to draw decorations around the shape.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>calculated severity level color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSeverityColor(java.awt.Color)">
<h3>setSeverityColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeverityColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> severityColor)</span></div>
<div class="block">Set severity color, The color may be used to draw decorations around the shape.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severityColor</code> - color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeverityImageIcon()">
<h3>getSeverityImageIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></span> <span class="element-name">getSeverityImageIcon</span>()</div>
<div class="block">Annotation icon by severity.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Image element of stereotype applied to the severity level.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConstraint()">
<h3>getConstraint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getConstraint</span>()</div>
<div class="block">Returns constraint that represents validation rule.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>constraint.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSeverityIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Image)">
<h3>setSeverityIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeverityIcon</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> severityIcon)</span></div>
<div class="block">Set annotation icon by severity</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severityIcon</code> - icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentObject()">
<h3>getParentObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getParentObject</span>()</div>
<div class="block">Returns parent object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentObject(java.lang.Object)">
<h3>setParentObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentObject</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentObject)</span></div>
<div class="block">Sets parent object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentObject</code> - new parent object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(com.nomagic.magicdraw.annotation.Annotation)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</span></div>
<div class="block">Returns icon of this annotation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - annotation</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeverityLevels(com.nomagic.magicdraw.core.Project)">
<h3>getSeverityLevels</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt;</span> <span class="element-name">getSeverityLevels</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">A utility method for accessing available in the project severity levels (they are mapped to Enumeration Literals).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - an owner of Enumeration</dd>
<dt>Returns:</dt>
<dd>a list of EnumerationLiterals corresponding to severity levels. Literals are sorted by priority
 (first is highest)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeverityLevel(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getSeverityLevel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getSeverityLevel</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Searches for a severity level with a given name in a project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - severity name</dd>
<dt>Returns:</dt>
<dd>return severity level with a given name or null</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSeverityLevels(com.nomagic.magicdraw.core.Project)"><code>getSeverityLevels(com.nomagic.magicdraw.core.Project)</code></a></li>
<li><a href="#ERROR"><code>ERROR</code></a></li>
<li><a href="#WARNING"><code>WARNING</code></a></li>
<li><a href="#INFO"><code>INFO</code></a></li>
<li><a href="#DEBUG"><code>DEBUG</code></a></li>
<li><a href="#FATAL"><code>FATAL</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPainters()">
<h3>getPainters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="painters/AnnotationPainter.html" title="interface in com.nomagic.magicdraw.annotation.painters">AnnotationPainter</a>&gt;</span> <span class="element-name">getPainters</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>painters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPainter(com.nomagic.magicdraw.annotation.painters.AnnotationPainter)">
<h3>addPainter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPainter</span><wbr/><span class="parameters">(<a href="painters/AnnotationPainter.html" title="interface in com.nomagic.magicdraw.annotation.painters">AnnotationPainter</a> painter)</span></div>
<div class="block">Add painter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>painter</code> - painter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePainter(com.nomagic.magicdraw.annotation.painters.AnnotationPainter)">
<h3>removePainter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePainter</span><wbr/><span class="parameters">(<a href="painters/AnnotationPainter.html" title="interface in com.nomagic.magicdraw.annotation.painters">AnnotationPainter</a> painter)</span></div>
<div class="block">Remove painter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>painter</code> - painter</dd>
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
