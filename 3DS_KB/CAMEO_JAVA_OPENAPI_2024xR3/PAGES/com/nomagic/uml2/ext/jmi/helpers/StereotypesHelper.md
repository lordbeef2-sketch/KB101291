# JAVA OPENAPI: StereotypesHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html`
- source_sha256: `67e314993b0b4c768500f4d0aa3e79a840698d422fb5ff51fdd751f87f2e6eb7`
- captured_utc: `2026-07-14T16:56:18.243711+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class StereotypesHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper](DeprecatedTagsHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.TagsHelper](TagsHelper.html)
com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper

@OpenApiAllpublic classStereotypesHelper
extends [TagsHelper](TagsHelper.html)
A helper class used to work with stereotypes and tagged values.
 This helper provides a lot of methods for applying stereotypes to elements, creating tagged values or setting values for tags.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML2METAMODEL](#UML2METAMODEL)`
Name of UML2 metamodel
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML2METAMODEL_PRIMITIVE_TYPES](#UML2METAMODEL_PRIMITIVE_TYPES)`
Name of primitives package in the UML2 metamodel
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML2METAMODEL_URI](#UML2METAMODEL_URI)`
URI of UML2 metamodel, must correspond UML standard profile metamodel uri.
Fields inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)
`[INVISIBLE_STEREOTYPE_NAME](DeprecatedStereotypesHelper.html#INVISIBLE_STEREOTYPE_NAME), [METAMODEL](DeprecatedStereotypesHelper.html#METAMODEL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StereotypesHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addStereotype](#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Applies stereotype to a given element.
`static void`
`[addStereotype](#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,int))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 int index)`
Applies stereotype to a given element.
`static void`
`[addStereotypes](#addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Applies stereotypes from collection for specified element.
`static void`
`[applyProfile](#applyProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Applies profile to the package
`static void`
`[applyProfiles](#applyProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> profiles)`
Applies profiles from collection to specified package
`static void`
`[assignImageFilesToStereotype](#assignImageFilesToStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> files)`
Assigns given image files to stereotype as icons.
`static boolean`
`[canApplyProfile](#canApplyProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Checks profile can apply to package.
`static boolean`
`[canApplyStereotype](#canApplyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if stereotype can be applied to element
`static boolean`
`[canAssignStereotype](#canAssignStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Indicates if stereotype can be applied to a given element.
`static boolean`
`[canRemoveProfile](#canRemoveProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Checks if it is possible to remove applied profile from package
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[checkForDerivedStereotype](#checkForDerivedStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if the given stereotype, or it's child is already applied to the element.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[checkForDerivedStereotype](#checkForDerivedStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Checks if there are child of at least one given stereotype already set to given element
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[checkForDerivedStereotype](#checkForDerivedStereotype(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) parent)`
Checks if there are given stereotype or derived stereotype in a given stereotypes collection.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[createStereotype](#createStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)`
Creates stereotype instance and sets base classes for it
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[createStereotype](#createStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) owner,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)`
Creates stereotype instance and sets base classes for it
`static void`
`[deriveStereotype](#deriveStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) parent,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) child)`
Derives stereotype from other stereotype.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[filterVisibleElement](#filterVisibleElement(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)`
Filter elements from given collection whose are "visible".
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[filterVisibleStereotypes](#filterVisibleStereotypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Filter stereotypes from given collection whose are "visible".
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[findCommonAssignedStereotypes](#findCommonAssignedStereotypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)`
Finds common applied stereotypes for list of collection
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getAllAssignedStereotypes](#getAllAssignedStereotypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)`
Returns all applied stereotypes for elements of collection
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getAllMetaClasses](#getAllMetaClasses(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns collection of all metamodel classes
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)>`
`[getAllMetaModels](#getAllMetaModels(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns collection of all model elements
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)>`
`[getAllProfiles](#getAllProfiles(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns list of all loaded profiles.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getAllStereotypes](#getAllStereotypes(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns collection of all stereotypes
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)>`
`[getAppliedProfiles](#getAppliedProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg)`
Returns collection of applied profiles on package
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getAppliedStereotypeByString](#getAppliedStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Returns stereotype applied to element with given name.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getAssignedMetaClassOfSubtype](#getAssignedMetaClassOfSubtype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) meta)`
Collect all subtypes of given metaclasses whose are extended by a given stereotype
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getBaseClass](#getBaseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns metaclass of given element.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getBaseClasses](#getBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all base (meta) classes for stereotype
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getBaseClasses](#getBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean includeFromParentStereotypes)`
Returns all base (meta) classes for stereotype
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[getBaseClassesAsClasses](#getBaseClassesAsClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns collection(java.lang.Class) of metaclasses from stereotype
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)`
`[getClassOfMetaClass](#getClassOfMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../magicdraw/classes/mdkernel/Class.html) metaClass)`
Returns java.lang.Class for metaclass by Class
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getDefaultMetaClasses](#getDefaultMetaClasses(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Dummy procedure for setting of metaclasses
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)>`
`[getDependingProfiles](#getDependingProfiles(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Returns collection of profiles depending on given profile
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getDerivedStereotypes](#getDerivedStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) parent,
 boolean includeParent)`
Returns applied derived stereotypes
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getDerivedStereotypesRecursively](#getDerivedStereotypesRecursively(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns derived stereotypes recursively
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getElementsRequiresExtension](#getElementsRequiresExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))([Extension](../../magicdraw/mdprofiles/Extension.html) extension)`
Checks which stereotyped elements requires this extension (it provides base class for stereotyped element).
`static [Extension](../../magicdraw/mdprofiles/Extension.html)`
`[getExtension](#getExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) baseClass)`
Checks if stereotype has baseClass as METACLASS
`static [ExtensionEnd](../../magicdraw/mdprofiles/ExtensionEnd.html)`
`[getExtensionEnd](#getExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))([Extension](../../magicdraw/mdprofiles/Extension.html) extension)`
ExtensionEnd of given Extension
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[getExtensionMetaProperty](#getExtensionMetaProperty(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Collects properties of MetaClass extension end
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[getExtensionMetaProperty](#getExtensionMetaProperty(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean includeInherited)`
Collects properties of MetaClass extension end
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Extension](../../magicdraw/mdprofiles/Extension.html)>`
`[getExtensions](#getExtensions(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) baseClass)`
Collects Extensions connected to this stereotype.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Extension](../../magicdraw/mdprofiles/Extension.html)>`
`[getExtensions](#getExtensions(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,boolean))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) baseClass,
 boolean takeInherited)`
Get Extension Meta Property.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getFirstStereotypeWithIcon](#getFirstStereotypeWithIcon(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> collectionOfStereotypes)`
Returns first stereotype with icon from given collection of stereotypes.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getFirstStereotypeWithIcon](#getFirstStereotypeWithIcon(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> collectionOfStereotypes,
 boolean includeInvisible)`
Returns first stereotype with icon from given collection of stereotypes.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getFirstVisibleStereotype](#getFirstVisibleStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns first visible stereotype applied to given element.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getFirstVisibleStereotype](#getFirstVisibleStereotype(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Returns first visible stereotype from given collection of stereotypes.
`static [ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns ICON from stereotype
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getMetaClassByClass](#getMetaClassByClass(com.nomagic.magicdraw.core.Project,java.lang.Class))([Project](../../../../magicdraw/core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz)`
Returns metaclass by given class.
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getMetaClassByName](#getMetaClassByName(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns metaclass by name
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getMetaClassByName](#getMetaClassByName(java.lang.String,java.util.Collection))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> models)`
Returns metaclass by name from collection of models
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getMetaClasses](#getMetaClasses(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> models)`
Returns metaclasses by collection of models
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getMetaClassesByClass](#getMetaClassesByClass(com.nomagic.magicdraw.core.Project,java.util.Collection))([Project](../../../../magicdraw/core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> classes)`
Returns names of metaclasses from collection
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getMetaClassesFromPackageByName](#getMetaClassesFromPackageByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Search for class in given scope(package) by class name.
`static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getMetaModelByElement](#getMetaModelByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns metamodel of specified element in the metamodel.
`static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getMetaModelByMetaClass](#getMetaModelByMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../magicdraw/classes/mdkernel/Class.html) metaClass)`
Returns meta model of specified meta class.
`static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getMetaModelByName](#getMetaModelByName(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Return metamodel with specified name.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getNamesOfMetaClasses](#getNamesOfMetaClasses(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> models)`
Returns names of metaclasses by collection of models
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getNamesOfSuperClasses](#getNamesOfSuperClasses(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../magicdraw/classes/mdkernel/Class.html) aClass)`
Returns names of supper classes for metaclass
`static [PrimitiveType](../../magicdraw/classes/mdkernel/PrimitiveType.html)`
`[getPrimitiveByName](#getPrimitiveByName(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Finds primitiveType by name
`static [Package](../../magicdraw/classes/mdkernel/Package.html)`
`[getPrimitiveTypesPackage](#getPrimitiveTypesPackage(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns primitive types package of UML2 metamodel.
`static [Profile](../../magicdraw/mdprofiles/Profile.html)`
`[getProfile](#getProfile(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)`
Returns profile element by name
`static [Profile](../../magicdraw/mdprofiles/Profile.html)`
`[getProfileByURI](#getProfileByURI(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileURI)`
Returns profile element by URI
`static [Package](../../magicdraw/classes/mdkernel/Package.html)`
`[getProfileForStereotype](#getProfileForStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns profile for a given stereotype.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)>`
`[getProfiles](#getProfiles(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)`
Filters all given project profiles by name.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getSettableStereotypes](#getSettableStereotypes(com.nomagic.magicdraw.core.Project,java.lang.String,boolean))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementType,
 boolean includeSuperTypes)`
Returns collection of settable stereotypes for element type
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getSettableStereotypes](#getSettableStereotypes(com.nomagic.magicdraw.core.Project,java.util.Collection,boolean))([Project](../../../../magicdraw/core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements,
 boolean includeSuperTypes)`
Returns collection of settable stereotypes for collection of elements
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Returns stereotype for given name by profile.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getStereotypedElements](#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all elements stereotyped by stereotype
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)>`
`[getStereotypedElementsIncludingDerived](#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getStereotypes](#getStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns all stereotypes applied to element.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getStereotypesByMetaClasses](#getStereotypesByMetaClasses(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)`
Collects stereotypes which extend given metaclasses.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getStereotypesByProfile](#getStereotypesByProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Returns collection of stereotypes by profile
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getTypeClasses](#getTypeClasses(java.util.Collection,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elementTypes,
 boolean includeSubtypes,
 boolean expandAbstract)`
Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getTypeClasses](#getTypeClasses(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> elementTypes)`
Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getUML2BaseClass](#getUML2BaseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Returns UML2 metamodel metaclass for a given Element.
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getUML2BaseClassByJavaClass](#getUML2BaseClassByJavaClass(com.nomagic.magicdraw.core.Project,java.lang.Class))([Project](../../../../magicdraw/core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) javaClass)`
Returns UML2 metamodel metaclass for a given Java class.
`static [Class](../../magicdraw/classes/mdkernel/Class.html)`
`[getUML2MetaClassByName](#getUML2MetaClassByName(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
/**
 Returns meta class from UML2 meta model by name
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)>`
`[getUML2MetaClasses](#getUML2MetaClasses(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns collection of all UML2 metaclasses
`static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getUML2MetaModel](#getUML2MetaModel(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Returns model element for UML2 meta model
`static boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Checks if element has applied stereotypes
`static boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if element has applied stereotype.
`static boolean`
`[hasStereotype](#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Checks if element has applied at least one stereotype from given collection of Stereotypes.
`static boolean`
`[hasStereotypedElements](#hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if stereotype has stereotyped elements
`static boolean`
`[hasStereotypeOrDerived](#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Checks if there are child of parent stereotype already set
`static boolean`
`[hasStereotypeOrDerived](#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Checks if element has applied at least one stereotype(or derived) from given collection of Stereotypes.
`static boolean`
`[hasSuperMetaClass](#hasSuperMetaClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) meta)`
Checks if stereotype has super metaclass.
`static boolean`
`[hasVisibleStereotype](#hasVisibleStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Check if given element has at least one visible stereotype.
`static boolean`
`[isBuiltInUML2Metamodel](#isBuiltInUML2Metamodel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model))([Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html) model)`
Checks if given model is built in (not user modeled) UML metamodel.
`static boolean`
`[isExtensionProperty](#isExtensionProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../magicdraw/classes/mdkernel/Property.html) property)`

`static boolean`
`[isFromPrimitiveTypes](#isFromPrimitiveTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Checks if given element is from UML2 metamodel primitive types package
`static boolean`
`[isInvisible](#isInvisible(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement))([RedefinableElement](../../magicdraw/classes/mdkernel/RedefinableElement.html) element)`
Check is element is invisible (has Invisible stereotype or one of its children)
`static boolean`
`[isMetaClass](#isMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../magicdraw/classes/mdkernel/Class.html) aClass)`
Checks if Class is metaclass, including user defined metaclasses.
`static boolean`
`[isMetaClass](#isMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Checks if given element is a metaclass, including user defined metaclasses.
`static boolean`
`[isOfType](#isOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> metaTypes,
 boolean checkDSL)`
Checks if element is of type from given meta-types
`static boolean`
`[isRequiredStereotypeForElement](#isRequiredStereotypeForElement(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Checks if stereotype is required for element
`static boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> typesCollection,
 boolean includeInherited)`
Checks if element is of type from typesCollection.
`static boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean,boolean))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> typesCollection,
 boolean includeInherited,
 boolean includeCustomTypes)`
Checks if element is of type from typesCollection.
`static boolean`
`[isUML2MetaClass](#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../magicdraw/classes/mdkernel/Class.html) aClass)`
Checks if Class is metaclass, and this metaclass represents currently instantiated UML model.
`static void`
`[optimizeStereotypes](#optimizeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Optimize applied stereotypes to an Element by removing more general stereotypes if more specific are applied.
`static void`
`[removeBaseClass](#removeBaseClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) metaClass)`
removes base (meta) class for stereotype
`static void`
`[removeProfile](#removeProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)`
Removes profile application from the package
`static void`
`[removeProfiles](#removeProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection))([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> profiles)`
Removes applied profiles in package from collection
`static void`
`[removeStereotype](#removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Remove applied stereotype from element.
`static void`
`[removeStereotypes](#removeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Removes all applied stereotypes from element.
`static void`
`[removeStereotypes](#removeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Removes all stereotypes from element.
`static void`
`[removeSuperMetaClasses](#removeSuperMetaClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) meta)`
Remove super metaclass from the given stereotype.
`static [Extension](../../magicdraw/mdprofiles/Extension.html)`
`[setBaseClass](#setBaseClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) metaClass,
 [Extension](../../magicdraw/mdprofiles/Extension.html) extension)`
Sets base (meta) class for stereotype
`static void`
`[setBaseClasses](#setBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)`
Sets base (meta) classes for stereotype
`static void`
`[setBaseClassesByName](#setBaseClassesByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection))([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> metaClasses)`
Sets base (meta) classes for stereotype by names
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[TagsHelper](TagsHelper.html)
`[addTaggedValueValue](TagsHelper.html#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean)), [addTaggedValueValue](TagsHelper.html#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean,boolean)), [clearStereotypeProperty](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [clearStereotypeProperty](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [clearStereotypeProperty](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [clearStereotypeProperty](TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)), [collectVisibleTaggedValues](TagsHelper.html#collectVisibleTaggedValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [createDefaultValues](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)), [createDefaultValues](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)), [getPropertiesWithDerived](TagsHelper.html#getPropertiesWithDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [getPropertiesWithDerivedOrdered](TagsHelper.html#getPropertiesWithDerivedOrdered(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [getPropertyByName](TagsHelper.html#getPropertyByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [getStereotypePropertyFirst](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [getStereotypePropertyFirst](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [getStereotypePropertyFirst](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [getStereotypePropertyFirst](TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)), [getStereotypePropertyStringValue](TagsHelper.html#getStereotypePropertyStringValue(java.lang.Object)), [getStereotypePropertyValue](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [getStereotypePropertyValue](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [getStereotypePropertyValue](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [getStereotypePropertyValue](TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)), [getStereotypePropertyValueAsString](TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [getStereotypePropertyValueAsString](TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)), [getTagDefinitionOwner](TagsHelper.html#getTagDefinitionOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue)), [getTaggedValue](TagsHelper.html#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [getTaggedValue](TagsHelper.html#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [getTaggedValue](TagsHelper.html#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [getTaggedValueOrCreate](TagsHelper.html#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [getTaggedValueOrCreate](TagsHelper.html#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)), [hasStereotypePropertyValues](TagsHelper.html#hasStereotypePropertyValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isValidTagType](TagsHelper.html#isValidTagType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)), [removeTaggedValueValue](TagsHelper.html#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)), [removeTaggedValueValue](TagsHelper.html#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object)), [setStereotypePropertyValue](TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)), [setStereotypePropertyValue](TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)), [setStereotypePropertyValue](TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean,boolean)), [setStereotypePropertyValue](TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)), [setStereotypePropertyValue](TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean)), [setStereotypePropertyValue](TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean,boolean)), [setStereotypePropertyValueWithClearPredicate](TagsHelper.html#setStereotypePropertyValueWithClearPredicate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,T,boolean,java.util.function.Predicate))`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedStereotypesHelper](DeprecatedStereotypesHelper.html)
`[addStereotypeByString](DeprecatedStereotypesHelper.html#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [addStereotypeByString](DeprecatedStereotypesHelper.html#addStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [addStereotypesWithNames](DeprecatedStereotypesHelper.html#addStereotypesWithNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)), [getExtendedElements](DeprecatedStereotypesHelper.html#getExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [getExtendedElementsIncludingDerived](DeprecatedStereotypesHelper.html#getExtendedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [getStereotype](DeprecatedStereotypesHelper.html#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String)), [getStereotype](DeprecatedStereotypesHelper.html#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)), [getStereotypePropertyValue](DeprecatedStereotypesHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [getStereotypePropertyValue](DeprecatedStereotypesHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [hasExtendedElements](DeprecatedStereotypesHelper.html#hasExtendedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [hasStereotype](DeprecatedStereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [hasStereotype](DeprecatedStereotypesHelper.html#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [hasStereotypeOrDerived](DeprecatedStereotypesHelper.html#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [isElementStereotypedBy](DeprecatedStereotypesHelper.html#isElementStereotypedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [removeStereotypeByString](DeprecatedStereotypesHelper.html#removeStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[DeprecatedTagsHelper](DeprecatedTagsHelper.html)
`[clearStereotypeProperty](DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [clearStereotypeProperty](DeprecatedTagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyFirst](DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyFirst](DeprecatedTagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyValue](DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyValue](DeprecatedTagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean)), [getStereotypePropertyValueAsString](DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String)), [getStereotypePropertyValueAsString](DeprecatedTagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
UML2METAMODEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML2METAMODEL
Name of UML2 metamodel
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper.UML2METAMODEL)
UML2METAMODEL_URI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML2METAMODEL_URI
URI of UML2 metamodel, must correspond UML standard profile metamodel uri.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper.UML2METAMODEL_URI)
UML2METAMODEL_PRIMITIVE_TYPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML2METAMODEL_PRIMITIVE_TYPES
Name of primitives package in the UML2 metamodel
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper.UML2METAMODEL_PRIMITIVE_TYPES)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StereotypesHelper
public StereotypesHelper()
 ============ METHOD DETAIL ========== 
Method Details
getAllProfiles
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> getAllProfiles([Project](../../../../magicdraw/core/Project.html) project)
Returns list of all loaded profiles. Returning writable copy.
Parameters:
`project` - project
Returns:
list of all loaded profiles
getProfile
@CheckForNullpublic static [Profile](../../magicdraw/mdprofiles/Profile.html) getProfile([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)
Returns profile element by name
Parameters:
`project` - project
`profileName` - profile name
Returns:
profile element or null if profile not found
getProfileByURI
@CheckForNullpublic static [Profile](../../magicdraw/mdprofiles/Profile.html) getProfileByURI([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileURI)
Returns profile element by URI
Parameters:
`project` - project
`profileURI` - profile uri
Returns:
profile element or null if profile not found
getProfiles
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> getProfiles([Project](../../../../magicdraw/core/Project.html) project,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)
Filters all given project profiles by name.
Parameters:
`project` - given project
`profileName` - the profile name
Returns:
list of profiles that name corresponds to the given profile name
getStereotypes
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getStereotypes([Element](../../magicdraw/classes/mdkernel/Element.html) element)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Returns all stereotypes applied to element.
Parameters:
`element` - element
Returns:
applied stereotypes for this element or empty list if there are no applied stereotypes
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
hasStereotype
public static boolean hasStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Checks if element has applied stereotypes
Parameters:
`element` - element
Returns:
true if it has applied stereotype
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
hasStereotype
public static boolean hasStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Checks if element has applied stereotype.
Parameters:
`element` - element
`stereotype` - stereotype name to check
Returns:
true if element has applied stereotype
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
hasStereotype
public static boolean hasStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Checks if element has applied at least one stereotype from given collection of Stereotypes.
Parameters:
`element` - element
`stereotypes` - a collection of stereotypes
Returns:
true if element has applied at least one stereotype from the given collection
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
addStereotype
public static void addStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Applies stereotype to a given element.
 The default tag values are not created, to create these values use [`TagsHelper.createDefaultValues(Element, Stereotype, boolean)`](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)).
Parameters:
`element` - element
`stereotype` - stereotype to apply
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype is null, or element is disposed
addStereotype
public static void addStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 int index)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Applies stereotype to a given element.
 The default tag values are not created, to create these values use [`TagsHelper.createDefaultValues(Element, Stereotype, boolean)`](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)).
Parameters:
`element` - element
`stereotype` - stereotype to apply
`index` - index of the stereotype
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype is null
addStereotypes
public static void addStereotypes([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Applies stereotypes from collection for specified element.
 The default tag values are not created, to create these values use [`TagsHelper.createDefaultValues(Element, Stereotype, boolean)`](TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)).
Parameters:
`element` - element on which stereotypes are applied
`stereotypes` - collection of `Stereotype` objects
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotypes is null
removeStereotype
public static void removeStereotype(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Remove applied stereotype from element.
Parameters:
`element` - element
`stereotype` - stereotype to remove
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotype is null
removeStereotypes
public static void removeStereotypes([Element](../../magicdraw/classes/mdkernel/Element.html) element)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Removes all applied stereotypes from element.
Parameters:
`element` - element
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
removeStereotypes
public static void removeStereotypes([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Removes all stereotypes from element.
Parameters:
`element` - element
`stereotypes` - collection of stereotypes to remove
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element or stereotypes is null
getAppliedStereotypeByString
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getAppliedStereotypeByString([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Returns stereotype applied to element with given name.
Parameters:
`element` - element
`stereotypeName` - name of stereotype
Returns:
applied stereotype with that name
getStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getStereotype([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName,
 @CheckForNull
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Returns stereotype for given name by profile.
 First search is performed directly in given profile and if no stereotype is found, then sub profiles are checked.
Parameters:
`project` - project
`stereotypeName` - name of stereotype
`profile` - stereotype's profile, null if any
Returns:
stereotype
getStereotypedElementsIncludingDerived
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getStereotypedElementsIncludingDerived(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.
Parameters:
`stereotype` - stereotype
Returns:
collection of elements stereotyped by stereotype
getStereotypedElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getStereotypedElements(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all elements stereotyped by stereotype
Parameters:
`stereotype` - stereotype
Returns:
list of elements stereotyped by stereotype
hasStereotypedElements
public static boolean hasStereotypedElements([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Checks if stereotype has stereotyped elements
Parameters:
`stereotype` - stereotype to check
Returns:
true if stereotype has stereotyped elements
getFirstStereotypeWithIcon
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getFirstStereotypeWithIcon([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> collectionOfStereotypes)
Returns first stereotype with icon from given collection of stereotypes.
Parameters:
`collectionOfStereotypes` - a collection of stereotypes
Returns:
first stereotype with icon
getFirstStereotypeWithIcon
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getFirstStereotypeWithIcon([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> collectionOfStereotypes,
 boolean includeInvisible)
Returns first stereotype with icon from given collection of stereotypes.
Parameters:
`collectionOfStereotypes` - a collection of stereotypes
`includeInvisible` - indicates whether invisible stereotypes should be taken into account
Returns:
first stereotype with icon
getFirstVisibleStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getFirstVisibleStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns first visible stereotype applied to given element.
Parameters:
`element` - given element
Returns:
first visible stereotype
getFirstVisibleStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getFirstVisibleStereotype([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Returns first visible stereotype from given collection of stereotypes.
Parameters:
`stereotypes` - a collection of stereotypes.
Returns:
first visible stereotype.
getAllStereotypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getAllStereotypes([Project](../../../../magicdraw/core/Project.html) project)
Returns collection of all stereotypes
Parameters:
`project` - project
Returns:
collection of all stereotypes
findCommonAssignedStereotypes
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> findCommonAssignedStereotypes([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)
Finds common applied stereotypes for list of collection
Parameters:
`elements` - collection of elements
Returns:
common stereotypes
getAllAssignedStereotypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getAllAssignedStereotypes([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)
Returns all applied stereotypes for elements of collection
Parameters:
`elements` - collection of elements
Returns:
all applied stereotypes
getExtension
@CheckForNullpublic static [Extension](../../magicdraw/mdprofiles/Extension.html) getExtension([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) baseClass)
Checks if stereotype has baseClass as METACLASS
Parameters:
`stereotype` - stereotype
`baseClass` - meta class
Returns:
extension for base class
getExtensions
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Extension](../../magicdraw/mdprofiles/Extension.html)> getExtensions([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) baseClass)
Collects Extensions connected to this stereotype.
Parameters:
`stereotype` - Stereotype
`baseClass` - Base class.
Returns:
List of extension.
getExtensions
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Extension](../../magicdraw/mdprofiles/Extension.html)> getExtensions([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) baseClass,
 boolean takeInherited)
Get Extension Meta Property.
Parameters:
`stereotype` - Stereotype
`baseClass` - Base class.
`takeInherited` - collect inherited extension ends also
Returns:
List of extension.
getBaseClasses
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getBaseClasses(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all base (meta) classes for stereotype
Parameters:
`stereotype` - stereotype
Returns:
collection(Class) of base (meta) classes
getBaseClasses
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getBaseClasses(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean includeFromParentStereotypes)
Returns all base (meta) classes for stereotype
Parameters:
`stereotype` - stereotype
`includeFromParentStereotypes` - also take bases classes from parent stereotypes
Returns:
collection(Class) of base (meta) classes
getSettableStereotypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getSettableStereotypes([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementType,
 boolean includeSuperTypes)
Returns collection of settable stereotypes for element type
Parameters:
`project` - project
`elementType` - element type
`includeSuperTypes` - include super types also
Returns:
collection of settable stereotypes
getSettableStereotypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getSettableStereotypes([Project](../../../../magicdraw/core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements,
 boolean includeSuperTypes)
Returns collection of settable stereotypes for collection of elements
Parameters:
`project` - project
`elements` - collection of elements
`includeSuperTypes` - include super types also
Returns:
collection of settable stereotypes
getUML2MetaModel
@CheckForNullpublic static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html) getUML2MetaModel([Project](../../../../magicdraw/core/Project.html) project)
Returns model element for UML2 meta model
Parameters:
`project` - project
Returns:
model element for UML2 meta model
isBuiltInUML2Metamodel
public static boolean isBuiltInUML2Metamodel([Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html) model)
Checks if given model is built in (not user modeled) UML metamodel. Built in metamodel is loaded from standard profile.
Parameters:
`model` - model to check
Returns:
true if model is built in uml model
getAllMetaModels
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> getAllMetaModels([Project](../../../../magicdraw/core/Project.html) project)
Returns collection of all model elements
Parameters:
`project` - project
Returns:
collection of all model elements
getMetaModelByName
@CheckForNullpublic static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html) getMetaModelByName([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Return metamodel with specified name.
Parameters:
`project` - project to search for metamodel.
`name` - name metamodel name.
Returns:
metamodel with specified name. `null` if not found.
getAllMetaClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getAllMetaClasses([Project](../../../../magicdraw/core/Project.html) project)
Returns collection of all metamodel classes
Parameters:
`project` - project
Returns:
collection of all meta model classes
getUML2MetaClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getUML2MetaClasses([Project](../../../../magicdraw/core/Project.html) project)
Returns collection of all UML2 metaclasses
Parameters:
`project` - project
Returns:
collection of all UML2 metaclasses
getMetaClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getMetaClasses([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> models)
Returns metaclasses by collection of models
Parameters:
`models` - collection of models
Returns:
collection(Class) of meta classes
getNamesOfMetaClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getNamesOfMetaClasses([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> models)
Returns names of metaclasses by collection of models
Parameters:
`models` - collection of models
Returns:
collection(String) of metaclasses
getMetaClassByName
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getMetaClassByName([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns metaclass by name
Parameters:
`project` - project
`name` - name of metaclass
Returns:
Class element of metaclass
getMetaClassByName
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getMetaClassByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html)> models)
Returns metaclass by name from collection of models
Parameters:
`name` - name of metaclass
`models` - collection of models to look for
Returns:
Class element of metaclass
getMetaClassesFromPackageByName
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getMetaClassesFromPackageByName([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Search for class in given scope(package) by class name.
 Search is using query.
Parameters:
`pkg` - Package instance.
`name` - Class name
Returns:
UML Class or null.
getUML2MetaClassByName
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getUML2MetaClassByName([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
/**
 Returns meta class from UML2 meta model by name
Parameters:
`project` - given project
`name` - name of metaclass
Returns:
Class element of metaclass
getMetaModelByMetaClass
@CheckForNullpublic static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html) getMetaModelByMetaClass([Class](../../magicdraw/classes/mdkernel/Class.html) metaClass)
Returns meta model of specified meta class.
Parameters:
`metaClass` - meta class
Returns:
metamodel of metaclass. `null` if `c` is not metaclass
getMetaModelByElement
@CheckForNullpublic static [Model](../../magicdraw/auxiliaryconstructs/mdmodels/Model.html) getMetaModelByElement([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns metamodel of specified element in the metamodel. Method is expanded to support
 enumerations and literals from model.
Parameters:
`element` - metaclass or other meta element.
Returns:
metamodel of metaclass. `null` if `element` is not metaclass
isMetaClass
public static boolean isMetaClass([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Checks if given element is a metaclass, including user defined metaclasses. For pure uml metaclass use [`isUML2MetaClass(Class)`](#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))
Parameters:
`element` - class
Returns:
true if element is metaclass
isMetaClass
public static boolean isMetaClass([Class](../../magicdraw/classes/mdkernel/Class.html) aClass)
Checks if Class is metaclass, including user defined metaclasses. For pure uml metaclass use [`isUML2MetaClass(Class)`](#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))
Parameters:
`aClass` - class
Returns:
true if Class is metaclass
isUML2MetaClass
public static boolean isUML2MetaClass([Class](../../magicdraw/classes/mdkernel/Class.html) aClass)
Checks if Class is metaclass, and this metaclass represents currently instantiated UML model.
Parameters:
`aClass` - class
Returns:
true if Class is uml 2 metaclass.
setBaseClassesByName
public static void setBaseClassesByName([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> metaClasses)
Sets base (meta) classes for stereotype by names
Parameters:
`stereotype` - stereotype
`metaClasses` - collection of metaclasses names
setBaseClasses
public static void setBaseClasses([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)
Sets base (meta) classes for stereotype
Parameters:
`stereotype` - stereotype
`metaClasses` - collection of metaclasses
setBaseClass
@CheckForNullpublic static [Extension](../../magicdraw/mdprofiles/Extension.html) setBaseClass([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Class](../../magicdraw/classes/mdkernel/Class.html) metaClass,
 @CheckForNull
 [Extension](../../magicdraw/mdprofiles/Extension.html) extension)
Sets base (meta) class for stereotype
Parameters:
`stereotype` - stereotype
`metaClass` - meta class
`extension` - extension for class and stereotype
Returns:
created Extension
removeBaseClass
public static void removeBaseClass([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 @CheckForNull
 [Class](../../magicdraw/classes/mdkernel/Class.html) metaClass)
removes base (meta) class for stereotype
Parameters:
`stereotype` - stereotype
`metaClass` - meta class
createStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) createStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) owner,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)
Creates stereotype instance and sets base classes for it
Parameters:
`owner` - owner of stereotype
`name` - name of stereotype
`metaClasses` - meta classes for stereotype
Returns:
stereotype
createStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) createStereotype([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)
Creates stereotype instance and sets base classes for it
Parameters:
`project` - project
`name` - name of stereotype
`metaClasses` - meta classes for stereotype
Returns:
created stereotype
getDefaultMetaClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getDefaultMetaClasses([Project](../../../../magicdraw/core/Project.html) project)
Dummy procedure for setting of metaclasses
Parameters:
`project` - project
Returns:
default meta class
getNamesOfSuperClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getNamesOfSuperClasses([Class](../../magicdraw/classes/mdkernel/Class.html) aClass)
Returns names of supper classes for metaclass
Parameters:
`aClass` - meta class UML class
Returns:
collection of names
canApplyStereotype
public static boolean canApplyStereotype(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Checks if stereotype can be applied to element
Parameters:
`element` - element
`stereotype` - stereotype
Returns:
true if stereotype can be applied to element
getIcon
@CheckForNullpublic static [ResizableIcon](../../../../ui/ResizableIcon.html) getIcon(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns ICON from stereotype
Parameters:
`stereotype` - stereotype
Returns:
icon
deriveStereotype
public static void deriveStereotype([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) parent,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) child)
Derives stereotype from other stereotype.
Parameters:
`parent` - parent stereotype
`child` - child stereotype
getMetaClassByClass
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getMetaClassByClass([Project](../../../../magicdraw/core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz)
Returns metaclass by given class.
Parameters:
`project` - project
`clazz` - class from which to get name from
Returns:
meta class
getMetaClassesByClass
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getMetaClassesByClass([Project](../../../../magicdraw/core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> classes)
Returns names of metaclasses from collection
Parameters:
`project` - project
`classes` - collection of metaclasses to get names from
Returns:
collection of names
getBaseClass
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getBaseClass([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns metaclass of given element.
Parameters:
`element` - given element
Returns:
Class element of metaclass
getUML2BaseClass
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getUML2BaseClass([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Returns UML2 metamodel metaclass for a given Element.
Parameters:
`element` - given element
Returns:
Class element of metaclass
getUML2BaseClassByJavaClass
@CheckForNullpublic static [Class](../../magicdraw/classes/mdkernel/Class.html) getUML2BaseClassByJavaClass([Project](../../../../magicdraw/core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) javaClass)
Returns UML2 metamodel metaclass for a given Java class.
Parameters:
`project` - project
`javaClass` - given Java Class
Returns:
Class element of metaclass
getBaseClassesAsClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> getBaseClassesAsClasses(@CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns collection(java.lang.Class) of metaclasses from stereotype
Parameters:
`stereotype` - stereotype
Returns:
collection of metaclasses
canAssignStereotype
public static boolean canAssignStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Indicates if stereotype can be applied to a given element.
 - checks if stereotype metaclass fits class of an element.
Parameters:
`element` - element to which stereotype should be applied.
`stereotype` - stereotype to assign.
Returns:
true if stereotype can be applied, false otherwise.
isInvisible
public static boolean isInvisible(@CheckForNull
 [RedefinableElement](../../magicdraw/classes/mdkernel/RedefinableElement.html) element)
Check is element is invisible (has Invisible stereotype or one of its children)
Parameters:
`element` - element
Returns:
true if element is invisible
See Also:
[`MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()`](../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype())
canApplyProfile
public static boolean canApplyProfile([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Checks profile can apply to package.
Parameters:
`pkg` - The given package.
`profile` - The given profile.
Returns:
boolean
applyProfile
public static void applyProfile([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Applies profile to the package
Parameters:
`pkg` - package
`profile` - profile to apply
removeProfile
public static void removeProfile([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Removes profile application from the package
Parameters:
`pkg` - package
`profile` - applied profile
getStereotypesByProfile
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getStereotypesByProfile([Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Returns collection of stereotypes by profile
Parameters:
`profile` - profile
Returns:
collection of stereotypes by profile
isRequiredStereotypeForElement
public static boolean isRequiredStereotypeForElement([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)
Checks if stereotype is required for element
Parameters:
`stereotype` - stereotype
`element` - element
Returns:
true if stereotype is required for element
getClassOfMetaClass
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) getClassOfMetaClass([Class](../../magicdraw/classes/mdkernel/Class.html) metaClass)
Returns java.lang.Class for metaclass by Class
Parameters:
`metaClass` - meta class
Returns:
java.lang.Class for metaclass
applyProfiles
public static void applyProfiles([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> profiles)
Applies profiles from collection to specified package
Parameters:
`pkg` - package
`profiles` - list of profiles
removeProfiles
public static void removeProfiles(@CheckForNull
 [Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> profiles)
Removes applied profiles in package from collection
Parameters:
`pkg` - package
`profiles` - collection of profiles
getAppliedProfiles
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> getAppliedProfiles(@CheckForNull
 [Package](../../magicdraw/classes/mdkernel/Package.html) pkg)
Returns collection of applied profiles on package
Parameters:
`pkg` - package
Returns:
collection of applied profiles
canRemoveProfile
public static boolean canRemoveProfile([Package](../../magicdraw/classes/mdkernel/Package.html) pkg,
 [Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Checks if it is possible to remove applied profile from package
Parameters:
`pkg` - package
`profile` - profile
Returns:
true if it is possible to remove applied profile
getDependingProfiles
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Profile](../../magicdraw/mdprofiles/Profile.html)> getDependingProfiles([Profile](../../magicdraw/mdprofiles/Profile.html) profile)
Returns collection of profiles depending on given profile
Parameters:
`profile` - profile
Returns:
collection of profiles
checkForDerivedStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) checkForDerivedStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Checks if the given stereotype, or it's child is already applied to the element.
Parameters:
`element` - element
`stereotype` - stereotype
Returns:
given stereotype or it's child applied to element
checkForDerivedStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) checkForDerivedStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Checks if there are child of at least one given stereotype already set to given element
Parameters:
`element` - element
`stereotypes` - a collection of stereotypes to check
Returns:
stereotype or child of stereotype applied to element
checkForDerivedStereotype
@CheckForNullpublic static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) checkForDerivedStereotype([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) parent)
Checks if there are given stereotype or derived stereotype in a given stereotypes collection.
Parameters:
`stereotypes` - collection of stereotypes to look in
`parent` - parent stereotype
Returns:
returns stereotype which equals to the given or is derived
getDerivedStereotypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getDerivedStereotypes([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) parent,
 boolean includeParent)
Returns applied derived stereotypes
Parameters:
`element` - element
`parent` - stereotype
`includeParent` - true if include parent stereotype in collection
Returns:
stereotype or child of stereotype for element
hasStereotypeOrDerived
public static boolean hasStereotypeOrDerived([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Checks if there are child of parent stereotype already set
Parameters:
`element` - element
`stereotype` - stereotype
Returns:
true if at least one child of parent is set for element
hasStereotypeOrDerived
public static boolean hasStereotypeOrDerived([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Checks if element has applied at least one stereotype(or derived) from given collection of Stereotypes.
Parameters:
`element` - element to check
`stereotypes` - a collection of stereotypes
Returns:
true if element has applied at least one stereotype from given collection
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if element is null
getStereotypesByMetaClasses
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getStereotypesByMetaClasses([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> metaClasses)
Collects stereotypes which extend given metaclasses.
Parameters:
`metaClasses` - meta classes
Returns:
stereotypes
getExtensionEnd
@CheckForNullpublic static [ExtensionEnd](../../magicdraw/mdprofiles/ExtensionEnd.html) getExtensionEnd([Extension](../../magicdraw/mdprofiles/Extension.html) extension)
ExtensionEnd of given Extension
Parameters:
`extension` - Extension
Returns:
ExtensionEnd of Extension
assignImageFilesToStereotype
public static void assignImageFilesToStereotype([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> files)
Assigns given image files to stereotype as icons.
Parameters:
`stereotype` - stereotype to which icons should be applied
`files` - image files to assign
getDerivedStereotypesRecursively
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getDerivedStereotypesRecursively([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns derived stereotypes recursively
Parameters:
`stereotype` - stereotype for which to return derived stereotypes
Returns:
list of derived stereotypes
getElementsRequiresExtension
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> getElementsRequiresExtension([Extension](../../magicdraw/mdprofiles/Extension.html) extension)
Checks which stereotyped elements requires this extension (it provides base class for stereotyped element).
Parameters:
`extension` - extension to check.
Returns:
elements which uses given extension.
getAssignedMetaClassOfSubtype
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](../../magicdraw/classes/mdkernel/Class.html)> getAssignedMetaClassOfSubtype([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) meta)
Collect all subtypes of given metaclasses whose are extended by a given stereotype
Parameters:
`stereotype` - stereotype
`meta` - meta class
Returns:
meta classes
hasSuperMetaClass
public static boolean hasSuperMetaClass([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) meta)
Checks if stereotype has super metaclass.
Parameters:
`stereotype` - stereotype
`meta` - meta class
Returns:
true if stereotype has super metaclass.
removeSuperMetaClasses
public static void removeSuperMetaClasses([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 [Class](../../magicdraw/classes/mdkernel/Class.html) meta)
Remove super metaclass from the given stereotype.
Parameters:
`stereotype` - stereotype
`meta` - meta class
isExtensionProperty
public static boolean isExtensionProperty([Property](../../magicdraw/classes/mdkernel/Property.html) property)
Parameters:
`property` - property
Returns:
true if given property is memberEnd of Extension
getProfileForStereotype
@CheckForNullpublic static [Package](../../magicdraw/classes/mdkernel/Package.html) getProfileForStereotype([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns profile for a given stereotype.
Parameters:
`stereotype` - stereotype
Returns:
profile where given stereotype is defined. If it has profile parent it is defined in profile, in other case parent package will be return.
getExtensionMetaProperty
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> getExtensionMetaProperty([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Collects properties of MetaClass extension end
Parameters:
`stereotype` - stereotype to check for metaclasses
Returns:
collection of properties.
getExtensionMetaProperty
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> getExtensionMetaProperty([Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype,
 boolean includeInherited)
Collects properties of MetaClass extension end
Parameters:
`stereotype` - stereotype to check for metaclasses
`includeInherited` - collection inherited meta properties
Returns:
collection of properties.
isFromPrimitiveTypes
public static boolean isFromPrimitiveTypes([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Checks if given element is from UML2 metamodel primitive types package
Parameters:
`element` - the given element
Returns:
true, if given element is from primitive types package.
getPrimitiveTypesPackage
@CheckForNullpublic static [Package](../../magicdraw/classes/mdkernel/Package.html) getPrimitiveTypesPackage([Project](../../../../magicdraw/core/Project.html) project)
Returns primitive types package of UML2 metamodel.
Parameters:
`project` - project.
Returns:
primitive types package.
getPrimitiveByName
@CheckForNullpublic static [PrimitiveType](../../magicdraw/classes/mdkernel/PrimitiveType.html) getPrimitiveByName([Project](../../../../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Finds primitiveType by name
Parameters:
`project` - project where find primitive.
`name` - primitive name.
Returns:
Primitive with given name.
hasVisibleStereotype
public static boolean hasVisibleStereotype([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Check if given element has at least one visible stereotype.
Parameters:
`element` - given element
Returns:
true if visible stereotype is applied to the given element
See Also:
[`MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()`](../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype())
filterVisibleStereotypes
@CheckForNullpublic static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> filterVisibleStereotypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Filter stereotypes from given collection whose are "visible". Stereotype is visible if it is not derived from <>
Parameters:
`stereotypes` - collection of stereotypes
Returns:
new collection of visible stereotypes
See Also:
[`MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()`](../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype())
filterVisibleElement
@CheckForNullpublic static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> filterVisibleElement(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elements)
Filter elements from given collection whose are "visible". Element is visible if it does not have applied stereotype <>
Parameters:
`elements` - collection of elements
Returns:
new collection of visible elements
See Also:
[`MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()`](../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype())
optimizeStereotypes
public static void optimizeStereotypes([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Optimize applied stereotypes to an Element by removing more general stereotypes if more specific are applied.
 This rule is applied only for stereotypes whose "hideMetatype" in DSL configuration
Parameters:
`element` - element
isTypeOf
public static boolean isTypeOf([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> typesCollection,
 boolean includeInherited)
Checks if element is of type from typesCollection. 3 scenarios can be tested
 1. Element is of specified type or inherited
 2. Element has applied stereotype or inherited stereotype
 3. InstanceSpecification has Classifier instance or inherited .
Parameters:
`element` - instance that type will be checked.
`typesCollection` - collection of types used to check if element type is part of it
`includeInherited` - if set to true all element type hierarchy will be checked against typesCollection
Returns:
true if element is of type from typesCollection
isTypeOf
public static boolean isTypeOf([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> typesCollection,
 boolean includeInherited,
 boolean includeCustomTypes)
Checks if element is of type from typesCollection. 3 scenarios can be tested
 1. Element is of specified type or inherited
 2. Element has applied stereotype or inherited stereotype
 3. InstanceSpecification has Classifier instance or inherited .
Parameters:
`element` - instance that type will be checked
`typesCollection` - collection of types used to check if element type is part of it
`includeInherited` - if set to true all element type hierarchy will be checked against typesCollection
`includeCustomTypes` - check against custom types
Returns:
true if element is of type from typesCollection
getTypeClasses
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getTypeClasses([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> elementTypes)
Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.
Parameters:
`elementTypes` - MetaType classes and stereotypes
Returns:
java.lang.Class objects and stereotypes.
getTypeClasses
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getTypeClasses([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> elementTypes,
 boolean includeSubtypes,
 boolean expandAbstract)
Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.
Parameters:
`elementTypes` - MetaType classes and stereotypes
`includeSubtypes` - if true derived stereotypes and metaClasses will be collected.
`expandAbstract` - if true and abstract metaClasses subtypes will be collected.
Returns:
java.lang.Class objects and stereotypes.
isOfType
public static boolean isOfType([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> metaTypes,
 boolean checkDSL)
Checks if element is of type from given meta-types
Parameters:
`element` - instance that type will be checked
`metaTypes` - meta types
`checkDSL` - take DSL rules into account
Returns:
true if element is of type from typesCollection

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class StereotypesHelper">Class StereotypesHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="DeprecatedTagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.DeprecatedTagsHelper</a>
<div class="inheritance"><a href="DeprecatedStereotypesHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.DeprecatedStereotypesHelper</a>
<div class="inheritance"><a href="TagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.TagsHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StereotypesHelper</span>
<span class="extends-implements">extends <a href="TagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">TagsHelper</a></span></div>
<div class="block">A helper class used to work with stereotypes and tagged values.
 This helper provides a lot of methods for applying stereotypes to elements, creating tagged values or setting values for tags.
 <p></p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UML2METAMODEL">UML2METAMODEL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Name of UML2 metamodel</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UML2METAMODEL_PRIMITIVE_TYPES">UML2METAMODEL_PRIMITIVE_TYPES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Name of primitives package in the UML2 metamodel</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UML2METAMODEL_URI">UML2METAMODEL_URI</a></code></div>
<div class="col-last even-row-color">
<div class="block">URI of UML2 metamodel, must correspond UML standard profile metamodel uri.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">StereotypesHelper</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">addStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies stereotype to a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,int)">addStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies stereotype to a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">addStereotypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies stereotypes from collection for specified element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">applyProfile</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies profile to the package</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection)">applyProfiles</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt; profiles)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies profiles from collection to specified package</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#assignImageFilesToStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection)">assignImageFilesToStereotype</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; files)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Assigns given image files to stereotype as icons.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canApplyProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">canApplyProfile</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks profile can apply to package.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canApplyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">canApplyStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if stereotype can be applied to element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAssignStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">canAssignStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if stereotype can be applied to a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canRemoveProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">canRemoveProfile</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if it is possible to remove applied profile from package</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkForDerivedStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">checkForDerivedStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if the given stereotype, or it's child is already applied to the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkForDerivedStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">checkForDerivedStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if there are child of at least one given stereotype already set to given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkForDerivedStereotype(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">checkForDerivedStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if there are given stereotype or derived stereotype in a given stereotypes collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection)">createStereotype</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates stereotype instance and sets base classes for it</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.util.Collection)">createStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates stereotype instance and sets base classes for it</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deriveStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">deriveStereotype</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> parent,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Derives stereotype from other stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterVisibleElement(java.util.Collection)">filterVisibleElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filter elements from given collection whose are "visible".</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterVisibleStereotypes(java.util.Collection)">filterVisibleStereotypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filter stereotypes from given collection whose are "visible".</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findCommonAssignedStereotypes(java.util.Collection)">findCommonAssignedStereotypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds common applied stereotypes for list of collection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllAssignedStereotypes(java.util.Collection)">getAllAssignedStereotypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all applied stereotypes for elements of collection</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllMetaClasses(com.nomagic.magicdraw.core.Project)">getAllMetaClasses</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of all metamodel classes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllMetaModels(com.nomagic.magicdraw.core.Project)">getAllMetaModels</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of all model elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllProfiles(com.nomagic.magicdraw.core.Project)">getAllProfiles</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns list of all loaded profiles.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllStereotypes(com.nomagic.magicdraw.core.Project)">getAllStereotypes</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of all stereotypes</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAppliedProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">getAppliedProfiles</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of applied profiles on package</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAppliedStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getAppliedStereotypeByString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns stereotype applied to element with given name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssignedMetaClassOfSubtype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getAssignedMetaClassOfSubtype</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> meta)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all subtypes of given metaclasses whose are extended by a given stereotype</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getBaseClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclass of given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getBaseClasses</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all base (meta) classes for stereotype</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">getBaseClasses</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean includeFromParentStereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all base (meta) classes for stereotype</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseClassesAsClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getBaseClassesAsClasses</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection(java.lang.Class) of metaclasses from stereotype</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassOfMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getClassOfMetaClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns java.lang.Class for metaclass by Class</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultMetaClasses(com.nomagic.magicdraw.core.Project)">getDefaultMetaClasses</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dummy procedure for setting of metaclasses</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependingProfiles(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">getDependingProfiles</a><wbr/>(<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of profiles depending on given profile</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDerivedStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">getDerivedStereotypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> parent,
 boolean includeParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns applied derived stereotypes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDerivedStereotypesRecursively(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getDerivedStereotypesRecursively</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns derived stereotypes recursively</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsRequiresExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">getElementsRequiresExtension</a><wbr/>(<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks which stereotyped elements requires this extension (it provides base class for stereotyped element).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getExtension</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> baseClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if stereotype has baseClass as METACLASS</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">getExtensionEnd</a><wbr/>(<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">ExtensionEnd of given Extension</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionMetaProperty(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getExtensionMetaProperty</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects properties of MetaClass extension end</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionMetaProperty(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">getExtensionMetaProperty</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean includeInherited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects properties of MetaClass extension end</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensions(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getExtensions</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> baseClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects Extensions connected to this stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensions(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,boolean)">getExtensions</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> baseClass,
 boolean takeInherited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Extension Meta Property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstStereotypeWithIcon(java.util.Collection)">getFirstStereotypeWithIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; collectionOfStereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first stereotype with icon from given collection of stereotypes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstStereotypeWithIcon(java.util.Collection,boolean)">getFirstStereotypeWithIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; collectionOfStereotypes,
 boolean includeInvisible)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first stereotype with icon from given collection of stereotypes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstVisibleStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getFirstVisibleStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first visible stereotype applied to given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstVisibleStereotype(java.util.Collection)">getFirstVisibleStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first visible stereotype from given collection of stereotypes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getIcon</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns ICON from stereotype</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassByClass(com.nomagic.magicdraw.core.Project,java.lang.Class)">getMetaClassByClass</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclass by given class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassByName(com.nomagic.magicdraw.core.Project,java.lang.String)">getMetaClassByName</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclass by name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassByName(java.lang.String,java.util.Collection)">getMetaClassByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt; models)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclass by name from collection of models</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClasses(java.util.Collection)">getMetaClasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt; models)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclasses by collection of models</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassesByClass(com.nomagic.magicdraw.core.Project,java.util.Collection)">getMetaClassesByClass</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt; classes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns names of metaclasses from collection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassesFromPackageByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">getMetaClassesFromPackageByName</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for class in given scope(package) by class name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaModelByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getMetaModelByElement</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metamodel of specified element in the metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaModelByMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getMetaModelByMetaClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns meta model of specified meta class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaModelByName(com.nomagic.magicdraw.core.Project,java.lang.String)">getMetaModelByName</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return metamodel with specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNamesOfMetaClasses(java.util.Collection)">getNamesOfMetaClasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt; models)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns names of metaclasses by collection of models</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNamesOfSuperClasses(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getNamesOfSuperClasses</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> aClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns names of supper classes for metaclass</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrimitiveByName(com.nomagic.magicdraw.core.Project,java.lang.String)">getPrimitiveByName</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds primitiveType by name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrimitiveTypesPackage(com.nomagic.magicdraw.core.Project)">getPrimitiveTypesPackage</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns primitive types package of UML2 metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfile(com.nomagic.magicdraw.core.Project,java.lang.String)">getProfile</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns profile element by name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfileByURI(com.nomagic.magicdraw.core.Project,java.lang.String)">getProfileByURI</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileURI)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns profile element by URI</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfileForStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getProfileForStereotype</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns profile for a given stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfiles(com.nomagic.magicdraw.core.Project,java.lang.String)">getProfiles</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters all given project profiles by name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSettableStereotypes(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">getSettableStereotypes</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementType,
 boolean includeSuperTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of settable stereotypes for element type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSettableStereotypes(com.nomagic.magicdraw.core.Project,java.util.Collection,boolean)">getSettableStereotypes</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean includeSuperTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of settable stereotypes for collection of elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">getStereotype</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns stereotype for given name by profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getStereotypedElements</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements stereotyped by stereotype</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getStereotypedElementsIncludingDerived</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements stereotyped by stereotype and by stereotypes derived from this stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStereotypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all stereotypes applied to element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypesByMetaClasses(java.util.Collection)">getStereotypesByMetaClasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects stereotypes which extend given metaclasses.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypesByProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">getStereotypesByProfile</a><wbr/>(<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of stereotypes by profile</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeClasses(java.util.Collection,boolean,boolean)">getTypeClasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementTypes,
 boolean includeSubtypes,
 boolean expandAbstract)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeClasses(java.util.Collection)">getTypeClasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUML2BaseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUML2BaseClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns UML2 metamodel metaclass for a given Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUML2BaseClassByJavaClass(com.nomagic.magicdraw.core.Project,java.lang.Class)">getUML2BaseClassByJavaClass</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> javaClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns UML2 metamodel metaclass for a given Java class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUML2MetaClassByName(com.nomagic.magicdraw.core.Project,java.lang.String)">getUML2MetaClassByName</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">/**
 Returns meta class from UML2 meta model by name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUML2MetaClasses(com.nomagic.magicdraw.core.Project)">getUML2MetaClasses</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns collection of all UML2 metaclasses</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUML2MetaModel(com.nomagic.magicdraw.core.Project)">getUML2MetaModel</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns model element for UML2 meta model</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element has applied stereotypes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">hasStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element has applied stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">hasStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element has applied at least one stereotype from given collection of Stereotypes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">hasStereotypedElements</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if stereotype has stereotyped elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">hasStereotypeOrDerived</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if there are child of parent stereotype already set</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">hasStereotypeOrDerived</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element has applied at least one stereotype(or derived) from given collection of Stereotypes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasSuperMetaClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">hasSuperMetaClass</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> meta)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if stereotype has super metaclass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasVisibleStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasVisibleStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element has at least one visible stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isBuiltInUML2Metamodel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">isBuiltInUML2Metamodel</a><wbr/>(<a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> model)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given model is built in (not user modeled) UML metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExtensionProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isExtensionProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFromPrimitiveTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFromPrimitiveTypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given element is from UML2 metamodel primitive types package</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInvisible(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement)">isInvisible</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check is element is invisible (has Invisible stereotype or one of its children)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">isMetaClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> aClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if Class is metaclass, including user defined metaclasses.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMetaClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given element is a metaclass, including user defined metaclasses.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">isOfType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt; metaTypes,
 boolean checkDSL)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element is of type from given meta-types</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequiredStereotypeForElement(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRequiredStereotypeForElement</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if stereotype is required for element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">isTypeOf</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; typesCollection,
 boolean includeInherited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element is of type from typesCollection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean,boolean)">isTypeOf</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; typesCollection,
 boolean includeInherited,
 boolean includeCustomTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element is of type from typesCollection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">isUML2MetaClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> aClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if Class is metaclass, and this metaclass represents currently instantiated UML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#optimizeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">optimizeStereotypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Optimize applied stereotypes to an Element by removing more general stereotypes if more specific are applied.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBaseClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">removeBaseClass</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">removes base (meta) class for stereotype</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">removeProfile</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes profile application from the package</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection)">removeProfiles</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt; profiles)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes applied profiles in package from collection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">removeStereotype</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove applied stereotype from element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeStereotypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all applied stereotypes from element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">removeStereotypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all stereotypes from element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSuperMetaClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">removeSuperMetaClasses</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> meta)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove super metaclass from the given stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setBaseClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">setBaseClass</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass,
 <a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets base (meta) class for stereotype</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection)">setBaseClasses</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets base (meta) classes for stereotype</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setBaseClassesByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection)">setBaseClassesByName</a><wbr/>(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; metaClasses)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets base (meta) classes for stereotype by names</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.TagsHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="TagsHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">TagsHelper</a></h3>
<code><a href="TagsHelper.html#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean)">addTaggedValueValue</a>, <a href="TagsHelper.html#addTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object,boolean,boolean)">addTaggedValueValue</a>, <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">clearStereotypeProperty</a>, <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">clearStereotypeProperty</a>, <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">clearStereotypeProperty</a>, <a href="TagsHelper.html#clearStereotypeProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">clearStereotypeProperty</a>, <a href="TagsHelper.html#collectVisibleTaggedValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectVisibleTaggedValues</a>, <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">createDefaultValues</a>, <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">createDefaultValues</a>, <a href="TagsHelper.html#getPropertiesWithDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getPropertiesWithDerived</a>, <a href="TagsHelper.html#getPropertiesWithDerivedOrdered(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getPropertiesWithDerivedOrdered</a>, <a href="TagsHelper.html#getPropertyByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getPropertyByName</a>, <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getStereotypePropertyFirst</a>, <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getStereotypePropertyFirst</a>, <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyFirst</a>, <a href="TagsHelper.html#getStereotypePropertyFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypePropertyFirst</a>, <a href="TagsHelper.html#getStereotypePropertyStringValue(java.lang.Object)">getStereotypePropertyStringValue</a>, <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getStereotypePropertyValue</a>, <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getStereotypePropertyValue</a>, <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyValue</a>, <a href="TagsHelper.html#getStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypePropertyValue</a>, <a href="TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getStereotypePropertyValueAsString</a>, <a href="TagsHelper.html#getStereotypePropertyValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getStereotypePropertyValueAsString</a>, <a href="TagsHelper.html#getTagDefinitionOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue)">getTagDefinitionOwner</a>, <a href="TagsHelper.html#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getTaggedValue</a>, <a href="TagsHelper.html#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getTaggedValue</a>, <a href="TagsHelper.html#getTaggedValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getTaggedValue</a>, <a href="TagsHelper.html#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getTaggedValueOrCreate</a>, <a href="TagsHelper.html#getTaggedValueOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">getTaggedValueOrCreate</a>, <a href="TagsHelper.html#hasStereotypePropertyValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasStereotypePropertyValues</a>, <a href="TagsHelper.html#isValidTagType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">isValidTagType</a>, <a href="TagsHelper.html#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)">removeTaggedValueValue</a>, <a href="TagsHelper.html#removeTaggedValueValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TaggedValue,java.lang.Object)">removeTaggedValueValue</a>, <a href="TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object)">setStereotypePropertyValue</a>, <a href="TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean)">setStereotypePropertyValue</a>, <a href="TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.lang.Object,boolean,boolean)">setStereotypePropertyValue</a>, <a href="TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object)">setStereotypePropertyValue</a>, <a href="TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean)">setStereotypePropertyValue</a>, <a href="TagsHelper.html#setStereotypePropertyValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,java.lang.Object,boolean,boolean)">setStereotypePropertyValue</a>, <a href="TagsHelper.html#setStereotypePropertyValueWithClearPredicate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,T,boolean,java.util.function.Predicate)">setStereotypePropertyValueWithClearPredicate</a></code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="UML2METAMODEL">
<h3>UML2METAMODEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML2METAMODEL</span></div>
<div class="block">Name of UML2 metamodel</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper.UML2METAMODEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UML2METAMODEL_URI">
<h3>UML2METAMODEL_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML2METAMODEL_URI</span></div>
<div class="block">URI of UML2 metamodel, must correspond UML standard profile metamodel uri.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper.UML2METAMODEL_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UML2METAMODEL_PRIMITIVE_TYPES">
<h3>UML2METAMODEL_PRIMITIVE_TYPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML2METAMODEL_PRIMITIVE_TYPES</span></div>
<div class="block">Name of primitives package in the UML2 metamodel</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper.UML2METAMODEL_PRIMITIVE_TYPES">Constant Field Values</a></li>
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
<h3>StereotypesHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StereotypesHelper</span>()</div>
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
<section class="detail" id="getAllProfiles(com.nomagic.magicdraw.core.Project)">
<h3>getAllProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</span> <span class="element-name">getAllProfiles</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns list of all loaded profiles. Returning writable copy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>list of all loaded profiles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfile(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getProfile</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">getProfile</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</span></div>
<div class="block">Returns profile element by name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>profileName</code> - profile name</dd>
<dt>Returns:</dt>
<dd>profile element or null if profile not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfileByURI(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getProfileByURI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">getProfileByURI</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileURI)</span></div>
<div class="block">Returns profile element by URI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>profileURI</code> - profile uri</dd>
<dt>Returns:</dt>
<dd>profile element or null if profile not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfiles(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</span> <span class="element-name">getProfiles</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</span></div>
<div class="block">Filters all given project profiles by name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - given project</dd>
<dd><code>profileName</code> - the profile name</dd>
<dt>Returns:</dt>
<dd>list of profiles that name corresponds to the given profile name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getStereotypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Returns all stereotypes applied to element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>applied stereotypes for this element or empty list if there are no applied stereotypes</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Checks if element has applied stereotypes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if it has applied stereotype</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Checks if element has applied stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype name to check</dd>
<dt>Returns:</dt>
<dd>true if element has applied stereotype</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Checks if element has applied at least one stereotype from given collection of Stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypes</code> - a collection of stereotypes</dd>
<dt>Returns:</dt>
<dd>true if element has applied at least one stereotype from the given collection</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>addStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Applies stereotype to a given element.
 The default tag values are not created, to create these values use <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)"><code>TagsHelper.createDefaultValues(Element, Stereotype, boolean)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype to apply</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype is null, or element is disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,int)">
<h3>addStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 int index)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Applies stereotype to a given element.
 The default tag values are not created, to create these values use <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)"><code>TagsHelper.createDefaultValues(Element, Stereotype, boolean)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype to apply</dd>
<dd><code>index</code> - index of the stereotype</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>addStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStereotypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Applies stereotypes from collection for specified element.
 The default tag values are not created, to create these values use <a href="TagsHelper.html#createDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)"><code>TagsHelper.createDefaultValues(Element, Stereotype, boolean)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element on which stereotypes are applied</dd>
<dd><code>stereotypes</code> - collection of <code>Stereotype</code> objects</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotypes is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>removeStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeStereotype</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Remove applied stereotype from element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype to remove</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotype is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeStereotypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Removes all applied stereotypes from element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>removeStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeStereotypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Removes all stereotypes from element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypes</code> - collection of stereotypes to remove</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element or stereotypes is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedStereotypeByString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getAppliedStereotypeByString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getAppliedStereotypeByString</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="block">Returns stereotype applied to element with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dt>Returns:</dt>
<dd>applied stereotype with that name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>getStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Returns stereotype for given name by profile.
 First search is performed directly in given profile and if no stereotype is found, then sub profiles are checked.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>stereotypeName</code> - name of stereotype</dd>
<dd><code>profile</code> - stereotype's profile, null if any</dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypedElementsIncludingDerived(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getStereotypedElementsIncludingDerived</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getStereotypedElementsIncludingDerived</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
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
<section class="detail" id="getStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getStereotypedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getStereotypedElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
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
<section class="detail" id="hasStereotypedElements(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>hasStereotypedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotypedElements</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Checks if stereotype has stereotyped elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype to check</dd>
<dt>Returns:</dt>
<dd>true if stereotype has stereotyped elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstStereotypeWithIcon(java.util.Collection)">
<h3>getFirstStereotypeWithIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFirstStereotypeWithIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; collectionOfStereotypes)</span></div>
<div class="block">Returns first stereotype with icon from given collection of stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collectionOfStereotypes</code> - a collection of stereotypes</dd>
<dt>Returns:</dt>
<dd>first stereotype with icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstStereotypeWithIcon(java.util.Collection,boolean)">
<h3>getFirstStereotypeWithIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFirstStereotypeWithIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; collectionOfStereotypes,
 boolean includeInvisible)</span></div>
<div class="block">Returns first stereotype with icon from given collection of stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collectionOfStereotypes</code> - a collection of stereotypes</dd>
<dd><code>includeInvisible</code> - indicates whether invisible stereotypes should be taken into account</dd>
<dt>Returns:</dt>
<dd>first stereotype with icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstVisibleStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getFirstVisibleStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFirstVisibleStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns first visible stereotype applied to given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>first visible stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstVisibleStereotype(java.util.Collection)">
<h3>getFirstVisibleStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFirstVisibleStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Returns first visible stereotype from given collection of stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - a collection of stereotypes.</dd>
<dt>Returns:</dt>
<dd>first visible stereotype.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllStereotypes(com.nomagic.magicdraw.core.Project)">
<h3>getAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAllStereotypes</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns collection of all stereotypes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of all stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findCommonAssignedStereotypes(java.util.Collection)">
<h3>findCommonAssignedStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">findCommonAssignedStereotypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Finds common applied stereotypes for list of collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of elements</dd>
<dt>Returns:</dt>
<dd>common stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllAssignedStereotypes(java.util.Collection)">
<h3>getAllAssignedStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAllAssignedStereotypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Returns all applied stereotypes for elements of collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of elements</dd>
<dt>Returns:</dt>
<dd>all applied stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getExtension</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></span> <span class="element-name">getExtension</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> baseClass)</span></div>
<div class="block">Checks if stereotype has baseClass as METACLASS</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>baseClass</code> - meta class</dd>
<dt>Returns:</dt>
<dd>extension for base class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensions(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getExtensions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a>&gt;</span> <span class="element-name">getExtensions</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> baseClass)</span></div>
<div class="block">Collects Extensions connected to this stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - Stereotype</dd>
<dd><code>baseClass</code> - Base class.</dd>
<dt>Returns:</dt>
<dd>List of extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensions(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,boolean)">
<h3>getExtensions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a>&gt;</span> <span class="element-name">getExtensions</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> baseClass,
 boolean takeInherited)</span></div>
<div class="block">Get Extension Meta Property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - Stereotype</dd>
<dd><code>baseClass</code> - Base class.</dd>
<dd><code>takeInherited</code> - collect inherited extension ends also</dd>
<dt>Returns:</dt>
<dd>List of extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getBaseClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getBaseClasses</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns all base (meta) classes for stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>collection(Class) of base (meta) classes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">
<h3>getBaseClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getBaseClasses</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean includeFromParentStereotypes)</span></div>
<div class="block">Returns all base (meta) classes for stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>includeFromParentStereotypes</code> - also take bases classes from parent stereotypes</dd>
<dt>Returns:</dt>
<dd>collection(Class) of base (meta) classes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSettableStereotypes(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">
<h3>getSettableStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getSettableStereotypes</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementType,
 boolean includeSuperTypes)</span></div>
<div class="block">Returns collection of settable stereotypes for element type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>elementType</code> - element type</dd>
<dd><code>includeSuperTypes</code> - include super types also</dd>
<dt>Returns:</dt>
<dd>collection of settable stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSettableStereotypes(com.nomagic.magicdraw.core.Project,java.util.Collection,boolean)">
<h3>getSettableStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getSettableStereotypes</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean includeSuperTypes)</span></div>
<div class="block">Returns collection of settable stereotypes for collection of elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>elements</code> - collection of elements</dd>
<dd><code>includeSuperTypes</code> - include super types also</dd>
<dt>Returns:</dt>
<dd>collection of settable stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUML2MetaModel(com.nomagic.magicdraw.core.Project)">
<h3>getUML2MetaModel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">getUML2MetaModel</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns model element for UML2 meta model</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>model element for UML2 meta model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBuiltInUML2Metamodel(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model)">
<h3>isBuiltInUML2Metamodel</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBuiltInUML2Metamodel</span><wbr/><span class="parameters">(<a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a> model)</span></div>
<div class="block">Checks if given model is built in (not user modeled) UML metamodel. Built in metamodel is loaded from standard profile.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>model</code> - model to check</dd>
<dt>Returns:</dt>
<dd>true if model is built in uml model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllMetaModels(com.nomagic.magicdraw.core.Project)">
<h3>getAllMetaModels</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt;</span> <span class="element-name">getAllMetaModels</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns collection of all model elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of all model elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaModelByName(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getMetaModelByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">getMetaModelByName</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Return metamodel with specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search for metamodel.</dd>
<dd><code>name</code> - name    metamodel name.</dd>
<dt>Returns:</dt>
<dd>metamodel with specified name. <code>null</code> if not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllMetaClasses(com.nomagic.magicdraw.core.Project)">
<h3>getAllMetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getAllMetaClasses</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns collection of all metamodel classes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of all meta model classes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUML2MetaClasses(com.nomagic.magicdraw.core.Project)">
<h3>getUML2MetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getUML2MetaClasses</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns collection of all UML2 metaclasses</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of all UML2 metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClasses(java.util.Collection)">
<h3>getMetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getMetaClasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt; models)</span></div>
<div class="block">Returns metaclasses by collection of models</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>models</code> - collection of models</dd>
<dt>Returns:</dt>
<dd>collection(Class) of meta classes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNamesOfMetaClasses(java.util.Collection)">
<h3>getNamesOfMetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNamesOfMetaClasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt; models)</span></div>
<div class="block">Returns names of metaclasses by collection of models</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>models</code> - collection of models</dd>
<dt>Returns:</dt>
<dd>collection(String) of metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassByName(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getMetaClassByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getMetaClassByName</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns metaclass by name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - name of metaclass</dd>
<dt>Returns:</dt>
<dd>Class element of metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassByName(java.lang.String,java.util.Collection)">
<h3>getMetaClassByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getMetaClassByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a>&gt; models)</span></div>
<div class="block">Returns metaclass by name from collection of models</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of metaclass</dd>
<dd><code>models</code> - collection of models to look for</dd>
<dt>Returns:</dt>
<dd>Class element of metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassesFromPackageByName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">
<h3>getMetaClassesFromPackageByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getMetaClassesFromPackageByName</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Search for class in given scope(package) by class name.
 Search is using query.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - Package instance.</dd>
<dd><code>name</code> - Class name</dd>
<dt>Returns:</dt>
<dd>UML Class or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUML2MetaClassByName(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getUML2MetaClassByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getUML2MetaClassByName</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">/**
 Returns meta class from UML2 meta model by name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - given project</dd>
<dd><code>name</code> - name of metaclass</dd>
<dt>Returns:</dt>
<dd>Class element of metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaModelByMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getMetaModelByMetaClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">getMetaModelByMetaClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</span></div>
<div class="block">Returns meta model of specified meta class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metaClass</code> - meta class</dd>
<dt>Returns:</dt>
<dd>metamodel of metaclass. <code>null</code>  if <code>c</code> is not metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaModelByElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getMetaModelByElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">getMetaModelByElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns metamodel of specified element in the metamodel. Method is expanded to support
 enumerations and literals from model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - metaclass or other meta element.</dd>
<dt>Returns:</dt>
<dd>metamodel of metaclass. <code>null</code> if <code>element</code> is not metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMetaClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Checks if given element is a metaclass, including user defined metaclasses. For pure uml metaclass use <a href="#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)"><code>isUML2MetaClass(Class)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - class</dd>
<dt>Returns:</dt>
<dd>true if element is metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>isMetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMetaClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> aClass)</span></div>
<div class="block">Checks if Class is metaclass, including user defined metaclasses. For pure uml metaclass use <a href="#isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)"><code>isUML2MetaClass(Class)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aClass</code> - class</dd>
<dt>Returns:</dt>
<dd>true if Class is metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUML2MetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>isUML2MetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUML2MetaClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> aClass)</span></div>
<div class="block">Checks if Class is metaclass, and this metaclass represents currently instantiated UML model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aClass</code> - class</dd>
<dt>Returns:</dt>
<dd>true if Class is uml 2  metaclass.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBaseClassesByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection)">
<h3>setBaseClassesByName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setBaseClassesByName</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; metaClasses)</span></div>
<div class="block">Sets base (meta) classes for stereotype by names</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>metaClasses</code> - collection of metaclasses names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBaseClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection)">
<h3>setBaseClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setBaseClasses</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</span></div>
<div class="block">Sets base (meta) classes for stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>metaClasses</code> - collection of metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBaseClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">
<h3>setBaseClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></span> <span class="element-name">setBaseClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</span></div>
<div class="block">Sets base (meta) class for stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>metaClass</code> - meta class</dd>
<dd><code>extension</code> - extension for class and stereotype</dd>
<dt>Returns:</dt>
<dd>created Extension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeBaseClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>removeBaseClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeBaseClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</span></div>
<div class="block">removes base (meta) class for stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>metaClass</code> - meta class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.util.Collection)">
<h3>createStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">createStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</span></div>
<div class="block">Creates stereotype instance and sets base classes for it</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - owner of stereotype</dd>
<dd><code>name</code> - name of stereotype</dd>
<dd><code>metaClasses</code> - meta classes for stereotype</dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotype(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection)">
<h3>createStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">createStereotype</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</span></div>
<div class="block">Creates stereotype instance and sets base classes for it</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - name of stereotype</dd>
<dd><code>metaClasses</code> - meta classes for stereotype</dd>
<dt>Returns:</dt>
<dd>created stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultMetaClasses(com.nomagic.magicdraw.core.Project)">
<h3>getDefaultMetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getDefaultMetaClasses</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Dummy procedure for setting of metaclasses</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>default meta class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNamesOfSuperClasses(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getNamesOfSuperClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNamesOfSuperClasses</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> aClass)</span></div>
<div class="block">Returns names of supper classes for metaclass</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aClass</code> - meta class UML class</dd>
<dt>Returns:</dt>
<dd>collection of names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canApplyStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>canApplyStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canApplyStereotype</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Checks if stereotype can be applied to element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>true if stereotype can be applied to element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns ICON from stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deriveStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>deriveStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">deriveStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> parent,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> child)</span></div>
<div class="block">Derives stereotype from other stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent stereotype</dd>
<dd><code>child</code> - child stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassByClass(com.nomagic.magicdraw.core.Project,java.lang.Class)">
<h3>getMetaClassByClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getMetaClassByClass</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz)</span></div>
<div class="block">Returns metaclass by given class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>clazz</code> - class from which to get name from</dd>
<dt>Returns:</dt>
<dd>meta class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassesByClass(com.nomagic.magicdraw.core.Project,java.util.Collection)">
<h3>getMetaClassesByClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getMetaClassesByClass</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt; classes)</span></div>
<div class="block">Returns names of metaclasses from collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>classes</code> - collection of metaclasses to get names from</dd>
<dt>Returns:</dt>
<dd>collection of names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getBaseClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getBaseClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns metaclass of given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>Class element of metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUML2BaseClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUML2BaseClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getUML2BaseClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns UML2 metamodel metaclass for a given Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>Class element of metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUML2BaseClassByJavaClass(com.nomagic.magicdraw.core.Project,java.lang.Class)">
<h3>getUML2BaseClassByJavaClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getUML2BaseClassByJavaClass</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> javaClass)</span></div>
<div class="block">Returns UML2 metamodel metaclass for a given Java class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>javaClass</code> - given Java Class</dd>
<dt>Returns:</dt>
<dd>Class element of metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseClassesAsClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getBaseClassesAsClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">getBaseClassesAsClasses</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns collection(java.lang.Class) of metaclasses from stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>collection of metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAssignStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>canAssignStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAssignStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Indicates if stereotype can be applied to a given element.
 <p>
 - checks if stereotype metaclass fits class of an element.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to which stereotype should be applied.</dd>
<dd><code>stereotype</code> - stereotype to assign.</dd>
<dt>Returns:</dt>
<dd>true if stereotype can be applied, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInvisible(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement)">
<h3>isInvisible</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInvisible</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a> element)</span></div>
<div class="block">Check is element is invisible (has Invisible stereotype or one of its children)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element is invisible</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype()"><code>MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canApplyProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>canApplyProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canApplyProfile</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Checks profile can apply to package.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - The given package.</dd>
<dd><code>profile</code> - The given profile.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>applyProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">applyProfile</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Applies profile to the package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - package</dd>
<dd><code>profile</code> - profile to apply</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>removeProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeProfile</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Removes profile application from the package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - package</dd>
<dd><code>profile</code> - applied profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypesByProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>getStereotypesByProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getStereotypesByProfile</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Returns collection of stereotypes by profile</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>profile</code> - profile</dd>
<dt>Returns:</dt>
<dd>collection of stereotypes by profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequiredStereotypeForElement(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRequiredStereotypeForElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequiredStereotypeForElement</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Checks if stereotype is required for element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if stereotype is required for element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassOfMetaClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getClassOfMetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></span> <span class="element-name">getClassOfMetaClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> metaClass)</span></div>
<div class="block">Returns java.lang.Class for metaclass by Class</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metaClass</code> - meta class</dd>
<dt>Returns:</dt>
<dd>java.lang.Class for metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection)">
<h3>applyProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">applyProfiles</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt; profiles)</span></div>
<div class="block">Applies profiles from collection to specified package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - package</dd>
<dd><code>profiles</code> - list of profiles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection)">
<h3>removeProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeProfiles</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt; profiles)</span></div>
<div class="block">Removes applied profiles in package from collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - package</dd>
<dd><code>profiles</code> - collection of profiles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAppliedProfiles(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>getAppliedProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</span> <span class="element-name">getAppliedProfiles</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg)</span></div>
<div class="block">Returns collection of applied profiles on package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - package</dd>
<dt>Returns:</dt>
<dd>collection of applied profiles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canRemoveProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>canRemoveProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canRemoveProfile</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Checks if it is possible to remove applied profile from package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pkg</code> - package</dd>
<dd><code>profile</code> - profile</dd>
<dt>Returns:</dt>
<dd>true if it is possible to remove applied profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependingProfiles(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>getDependingProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a>&gt;</span> <span class="element-name">getDependingProfiles</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> profile)</span></div>
<div class="block">Returns collection of profiles depending on given profile</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>profile</code> - profile</dd>
<dt>Returns:</dt>
<dd>collection of profiles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkForDerivedStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>checkForDerivedStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">checkForDerivedStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Checks if the given stereotype, or it's child is already applied to the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>given stereotype or it's child applied to element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkForDerivedStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>checkForDerivedStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">checkForDerivedStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Checks if there are child of at least one given stereotype already set to given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypes</code> - a collection of stereotypes to check</dd>
<dt>Returns:</dt>
<dd>stereotype or child of stereotype applied to element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkForDerivedStereotype(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>checkForDerivedStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">checkForDerivedStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> parent)</span></div>
<div class="block">Checks if there are given stereotype or derived stereotype in a given stereotypes collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - collection of stereotypes to look in</dd>
<dd><code>parent</code> - parent stereotype</dd>
<dt>Returns:</dt>
<dd>returns stereotype which equals to the given or is derived</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDerivedStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">
<h3>getDerivedStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getDerivedStereotypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> parent,
 boolean includeParent)</span></div>
<div class="block">Returns applied derived stereotypes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>parent</code> - stereotype</dd>
<dd><code>includeParent</code> - true if include parent stereotype in collection</dd>
<dt>Returns:</dt>
<dd>stereotype or child of stereotype for element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>hasStereotypeOrDerived</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotypeOrDerived</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Checks if there are child of parent stereotype already set</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>true if at least one child of parent is set for element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotypeOrDerived(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>hasStereotypeOrDerived</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotypeOrDerived</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Checks if element has applied at least one stereotype(or derived) from given collection of Stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dd><code>stereotypes</code> - a collection of stereotypes</dd>
<dt>Returns:</dt>
<dd>true if element has applied at least one stereotype from given collection</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if element is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypesByMetaClasses(java.util.Collection)">
<h3>getStereotypesByMetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getStereotypesByMetaClasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt; metaClasses)</span></div>
<div class="block">Collects stereotypes which extend given metaclasses.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metaClasses</code> - meta classes</dd>
<dt>Returns:</dt>
<dd>stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">
<h3>getExtensionEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></span> <span class="element-name">getExtensionEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</span></div>
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
<section class="detail" id="assignImageFilesToStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.util.Collection)">
<h3>assignImageFilesToStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">assignImageFilesToStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; files)</span></div>
<div class="block">Assigns given image files to stereotype as icons.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype to which icons should be applied</dd>
<dd><code>files</code> - image files to assign</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDerivedStereotypesRecursively(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getDerivedStereotypesRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getDerivedStereotypesRecursively</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns derived stereotypes recursively</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype for which to return derived stereotypes</dd>
<dt>Returns:</dt>
<dd>list of derived stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsRequiresExtension(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">
<h3>getElementsRequiresExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElementsRequiresExtension</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> extension)</span></div>
<div class="block">Checks which stereotyped elements requires this extension (it provides base class for stereotyped element).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extension</code> - extension to check.</dd>
<dt>Returns:</dt>
<dd>elements which uses given extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssignedMetaClassOfSubtype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getAssignedMetaClassOfSubtype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getAssignedMetaClassOfSubtype</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> meta)</span></div>
<div class="block">Collect all subtypes of given metaclasses whose are extended by a given stereotype</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>meta</code> - meta class</dd>
<dt>Returns:</dt>
<dd>meta classes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSuperMetaClass(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>hasSuperMetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasSuperMetaClass</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> meta)</span></div>
<div class="block">Checks if stereotype has super metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>meta</code> - meta class</dd>
<dt>Returns:</dt>
<dd>true if stereotype has super metaclass.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSuperMetaClasses(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>removeSuperMetaClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeSuperMetaClasses</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> meta)</span></div>
<div class="block">Remove super metaclass from the given stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dd><code>meta</code> - meta class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExtensionProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>isExtensionProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExtensionProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property</dd>
<dt>Returns:</dt>
<dd>true if given property is memberEnd of Extension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfileForStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getProfileForStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getProfileForStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns profile for a given stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>profile where given stereotype is defined. If it has profile parent it is defined in profile, in other case parent package will be return.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionMetaProperty(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getExtensionMetaProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getExtensionMetaProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Collects properties of MetaClass extension end</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype to check for metaclasses</dd>
<dt>Returns:</dt>
<dd>collection of properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionMetaProperty(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,boolean)">
<h3>getExtensionMetaProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getExtensionMetaProperty</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 boolean includeInherited)</span></div>
<div class="block">Collects properties of MetaClass extension end</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - stereotype to check for metaclasses</dd>
<dd><code>includeInherited</code> - collection inherited meta properties</dd>
<dt>Returns:</dt>
<dd>collection of properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFromPrimitiveTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFromPrimitiveTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFromPrimitiveTypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Checks if given element is from UML2 metamodel primitive types package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dt>Returns:</dt>
<dd>true, if given element is from primitive types package.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimitiveTypesPackage(com.nomagic.magicdraw.core.Project)">
<h3>getPrimitiveTypesPackage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getPrimitiveTypesPackage</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns primitive types package of UML2 metamodel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dt>Returns:</dt>
<dd>primitive types package.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimitiveByName(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getPrimitiveByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></span> <span class="element-name">getPrimitiveByName</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Finds primitiveType by name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project where find primitive.</dd>
<dd><code>name</code> - primitive name.</dd>
<dt>Returns:</dt>
<dd>Primitive with given name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasVisibleStereotype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasVisibleStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasVisibleStereotype</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element has at least one visible stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>true if visible stereotype is applied to the given element</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype()"><code>MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterVisibleStereotypes(java.util.Collection)">
<h3>filterVisibleStereotypes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">filterVisibleStereotypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Filter stereotypes from given collection whose are "visible". Stereotype is visible if it is not derived from &lt;<invisiblestereotype>&gt;</invisiblestereotype></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - collection of stereotypes</dd>
<dt>Returns:</dt>
<dd>new collection of visible stereotypes</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype()"><code>MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterVisibleElement(java.util.Collection)">
<h3>filterVisibleElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">filterVisibleElement</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Filter elements from given collection whose are "visible". Element is visible if it does not have applied stereotype &lt;<invisiblestereotype>&gt;</invisiblestereotype></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of elements</dd>
<dt>Returns:</dt>
<dd>new collection of visible elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../MagicDrawProfile.InvisibleStereotypeStereotype.html#getStereotype()"><code>MagicDrawProfile.InvisibleStereotypeStereotype.getStereotype()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="optimizeStereotypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>optimizeStereotypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">optimizeStereotypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Optimize applied stereotypes to an Element by removing more general stereotypes if more specific are applied.
 This rule is applied only for stereotypes whose "hideMetatype" in DSL configuration</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; typesCollection,
 boolean includeInherited)</span></div>
<div class="block">Checks if element is of type from typesCollection. 3 scenarios can be tested
 1. Element is of specified type or inherited
 2. Element has applied stereotype or inherited stereotype
 3. InstanceSpecification has Classifier instance or inherited .</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - instance that type will be checked.</dd>
<dd><code>typesCollection</code> - collection of types used to check if element type is part of it</dd>
<dd><code>includeInherited</code> - if set to true all element type hierarchy will be checked against typesCollection</dd>
<dt>Returns:</dt>
<dd>true if element is of type from typesCollection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean,boolean)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; typesCollection,
 boolean includeInherited,
 boolean includeCustomTypes)</span></div>
<div class="block">Checks if element is of type from typesCollection. 3 scenarios can be tested
 1. Element is of specified type or inherited
 2. Element has applied stereotype or inherited stereotype
 3. InstanceSpecification has Classifier instance or inherited .</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - instance that type will be checked</dd>
<dd><code>typesCollection</code> - collection of types used to check if element type is part of it</dd>
<dd><code>includeInherited</code> - if set to true all element type hierarchy will be checked against typesCollection</dd>
<dd><code>includeCustomTypes</code> - check against custom types</dd>
<dt>Returns:</dt>
<dd>true if element is of type from typesCollection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeClasses(java.util.Collection)">
<h3>getTypeClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getTypeClasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementTypes)</span></div>
<div class="block">Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementTypes</code> - MetaType classes and stereotypes</dd>
<dt>Returns:</dt>
<dd>java.lang.Class objects and stereotypes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeClasses(java.util.Collection,boolean,boolean)">
<h3>getTypeClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getTypeClasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementTypes,
 boolean includeSubtypes,
 boolean expandAbstract)</span></div>
<div class="block">Converts Meta Class elements to java.lang.Class objects, stereotypes are left unchanged.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementTypes</code> - MetaType classes and stereotypes</dd>
<dd><code>includeSubtypes</code> - if true derived stereotypes and metaClasses will be collected.</dd>
<dd><code>expandAbstract</code> - if true and abstract metaClasses subtypes will be collected.</dd>
<dt>Returns:</dt>
<dd>java.lang.Class objects and stereotypes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,boolean)">
<h3>isOfType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOfType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt; metaTypes,
 boolean checkDSL)</span></div>
<div class="block">Checks if element is of type from given meta-types</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - instance that type will be checked</dd>
<dd><code>metaTypes</code> - meta types</dd>
<dd><code>checkDSL</code> - take DSL rules into account</dd>
<dt>Returns:</dt>
<dd>true if element is of type from typesCollection</dd>
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
