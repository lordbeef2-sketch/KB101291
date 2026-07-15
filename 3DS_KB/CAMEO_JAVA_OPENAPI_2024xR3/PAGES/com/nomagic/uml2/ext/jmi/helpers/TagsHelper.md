# JAVA OPENAPI: TagsHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/TagsHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/TagsHelper.html`
- source_sha256: `b7f25d8abd844d637fbe4e00b60383b9e5eb3edf24a5d55e61ad3ae6db384c11`
- captured_utc: `2026-07-14T16:56:16.648694+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class TagsHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper](DeprecatedTagsHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)
com.nomagic.uml2.ext.jmi.helpers.TagsHelper

Direct Known Subclasses:
`[StereotypesHelper](StereotypesHelper.html)`

@OpenApiAllpublic classTagsHelper
extends [DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)

Utility class to work with tagged values.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)
`[INVISIBLE_STEREOTYPE_NAME](DeprecatedStereotypesHelper.html#INVISIBLE_STEREOTYPE_NAME), [METAMODEL](DeprecatedStereotypesHelper.html#METAMODEL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TagsHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[addTaggedValueValue](#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean))([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean append)`
Add value to the given TaggedValue.
`static boolean`
`[addTaggedValueValue](#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean,boolean))([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean append,
 boolean setAnotherEnd)`
Add value to the given TaggedValue.
`static void`
`[clearStereotypeProperty](#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag)`
Clears tagged values.
`static void`
`[clearStereotypeProperty](#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 boolean disposeTaggedValue)`
Clears tagged values and removes TaggedValue if needed.
`static void`
`[clearStereotypeProperty](#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Clears tagged values.
`static void`
`[clearStereotypeProperty](#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean disposeTaggedValue)`
Clears tagged values and removes TaggedValue if needed.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)>`
`[collectVisibleTaggedValues](#collectVisibleTaggedValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns visible tagged values applied to the element.
`static void`
`[createDefaultValues](#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean createAll)`
Creates tagged values with default values for given element from given Stereotype.
`static void`
`[createDefaultValues](#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 boolean createAll)`
Creates tagged values with default values for given element from given Stereotypes.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[getPropertiesWithDerived](#getPropertiesWithDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns properties of stereotype including derived ones.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[getPropertiesWithDerivedOrdered](#getPropertiesWithDerivedOrdered(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns properties of stereotype including derived ones, first will be own element properties then parent and so on.
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[getPropertyByName](#getPropertyByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Returns property of stereotype by name
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypePropertyFirst](#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag)`
Returns first value of TaggedValue.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypePropertyFirst](#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 boolean calculateDerived)`
Returns first value of TaggedValue.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypePropertyFirst](#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Returns first value of TaggedValue.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getStereotypePropertyFirst](#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)`
Returns first value of TaggedValue.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStereotypePropertyStringValue](#getStereotypePropertyStringValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Converts given stereotype property value to a string.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition)`
Gets tagged values as list.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition,
 boolean calculateDerived)`
Gets tagged values as list.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Gets tagged values as list.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)`
Gets tagged values as list.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getStereotypePropertyValueAsString](#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Gets tagged values as list of strings.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getStereotypePropertyValueAsString](#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)`
Gets tagged values as list of strings
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getTagDefinitionOwner](#getTagDefinitionOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue))([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue)`
Returns stereotype owning tag definition of given tagged value.
`static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)`
`[getTaggedValue](#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition)`
Returns tagged value for given tag definition.
`static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)`
`[getTaggedValue](#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Returns tagged value for stereotype tag
`static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)`
`[getTaggedValue](#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)`
Looks for tagged value with given tag name in the given element.
`static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)`
`[getTaggedValueOrCreate](#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition,
 boolean createDefaultValue)`
Returns tagged value for stereotype tag.
`static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)`
`[getTaggedValueOrCreate](#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean createDefaultValue)`
Returns tagged value for stereotype tag
`static boolean`
`[hasStereotypePropertyValues](#hasStereotypePropertyValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Checks if given element has some tagged values.
`static boolean`
`[isValidTagType](#isValidTagType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../../magicdraw/classes/mdkernel/Type.html) type)`
Check if given type is valid for a tag of a Stereotype.
`static void`
`[removeTaggedValueValue](#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Removes a value from the tagged value.
`static void`
`[removeTaggedValueValue](#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object))([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Removes value from given TaggedValue.
`static void`
`[setStereotypePropertyValue](#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets tagged values.
`static void`
`[setStereotypePropertyValue](#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues)`
Sets tagged values.
`static void`
`[setStereotypePropertyValue](#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues,
 boolean setAnotherEnd)`
Sets tagged values.
`static void`
`[setStereotypePropertyValue](#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets tagged values.
`static void`
`[setStereotypePropertyValue](#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues)`
Sets tagged values.
`static void`
`[setStereotypePropertyValue](#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues,
 boolean setAnotherEnd)`
Sets tagged values.
`static <T> void`
`[setStereotypePropertyValueWithClearPredicate](#setStereotypePropertyValueWithClearPredicate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,T,boolean,java.util.function.Predicate))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 T value,
 boolean appendValues,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<T> clearValuesPredicate)`
Sets tagged values.
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)
`[addStereotypeByString](DeprecatedStereotypesHelper.html#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [addStereotypeByString](DeprecatedStereotypesHelper.html#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [addStereotypesWithNames](DeprecatedStereotypesHelper.html#addStereotypesWithNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)), [getExtendedElements](DeprecatedStereotypesHelper.html#getExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [getExtendedElementsIncludingDerived](DeprecatedStereotypesHelper.html#getExtendedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [getStereotype](DeprecatedStereotypesHelper.html#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String)), [getStereotype](DeprecatedStereotypesHelper.html#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)), [getStereotypePropertyValue](DeprecatedStereotypesHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [getStereotypePropertyValue](DeprecatedStereotypesHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [hasExtendedElements](DeprecatedStereotypesHelper.html#hasExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [hasStereotype](DeprecatedStereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [hasStereotype](DeprecatedStereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [hasStereotypeOrDerived](DeprecatedStereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [isElementStereotypedBy](DeprecatedStereotypesHelper.html#isElementStereotypedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [removeStereotypeByString](DeprecatedStereotypesHelper.html#removeStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedTagsHelper](DeprecatedTagsHelper.html)
`[clearStereotypeProperty](DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [clearStereotypeProperty](DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyFirst](DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyFirst](DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyValue](DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyValue](DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyValueAsString](DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyValueAsString](DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TagsHelper
public TagsHelper()
 ============ METHOD DETAIL ========== 
Method Details
getStereotypePropertyStringValue
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStereotypePropertyStringValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Converts given stereotype property value to a string.
Parameters:
`o` - value object
Returns:
string representation of given value object
getTagDefinitionOwner
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getTagDefinitionOwner([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue)
Returns stereotype owning tag definition of given tagged value.
Parameters:
`taggedValue` - the given TaggedValue
Returns:
stereotype owning tag definition of given tagged value
removeTaggedValueValue
public static void removeTaggedValueValue(@CheckForNull
 [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Removes value from given TaggedValue.
Parameters:
`taggedValue` - the given TaggedValue
`value` - value to remove
addTaggedValueValue
public static boolean addTaggedValueValue([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean append)
Add value to the given TaggedValue.
Parameters:
`taggedValue` - the given TaggedValue
`value` - value to add
`append` - True - Don't remove the append value
Returns:
true if succeeded
addTaggedValueValue
public static boolean addTaggedValueValue([TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) taggedValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean append,
 boolean setAnotherEnd)
Add value to the given TaggedValue.
Parameters:
`taggedValue` - the given TaggedValue
`value` - value
`append` - True - Don't remove the append value
`setAnotherEnd` - set another meta association end value
Returns:
true if succeeded
removeTaggedValueValue
public static void removeTaggedValueValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Removes a value from the tagged value.
Parameters:
`element` - element which has the tagged value
`stereotype` - stereotype which defines the tag
`tagName` - tag name
`value` - value to remove
getPropertyByName
@CheckForNullpublic static [Property](../../magicdraw/classes/mdkernel/Property.html) getPropertyByName(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Returns property of stereotype by name
Parameters:
`stereotype` - stereotype to get property from
`tagName` - name of tag definition
Returns:
property
getTaggedValue
@CheckForNullpublic static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) getTaggedValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Returns tagged value for stereotype tag
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
Returns:
TaggedValue of the tag
getTaggedValueOrCreate
@CheckForNullpublic static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) getTaggedValueOrCreate([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean createDefaultValue)
Returns tagged value for stereotype tag
Parameters:
`element` - element with assigned stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
`createDefaultValue` - create default values for a tagged value
Returns:
TaggedValue of the tag
getTaggedValueOrCreate
@CheckForNullpublic static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) getTaggedValueOrCreate([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition,
 boolean createDefaultValue)
Returns tagged value for stereotype tag.
Parameters:
`element` - element with assigned stereotype
`stereotype` - stereotype
`tagDefinition` - tag definition
`createDefaultValue` - create default values for a tagged value
Returns:
TaggedValue of the tag
getTaggedValue
@CheckForNullpublic static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) getTaggedValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition)
Returns tagged value for given tag definition.
Parameters:
`element` - element with applied tagged values
`tagDefinition` - tag definition
Returns:
TaggedValue of the tag
createDefaultValues
public static void createDefaultValues([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 boolean createAll)
Creates tagged values with default values for given element from given Stereotypes.
Parameters:
`element` - in this element tagged values will be created
`stereotypes` - tags providers
`createAll` - creates tagged values for all tags (do not check multiplicity). If false, tagged values will be created for tags which have multiplicity lower >=1.
createDefaultValues
public static void createDefaultValues([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean createAll)
Creates tagged values with default values for given element from given Stereotype.
Parameters:
`element` - in this element tagged values will be created
`stereotype` - tags provider
`createAll` - creates tagged values for all tags (do not check multiplicity). If false, tagged values will be created for tags which have multiplicity lower >=1.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null or second argument is not Stereotype
getStereotypePropertyValueAsString
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getStereotypePropertyValueAsString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Gets tagged values as list of strings.
Parameters:
`element` - element with assigned stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
Returns:
values
getStereotypePropertyValueAsString
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getStereotypePropertyValueAsString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)
Gets tagged values as list of strings
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
`calculateDerived` - if to calculate derived property value
Returns:
values
getStereotypePropertyValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
Returns:
values
getStereotypePropertyValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition)
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`tagDefinition` - tag definition
Returns:
values
getStereotypePropertyValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition,
 boolean calculateDerived)
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`tagDefinition` - property
`calculateDerived` - if to calculate derived property value
Returns:
values
getStereotypePropertyValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
`calculateDerived` - if to calculate derived property value
Returns:
values
setStereotypePropertyValue
public static void setStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues)
Sets tagged values.
Parameters:
`element` - element with applied stereotype
`stereotype` - name of stereotype
`tagName` - name of tag definition
`value` - value
`appendValues` - append or replace existing values
setStereotypePropertyValueWithClearPredicate
public static <T> void setStereotypePropertyValueWithClearPredicate([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 @CheckForNull
 T value,
 boolean appendValues,
 @CheckForNull
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<T> clearValuesPredicate)
Sets tagged values. If clear predicate is found and true, clears tagged values and removes TaggedValue, otherwise continues on setting tagged value.
Parameters:
`element` - element with applied stereotype
`stereotype` - name of stereotype
`tagName` - name of tag definition
`value` - value
`appendValues` - append or replace existing values
`clearValuesPredicate` - clear values predicate to check if value needs to be removed
setStereotypePropertyValue
public static void setStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets tagged values. Existing values will be replaced.
Parameters:
`element` - element with applied stereotype
`stereotype` - name of stereotype
`tagName` - name of tag definition
`value` - value
setStereotypePropertyValue
public static void setStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues,
 boolean setAnotherEnd)
Sets tagged values.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagName` - name of tag definition
`value` - value
`appendValues` - true to leave current value intact and add new one, false to replace current value with new one.
`setAnotherEnd` - calculate and change value of another meta association end
setStereotypePropertyValue
public static void setStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues)
Sets tagged values.
Parameters:
`element` - element with applied stereotype
`stereotype` - name of stereotype
`tag` - tag definition
`value` - value
`appendValues` - append or replace existing values
setStereotypePropertyValue
public static void setStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets tagged values. Existing values will be replaced.
Parameters:
`element` - element with applied stereotype
`stereotype` - name of stereotype
`tag` - tag definition
`value` - value
setStereotypePropertyValue
public static void setStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean appendValues,
 boolean setAnotherEnd)
Sets tagged values.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tag` - tag definition
`value` - value
`appendValues` - true to leave current value intact and add new one, false to replace current value with new one.
`setAnotherEnd` - calculate and change value of another meta association end
getTaggedValue
@CheckForNullpublic static [TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html) getTaggedValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Looks for tagged value with given tag name in the given element.
Parameters:
`element` - element
`tagName` - tag name
Returns:
tagged value with given tag name in the given element or null
isValidTagType
public static boolean isValidTagType([Type](../../magicdraw/classes/mdkernel/Type.html) type)
Check if given type is valid for a tag of a Stereotype. Tag can be typed just by Stereotype, Data Type or metaclass.
Parameters:
`type` - type
Returns:
true if valid
collectVisibleTaggedValues
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[TaggedValue](../../magicdraw/classes/mdkernel/TaggedValue.html)> collectVisibleTaggedValues(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns visible tagged values applied to the element.
Parameters:
`element` - element
Returns:
list of visible tagged values
hasStereotypePropertyValues
public static boolean hasStereotypePropertyValues(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)
Checks if given element has some tagged values.
Parameters:
`element` - given element
Returns:
true if some tagged value is created for a given element
clearStereotypeProperty
public static void clearStereotypeProperty([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Clears tagged values.
Parameters:
`element` - element
`stereotype` - stereotype
`tagName` - name of tag definition
clearStereotypeProperty
public static void clearStereotypeProperty([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean disposeTaggedValue)
Clears tagged values and removes TaggedValue if needed.
Parameters:
`element` - element
`stereotype` - stereotype of property
`tagName` - name of tag definition
`disposeTaggedValue` - disposes TaggedValue
clearStereotypeProperty
public static void clearStereotypeProperty([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag)
Clears tagged values.
Parameters:
`element` - element
`tag` - tag definition
clearStereotypeProperty
public static void clearStereotypeProperty([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 boolean disposeTaggedValue)
Clears tagged values and removes TaggedValue if needed.
Parameters:
`element` - element
`tag` - tag definition
`disposeTaggedValue` - disposes TaggedValue
getStereotypePropertyFirst
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypePropertyFirst([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName)
Returns first value of TaggedValue.
Parameters:
`element` - element
`stereotype` - stereotype
`tagName` - name of tag definition
Returns:
first value of TaggedValue
getStereotypePropertyFirst
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypePropertyFirst([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 boolean calculateDerived)
Returns first value of TaggedValue.
Parameters:
`element` - element
`stereotype` - stereotype
`tagName` - name of tag definition
`calculateDerived` - if to calculate derived value
Returns:
first value of TaggedValue
getStereotypePropertyFirst
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypePropertyFirst([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag)
Returns first value of TaggedValue.
Parameters:
`element` - element
`tag` - tag definition
Returns:
first value of TaggedValue
getStereotypePropertyFirst
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getStereotypePropertyFirst([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) tag,
 boolean calculateDerived)
Returns first value of TaggedValue.
Parameters:
`element` - element
`tag` - tag definition
`calculateDerived` - if to calculate derived value
Returns:
first value of TaggedValue
getPropertiesWithDerived
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> getPropertiesWithDerived([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns properties of stereotype including derived ones. Use this only if you do not care about order of collected properties.
Parameters:
`stereotype` - stereotype
Returns:
set of properties
getPropertiesWithDerivedOrdered
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> getPropertiesWithDerivedOrdered([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns properties of stereotype including derived ones, first will be own element properties then parent and so on.
Parameters:
`stereotype` - stereotype
Returns:
list of properties

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class TagsHelper">Class TagsHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="DeprecatedTagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper</a>
<div class="inheritance"><a href="DeprecatedStereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.TagsHelper</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="StereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypesHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TagsHelper</span>
<span class="extends-implements">extends <a href="DeprecatedStereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">DeprecatedStereotypesHelper</a></span></div>
<div class="block">Utility class to work with tagged values.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper">Fields inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="DeprecatedStereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">DeprecatedStereotypesHelper</a></h3>
<code><a href="DeprecatedStereotypesHelper.html#INVISIBLE_STEREOTYPE_NAME">INVISIBLE_STEREOTYPE_NAME</a>, <a href="DeprecatedStereotypesHelper.html#METAMODEL">METAMODEL</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TagsHelper</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean)">addTaggedValueValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean append)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add value to the given TaggedValue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean,boolean)">addTaggedValueValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean append,
 boolean setAnotherEnd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add value to the given TaggedValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">clearStereotypeProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clears tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">clearStereotypeProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 boolean disposeTaggedValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clears tagged values and removes TaggedValue if needed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">clearStereotypeProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clears tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">clearStereotypeProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean disposeTaggedValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clears tagged values and removes TaggedValue if needed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectVisibleTaggedValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectVisibleTaggedValues</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns visible tagged values applied to the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">createDefaultValues</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean createAll)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates tagged values with default values for given element from given Stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">createDefaultValues</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 boolean createAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates tagged values with default values for given element from given Stereotypes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertiesWithDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getPropertiesWithDerived</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns properties of stereotype including derived ones.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertiesWithDerivedOrdered(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getPropertiesWithDerivedOrdered</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns properties of stereotype including derived ones, first will be own element properties then parent and so on.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getPropertyByName</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns property of stereotype by name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getStereotypePropertyFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first value of TaggedValue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getStereotypePropertyFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 boolean calculateDerived)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first value of TaggedValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first value of TaggedValue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypePropertyFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first value of TaggedValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyStringValue(java.lang.Object)">getStereotypePropertyStringValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts given stereotype property value to a string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets tagged values as list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition,
 boolean calculateDerived)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets tagged values as list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets tagged values as list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets tagged values as list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyValueAsString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets tagged values as list of strings.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypePropertyValueAsString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets tagged values as list of strings</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTagDefinitionOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue)">getTagDefinitionOwner</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns stereotype owning tag definition of given tagged value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getTaggedValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns tagged value for given tag definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getTaggedValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns tagged value for stereotype tag</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getTaggedValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for tagged value with given tag name in the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getTaggedValueOrCreate</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition,
 boolean createDefaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns tagged value for stereotype tag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getTaggedValueOrCreate</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean createDefaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns tagged value for stereotype tag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotypePropertyValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasStereotypePropertyValues</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given element has some tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isValidTagType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">isValidTagType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given type is valid for a tag of a Stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)">removeTaggedValueValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes a value from the tagged value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object)">removeTaggedValueValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes value from given TaggedValue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">setStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">setStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean,boolean)">setStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues,
 boolean setAnotherEnd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)">setStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean)">setStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean,boolean)">setStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues,
 boolean setAnotherEnd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStereotypePropertyValueWithClearPredicate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,T,boolean,java.util.function.Predicate)">setStereotypePropertyValueWithClearPredicate</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 T value,
 boolean appendValues,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; clearValuesPredicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets tagged values.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="DeprecatedStereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">DeprecatedStereotypesHelper</a></h3>
<code><a href="DeprecatedStereotypesHelper.html#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addStereotypeByString</a>, <a href="DeprecatedStereotypesHelper.html#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">addStereotypeByString</a>, <a href="DeprecatedStereotypesHelper.html#addStereotypesWithNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">addStereotypesWithNames</a>, <a href="DeprecatedStereotypesHelper.html#getExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getExtendedElements</a>, <a href="DeprecatedStereotypesHelper.html#getExtendedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getExtendedElementsIncludingDerived</a>, <a href="DeprecatedStereotypesHelper.html#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String)">getStereotype</a>, <a href="DeprecatedStereotypesHelper.html#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)">getStereotype</a>, <a href="DeprecatedStereotypesHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getStereotypePropertyValue</a>, <a href="DeprecatedStereotypesHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getStereotypePropertyValue</a>, <a href="DeprecatedStereotypesHelper.html#hasExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">hasExtendedElements</a>, <a href="DeprecatedStereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">hasStereotype</a>, <a href="DeprecatedStereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">hasStereotype</a>, <a href="DeprecatedStereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">hasStereotypeOrDerived</a>, <a href="DeprecatedStereotypesHelper.html#isElementStereotypedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isElementStereotypedBy</a>, <a href="DeprecatedStereotypesHelper.html#removeStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeStereotypeByString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="DeprecatedTagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">DeprecatedTagsHelper</a></h3>
<code><a href="DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">clearStereotypeProperty</a>, <a href="DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">clearStereotypeProperty</a>, <a href="DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyFirst</a>, <a href="DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypePropertyFirst</a>, <a href="DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyValue</a>, <a href="DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypePropertyValue</a>, <a href="DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">getStereotypePropertyValueAsString</a>, <a href="DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)">getStereotypePropertyValueAsString</a></code></div>
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
<h3>TagsHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TagsHelper</span>()</div>
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
<section class="detail" id="getStereotypePropertyStringValue(java.lang.Object)">
<h3>getStereotypePropertyStringValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStereotypePropertyStringValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Converts given stereotype property value to a string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - value object</dd>
<dt>Returns:</dt>
<dd>string representation of given value object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTagDefinitionOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue)">
<h3>getTagDefinitionOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getTagDefinitionOwner</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue)</span></div>
<div class="block">Returns stereotype owning tag definition of given tagged value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - the given TaggedValue</dd>
<dt>Returns:</dt>
<dd>stereotype owning tag definition of given tagged value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object)">
<h3>removeTaggedValueValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeTaggedValueValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Removes value from given TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - the given TaggedValue</dd>
<dd><code>value</code> - value to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean)">
<h3>addTaggedValueValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">addTaggedValueValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean append)</span></div>
<div class="block">Add value to the given TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - the given TaggedValue</dd>
<dd><code>value</code> - value to add</dd>
<dd><code>append</code> - True - Don't remove the append value</dd>
<dt>Returns:</dt>
<dd>true if succeeded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean,boolean)">
<h3>addTaggedValueValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">addTaggedValueValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a> taggedValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean append,
 boolean setAnotherEnd)</span></div>
<div class="block">Add value to the given TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taggedValue</code> - the given TaggedValue</dd>
<dd><code>value</code> - value</dd>
<dd><code>append</code> - True - Don't remove the append value</dd>
<dd><code>setAnotherEnd</code> - set another meta association end value</dd>
<dt>Returns:</dt>
<dd>true if succeeded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)">
<h3>removeTaggedValueValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeTaggedValueValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Removes a value from the tagged value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which has the tagged value</dd>
<dd><code>stereotype</code> - stereotype which defines the tag</dd>
<dd><code>tagName</code> - tag name</dd>
<dd><code>value</code> - value to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getPropertyByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getPropertyByName</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Returns property of stereotype by name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype to get property from</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getTaggedValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></span> <span class="element-name">getTaggedValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Returns tagged value for stereotype tag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>TaggedValue of the tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>getTaggedValueOrCreate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></span> <span class="element-name">getTaggedValueOrCreate</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean createDefaultValue)</span></div>
<div class="block">Returns tagged value for stereotype tag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with assigned stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>createDefaultValue</code> - create default values for a tagged value</dd>
<dt>Returns:</dt>
<dd>TaggedValue of the tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>getTaggedValueOrCreate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></span> <span class="element-name">getTaggedValueOrCreate</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition,
 boolean createDefaultValue)</span></div>
<div class="block">Returns tagged value for stereotype tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with assigned stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagDefinition</code> - tag definition</dd>
<dd><code>createDefaultValue</code> - create default values for a tagged value</dd>
<dt>Returns:</dt>
<dd>TaggedValue of the tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getTaggedValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></span> <span class="element-name">getTaggedValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition)</span></div>
<div class="block">Returns tagged value for given tag definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied tagged values</dd>
<dd><code>tagDefinition</code> - tag definition</dd>
<dt>Returns:</dt>
<dd>TaggedValue of the tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">
<h3>createDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createDefaultValues</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 boolean createAll)</span></div>
<div class="block">Creates tagged values with default values for given element from given Stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - in this element tagged values will be created</dd>
<dd><code>stereotypes</code> - tags providers</dd>
<dd><code>createAll</code> - creates tagged values for all tags (do not check multiplicity). If false, tagged values will be created for tags which have multiplicity lower &gt;=1.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">
<h3>createDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createDefaultValues</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean createAll)</span></div>
<div class="block">Creates tagged values with default values for given element from given Stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - in this element tagged values will be created</dd>
<dd><code>stereotype</code> - tags provider</dd>
<dd><code>createAll</code> - creates tagged values for all tags (do not check multiplicity). If false, tagged values will be created for tags which have multiplicity lower &gt;=1.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null or second argument is not Stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getStereotypePropertyValueAsString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStereotypePropertyValueAsString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Gets tagged values as list of strings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with assigned stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>getStereotypePropertyValueAsString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStereotypePropertyValueAsString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</span></div>
<div class="block">Gets tagged values as list of strings</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived property value</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition)</span></div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>tagDefinition</code> - tag definition</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition,
 boolean calculateDerived)</span></div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>tagDefinition</code> - property</dd>
<dd><code>calculateDerived</code> - if to calculate derived property value</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</span></div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived property value</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean)">
<h3>setStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues)</span></div>
<div class="block">Sets tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - name of stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>value</code> - value</dd>
<dd><code>appendValues</code> - append or replace existing values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValueWithClearPredicate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,T,boolean,java.util.function.Predicate)">
<h3 id="setStereotypePropertyValueWithClearPredicate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean,java.util.function.Predicate)">setStereotypePropertyValueWithClearPredicate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValueWithClearPredicate</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 @CheckForNull
 T value,
 boolean appendValues,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; clearValuesPredicate)</span></div>
<div class="block">Sets tagged values. If clear predicate is found and true, clears tagged values and removes TaggedValue, otherwise continues on setting tagged value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - name of stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>value</code> - value</dd>
<dd><code>appendValues</code> - append or replace existing values</dd>
<dd><code>clearValuesPredicate</code> - clear values predicate to check if value needs to be removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)">
<h3>setStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - name of stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>value</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean,boolean)">
<h3>setStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues,
 boolean setAnotherEnd)</span></div>
<div class="block">Sets tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>value</code> - value</dd>
<dd><code>appendValues</code> - true to leave current value intact and add new one, false to replace current value with new one.</dd>
<dd><code>setAnotherEnd</code> - calculate and change value of another meta association end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">
<h3>setStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues)</span></div>
<div class="block">Sets tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - name of stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value</dd>
<dd><code>appendValues</code> - append or replace existing values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">
<h3>setStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets tagged values. Existing values will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - name of stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean,boolean)">
<h3>setStereotypePropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean appendValues,
 boolean setAnotherEnd)</span></div>
<div class="block">Sets tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>value</code> - value</dd>
<dd><code>appendValues</code> - true to leave current value intact and add new one, false to replace current value with new one.</dd>
<dd><code>setAnotherEnd</code> - calculate and change value of another meta association end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getTaggedValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a></span> <span class="element-name">getTaggedValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Looks for tagged value with given tag name in the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>tagName</code> - tag name</dd>
<dt>Returns:</dt>
<dd>tagged value with given tag name in the given element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValidTagType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>isValidTagType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isValidTagType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="block">Check if given type is valid for a tag of a Stereotype. Tag can be typed just by Stereotype, Data Type or metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - type</dd>
<dt>Returns:</dt>
<dd>true if valid</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectVisibleTaggedValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>collectVisibleTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt;</span> <span class="element-name">collectVisibleTaggedValues</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns visible tagged values applied to the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list of visible tagged values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotypePropertyValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasStereotypePropertyValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotypePropertyValues</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Checks if given element has some tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>true if some tagged value is created for a given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>clearStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Clears tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>clearStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean disposeTaggedValue)</span></div>
<div class="block">Clears tagged values and removes TaggedValue if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype of property</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>disposeTaggedValue</code> - disposes  TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>clearStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</span></div>
<div class="block">Clears tagged values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>tag</code> - tag definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>clearStereotypeProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearStereotypeProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 boolean disposeTaggedValue)</span></div>
<div class="block">Clears tagged values and removes TaggedValue if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>disposeTaggedValue</code> - disposes  TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>getStereotypePropertyFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypePropertyFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Returns first value of TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dt>Returns:</dt>
<dd>first value of TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>getStereotypePropertyFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypePropertyFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean calculateDerived)</span></div>
<div class="block">Returns first value of TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagName</code> - name of tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived value</dd>
<dt>Returns:</dt>
<dd>first value of TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getStereotypePropertyFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypePropertyFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag)</span></div>
<div class="block">Returns first value of TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>tag</code> - tag definition</dd>
<dt>Returns:</dt>
<dd>first value of TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>getStereotypePropertyFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getStereotypePropertyFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tag,
 boolean calculateDerived)</span></div>
<div class="block">Returns first value of TaggedValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>tag</code> - tag definition</dd>
<dd><code>calculateDerived</code> - if to calculate derived value</dd>
<dt>Returns:</dt>
<dd>first value of TaggedValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertiesWithDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getPropertiesWithDerived</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getPropertiesWithDerived</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns properties of stereotype including derived ones. Use this only if you do not care about order of collected properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>set of properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertiesWithDerivedOrdered(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getPropertiesWithDerivedOrdered</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getPropertiesWithDerivedOrdered</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns properties of stereotype including derived ones, first will be own element properties then parent and so on.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>list of properties</dd>
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
