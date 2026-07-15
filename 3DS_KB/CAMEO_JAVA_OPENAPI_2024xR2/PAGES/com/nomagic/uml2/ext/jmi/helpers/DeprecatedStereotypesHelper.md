# JAVA OPENAPI: DeprecatedStereotypesHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/jmi/helpers/DeprecatedStereotypesHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/DeprecatedStereotypesHelper.html`
- source_sha256: `34f2107917a45eb3fe3de82fbc874bb2ee741c2fd8c32362dcca7269475c8784`
- captured_utc: `2026-07-14T16:56:08.442602+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class DeprecatedStereotypesHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper](DeprecatedTagsHelper.html)
com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper

Direct Known Subclasses:
`[TagsHelper](TagsHelper.html)`

@OpenApiAllpublic classDeprecatedStereotypesHelper
extends [DeprecatedTagsHelper](DeprecatedTagsHelper.html)

Utility class to work with stereotypes. It has only deprecated methods for API compatibility.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INVISIBLE_STEREOTYPE_NAME](#INVISIBLE_STEREOTYPE_NAME)`
Deprecated.
use [`MagicDrawProfile.InvisibleStereotypeStereotype.STEREOTYPE_NAME`](../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#STEREOTYPE_NAME)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[METAMODEL](#METAMODEL)`
Deprecated.
use [`StandardProfile.METAMODEL_STEREOTYPE`](../../../StandardProfile.html#METAMODEL_STEREOTYPE)
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DeprecatedStereotypesHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[addStereotypeByString](#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)`
Deprecated.
use [`StereotypesHelper.addStereotype(Element, Stereotype)`](StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
`static void`
`[addStereotypeByString](#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)`
Deprecated.
use [`StereotypesHelper.addStereotype(Element, Stereotype)`](StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
`static void`
`[addStereotypesWithNames](#addStereotypesWithNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> stereotypesNames)`
Deprecated.
use [`StereotypesHelper.addStereotypes(Element, Collection)`](StereotypesHelper.html#addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getExtendedElements](#getExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Deprecated.
use [`StereotypesHelper.getStereotypedElements(Stereotype)`](StereotypesHelper.html#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)) as it has better naming of the method
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getExtendedElementsIncludingDerived](#getExtendedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Deprecated.
use [`StereotypesHelper.getStereotypedElementsIncludingDerived(Stereotype)`](StereotypesHelper.html#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)) as it has better naming of the method
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Deprecated.
this method returns first found stereotype from the project.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)`
Deprecated.
this method is not suitable when project contains more than one profile with same name but different URI.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition)`
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Property)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getStereotypePropertyValue](#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition,
 boolean calculateDerived)`
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Property, boolean)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))
`static boolean`
`[hasExtendedElements](#hasExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Deprecated.
use [`StereotypesHelper.hasStereotypedElements(Stereotype)`](StereotypesHelper.html#hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)) as it has better naming of the method
`static boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)`
Deprecated.
use [`StereotypesHelper.hasStereotype(Element, Stereotype)`](StereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
`static boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)`
Deprecated.
this method is not suitable when project contains more than one profile with same name but different URI.
`static boolean`
`[hasStereotypeOrDerived](#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Deprecated.
use [`StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)`](StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
`static boolean`
`[isElementStereotypedBy](#isElementStereotypedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Deprecated.
use [`StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)`](StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
`static void`
`[removeStereotypeByString](#removeStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)`
Deprecated.
use [`StereotypesHelper.removeStereotype(Element, Stereotype)`](StereotypesHelper.html#removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedTagsHelper](DeprecatedTagsHelper.html)
`[clearStereotypeProperty](DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [clearStereotypeProperty](DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyFirst](DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyFirst](DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyValue](DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyValue](DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyValueAsString](DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyValueAsString](DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
INVISIBLE_STEREOTYPE_NAME
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INVISIBLE_STEREOTYPE_NAME
Deprecated.
use [`MagicDrawProfile.InvisibleStereotypeStereotype.STEREOTYPE_NAME`](../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#STEREOTYPE_NAME)
Name of invisible stereotype
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper.INVISIBLE_STEREOTYPE_NAME)
METAMODEL
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) METAMODEL
Deprecated.
use [`StandardProfile.METAMODEL_STEREOTYPE`](../../../StandardProfile.html#METAMODEL_STEREOTYPE)
Name of metamodel stereotype
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper.METAMODEL)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DeprecatedStereotypesHelper
public DeprecatedStereotypesHelper()
 ============ METHOD DETAIL ========== 
Method Details
hasStereotype
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean hasStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Deprecated.
this method is not suitable when project contains more than one profile with same name but different URI. Use [`StereotypesHelper.hasStereotype(Element, Stereotype)`](StereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Checks if element has applied stereotype
Parameters:
`element` - element to check
`stereotypeName` - stereotype name to check
`profileName` - profile name where reside the stereotype
Returns:
true if element has applied stereotype with given name
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype or profileName is null
addStereotypeByString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void addStereotypeByString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Deprecated.
use [`StereotypesHelper.addStereotype(Element, Stereotype)`](StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Applies stereotype on element by name.
 The default tag values are not created, to create these values use [`TagsHelper.createDefaultValues(Element, Stereotype, boolean)`](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)).
Parameters:
`element` - element
`stereotype` - name of stereotype to apply
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype is null
addStereotypeByString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void addStereotypeByString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Deprecated.
use [`StereotypesHelper.addStereotype(Element, Stereotype)`](StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Applies stereotype on element by name.
 The default tag values are not created, to create these values use [`TagsHelper.createDefaultValues(Element, Stereotype, boolean)`](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)).
Parameters:
`element` - element
`stereotype` - name of stereotype to apply
`profileName` - name of profile where reside the stereotype
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype pr profileName is null
addStereotypesWithNames
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void addStereotypesWithNames([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> stereotypesNames)
Deprecated.
use [`StereotypesHelper.addStereotypes(Element, Collection)`](StereotypesHelper.html#addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))
Applies stereotypes for specified element.
 The default tag values are created for tags with multiplicity lower bound >=1.
Parameters:
`element` - element on which stereotypes are applied
`stereotypesNames` - stereotype names, collection of String objects
removeStereotypeByString
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void removeStereotypeByString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Deprecated.
use [`StereotypesHelper.removeStereotype(Element, Stereotype)`](StereotypesHelper.html#removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Removes applied stereotype from given element.
Parameters:
`element` - element
`stereotype` - name of stereotype to remove
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype is null
hasStereotype
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean hasStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotype)
Deprecated.
use [`StereotypesHelper.hasStereotype(Element, Stereotype)`](StereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Checks if element has applied stereotype with given name.
Parameters:
`element` - element to check
`stereotype` - stereotype name to check
Returns:
true if element has applied stereotype with given name
getStereotype
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getStereotype([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Deprecated.
this method returns first found stereotype from the project. It is better to narrow down the search with profile, use `StereotypesHelper.getStereotype(Project project, String stereotypeName, Profile profile)`
Returns stereotype for given name
Parameters:
`project` - project
`stereotypeName` - name of stereotype
Returns:
found stereotype or null
getStereotype
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getStereotype(@CheckForNull
 [Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)
Deprecated.
this method is not suitable when project contains more than one profile with same name but different URI. Use `StereotypesHelper.getStereotype(Project project, String stereotypeName, Profile profile)`
Returns stereotype for given name
Parameters:
`project` - project to search for a stereotype
`stereotypeName` - name of stereotype
`profileName` - profile name
Returns:
found stereotype or null
hasStereotypeOrDerived
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean hasStereotypeOrDerived([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Deprecated.
use [`StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)`](StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Checks if element has assigned given stereotype or derived stereotype from given.
Parameters:
`element` - element
`stereotypeName` - name of stereotype
Returns:
boolean true if element is stereotyped by given stereotype
isElementStereotypedBy
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isElementStereotypedBy([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Deprecated.
use [`StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)`](StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
Checks if element has assigned given stereotype or derived stereotype from given.
Parameters:
`element` - element
`stereotypeName` - name of stereotype
Returns:
boolean true if element is stereotyped by given stereotype
getStereotypePropertyValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition)
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Property)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype
`tagDefinition` - tag definition
Returns:
values
getStereotypePropertyValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getStereotypePropertyValue([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Property](../../magicdraw/classes/mdkernel/Property.html) tagDefinition,
 boolean calculateDerived)
Deprecated.
use [`TagsHelper.getStereotypePropertyValue(Element, Property, boolean)`](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))
Gets tagged values as list.
Parameters:
`element` - element with applied stereotype
`stereotype` - stereotype not used parameter - left here for compatibility
`tagDefinition` - property
`calculateDerived` - if to calculate derived property value
Returns:
values
getExtendedElementsIncludingDerived
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getExtendedElementsIncludingDerived(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Deprecated.
use [`StereotypesHelper.getStereotypedElementsIncludingDerived(Stereotype)`](StereotypesHelper.html#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)) as it has better naming of the method
Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.
Parameters:
`stereotype` - stereotype
Returns:
collection of elements stereotyped by stereotype
getExtendedElements
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getExtendedElements(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Deprecated.
use [`StereotypesHelper.getStereotypedElements(Stereotype)`](StereotypesHelper.html#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)) as it has better naming of the method
Returns all elements stereotyped by stereotype
Parameters:
`stereotype` - stereotype
Returns:
list of elements stereotyped by stereotype
hasExtendedElements
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean hasExtendedElements([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Deprecated.
use [`StereotypesHelper.hasStereotypedElements(Stereotype)`](StereotypesHelper.html#hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)) as it has better naming of the method
Checks if stereotype has stereotyped elements
Parameters:
`stereotype` - stereotype to check
Returns:
true if stereotype has stereotyped elements

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class DeprecatedStereotypesHelper">Class DeprecatedStereotypesHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="DeprecatedTagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="TagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">TagsHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DeprecatedStereotypesHelper</span>
<span class="extends-implements">extends <a href="DeprecatedTagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">DeprecatedTagsHelper</a></span></div>
<div class="block">Utility class to work with stereotypes. It has only deprecated methods for API compatibility.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INVISIBLE_STEREOTYPE_NAME">INVISIBLE_STEREOTYPE_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#STEREOTYPE_NAME"><code>MagicDrawProfile.InvisibleStereotypeStereotype.STEREOTYPE_NAME</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METAMODEL">METAMODEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../StandardProfile.html#METAMODEL_STEREOTYPE"><code>StandardProfile.METAMODEL_STEREOTYPE</code></a></div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DeprecatedStereotypesHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addStereotypeByString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.addStereotype(Element, Stereotype)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">addStereotypeByString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.addStereotype(Element, Stereotype)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addStereotypesWithNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">addStereotypesWithNames</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; stereotypesNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)"><code>StereotypesHelper.addStereotypes(Element, Collection)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getExtendedElements</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.getStereotypedElements(Stereotype)</code></a> as it has better naming of the method</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getExtendedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getExtendedElementsIncludingDerived</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.getStereotypedElementsIncludingDerived(Stereotype)</code></a> as it has better naming of the method</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String)">getStereotype</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">this method returns first found stereotype from the project.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)">getStereotype</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">this method is not suitable when project contains more than one profile with same name but different URI.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)"><code>TagsHelper.getStereotypePropertyValue(Element, Property)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getStereotypePropertyValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition,
 boolean calculateDerived)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)"><code>TagsHelper.getStereotypePropertyValue(Element, Property, boolean)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hasExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">hasExtendedElements</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotypedElements(Stereotype)</code></a> as it has better naming of the method</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">hasStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotype(Element, Stereotype)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">hasStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">this method is not suitable when project contains more than one profile with same name but different URI.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">hasStereotypeOrDerived</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isElementStereotypedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isElementStereotypedBy</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#removeStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeStereotypeByString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.removeStereotype(Element, Stereotype)</code></a></div>
</div>
</div>
</div>
</div>
</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="INVISIBLE_STEREOTYPE_NAME">
<h3>INVISIBLE_STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INVISIBLE_STEREOTYPE_NAME</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#STEREOTYPE_NAME"><code>MagicDrawProfile.InvisibleStereotypeStereotype.STEREOTYPE_NAME</code></a></div>
</div>
<div class="block">Name of invisible stereotype</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper.INVISIBLE_STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METAMODEL">
<h3>METAMODEL</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">METAMODEL</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../StandardProfile.html#METAMODEL_STEREOTYPE"><code>StandardProfile.METAMODEL_STEREOTYPE</code></a></div>
</div>
<div class="block">Name of metamodel stereotype</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper.METAMODEL">Constant Field Values</a></li>
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
<h3>DeprecatedStereotypesHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DeprecatedStereotypesHelper</span>()</div>
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
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">this method is not suitable when project contains more than one profile with same name but different URI. Use <a href="StereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotype(Element, Stereotype)</code></a></div>
</div>
<div class="block">Checks if element has applied stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dd><code>stereotypeName</code> - stereotype name to check</dd>
<dd><code>profileName</code> - profile name where reside the stereotype</dd>
<dt>Returns:</dt>
<dd>true if element has applied stereotype with given name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype or profileName is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addStereotypeByString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStereotypeByString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.addStereotype(Element, Stereotype)</code></a></div>
</div>
<div class="block">Applies stereotype on element by name.
 The default tag values are not created, to create these values use <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)"><code>TagsHelper.createDefaultValues(Element, Stereotype, boolean)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - name of stereotype to apply</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)">
<h3>addStereotypeByString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStereotypeByString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.addStereotype(Element, Stereotype)</code></a></div>
</div>
<div class="block">Applies stereotype on element by name.
 The default tag values are not created, to create these values use <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)"><code>TagsHelper.createDefaultValues(Element, Stereotype, boolean)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - name of stereotype to apply</dd>
<dd><code>profileName</code> - name of profile where reside the stereotype</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype pr profileName  is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotypesWithNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>addStereotypesWithNames</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStereotypesWithNames</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; stereotypesNames)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)"><code>StereotypesHelper.addStereotypes(Element, Collection)</code></a></div>
</div>
<div class="block">Applies stereotypes for specified element.
 The default tag values are created for tags with multiplicity lower bound &gt;=1.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element on which stereotypes are applied</dd>
<dd><code>stereotypesNames</code> - stereotype names, collection of String objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeStereotypeByString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeStereotypeByString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.removeStereotype(Element, Stereotype)</code></a></div>
</div>
<div class="block">Removes applied stereotype from given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - name of stereotype to remove</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotype(Element, Stereotype)</code></a></div>
</div>
<div class="block">Checks if element has applied stereotype with given name.</div>
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
<section class="detail" id="getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getStereotype</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">this method returns first found stereotype from the project. It is better to narrow down the search with profile, use <code>StereotypesHelper.getStereotype(Project project, String stereotypeName, Profile profile)</code></div>
</div>
<div class="block">Returns stereotype for given name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dt>Returns:</dt>
<dd>found stereotype or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)">
<h3>getStereotype</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">this method is not suitable when project contains more than one profile with same name but different URI. Use <code>StereotypesHelper.getStereotype(Project project, String stereotypeName, Profile profile)</code></div>
</div>
<div class="block">Returns stereotype for given name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search for a stereotype</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dd><code>profileName</code> - profile name</dd>
<dt>Returns:</dt>
<dd>found stereotype or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>hasStereotypeOrDerived</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotypeOrDerived</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)</code></a></div>
</div>
<div class="block">Checks if element has assigned given stereotype or derived stereotype from given.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dt>Returns:</dt>
<dd>boolean true if  element is stereotyped by given stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementStereotypedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>isElementStereotypedBy</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isElementStereotypedBy</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotypeOrDerived(Element, Stereotype)</code></a></div>
</div>
<div class="block">Checks if element has assigned given stereotype or derived stereotype from given.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dt>Returns:</dt>
<dd>boolean true if  element is stereotyped by given stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)"><code>TagsHelper.getStereotypePropertyValue(Element, Property)</code></a></div>
</div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>tagDefinition</code> - tag definition</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>getStereotypePropertyValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getStereotypePropertyValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> tagDefinition,
 boolean calculateDerived)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)"><code>TagsHelper.getStereotypePropertyValue(Element, Property, boolean)</code></a></div>
</div>
<div class="block">Gets tagged values as list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with applied stereotype</dd>
<dd><code>stereotype</code> - stereotype  not used parameter - left here for compatibility</dd>
<dd><code>tagDefinition</code> - property</dd>
<dd><code>calculateDerived</code> - if to calculate derived property value</dd>
<dt>Returns:</dt>
<dd>values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtendedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getExtendedElementsIncludingDerived</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getExtendedElementsIncludingDerived</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.getStereotypedElementsIncludingDerived(Stereotype)</code></a> as it has better naming of the method</div>
</div>
<div class="block">Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>collection of elements stereotyped by stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getExtendedElements</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getExtendedElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.getStereotypedElements(Stereotype)</code></a> as it has better naming of the method</div>
</div>
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
<section class="detail" id="hasExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>hasExtendedElements</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasExtendedElements</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="StereotypesHelper.html#hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>StereotypesHelper.hasStereotypedElements(Stereotype)</code></a> as it has better naming of the method</div>
</div>
<div class="block">Checks if stereotype has stereotyped elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype to check</dd>
<dt>Returns:</dt>
<dd>true if stereotype has stereotyped elements</dd>
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
