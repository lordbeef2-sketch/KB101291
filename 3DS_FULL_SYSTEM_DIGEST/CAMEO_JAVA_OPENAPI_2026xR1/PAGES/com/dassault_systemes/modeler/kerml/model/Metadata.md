# JAVA OPENAPI: Metadata (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Metadata.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Metadata.html`
- source_sha256: `b0d42873b92327aeacb007069cd32d57d877ff00fa968459f64a5ad3aa50edc4`
- captured_utc: `2026-07-14T16:44:47.991843+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Metadata

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Metadata

@OpenApiAllpublic classMetadata
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`MetadataFeature`](kerml/MetadataFeature.html) or [`Metaclass`](kerml/Metaclass.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Metadata](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[createMetadata](#createMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Namespace](kerml/Namespace.html) owner,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Creates metadata inside given [`Namespace`](kerml/Namespace.html) and applies it for a given [`Element`](kerml/Element.html)
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[createOwnedMetadata](#createOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Creates and applies owned metadata for a given [`Element`](kerml/Element.html)
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)>`
`[getAnnotatedElementTypes](#getAnnotatedElementTypes(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature))([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)`
Returns the annotated element types for the given metadata feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)>`
`[getBaseTypes](#getBaseTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) target)`
Returns base types associated with metadata applied to the given type.
`static org.eclipse.emf.ecore.EClass`
`[getEClassFor](#getEClassFor(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Metaclass](kerml/Metaclass.html) metaclass)`
Returns the EClass corresponding to the given metaclass.
`static org.eclipse.emf.ecore.EClass`
`[getEClassIfSelfMetadata](#getEClassIfSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature))([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)`
Returns the EClass of the syntax element for self metadata.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)>`
`[getMetaclassesOfMetadata](#getMetaclassesOfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns metaclasses of all metadata applied to the element.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)>`
`[getMetaclassesOfOwnedMetadata](#getMetaclassesOfOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns metaclasses of owned metadata applied to the element.
`static [Metaclass](kerml/Metaclass.html)`
`[getMetaClassFor](#getMetaClassFor(com.dassault_systemes.modeler.foundation.project.ModelElementProject,org.eclipse.emf.ecore.EClass))([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 org.eclipse.emf.ecore.EClass eClass)`
Returns the metaclass corresponding to the given EClass.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMetaclassName](#getMetaclassName(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Metaclass](kerml/Metaclass.html) metaclass)`
Returns the name of the given metaclass.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMetaclassName](#getMetaclassName(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature))([MetadataFeature](kerml/MetadataFeature.html) feature)`
Returns the name of the metaclass of the given metadata feature.
`static [Metaclass](kerml/Metaclass.html)`
`[getMetaClassOf](#getMetaClassOf(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the metaclass of the given element.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)>`
`[getMetadata](#getMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns all metadata applied to the given [`Element`](kerml/Element.html).
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[getMetadata](#getMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Returns metadata applied to the element matching the given metaclass.
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[getMetadata](#getMetadata(java.util.Collection,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Returns metadata from the given collection matching the given metaclass.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)>`
`[getMetadataWithSelf](#getMetadataWithSelf(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns all metadata applied to the given [`Element`](kerml/Element.html) including also "self" metadata.
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[getOrCreateOwnedMetadata](#getOrCreateOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Looks for owned metadata matching given metaclass or creates and applies a new one.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)>`
`[getOwnedMetadata](#getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns owned metadata applied to the given [`Element`](kerml/Element.html).
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[getOwnedMetadata](#getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Returns owned metadata applied to the element matching the given metaclass.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)>`
`[getOwnedSemanticMetadata](#getOwnedSemanticMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns semantic metadata applied to the given [`Element`](kerml/Element.html).
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[getSelfMetadata](#getSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the self metadata feature of the element, if any.
`static boolean`
`[isAnnotatedWithOwnedMetadata](#isAnnotatedWithOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Checks whether the element is annotated with owned metadata of the given metaclass.
`static boolean`
`[isApplicable](#isApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether metadata is applicable to the given element.
`static boolean`
`[isInstanceOfMetamodelMetaclass](#isInstanceOfMetamodelMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)`
Checks whether the element is an instance of the given metamodel metaclass.
`static boolean`
`[isInstanceOfMetamodelMetaclass](#isInstanceOfMetamodelMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Collection))([Element](kerml/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Metaclass](kerml/Metaclass.html)> metaclasses)`
Checks whether the element is an instance of the given metamodel metaclasses.
`static boolean`
`[isMetamodelFeature](#isMetamodelFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the given feature is a metamodel feature.
`static boolean`
`[isSelfMetadata](#isSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature))([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)`
Checks whether the given metadata feature is self metadata.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)>`
`[mapMetadataToMetaclasses](#mapMetadataToMetaclasses(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadataFeatures)`
Maps metadata features to their metaclasses.
`static void`
`[setOwnedMetadata](#setOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Collection,boolean))([Element](kerml/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Metaclass](kerml/Metaclass.html)> metaclasses,
 boolean disposeNotMatching)`
Sets owned metadata of [`Element`](kerml/Element.html) matching given metaclasses.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)>`
`[toClassifiers](#toClassifiers(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> baseType)`
Converts base types to classifiers by expanding feature types.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)>`
`[toFeatures](#toFeatures(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> baseType)`
Filters the given list of types to only those that are features.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Metadata
public Metadata()
 ============ METHOD DETAIL ========== 
Method Details
getOwnedSemanticMetadata
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)> getOwnedSemanticMetadata([Element](kerml/Element.html) element)
Returns semantic metadata applied to the given [`Element`](kerml/Element.html).
Parameters:
`element` - element
Returns:
semantic metadata
getMetadata
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)> getMetadata([Element](kerml/Element.html) element)
Returns all metadata applied to the given [`Element`](kerml/Element.html).
Parameters:
`element` - element
Returns:
metadata
getMetadataWithSelf
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)> getMetadataWithSelf([Element](kerml/Element.html) element)
Returns all metadata applied to the given [`Element`](kerml/Element.html) including also "self" metadata.
Parameters:
`element` - element
Returns:
metadata
getOwnedMetadata
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)> getOwnedMetadata([Element](kerml/Element.html) element)
Returns owned metadata applied to the given [`Element`](kerml/Element.html).
Parameters:
`element` - element
Returns:
metadata
createOwnedMetadata
public static [MetadataFeature](kerml/MetadataFeature.html) createOwnedMetadata([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)
Creates and applies owned metadata for a given [`Element`](kerml/Element.html)
Parameters:
`element` - element
`metaclass` - metaclass of metadata to apply
Returns:
created metadata
createMetadata
public static [MetadataFeature](kerml/MetadataFeature.html) createMetadata([Element](kerml/Element.html) element,
 [Namespace](kerml/Namespace.html) owner,
 [Metaclass](kerml/Metaclass.html) metaclass)
Creates metadata inside given [`Namespace`](kerml/Namespace.html) and applies it for a given [`Element`](kerml/Element.html)
Parameters:
`element` - element
`owner` - owner of created metadata
`metaclass` - metaclass of metadata to apply
Returns:
created metadata
getOrCreateOwnedMetadata
public static [MetadataFeature](kerml/MetadataFeature.html) getOrCreateOwnedMetadata([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)
Looks for owned metadata matching given metaclass or creates and applies a new one.
Parameters:
`element` - element
`metaclass` - metaclass of metadata to apply
Returns:
metadata
See Also:
[`createOwnedMetadata(Element, Metaclass)`](#createOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass))
getMetadata
@CheckForNullpublic static [MetadataFeature](kerml/MetadataFeature.html) getMetadata([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)
Returns metadata applied to the element matching the given metaclass.
Parameters:
`element` - element
`metaclass` - metaclass to match
Returns:
matching metadata, or null
getOwnedMetadata
@CheckForNullpublic static [MetadataFeature](kerml/MetadataFeature.html) getOwnedMetadata([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)
Returns owned metadata applied to the element matching the given metaclass.
Parameters:
`element` - element
`metaclass` - metaclass to match
Returns:
matching metadata, or null
getMetadata
@CheckForNullpublic static [MetadataFeature](kerml/MetadataFeature.html) getMetadata([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata,
 [Metaclass](kerml/Metaclass.html) metaclass)
Returns metadata from the given collection matching the given metaclass.
Parameters:
`metadata` - metadata collection
`metaclass` - metaclass to match
Returns:
matching metadata, or null
setOwnedMetadata
public static void setOwnedMetadata([Element](kerml/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Metaclass](kerml/Metaclass.html)> metaclasses,
 boolean disposeNotMatching)
Sets owned metadata of [`Element`](kerml/Element.html) matching given metaclasses.
Parameters:
`element` - element
`metaclasses` - metaclasses
`disposeNotMatching` - disposes existing owned metadata not matching given metaclasses
getMetaclassesOfOwnedMetadata
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)> getMetaclassesOfOwnedMetadata([Element](kerml/Element.html) element)
Returns metaclasses of owned metadata applied to the element.
Parameters:
`element` - element
Returns:
list of metaclasses
getMetaclassesOfMetadata
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)> getMetaclassesOfMetadata([Element](kerml/Element.html) element)
Returns metaclasses of all metadata applied to the element.
Parameters:
`element` - element
Returns:
list of metaclasses
mapMetadataToMetaclasses
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)> mapMetadataToMetaclasses([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadataFeatures)
Maps metadata features to their metaclasses.
Parameters:
`metadataFeatures` - metadata features
Returns:
list of metaclasses
getAnnotatedElementTypes
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Metaclass](kerml/Metaclass.html)> getAnnotatedElementTypes([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)
Returns the annotated element types for the given metadata feature.
Parameters:
`metadataFeature` - metadata feature
Returns:
list of annotated element types
getBaseTypes
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> getBaseTypes([Type](kerml/Type.html) target)
Returns base types associated with metadata applied to the given type.
Parameters:
`target` - type
Returns:
list of base types
toClassifiers
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> toClassifiers([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> baseType)
Converts base types to classifiers by expanding feature types.
Parameters:
`baseType` - list of types
Returns:
list of classifier types
toFeatures
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> toFeatures([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> baseType)
Filters the given list of types to only those that are features.
Parameters:
`baseType` - list of types
Returns:
list containing only feature types
getMetaclassName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMetaclassName([MetadataFeature](kerml/MetadataFeature.html) feature)
Returns the name of the metaclass of the given metadata feature.
Parameters:
`feature` - metadata feature
Returns:
metaclass name, or null
getMetaclassName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMetaclassName([Metaclass](kerml/Metaclass.html) metaclass)
Returns the name of the given metaclass.
Parameters:
`metaclass` - metaclass
Returns:
short name or name, or null
isApplicable
public static boolean isApplicable([Element](kerml/Element.html) element)
Checks whether metadata is applicable to the given element.
Parameters:
`element` - element
Returns:
true if metadata can be applied
getSelfMetadata
@CheckForNullpublic static [MetadataFeature](kerml/MetadataFeature.html) getSelfMetadata([Element](kerml/Element.html) element)
Returns the self metadata feature of the element, if any.
Parameters:
`element` - element
Returns:
self metadata, or null
isSelfMetadata
public static boolean isSelfMetadata([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)
Checks whether the given metadata feature is self metadata.
Parameters:
`metadataFeature` - metadata feature
Returns:
true if it is self metadata
getEClassIfSelfMetadata
@CheckForNullpublic static org.eclipse.emf.ecore.EClass getEClassIfSelfMetadata([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)
Returns the EClass of the syntax element for self metadata.
Parameters:
`metadataFeature` - metadata feature
Returns:
EClass of syntax element, or null
getMetaClassOf
@CheckForNullpublic static [Metaclass](kerml/Metaclass.html) getMetaClassOf([Element](kerml/Element.html) element)
Returns the metaclass of the given element.
Parameters:
`element` - element
Returns:
metaclass, or null
getMetaClassFor
@CheckForNullpublic static [Metaclass](kerml/Metaclass.html) getMetaClassFor([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 org.eclipse.emf.ecore.EClass eClass)
Returns the metaclass corresponding to the given EClass.
Parameters:
`project` - project
`eClass` - EClass
Returns:
metaclass, or null
getEClassFor
@CheckForNullpublic static org.eclipse.emf.ecore.EClass getEClassFor([Metaclass](kerml/Metaclass.html) metaclass)
Returns the EClass corresponding to the given metaclass.
Parameters:
`metaclass` - metaclass
Returns:
EClass, or null
isMetamodelFeature
public static boolean isMetamodelFeature([Feature](kerml/Feature.html) feature)
Checks whether the given feature is a metamodel feature.
Parameters:
`feature` - feature
Returns:
true if the feature belongs to a metaclass with a resolvable EClass
isAnnotatedWithOwnedMetadata
public static boolean isAnnotatedWithOwnedMetadata([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)
Checks whether the element is annotated with owned metadata of the given metaclass.
Parameters:
`element` - element
`metaclass` - metaclass
Returns:
true if matching owned metadata exists
isInstanceOfMetamodelMetaclass
public static boolean isInstanceOfMetamodelMetaclass([Element](kerml/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Metaclass](kerml/Metaclass.html)> metaclasses)
Checks whether the element is an instance of the given metamodel metaclasses.
Parameters:
`element` - element
`metaclasses` - metaclasses
Returns:
true if the element matches any metaclass
isInstanceOfMetamodelMetaclass
public static boolean isInstanceOfMetamodelMetaclass([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass)
Checks whether the element is an instance of the given metamodel metaclass.
Parameters:
`element` - element
`metaclass` - metaclass
Returns:
true if the element matches the metaclass

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Metadata">Class Metadata</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Metadata</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Metadata</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a> or <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Metaclass</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Metadata</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">createMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> owner,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates metadata inside given <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a> and applies it for a given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">createOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates and applies owned metadata for a given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotatedElementTypes(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">getAnnotatedElementTypes</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the annotated element types for the given metadata feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getBaseTypes</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns base types associated with metadata applied to the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEClassFor(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">getEClassFor</a><wbr/>(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the EClass corresponding to the given metaclass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEClassIfSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">getEClassIfSelfMetadata</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the EClass of the syntax element for self metadata.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaclassesOfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getMetaclassesOfMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclasses of all metadata applied to the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaclassesOfOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getMetaclassesOfOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metaclasses of owned metadata applied to the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassFor(com.dassault_systemes.modeler.foundation.project.ModelElementProject,org.eclipse.emf.ecore.EClass)">getMetaClassFor</a><wbr/>(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the metaclass corresponding to the given EClass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaclassName(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">getMetaclassName</a><wbr/>(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the name of the given metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaclassName(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">getMetaclassName</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the name of the metaclass of the given metadata feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaClassOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getMetaClassOf</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the metaclass of the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">getMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metadata applied to the element matching the given metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadata(java.util.Collection,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">getMetadata</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns metadata from the given collection matching the given metaclass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadataWithSelf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getMetadataWithSelf</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a> including also "self" metadata.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">getOrCreateOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for owned metadata matching given metaclass or creates and applies a new one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns owned metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">getOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns owned metadata applied to the element matching the given metaclass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedSemanticMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getOwnedSemanticMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns semantic metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getSelfMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the self metadata feature of the element, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAnnotatedWithOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">isAnnotatedWithOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is annotated with owned metadata of the given metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isApplicable</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether metadata is applicable to the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstanceOfMetamodelMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">isInstanceOfMetamodelMetaclass</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is an instance of the given metamodel metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstanceOfMetamodelMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Collection)">isInstanceOfMetamodelMetaclass</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt; metaclasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is an instance of the given metamodel metaclasses.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMetamodelFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isMetamodelFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a metamodel feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">isSelfMetadata</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given metadata feature is self metadata.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mapMetadataToMetaclasses(java.util.List)">mapMetadataToMetaclasses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadataFeatures)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Maps metadata features to their metaclasses.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Collection,boolean)">setOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt; metaclasses,
 boolean disposeNotMatching)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets owned metadata of <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a> matching given metaclasses.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toClassifiers(java.util.List)">toClassifiers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; baseType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts base types to classifiers by expanding feature types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toFeatures(java.util.List)">toFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; baseType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters the given list of types to only those that are features.</div>
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
<h3>Metadata</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Metadata</span>()</div>
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
<section class="detail" id="getOwnedSemanticMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getOwnedSemanticMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</span> <span class="element-name">getOwnedSemanticMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns semantic metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>semantic metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</span> <span class="element-name">getMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns all metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadataWithSelf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getMetadataWithSelf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</span> <span class="element-name">getMetadataWithSelf</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns all metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a> including also "self" metadata.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</span> <span class="element-name">getOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns owned metadata applied to the given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>createOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">createOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Creates and applies owned metadata for a given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass of metadata to apply</dd>
<dt>Returns:</dt>
<dd>created metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>createMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">createMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> owner,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Creates metadata inside given <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a> and applies it for a given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>owner</code> - owner of created metadata</dd>
<dd><code>metaclass</code> - metaclass of metadata to apply</dd>
<dt>Returns:</dt>
<dd>created metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>getOrCreateOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">getOrCreateOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Looks for owned metadata matching given metaclass or creates and applies a new one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass of metadata to apply</dd>
<dt>Returns:</dt>
<dd>metadata</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)"><code>createOwnedMetadata(Element, Metaclass)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>getMetadata</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">getMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Returns metadata applied to the element matching the given metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass to match</dd>
<dt>Returns:</dt>
<dd>matching metadata, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>getOwnedMetadata</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">getOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Returns owned metadata applied to the element matching the given metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass to match</dd>
<dt>Returns:</dt>
<dd>matching metadata, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata(java.util.Collection,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>getMetadata</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">getMetadata</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Returns metadata from the given collection matching the given metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadata</code> - metadata collection</dd>
<dd><code>metaclass</code> - metaclass to match</dd>
<dt>Returns:</dt>
<dd>matching metadata, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Collection,boolean)">
<h3>setOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt; metaclasses,
 boolean disposeNotMatching)</span></div>
<div class="block">Sets owned metadata of <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a> matching given metaclasses.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclasses</code> - metaclasses</dd>
<dd><code>disposeNotMatching</code> - disposes existing owned metadata not matching given metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaclassesOfOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getMetaclassesOfOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</span> <span class="element-name">getMetaclassesOfOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns metaclasses of owned metadata applied to the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list of metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaclassesOfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getMetaclassesOfMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</span> <span class="element-name">getMetaclassesOfMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns metaclasses of all metadata applied to the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list of metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mapMetadataToMetaclasses(java.util.List)">
<h3>mapMetadataToMetaclasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</span> <span class="element-name">mapMetadataToMetaclasses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadataFeatures)</span></div>
<div class="block">Maps metadata features to their metaclasses.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadataFeatures</code> - metadata features</dd>
<dt>Returns:</dt>
<dd>list of metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotatedElementTypes(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">
<h3>getAnnotatedElementTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt;</span> <span class="element-name">getAnnotatedElementTypes</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</span></div>
<div class="block">Returns the annotated element types for the given metadata feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadataFeature</code> - metadata feature</dd>
<dt>Returns:</dt>
<dd>list of annotated element types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getBaseTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getBaseTypes</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> target)</span></div>
<div class="block">Returns base types associated with metadata applied to the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - type</dd>
<dt>Returns:</dt>
<dd>list of base types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toClassifiers(java.util.List)">
<h3>toClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">toClassifiers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; baseType)</span></div>
<div class="block">Converts base types to classifiers by expanding feature types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>baseType</code> - list of types</dd>
<dt>Returns:</dt>
<dd>list of classifier types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toFeatures(java.util.List)">
<h3>toFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">toFeatures</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; baseType)</span></div>
<div class="block">Filters the given list of types to only those that are features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>baseType</code> - list of types</dd>
<dt>Returns:</dt>
<dd>list containing only feature types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaclassName(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">
<h3>getMetaclassName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMetaclassName</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> feature)</span></div>
<div class="block">Returns the name of the metaclass of the given metadata feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - metadata feature</dd>
<dt>Returns:</dt>
<dd>metaclass name, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaclassName(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>getMetaclassName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMetaclassName</span><wbr/><span class="parameters">(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Returns the name of the given metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metaclass</code> - metaclass</dd>
<dt>Returns:</dt>
<dd>short name or name, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isApplicable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isApplicable</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether metadata is applicable to the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if metadata can be applied</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getSelfMetadata</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">getSelfMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the self metadata feature of the element, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>self metadata, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">
<h3>isSelfMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSelfMetadata</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</span></div>
<div class="block">Checks whether the given metadata feature is self metadata.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadataFeature</code> - metadata feature</dd>
<dt>Returns:</dt>
<dd>true if it is self metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEClassIfSelfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">
<h3>getEClassIfSelfMetadata</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getEClassIfSelfMetadata</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</span></div>
<div class="block">Returns the EClass of the syntax element for self metadata.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadataFeature</code> - metadata feature</dd>
<dt>Returns:</dt>
<dd>EClass of syntax element, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getMetaClassOf</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></span> <span class="element-name">getMetaClassOf</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the metaclass of the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>metaclass, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaClassFor(com.dassault_systemes.modeler.foundation.project.ModelElementProject,org.eclipse.emf.ecore.EClass)">
<h3>getMetaClassFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></span> <span class="element-name">getMetaClassFor</span><wbr/><span class="parameters">(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns the metaclass corresponding to the given EClass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>eClass</code> - EClass</dd>
<dt>Returns:</dt>
<dd>metaclass, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEClassFor(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>getEClassFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getEClassFor</span><wbr/><span class="parameters">(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Returns the EClass corresponding to the given metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metaclass</code> - metaclass</dd>
<dt>Returns:</dt>
<dd>EClass, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMetamodelFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isMetamodelFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMetamodelFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a metamodel feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature</dd>
<dt>Returns:</dt>
<dd>true if the feature belongs to a metaclass with a resolvable EClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAnnotatedWithOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>isAnnotatedWithOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAnnotatedWithOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Checks whether the element is annotated with owned metadata of the given metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass</dd>
<dt>Returns:</dt>
<dd>true if matching owned metadata exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstanceOfMetamodelMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Collection)">
<h3>isInstanceOfMetamodelMetaclass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstanceOfMetamodelMetaclass</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a>&gt; metaclasses)</span></div>
<div class="block">Checks whether the element is an instance of the given metamodel metaclasses.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclasses</code> - metaclasses</dd>
<dt>Returns:</dt>
<dd>true if the element matches any metaclass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstanceOfMetamodelMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass)">
<h3>isInstanceOfMetamodelMetaclass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstanceOfMetamodelMetaclass</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass)</span></div>
<div class="block">Checks whether the element is an instance of the given metamodel metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass</dd>
<dt>Returns:</dt>
<dd>true if the element matches the metaclass</dd>
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
