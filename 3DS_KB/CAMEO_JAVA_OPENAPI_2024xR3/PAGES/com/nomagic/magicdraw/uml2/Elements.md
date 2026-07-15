# JAVA OPENAPI: Elements (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/Elements.html
- source_path: `com/nomagic/magicdraw/uml2/Elements.html`
- source_sha256: `91caabda66ad38100c7445aa0deef47e3e6dfb19337a8df872296165898bf9d3`
- captured_utc: `2026-07-14T16:56:07.526593+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Elements

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Elements

public classElements
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenient static methods to work with Elements.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>>`
`[RELATIONSHIP_TYPES](#RELATIONSHIP_TYPES)`
Relationship like classes
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Elements](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[dispose](#dispose(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Dispose all elements in the given collection.
`static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfStrictType](#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> ownerType)`
Finds an owner of an element of a specific class type.
`static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfStrictTypeIncludingItself](#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> ownerType)`
Finds an owner of an element of a specific class type.
`static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfType](#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)`
Searches for the first direct or indirect owner of the given type among owners of the given element.
`static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfTypeIncludingItself](#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)`
Searches for the first direct or indirect owner of the given type among owners of the given element.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getClientElement](#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship)`
Get a client of the relationship.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getComment](#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation of given element.
`static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)`
`[getCommentElement](#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation Comment for this Element.
`static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)`
`[getCommentElement](#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)> commentOfAnnotatedElement)`

`static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)`
`[getCommentElementOrCreate](#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation Comment for this element.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)>`
`[getDependentClients](#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class))([NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)`
Collects elements those are connected with Dependencies as clients with a given element
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)>`
`[getDependentSuppliers](#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class))([NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)`
Collects elements those are connected with Dependencies as suppliers with a given element
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMultiplicity](#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element)`
Returns multiplicity string for a specified multiplicity element.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Return a name of given element
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getOppositeEnd](#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) end)`
Return the opposite relationship end
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSupplierElement](#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship)`
Get supplier of the relationship.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSupplierElement](#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 boolean takeUserFriendly)`
Get supplier of the relationship.
`static boolean`
`[hasParentIn](#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> possibleParents,
 [BaseElement](../uml/BaseElement.html) possibleChild)`
Checks if given object is child of any of the given parent objects.
`static boolean`
`[isChildOf](#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> owners,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) child)`
Is given element is child of one of the given owners.
`static boolean`
`[isDocumentationComment](#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment))([Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) comment)`
Checks if given comment used for storing element documentation.
`static boolean`
`[isMultiplicityMany](#isMultiplicityMany(int))(int value)`
Check if given value is 'many' - it is more than 1 or is unlimited (-1).
`static boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) possibleParent,
 [BaseElement](../uml/BaseElement.html) possibleChild)`
Checks if the given element is child of a given parent.
`static boolean`
`[isParentOf](#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) possibleParent,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) possibleChild)`
Checks if the given element is child of a given parent.
`static boolean`
`[isRelationship](#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if a given element is a relationship.
`static boolean`
`[isRelationship](#isRelationship(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)`
Check if given class is relationship
`static boolean`
`[isRelationshipAlwaysInClient](#isRelationshipAlwaysInClient(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) relationshipClass)`
Check if the Relationship of the given class type is always owned by a client element
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[parseMultiplicityString](#parseMultiplicityString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) expression)`
Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds
`static void`
`[setClientElement](#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) client)`
Set client of the relationship.
`static void`
`[setComment](#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) documentation)`
Set comment (documentation) for an element.
`static void`
`[setCommentElement](#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) comment)`
Set given Comment as documentation of given Element.
`static void`
`[setMultiplicity](#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))(int lower,
 int upper,
 [MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element)`
Set multiplicity to an element.
`static void`
`[setMultiplicity](#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) expression,
 [MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element)`
Sets multiplicity for a specified multiplicity element.
`static void`
`[setSupplierElement](#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplier)`
Set supplier of the relationship.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
RELATIONSHIP_TYPES
public static final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>> RELATIONSHIP_TYPES
Relationship like classes
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Elements
public Elements()
 ============ METHOD DETAIL ========== 
Method Details
hasParentIn
public static boolean hasParentIn([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> possibleParents,
 [BaseElement](../uml/BaseElement.html) possibleChild)
Checks if given object is child of any of the given parent objects.
Parameters:
`possibleChild` - possible child
`possibleParents` - possible parents
Returns:
true if the given possibleChild is a child of any of given possibleParents
isParentOf
public static boolean isParentOf([BaseElement](../uml/BaseElement.html) possibleParent,
 [BaseElement](../uml/BaseElement.html) possibleChild)
Checks if the given element is child of a given parent.
Parameters:
`possibleChild` - possible child
`possibleParent` - possible parent
Returns:
true if possibleChild is a child of possibleParent
isParentOf
public static boolean isParentOf([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) possibleParent,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) possibleChild)
Checks if the given element is child of a given parent.
Parameters:
`possibleChild` - possible child
`possibleParent` - possible parent
Returns:
true if possibleChild is a child of possibleParent
isChildOf
public static boolean isChildOf([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> owners,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) child)
Is given element is child of one of the given owners.
Parameters:
`owners` - the owners to check.
`child` - the child element to check owners for
Returns:
true, if given child is child of some given owner
setComment
public static void setComment([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) documentation)
Set comment (documentation) for an element. Comment is set on the first element in an owned comments collection.
 If documentation is null or empty string, remove the comment.
Parameters:
`element` - element to set documentation
`documentation` - documentation text
getComment
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getComment([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns documentation of given element.
Parameters:
`element` - element to get documentation.
Returns:
element documentation.
getCommentElementOrCreate
public static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) getCommentElementOrCreate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns documentation Comment for this element. If Comment is not set yet, new Comment is created.
Parameters:
`element` - element
Returns:
comment
getCommentElement
@CheckForNullpublic static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) getCommentElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns documentation Comment for this Element. If Comment is not set, returns null.
Parameters:
`element` - element
Returns:
comment
getCommentElement
@CheckForNullpublic static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) getCommentElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)> commentOfAnnotatedElement)
isDocumentationComment
public static boolean isDocumentationComment([Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) comment)
Checks if given comment used for storing element documentation.
Parameters:
`comment` - comment
Returns:
true if comment is used as documentation
setCommentElement
public static void setCommentElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) comment)
Set given Comment as documentation of given Element.
Parameters:
`element` - element
`comment` - comment
findOwnerOfTypeIncludingItself
@CheckForNullpublic static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> T findOwnerOfTypeIncludingItself(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)
Searches for the first direct or indirect owner of the given type among owners of the given element.
 Checks if the element itself is an instance of given ownerType. If yes, returns it, if no, looks
 for an owner of given instance in all element's ownership hierarchy. If such an owner does not exist, returns null.
Parameters:
`element` - element
`ownerType` - the metaclass of owner to find. Found owner must be an instance of this class
Returns:
found owner or null
findOwnerOfType
@CheckForNullpublic static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> T findOwnerOfType(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)
Searches for the first direct or indirect owner of the given type among owners of the given element.
 Look for owner of given instance in all element's ownership hierarchy. If such an owner does not exist, returns null.
Parameters:
`element` - element.
`ownerType` - the metaclass of owner to find. Found owner must be an instance of this class.
Returns:
found owner or null.
findOwnerOfStrictTypeIncludingItself
@CheckForNullpublic static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> T findOwnerOfStrictTypeIncludingItself(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> ownerType)
Finds an owner of an element of a specific class type.
Parameters:
`element` - element for which owner of a specific type should be found
`ownerType` - class type of the owner
Returns:
found owner or null if the owner of a specific type was not found
findOwnerOfStrictType
@CheckForNullpublic static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> T findOwnerOfStrictType([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> ownerType)
Finds an owner of an element of a specific class type.
Parameters:
`element` - element for which parent of a specific type should be found
`ownerType` - class type of the owner
Returns:
found owner or null if an owner of a specific type was not found
setMultiplicity
public static void setMultiplicity(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) expression,
 [MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element)
Sets multiplicity for a specified multiplicity element.
Parameters:
`expression` - values that make sense: "0", "1", "*", "0..*", "1..*", "0..1". If null, multiplicity will become unspecified
`element` - multiplicity element.
parseMultiplicityString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] parseMultiplicityString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) expression)
Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds
Parameters:
`expression` - expression
isMultiplicityMany
public static boolean isMultiplicityMany(int value)
Check if given value is 'many' - it is more than 1 or is unlimited (-1).
Parameters:
`value` - value
Returns:
true if value is many
setMultiplicity
public static void setMultiplicity(int lower,
 int upper,
 [MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element)
Set multiplicity to an element.
Parameters:
`lower` - lover
`upper` - upper
`element` - element
dispose
public static void dispose([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Dispose all elements in the given collection.
Parameters:
`elements` - elements to dispose
isRelationship
public static boolean isRelationship(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if a given element is a relationship. MD treats Transition, ActivityEdge and InstanceSpecifications used as Links as relationships.
Parameters:
`element` - element
Returns:
true if an element is relationship
isRelationship
public static boolean isRelationship([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)
Check if given class is relationship
Parameters:
`type` - given class
Returns:
true if relationship
isRelationshipAlwaysInClient
public static boolean isRelationshipAlwaysInClient([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) relationshipClass)
Check if the Relationship of the given class type is always owned by a client element
Parameters:
`relationshipClass` - relationship class type
Returns:
return true if given relationship is always owned by client element
getClientElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getClientElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship)
Get a client of the relationship.
Parameters:
`relationship` - relationship model element.
Returns:
client of given relationship
getSupplierElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSupplierElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship)
Get supplier of the relationship.
Parameters:
`relationship` - relationship model element.
getSupplierElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSupplierElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 boolean takeUserFriendly)
Get supplier of the relationship.
Parameters:
`relationship` - relationship model element.
`takeUserFriendly` - take a user-friendly element in some cases (for example, owning classifier instead of template signature)
setClientElement
public static void setClientElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) client)
Set client of the relationship.
Parameters:
`relationship` - relationship model element
`client` - client element that will be set to a specified relationship model element
setSupplierElement
public static void setSupplierElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) supplier)
Set supplier of the relationship.
Parameters:
`relationship` - relationship model element.
`supplier` - supplier element that will be set to a specified relationship model element.
getDependentClients
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> getDependentClients([NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)
Collects elements those are connected with Dependencies as clients with a given element
Parameters:
`element` - the given element
`dependencyClass` - dependency class to filter
Returns:
list of dependent client elements
getDependentSuppliers
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> getDependentSuppliers([NamedElement](../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)
Collects elements those are connected with Dependencies as suppliers with a given element
Parameters:
`element` - the given element
`dependencyClass` - dependency class to filter
Returns:
list of dependent supplier elements
getMultiplicity
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMultiplicity([MultiplicityElement](../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element)
Returns multiplicity string for a specified multiplicity element.
Parameters:
`element` - multiplicity element.
Returns:
multiplicity expression: "0", "1", "*", "0..*", "1..*", "0..1". "" is returned if no multiplicity is set.
getName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName([BaseElement](../uml/BaseElement.html) element)
Return a name of given element
Parameters:
`element` - name
Returns:
name of give an element
getOppositeEnd
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getOppositeEnd([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) end)
Return the opposite relationship end
Parameters:
`relationship` - relationship
`end` - end
Returns:
opposite end

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Elements">Class Elements</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Elements</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Elements</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenient static methods to work with Elements.</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATIONSHIP_TYPES">RELATIONSHIP_TYPES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Relationship like classes</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Elements</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose(java.util.Collection)">dispose</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dispose all elements in the given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds an owner of an element of a specific class type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictTypeIncludingItself</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds an owner of an element of a specific class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for the first direct or indirect owner of the given type among owners of the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfTypeIncludingItself</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for the first direct or indirect owner of the given type among owners of the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClientElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get a client of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComment</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns documentation of given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns documentation Comment for this Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">getCommentElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt; commentOfAnnotatedElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElementOrCreate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns documentation Comment for this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentClients</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects elements those are connected with Dependencies as clients with a given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentSuppliers</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects elements those are connected with Dependencies as suppliers with a given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">getMultiplicity</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns multiplicity string for a specified multiplicity element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getName(com.nomagic.magicdraw.uml.BaseElement)">getName</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a name of given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOppositeEnd</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the opposite relationship end</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSupplierElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get supplier of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getSupplierElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 boolean takeUserFriendly)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get supplier of the relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">hasParentIn</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; possibleParents,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given object is child of any of the given parent objects.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isChildOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owners,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Is given element is child of one of the given owners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">isDocumentationComment</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given comment used for storing element documentation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMultiplicityMany(int)">isMultiplicityMany</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given value is 'many' - it is more than 1 or is unlimited (-1).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleParent,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if the given element is child of a given parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isParentOf</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleParent,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if the given element is child of a given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRelationship</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if a given element is a relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelationship(java.lang.Class)">isRelationship</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given class is relationship</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelationshipAlwaysInClient(java.lang.Class)">isRelationshipAlwaysInClient</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> relationshipClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if the Relationship of the given class type is always owned by a client element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseMultiplicityString(java.lang.String)">parseMultiplicityString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setClientElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> client)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set client of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setComment</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> documentation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set comment (documentation) for an element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">setCommentElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set given Comment as documentation of given Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a><wbr/>(int lower,
 int upper,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set multiplicity to an element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets multiplicity for a specified multiplicity element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSupplierElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set supplier of the relationship.</div>
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
<section class="detail" id="RELATIONSHIP_TYPES">
<h3>RELATIONSHIP_TYPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt;</span> <span class="element-name">RELATIONSHIP_TYPES</span></div>
<div class="block">Relationship like classes</div>
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
<h3>Elements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Elements</span>()</div>
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
<section class="detail" id="hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>hasParentIn</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasParentIn</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; possibleParents,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</span></div>
<div class="block">Checks if given object is child of any of the given parent objects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleChild</code> - possible child</dd>
<dd><code>possibleParents</code> - possible parents</dd>
<dt>Returns:</dt>
<dd>true if the given possibleChild is a child of any of given possibleParents</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleParent,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</span></div>
<div class="block">Checks if the given element is child of a given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleChild</code> - possible child</dd>
<dd><code>possibleParent</code> - possible parent</dd>
<dt>Returns:</dt>
<dd>true if possibleChild is a child of possibleParent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleParent,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleChild)</span></div>
<div class="block">Checks if the given element is child of a given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleChild</code> - possible child</dd>
<dd><code>possibleParent</code> - possible parent</dd>
<dt>Returns:</dt>
<dd>true if possibleChild is a child of possibleParent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isChildOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isChildOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owners,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> child)</span></div>
<div class="block">Is given element is child of one of the given owners.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owners</code> - the owners to check.</dd>
<dd><code>child</code> - the child element to check owners for</dd>
<dt>Returns:</dt>
<dd>true, if given child is child of some given owner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setComment</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> documentation)</span></div>
<div class="block">Set comment (documentation) for an element. Comment is set on the first element in an owned comments collection.
 If documentation is null or empty string, remove the comment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to set documentation</dd>
<dd><code>documentation</code> - documentation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getComment</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns documentation of given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to get documentation.</dd>
<dt>Returns:</dt>
<dd>element documentation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCommentElementOrCreate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">getCommentElementOrCreate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns documentation Comment for this element. If Comment is not set yet, new Comment is created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCommentElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">getCommentElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns documentation Comment for this Element. If Comment is not set, returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>getCommentElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">getCommentElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt; commentOfAnnotatedElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">
<h3>isDocumentationComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDocumentationComment</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</span></div>
<div class="block">Checks if given comment used for storing element documentation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>comment</code> - comment</dd>
<dt>Returns:</dt>
<dd>true if comment is used as documentation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">
<h3>setCommentElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCommentElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</span></div>
<div class="block">Set given Comment as documentation of given Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>comment</code> - comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfTypeIncludingItself</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfTypeIncludingItself</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</span></div>
<div class="block">Searches for the first direct or indirect owner of the given type among owners of the given element.
 Checks if the element itself is an instance of given ownerType. If yes, returns it, if no, looks
 for an owner of given instance in all element's ownership hierarchy. If such an owner does not exist, returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>ownerType</code> - the metaclass of owner to find. Found owner must be an instance of this class</dd>
<dt>Returns:</dt>
<dd>found owner or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</span></div>
<div class="block">Searches for the first direct or indirect owner of the given type among owners of the given element.
 Look for owner of given instance in all element's ownership hierarchy. If such an owner does not exist, returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element.</dd>
<dd><code>ownerType</code> - the metaclass of owner to find. Found owner must be an instance of this class.</dd>
<dt>Returns:</dt>
<dd>found owner or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfStrictTypeIncludingItself</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfStrictTypeIncludingItself</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</span></div>
<div class="block">Finds an owner of an element of a specific class type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which owner of a specific type should be found</dd>
<dd><code>ownerType</code> - class type of the owner</dd>
<dt>Returns:</dt>
<dd>found owner or null if the owner of a specific type was not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfStrictType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfStrictType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</span></div>
<div class="block">Finds an owner of an element of a specific class type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which parent of a specific type should be found</dd>
<dd><code>ownerType</code> - class type of the owner</dd>
<dt>Returns:</dt>
<dd>found owner or null if an owner of a specific type was not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>setMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMultiplicity</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</span></div>
<div class="block">Sets multiplicity for a specified multiplicity element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - values that make sense: "0", "1", "*", "0..*", "1..*", "0..1". If null, multiplicity will become unspecified</dd>
<dd><code>element</code> - multiplicity element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseMultiplicityString(java.lang.String)">
<h3>parseMultiplicityString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">parseMultiplicityString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</span></div>
<div class="block">Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiplicityMany(int)">
<h3>isMultiplicityMany</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMultiplicityMany</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Check if given value is 'many' - it is more than 1 or is unlimited (-1).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value</dd>
<dt>Returns:</dt>
<dd>true if value is many</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>setMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMultiplicity</span><wbr/><span class="parameters">(int lower,
 int upper,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</span></div>
<div class="block">Set multiplicity to an element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - lover</dd>
<dd><code>upper</code> - upper</dd>
<dd><code>element</code> - element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose(java.util.Collection)">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">dispose</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Dispose all elements in the given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to dispose</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRelationship</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if a given element is a relationship. MD treats Transition, ActivityEdge and InstanceSpecifications used as Links as relationships.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if an element is relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelationship(java.lang.Class)">
<h3>isRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRelationship</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</span></div>
<div class="block">Check if given class is relationship</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - given class</dd>
<dt>Returns:</dt>
<dd>true if relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelationshipAlwaysInClient(java.lang.Class)">
<h3>isRelationshipAlwaysInClient</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRelationshipAlwaysInClient</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> relationshipClass)</span></div>
<div class="block">Check if the Relationship of the given class type is always owned by a client element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationshipClass</code> - relationship class type</dd>
<dt>Returns:</dt>
<dd>return true if given relationship is always owned by client element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getClientElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getClientElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</span></div>
<div class="block">Get a client of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dt>Returns:</dt>
<dd>client of given relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSupplierElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSupplierElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</span></div>
<div class="block">Get supplier of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getSupplierElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSupplierElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 boolean takeUserFriendly)</span></div>
<div class="block">Get supplier of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dd><code>takeUserFriendly</code> - take a user-friendly element in some cases (for example, owning classifier instead of template signature)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setClientElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClientElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> client)</span></div>
<div class="block">Set client of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element</dd>
<dd><code>client</code> - client element that will be set to a specified relationship model element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setSupplierElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSupplierElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplier)</span></div>
<div class="block">Set supplier of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dd><code>supplier</code> - supplier element that will be set to a specified relationship model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">
<h3>getDependentClients</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getDependentClients</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</span></div>
<div class="block">Collects elements those are connected with Dependencies as clients with a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>dependencyClass</code> - dependency class to filter</dd>
<dt>Returns:</dt>
<dd>list of dependent client elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">
<h3>getDependentSuppliers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getDependentSuppliers</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</span></div>
<div class="block">Collects elements those are connected with Dependencies as suppliers with a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dd><code>dependencyClass</code> - dependency class to filter</dd>
<dt>Returns:</dt>
<dd>list of dependent supplier elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>getMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMultiplicity</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</span></div>
<div class="block">Returns multiplicity string for a specified multiplicity element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - multiplicity element.</dd>
<dt>Returns:</dt>
<dd>multiplicity expression: "0", "1", "*", "0..*", "1..*", "0..1". "" is returned if no multiplicity is set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return a name of given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - name</dd>
<dt>Returns:</dt>
<dd>name of give an element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getOppositeEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getOppositeEnd</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> end)</span></div>
<div class="block">Return the opposite relationship end</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship</dd>
<dd><code>end</code> - end</dd>
<dt>Returns:</dt>
<dd>opposite end</dd>
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
