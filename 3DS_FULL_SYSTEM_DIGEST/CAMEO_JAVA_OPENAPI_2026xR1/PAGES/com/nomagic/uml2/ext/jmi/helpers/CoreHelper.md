# JAVA OPENAPI: CoreHelper (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/helpers/CoreHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/CoreHelper.html`
- source_sha256: `6316c1a869e11b7aae02ebed189be0b0ca822e04aee44fddcb2f263af4c5a25e`
- captured_utc: `2026-07-14T16:46:22.358098+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class CoreHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.helpers.CoreHelper

Direct Known Subclasses:
`[ValueSpecificationHelper](ValueSpecificationHelper.html)`

@OpenApiAllpublic classCoreHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Utility class for working with core UML elements

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CoreHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[areElementsEditable](#areElementsEditable(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)`
Indicates if all elements in a collection are editable.
`static boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../magicdraw/uml/BaseElement.html) parent,
 [BaseElement](../../../../magicdraw/uml/BaseElement.html) child)`
Checks if current element can add given element.
`static boolean`
`[canAssignName](#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) data,
 boolean symbol)`
Checks if given name can be assigned to the given ModelElement.
`static boolean`
`[canAssignName](#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) data,
 boolean symbol,
 boolean showError)`
Checks if given name can be assigned to the given Element.
`static boolean`
`[canAssignName](#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) data,
 boolean symbol,
 boolean showError,
 boolean doNotCheckBehavioralFeature)`
Checks if given name can be assigned to the given ModelElement.
`static boolean`
`[canMoveChildInto](#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) parent,
 [Element](../../magicdraw/classes/mdkernel/Element.html) child)`
Returns true, if child can be moved to the parent.
`static boolean`
`[canMoveChildInto](#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) parent,
 [Element](../../magicdraw/classes/mdkernel/Element.html) child,
 boolean checkPermissions)`
Returns true, if child can be moved to the parent.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[collectRelationships](#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Collects connected relations of specified element.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[collectRelationships](#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> predicate,
 boolean includeIndirect)`
Collects connected relations of specified element.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[collectRelationshipsByType](#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> relationType,
 boolean includeIndirect)`
Collects relations connected to specified element by relation class type.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[collectRelationshipsIncludeIndirect](#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Collects relations connected to specified element and some elements that are owned by that element.
`static void`
`[dispose](#dispose(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)`
Dispose all elements in the given collection.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[findAcceptableParentFor](#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../magicdraw/classes/mdkernel/Element.html) owner)`
Goes up in the hierarchy of ownership until owner is found for a given element.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[findAcceptableParentFor](#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../magicdraw/classes/mdkernel/Element.html) owner,
 boolean checkPermissions)`
Goes up in the hierarchy of ownership until owner is found for a given element.
`static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfStrictType](#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> ownerType)`
Finds owner of an element of a specific class type.
`static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfStrictTypeIncludingItself](#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> ownerType)`
Finds owner of an element of a specific class type.
`static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfType](#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)`
Searches for first direct or indirect owner of the given type among owners of the given element.
`static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> 
T`
`[findOwnerOfTypeIncludingItself](#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)`
Searches for first direct or indirect owner of the given type among owners of the given element.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[findParent](#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) clientME,
 [Element](../../magicdraw/classes/mdkernel/Element.html) supplierME,
 [Element](../../magicdraw/classes/mdkernel/Element.html) diagramParent)`
Looks for a possible parent for given relationship.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[findParent](#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) clientME,
 [Element](../../magicdraw/classes/mdkernel/Element.html) supplierME,
 [Element](../../magicdraw/classes/mdkernel/Element.html) diagramParent,
 boolean checkPermissions)`
Looks for a possible parent for given relationship.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getAdditionalElementsIterator](#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns iterator of additional contained elements defined in DSL specification by additionalContentProperty.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getClientElement](#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship)`
Get client of the relationship.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getComment](#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation of given element.
`static [Comment](../../magicdraw/classes/mdkernel/Comment.html)`
`[getCommentElement](#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation Comment for this Element.
`static [Comment](../../magicdraw/classes/mdkernel/Comment.html)`
`[getCommentElementOrCreate](#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns documentation Comment for this element.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html)>`
`[getDependentClients](#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class))([NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)`
Collects elements those are connected with Dependencies as clients with a given element
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html)>`
`[getDependentSuppliers](#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class))([NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)`
Collects elements those are connected with Dependencies as suppliers with a given element
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[getFirstMemberEnd](#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../magicdraw/classes/mdkernel/Association.html) assoc)`
Get first property member end of association.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMultiplicity](#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([MultiplicityElement](../../magicdraw/classes/mdkernel/MultiplicityElement.html) element)`
Returns multiplicity string for specified multiplicity element.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../magicdraw/uml/BaseElement.html) element)`
Return a name of given element
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getOppositeEnd](#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) end)`
Return opposite relationship end
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getOwnedElementsIncludingAdditional](#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned)`
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[getSecondMemberEnd](#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../magicdraw/classes/mdkernel/Association.html) assoc)`
Get second property member end of association.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getSupplierElement](#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship)`
Get supplier of the relationship.
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getSupplierElement](#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 boolean takeUserFriendly)`
Get supplier of the relationship.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getSupplierElements](#getSupplierElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> relationships)`
Collect suppliers of the given relationships
`static boolean`
`[hasParentIn](#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../../../magicdraw/uml/BaseElement.html)> possibleParents,
 [BaseElement](../../../../magicdraw/uml/BaseElement.html) possibleChild)`
Checks if given object is child of any of the given parent objects.
`static boolean`
`[isChildOf](#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> owners,
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Is given element is child of some given owner.
`static boolean`
`[isDocumentationComment](#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment))([Comment](../../magicdraw/classes/mdkernel/Comment.html) comment)`
Checks if given comment used for storing element documentation.
`static boolean`
`[isMultiplicityMany](#isMultiplicityMany(int))(int value)`
Check if given value is 'many' -it is more than 1 or is unlimited (-1).
`static boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../magicdraw/uml/BaseElement.html) possibleParent,
 [BaseElement](../../../../magicdraw/uml/BaseElement.html) possibleChild)`
Checks if given object is child of given parent object.
`static boolean`
`[isParentOf](#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) possibleParent,
 [Element](../../magicdraw/classes/mdkernel/Element.html) possibleChild)`
Checks if given object is child of given parent object.
`static boolean`
`[isRelationship](#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Check if given element is a relationship.
`static boolean`
`[isRelationshipAlwaysInClient](#isRelationshipAlwaysInClient(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) relationshipClass)`
Check if relationship if given class type is always owned by a client element
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]`
`[parseMultiplicityString](#parseMultiplicityString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression)`
Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds
`static void`
`[setClientElement](#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) client)`
Set client of the relationship.
`static void`
`[setComment](#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) documentation)`
Set comment (documentation) for element.
`static void`
`[setCommentElement](#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Comment](../../magicdraw/classes/mdkernel/Comment.html) comment)`
Set given Comment as documentation of given Element.
`static void`
`[setConstraintText](#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean))([Constraint](../../magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean useName,
 boolean useExpression)`
Set text for constraint as name or as expression
`static void`
`[setConstraintText](#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean))([Constraint](../../magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean useName,
 boolean useExpression,
 boolean showWarnings)`
Set text for constraint as name or as expression
`static void`
`[setMultiplicity](#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))(int lower,
 int upper,
 [MultiplicityElement](../../magicdraw/classes/mdkernel/MultiplicityElement.html) element)`
Set multiplicity to element
`static void`
`[setMultiplicity](#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression,
 [MultiplicityElement](../../magicdraw/classes/mdkernel/MultiplicityElement.html) element)`
Sets multiplicity for specified multiplicity element.
`static void`
`[setSupplierElement](#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) supplier)`
Set supplier of the relationship.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CoreHelper
public CoreHelper()
 ============ METHOD DETAIL ========== 
Method Details
hasParentIn
public static boolean hasParentIn([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../../../../magicdraw/uml/BaseElement.html)> possibleParents,
 [BaseElement](../../../../magicdraw/uml/BaseElement.html) possibleChild)
Checks if given object is child of any of the given parent objects.
Parameters:
`possibleParents` - possible parents
`possibleChild` - possible child
Returns:
true if the given possibleChild is a child of any of given possibleParents
isParentOf
public static boolean isParentOf([BaseElement](../../../../magicdraw/uml/BaseElement.html) possibleParent,
 [BaseElement](../../../../magicdraw/uml/BaseElement.html) possibleChild)
Checks if given object is child of given parent object.
Parameters:
`possibleParent` - possible parent
`possibleChild` - possible child
Returns:
true if possibleChild is child of possibleParent.
isParentOf
public static boolean isParentOf([Element](../../magicdraw/classes/mdkernel/Element.html) possibleParent,
 [Element](../../magicdraw/classes/mdkernel/Element.html) possibleChild)
Checks if given object is child of given parent object.
Parameters:
`possibleParent` - possible parent
`possibleChild` - possible child
Returns:
true if possibleChild is child of possibleParent
setComment
public static void setComment([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) documentation)
Set comment (documentation) for element. Comment is set on the first element in owned comments collection.
 If documentation is null or empty string, removed the comment.
Parameters:
`element` - element to set documentation.
`documentation` - documentation text.
getComment
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getComment([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns documentation of given element.
Parameters:
`element` - element to get documentation.
Returns:
element documentation.
getCommentElementOrCreate
public static [Comment](../../magicdraw/classes/mdkernel/Comment.html) getCommentElementOrCreate([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns documentation Comment for this element. If Comment is not set yet, new Comment is created.
Parameters:
`element` - element
Returns:
comment
getCommentElement
@CheckForNullpublic static [Comment](../../magicdraw/classes/mdkernel/Comment.html) getCommentElement([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns documentation Comment for this Element. If Comment is not set, returns null.
Parameters:
`element` - element
Returns:
comment
setCommentElement
public static void setCommentElement([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Comment](../../magicdraw/classes/mdkernel/Comment.html) comment)
Set given Comment as documentation of given Element.
Parameters:
`element` - element
`comment` - comment
isDocumentationComment
public static boolean isDocumentationComment([Comment](../../magicdraw/classes/mdkernel/Comment.html) comment)
Checks if given comment used for storing element documentation.
Parameters:
`comment` - comment
Returns:
true if comment is used as documentation
findOwnerOfTypeIncludingItself
@CheckForNullpublic static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> T findOwnerOfTypeIncludingItself(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)
Searches for first direct or indirect owner of the given type among owners of the given element.
 Checks if the element itself is an instance of given ownerType. If yes, returns it, if no, looks
 for owner of given instance in all element's ownership hierarchy. If such owner does not exist, returns null.
Parameters:
`element` - element
`ownerType` - the meta class of owner to find. Found owner must be instance of this class
Returns:
found owner or null
findOwnerOfType
@CheckForNullpublic static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> T findOwnerOfType(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends T> ownerType)
Searches for first direct or indirect owner of the given type among owners of the given element.
 Look for owner of given instance in all element's ownership hierarchy. If such owner does not exist, returns null.
Parameters:
`element` - element.
`ownerType` - the meta class of owner to find. Found owner must be instance of this class.
Returns:
found owner or null.
findOwnerOfStrictTypeIncludingItself
@CheckForNullpublic static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> T findOwnerOfStrictTypeIncludingItself(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> ownerType)
Finds owner of an element of a specific class type.
Parameters:
`element` - element for which owner of a specific type should be found
`ownerType` - class type of the owner
Returns:
found owner or null if owner of a specific type was not found
findOwnerOfStrictType
@CheckForNullpublic static <T extends [Element](../../magicdraw/classes/mdkernel/Element.html)> T findOwnerOfStrictType([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> ownerType)
Finds owner of an element of a specific class type.
Parameters:
`element` - element for which parent of a specific type should be found
`ownerType` - class type of the owner
Returns:
found owner or null if owner of a specific type was not found
dispose
public static void dispose([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)
Dispose all elements in the given collection.
Parameters:
`elements` - elements to dispose
setMultiplicity
public static void setMultiplicity(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression,
 [MultiplicityElement](../../magicdraw/classes/mdkernel/MultiplicityElement.html) element)
Sets multiplicity for specified multiplicity element.
Parameters:
`expression` - values that make sense: "0", "1", "*", "0..*", "1..*", "0..1". If null, multiplicity will become unspecified
`element` - multiplicity element.
parseMultiplicityString
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] parseMultiplicityString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression)
Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds
Parameters:
`expression` - expression
getMultiplicity
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMultiplicity(@CheckForNull
 [MultiplicityElement](../../magicdraw/classes/mdkernel/MultiplicityElement.html) element)
Returns multiplicity string for specified multiplicity element.
Parameters:
`element` - multiplicity element.
Returns:
multiplicity expression : "0", "1", "*", "0..*", "1..*", "0..1". "" is returned if no multiplicity is set.
isMultiplicityMany
public static boolean isMultiplicityMany(int value)
Check if given value is 'many' -it is more than 1 or is unlimited (-1).
Parameters:
`value` - value
Returns:
true if value is many
setMultiplicity
public static void setMultiplicity(int lower,
 int upper,
 [MultiplicityElement](../../magicdraw/classes/mdkernel/MultiplicityElement.html) element)
Set multiplicity to element
Parameters:
`lower` - lover
`upper` - upper
`element` - element
getSupplierElements
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getSupplierElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> relationships)
Collect suppliers of the given relationships
Parameters:
`relationships` - relationships
Returns:
suppliers of relationships
getSupplierElement
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getSupplierElement([Element](../../magicdraw/classes/mdkernel/Element.html) relationship)
Get supplier of the relationship.
Parameters:
`relationship` - relationship model element.
getSupplierElement
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getSupplierElement([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 boolean takeUserFriendly)
Get supplier of the relationship.
Parameters:
`relationship` - relationship model element.
`takeUserFriendly` - take user friendly element in some cases (for example owning classifier instead of template signature)
setSupplierElement
public static void setSupplierElement([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) supplier)
Set supplier of the relationship.
Parameters:
`relationship` - relationship model element.
`supplier` - supplier element that will be set to specified relationship model element.
getClientElement
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getClientElement([Element](../../magicdraw/classes/mdkernel/Element.html) relationship)
Get client of the relationship.
Parameters:
`relationship` - relationship model element.
Returns:
client of given relationship
collectRelationships
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> collectRelationships([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> predicate,
 boolean includeIndirect)
Collects connected relations of specified element.
Parameters:
`element` - element
`predicate` - filters collected relations
`includeIndirect` - include indirect relations.
Returns:
relations that are connected to specified element.
collectRelationships
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> collectRelationships([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Collects connected relations of specified element.
Parameters:
`element` - element
Returns:
relations that are connected to specified element.
collectRelationshipsIncludeIndirect
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> collectRelationshipsIncludeIndirect([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Collects relations connected to specified element and some elements that are owned by that element. For example if element is action collects relations attached to it and it's input or output pins.
Parameters:
`element` - element
Returns:
relations that are connected to specified element and some elements that are owned by that element.
collectRelationshipsByType
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collectRelationshipsByType([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> relationType,
 boolean includeIndirect)
Collects relations connected to specified element by relation class type.
Parameters:
`element` - element
`relationType` - relation class type
`includeIndirect` - should include indirect
Returns:
relations that are connected to specified element and some elements that are owned by that element.
setClientElement
public static void setClientElement([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) client)
Set client of the relationship.
Parameters:
`relationship` - relationship model element.
`client` - client element that will be set to specified relationship model element.
getFirstMemberEnd
public static [Property](../../magicdraw/classes/mdkernel/Property.html) getFirstMemberEnd([Association](../../magicdraw/classes/mdkernel/Association.html) assoc)
Get first property member end of association.
Parameters:
`assoc` - association model element.
Returns:
first property member end of association.
getSecondMemberEnd
public static [Property](../../magicdraw/classes/mdkernel/Property.html) getSecondMemberEnd([Association](../../magicdraw/classes/mdkernel/Association.html) assoc)
Get second property member end of association.
Parameters:
`assoc` - association model element.
Returns:
second property member end of association.
areElementsEditable
public static boolean areElementsEditable([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)
Indicates if all elements in a collection are editable.
Parameters:
`elements` - a collection of elements to check
Returns:
true if all elements in a collection are editable, false otherwise
findAcceptableParentFor
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) findAcceptableParentFor([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) owner,
 boolean checkPermissions)
Goes up in the hierarchy of ownership until owner is found for a given element.
Parameters:
`element` - element
`owner` - candidate for owner
`checkPermissions` - check editing permissions
Returns:
found owner or null
findAcceptableParentFor
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) findAcceptableParentFor([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) owner)
Goes up in the hierarchy of ownership until owner is found for a given element. Checks owner editing permissions.
Parameters:
`element` - element
`owner` - candidate for owner
Returns:
found owner or null
canMoveChildInto
public static boolean canMoveChildInto([Element](../../magicdraw/classes/mdkernel/Element.html) parent,
 [Element](../../magicdraw/classes/mdkernel/Element.html) child)
Returns true, if child can be moved to the parent.
 This can be done if parent can add such child and parent does not have other child with the same name for example.
canMoveChildInto
public static boolean canMoveChildInto([Element](../../magicdraw/classes/mdkernel/Element.html) parent,
 [Element](../../magicdraw/classes/mdkernel/Element.html) child,
 boolean checkPermissions)
Returns true, if child can be moved to the parent.
 This can be done if parent can add such child and parent does not have other child with the same
 name.
canAssignName
public static boolean canAssignName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) data,
 boolean symbol,
 boolean showError)
Checks if given name can be assigned to the given Element.
Parameters:
`name` - a new name for Element
`data` - a given Element
`symbol` - true if changing symbol name
`showError` - show error in UI in case of name conflict
Returns:
true if name can be changed
canAssignName
public static boolean canAssignName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) data,
 boolean symbol)
Checks if given name can be assigned to the given ModelElement.
Parameters:
`name` - a new name for ModelElement.
`data` - a given ModelElement.
`symbol` - true if changing symbol name
Returns:
new name for ModelElement or null if given name can not be assigned to the ModelElement.
canAssignName
public static boolean canAssignName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) data,
 boolean symbol,
 boolean showError,
 boolean doNotCheckBehavioralFeature)
Checks if given name can be assigned to the given ModelElement.
Parameters:
`name` - a new name for ModelElement.
`data` - a given ModelElement.
`symbol` - true if changing symbol name
`showError` - show error in UI in case of name conflict
Returns:
new name for ModelElement or null if given name can not be assigned to the ModelElement.
isRelationship
public static boolean isRelationship(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)
Check if given element is a relationship. MD treats Transition, ActivityEdge and InstanceSpecifications used as Links as relationships.
Parameters:
`element` - element
Returns:
true if element is relationship
getOppositeEnd
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getOppositeEnd([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) end)
Return opposite relationship end
Parameters:
`relationship` - relationship
`end` - end
Returns:
opposite end
findParent
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) findParent([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) clientME,
 [Element](../../magicdraw/classes/mdkernel/Element.html) supplierME,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) diagramParent)
Looks for a possible parent for given relationship.
 Possible parent is calculated according client/supplier and relationship type.
Parameters:
`relationship` - relation for which possible parent should be found.
`clientME` - relationship client element
`supplierME` - relationship supplier element
`diagramParent` - can be null if diagram is not important in context
Returns:
possible parent for a given relation if found, null otherwise.
findParent
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) findParent([Element](../../magicdraw/classes/mdkernel/Element.html) relationship,
 [Element](../../magicdraw/classes/mdkernel/Element.html) clientME,
 [Element](../../magicdraw/classes/mdkernel/Element.html) supplierME,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) diagramParent,
 boolean checkPermissions)
Looks for a possible parent for given relationship.
 Possible parent is calculated according client/supplier and relationship type.
Parameters:
`relationship` - relation for which possible parent should be found.
`clientME` - relationship client element
`supplierME` - relationship supplier element
`diagramParent` - can be null if diagram is not important in context
`checkPermissions` - indicates if permissions should be checked.
Returns:
possible parent for a given relation if found, null otherwise.
isRelationshipAlwaysInClient
public static boolean isRelationshipAlwaysInClient([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) relationshipClass)
Check if relationship if given class type is always owned by a client element
Parameters:
`relationshipClass` - relationship class type
Returns:
return true if given relationship is always owned by client element
isChildOf
public static boolean isChildOf([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> owners,
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)
Is given element is child of some given owner.
Parameters:
`owners` - the given owners.
`element` - the given element
Returns:
true if given element is child of some given owner.
getOwnedElementsIncludingAdditional
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getOwnedElementsIncludingAdditional([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 boolean includePureOwned)
Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.
Parameters:
`includePureOwned` - include element owned directly in ownedElement UML meta property
Returns:
owned elements of the given Element
getAdditionalElementsIterator
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getAdditionalElementsIterator([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns iterator of additional contained elements defined in DSL specification by additionalContentProperty.
Returns:
iterator of additional elements
getName
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName([BaseElement](../../../../magicdraw/uml/BaseElement.html) element)
Return a name of given element
Parameters:
`element` - name
Returns:
name of give element
canAddChild
public static boolean canAddChild([BaseElement](../../../../magicdraw/uml/BaseElement.html) parent,
 [BaseElement](../../../../magicdraw/uml/BaseElement.html) child)
Checks if current element can add given element.
 

 Uses such rules:
 1. current object is not the same as given object.
 2. current object is not a child of given object.
 Current implementation returns false.
Returns:
true, if checking rules are true.
setConstraintText
public static void setConstraintText([Constraint](../../magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean useName,
 boolean useExpression)
Set text for constraint as name or as expression
Parameters:
`constraint` - constraint
`text` - text
`useName` - set text as name
`useExpression` - set text as expression
setConstraintText
public static void setConstraintText([Constraint](../../magicdraw/classes/mdkernel/Constraint.html) constraint,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean useName,
 boolean useExpression,
 boolean showWarnings)
Set text for constraint as name or as expression
Parameters:
`constraint` - constraint
`text` - text
`useName` - set text as name
`useExpression` - set text as expression
`showWarnings` - shows parsing warnings in UI if there were any
getDependentClients
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html)> getDependentClients([NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)
Collects elements those are connected with Dependencies as clients with a given element
Parameters:
`element` - the given element
`dependencyClass` - dependency class to filter
Returns:
list of dependent client elements
getDependentSuppliers
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html)> getDependentSuppliers([NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Dependency](../../magicdraw/classes/mddependencies/Dependency.html)> dependencyClass)
Collects elements those are connected with Dependencies as suppliers with a given element
Parameters:
`element` - the given element
`dependencyClass` - dependency class to filter
Returns:
list of dependent supplier elements

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class CoreHelper">Class CoreHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.CoreHelper</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ValueSpecificationHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CoreHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for working with core UML elements</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CoreHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#areElementsEditable(java.util.Collection)">areElementsEditable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if all elements in a collection are editable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a><wbr/>(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> parent,
 <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if current element can add given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">canAssignName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> data,
 boolean symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given name can be assigned to the given ModelElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)">canAssignName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> data,
 boolean symbol,
 boolean showError)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given name can be assigned to the given Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)">canAssignName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> data,
 boolean symbol,
 boolean showError,
 boolean doNotCheckBehavioralFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given name can be assigned to the given ModelElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canMoveChildInto</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true, if child can be moved to the parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">canMoveChildInto</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> child,
 boolean checkPermissions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true, if child can be moved to the parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationships</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects connected relations of specified element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)">collectRelationships</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; predicate,
 boolean includeIndirect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects connected relations of specified element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">collectRelationshipsByType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; relationType,
 boolean includeIndirect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects relations connected to specified element by relation class type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationshipsIncludeIndirect</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects relations connected to specified element and some elements that are owned by that element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose(java.util.Collection)">dispose</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dispose all elements in the given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findAcceptableParentFor</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Goes up in the hierarchy of ownership until owner is found for a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findAcceptableParentFor</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner,
 boolean checkPermissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Goes up in the hierarchy of ownership until owner is found for a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds owner of an element of a specific class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictTypeIncludingItself</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds owner of an element of a specific class type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for first direct or indirect owner of the given type among owners of the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfTypeIncludingItself</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for first direct or indirect owner of the given type among owners of the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findParent</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientME,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierME,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> diagramParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a possible parent for given relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findParent</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientME,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierME,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> diagramParent,
 boolean checkPermissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a possible parent for given relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAdditionalElementsIterator</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns iterator of additional contained elements defined in DSL specification by additionalContentProperty.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClientElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get client of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComment</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns documentation of given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns documentation Comment for this Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElementOrCreate</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns documentation Comment for this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentClients</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects elements those are connected with Dependencies as clients with a given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentSuppliers</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects elements those are connected with Dependencies as suppliers with a given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getFirstMemberEnd</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> assoc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get first property member end of association.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">getMultiplicity</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns multiplicity string for specified multiplicity element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getName(com.nomagic.magicdraw.uml.BaseElement)">getName</a><wbr/>(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a name of given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOppositeEnd</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return opposite relationship end</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getOwnedElementsIncludingAdditional</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getSecondMemberEnd</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> assoc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get second property member end of association.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSupplierElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get supplier of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getSupplierElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 boolean takeUserFriendly)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get supplier of the relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElements(java.util.Collection)">getSupplierElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; relationships)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect suppliers of the given relationships</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">hasParentIn</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; possibleParents,
 <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given object is child of any of the given parent objects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isChildOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owners,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Is given element is child of some given owner.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">isDocumentationComment</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given comment used for storing element documentation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMultiplicityMany(int)">isMultiplicityMany</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given value is 'many' -it is more than 1 or is unlimited (-1).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleParent,
 <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given object is child of given parent object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isParentOf</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleParent,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleChild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given object is child of given parent object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRelationship</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element is a relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRelationshipAlwaysInClient(java.lang.Class)">isRelationshipAlwaysInClient</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> relationshipClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if relationship if given class type is always owned by a client element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseMultiplicityString(java.lang.String)">parseMultiplicityString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setClientElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> client)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set client of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setComment</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> documentation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set comment (documentation) for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">setCommentElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set given Comment as documentation of given Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)">setConstraintText</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean useName,
 boolean useExpression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set text for constraint as name or as expression</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)">setConstraintText</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean useName,
 boolean useExpression,
 boolean showWarnings)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set text for constraint as name or as expression</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a><wbr/>(int lower,
 int upper,
 <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set multiplicity to element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression,
 <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets multiplicity for specified multiplicity element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSupplierElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set supplier of the relationship.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>CoreHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CoreHelper</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasParentIn</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; possibleParents,
 <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</span></div>
<div class="block">Checks if given object is child of any of the given parent objects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleParents</code> - possible parents</dd>
<dd><code>possibleChild</code> - possible child</dd>
<dt>Returns:</dt>
<dd>true if the given possibleChild is a child of any of given possibleParents</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleParent,
 <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</span></div>
<div class="block">Checks if given object is child of given parent object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleParent</code> - possible parent</dd>
<dd><code>possibleChild</code> - possible child</dd>
<dt>Returns:</dt>
<dd>true if possibleChild is child of possibleParent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleParent,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> possibleChild)</span></div>
<div class="block">Checks if given object is child of given parent object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleParent</code> - possible parent</dd>
<dd><code>possibleChild</code> - possible child</dd>
<dt>Returns:</dt>
<dd>true if possibleChild is child of possibleParent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setComment</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> documentation)</span></div>
<div class="block">Set comment (documentation) for element. Comment is set on the first element in owned comments collection.
 If documentation is null or empty string, removed the comment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to set documentation.</dd>
<dd><code>documentation</code> - documentation text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getComment</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">getCommentElementOrCreate</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">getCommentElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
<section class="detail" id="setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">
<h3>setCommentElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCommentElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</span></div>
<div class="block">Set given Comment as documentation of given Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>comment</code> - comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">
<h3>isDocumentationComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDocumentationComment</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</span></div>
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
<section class="detail" id="findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfTypeIncludingItself</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfTypeIncludingItself</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</span></div>
<div class="block">Searches for first direct or indirect owner of the given type among owners of the given element.
 Checks if the element itself is an instance of given ownerType. If yes, returns it, if no, looks
 for owner of given instance in all element's ownership hierarchy. If such owner does not exist, returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>ownerType</code> - the meta class of owner to find. Found owner must be instance of this class</dd>
<dt>Returns:</dt>
<dd>found owner or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends T&gt; ownerType)</span></div>
<div class="block">Searches for first direct or indirect owner of the given type among owners of the given element.
 Look for owner of given instance in all element's ownership hierarchy. If such owner does not exist, returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element.</dd>
<dd><code>ownerType</code> - the meta class of owner to find. Found owner must be instance of this class.</dd>
<dt>Returns:</dt>
<dd>found owner or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfStrictTypeIncludingItself</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfStrictTypeIncludingItself</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</span></div>
<div class="block">Finds owner of an element of a specific class type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which owner of a specific type should be found</dd>
<dd><code>ownerType</code> - class type of the owner</dd>
<dt>Returns:</dt>
<dd>found owner or null if owner of a specific type was not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findOwnerOfStrictType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findOwnerOfStrictType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ownerType)</span></div>
<div class="block">Finds owner of an element of a specific class type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which parent of a specific type should be found</dd>
<dd><code>ownerType</code> - class type of the owner</dd>
<dt>Returns:</dt>
<dd>found owner or null if owner of a specific type was not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose(java.util.Collection)">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">dispose</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Dispose all elements in the given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to dispose</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>setMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMultiplicity</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression,
 <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</span></div>
<div class="block">Sets multiplicity for specified multiplicity element.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">parseMultiplicityString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</span></div>
<div class="block">Parses multiplicity of form 1..* and return array of 2 string [lower, upper] representing bounds</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>getMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMultiplicity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</span></div>
<div class="block">Returns multiplicity string for specified multiplicity element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - multiplicity element.</dd>
<dt>Returns:</dt>
<dd>multiplicity expression : "0", "1", "*", "0..*", "1..*", "0..1". "" is returned if no multiplicity is set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiplicityMany(int)">
<h3>isMultiplicityMany</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMultiplicityMany</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Check if given value is 'many' -it is more than 1 or is unlimited (-1).</div>
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
 <a href="../../magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element)</span></div>
<div class="block">Set multiplicity to element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - lover</dd>
<dd><code>upper</code> - upper</dd>
<dd><code>element</code> - element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierElements(java.util.Collection)">
<h3>getSupplierElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getSupplierElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; relationships)</span></div>
<div class="block">Collect suppliers of the given relationships</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationships</code> - relationships</dd>
<dt>Returns:</dt>
<dd>suppliers of  relationships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSupplierElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSupplierElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSupplierElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 boolean takeUserFriendly)</span></div>
<div class="block">Get supplier of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dd><code>takeUserFriendly</code> - take user friendly element in some cases (for example owning classifier instead of template signature)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setSupplierElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSupplierElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplier)</span></div>
<div class="block">Set supplier of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dd><code>supplier</code> - supplier element that will be set to specified relationship model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getClientElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getClientElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship)</span></div>
<div class="block">Get client of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dt>Returns:</dt>
<dd>client of given relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)">
<h3>collectRelationships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelationships</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; predicate,
 boolean includeIndirect)</span></div>
<div class="block">Collects connected relations of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>predicate</code> - filters collected relations</dd>
<dd><code>includeIndirect</code> - include indirect relations.</dd>
<dt>Returns:</dt>
<dd>relations that are connected to specified element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>collectRelationships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelationships</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Collects connected relations of specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>relations that are connected to specified element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>collectRelationshipsIncludeIndirect</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelationshipsIncludeIndirect</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Collects relations connected to specified element and some elements that are owned by that element. For example if element is action collects relations attached to it and it's input or output pins.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>relations that are connected to specified element and some elements that are owned by that element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">
<h3>collectRelationshipsByType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">collectRelationshipsByType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; relationType,
 boolean includeIndirect)</span></div>
<div class="block">Collects relations connected to specified element by relation class type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>relationType</code> - relation class type</dd>
<dd><code>includeIndirect</code> - should include indirect</dd>
<dt>Returns:</dt>
<dd>relations that are connected to specified element and some elements that are owned by that element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setClientElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClientElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> client)</span></div>
<div class="block">Set client of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship model element.</dd>
<dd><code>client</code> - client element that will be set to specified relationship model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>getFirstMemberEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getFirstMemberEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> assoc)</span></div>
<div class="block">Get first property member end of association.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>assoc</code> - association model element.</dd>
<dt>Returns:</dt>
<dd>first property member end of association.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>getSecondMemberEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSecondMemberEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> assoc)</span></div>
<div class="block">Get second property member end of association.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>assoc</code> - association model element.</dd>
<dt>Returns:</dt>
<dd>second property member end of association.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areElementsEditable(java.util.Collection)">
<h3>areElementsEditable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">areElementsEditable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Indicates if all elements in a collection are editable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - a collection of elements to check</dd>
<dt>Returns:</dt>
<dd>true if all elements in a collection are editable, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>findAcceptableParentFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">findAcceptableParentFor</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner,
 boolean checkPermissions)</span></div>
<div class="block">Goes up in the hierarchy of ownership until owner is found for a given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>owner</code> - candidate for owner</dd>
<dd><code>checkPermissions</code> - check editing permissions</dd>
<dt>Returns:</dt>
<dd>found owner or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>findAcceptableParentFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">findAcceptableParentFor</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner)</span></div>
<div class="block">Goes up in the hierarchy of ownership until owner is found for a given element. Checks owner editing permissions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>owner</code> - candidate for owner</dd>
<dt>Returns:</dt>
<dd>found owner or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>canMoveChildInto</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canMoveChildInto</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> child)</span></div>
<div class="block">Returns true, if child can be moved to the parent.
 This can be done if parent can add such child and parent does not have other child with the same name for example.</div>
</section>
</li>
<li>
<section class="detail" id="canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>canMoveChildInto</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canMoveChildInto</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> child,
 boolean checkPermissions)</span></div>
<div class="block">Returns true, if child can be moved to the parent.
 This can be done if parent can add such child and parent does not have other child with the same
 name.</div>
</section>
</li>
<li>
<section class="detail" id="canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)">
<h3>canAssignName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAssignName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> data,
 boolean symbol,
 boolean showError)</span></div>
<div class="block">Checks if given name can be assigned to the given Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - a new name for Element</dd>
<dd><code>data</code> - a given Element</dd>
<dd><code>symbol</code> - true if changing symbol name</dd>
<dd><code>showError</code> - show error in UI in case of name conflict</dd>
<dt>Returns:</dt>
<dd>true if name can be changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">
<h3>canAssignName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAssignName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> data,
 boolean symbol)</span></div>
<div class="block">Checks if given name can be assigned to the given ModelElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - a new name for ModelElement.</dd>
<dd><code>data</code> - a given ModelElement.</dd>
<dd><code>symbol</code> - true if changing symbol name</dd>
<dt>Returns:</dt>
<dd>new name for ModelElement or null if given name can not be assigned to the ModelElement.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)">
<h3>canAssignName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAssignName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> data,
 boolean symbol,
 boolean showError,
 boolean doNotCheckBehavioralFeature)</span></div>
<div class="block">Checks if given name can be assigned to the given ModelElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - a new name for ModelElement.</dd>
<dd><code>data</code> - a given ModelElement.</dd>
<dd><code>symbol</code> - true if changing symbol name</dd>
<dd><code>showError</code> - show error in UI in case of name conflict</dd>
<dt>Returns:</dt>
<dd>new name for ModelElement or null if given name can not be assigned to the ModelElement.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRelationship</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element is a relationship. MD treats Transition, ActivityEdge and InstanceSpecifications used as Links as relationships.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element is relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getOppositeEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getOppositeEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> end)</span></div>
<div class="block">Return opposite relationship end</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship</dd>
<dd><code>end</code> - end</dd>
<dt>Returns:</dt>
<dd>opposite end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>findParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">findParent</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientME,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierME,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> diagramParent)</span></div>
<div class="block">Looks for a possible parent for given relationship.
 Possible parent is calculated according client/supplier and relationship type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relation for which possible parent should be found.</dd>
<dd><code>clientME</code> - relationship client element</dd>
<dd><code>supplierME</code> - relationship supplier element</dd>
<dd><code>diagramParent</code> - can be null if diagram is not important in context</dd>
<dt>Returns:</dt>
<dd>possible parent for a given relation if found, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>findParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">findParent</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> clientME,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> supplierME,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> diagramParent,
 boolean checkPermissions)</span></div>
<div class="block">Looks for a possible parent for given relationship.
 Possible parent is calculated according client/supplier and relationship type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relation for which possible parent should be found.</dd>
<dd><code>clientME</code> - relationship client element</dd>
<dd><code>supplierME</code> - relationship supplier element</dd>
<dd><code>diagramParent</code> - can be null if diagram is not important in context</dd>
<dd><code>checkPermissions</code> - indicates if permissions should be checked.</dd>
<dt>Returns:</dt>
<dd>possible parent for a given relation if found, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRelationshipAlwaysInClient(java.lang.Class)">
<h3>isRelationshipAlwaysInClient</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRelationshipAlwaysInClient</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> relationshipClass)</span></div>
<div class="block">Check if relationship if given class type is always owned by a client element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationshipClass</code> - relationship class type</dd>
<dt>Returns:</dt>
<dd>return true if given relationship is always owned by client element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isChildOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isChildOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owners,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Is given element is child of some given owner.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owners</code> - the given owners.</dd>
<dd><code>element</code> - the given element</dd>
<dt>Returns:</dt>
<dd>true if given element is child of some given owner.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getOwnedElementsIncludingAdditional</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOwnedElementsIncludingAdditional</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includePureOwned)</span></div>
<div class="block">Return owned elements of the given Element including additional owned elements defined in DSL specification by additionalContentProperty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includePureOwned</code> - include element owned directly in ownedElement UML meta property</dd>
<dt>Returns:</dt>
<dd>owned elements of the given Element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAdditionalElementsIterator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getAdditionalElementsIterator</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns iterator of additional contained elements defined in DSL specification by additionalContentProperty.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>iterator of additional elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return a name of given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - name</dd>
<dt>Returns:</dt>
<dd>name of give element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> parent,
 <a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</span></div>
<div class="block">Checks if current element can add given element.
 <br/>
 Uses such rules:
 1. current object is not the same as given object.
 2. current object is not a child of given object.
 Current implementation returns false.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if checking rules are true.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)">
<h3>setConstraintText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setConstraintText</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean useName,
 boolean useExpression)</span></div>
<div class="block">Set text for constraint as name or as expression</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint</dd>
<dd><code>text</code> - text</dd>
<dd><code>useName</code> - set text as name</dd>
<dd><code>useExpression</code> - set text as expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)">
<h3>setConstraintText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setConstraintText</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean useName,
 boolean useExpression,
 boolean showWarnings)</span></div>
<div class="block">Set text for constraint as name or as expression</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint</dd>
<dd><code>text</code> - text</dd>
<dd><code>useName</code> - set text as name</dd>
<dd><code>useExpression</code> - set text as expression</dd>
<dd><code>showWarnings</code> - shows parsing warnings in UI if there were any</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">
<h3>getDependentClients</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getDependentClients</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getDependentSuppliers</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a>&gt; dependencyClass)</span></div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
