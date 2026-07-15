# JAVA OPENAPI: Profiles (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml2/Profiles.html
- source_path: `com/nomagic/magicdraw/uml2/Profiles.html`
- source_sha256: `e695622e78249d8b8e6ea885271d4b941320e4f7db01a6227cd167123c5c4775`
- captured_utc: `2026-07-14T16:52:24.446045+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Profiles

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Profiles

public classProfiles
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience static methods to work with Stereotyped elements and tagged values. Common for Stereotypes from any Profile.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Profiles](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addValue](#addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Adds tagged values.
`static void`
`[addValue](#addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Adds tagged values.
`static void`
`[addValue](#addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean setOppositeEnd)`
Adds tagged values.
`static void`
`[applyStereotype](#applyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Extends given element with the stereotype.
`static void`
`[clearValue](#clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)`
Clears value of tagged value and disposes the tagged value
`static void`
`[clearValue](#clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 boolean disposeTaggedValue)`
Clears value of tagged value and disposes the tagged value
`static void`
`[clearValue](#clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,boolean))([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 boolean disposeTaggedValue)`
Clear value of given tagged value
`static void`
`[createDefaultValue](#createDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,boolean))([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 boolean createAll)`
Creates default values for given tagged value.
`static void`
`[createDefaultValues](#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean createAll)`
Creates tagged values with default values for tags of the given stereotype.
`static [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getAppliedIncludingDerived](#getAppliedIncludingDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if the given stereotype or it's subtype stereotype is already applied to the element, and returns the applied stereotype
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[getAppliedStereotypes](#getAppliedStereotypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Returns a set of all applied stereotypes for any of the elements in the collection
`static [ExtensionEnd](../../uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html)`
`[getExtensionEnd](#getExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))([Extension](../../uml2/ext/magicdraw/mdprofiles/Extension.html) extension)`
ExtensionEnd of given Extension
`static [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFirstApplied](#getFirstApplied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Checks if there is at least one stereotype is already applied to the element, and returns the first found stereotype.
`static [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFirstAppliedIncludingDerived](#getFirstAppliedIncludingDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Checks if there is at least one stereotype or stereotype derived from it already applied to the element, and returns the first found stereotype
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getFirstValue](#getFirstValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)`

`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getStereotypedElements](#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all elements stereotyped by stereotype
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getStereotypedElementsIncludingDerived](#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.
`static [TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html)`
`[getTaggedValue](#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)`
Return tagged value for given tag definition.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?>`
`[getValue](#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)`
Gets the value of the stereotype property (a.k.a tag) as list.
`static boolean`
`[isStereotypeApplied](#isStereotypeApplied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if element has the given stereotype applied
`static void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets tagged values.
`static void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets tagged values.
`static void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean setOppositeEnd)`
Sets tagged values.
`static void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object))([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets tagged values.
`static void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean))([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean setOppositeEnd)`
Sets tagged values.
`static void`
`[unapplyStereotype](#unapplyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Remove stereotype from element, if it is applied.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Profiles
public Profiles()
 ============ METHOD DETAIL ========== 
Method Details
getStereotypedElements
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getStereotypedElements(@CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all elements stereotyped by stereotype
Parameters:
`stereotype` - stereotype
Returns:
list of elements stereotyped by stereotype
getStereotypedElementsIncludingDerived
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getStereotypedElementsIncludingDerived([Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.
Parameters:
`stereotype` - stereotype
Returns:
collection of elements stereotyped by stereotype or derived ones
getAppliedIncludingDerived
@CheckForNullpublic static [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getAppliedIncludingDerived([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Checks if the given stereotype or it's subtype stereotype is already applied to the element, and returns the applied stereotype
Parameters:
`element` - element
`stereotype` - stereotype to check for
Returns:
given stereotype or stereotype derived from it, if applied to the element
getAppliedStereotypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> getAppliedStereotypes([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Returns a set of all applied stereotypes for any of the elements in the collection
Parameters:
`elements` - collection of elements
Returns:
collection stereotypes, each is applied on one or more of the provided elements
getFirstApplied
@CheckForNullpublic static [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getFirstApplied([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Checks if there is at least one stereotype is already applied to the element, and returns the first found stereotype.
Parameters:
`element` - element
`stereotypes` - a collection of stereotypes to check
Returns:
one of the provided stereotypes if applied to this element
getFirstAppliedIncludingDerived
@CheckForNullpublic static [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getFirstAppliedIncludingDerived([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Checks if there is at least one stereotype or stereotype derived from it already applied to the element, and returns the first found stereotype
Parameters:
`element` - element
`stereotypes` - a collection of stereotypes to check
Returns:
one of the provided stereotypes, or stereotype derived from it, if applied to this element
isStereotypeApplied
public static boolean isStereotypeApplied([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Checks if element has the given stereotype applied
Parameters:
`element` - element to check
`stereotype` - stereotype name to check
Returns:
true if element has applied stereotype with given name
applyStereotype
public static void applyStereotype([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Extends given element with the stereotype. The default tag values are not created.
 The default tag values are not created, to create these values use
 [`createDefaultValues(Element, Stereotype, boolean)`](#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))
Parameters:
`element` - element
`stereotype` - stereotype to add
unapplyStereotype
public static void unapplyStereotype([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Remove stereotype from element, if it is applied. Removes also tagged values of removed stereotype
Parameters:
`element` - element
`stereotype` - stereotype to remove
createDefaultValues
public static void createDefaultValues([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean createAll)
Creates tagged values with default values for tags of the given stereotype.
 The stereotype must be already applied to the element.
Parameters:
`element` - element that has the stereotype applied
`stereotype` - stereotype applied to the element
`createAll` - provide true to creates tagged values for all tags with default value (do not check multiplicity).
 false, to only create tagged values for tags with mandatory value, i.e. with lower multiplicity >= 1.
createDefaultValue
public static void createDefaultValue([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 boolean createAll)
Creates default values for given tagged value.
Parameters:
`taggedValue` - tagged value
`createAll` - provide true to creates default value (do not check multiplicity).
 false, to only create tagged values for tags with mandatory value, i.e. with lower multiplicity >= 1.
getValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> getValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)
Gets the value of the stereotype property (a.k.a tag) as list.
Parameters:
`element` - element with applied stereotype
`tag` - property owned by the applied stereotype
Returns:
tagged values values (a modifiable copy of original values lists)
getFirstValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getFirstValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)
getTaggedValue
@CheckForNullpublic static [TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) getTaggedValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)
Return tagged value for given tag definition.
Parameters:
`element` - element
`tag` - tag definition
Returns:
tagged value
setValue
public static void setValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets tagged values. Existing values will be replaced.
Parameters:
`element` - element with applied stereotype
`tag` - property owned by the stereotype
`value` - value to set, null is ignored
setValue
public static void setValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets tagged values. Existing values will be replaced.
Parameters:
`element` - element with applied stereotype
`stereotype` - the applied stereotype
`tag` - tag definition
`value` - value to set, null is ignored
setValue
public static void setValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean setOppositeEnd)
Sets tagged values. Existing values will be replaced.
Parameters:
`element` - element with applied stereotype
`stereotype` - the applied stereotype
`tag` - tag definition
`value` - value to set, null is ignored
`setOppositeEnd` - provide true to update the value of the tag which is the opposite end of the tag's association
addValue
public static void addValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Adds tagged values.
Parameters:
`element` - element with applied stereotype
`tag` - property owned by the stereotype
`value` - value to add, null is ignored
addValue
public static void addValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Adds tagged values.
Parameters:
`element` - element with applied stereotype
`stereotype` - the applied stereotype
`tag` - tag definition
`value` - value to add, null is ignored
addValue
public static void addValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean setOppositeEnd)
Adds tagged values.
Parameters:
`element` - element with applied stereotype
`stereotype` - the applied stereotype
`tag` - tag definition
`value` - value to add, null is ignored
`setOppositeEnd` - provide true to update the value of the tag which is the opposite end of the tag's association
getExtensionEnd
@CheckForNullpublic static [ExtensionEnd](../../uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html) getExtensionEnd([Extension](../../uml2/ext/magicdraw/mdprofiles/Extension.html) extension)
ExtensionEnd of given Extension
Parameters:
`extension` - Extension
Returns:
ExtensionEnd of Extension
setValue
public static void setValue([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean setOppositeEnd)
Sets tagged values. Existing values will be replaced.
Parameters:
`taggedValue` - tagged value
`value` - value to set
`setOppositeEnd` - provide true to update the value of the tag which is the opposite end of the tag's association
setValue
public static void setValue([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets tagged values. Existing values will be replaced.
Parameters:
`taggedValue` - tagged value
`value` - value to set
clearValue
public static void clearValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag,
 boolean disposeTaggedValue)
Clears value of tagged value and disposes the tagged value
Parameters:
`element` - stereotyped element
`tag` - tag definition
`disposeTaggedValue` - dispose tagged value, not just clear values¬
clearValue
public static void clearValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) tag)
Clears value of tagged value and disposes the tagged value
Parameters:
`element` - stereotyped element
`tag` - tag definition
clearValue
public static void clearValue([TaggedValue](../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 boolean disposeTaggedValue)
Clear value of given tagged value
Parameters:
`taggedValue` - tagged value
`disposeTaggedValue` - dispose tagged value, not just clear values¬

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Profiles">Class Profiles</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Profiles</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Profiles</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience static methods to work with Stereotyped elements and tagged values. Common for Stereotypes from any Profile.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Profiles</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">addValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">addValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">addValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean setOppositeEnd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">applyStereotype</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extends given element with the stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">clearValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clears value of tagged value and disposes the tagged value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">clearValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 boolean disposeTaggedValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clears value of tagged value and disposes the tagged value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,boolean)">clearValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 boolean disposeTaggedValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clear value of given tagged value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,boolean)">createDefaultValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 boolean createAll)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates default values for given tagged value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">createDefaultValues</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean createAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates tagged values with default values for tags of the given stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAppliedIncludingDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getAppliedIncludingDerived</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if the given stereotype or it's subtype stereotype is already applied to the element, and returns the applied stereotype</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAppliedStereotypes(java.util.Collection)">getAppliedStereotypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a set of all applied stereotypes for any of the elements in the collection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">getExtensionEnd</a><wbr/>(<a href="../../uml2/ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">ExtensionEnd of given Extension</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstApplied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">getFirstApplied</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if there is at least one stereotype is already applied to the element, and returns the first found stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstAppliedIncludingDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">getFirstAppliedIncludingDerived</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if there is at least one stereotype or stereotype derived from it already applied to the element, and returns the first found stereotype</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getFirstValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getStereotypedElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements stereotyped by stereotype</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getStereotypedElementsIncludingDerived</a><wbr/>(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getTaggedValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return tagged value for given tag definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the value of the stereotype property (a.k.a tag) as list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStereotypeApplied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isStereotypeApplied</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element has the given stereotype applied</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">setValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">setValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">setValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean setOppositeEnd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object)">setValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean)">setValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean setOppositeEnd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unapplyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">unapplyStereotype</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove stereotype from element, if it is applied.</div>
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
<h3>Profiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Profiles</span>()</div>
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
<section class="detail" id="getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getStereotypedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getStereotypedElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns all elements stereotyped by stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>list of elements stereotyped by stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getStereotypedElementsIncludingDerived</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getStereotypedElementsIncludingDerived</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>collection of elements stereotyped by stereotype or derived ones</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedIncludingDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getAppliedIncludingDerived</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getAppliedIncludingDerived</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Checks if the given stereotype or it's subtype stereotype is already applied to the element, and returns the applied stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype to check for</dd>
<dt>Returns:</dt>
<dd>given stereotype or stereotype derived from it, if applied to the element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedStereotypes(java.util.Collection)">
<h3>getAppliedStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAppliedStereotypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Returns a set of all applied stereotypes for any of the elements in the collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of elements</dd>
<dt>Returns:</dt>
<dd>collection stereotypes, each is applied on one or more of the provided elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstApplied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>getFirstApplied</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFirstApplied</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Checks if there is at least one stereotype is already applied to the element, and returns the first found stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypes</code> - a collection of stereotypes to check</dd>
<dt>Returns:</dt>
<dd>one of the provided stereotypes if applied to this element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstAppliedIncludingDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>getFirstAppliedIncludingDerived</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFirstAppliedIncludingDerived</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Checks if there is at least one stereotype or stereotype derived from it already applied to the element, and returns the first found stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypes</code> - a collection of stereotypes to check</dd>
<dt>Returns:</dt>
<dd>one of the provided stereotypes, or stereotype derived from it, if applied to this element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStereotypeApplied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>isStereotypeApplied</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStereotypeApplied</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Checks if element has the given stereotype applied</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dd><code>stereotype</code> - stereotype name to check</dd>
<dt>Returns:</dt>
<dd>true if element has applied stereotype with given name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>applyStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">applyStereotype</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Extends given element with the stereotype. The default tag values are not created.
 The default tag values are not created, to create these values use
 <a href="#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)"><code>createDefaultValues(Element, Stereotype, boolean)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unapplyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>unapplyStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unapplyStereotype</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Remove stereotype from element, if it is applied. Removes also tagged values of removed stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">
<h3>createDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createDefaultValues</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean createAll)</span></div>
<div class="block">Creates tagged values with default values for tags of the given stereotype.
 The stereotype must be already applied to the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element that has the stereotype applied</dd>
<dd><code>stereotype</code> - stereotype applied to the element</dd>
<dd><code>createAll</code> - provide true to creates tagged values for all tags with default value (do not check multiplicity).
                   false, to only create tagged values for tags with mandatory value, i.e. with lower multiplicity &gt;= 1.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,boolean)">
<h3>createDefaultValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createDefaultValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 boolean createAll)</span></div>
<div class="block">Creates default values for given tagged value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - tagged value</dd>
<dd><code>createAll</code> - provide true to creates default value (do not check multiplicity).
                    false, to only create tagged values for tags with mandatory value, i.e. with lower multiplicity &gt;= 1.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt;</span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</span></div>
<div class="block">Gets the value of the stereotype property (a.k.a tag) as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>tag</code> - property owned by the applied stereotype</dd>
<dt>Returns:</dt>
<dd>tagged values values (a modifiable copy of original values lists)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getFirstValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getFirstValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getTaggedValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></span> <span class="element-name">getTaggedValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</span></div>
<div class="block">Return tagged value for given tag definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>tag</code> - tag definition</dd>
<dt>Returns:</dt>
<dd>tagged value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>tag</code> - property owned by the stereotype</dd>
<dd><code>value</code> - value to set, null is ignored</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - the applied stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value to set, null is ignored</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean setOppositeEnd)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - the applied stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value to set, null is ignored</dd>
<dd><code>setOppositeEnd</code> - provide true to update the value of the tag which is the opposite end of the tag's association</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">
<h3>addValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Adds tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>tag</code> - property owned by the stereotype</dd>
<dd><code>value</code> - value to add, null is ignored</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">
<h3>addValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Adds tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - the applied stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value to add, null is ignored</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">
<h3>addValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean setOppositeEnd)</span></div>
<div class="block">Adds tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - the applied stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value to add, null is ignored</dd>
<dd><code>setOppositeEnd</code> - provide true to update the value of the tag which is the opposite end of the tag's association</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">
<h3>getExtensionEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></span> <span class="element-name">getExtensionEnd</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</span></div>
<div class="block">ExtensionEnd of given Extension</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extension</code> - Extension</dd>
<dt>Returns:</dt>
<dd>ExtensionEnd of Extension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean setOppositeEnd)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - tagged value</dd>
<dd><code>value</code> - value to set</dd>
<dd><code>setOppositeEnd</code> - provide true to update the value of the tag which is the opposite end of the tag's association</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - tagged value</dd>
<dd><code>value</code> - value to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>clearValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 boolean disposeTaggedValue)</span></div>
<div class="block">Clears value of tagged value and disposes the tagged value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - stereotyped element</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>disposeTaggedValue</code> - dispose tagged value, not just clear values¬</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>clearValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</span></div>
<div class="block">Clears value of tagged value and disposes the tagged value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - stereotyped element</dd>
<dd><code>tag</code> - tag definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,boolean)">
<h3>clearValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 boolean disposeTaggedValue)</span></div>
<div class="block">Clear value of given tagged value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - tagged value</dd>
<dd><code>disposeTaggedValue</code> - dispose tagged value, not just clear values¬</dd>
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
