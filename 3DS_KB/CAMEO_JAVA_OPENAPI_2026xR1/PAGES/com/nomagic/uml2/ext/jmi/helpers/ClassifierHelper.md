# JAVA OPENAPI: ClassifierHelper (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/helpers/ClassifierHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/ClassifierHelper.html`
- source_sha256: `52b9580b6dbcc89ee799041ff1408feec41233e414d079963c15d5d9e4ab508d`
- captured_utc: `2026-07-14T16:46:22.676103+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class ClassifierHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.CoreHelper](CoreHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper](ValueSpecificationHelper.html)
com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper

Direct Known Subclasses:
`[InstanceSpecificationHelper](InstanceSpecificationHelper.html)`

@OpenApiAllpublic classClassifierHelper
extends [ValueSpecificationHelper](ValueSpecificationHelper.html)

Utility class for working with UML classifiers

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ClassifierHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[areEqualParameterTypes](#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature1,
 [BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature2)`
Method compares parameters and returns true if parameters types are equals.
`static boolean`
`[areEqualParameterTypes](#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature1,
 [BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature2,
 boolean compareReturnParameter)`
Method compares parameters and returns true if parameters types are equals.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)>`
`[associations](#associations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Get iterator of association from given classifier.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)>`
`[associationsIncludingInherited](#associationsIncludingInherited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Collects connected directly and inherited associations
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[attributes](#attributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Get iterator of Attribute from given classifier.
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[checkForDerivedClassifier](#checkForDerivedClassifier(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) checkFor)`
Checks if there are given classifier or some derived classifier in a given classifier collection.
`static void`
`[collectBaseClassInheritableAttributes](#collectBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned attributes from the given classifier.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)>`
`[collectCommonAssociations](#collectCommonAssociations(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers1,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers2)`
Collect association connected between given classifiers
`static void`
`[collectDerivedClassifiersRecursively](#collectDerivedClassifiersRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> result,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general)`
Collect all derived classifiers recursively (not only the direct children).
`static <T extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[collectGeneralClassifiersAndRealizedInterfacesRecursively](#collectGeneralClassifiersAndRealizedInterfacesRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> result)`
Collects all general classifiers including the indirect ones up to hierarchy top.
`static <T extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[collectGeneralClassifiersRecursively](#collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> result)`
Collects all general classifiers including the indirect ones up to hierarchy top.
`static void`
`[collectInheritedAttributes](#collectInheritedAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned attributes from the given classifier.
`static void`
`[collectInheritedBehaviors](#collectInheritedBehaviors(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean,boolean))([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html)> result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned behaviors from the given classifier
`static void`
`[collectInheritedEnumerationLiterals](#collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean))([Enumeration](../../magicdraw/classes/mdkernel/Enumeration.html) enumeration,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned literals from the given enumeration.
`static void`
`[collectInheritedExtensionPoints](#collectInheritedExtensionPoints(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,java.util.Collection,boolean,boolean))([UseCase](../../magicdraw/mdusecases/UseCase.html) useCase,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned extension points from the given use case.
`static void`
`[collectInheritedOperations](#collectInheritedOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned operations from the given classifier.
`static void`
`[collectInheritedPorts](#collectInheritedPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned ports from the given classifier.
`static void`
`[collectInheritedPureAttributes](#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned)`
Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier.
`static void`
`[collectInheritedPureAttributes](#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier.
`static void`
`[collectInheritedRealizedInterfaces](#collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean))([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned)`
Collect inherited and directly realized interfaces from the given classifier
`static void`
`[collectInheritedReceptions](#collectInheritedReceptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)`
Collect inherited and owned receptions from the given classifier
`static void`
`[collectInheritedRelations](#collectInheritedRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> result,
 boolean collectOwned)`
Collect inherited and directly connected relationships to the classifier
`static void`
`[collectRealizedInterfaces](#collectRealizedInterfaces(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../magicdraw/classes/mdinterfaces/Interface.html)> result)`
Collects realized interfaces by given classifiers.
`static [Property](../../magicdraw/classes/mdkernel/Property.html)`
`[findAssociationEndForType](#findAssociationEndForType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Looks for AssociationEnd connected to the given classifier 'classifier' which can be mapped into 'classifier' attribute
 with name 'name' and type 'type'.
`static [Generalization](../../magicdraw/classes/mdkernel/Generalization.html)`
`[findGeneralization](#findGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) specific)`
Look for generalization between given classifiers.
`static [InterfaceRealization](../../magicdraw/classes/mdinterfaces/InterfaceRealization.html)`
`[findInterfaceRealization](#findInterfaceRealization(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) implementingClass,
 [Interface](../../magicdraw/classes/mdinterfaces/Interface.html) contract)`
Look for interface realization between given class and interface.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EnumerationLiteral](../../magicdraw/classes/mdkernel/EnumerationLiteral.html)>`
`[getAllLiterals](#getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration))([Enumeration](../../magicdraw/classes/mdkernel/Enumeration.html) enumeration)`
Return owned and inherited enumeration literals
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TypedElement](../../magicdraw/classes/mdkernel/TypedElement.html)>`
`[getAssociationEndOwnedByAssociation](#getAssociationEndOwnedByAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Returns a collection of properties connected to given classifier by associations.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getClassifiersIncludingDerived](#getClassifiersIncludingDerived(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> generalClassifiers)`
Returns set of provided classifiers plus directly derived ones
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getClassifiersIncludingDerivedRecursively](#getClassifiersIncludingDerivedRecursively(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers)`
Returns all general classifiers including the indirect ones down to the leafs of the hierarchy.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getClassifiersIncludingGeneralRecursively](#getClassifiersIncludingGeneralRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Returns all general classifiers including the indirect ones up to hierarchy top.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getClassifiersIncludingGeneralRecursively](#getClassifiersIncludingGeneralRecursively(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers)`
Returns all general classifiers including the indirect ones up to hierarchy top.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getDerivedClassifiers](#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general)`
Return classifiers derived directly from the given classifier
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getDerivedClassifiersRecursively](#getDerivedClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general)`
Get all derived classifiers for given classifier.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getGeneralClassifiers](#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Returns general classifiers from which the given classifier is directly derived.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[getGeneralClassifiersRecursively](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Returns all general classifiers including the indirect ones up to hierarchy top.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)>`
`[getImplementedClasses](#getImplementedClasses(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([Interface](../../magicdraw/classes/mdinterfaces/Interface.html) anInterface)`
Gets classifiers which realize (implement) a given interface.
`static int`
`[getInheritanceDeep](#getInheritanceDeep(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets the deep of inherited tree for classifier.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Parameter](../../magicdraw/classes/mdkernel/Parameter.html)>`
`[getParameters](#getParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature)`
Returns parameters without return parameter
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[getPropertiesWithoutRedefined](#getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Gets owned and inherited properties without redefined ones.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../magicdraw/classes/mdinterfaces/Interface.html)>`
`[getProvided](#getProvided(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../magicdraw/classes/mdkernel/Class.html) component)`
Component provided interfaces collection consists of:
 1) interfaces, realized by the component through `InterfaceRealization`,
 2) provided interfaces of the component ports,
 3) component port types which are interfaces.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Interface](../../magicdraw/classes/mdinterfaces/Interface.html)>`
`[getRealizedInterfaces](#getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier)`
Collects realized interfaces by the given classifier.
`static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html)`
`[getReturnParameter](#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature)`
Return parameter of given behaviour feature.
`static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html)`
`[getReturnParameter](#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature,
 boolean create)`
Return parameter of given behaviour feature.
`static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html)`
`[getReturnParameter](#getReturnParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean))([Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean create)`
Return parameter of given behaviour.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Parameter](../../magicdraw/classes/mdkernel/Parameter.html)>`
`[getReturnParameters](#getReturnParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature)`
Returns parameters without return parameter
`static boolean`
`[isBehavioralFeatureEqual](#isBehavioralFeatureEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean))([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature1,
 [BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature2,
 boolean compareReturnParameter)`
Compare the two given features by name and by parameters
`static boolean`
`[isClassifierOfType](#isClassifierOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type)`
Tests if given classifier isTypeOf (equals or is derived) given type.
`static boolean`
`[isClassifierOfType](#isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type)`
Tests if there is at least one classifier among given ones which isTypeOf (equals or is derived) given type.
`static boolean`
`[isDerivedClassifier](#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child)`
Checks if child is derived from parent by generalization
`static boolean`
`[isDerivedOrRealizes](#isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type)`
Checks if classifier is derived from given type or realizes the given type.
`static boolean`
`[isLegalInheritance](#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child)`
Checks if new generalization relationship is legal between given parent and child.
`static boolean`
`[isLegalInheritance](#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Relationship](../../magicdraw/classes/mdkernel/Relationship.html)> ignore)`
Checks if new generalization relationship is legal between given parent and child.
`static boolean`
`[isOperationEqual](#isOperationEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](../../magicdraw/classes/mdkernel/Operation.html) op1,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) op2)`
Compare the two given operation.
`static boolean`
`[isReturnParameter](#isReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter))([Parameter](../../magicdraw/classes/mdkernel/Parameter.html) parameter)`

`static boolean`
`[isSameOrDerivedClassifier](#isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child)`
Checks if given classifier "child" is same as "parent" or is derived from "parent".
`static boolean`
`[isSameOrRedefined](#isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../magicdraw/classes/mdkernel/Property.html) first,
 [Property](../../magicdraw/classes/mdkernel/Property.html) second)`
Check if given first property is the same as second property or first property is redefined by second property
`static boolean`
`[isSecondTypeCompatibleToFirst](#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean))([Type](../../magicdraw/classes/mdkernel/Type.html) firstType,
 [Type](../../magicdraw/classes/mdkernel/Type.html) secondType,
 boolean checkRealizedInterfaces)`
Indicates if second parameter type is compatible to the first (is same type or a subtype).
`static boolean`
`[isSecondTypeCompatibleToFirst](#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.util.Collection,boolean))([Type](../../magicdraw/classes/mdkernel/Type.html) firstType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](../../magicdraw/classes/mdkernel/Type.html)> secondType,
 boolean checkRealizedInterfaces)`
Indicates at least one type from second type collection is compatible to the first type.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)>`
`[operations](#operations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Get iterator of operations from given classifier.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Port](../../magicdraw/compositestructures/mdports/Port.html)>`
`[ports](#ports(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Get iterator of port from given classifier.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)>`
`[pureAttributes](#pureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Get iterator of pure attribute from given classifier.
`static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Reception](../../magicdraw/commonbehaviors/mdcommunications/Reception.html)>`
`[receptions](#receptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Get iterator of reception from given classifier.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)>`
`[removeDerivedClassifiers](#removeDerivedClassifiers(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers)`
Given a collection of classifiers, returns a collection without derived classifiers in their generalization hierarchy.
`static void`
`[removeRedefined](#removeRedefined(java.util.Collection,java.util.Collection...))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../magicdraw/classes/mdkernel/RedefinableElement.html)> major,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../magicdraw/classes/mdkernel/RedefinableElement.html)>... additional)`
Removes redefined elements from a given major collection.
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[ValueSpecificationHelper](ValueSpecificationHelper.html)
`[cloneValueSpecification](ValueSpecificationHelper.html#cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)), [getValueSpecificationClass](ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)), [getValueSpecificationClass](ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)), [getValueSpecificationValue](ValueSpecificationHelper.html#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [getValueString](ValueSpecificationHelper.html#getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [isValueSpecificationClassElementValue](ValueSpecificationHelper.html#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)), [setValueDisposeIfNeeded](ValueSpecificationHelper.html#setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setValueSpecificationValue](ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)), [setValueSpecificationValue](ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean)), [setValueSpecificationValue](ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object))`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[CoreHelper](CoreHelper.html)
`[areElementsEditable](CoreHelper.html#areElementsEditable(java.util.Collection)), [canAddChild](CoreHelper.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)), [canMoveChildInto](CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [canMoveChildInto](CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [collectRelationships](CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [collectRelationships](CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)), [collectRelationshipsByType](CoreHelper.html#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [collectRelationshipsIncludeIndirect](CoreHelper.html#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [dispose](CoreHelper.html#dispose(java.util.Collection)), [findAcceptableParentFor](CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [findAcceptableParentFor](CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [findOwnerOfStrictType](CoreHelper.html#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfStrictTypeIncludingItself](CoreHelper.html#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfType](CoreHelper.html#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfTypeIncludingItself](CoreHelper.html#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findParent](CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [findParent](CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getAdditionalElementsIterator](CoreHelper.html#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getClientElement](CoreHelper.html#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getComment](CoreHelper.html#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getCommentElement](CoreHelper.html#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getCommentElementOrCreate](CoreHelper.html#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getDependentClients](CoreHelper.html#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)), [getDependentSuppliers](CoreHelper.html#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)), [getFirstMemberEnd](CoreHelper.html#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [getMultiplicity](CoreHelper.html#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [getName](CoreHelper.html#getName(com.nomagic.magicdraw.uml.BaseElement)), [getOppositeEnd](CoreHelper.html#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getOwnedElementsIncludingAdditional](CoreHelper.html#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getSecondMemberEnd](CoreHelper.html#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [getSupplierElement](CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getSupplierElement](CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getSupplierElements](CoreHelper.html#getSupplierElements(java.util.Collection)), [hasParentIn](CoreHelper.html#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [isChildOf](CoreHelper.html#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDocumentationComment](CoreHelper.html#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)), [isMultiplicityMany](CoreHelper.html#isMultiplicityMany(int)), [isParentOf](CoreHelper.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](CoreHelper.html#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isRelationship](CoreHelper.html#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isRelationshipAlwaysInClient](CoreHelper.html#isRelationshipAlwaysInClient(java.lang.Class)), [parseMultiplicityString](CoreHelper.html#parseMultiplicityString(java.lang.String)), [setClientElement](CoreHelper.html#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setComment](CoreHelper.html#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [setCommentElement](CoreHelper.html#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)), [setConstraintText](CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)), [setConstraintText](CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)), [setMultiplicity](CoreHelper.html#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setMultiplicity](CoreHelper.html#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setSupplierElement](CoreHelper.html#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ClassifierHelper
public ClassifierHelper()
 ============ METHOD DETAIL ========== 
Method Details
getDerivedClassifiersRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getDerivedClassifiersRecursively([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general)
Get all derived classifiers for given classifier. Result does not include the given classifier.
Parameters:
`general` - given classifier to collect specific classifiers for
Returns:
collection of all derived classifiers
getClassifiersIncludingDerivedRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getClassifiersIncludingDerivedRecursively([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers)
Returns all general classifiers including the indirect ones down to the leafs of the hierarchy.
 Result includes given classifiers.
Parameters:
`classifiers` - classifiers
Returns:
general elements
See Also:
[`getGeneralClassifiersRecursively(Classifier)`](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
collectDerivedClassifiersRecursively
public static void collectDerivedClassifiersRecursively([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> result,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general)
Collect all derived classifiers recursively (not only the direct children).
Parameters:
`result` - collection of all derived classifiers
`general` - general classifier
getDerivedClassifiers
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getDerivedClassifiers(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general)
Return classifiers derived directly from the given classifier
Parameters:
`general` - general classifier
Returns:
collection of derived classifiers
getClassifiersIncludingDerived
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getClassifiersIncludingDerived([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> generalClassifiers)
Returns set of provided classifiers plus directly derived ones
Parameters:
`generalClassifiers` - classifier collection
Returns:
collection of classifiers including derived
See Also:
[`getClassifiersIncludingDerivedRecursively(java.util.Collection<? extends com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier>)`](#getClassifiersIncludingDerivedRecursively(java.util.Collection))
getGeneralClassifiers
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getGeneralClassifiers([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Returns general classifiers from which the given classifier is directly derived.
Parameters:
`classifier` - classifier
Returns:
direct general classifiers
See Also:
[`getGeneralClassifiersRecursively(Classifier)`](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
getGeneralClassifiersRecursively
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getGeneralClassifiersRecursively([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Returns all general classifiers including the indirect ones up to hierarchy top.
 Result does not include the given classifier.
Parameters:
`classifier` - classifier
Returns:
general elements
See Also:
[`getGeneralClassifiers(Classifier)`](#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
getClassifiersIncludingGeneralRecursively
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getClassifiersIncludingGeneralRecursively([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Returns all general classifiers including the indirect ones up to hierarchy top.
 Result includes given classifier.
Parameters:
`classifier` - classifier
Returns:
general elements
See Also:
[`getGeneralClassifiers(Classifier)`](#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
getClassifiersIncludingGeneralRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> getClassifiersIncludingGeneralRecursively([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers)
Returns all general classifiers including the indirect ones up to hierarchy top.
 Result includes given classifiers.
Parameters:
`classifiers` - classifier
Returns:
general elements
See Also:
[`getGeneralClassifiersRecursively(Classifier)`](#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
collectGeneralClassifiersRecursively
public static <T extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collectGeneralClassifiersRecursively([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> result)
Collects all general classifiers including the indirect ones up to hierarchy top.
Parameters:
`classifier` - classifier
`result` - result collection
Returns:
result collection
collectGeneralClassifiersAndRealizedInterfacesRecursively
public static <T extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collectGeneralClassifiersAndRealizedInterfacesRecursively([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> result)
Collects all general classifiers including the indirect ones up to hierarchy top. Also collects all realized interfaces from the collected general classifiers.
Parameters:
`classifier` - classifier
`result` - result collection
Returns:
result collection
getInheritanceDeep
public static int getInheritanceDeep([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets the deep of inherited tree for classifier.
 Used to sort stereotypes by inheritance.
Parameters:
`classifier` - classifier
Returns:
result deep
isLegalInheritance
public static boolean isLegalInheritance([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child)
Checks if new generalization relationship is legal between given parent and child.
 Legal if it does not create cycle and child isKindOf parent.
Parameters:
`parent` - parent element of generalization.
`child` - child element of generalization.
Returns:
true - if generalization is legal, otherwise return false.
isLegalInheritance
public static boolean isLegalInheritance([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Relationship](../../magicdraw/classes/mdkernel/Relationship.html)> ignore)
Checks if new generalization relationship is legal between given parent and child.
 Legal if it does not create cycle and child isKindOf parent.
Parameters:
`parent` - parent element of generalization.
`child` - child element of generalization.
`ignore` - a collection of classifiers that should be ignored.
Returns:
true - if generalization is legal, otherwise return false.
findAssociationEndForType
@CheckForNullpublic static [Property](../../magicdraw/classes/mdkernel/Property.html) findAssociationEndForType([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Looks for AssociationEnd connected to the given classifier 'classifier' which can be mapped into 'classifier' attribute
 with name 'name' and type 'type'.
Parameters:
`classifier` - the given classifier.
`type` - the type of the association end.
`name` - the name of the association end.
Returns:
found AssociationEnd or null.
getReturnParameter
public static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html) getReturnParameter([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature)
Return parameter of given behaviour feature. A new parameter is created if feature does not have it.
Parameters:
`feature` - a given feature
Returns:
return parameter (existing one or created)
isReturnParameter
public static boolean isReturnParameter([Parameter](../../magicdraw/classes/mdkernel/Parameter.html) parameter)
Parameters:
`parameter` - parameter
Returns:
true if given Parameter has return kind
getReturnParameter
@CheckForNullpublic static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html) getReturnParameter([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature,
 boolean create)
Return parameter of given behaviour feature. A new parameter may be created if feature does not have it.
Parameters:
`feature` - a given feature
`create` - creates a new parameter if needed
Returns:
return parameter
getReturnParameter
@CheckForNullpublic static [Parameter](../../magicdraw/classes/mdkernel/Parameter.html) getReturnParameter([Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 boolean create)
Return parameter of given behaviour. A new parameter may be created if behavior does not have it.
Parameters:
`behavior` - a given behavior
`create` - creates a new parameter if needed
Returns:
return parameter
operations
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> operations([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Get iterator of operations from given classifier.
Parameters:
`classifier` - The given classifier.
Returns:
iterator
receptions
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Reception](../../magicdraw/commonbehaviors/mdcommunications/Reception.html)> receptions([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Get iterator of reception from given classifier.
Parameters:
`classifier` - The given classifier.
Returns:
iterator
attributes
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> attributes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Get iterator of Attribute from given classifier.
Parameters:
`classifier` - The given classifier.
Returns:
iterator
ports
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Port](../../magicdraw/compositestructures/mdports/Port.html)> ports([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Get iterator of port from given classifier.
Parameters:
`classifier` - The given classifier.
Returns:
iterator
pureAttributes
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> pureAttributes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Get iterator of pure attribute from given classifier.
Parameters:
`classifier` - The given classifier.
Returns:
iterator
associations
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)> associations([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Get iterator of association from given classifier.
Parameters:
`classifier` - The given classifier.
Returns:
iterator
associationsIncludingInherited
public static [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)> associationsIncludingInherited([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Collects connected directly and inherited associations
Parameters:
`classifier` - classifier
collectInheritedAttributes
public static void collectInheritedAttributes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned attributes from the given classifier.
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectBaseClassInheritableAttributes
public static void collectBaseClassInheritableAttributes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned attributes from the given classifier.
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedPureAttributes
public static void collectInheritedPureAttributes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned)
Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier. Private attributes are collected.
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
collectInheritedPureAttributes
public static void collectInheritedPureAttributes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier.
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedRelations
public static void collectInheritedRelations([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../magicdraw/classes/mdkernel/Element.html)> result,
 boolean collectOwned)
Collect inherited and directly connected relationships to the classifier
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
getAssociationEndOwnedByAssociation
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TypedElement](../../magicdraw/classes/mdkernel/TypedElement.html)> getAssociationEndOwnedByAssociation([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Returns a collection of properties connected to given classifier by associations. Properties are owned by Association
Parameters:
`classifier` - the given classifier
Returns:
collection of properties
collectInheritedPorts
public static void collectInheritedPorts([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned ports from the given classifier.
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedExtensionPoints
public static void collectInheritedExtensionPoints([UseCase](../../magicdraw/mdusecases/UseCase.html) useCase,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned extension points from the given use case.
Parameters:
`useCase` - use case
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedOperations
public static void collectInheritedOperations([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned operations from the given classifier.
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedBehaviors
public static void collectInheritedBehaviors([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html)> result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned behaviors from the given classifier
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedReceptions
public static void collectInheritedReceptions([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned receptions from the given classifier
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
collectInheritedRealizedInterfaces
public static void collectInheritedRealizedInterfaces([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned)
Collect inherited and directly realized interfaces from the given classifier
Parameters:
`classifier` - classifier
`result` - result collection
`collectOwned` - if true, collected also owned
getAllLiterals
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EnumerationLiteral](../../magicdraw/classes/mdkernel/EnumerationLiteral.html)> getAllLiterals([Enumeration](../../magicdraw/classes/mdkernel/Enumeration.html) enumeration)
Return owned and inherited enumeration literals
Parameters:
`enumeration` - enumeration
Returns:
literals
collectInheritedEnumerationLiterals
public static void collectInheritedEnumerationLiterals([Enumeration](../../magicdraw/classes/mdkernel/Enumeration.html) enumeration,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) result,
 boolean collectOwned,
 boolean collectPrivate)
Collect inherited and owned literals from the given enumeration.
Parameters:
`enumeration` - enumeration
`result` - result collection
`collectOwned` - if true, collected also owned
`collectPrivate` - if false, do not collect private
isClassifierOfType
public static boolean isClassifierOfType([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type)
Tests if given classifier isTypeOf (equals or is derived) given type.
Parameters:
`classifier` - the give classifier
`type` - the given type
Returns:
true if classifier isTypeOf type
isClassifierOfType
public static boolean isClassifierOfType([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type)
Tests if there is at least one classifier among given ones which isTypeOf (equals or is derived) given type.
Parameters:
`classifiers` - the given classifier
`type` - the given type
Returns:
true if classifiers contains at least one classifier which isTypeOf type
getRealizedInterfaces
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Interface](../../magicdraw/classes/mdinterfaces/Interface.html)> getRealizedInterfaces([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) classifier)
Collects realized interfaces by the given classifier.
Parameters:
`classifier` - given classifier
Returns:
a collection of realized interfaces(may be empty)
checkForDerivedClassifier
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) checkForDerivedClassifier([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) checkFor)
Checks if there are given classifier or some derived classifier in a given classifier collection.
Parameters:
`classifiers` - collection of classifiers to look in
`checkFor` - target classifier
Returns:
returns classifier which equals to the given or is derived
isSameOrDerivedClassifier
public static boolean isSameOrDerivedClassifier(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 @CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child)
Checks if given classifier "child" is same as "parent" or is derived from "parent".
Parameters:
`parent` - parent classifier
`child` - child classifier
Returns:
true if same or derived
See Also:
[`Classifiers.isDerivedClassifier(Classifier, Classifier)`](../../../../magicdraw/uml2/Classifiers.html#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
isDerivedClassifier
public static boolean isDerivedClassifier(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) parent,
 @CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) child)
Checks if child is derived from parent by generalization
Parameters:
`parent` - parent
`child` - possible parent
Returns:
true if derived
isDerivedOrRealizes
public static boolean isDerivedOrRealizes([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type)
Checks if classifier is derived from given type or realizes the given type.
Parameters:
`classifier` - classifier to check
`type` - type
Returns:
true if derived or realizes
isSecondTypeCompatibleToFirst
public static boolean isSecondTypeCompatibleToFirst([Type](../../magicdraw/classes/mdkernel/Type.html) firstType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](../../magicdraw/classes/mdkernel/Type.html)> secondType,
 boolean checkRealizedInterfaces)
Indicates at least one type from second type collection is compatible to the first type.
Parameters:
`firstType` - type to which types should be checked.
`secondType` - types which should be compared to the first type.
`checkRealizedInterfaces` - indicates if realized interfaces should be taken into account when checking type compatibility.
Returns:
true if parameters are compatible, false otherwise.
isSecondTypeCompatibleToFirst
public static boolean isSecondTypeCompatibleToFirst(@CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) firstType,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) secondType,
 boolean checkRealizedInterfaces)
Indicates if second parameter type is compatible to the first (is same type or a subtype).
Parameters:
`firstType` - parameter, to which the 2nd parameter must be compatible.
`secondType` - parameter, which should be compatible to the 1st.
`checkRealizedInterfaces` - indicates if realized interfaces should be taken into account when checking type compatibility.
Returns:
true if parameters are compatible, false otherwise.
collectRealizedInterfaces
public static void collectRealizedInterfaces([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../magicdraw/classes/mdinterfaces/Interface.html)> result)
Collects realized interfaces by given classifiers.
Parameters:
`classifiers` - classifiers for which realized interfaces should be collected.
`result` - a set in which realized interfaces should be collected.
removeDerivedClassifiers
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> removeDerivedClassifiers([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers)
Given a collection of classifiers, returns a collection without derived classifiers in their generalization hierarchy.
Parameters:
`classifiers` - classifier hierarchy to optimize
Returns:
optimized classifier hierarchy.
isOperationEqual
public static boolean isOperationEqual([Operation](../../magicdraw/classes/mdkernel/Operation.html) op1,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) op2)
Compare the two given operation.
Parameters:
`op1` - First operation.
`op2` - Second operation.
Returns:
boolean
isBehavioralFeatureEqual
public static boolean isBehavioralFeatureEqual([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature1,
 [BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature2,
 boolean compareReturnParameter)
Compare the two given features by name and by parameters
Parameters:
`feature1` - first feature
`feature2` - second feature
`compareReturnParameter` - take into account return parameter(s)
Returns:
true if names are equals and parameters are equals
areEqualParameterTypes
public static boolean areEqualParameterTypes([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature1,
 [BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature2)
Method compares parameters and returns true if parameters types are equals.
Parameters:
`feature1` - feature to be compared with.
`feature2` - feature to be compared with.
Returns:
true if parameters are equals.
areEqualParameterTypes
public static boolean areEqualParameterTypes([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature1,
 [BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature2,
 boolean compareReturnParameter)
Method compares parameters and returns true if parameters types are equals.
Parameters:
`feature1` - feature to be compared with.
`feature2` - feature to be compared with.
`compareReturnParameter` - take into account return parameter(s)
Returns:
true if parameters are equals.
findInterfaceRealization
@CheckForNullpublic static [InterfaceRealization](../../magicdraw/classes/mdinterfaces/InterfaceRealization.html) findInterfaceRealization([BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) implementingClass,
 [Interface](../../magicdraw/classes/mdinterfaces/Interface.html) contract)
Look for interface realization between given class and interface.
Parameters:
`implementingClass` - class
`contract` - interface
findGeneralization
@CheckForNullpublic static [Generalization](../../magicdraw/classes/mdkernel/Generalization.html) findGeneralization([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) general,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) specific)
Look for generalization between given classifiers.
Parameters:
`general` - general classifier
`specific` - specific classifier
getParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Parameter](../../magicdraw/classes/mdkernel/Parameter.html)> getParameters([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature)
Returns parameters without return parameter
Parameters:
`feature` - the given feature
getReturnParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Parameter](../../magicdraw/classes/mdkernel/Parameter.html)> getReturnParameters([BehavioralFeature](../../magicdraw/classes/mdkernel/BehavioralFeature.html) feature)
Returns parameters without return parameter
Parameters:
`feature` - the given feature
collectCommonAssociations
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)> collectCommonAssociations([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers1,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers2)
Collect association connected between given classifiers
Parameters:
`classifiers1` - one classifiers collection
`classifiers2` - second classifiers collection
Returns:
common Associations between two collections of classifiers
getProvided
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../magicdraw/classes/mdinterfaces/Interface.html)> getProvided([Class](../../magicdraw/classes/mdkernel/Class.html) component)
Component provided interfaces collection consists of:
 1) interfaces, realized by the component through `InterfaceRealization`,
 2) provided interfaces of the component ports,
 3) component port types which are interfaces.
Returns:
provided interfaces.
getImplementedClasses
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)> getImplementedClasses([Interface](../../magicdraw/classes/mdinterfaces/Interface.html) anInterface)
Gets classifiers which realize (implement) a given interface.
Parameters:
`anInterface` - an interface for which to get classifiers.
Returns:
list of classifiers which realize a given interface.
removeRedefined
public static void removeRedefined([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../magicdraw/classes/mdkernel/RedefinableElement.html)> major,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [RedefinableElement](../../magicdraw/classes/mdkernel/RedefinableElement.html)>... additional)
Removes redefined elements from a given major collection. Major collection is a result. Additional collections are optional and are used only for redefined elements collecting
Parameters:
`major` - elements to remove redefined elements from
`additional` - elements to remove redefined elements from major
isSameOrRedefined
public static boolean isSameOrRedefined(@CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) first,
 @CheckForNull
 [Property](../../magicdraw/classes/mdkernel/Property.html) second)
Check if given first property is the same as second property or first property is redefined by second property
Parameters:
`first` - first property
`second` - second property
Returns:
first is the same as second or is redefined by second
getPropertiesWithoutRedefined
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> getPropertiesWithoutRedefined([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Gets owned and inherited properties without redefined ones.
Parameters:
`classifier` - classifiers from which properties will be collected
Returns:
owned and inherited properties without redefined ones.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class ClassifierHelper">Class ClassifierHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.CoreHelper</a>
<div class="inheritance"><a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="InstanceSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">InstanceSpecificationHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ClassifierHelper</span>
<span class="extends-implements">extends <a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ValueSpecificationHelper</a></span></div>
<div class="block">Utility class for working with UML classifiers</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ClassifierHelper</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">areEqualParameterTypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature1,
 <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method compares parameters and  returns true if parameters types are equals.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">areEqualParameterTypes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature1,
 <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature2,
 boolean compareReturnParameter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method compares parameters and  returns true if parameters types are equals.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#associations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">associations</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get iterator of association from given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#associationsIncludingInherited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">associationsIncludingInherited</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects connected directly and inherited associations</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#attributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">attributes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get iterator of Attribute from given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkForDerivedClassifier(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">checkForDerivedClassifier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> checkFor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if there are given classifier or some derived classifier in a given classifier collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectBaseClassInheritableAttributes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned attributes from the given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectCommonAssociations(java.util.Collection,java.util.Collection)">collectCommonAssociations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect association connected between given classifiers</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectDerivedClassifiersRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">collectDerivedClassifiersRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; result,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all derived classifiers recursively (not only the direct children).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectGeneralClassifiersAndRealizedInterfacesRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectGeneralClassifiersAndRealizedInterfacesRecursively</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all general classifiers including the indirect ones up to hierarchy top.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectGeneralClassifiersRecursively</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all general classifiers including the indirect ones up to hierarchy top.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedAttributes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned attributes from the given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedBehaviors(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean,boolean)">collectInheritedBehaviors</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt; result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned behaviors from the given classifier</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean)">collectInheritedEnumerationLiterals</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned literals from the given enumeration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedExtensionPoints(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,java.util.Collection,boolean,boolean)">collectInheritedExtensionPoints</a><wbr/>(<a href="../../magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned extension points from the given use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedOperations</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned operations from the given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedPorts</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned ports from the given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)">collectInheritedPureAttributes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedPureAttributes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean)">collectInheritedRealizedInterfaces</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and directly realized interfaces from the given classifier</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedReceptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedReceptions</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and owned receptions from the given classifier</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInheritedRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)">collectInheritedRelations</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; result,
 boolean collectOwned)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect inherited and directly connected relationships to the classifier</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRealizedInterfaces(java.util.Collection,java.util.Collection)">collectRealizedInterfaces</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects realized interfaces by given classifiers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAssociationEndForType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String)">findAssociationEndForType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for AssociationEnd connected to the given classifier 'classifier' which can be mapped into 'classifier' attribute
 with name 'name' and type 'type'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">findGeneralization</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> specific)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Look for generalization between given classifiers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findInterfaceRealization(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">findInterfaceRealization</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> implementingClass,
 <a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> contract)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Look for interface realization between given class and interface.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">getAllLiterals</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return owned and inherited enumeration literals</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationEndOwnedByAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getAssociationEndOwnedByAssociation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a collection of properties connected to given classifier by associations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifiersIncludingDerived(java.util.Collection)">getClassifiersIncludingDerived</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; generalClassifiers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns set of provided classifiers plus directly derived ones</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifiersIncludingDerivedRecursively(java.util.Collection)">getClassifiersIncludingDerivedRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all general classifiers including the indirect ones down to the leafs of the hierarchy.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifiersIncludingGeneralRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getClassifiersIncludingGeneralRecursively</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifiersIncludingGeneralRecursively(java.util.Collection)">getClassifiersIncludingGeneralRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDerivedClassifiers</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return classifiers derived directly from the given classifier</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDerivedClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDerivedClassifiersRecursively</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get all derived classifiers for given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getGeneralClassifiers</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns general classifiers from which the given classifier is directly derived.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getGeneralClassifiersRecursively</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getImplementedClasses(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">getImplementedClasses</a><wbr/>(<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> anInterface)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets classifiers which realize (implement) a given interface.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInheritanceDeep(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getInheritanceDeep</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the deep of inherited tree for classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">getParameters</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns parameters without return parameter</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getPropertiesWithoutRedefined</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets owned and inherited properties without redefined ones.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProvided(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getProvided</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> component)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Component provided interfaces collection consists of:
 1) interfaces, realized by the component through <code>InterfaceRealization</code>,
 2) provided interfaces of the component ports,
 3) component port types which are interfaces.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">getRealizedInterfaces</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects realized interfaces by the given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">getReturnParameter</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return parameter of given behaviour feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">getReturnParameter</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature,
 boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return parameter of given behaviour feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReturnParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean)">getReturnParameter</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean create)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return parameter of given behaviour.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReturnParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">getReturnParameters</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns parameters without return parameter</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isBehavioralFeatureEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">isBehavioralFeatureEqual</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature1,
 <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature2,
 boolean compareReturnParameter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare the two given features by name and by parameters</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isClassifierOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isClassifierOfType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Tests if given classifier isTypeOf (equals or is derived) given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isClassifierOfType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Tests if there is at least one classifier among  given ones which isTypeOf (equals or is derived) given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedClassifier</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if child is derived from parent by generalization</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedOrRealizes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if classifier is derived from given type or realizes the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isLegalInheritance</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if new generalization relationship is legal between given parent and child.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">isLegalInheritance</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a>&gt; ignore)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if new generalization relationship is legal between given parent and child.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOperationEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">isOperationEqual</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> op1,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> op2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare the two given operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">isReturnParameter</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isSameOrDerivedClassifier</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given classifier "child" is same as "parent" or is derived from "parent".</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isSameOrRedefined</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> first,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> second)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given first property is the same as second property or first property is redefined by second property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean)">isSecondTypeCompatibleToFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> firstType,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> secondType,
 boolean checkRealizedInterfaces)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if second parameter type is compatible to the first (is same type or a subtype).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.util.Collection,boolean)">isSecondTypeCompatibleToFirst</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> firstType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt; secondType,
 boolean checkRealizedInterfaces)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates at least one type from second type collection is compatible to the first type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#operations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">operations</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get iterator of operations from given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ports(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">ports</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get iterator of port from given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#pureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">pureAttributes</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get iterator of pure attribute from given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#receptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">receptions</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get iterator of reception from given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDerivedClassifiers(java.util.Collection)">removeDerivedClassifiers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a collection of classifiers, returns a collection without derived classifiers in their generalization hierarchy.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRedefined(java.util.Collection,java.util.Collection...)">removeRedefined</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt; major,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;... additional)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes redefined elements from a given major collection.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ValueSpecificationHelper</a></h3>
<code><a href="ValueSpecificationHelper.html#cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">cloneValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">getValueSpecificationClass</a>, <a href="ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">getValueSpecificationClass</a>, <a href="ValueSpecificationHelper.html#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueSpecificationValue</a>, <a href="ValueSpecificationHelper.html#getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueString</a>, <a href="ValueSpecificationHelper.html#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">isValueSpecificationClassElementValue</a>, <a href="ValueSpecificationHelper.html#setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setValueDisposeIfNeeded</a>, <a href="ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">setValueSpecificationValue</a>, <a href="ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean)">setValueSpecificationValue</a>, <a href="ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object)">setValueSpecificationValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.CoreHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">CoreHelper</a></h3>
<code><a href="CoreHelper.html#areElementsEditable(java.util.Collection)">areElementsEditable</a>, <a href="CoreHelper.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">canAssignName</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)">canAssignName</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)">canAssignName</a>, <a href="CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canMoveChildInto</a>, <a href="CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">canMoveChildInto</a>, <a href="CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationships</a>, <a href="CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)">collectRelationships</a>, <a href="CoreHelper.html#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">collectRelationshipsByType</a>, <a href="CoreHelper.html#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationshipsIncludeIndirect</a>, <a href="CoreHelper.html#dispose(java.util.Collection)">dispose</a>, <a href="CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findAcceptableParentFor</a>, <a href="CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findAcceptableParentFor</a>, <a href="CoreHelper.html#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictType</a>, <a href="CoreHelper.html#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictTypeIncludingItself</a>, <a href="CoreHelper.html#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfType</a>, <a href="CoreHelper.html#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfTypeIncludingItself</a>, <a href="CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findParent</a>, <a href="CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findParent</a>, <a href="CoreHelper.html#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAdditionalElementsIterator</a>, <a href="CoreHelper.html#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClientElement</a>, <a href="CoreHelper.html#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComment</a>, <a href="CoreHelper.html#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElement</a>, <a href="CoreHelper.html#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElementOrCreate</a>, <a href="CoreHelper.html#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentClients</a>, <a href="CoreHelper.html#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentSuppliers</a>, <a href="CoreHelper.html#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getFirstMemberEnd</a>, <a href="CoreHelper.html#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">getMultiplicity</a>, <a href="CoreHelper.html#getName(com.nomagic.magicdraw.uml.BaseElement)">getName</a>, <a href="CoreHelper.html#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOppositeEnd</a>, <a href="CoreHelper.html#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getOwnedElementsIncludingAdditional</a>, <a href="CoreHelper.html#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getSecondMemberEnd</a>, <a href="CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSupplierElement</a>, <a href="CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getSupplierElement</a>, <a href="CoreHelper.html#getSupplierElements(java.util.Collection)">getSupplierElements</a>, <a href="CoreHelper.html#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">hasParentIn</a>, <a href="CoreHelper.html#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isChildOf</a>, <a href="CoreHelper.html#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">isDocumentationComment</a>, <a href="CoreHelper.html#isMultiplicityMany(int)">isMultiplicityMany</a>, <a href="CoreHelper.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="CoreHelper.html#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isParentOf</a>, <a href="CoreHelper.html#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRelationship</a>, <a href="CoreHelper.html#isRelationshipAlwaysInClient(java.lang.Class)">isRelationshipAlwaysInClient</a>, <a href="CoreHelper.html#parseMultiplicityString(java.lang.String)">parseMultiplicityString</a>, <a href="CoreHelper.html#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setClientElement</a>, <a href="CoreHelper.html#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setComment</a>, <a href="CoreHelper.html#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">setCommentElement</a>, <a href="CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)">setConstraintText</a>, <a href="CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)">setConstraintText</a>, <a href="CoreHelper.html#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a>, <a href="CoreHelper.html#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a>, <a href="CoreHelper.html#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSupplierElement</a></code></div>
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
<h3>ClassifierHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassifierHelper</span>()</div>
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
<section class="detail" id="getDerivedClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getDerivedClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getDerivedClassifiersRecursively</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</span></div>
<div class="block">Get all derived classifiers for given classifier. Result does not include the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>general</code> - given classifier to collect specific classifiers for</dd>
<dt>Returns:</dt>
<dd>collection of all derived classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifiersIncludingDerivedRecursively(java.util.Collection)">
<h3>getClassifiersIncludingDerivedRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getClassifiersIncludingDerivedRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</span></div>
<div class="block">Returns all general classifiers including the indirect ones down to the leafs of the hierarchy.
 Result includes given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifiers</dd>
<dt>Returns:</dt>
<dd>general elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiersRecursively(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectDerivedClassifiersRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>collectDerivedClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectDerivedClassifiersRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; result,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</span></div>
<div class="block">Collect all derived classifiers recursively (not only the direct children).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>result</code> - collection of all derived classifiers</dd>
<dd><code>general</code> - general classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getDerivedClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getDerivedClassifiers</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general)</span></div>
<div class="block">Return classifiers derived directly from the given classifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>general</code> - general classifier</dd>
<dt>Returns:</dt>
<dd>collection of derived classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifiersIncludingDerived(java.util.Collection)">
<h3>getClassifiersIncludingDerived</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getClassifiersIncludingDerived</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; generalClassifiers)</span></div>
<div class="block">Returns set of provided classifiers plus directly derived ones</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>generalClassifiers</code> - classifier collection</dd>
<dt>Returns:</dt>
<dd>collection of classifiers including derived</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#getClassifiersIncludingDerivedRecursively(java.util.Collection)"><code>getClassifiersIncludingDerivedRecursively(java.util.Collection&lt;? extends com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier&gt;)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getGeneralClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getGeneralClassifiers</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Returns general classifiers from which the given classifier is directly derived.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>direct general classifiers</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiersRecursively(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getGeneralClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getGeneralClassifiersRecursively</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.
 Result does not include the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>general elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiers(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifiersIncludingGeneralRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getClassifiersIncludingGeneralRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getClassifiersIncludingGeneralRecursively</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.
 Result includes given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>general elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiers(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifiersIncludingGeneralRecursively(java.util.Collection)">
<h3>getClassifiersIncludingGeneralRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getClassifiersIncludingGeneralRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</span></div>
<div class="block">Returns all general classifiers including the indirect ones up to hierarchy top.
 Result includes given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifier</dd>
<dt>Returns:</dt>
<dd>general elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>getGeneralClassifiersRecursively(Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>collectGeneralClassifiersRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">collectGeneralClassifiersRecursively</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</span></div>
<div class="block">Collects all general classifiers including the indirect ones up to hierarchy top.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dt>Returns:</dt>
<dd>result collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectGeneralClassifiersAndRealizedInterfacesRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>collectGeneralClassifiersAndRealizedInterfacesRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">collectGeneralClassifiersAndRealizedInterfacesRecursively</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; result)</span></div>
<div class="block">Collects all general classifiers including the indirect ones up to hierarchy top. Also collects all realized interfaces from the collected general classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dt>Returns:</dt>
<dd>result collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritanceDeep(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getInheritanceDeep</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getInheritanceDeep</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets the deep of inherited tree for classifier.
 Used to sort stereotypes by inheritance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>result deep</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isLegalInheritance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLegalInheritance</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</span></div>
<div class="block">Checks if new generalization relationship is legal between given parent and child.
 Legal if it does not create cycle and child isKindOf parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent element of generalization.</dd>
<dd><code>child</code> - child element of generalization.</dd>
<dt>Returns:</dt>
<dd>true - if generalization is legal, otherwise return false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>isLegalInheritance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLegalInheritance</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a>&gt; ignore)</span></div>
<div class="block">Checks if new generalization relationship is legal between given parent and child.
 Legal if it does not create cycle and child isKindOf parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent element of generalization.</dd>
<dd><code>child</code> - child element of generalization.</dd>
<dd><code>ignore</code> - a collection of classifiers that should be ignored.</dd>
<dt>Returns:</dt>
<dd>true - if generalization is legal, otherwise return false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAssociationEndForType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String)">
<h3>findAssociationEndForType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">findAssociationEndForType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Looks for AssociationEnd connected to the given classifier 'classifier' which can be mapped into 'classifier' attribute
 with name 'name' and type 'type'.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the given classifier.</dd>
<dd><code>type</code> - the type of the association end.</dd>
<dd><code>name</code> - the name of the association end.</dd>
<dt>Returns:</dt>
<dd>found AssociationEnd or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>getReturnParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">getReturnParameter</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature)</span></div>
<div class="block">Return parameter of given behaviour feature. A new parameter is created if feature does not have it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a given feature</dd>
<dt>Returns:</dt>
<dd>return parameter (existing one or created)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">
<h3>isReturnParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isReturnParameter</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameter</code> - parameter</dd>
<dt>Returns:</dt>
<dd>true if given Parameter has return kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">
<h3>getReturnParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">getReturnParameter</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature,
 boolean create)</span></div>
<div class="block">Return parameter of given behaviour feature. A new parameter may be created if feature does not have it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - a given feature</dd>
<dd><code>create</code> - creates a new parameter if needed</dd>
<dt>Returns:</dt>
<dd>return parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReturnParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean)">
<h3>getReturnParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">getReturnParameter</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 boolean create)</span></div>
<div class="block">Return parameter of given behaviour. A new parameter may be created if behavior does not have it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - a given behavior</dd>
<dd><code>create</code> - creates a new parameter if needed</dd>
<dt>Returns:</dt>
<dd>return parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="operations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>operations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">operations</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Get iterator of operations from given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - The given classifier.</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="receptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>receptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</span> <span class="element-name">receptions</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Get iterator of reception from given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - The given classifier.</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="attributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>attributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">attributes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Get iterator of Attribute from given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - The given classifier.</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ports(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>ports</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</span> <span class="element-name">ports</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Get iterator of port from given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - The given classifier.</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="pureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>pureAttributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">pureAttributes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Get iterator of pure attribute from given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - The given classifier.</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="associations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>associations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</span> <span class="element-name">associations</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Get iterator of association from given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - The given classifier.</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="associationsIncludingInherited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>associationsIncludingInherited</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</span> <span class="element-name">associationsIncludingInherited</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Collects connected directly and inherited associations</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">
<h3>collectInheritedAttributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedAttributes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned attributes from the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">
<h3>collectBaseClassInheritableAttributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectBaseClassInheritableAttributes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned attributes from the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)">
<h3>collectInheritedPureAttributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedPureAttributes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned)</span></div>
<div class="block">Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier. Private attributes are collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">
<h3>collectInheritedPureAttributes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedPureAttributes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned attributes (just Property, not Port and etc) from the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)">
<h3>collectInheritedRelations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedRelations</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; result,
 boolean collectOwned)</span></div>
<div class="block">Collect inherited and directly connected relationships to the classifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationEndOwnedByAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getAssociationEndOwnedByAssociation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a>&gt;</span> <span class="element-name">getAssociationEndOwnedByAssociation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Returns a collection of properties connected to given classifier by associations. Properties are owned by Association</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the given classifier</dd>
<dt>Returns:</dt>
<dd>collection of properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">
<h3>collectInheritedPorts</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedPorts</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned ports from the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedExtensionPoints(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,java.util.Collection,boolean,boolean)">
<h3>collectInheritedExtensionPoints</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedExtensionPoints</span><wbr/><span class="parameters">(<a href="../../magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned extension points from the given use case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - use case</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">
<h3>collectInheritedOperations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedOperations</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned operations from the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedBehaviors(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean,boolean)">
<h3>collectInheritedBehaviors</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedBehaviors</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt; result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned behaviors from the given classifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedReceptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">
<h3>collectInheritedReceptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedReceptions</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
 boolean collectOwned,
 boolean collectPrivate)</span></div>
<div class="block">Collect inherited and owned receptions from the given classifier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>result</code> - result collection</dd>
<dd><code>collectOwned</code> - if true, collected also owned</dd>
<dd><code>collectPrivate</code> - if false, do not collect private</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean)">
<h3>collectInheritedRealizedInterfaces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedRealizedInterfaces</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
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
<section class="detail" id="getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">
<h3>getAllLiterals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a>&gt;</span> <span class="element-name">getAllLiterals</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration)</span></div>
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
<section class="detail" id="collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean)">
<h3>collectInheritedEnumerationLiterals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectInheritedEnumerationLiterals</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a> enumeration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> result,
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
<section class="detail" id="isClassifierOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isClassifierOfType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isClassifierOfType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</span></div>
<div class="block">Tests if given classifier isTypeOf (equals or is derived) given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the give classifier</dd>
<dd><code>type</code> - the given type</dd>
<dt>Returns:</dt>
<dd>true if classifier isTypeOf type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isClassifierOfType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isClassifierOfType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</span></div>
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
<section class="detail" id="getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>getRealizedInterfaces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getRealizedInterfaces</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> classifier)</span></div>
<div class="block">Collects realized interfaces by the given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - given classifier</dd>
<dt>Returns:</dt>
<dd>a collection of realized interfaces(may be empty)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkForDerivedClassifier(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>checkForDerivedClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">checkForDerivedClassifier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> checkFor)</span></div>
<div class="block">Checks if there are given classifier or some derived classifier in a given classifier collection.</div>
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
<section class="detail" id="isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isSameOrDerivedClassifier</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSameOrDerivedClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</span></div>
<div class="block">Checks if given classifier "child" is same as "parent" or is derived from "parent".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent classifier</dd>
<dd><code>child</code> - child classifier</dd>
<dt>Returns:</dt>
<dd>true if same or derived</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../../../magicdraw/uml2/Classifiers.html#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>Classifiers.isDerivedClassifier(Classifier, Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isDerivedClassifier</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> parent,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> child)</span></div>
<div class="block">Checks if child is derived from parent by generalization</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent</dd>
<dd><code>child</code> - possible parent</dd>
<dt>Returns:</dt>
<dd>true if derived</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>isDerivedOrRealizes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDerivedOrRealizes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type)</span></div>
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
<section class="detail" id="isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.util.Collection,boolean)">
<h3>isSecondTypeCompatibleToFirst</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSecondTypeCompatibleToFirst</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> firstType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt; secondType,
 boolean checkRealizedInterfaces)</span></div>
<div class="block">Indicates at least one type from second type collection is compatible to the first type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>firstType</code> - type to which types should be checked.</dd>
<dd><code>secondType</code> - types which should be compared to the first type.</dd>
<dd><code>checkRealizedInterfaces</code> - indicates if realized interfaces should be taken into account when checking type compatibility.</dd>
<dt>Returns:</dt>
<dd>true if parameters are compatible, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean)">
<h3>isSecondTypeCompatibleToFirst</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSecondTypeCompatibleToFirst</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> firstType,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> secondType,
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
<li>
<section class="detail" id="collectRealizedInterfaces(java.util.Collection,java.util.Collection)">
<h3>collectRealizedInterfaces</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collectRealizedInterfaces</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt; result)</span></div>
<div class="block">Collects realized interfaces by given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifiers for which realized interfaces should be collected.</dd>
<dd><code>result</code> - a set in which realized interfaces should be collected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeDerivedClassifiers(java.util.Collection)">
<h3>removeDerivedClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">removeDerivedClassifiers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers)</span></div>
<div class="block">Given a collection of classifiers, returns a collection without derived classifiers in their generalization hierarchy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifier hierarchy to optimize</dd>
<dt>Returns:</dt>
<dd>optimized classifier hierarchy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOperationEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>isOperationEqual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOperationEqual</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> op1,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> op2)</span></div>
<div class="block">Compare the two given operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>op1</code> - First operation.</dd>
<dd><code>op2</code> - Second operation.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBehavioralFeatureEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">
<h3>isBehavioralFeatureEqual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBehavioralFeatureEqual</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature1,
 <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature2,
 boolean compareReturnParameter)</span></div>
<div class="block">Compare the two given features by name and by parameters</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature1</code> - first feature</dd>
<dd><code>feature2</code> - second feature</dd>
<dd><code>compareReturnParameter</code> - take into account return parameter(s)</dd>
<dt>Returns:</dt>
<dd>true if names are equals and parameters are equals</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>areEqualParameterTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">areEqualParameterTypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature1,
 <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature2)</span></div>
<div class="block">Method compares parameters and  returns true if parameters types are equals.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature1</code> - feature to be compared with.</dd>
<dd><code>feature2</code> - feature to be compared with.</dd>
<dt>Returns:</dt>
<dd>true if parameters are equals.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">
<h3>areEqualParameterTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">areEqualParameterTypes</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature1,
 <a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature2,
 boolean compareReturnParameter)</span></div>
<div class="block">Method compares parameters and  returns true if parameters types are equals.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature1</code> - feature to be compared with.</dd>
<dd><code>feature2</code> - feature to be compared with.</dd>
<dd><code>compareReturnParameter</code> - take into account return parameter(s)</dd>
<dt>Returns:</dt>
<dd>true if parameters are equals.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findInterfaceRealization(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>findInterfaceRealization</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></span> <span class="element-name">findInterfaceRealization</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> implementingClass,
 <a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> contract)</span></div>
<div class="block">Look for interface realization between given class and interface.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>implementingClass</code> - class</dd>
<dd><code>contract</code> - interface</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>findGeneralization</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a></span> <span class="element-name">findGeneralization</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> general,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> specific)</span></div>
<div class="block">Look for generalization between given classifiers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>general</code> - general classifier</dd>
<dd><code>specific</code> - specific classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>getParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</span> <span class="element-name">getParameters</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature)</span></div>
<div class="block">Returns parameters without return parameter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the given feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReturnParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>getReturnParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</span> <span class="element-name">getReturnParameters</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> feature)</span></div>
<div class="block">Returns parameters without return parameter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the given feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectCommonAssociations(java.util.Collection,java.util.Collection)">
<h3>collectCommonAssociations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</span> <span class="element-name">collectCommonAssociations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers2)</span></div>
<div class="block">Collect association connected between given classifiers</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers1</code> - one classifiers collection</dd>
<dd><code>classifiers2</code> - second classifiers collection</dd>
<dt>Returns:</dt>
<dd>common Associations between two collections of classifiers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProvided(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>getProvided</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getProvided</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> component)</span></div>
<div class="block">Component provided interfaces collection consists of:
 1) interfaces, realized by the component through <code>InterfaceRealization</code>,
 2) provided interfaces of the component ports,
 3) component port types which are interfaces.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>provided interfaces.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImplementedClasses(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>getImplementedClasses</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a>&gt;</span> <span class="element-name">getImplementedClasses</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> anInterface)</span></div>
<div class="block">Gets classifiers which realize (implement) a given interface.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>anInterface</code> - an interface for which to get classifiers.</dd>
<dt>Returns:</dt>
<dd>list of classifiers which realize a given interface.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRedefined(java.util.Collection,java.util.Collection...)">
<h3>removeRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeRedefined</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt; major,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;... additional)</span></div>
<div class="block">Removes redefined elements from a given major collection. Major collection is a result. Additional collections are optional and are used only for redefined elements collecting</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>major</code> - elements to remove redefined elements from</dd>
<dd><code>additional</code> - elements to remove redefined elements from major</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>isSameOrRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSameOrRedefined</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> first,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> second)</span></div>
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
<section class="detail" id="getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getPropertiesWithoutRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getPropertiesWithoutRedefined</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Gets owned and inherited properties without redefined ones.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifiers from which properties will be collected</dd>
<dt>Returns:</dt>
<dd>owned and inherited properties without redefined ones.</dd>
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
