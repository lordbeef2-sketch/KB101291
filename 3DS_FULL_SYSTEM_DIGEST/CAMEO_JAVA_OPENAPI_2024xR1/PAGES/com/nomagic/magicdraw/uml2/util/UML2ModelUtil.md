# JAVA OPENAPI: UML2ModelUtil (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/util/UML2ModelUtil.html
- source_path: `com/nomagic/magicdraw/uml2/util/UML2ModelUtil.html`
- source_sha256: `cce072f3f37bcd2519d384514dab828ce8aa824d8480333703f3cdb0ef518dd6`
- captured_utc: `2026-07-14T16:52:18.986973+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class UML2ModelUtil

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.util.UML2ModelUtil

public classUML2ModelUtil
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Contains various UML2 model related utility methods.

Version:
1.0

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE__MD_CONTAINMENT](#ANNOTATION_SOURCE__MD_CONTAINMENT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE__MD_TRANSIENT](#ANNOTATION_SOURCE__MD_TRANSIENT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE__MOF](#ANNOTATION_SOURCE__MOF)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE__RENAMED](#ANNOTATION_SOURCE__RENAMED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE__SUBSETS](#ANNOTATION_SOURCE__SUBSETS)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE__UNION](#ANNOTATION_SOURCE__UNION)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANNOTATION_SOURCE_REDEFINES](#ANNOTATION_SOURCE_REDEFINES)`

`static final com.dassault_systemes.modeler.foundation.util.FeatureValueCompatibility`
`[FEATURE_VALUE_COMPATIBILITY](#FEATURE_VALUE_COMPATIBILITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[checkCompatibility](#checkCompatibility(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object))(org.eclipse.emf.ecore.EObject object,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Checks whether the specified object and specified feature value is valid.
`static void`
`[collectAllEClassifiers](#collectAllEClassifiers(org.eclipse.emf.ecore.EPackage,java.util.Collection))(org.eclipse.emf.ecore.EPackage ePackage,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClassifier> result)`
Collects all classifiers from the specified package recursively.
`static void`
`[collectEAllClasses](#collectEAllClasses(org.eclipse.emf.ecore.EPackage,java.util.Collection))(org.eclipse.emf.ecore.EPackage root,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClass> result)`
Collect all classifiers recursively into specified result collection.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClassifier>`
`[getAllEClassifiers](#getAllEClassifiers(org.eclipse.emf.ecore.EPackage))(org.eclipse.emf.ecore.EPackage aPackage)`
Returns all classifiers from the specified package recursively.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getChangePropertyName](#getChangePropertyName(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object))(org.eclipse.emf.ecore.EObject target,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Returns change property name.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClassifier>`
`[getCompatibleTypes](#getCompatibleTypes(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns Collection of EClassifiers which instances can be set as values to the specified
 feature to an instance of the type eClass.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDefault](#getDefault(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)`
Returns string representation of the default value of the property.
`static org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EClass>`
`[getEAllSubClasses](#getEAllSubClasses(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns all subclasses of the specified class.
`static org.eclipse.emf.ecore.EStructuralFeature`
`[getEStructuralFeature](#getEStructuralFeature(org.eclipse.emf.ecore.EClass,java.lang.String))(org.eclipse.emf.ecore.EClass eClass,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) publicFeatureName)`
Returns structural feature from the specified class by public feature name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMOFPackageName](#getMOFPackageName(org.eclipse.emf.ecore.EClassifier))(org.eclipse.emf.ecore.EClassifier classifier)`
Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.
`static org.eclipse.emf.ecore.EStructuralFeature`
`[getOppositeRedefinition](#getOppositeRedefinition(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns structural feature that redefines the specified feature.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPrivateFeatureName](#getPrivateFeatureName(org.eclipse.emf.ecore.EClass,java.lang.String))(org.eclipse.emf.ecore.EClass containingClass,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) publicFeatureName)`
Returns private name of the specified feature.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPublicFeatureName](#getPublicFeatureName(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns public name of the structural feature.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getQualifiedMOFPackageName](#getQualifiedMOFPackageName(org.eclipse.emf.ecore.EClassifier))(org.eclipse.emf.ecore.EClassifier classifier)`
Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature>`
`[getRedefinedFeatures](#getRedefinedFeatures(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns redefined features of the specified feature.
`static org.eclipse.emf.ecore.EStructuralFeature`
`[getRedefinition](#getRedefinition(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns structural feature that redefines the specified feature.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature>`
`[getSortedFeatures](#getSortedFeatures(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns sorted features.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EReference>`
`[getSortedReferences](#getSortedReferences(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns sorted reference.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature>`
`[getSubsetFeatures](#getSubsetFeatures(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature,boolean,boolean))(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature supersetFeature,
 boolean includeDerived,
 boolean includeMany)`
Returns subset features of the specified superset feature.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature>`
`[getSubsettedFeatures](#getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)`
Returns subsetted feature list of the specified feature.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature>`
`[getSubsettedFeatures](#getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature,boolean))(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature,
 boolean recursive)`
Returns subsetted feature list of the specified feature.
`static boolean`
`[isAssignableFrom](#isAssignableFrom(org.eclipse.emf.ecore.EClassifier,org.eclipse.emf.ecore.EClassifier))(org.eclipse.emf.ecore.EClassifier a,
 org.eclipse.emf.ecore.EClassifier b)`
Determines if the instance class represented by the first EClassifier object is either the same as,
 or is a superclass of the instance class represented by the specified second EClassifier parameter.
`static boolean`
`[isCheckCompatibility](#isCheckCompatibility())()`

`static boolean`
`[isCompatible](#isCompatible(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object))(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Checks whether the specified object and specified feature value is valid.
`static boolean`
`[isContainer](#isContainer(org.eclipse.emf.ecore.EReference))(org.eclipse.emf.ecore.EReference reference)`
Returns true if the reference should be treated as container reference.
`static boolean`
`[isContainment](#isContainment(org.eclipse.emf.ecore.EReference))(org.eclipse.emf.ecore.EReference reference)`
Returns true if the reference should be treated as containment reference.
`static boolean`
`[isDerivedButNotUnion](#isDerivedButNotUnion(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns true if the specified feature is derived but not derived union.
`static boolean`
`[isDerivedUnion](#isDerivedUnion(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Checks whether the specified feature is derived union.
`static boolean`
`[isFullyCompatible](#isFullyCompatible(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object))(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Returns whether the specified object feature can be set to/value added to collection representing value of
 the feature or can not.
`static boolean`
`[isMDMultiplicityMany](#isMDMultiplicityMany(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns true if the multiplicity of the property should be treated as many.
`static boolean`
`[isMDTransient](#isMDTransient(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns true if the feature is marked transient in MD.
`static boolean`
`[isOppositeRedefined](#isOppositeRedefined(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns whether the specified feature is redefined.
`static boolean`
`[isRedefined](#isRedefined(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns whether the specified feature is redefined.
`static boolean`
`[isRedefinition](#isRedefinition(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns true if the specified feature is redefinition of another feature.
`static boolean`
`[isRenamed](#isRenamed(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns true if the specified feature is renamed.
`static boolean`
`[isSubsets](#isSubsets(org.eclipse.emf.ecore.EReference))(org.eclipse.emf.ecore.EReference reference)`

`static boolean`
`[isSuperset](#isSuperset(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)`
Returns true if the specified structural feature in the specified EClass is superset.
`static boolean`
`[isTransient](#isTransient(org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EStructuralFeature feature)`
Returns true if the feature is transient or marked transient in MD.
`static void`
`[setCheckCompatibility](#setCheckCompatibility(boolean))(boolean checkCompatibility)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ANNOTATION_SOURCE__UNION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE__UNION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__UNION)
ANNOTATION_SOURCE__SUBSETS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE__SUBSETS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__SUBSETS)
ANNOTATION_SOURCE_REDEFINES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE_REDEFINES
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE_REDEFINES)
ANNOTATION_SOURCE__MD_TRANSIENT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE__MD_TRANSIENT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__MD_TRANSIENT)
ANNOTATION_SOURCE__MOF
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE__MOF
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__MOF)
ANNOTATION_SOURCE__RENAMED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE__RENAMED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__RENAMED)
ANNOTATION_SOURCE__MD_CONTAINMENT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANNOTATION_SOURCE__MD_CONTAINMENT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__MD_CONTAINMENT)
FEATURE_VALUE_COMPATIBILITY
public static final com.dassault_systemes.modeler.foundation.util.FeatureValueCompatibility FEATURE_VALUE_COMPATIBILITY
 ============ METHOD DETAIL ========== 
Method Details
isCheckCompatibility
public static boolean isCheckCompatibility()
setCheckCompatibility
public static void setCheckCompatibility(boolean checkCompatibility)
isDerivedUnion
public static boolean isDerivedUnion(org.eclipse.emf.ecore.EStructuralFeature feature)
Checks whether the specified feature is derived union.
Parameters:
`feature` - a feature.
Returns:
true if it is derived union.
isSubsets
public static boolean isSubsets(org.eclipse.emf.ecore.EReference reference)
getSubsettedFeatures
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature> getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)
Returns subsetted feature list of the specified feature. Returns empty list if the features has no
 subsetted features.
Parameters:
`eStructuralFeature` - feature which subsetted features should be returned.
Returns:
list of subsetted features.
getSubsettedFeatures
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature> getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature,
 boolean recursive)
Returns subsetted feature list of the specified feature. Returns empty list if the features has no
 subsetted features.
Parameters:
`eStructuralFeature` - feature which subsetted features should be returned.
`recursive` - if true then search for subsetted features recursively.
Returns:
list of subsetted features.
getSubsetFeatures
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature> getSubsetFeatures(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature supersetFeature,
 boolean includeDerived,
 boolean includeMany)
Returns subset features of the specified superset feature.
Parameters:
`eClass` - EClass that is a context of search.
`supersetFeature` - superset feature.
`includeDerived` - if value is true then derived properties should be included into result.
`includeMany` - if true then multivalue features should be included into result.
Returns:
list of subset features.
isSuperset
public static boolean isSuperset(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)
Returns true if the specified structural feature in the specified EClass is superset.
Parameters:
`eClass` - EClass object which features will be analysed.
`eStructuralFeature` - structural feature.
Returns:
true if it is superset.
isRedefinition
public static boolean isRedefinition(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns true if the specified feature is redefinition of another feature.
Parameters:
`feature` - a feature.
Returns:
true if redefinition.
isMDTransient
public static boolean isMDTransient(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns true if the feature is marked transient in MD.

 This method does not fully replace isPrivatePropertyName, use [`isTransient(EStructuralFeature)`](#isTransient(org.eclipse.emf.ecore.EStructuralFeature)) for this.
Parameters:
`feature` - structural feature.
Returns:
true if md transient.
isTransient
public static boolean isTransient(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns true if the feature is transient or marked transient in MD.
Parameters:
`feature` - structural feature.
Returns:
true if transient or md transient.
getMOFPackageName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMOFPackageName(org.eclipse.emf.ecore.EClassifier classifier)
Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.
 Separator used in the qualified name is '.'
Parameters:
`classifier` - classifier from UML metamodel.
Returns:
package name or null if the classifier is not from UML metamodel.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the classifier parameter is null.
getQualifiedMOFPackageName
@CheckForNullpublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getQualifiedMOFPackageName(org.eclipse.emf.ecore.EClassifier classifier)
Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.
Parameters:
`classifier` - classifier from UML metamodel.
Returns:
list of MOF package names null if the classifier is not from UML metamodel.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the classifier parameter is null.
collectEAllClasses
public static void collectEAllClasses(org.eclipse.emf.ecore.EPackage root,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClass> result)
Collect all classifiers recursively into specified result collection.
Parameters:
`root` - root EPackage.
`result` - result collection.
getRedefinedFeatures
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature> getRedefinedFeatures(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns redefined features of the specified feature.
Parameters:
`feature` - a structural feature.
Returns:
redefined features.
getRedefinition
@CheckForNullpublic static org.eclipse.emf.ecore.EStructuralFeature getRedefinition(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)
Returns structural feature that redefines the specified feature. Uses map for fast search.
Parameters:
`eContainingClass` - containing EClass.
`feature` - structural feature that mey be redefined.
Returns:
redefinition feature or null if the specified feature is not redefined.
getOppositeRedefinition
@CheckForNullpublic static org.eclipse.emf.ecore.EStructuralFeature getOppositeRedefinition(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)
Returns structural feature that redefines the specified feature.
Parameters:
`eClass` - containing EClass.
`feature` - structural feature that mey be redefined.
Returns:
redefinition feature or null if the specified feature is not
 redefined.
isRedefined
public static boolean isRedefined(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)
Returns whether the specified feature is redefined.
Parameters:
`eContainingClass` - containing EClass.
`feature` - structural feature that mey be redefined.
Returns:
true if redefined.
isOppositeRedefined
public static boolean isOppositeRedefined(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)
Returns whether the specified feature is redefined.
Parameters:
`eClass` - containing EClass.
`feature` - structural feature that mey be redefined.
Returns:
true if redefined.
isFullyCompatible
public static boolean isFullyCompatible(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Returns whether the specified object feature can be set to/value added to collection representing value of
 the feature or can not.
Parameters:
`obj` - an object which feature should be analysed.
`feature` - a feature that should be analysed.
`value` - a value of the feature.
Returns:
true if value can be set.
isCompatible
public static boolean isCompatible(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Checks whether the specified object and specified feature value is valid.
Parameters:
`obj` - an object.
`feature` - a feature that should be checked.
`value` - value that should be checked.
Returns:
true if compatible.
checkCompatibility
public static void checkCompatibility(org.eclipse.emf.ecore.EObject object,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Checks whether the specified object and specified feature value is valid.
Parameters:
`object` - an object.
`structuralFeature` - a structural feature.
`value` - a value.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the specified value is not compatible.
isRenamed
public static boolean isRenamed(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns true if the specified feature is renamed.
Parameters:
`feature` - a feature.
Returns:
renamed.
getPublicFeatureName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPublicFeatureName(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns public name of the structural feature.
Parameters:
`feature` - a structural feature.
Returns:
public name.
getPrivateFeatureName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPrivateFeatureName(org.eclipse.emf.ecore.EClass containingClass,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) publicFeatureName)
Returns private name of the specified feature.
Parameters:
`containingClass` - a class that private feature name should be returned.
`publicFeatureName` - public name of the feature.
Returns:
private name of the feature.
getChangePropertyName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getChangePropertyName(org.eclipse.emf.ecore.EObject target,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Returns change property name.
Parameters:
`target` - owner of the property.
`structuralFeature` - feature changed.
`value` - value of the property.
Returns:
name of the property change.
getEStructuralFeature
public static org.eclipse.emf.ecore.EStructuralFeature getEStructuralFeature(org.eclipse.emf.ecore.EClass eClass,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) publicFeatureName)
Returns structural feature from the specified class by public feature name.
Parameters:
`eClass` - EClass.
`publicFeatureName` - public feature name.
Returns:
structural feature or null if no such exist.
isContainment
public static boolean isContainment(org.eclipse.emf.ecore.EReference reference)
Returns true if the reference should be treated as containment reference.
Parameters:
`reference` - a reference.
Returns:
true if it is containment reference.
isContainer
public static boolean isContainer(org.eclipse.emf.ecore.EReference reference)
Returns true if the reference should be treated as container reference.
Parameters:
`reference` - a reference.
Returns:
true if it is container reference.
getSortedReferences
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EReference> getSortedReferences(org.eclipse.emf.ecore.EClass eClass)
Returns sorted reference. References are sorted in the order that allows correct sequential modification
 of reference values.
Parameters:
`eClass` - EClass object.
Returns:
references where supersets are in the latest positions.
getSortedFeatures
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EStructuralFeature> getSortedFeatures(org.eclipse.emf.ecore.EClass eClass)
Returns sorted features. Features are sorted in the order that allows correct sequential modification
 of feature values.
Parameters:
`eClass` - EClass instance.
Returns:
sorted features.
isDerivedButNotUnion
public static boolean isDerivedButNotUnion(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns true if the specified feature is derived but not derived union.
Parameters:
`feature` - a structural feature.
Returns:
true if the feature is derived but not derived union.
getEAllSubClasses
public static org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EClass> getEAllSubClasses(org.eclipse.emf.ecore.EClass eClass)
Returns all subclasses of the specified class. The method returns subclasses from the package to which
 belongs the specified class. If there are other packages that contains classes that extends the specified class
 then these classes will not be returned. The method return only not abstract classes.
Parameters:
`eClass` - a class which subclasses must be returned.
Returns:
list of subclasses.
collectAllEClassifiers
public static void collectAllEClassifiers(org.eclipse.emf.ecore.EPackage ePackage,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClassifier> result)
Collects all classifiers from the specified package recursively.
Parameters:
`ePackage` - a package from which to collect classifiers.
`result` - result collection.
getAllEClassifiers
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClassifier> getAllEClassifiers(org.eclipse.emf.ecore.EPackage aPackage)
Returns all classifiers from the specified package recursively.
Parameters:
`aPackage` - a package.
Returns:
result collection.
isAssignableFrom
public static boolean isAssignableFrom(org.eclipse.emf.ecore.EClassifier a,
 org.eclipse.emf.ecore.EClassifier b)
Determines if the instance class represented by the first EClassifier object is either the same as,
 or is a superclass of the instance class represented by the specified second EClassifier parameter.
Parameters:
`a` - first classifier.
`b` - second classifier.
Returns:
true if assignable.
getCompatibleTypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<org.eclipse.emf.ecore.EClassifier> getCompatibleTypes(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)
Returns Collection of EClassifiers which instances can be set as values to the specified
 feature to an instance of the type eClass.
Parameters:
`eClass` - EClass object which reference should be analyzed.
`feature` - a structural feature which should be analyzed.
Returns:
compatible type.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the specified EClass is not from UML package or
 if the specified feature is not contained by the class.
getDefault
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDefault([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)
Returns string representation of the default value of the property.
Parameters:
`property` - a property.
Returns:
default value as string.
isMDMultiplicityMany
public static boolean isMDMultiplicityMany(org.eclipse.emf.ecore.EStructuralFeature feature)
Returns true if the multiplicity of the property should be treated as many. Otherwise - false.
Parameters:
`feature` - a structural feature.
Returns:
true if many otherwise - false.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class UML2ModelUtil">Class UML2ModelUtil</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.util.UML2ModelUtil</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">UML2ModelUtil</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains various UML2 model related utility methods.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
</dl>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE__MD_CONTAINMENT">ANNOTATION_SOURCE__MD_CONTAINMENT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE__MD_TRANSIENT">ANNOTATION_SOURCE__MD_TRANSIENT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE__MOF">ANNOTATION_SOURCE__MOF</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE__RENAMED">ANNOTATION_SOURCE__RENAMED</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE__SUBSETS">ANNOTATION_SOURCE__SUBSETS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE__UNION">ANNOTATION_SOURCE__UNION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANNOTATION_SOURCE_REDEFINES">ANNOTATION_SOURCE_REDEFINES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final com.dassault_systemes.modeler.foundation.util.FeatureValueCompatibility</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FEATURE_VALUE_COMPATIBILITY">FEATURE_VALUE_COMPATIBILITY</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkCompatibility(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">checkCompatibility</a><wbr/>(org.eclipse.emf.ecore.EObject object,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the specified object and specified feature value is valid.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectAllEClassifiers(org.eclipse.emf.ecore.EPackage,java.util.Collection)">collectAllEClassifiers</a><wbr/>(org.eclipse.emf.ecore.EPackage ePackage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClassifier&gt; result)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all classifiers from the specified package recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectEAllClasses(org.eclipse.emf.ecore.EPackage,java.util.Collection)">collectEAllClasses</a><wbr/>(org.eclipse.emf.ecore.EPackage root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClass&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all classifiers recursively into specified result collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClassifier&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllEClassifiers(org.eclipse.emf.ecore.EPackage)">getAllEClassifiers</a><wbr/>(org.eclipse.emf.ecore.EPackage aPackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all classifiers from the specified package recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getChangePropertyName(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">getChangePropertyName</a><wbr/>(org.eclipse.emf.ecore.EObject target,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns change property name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClassifier&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompatibleTypes(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">getCompatibleTypes</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns Collection of EClassifiers which instances can be set as values to the specified
 feature to an instance of the type eClass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefault(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getDefault</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns string representation of the default value of the property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.common.util.EList&lt;org.eclipse.emf.ecore.EClass&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEAllSubClasses(org.eclipse.emf.ecore.EClass)">getEAllSubClasses</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all subclasses of the specified class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EStructuralFeature</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEStructuralFeature(org.eclipse.emf.ecore.EClass,java.lang.String)">getEStructuralFeature</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> publicFeatureName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns structural feature from the specified class by public feature name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMOFPackageName(org.eclipse.emf.ecore.EClassifier)">getMOFPackageName</a><wbr/>(org.eclipse.emf.ecore.EClassifier classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EStructuralFeature</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOppositeRedefinition(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">getOppositeRedefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns structural feature that redefines the specified feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrivateFeatureName(org.eclipse.emf.ecore.EClass,java.lang.String)">getPrivateFeatureName</a><wbr/>(org.eclipse.emf.ecore.EClass containingClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> publicFeatureName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns private name of the specified feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPublicFeatureName(org.eclipse.emf.ecore.EStructuralFeature)">getPublicFeatureName</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns public name of the structural feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifiedMOFPackageName(org.eclipse.emf.ecore.EClassifier)">getQualifiedMOFPackageName</a><wbr/>(org.eclipse.emf.ecore.EClassifier classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinedFeatures(org.eclipse.emf.ecore.EStructuralFeature)">getRedefinedFeatures</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns redefined features of the specified feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EStructuralFeature</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinition(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">getRedefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns structural feature that redefines the specified feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortedFeatures(org.eclipse.emf.ecore.EClass)">getSortedFeatures</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns sorted features.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EReference&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortedReferences(org.eclipse.emf.ecore.EClass)">getSortedReferences</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns sorted reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubsetFeatures(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature,boolean,boolean)">getSubsetFeatures</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature supersetFeature,
 boolean includeDerived,
 boolean includeMany)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns subset features of the specified superset feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature)">getSubsettedFeatures</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns subsetted feature list of the specified feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature,boolean)">getSubsettedFeatures</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature,
 boolean recursive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns subsetted feature list of the specified feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssignableFrom(org.eclipse.emf.ecore.EClassifier,org.eclipse.emf.ecore.EClassifier)">isAssignableFrom</a><wbr/>(org.eclipse.emf.ecore.EClassifier a,
 org.eclipse.emf.ecore.EClassifier b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines if the instance class represented by the first EClassifier object is either the same as,
 or is a superclass of the instance class represented by the specified second EClassifier parameter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCheckCompatibility()">isCheckCompatibility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCompatible(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">isCompatible</a><wbr/>(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the specified object and specified feature value is valid.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isContainer(org.eclipse.emf.ecore.EReference)">isContainer</a><wbr/>(org.eclipse.emf.ecore.EReference reference)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the reference should be treated as container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isContainment(org.eclipse.emf.ecore.EReference)">isContainment</a><wbr/>(org.eclipse.emf.ecore.EReference reference)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the reference should be treated as containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedButNotUnion(org.eclipse.emf.ecore.EStructuralFeature)">isDerivedButNotUnion</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the specified feature is derived but not derived union.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedUnion(org.eclipse.emf.ecore.EStructuralFeature)">isDerivedUnion</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the specified feature is derived union.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFullyCompatible(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">isFullyCompatible</a><wbr/>(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the specified object feature can be set to/value added to collection representing value of
 the feature or can not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMDMultiplicityMany(org.eclipse.emf.ecore.EStructuralFeature)">isMDMultiplicityMany</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the multiplicity of the property should be treated as many.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMDTransient(org.eclipse.emf.ecore.EStructuralFeature)">isMDTransient</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the feature is marked transient in MD.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOppositeRedefined(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">isOppositeRedefined</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the specified feature is redefined.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRedefined(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">isRedefined</a><wbr/>(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the specified feature is redefined.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRedefinition(org.eclipse.emf.ecore.EStructuralFeature)">isRedefinition</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the specified feature is redefinition of another feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRenamed(org.eclipse.emf.ecore.EStructuralFeature)">isRenamed</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the specified feature is renamed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSubsets(org.eclipse.emf.ecore.EReference)">isSubsets</a><wbr/>(org.eclipse.emf.ecore.EReference reference)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuperset(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">isSuperset</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the specified structural feature in the specified EClass is superset.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isTransient(org.eclipse.emf.ecore.EStructuralFeature)">isTransient</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the feature is transient or marked transient in MD.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCheckCompatibility(boolean)">setCheckCompatibility</a><wbr/>(boolean checkCompatibility)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<section class="detail" id="ANNOTATION_SOURCE__UNION">
<h3>ANNOTATION_SOURCE__UNION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE__UNION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__UNION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION_SOURCE__SUBSETS">
<h3>ANNOTATION_SOURCE__SUBSETS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE__SUBSETS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__SUBSETS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION_SOURCE_REDEFINES">
<h3>ANNOTATION_SOURCE_REDEFINES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE_REDEFINES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE_REDEFINES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION_SOURCE__MD_TRANSIENT">
<h3>ANNOTATION_SOURCE__MD_TRANSIENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE__MD_TRANSIENT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__MD_TRANSIENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION_SOURCE__MOF">
<h3>ANNOTATION_SOURCE__MOF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE__MOF</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__MOF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION_SOURCE__RENAMED">
<h3>ANNOTATION_SOURCE__RENAMED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE__RENAMED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__RENAMED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION_SOURCE__MD_CONTAINMENT">
<h3>ANNOTATION_SOURCE__MD_CONTAINMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANNOTATION_SOURCE__MD_CONTAINMENT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml2.util.UML2ModelUtil.ANNOTATION_SOURCE__MD_CONTAINMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_VALUE_COMPATIBILITY">
<h3>FEATURE_VALUE_COMPATIBILITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">com.dassault_systemes.modeler.foundation.util.FeatureValueCompatibility</span> <span class="element-name">FEATURE_VALUE_COMPATIBILITY</span></div>
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
<section class="detail" id="isCheckCompatibility()">
<h3>isCheckCompatibility</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCheckCompatibility</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCheckCompatibility(boolean)">
<h3>setCheckCompatibility</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCheckCompatibility</span><wbr/><span class="parameters">(boolean checkCompatibility)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDerivedUnion(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isDerivedUnion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedUnion</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Checks whether the specified feature is derived union.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a feature.</dd>
<dt>Returns:</dt>
<dd>true if it is derived union.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSubsets(org.eclipse.emf.ecore.EReference)">
<h3>isSubsets</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSubsets</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EReference reference)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>getSubsettedFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</span> <span class="element-name">getSubsettedFeatures</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</span></div>
<div class="block">Returns subsetted feature list of the specified feature. Returns empty list if the features has no
 subsetted features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eStructuralFeature</code> - feature which subsetted features should be returned.</dd>
<dt>Returns:</dt>
<dd>list of subsetted features.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubsettedFeatures(org.eclipse.emf.ecore.EStructuralFeature,boolean)">
<h3>getSubsettedFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</span> <span class="element-name">getSubsettedFeatures</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature,
 boolean recursive)</span></div>
<div class="block">Returns subsetted feature list of the specified feature. Returns empty list if the features has no
 subsetted features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eStructuralFeature</code> - feature which subsetted features should be returned.</dd>
<dd><code>recursive</code> - if true then search for subsetted features recursively.</dd>
<dt>Returns:</dt>
<dd>list of subsetted features.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubsetFeatures(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature,boolean,boolean)">
<h3>getSubsetFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</span> <span class="element-name">getSubsetFeatures</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature supersetFeature,
 boolean includeDerived,
 boolean includeMany)</span></div>
<div class="block">Returns subset features of the specified superset feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - EClass that is a context of search.</dd>
<dd><code>supersetFeature</code> - superset feature.</dd>
<dd><code>includeDerived</code> - if value is true then derived properties should be included into result.</dd>
<dd><code>includeMany</code> - if true then multivalue features should be included into result.</dd>
<dt>Returns:</dt>
<dd>list of subset features.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSuperset(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isSuperset</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSuperset</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</span></div>
<div class="block">Returns true if the specified structural feature in the specified EClass is superset.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - EClass object which features will be analysed.</dd>
<dd><code>eStructuralFeature</code> - structural feature.</dd>
<dt>Returns:</dt>
<dd>true if it is superset.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRedefinition(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isRedefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRedefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns true if the specified feature is redefinition of another feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a feature.</dd>
<dt>Returns:</dt>
<dd>true if redefinition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMDTransient(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isMDTransient</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMDTransient</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns true if the feature is marked transient in MD.

 This method does not fully replace isPrivatePropertyName, use <a href="#isTransient(org.eclipse.emf.ecore.EStructuralFeature)"><code>isTransient(EStructuralFeature)</code></a> for this.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - structural feature.</dd>
<dt>Returns:</dt>
<dd>true if md transient.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTransient(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isTransient</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTransient</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns true if the feature is transient or marked transient in MD.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - structural feature.</dd>
<dt>Returns:</dt>
<dd>true if transient or  md transient.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMOFPackageName(org.eclipse.emf.ecore.EClassifier)">
<h3>getMOFPackageName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMOFPackageName</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClassifier classifier)</span></div>
<div class="block">Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.
 Separator used in the qualified name is '.'</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier from UML metamodel.</dd>
<dt>Returns:</dt>
<dd>package name or null if the classifier is not from UML metamodel.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the classifier parameter is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedMOFPackageName(org.eclipse.emf.ecore.EClassifier)">
<h3>getQualifiedMOFPackageName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getQualifiedMOFPackageName</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClassifier classifier)</span></div>
<div class="block">Returns qualified MOF package name of the EClassifier that represents UML model element metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier from UML metamodel.</dd>
<dt>Returns:</dt>
<dd>list of MOF package names null if the classifier is not from UML metamodel.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the classifier parameter is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectEAllClasses(org.eclipse.emf.ecore.EPackage,java.util.Collection)">
<h3>collectEAllClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectEAllClasses</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EPackage root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClass&gt; result)</span></div>
<div class="block">Collect all classifiers recursively into specified result collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root EPackage.</dd>
<dd><code>result</code> - result collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedFeatures(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>getRedefinedFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</span> <span class="element-name">getRedefinedFeatures</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns redefined features of the specified feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a structural feature.</dd>
<dt>Returns:</dt>
<dd>redefined features.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinition(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>getRedefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EStructuralFeature</span> <span class="element-name">getRedefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns structural feature that redefines the specified feature. Uses map for fast search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eContainingClass</code> - containing EClass.</dd>
<dd><code>feature</code> - structural feature that mey be redefined.</dd>
<dt>Returns:</dt>
<dd>redefinition feature or null if the specified feature is not redefined.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOppositeRedefinition(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>getOppositeRedefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EStructuralFeature</span> <span class="element-name">getOppositeRedefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns structural feature that redefines the specified feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - containing EClass.</dd>
<dd><code>feature</code> - structural feature that mey be redefined.</dd>
<dt>Returns:</dt>
<dd>redefinition feature or null if the specified feature is not
         redefined.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRedefined(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRedefined</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eContainingClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns whether the specified feature is redefined.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eContainingClass</code> - containing EClass.</dd>
<dd><code>feature</code> - structural feature that mey be redefined.</dd>
<dt>Returns:</dt>
<dd>true if redefined.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOppositeRedefined(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isOppositeRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOppositeRedefined</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns whether the specified feature is redefined.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - containing EClass.</dd>
<dd><code>feature</code> - structural feature that mey be redefined.</dd>
<dt>Returns:</dt>
<dd>true if redefined.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFullyCompatible(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">
<h3>isFullyCompatible</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFullyCompatible</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Returns whether the specified object feature can be set to/value added to collection representing value of
 the feature or can not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - an object which feature should be analysed.</dd>
<dd><code>feature</code> - a feature that should be analysed.</dd>
<dd><code>value</code> - a value of the feature.</dd>
<dt>Returns:</dt>
<dd>true if value can be set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCompatible(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">
<h3>isCompatible</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCompatible</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject obj,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Checks whether the specified object and specified feature value is valid.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - an object.</dd>
<dd><code>feature</code> - a feature that should be checked.</dd>
<dd><code>value</code> - value that should be checked.</dd>
<dt>Returns:</dt>
<dd>true if compatible.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkCompatibility(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">
<h3>checkCompatibility</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">checkCompatibility</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject object,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Checks whether the specified object and specified feature value is valid.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - an object.</dd>
<dd><code>structuralFeature</code> - a structural feature.</dd>
<dd><code>value</code> - a value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the specified value is not compatible.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRenamed(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isRenamed</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRenamed</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns true if the specified feature is renamed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a feature.</dd>
<dt>Returns:</dt>
<dd>renamed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPublicFeatureName(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>getPublicFeatureName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPublicFeatureName</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns public name of the structural feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a structural feature.</dd>
<dt>Returns:</dt>
<dd>public name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrivateFeatureName(org.eclipse.emf.ecore.EClass,java.lang.String)">
<h3>getPrivateFeatureName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPrivateFeatureName</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass containingClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> publicFeatureName)</span></div>
<div class="block">Returns private name of the specified feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>containingClass</code> - a class that private feature name should be returned.</dd>
<dd><code>publicFeatureName</code> - public name of the feature.</dd>
<dt>Returns:</dt>
<dd>private name of the feature.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangePropertyName(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">
<h3>getChangePropertyName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getChangePropertyName</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject target,
 org.eclipse.emf.ecore.EStructuralFeature structuralFeature,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Returns change property name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - owner of the property.</dd>
<dd><code>structuralFeature</code> - feature changed.</dd>
<dd><code>value</code> - value of the property.</dd>
<dt>Returns:</dt>
<dd>name of the property change.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEStructuralFeature(org.eclipse.emf.ecore.EClass,java.lang.String)">
<h3>getEStructuralFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EStructuralFeature</span> <span class="element-name">getEStructuralFeature</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> publicFeatureName)</span></div>
<div class="block">Returns structural feature from the specified class by public feature name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - EClass.</dd>
<dd><code>publicFeatureName</code> - public feature name.</dd>
<dt>Returns:</dt>
<dd>structural feature or null if no such exist.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isContainment(org.eclipse.emf.ecore.EReference)">
<h3>isContainment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isContainment</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EReference reference)</span></div>
<div class="block">Returns true if the reference should be treated as containment reference.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - a reference.</dd>
<dt>Returns:</dt>
<dd>true if it is containment reference.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isContainer(org.eclipse.emf.ecore.EReference)">
<h3>isContainer</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isContainer</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EReference reference)</span></div>
<div class="block">Returns true if the reference should be treated as container reference.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - a reference.</dd>
<dt>Returns:</dt>
<dd>true if it is container reference.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortedReferences(org.eclipse.emf.ecore.EClass)">
<h3>getSortedReferences</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EReference&gt;</span> <span class="element-name">getSortedReferences</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns sorted reference. References are sorted in the order that allows correct sequential modification
 of reference values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - EClass object.</dd>
<dt>Returns:</dt>
<dd>references where supersets are in the latest positions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortedFeatures(org.eclipse.emf.ecore.EClass)">
<h3>getSortedFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EStructuralFeature&gt;</span> <span class="element-name">getSortedFeatures</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns sorted features. Features are sorted in the order that allows correct sequential modification
 of feature values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - EClass instance.</dd>
<dt>Returns:</dt>
<dd>sorted features.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedButNotUnion(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isDerivedButNotUnion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedButNotUnion</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns true if the specified feature is derived but not derived union.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a structural feature.</dd>
<dt>Returns:</dt>
<dd>true if the feature is derived but not derived union.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEAllSubClasses(org.eclipse.emf.ecore.EClass)">
<h3>getEAllSubClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.common.util.EList&lt;org.eclipse.emf.ecore.EClass&gt;</span> <span class="element-name">getEAllSubClasses</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns all subclasses of the specified class. The method returns subclasses from the package to which
 belongs the specified class. If there are other packages that contains classes that extends the specified class
 then these classes will not be returned. The method return only not abstract classes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - a class which subclasses must be returned.</dd>
<dt>Returns:</dt>
<dd>list of subclasses.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectAllEClassifiers(org.eclipse.emf.ecore.EPackage,java.util.Collection)">
<h3>collectAllEClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectAllEClassifiers</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EPackage ePackage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClassifier&gt; result)</span></div>
<div class="block">Collects all classifiers from the specified package recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ePackage</code> - a package from which to collect classifiers.</dd>
<dd><code>result</code> - result collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllEClassifiers(org.eclipse.emf.ecore.EPackage)">
<h3>getAllEClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClassifier&gt;</span> <span class="element-name">getAllEClassifiers</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EPackage aPackage)</span></div>
<div class="block">Returns all classifiers from the specified package recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aPackage</code> - a package.</dd>
<dt>Returns:</dt>
<dd>result collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssignableFrom(org.eclipse.emf.ecore.EClassifier,org.eclipse.emf.ecore.EClassifier)">
<h3>isAssignableFrom</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAssignableFrom</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClassifier a,
 org.eclipse.emf.ecore.EClassifier b)</span></div>
<div class="block">Determines if the instance class represented by the first EClassifier object is either the same as,
 or is a superclass of the instance class represented by the specified second EClassifier parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - first classifier.</dd>
<dd><code>b</code> - second classifier.</dd>
<dt>Returns:</dt>
<dd>true if assignable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCompatibleTypes(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>getCompatibleTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;org.eclipse.emf.ecore.EClassifier&gt;</span> <span class="element-name">getCompatibleTypes</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns Collection of EClassifiers which instances can be set as values to the specified
 feature to an instance of the type eClass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - EClass object which reference should be analyzed.</dd>
<dd><code>feature</code> - a structural feature which should be analyzed.</dd>
<dt>Returns:</dt>
<dd>compatible type.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the specified EClass is not from UML package or
                                  if the specified feature is not contained by the class.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefault(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getDefault</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefault</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Returns string representation of the default value of the property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - a property.</dd>
<dt>Returns:</dt>
<dd>default value as string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMDMultiplicityMany(org.eclipse.emf.ecore.EStructuralFeature)">
<h3>isMDMultiplicityMany</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMDMultiplicityMany</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature feature)</span></div>
<div class="block">Returns true if the multiplicity of the property should be treated as many. Otherwise - false.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a structural feature.</dd>
<dt>Returns:</dt>
<dd>true if many otherwise - false.</dd>
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
