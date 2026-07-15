# JAVA OPENAPI: Classifiers (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml2/Classifiers.html
- source_path: `com/nomagic/magicdraw/uml2/Classifiers.html`
- source_sha256: `0b40ad94eb8a544bf5e84dcc9fcff7f5e0c605d02db7a6931ad632ab89442102`
- captured_utc: `2026-07-14T16:52:20.209988+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Classifiers

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Classifiers

public classClassifiers
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience utility methods that operate on or return [`Classifier`](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Classifiers](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static <T extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> 
void`
`[collectDerivedClassifiers](#collectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) general,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> result)`
Collect all derived classifiers recursively (not only the direct children).
`static <T extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> 
void`
`[collectGeneralClassifiersRecursively](#collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) specific,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> result)`
Collects all general classifiers including the indirect ones up to the hierarchy top.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[collectGeneralClassifiersRecursively](#collectGeneralClassifiersRecursively(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers)`
Returns all general classifiers including the indirect ones up to hierarchy top.
`static void`
`[collectInheritedEnumerationLiterals](#collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean))([Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) enumeration,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)> result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned literals from the given enumeration.
`static void`
`[collectInheritedRealizedInterfaces](#collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean))([BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)> result,
 boolean collectOwned)`
Collect inherited and directly realized interfaces from the given classifier
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[InterfaceRealization](../../uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html)>`
`[collectInterfaceRealizations](#collectInterfaceRealizations(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html) contract)`
Collects interface realizations for the given contract
`static void`
`[collectRealizedInterfacesRecursively](#collectRealizedInterfacesRecursively(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)> result)`
Collects all realized interfaces by the given classifiers and their general classifiers recursively.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)>`
`[getAllLiterals](#getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration))([Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) enumeration)`
Return owned and inherited enumeration literals
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[getClassifierOrDerived](#getClassifierOrDerived(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) checkFor)`
Checks if classifier collection contains given classifier or any derived from it, and returns the first found
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getDerivedClassifiers](#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) general)`
Get all derived classifiers for given classifier recursively.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getDirectDerivedClassifiers](#getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) general)`
Return classifiers derived directly from the given classifier
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getDirectGeneralClassifiers](#getDirectGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Returns general classifiers from which the given classifier is directly derived.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getGeneralClassifiersRecursively](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) specific)`
Returns all general classifiers including the indirect ones up to the hierarchy top.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)>`
`[getPropertiesWithoutRedefined](#getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets owned and inherited properties without redefined ones.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)>`
`[getRealizedInterfaces](#getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier)`
Collects all realized interfaces by the given classifier directly.
`static [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getSameOrRedefined](#getSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)`
Resolves given property to itself or property redefined in the given classifier.
`static boolean`
`[isClassifierOfType](#isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) type)`
Tests if there is at least one classifier among given ones which isTypeOf (equals or is derived) given type.
`static boolean`
`[isDerivedClassifier](#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) child)`
Checks if given classifier "child" is derived from "parent".
`static boolean`
`[isDerivedOrRealizes](#isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) type)`
Checks if classifier is derived from given type or realizes the given type.
`static boolean`
`[isSameOrDerivedClassifier](#isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) child)`
Checks if given classifier "child" is same as "parent" or is derived from "parent".
`static boolean`
`[isSameOrRedefined](#isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) first,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) second)`
Check if given first property is the same as second property or first property is redefined by second property
`static boolean`
`[isSecondTypeCompatibleToFirst](#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean))([Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) firstType,
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) secondType,
 boolean checkRealizedInterfaces)`
Indicates if second parameter type is compatible to the first (is same type or a subtype).
`static void`
`[removeRedefined](#removeRedefined(java.util.Collection,java.util.Collection...))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html)> major,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html)>... additional)`
Removes redefined elements from a given major collection.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Classifiers
public Classifiers()
 ============ METHOD DETAIL ========== 
Method Details
getDerivedClassifiers
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getDerivedClassifiers([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) general)
Get all derived classifiers for given classifier recursively. Result does not include given classifier.
Parameters:
`general` - given classifier to collect specific classifiers for
Returns:
collection of all derived classifiers
collectDerivedClassifiers
public static <T extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> void collectDerivedClassifiers([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) general,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> result)
Collect all derived classifiers recursively (not only the direct children).
Parameters:
`general` - general classifier
`result` - collection of all derived classifiers
See Also:
[`getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)`](#getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
isClassifierOfType
public static boolean isClassifierOfType([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) type)
Tests if there is at least one classifier among given ones which isTypeOf (equals or is derived) given type.
Parameters:
`classifiers` - the given classifier
`type` - the given type
Returns:
true if classifiers contains at least one classifier which isTypeOf type
isSameOrDerivedClassifier
public static boolean isSameOrDerivedClassifier(@CheckForNull
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parent,
 @CheckForNull
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) child)
Checks if given classifier "child" is same as "parent" or is derived from "parent".
Parameters:
`parent` - parent classifier
`child` - child classifier
Returns:
true if same or derived
See Also:
[`isDerivedClassifier(Classifier, Classifier)`](#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
isDerivedClassifier
public static boolean isDerivedClassifier(@CheckForNull
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) parent,
 @CheckForNull
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) child)
Checks if given classifier "child" is derived from "parent".
Parameters:
`parent` - parent classifier
`child` - child classifier
Returns:
true if derived
See Also:
[`isDerivedClassifier(Classifier, Classifier)`](#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
getDirectDerivedClassifiers
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getDirectDerivedClassifiers(@CheckForNull
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) general)
Return classifiers derived directly from the given classifier
Parameters:
`general` - general classifier
Returns:
collection of direct derived classifiers
getClassifierOrDerived
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) getClassifierOrDerived([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) checkFor)
Checks if classifier collection contains given classifier or any derived from it, and returns the first found
Parameters:
`classifiers` - collection of classifiers to look in
`checkFor` - target classifier
Returns:
returns classifier which equals to the given or is derived
getGeneralClassifiersRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getGeneralClassifiersRecursively([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) specific)
Returns all general classifiers including the indirect ones up to the hierarchy top.
Parameters:
`specific` - classifier
Returns:
general classifiers
See Also:
[`getDirectGeneralClassifiers(Classifier)`](#getDirectGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
collectGeneralClassifiersRecursively
public static <T extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> void collectGeneralClassifiersRecursively([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) specific,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> result)
Collects all general classifiers including the indirect ones up to the hierarchy top.
Parameters:
`specific` - classifier
`result` - general classifiers
collectGeneralClassifiersRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> collectGeneralClassifiersRecursively([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers)
Returns all general classifiers including the indirect ones up to hierarchy top.
 Result includes given classifiers.
Parameters:
`classifiers` - classifier
Returns:
general elements
See Also:
[`getGeneralClassifiersRecursively(Classifier)`](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
getDirectGeneralClassifiers
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getDirectGeneralClassifiers([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Returns general classifiers from which the given classifier is directly derived.
Parameters:
`classifier` - classifier
Returns:
direct general classifiers
See Also:
[`getGeneralClassifiersRecursively(Classifier)`](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
isDerivedOrRealizes
public static boolean isDerivedOrRealizes([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) type)
Checks if classifier is derived from given type or realizes the given type.
Parameters:
`classifier` - classifier to check
`type` - type
Returns:
true if derived or realizes
getRealizedInterfaces
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)> getRealizedInterfaces([BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier)
Collects all realized interfaces by the given classifier directly.
Parameters:
`classifier` - given classifier
Returns:
a collection of realized interfaces(may be empty)
collectRealizedInterfacesRecursively
public static void collectRealizedInterfacesRecursively([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)> result)
Collects all realized interfaces by the given classifiers and their general classifiers recursively.
Parameters:
`classifiers` - classifiers to collect realized interfaces from
`result` - a collection to append interfaces to
collectInterfaceRealizations
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[InterfaceRealization](../../uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html)> collectInterfaceRealizations([BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html) contract)
Collects interface realizations for the given contract
Parameters:
`classifier` - classifier that might realize the interface
`contract` - interface to check realizations for
Returns:
a collection of interface realizations (may be empty)
collectInheritedRealizedInterfaces
public static void collectInheritedRealizedInterfaces([BehavioredClassifier](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html)> result,
 boolean collectOwned)
Collect inherited and directly realized interfaces from the given classifier
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
collectInheritedEnumerationLiterals
public static void collectInheritedEnumerationLiterals([Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) enumeration,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)> result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned literals from the given enumeration.
Parameters:
`enumeration` - enumeration
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
getAllLiterals
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)> getAllLiterals([Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) enumeration)
Return owned and inherited enumeration literals
Parameters:
`enumeration` - enumeration
Returns:
literals
getPropertiesWithoutRedefined
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> getPropertiesWithoutRedefined([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets owned and inherited properties without redefined ones.
Parameters:
`classifier` - classifiers from which properties will be collected
Returns:
owned and inherited properties without redefined ones.
removeRedefined
public static void removeRedefined([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html)> major,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html)>... additional)
Removes redefined elements from a given major collection. Major collection is a result. Additional collections are optional and are used only for redefined elements collecting
Parameters:
`major` - elements to remove redefined elements from
`additional` - elements to remove redefined elements from
isSameOrRedefined
public static boolean isSameOrRedefined(@CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) first,
 @CheckForNull
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) second)
Check if given first property is the same as second property or first property is redefined by second property
Parameters:
`first` - first property
`second` - second property
Returns:
first is the same as second or is redefined by second
getSameOrRedefined
public static [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getSameOrRedefined([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)
Resolves given property to itself or property redefined in the given classifier.
Parameters:
`classifier` - classifier
`property` - property to check
Returns:
given property or redefined if classifier redefines given property directly or indirectly
isSecondTypeCompatibleToFirst
public static boolean isSecondTypeCompatibleToFirst(@CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) firstType,
 @CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) secondType,
 boolean checkRealizedInterfaces)
Indicates if second parameter type is compatible to the first (is same type or a subtype).
Parameters:
`firstType` - parameter, to which the 2nd parameter must be compatible.
`secondType` - parameter, which should be compatible to the 1st.
`checkRealizedInterfaces` - indicates if realized interfaces should be taken into account when checking type compatibility.
Returns:
true if parameters are compatible, false otherwise.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Classifiers">Class Classifiers</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Classifiers</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Classifiers</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience utility methods that operate on or return <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a> elements.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Classifiers</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;<br/>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectDerivedClassifiers</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all derived classifiers recursively (not only the direct children).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;<br/>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectGeneralClassifiersRecursively</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> specific,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all general classifiers including the indirect ones up to the hierarchy top.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectGeneralClassifiersRecursively(java.util.Collection)">collectGeneralClassifiersRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean)">collectInheritedEnumerationLiterals</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt; result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned literals from the given enumeration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean)">collectInheritedRealizedInterfaces</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt; result,
 boolean collectOwned)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and directly realized interfaces from the given classifier</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInterfaceRealizations(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">collectInterfaceRealizations</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> contract)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects interface realizations for the given contract</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRealizedInterfacesRecursively(java.util.Collection,java.util.Collection)">collectRealizedInterfacesRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all realized interfaces by the given classifiers and their general classifiers recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">getAllLiterals</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return owned and inherited enumeration literals</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifierOrDerived(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getClassifierOrDerived</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> checkFor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if classifier collection contains given classifier or any derived from it, and returns the first found</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDerivedClassifiers</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get all derived classifiers for given classifier recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDirectDerivedClassifiers</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return classifiers derived directly from the given classifier</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDirectGeneralClassifiers</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns general classifiers from which the given classifier is directly derived.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getGeneralClassifiersRecursively</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> specific)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all general classifiers including the indirect ones up to the hierarchy top.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getPropertiesWithoutRedefined</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets owned and inherited properties without redefined ones.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">getRealizedInterfaces</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all realized interfaces by the given classifier directly.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getSameOrRedefined</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resolves given property to itself or property redefined in the given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isClassifierOfType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Tests if there is at least one classifier among  given ones which isTypeOf (equals or is derived) given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedClassifier</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given classifier "child" is derived from "parent".</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedOrRealizes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if classifier is derived from given type or realizes the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isSameOrDerivedClassifier</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given classifier "child" is same as "parent" or is derived from "parent".</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isSameOrRedefined</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> first,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> second)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given first property is the same as second property or first property is redefined by second property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean)">isSecondTypeCompatibleToFirst</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> firstType,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> secondType,
 boolean checkRealizedInterfaces)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if second parameter type is compatible to the first (is same type or a subtype).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRedefined(java.util.Collection,java.util.Collection...)">removeRedefined</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt; major,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;... additional)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes redefined elements from a given major collection.</div>
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
<h3>Classifiers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Classifiers</span>()</div>
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
<section class="detail" id="getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getDerivedClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getDerivedClassifiers</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</span></div>
<div class="block">Get all derived classifiers for given classifier recursively. Result does not include given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>general</code> - given classifier to collect specific classifiers for</dd>
<dt>Returns:</dt>
<dd>collection of all derived classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>collectDerivedClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">collectDerivedClassifiers</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</span></div>
<div class="block">Collect all derived classifiers recursively (not only the direct children).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>general</code> - general classifier</dd>
<dd><code>result</code> - collection of all derived classifiers</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isClassifierOfType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isClassifierOfType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</span></div>
<div class="block">Tests if there is at least one classifier among  given ones which isTypeOf (equals or is derived) given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - the given classifier</dd>
<dd><code>type</code> - the given type</dd>
<dt>Returns:</dt>
<dd>true if classifiers contains at least one classifier which isTypeOf type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isSameOrDerivedClassifier</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSameOrDerivedClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</span></div>
<div class="block">Checks if given classifier "child" is same as "parent" or is derived from "parent".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent classifier</dd>
<dd><code>child</code> - child classifier</dd>
<dt>Returns:</dt>
<dd>true if same or derived</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>isDerivedClassifier(Classifier, Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isDerivedClassifier</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</span></div>
<div class="block">Checks if given classifier "child" is derived from "parent".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent classifier</dd>
<dd><code>child</code> - child classifier</dd>
<dt>Returns:</dt>
<dd>true if derived</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>isDerivedClassifier(Classifier, Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getDirectDerivedClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getDirectDerivedClassifiers</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</span></div>
<div class="block">Return classifiers derived directly from the given classifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>general</code> - general classifier</dd>
<dt>Returns:</dt>
<dd>collection of direct derived classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifierOrDerived(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getClassifierOrDerived</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getClassifierOrDerived</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> checkFor)</span></div>
<div class="block">Checks if classifier collection contains given classifier or any derived from it, and returns the first found</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - collection of classifiers to look in</dd>
<dd><code>checkFor</code> - target classifier</dd>
<dt>Returns:</dt>
<dd>returns classifier which equals to the given or is derived</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getGeneralClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getGeneralClassifiersRecursively</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> specific)</span></div>
<div class="block">Returns all general classifiers including the indirect ones up to the hierarchy top.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>specific</code> - classifier</dd>
<dt>Returns:</dt>
<dd>general classifiers</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getDirectGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getDirectGeneralClassifiers(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>collectGeneralClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="return-type">void</span> <span class="element-name">collectGeneralClassifiersRecursively</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> specific,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</span></div>
<div class="block">Collects all general classifiers including the indirect ones up to the hierarchy top.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>specific</code> - classifier</dd>
<dd><code>result</code> - general classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectGeneralClassifiersRecursively(java.util.Collection)">
<h3>collectGeneralClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">collectGeneralClassifiersRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</span></div>
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.
 Result includes given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifier</dd>
<dt>Returns:</dt>
<dd>general elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiersRecursively(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getDirectGeneralClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getDirectGeneralClassifiers</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Returns general classifiers from which the given classifier is directly derived.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>direct general classifiers</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiersRecursively(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isDerivedOrRealizes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedOrRealizes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</span></div>
<div class="block">Checks if classifier is derived from given type or realizes the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier to check</dd>
<dd><code>type</code> - type</dd>
<dt>Returns:</dt>
<dd>true if derived or realizes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>getRealizedInterfaces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getRealizedInterfaces</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier)</span></div>
<div class="block">Collects all realized interfaces by the given classifier directly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - given classifier</dd>
<dt>Returns:</dt>
<dd>a collection of realized interfaces(may be empty)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRealizedInterfacesRecursively(java.util.Collection,java.util.Collection)">
<h3>collectRealizedInterfacesRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectRealizedInterfacesRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt; result)</span></div>
<div class="block">Collects all realized interfaces by the given classifiers and their general classifiers recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifiers to collect realized interfaces from</dd>
<dd><code>result</code> - a collection to append interfaces to</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInterfaceRealizations(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>collectInterfaceRealizations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a>&gt;</span> <span class="element-name">collectInterfaceRealizations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> contract)</span></div>
<div class="block">Collects interface realizations for the given contract</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier that might realize the interface</dd>
<dd><code>contract</code> - interface to check realizations for</dd>
<dt>Returns:</dt>
<dd>a collection of interface realizations (may be empty)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean)">
<h3>collectInheritedRealizedInterfaces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedRealizedInterfaces</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt; result,
 boolean collectOwned)</span></div>
<div class="block">Collect inherited and directly realized interfaces from the given classifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean)">
<h3>collectInheritedEnumerationLiterals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedEnumerationLiterals</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt; result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned literals from the given enumeration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumeration</code> - enumeration</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">
<h3>getAllLiterals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt;</span> <span class="element-name">getAllLiterals</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration)</span></div>
<div class="block">Return owned and inherited enumeration literals</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enumeration</code> - enumeration</dd>
<dt>Returns:</dt>
<dd>literals</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getPropertiesWithoutRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getPropertiesWithoutRedefined</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets owned and inherited properties without redefined ones.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifiers from which properties will be collected</dd>
<dt>Returns:</dt>
<dd>owned and inherited properties without redefined ones.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRedefined(java.util.Collection,java.util.Collection...)">
<h3>removeRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeRedefined</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt; major,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;... additional)</span></div>
<div class="block">Removes redefined elements from a given major collection. Major collection is a result. Additional collections are optional and are used only for redefined elements collecting</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>major</code> - elements to remove redefined elements from</dd>
<dd><code>additional</code> - elements to remove redefined elements from</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>isSameOrRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSameOrRedefined</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> first,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> second)</span></div>
<div class="block">Check if given first property is the same as second property or first property is redefined by second property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>first</code> - first property</dd>
<dd><code>second</code> - second property</dd>
<dt>Returns:</dt>
<dd>first is the same as second or is redefined by second</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getSameOrRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSameOrRedefined</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Resolves given property to itself or property redefined in the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>property</code> - property to check</dd>
<dt>Returns:</dt>
<dd>given property or redefined if classifier redefines given property directly or indirectly</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean)">
<h3>isSecondTypeCompatibleToFirst</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSecondTypeCompatibleToFirst</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> firstType,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> secondType,
 boolean checkRealizedInterfaces)</span></div>
<div class="block">Indicates if second parameter type is compatible to the first (is same type or a subtype).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>firstType</code> - parameter, to which the 2nd parameter must be compatible.</dd>
<dd><code>secondType</code> - parameter, which should be compatible to the 1st.</dd>
<dd><code>checkRealizedInterfaces</code> - indicates if realized interfaces should be taken into account when checking type compatibility.</dd>
<dt>Returns:</dt>
<dd>true if parameters are compatible, false otherwise.</dd>
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
