# JAVA OPENAPI: Relationships (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Relationships.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Relationships.html`
- source_sha256: `39db4a05ee0d6d9d02c38f769c1b42d9043270a8ad4ffe133ffa4f2a6cf48459`
- captured_utc: `2026-07-14T16:44:48.493850+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Relationships

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Relationships

@OpenApiAllpublic classRelationships
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Relationship`](kerml/Relationship.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Relationships](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static <R extends [Relationship](kerml/Relationship.html)> 
void`
`[addOwnedNotImpliedRelationships](#addOwnedNotImpliedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets)`
Appends new non‑implied relationships of the given type for the provided targets.
`static <R extends [Relationship](kerml/Relationship.html)> 
void`
`[editNotImpliedOwnedRelationships](#editNotImpliedOwnedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List,boolean))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets,
 boolean set)`
Edits not implied owned relationships and their targets.
`static <R extends [Relationship](kerml/Relationship.html)> 
void`
`[editOwnedRelationships](#editOwnedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List,boolean,boolean))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets,
 boolean set,
 boolean notImplied)`
Edits not implied owned relationships and their targets.
`static [Element](kerml/Element.html)`
`[findOwnerFor](#findOwnerFor(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element,boolean))([Relationship](kerml/Relationship.html) relationship,
 [Element](kerml/Element.html) source,
 [Element](kerml/Element.html) target,
 [Element](kerml/Element.html) diagramOwner,
 boolean checkPermissions)`
Looks for a possible owner for a given Relationship.
`static [Element](kerml/Element.html)`
`[getFirstOwnedRelatedElement](#getFirstOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))([Relationship](kerml/Relationship.html) relationship)`
Returns the first owned related element of the given relationship.
`static <T extends [Element](kerml/Element.html)> 
T`
`[getFirstOwnedRelatedElement](#getFirstOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,java.lang.Class))([Relationship](kerml/Relationship.html) relationship,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> clazz)`
Returns the first owned related element of the given relationship
 if it is an instance of the specified class.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Relationship](kerml/Relationship.html)>`
`[getIncoming](#getIncoming(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns all incoming relationships of the element.
`static <T extends [Relationship](kerml/Relationship.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[getIncoming](#getIncoming(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> ofType)`
Returns all incoming relationships of the given type.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Relationship](kerml/Relationship.html)>`
`[getOutgoing](#getOutgoing(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns all outgoing relationships of the element.
`static org.eclipse.emf.ecore.EClass`
`[getOwningMembershipEClass](#getOwningMembershipEClass(org.eclipse.emf.ecore.EClass,com.dassault_systemes.modeler.kerml.model.kerml.Namespace))(org.eclipse.emf.ecore.EClass childEClass,
 [Namespace](kerml/Namespace.html) owner)`
Determines the appropriate owning membership EClass for a child element.
`static <T extends [Relationship](kerml/Relationship.html)> 
[Feature](kerml/Feature.html)`
`[getRelationshipSourceFeature](#getRelationshipSourceFeature(T,java.util.function.Function))(T relationship,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<T,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> endFeatureProvider)`
Returns the source feature of a relationship when exactly two features exist.
`static <T extends [Relationship](kerml/Relationship.html)> 
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getRelationshipTargetFeature](#getRelationshipTargetFeature(T,java.util.function.Function))(T relationship,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<T,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> endFeatureProvider)`
Returns the target feature(s) of a relationship.
`static [Element](kerml/Element.html)`
`[getSource](#getSource(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))([Relationship](kerml/Relationship.html) relationship)`
Returns the first source element of the relationship.
`static [Element](kerml/Element.html)`
`[getTarget](#getTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))([Relationship](kerml/Relationship.html) relationship)`
Returns the first target element of the relationship.
`static boolean`
`[isAssociationOrConnector](#isAssociationOrConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element is an association or connector.
`static boolean`
`[isAssociationOrConnector](#isAssociationOrConnector(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the EClass represents an association or connector.
`static boolean`
`[isMemberRelationship](#isMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element is a member relationship.
`static boolean`
`[isMemberRelationship](#isMemberRelationship(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the EClass represents a member relationship.
`static boolean`
`[isNonMemberRelationship](#isNonMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element is a non‑member relationship.
`static boolean`
`[isNonMemberRelationship](#isNonMemberRelationship(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the EClass represents a non‑member relationship.
`static <R extends [Relationship](kerml/Relationship.html)> 
void`
`[setOwnedNotImpliedRelationships](#setOwnedNotImpliedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets)`
Replaces existing non‑implied relationships with new ones referencing the given targets.
`static void`
`[setSingleOwnedRelatedElement](#setSingleOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element))([Relationship](kerml/Relationship.html) relationship,
 [Element](kerml/Element.html) ownedRelatedElement)`
Sets the single owned related element of the relationship.
`static boolean`
`[setSource](#setSource(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element))([Relationship](kerml/Relationship.html) relationship,
 [Element](kerml/Element.html) source)`
Sets the source of the relationship.
`static boolean`
`[setTarget](#setTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element))([Relationship](kerml/Relationship.html) relationship,
 [Element](kerml/Element.html) target)`
Sets the target of the relationship.
`static <T extends [Relationship](kerml/Relationship.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[streamOfOwnedNotImpliedRelationship](#streamOfOwnedNotImpliedRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> clazz,
 boolean isInstance)`
Returns a stream of owned, non‑implied relationships of the given type.
`static <T extends [Relationship](kerml/Relationship.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[streamOfOwnedRelationship](#streamOfOwnedRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> clazz,
 boolean isInstance)`
Retrieve matching owned relationships.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Relationships
public Relationships()
 ============ METHOD DETAIL ========== 
Method Details
getFirstOwnedRelatedElement
@CheckForNullpublic static [Element](kerml/Element.html) getFirstOwnedRelatedElement([Relationship](kerml/Relationship.html) relationship)
Returns the first owned related element of the given relationship.
Parameters:
`relationship` - the relationship to inspect
Returns:
the first owned related element, or null if none exist
getFirstOwnedRelatedElement
@CheckForNullpublic static <T extends [Element](kerml/Element.html)> T getFirstOwnedRelatedElement([Relationship](kerml/Relationship.html) relationship,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> clazz)
Returns the first owned related element of the given relationship
 if it is an instance of the specified class.
Type Parameters:
`T` - element type
Parameters:
`relationship` - the relationship to inspect
`clazz` - the expected element type
Returns:
the first matching element, or null if none match
setSingleOwnedRelatedElement
public static void setSingleOwnedRelatedElement([Relationship](kerml/Relationship.html) relationship,
 @CheckForNull
 [Element](kerml/Element.html) ownedRelatedElement)
Sets the single owned related element of the relationship.
 Clears existing related elements before setting the new one.
Parameters:
`relationship` - the relationship to modify
`ownedRelatedElement` - the element to set, or null to clear
streamOfOwnedRelationship
public static <T extends [Relationship](kerml/Relationship.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> streamOfOwnedRelationship([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> clazz,
 boolean isInstance)
Retrieve matching owned relationships.
Parameters:
`element` - element
`clazz` - relationship instance class
`isInstance` - check "instanceOf" if true or strict equals if false
Returns:
owned relationships matching given clazz
streamOfOwnedNotImpliedRelationship
public static <T extends [Relationship](kerml/Relationship.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> streamOfOwnedNotImpliedRelationship([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> clazz,
 boolean isInstance)
Returns a stream of owned, non‑implied relationships of the given type.
Type Parameters:
`T` - relationship type
Parameters:
`element` - the element whose relationships are inspected
`clazz` - the relationship class
`isInstance` - whether to use instanceof or exact class match
Returns:
stream of non‑implied relationships
addOwnedNotImpliedRelationships
public static <R extends [Relationship](kerml/Relationship.html)> void addOwnedNotImpliedRelationships([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets)
Appends new non‑implied relationships of the given type for the provided targets.
Type Parameters:
`R` - relationship type
Parameters:
`element` - the element to modify
`clazz` - relationship class
`targets` - target elements
setOwnedNotImpliedRelationships
public static <R extends [Relationship](kerml/Relationship.html)> void setOwnedNotImpliedRelationships([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets)
Replaces existing non‑implied relationships with new ones referencing the given targets.
Type Parameters:
`R` - relationship type
Parameters:
`element` - the element to modify
`clazz` - relationship class
`targets` - target elements
editNotImpliedOwnedRelationships
public static <R extends [Relationship](kerml/Relationship.html)> void editNotImpliedOwnedRelationships([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets,
 boolean set)
Edits not implied owned relationships and their targets.
 If 'set' is true, then makes all not implied owned relationships to reference passed targets.
 Ensures that element has the same number of relationships of given class as there are targets.
 If there is a lack of relationships, they are created.
 Any excess relationships are disposed.
 If 'set' is false, passed targets are appended to the currently referenced.
 If some target is already referenced, it is skipped.
Type Parameters:
`R` - relationship class
Parameters:
`element` - whose owned relationships shall be edited?
`clazz` - relationship class
`targets` - targets
`set` - should set pass targets as referenced elements or append them to the currently referenced elements
editOwnedRelationships
public static <R extends [Relationship](kerml/Relationship.html)> void editOwnedRelationships([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<R> clazz,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Element](kerml/Element.html)> targets,
 boolean set,
 boolean notImplied)
Edits not implied owned relationships and their targets.
 If 'set' is true, then makes all not implied owned relationships to reference passed targets.
 Ensures that element has the same number of relationships of given class as there are targets.
 If there is a lack of relationships, they are created.
 Any excess relationships are disposed.
 If 'set' is false, passed targets are appended to the currently referenced.
 If some target is already referenced, it is skipped.
Type Parameters:
`R` - relationship class
Parameters:
`element` - whose owned relationships shall be edited?
`clazz` - relationship class
`targets` - targets
`set` - should set pass targets as referenced elements or append them to the currently referenced elements
`notImplied` - take into account only not implied relationships
getSource
@CheckForNullpublic static [Element](kerml/Element.html) getSource([Relationship](kerml/Relationship.html) relationship)
Returns the first source element of the relationship.
Parameters:
`relationship` - the relationship to inspect
Returns:
the source element, or null if none exist
getTarget
@CheckForNullpublic static [Element](kerml/Element.html) getTarget([Relationship](kerml/Relationship.html) relationship)
Returns the first target element of the relationship.
Parameters:
`relationship` - the relationship to inspect
Returns:
the target element, or null if none exist
getIncoming
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Relationship](kerml/Relationship.html)> getIncoming([Element](kerml/Element.html) element)
Returns all incoming relationships of the element.
Parameters:
`element` - the element to inspect
Returns:
collection of incoming relationships
getIncoming
public static <T extends [Relationship](kerml/Relationship.html)>
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> getIncoming([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> ofType)
Returns all incoming relationships of the given type.
Type Parameters:
`T` - relationship type
Parameters:
`element` - the element to inspect
`ofType` - relationship class
Returns:
collection of incoming relationships
getOutgoing
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Relationship](kerml/Relationship.html)> getOutgoing([Element](kerml/Element.html) element)
Returns all outgoing relationships of the element.
Parameters:
`element` - the element to inspect
Returns:
collection of outgoing relationships
setSource
public static boolean setSource([Relationship](kerml/Relationship.html) relationship,
 @CheckForNull
 [Element](kerml/Element.html) source)
Sets the source of the relationship.
Parameters:
`relationship` - the relationship to modify
`source` - the new source element
Returns:
true if the source was set successfully
setTarget
public static boolean setTarget([Relationship](kerml/Relationship.html) relationship,
 @CheckForNull
 [Element](kerml/Element.html) target)
Sets the target of the relationship.
Parameters:
`relationship` - the relationship to modify
`target` - the new target element
Returns:
true if the target was set successfully
isAssociationOrConnector
public static boolean isAssociationOrConnector(@CheckForNull
 [Element](kerml/Element.html) element)
Checks whether the element is an association or connector.
Parameters:
`element` - the element to check
Returns:
true if it is an association or connector
isAssociationOrConnector
public static boolean isAssociationOrConnector(org.eclipse.emf.ecore.EClass eClass)
Checks whether the EClass represents an association or connector.
Parameters:
`eClass` - the class to check
Returns:
true if it represents an association or connector
isNonMemberRelationship
public static boolean isNonMemberRelationship(@CheckForNull
 [Element](kerml/Element.html) element)
Checks whether the element is a non‑member relationship.
Parameters:
`element` - the element to check
Returns:
true if it is a non‑member relationship
isNonMemberRelationship
public static boolean isNonMemberRelationship(org.eclipse.emf.ecore.EClass eClass)
Checks whether the EClass represents a non‑member relationship.
Parameters:
`eClass` - the class to check
Returns:
true if it represents a non‑member relationship
isMemberRelationship
public static boolean isMemberRelationship(@CheckForNull
 [Element](kerml/Element.html) element)
Checks whether the element is a member relationship.
Parameters:
`element` - the element to check
Returns:
true if it is a member relationship
isMemberRelationship
public static boolean isMemberRelationship(org.eclipse.emf.ecore.EClass eClass)
Checks whether the EClass represents a member relationship.
Parameters:
`eClass` - the class to check
Returns:
true if it represents a member relationship
getOwningMembershipEClass
@CheckForNullpublic static org.eclipse.emf.ecore.EClass getOwningMembershipEClass(org.eclipse.emf.ecore.EClass childEClass,
 [Namespace](kerml/Namespace.html) owner)
Determines the appropriate owning membership EClass for a child element.
Parameters:
`childEClass` - the child element class
`owner` - the owning namespace
Returns:
the owning membership EClass, or null if none applies
getRelationshipSourceFeature
@CheckForNullpublic static <T extends [Relationship](kerml/Relationship.html)> [Feature](kerml/Feature.html) getRelationshipSourceFeature(T relationship,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<T,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> endFeatureProvider)
Returns the source feature of a relationship when exactly two features exist.
Type Parameters:
`T` - relationship type
Parameters:
`relationship` - the relationship to inspect
`endFeatureProvider` - provider returning the relationship ends
Returns:
the source feature, or null if not applicable
getRelationshipTargetFeature
public static <T extends [Relationship](kerml/Relationship.html)>
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getRelationshipTargetFeature(T relationship,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<T,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> endFeatureProvider)
Returns the target feature(s) of a relationship.
Type Parameters:
`T` - relationship type
Parameters:
`relationship` - the relationship to inspect
`endFeatureProvider` - provider returning the relationship ends
Returns:
list of target features
findOwnerFor
@CheckForNullpublic static [Element](kerml/Element.html) findOwnerFor([Relationship](kerml/Relationship.html) relationship,
 [Element](kerml/Element.html) source,
 [Element](kerml/Element.html) target,
 @CheckForNull
 [Element](kerml/Element.html) diagramOwner,
 boolean checkPermissions)
Looks for a possible owner for a given Relationship.
 Possible owner is calculated according to source/target and diagram owner.
 'Non-member' relationships are always owned in that source.
Parameters:
`relationship` - relation for which possible owner should be found
`source` - relationship's source element
`target` - relationship's target element
`diagramOwner` - diagram owner if any
`checkPermissions` - indicates if permissions should be checked
Returns:
possible owner
See Also:
[`isNonMemberRelationship(Element)`](#isNonMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Relationships">Class Relationships</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Relationships</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Relationships</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Relationship</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Relationships</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addOwnedNotImpliedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List)">addOwnedNotImpliedRelationships</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Appends new non‑implied relationships of the given type for the provided targets.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#editNotImpliedOwnedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List,boolean)">editNotImpliedOwnedRelationships</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets,
 boolean set)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Edits not implied owned relationships and their targets.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#editOwnedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List,boolean,boolean)">editOwnedRelationships</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets,
 boolean set,
 boolean notImplied)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Edits not implied owned relationships and their targets.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerFor(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element,boolean)">findOwnerFor</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> source,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> diagramOwner,
 boolean checkPermissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a possible owner for a given Relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">getFirstOwnedRelatedElement</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first owned related element of the given relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,java.lang.Class)">getFirstOwnedRelatedElement</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; clazz)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first owned related element of the given relationship
 if it is an instance of the specified class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncoming(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getIncoming</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all incoming relationships of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncoming(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class)">getIncoming</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ofType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all incoming relationships of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutgoing(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getOutgoing</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all outgoing relationships of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwningMembershipEClass(org.eclipse.emf.ecore.EClass,com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">getOwningMembershipEClass</a><wbr/>(org.eclipse.emf.ecore.EClass childEClass,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> owner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines the appropriate owning membership EClass for a child element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipSourceFeature(T,java.util.function.Function)">getRelationshipSourceFeature</a><wbr/>(T relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; endFeatureProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source feature of a relationship when exactly two features exist.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipTargetFeature(T,java.util.function.Function)">getRelationshipTargetFeature</a><wbr/>(T relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; endFeatureProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target feature(s) of a relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSource(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">getSource</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first source element of the relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">getTarget</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first target element of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssociationOrConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isAssociationOrConnector</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is an association or connector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssociationOrConnector(org.eclipse.emf.ecore.EClass)">isAssociationOrConnector</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the EClass represents an association or connector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isMemberRelationship</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a member relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMemberRelationship(org.eclipse.emf.ecore.EClass)">isMemberRelationship</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the EClass represents a member relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNonMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isNonMemberRelationship</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a non‑member relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNonMemberRelationship(org.eclipse.emf.ecore.EClass)">isNonMemberRelationship</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the EClass represents a non‑member relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwnedNotImpliedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List)">setOwnedNotImpliedRelationships</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces existing non‑implied relationships with new ones referencing the given targets.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSingleOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element)">setSingleOwnedRelatedElement</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> ownedRelatedElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the single owned related element of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSource(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element)">setSource</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the source of the relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element)">setTarget</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the target of the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfOwnedNotImpliedRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean)">streamOfOwnedNotImpliedRelationship</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; clazz,
 boolean isInstance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of owned, non‑implied relationships of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfOwnedRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean)">streamOfOwnedRelationship</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; clazz,
 boolean isInstance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieve matching owned relationships.</div>
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
<h3>Relationships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Relationships</span>()</div>
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
<section class="detail" id="getFirstOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">
<h3>getFirstOwnedRelatedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getFirstOwnedRelatedElement</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship)</span></div>
<div class="block">Returns the first owned related element of the given relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to inspect</dd>
<dt>Returns:</dt>
<dd>the first owned related element, or null if none exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,java.lang.Class)">
<h3>getFirstOwnedRelatedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">getFirstOwnedRelatedElement</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; clazz)</span></div>
<div class="block">Returns the first owned related element of the given relationship
 if it is an instance of the specified class.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to inspect</dd>
<dd><code>clazz</code> - the expected element type</dd>
<dt>Returns:</dt>
<dd>the first matching element, or null if none match</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSingleOwnedRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setSingleOwnedRelatedElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSingleOwnedRelatedElement</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> ownedRelatedElement)</span></div>
<div class="block">Sets the single owned related element of the relationship.
 Clears existing related elements before setting the new one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to modify</dd>
<dd><code>ownedRelatedElement</code> - the element to set, or null to clear</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfOwnedRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean)">
<h3>streamOfOwnedRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">streamOfOwnedRelationship</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; clazz,
 boolean isInstance)</span></div>
<div class="block">Retrieve matching owned relationships.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>clazz</code> - relationship instance class</dd>
<dd><code>isInstance</code> - check "instanceOf" if true or strict equals if false</dd>
<dt>Returns:</dt>
<dd>owned relationships matching given clazz</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfOwnedNotImpliedRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean)">
<h3>streamOfOwnedNotImpliedRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">streamOfOwnedNotImpliedRelationship</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; clazz,
 boolean isInstance)</span></div>
<div class="block">Returns a stream of owned, non‑implied relationships of the given type.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - relationship type</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the element whose relationships are inspected</dd>
<dd><code>clazz</code> - the relationship class</dd>
<dd><code>isInstance</code> - whether to use instanceof or exact class match</dd>
<dt>Returns:</dt>
<dd>stream of non‑implied relationships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addOwnedNotImpliedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List)">
<h3>addOwnedNotImpliedRelationships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">addOwnedNotImpliedRelationships</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets)</span></div>
<div class="block">Appends new non‑implied relationships of the given type for the provided targets.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>R</code> - relationship type</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the element to modify</dd>
<dd><code>clazz</code> - relationship class</dd>
<dd><code>targets</code> - target elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedNotImpliedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List)">
<h3>setOwnedNotImpliedRelationships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">setOwnedNotImpliedRelationships</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets)</span></div>
<div class="block">Replaces existing non‑implied relationships with new ones referencing the given targets.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>R</code> - relationship type</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the element to modify</dd>
<dd><code>clazz</code> - relationship class</dd>
<dd><code>targets</code> - target elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editNotImpliedOwnedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List,boolean)">
<h3>editNotImpliedOwnedRelationships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">editNotImpliedOwnedRelationships</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets,
 boolean set)</span></div>
<div class="block">Edits not implied owned relationships and their targets.
 If 'set' is true, then makes all not implied owned relationships to reference passed targets.
 Ensures that element has the same number of relationships of given class as there are targets.
 If there is a lack of relationships, they are created.
 Any excess relationships are disposed.
 If 'set' is false, passed targets are appended to the currently referenced.
 If some target is already referenced, it is skipped.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>R</code> - relationship class</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - whose owned relationships shall be edited?</dd>
<dd><code>clazz</code> - relationship class</dd>
<dd><code>targets</code> - targets</dd>
<dd><code>set</code> - should set pass targets as referenced elements or append them to the currently referenced elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editOwnedRelationships(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,java.util.List,boolean,boolean)">
<h3>editOwnedRelationships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">editOwnedRelationships</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;R&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; targets,
 boolean set,
 boolean notImplied)</span></div>
<div class="block">Edits not implied owned relationships and their targets.
 If 'set' is true, then makes all not implied owned relationships to reference passed targets.
 Ensures that element has the same number of relationships of given class as there are targets.
 If there is a lack of relationships, they are created.
 Any excess relationships are disposed.
 If 'set' is false, passed targets are appended to the currently referenced.
 If some target is already referenced, it is skipped.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>R</code> - relationship class</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - whose owned relationships shall be edited?</dd>
<dd><code>clazz</code> - relationship class</dd>
<dd><code>targets</code> - targets</dd>
<dd><code>set</code> - should set pass targets as referenced elements or append them to the currently referenced elements</dd>
<dd><code>notImplied</code> - take into account only not implied relationships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSource(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">
<h3>getSource</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getSource</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship)</span></div>
<div class="block">Returns the first source element of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to inspect</dd>
<dt>Returns:</dt>
<dd>the source element, or null if none exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">
<h3>getTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getTarget</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship)</span></div>
<div class="block">Returns the first target element of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to inspect</dd>
<dt>Returns:</dt>
<dd>the target element, or null if none exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncoming(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getIncoming</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="element-name">getIncoming</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns all incoming relationships of the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>collection of incoming relationships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncoming(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class)">
<h3>getIncoming</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span>
<span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">getIncoming</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; ofType)</span></div>
<div class="block">Returns all incoming relationships of the given type.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - relationship type</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dd><code>ofType</code> - relationship class</dd>
<dt>Returns:</dt>
<dd>collection of incoming relationships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutgoing(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getOutgoing</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="element-name">getOutgoing</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns all outgoing relationships of the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to inspect</dd>
<dt>Returns:</dt>
<dd>collection of outgoing relationships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSource(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setSource</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setSource</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> source)</span></div>
<div class="block">Sets the source of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to modify</dd>
<dd><code>source</code> - the new source element</dd>
<dt>Returns:</dt>
<dd>true if the source was set successfully</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setTarget</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setTarget</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target)</span></div>
<div class="block">Sets the target of the relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to modify</dd>
<dd><code>target</code> - the new target element</dd>
<dt>Returns:</dt>
<dd>true if the target was set successfully</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssociationOrConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isAssociationOrConnector</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAssociationOrConnector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is an association or connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if it is an association or connector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssociationOrConnector(org.eclipse.emf.ecore.EClass)">
<h3>isAssociationOrConnector</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAssociationOrConnector</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the EClass represents an association or connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if it represents an association or connector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNonMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isNonMemberRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNonMemberRelationship</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a non‑member relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if it is a non‑member relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNonMemberRelationship(org.eclipse.emf.ecore.EClass)">
<h3>isNonMemberRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNonMemberRelationship</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the EClass represents a non‑member relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if it represents a non‑member relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isMemberRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMemberRelationship</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a member relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if it is a member relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMemberRelationship(org.eclipse.emf.ecore.EClass)">
<h3>isMemberRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMemberRelationship</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the EClass represents a member relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if it represents a member relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningMembershipEClass(org.eclipse.emf.ecore.EClass,com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>getOwningMembershipEClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getOwningMembershipEClass</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass childEClass,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> owner)</span></div>
<div class="block">Determines the appropriate owning membership EClass for a child element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>childEClass</code> - the child element class</dd>
<dd><code>owner</code> - the owning namespace</dd>
<dt>Returns:</dt>
<dd>the owning membership EClass, or null if none applies</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationshipSourceFeature(T,java.util.function.Function)">
<h3 id="getRelationshipSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,java.util.function.Function)">getRelationshipSourceFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRelationshipSourceFeature</span><wbr/><span class="parameters">(T relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; endFeatureProvider)</span></div>
<div class="block">Returns the source feature of a relationship when exactly two features exist.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - relationship type</dd>
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to inspect</dd>
<dd><code>endFeatureProvider</code> - provider returning the relationship ends</dd>
<dt>Returns:</dt>
<dd>the source feature, or null if not applicable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationshipTargetFeature(T,java.util.function.Function)">
<h3 id="getRelationshipTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,java.util.function.Function)">getRelationshipTargetFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span>
<span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getRelationshipTargetFeature</span><wbr/><span class="parameters">(T relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; endFeatureProvider)</span></div>
<div class="block">Returns the target feature(s) of a relationship.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - relationship type</dd>
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship to inspect</dd>
<dd><code>endFeatureProvider</code> - provider returning the relationship ends</dd>
<dt>Returns:</dt>
<dd>list of target features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerFor(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element,boolean)">
<h3>findOwnerFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">findOwnerFor</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> relationship,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> source,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> target,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> diagramOwner,
 boolean checkPermissions)</span></div>
<div class="block">Looks for a possible owner for a given Relationship.
 Possible owner is calculated according to source/target and diagram owner.
 'Non-member' relationships are always owned in that source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relation for which possible owner should be found</dd>
<dd><code>source</code> - relationship's source element</dd>
<dd><code>target</code> - relationship's target element</dd>
<dd><code>diagramOwner</code> - diagram owner if any</dd>
<dd><code>checkPermissions</code> - indicates if permissions should be checked</dd>
<dt>Returns:</dt>
<dd>possible owner</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#isNonMemberRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)"><code>isNonMemberRelationship(Element)</code></a></li>
</ul>
</dd>
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
