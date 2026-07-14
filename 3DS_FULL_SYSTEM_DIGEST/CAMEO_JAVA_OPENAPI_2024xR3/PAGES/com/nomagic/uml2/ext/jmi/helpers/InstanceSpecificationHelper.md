# JAVA OPENAPI: InstanceSpecificationHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/InstanceSpecificationHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/InstanceSpecificationHelper.html`
- source_sha256: `c1e856f2d1f17e4b31e4d3ef98ba750e956437df5c31383ffd5bcd534953a65b`
- captured_utc: `2026-07-14T16:56:15.909687+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class InstanceSpecificationHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.CoreHelper](CoreHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper](ValueSpecificationHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper](ClassifierHelper.html)
com.nomagic.uml2.ext.jmi.helpers.InstanceSpecificationHelper

Direct Known Subclasses:
`[ModelHelper](ModelHelper.html)`

@OpenApiAllpublic classInstanceSpecificationHelper
extends [ClassifierHelper](ClassifierHelper.html)

An utility class with utility methods operating on InstanceSpecification domain elements

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[InstanceSpecificationHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html)>`
`[collectAllInstances](#collectAllInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html)> result)`
Collect all instances of given classifier.
`static [Slot](../../magicdraw/classes/mdkernel/Slot.html)`
`[createSlot](#createSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean createDefaultValue)`
Creates slot for property
`static void`
`[createSlotsForDefaultValues](#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createAll)`
Creates slots for properties of all assigned classifiers to instance.
`static void`
`[createSlotsForDefaultValues](#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 boolean createAll)`
Creates slots for properties of given classifier.
`static [Slot](../../magicdraw/classes/mdkernel/Slot.html)`
`[findSlot](#findSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property)`
Looks for existing slot for a given property in given instance.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)>`
`[getAssignableAssociationsForLink](#getAssignableAssociationsForLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) clientInstance,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) supplierInstance)`
Gets available associations which are allowed to assign for a link.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)>`
`[getAssociationOfLink](#getAssociationOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance)`
Gets Association classifier from Link InstanceSpecification, if exists.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html)>`
`[getLinksBetweenInstances](#getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) client,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) supplier)`
Returns links found between client and supplier instances
`static [Slot](../../magicdraw/classes/mdkernel/Slot.html)`
`[getNestedSlot](#getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> path,
 int index)`

`static [Slot](../../magicdraw/classes/mdkernel/Slot.html)`
`[getSlot](#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean createSlotIfNotExists)`
Returns existing of creates a new Slot for the given property.
`static [Slot](../../magicdraw/classes/mdkernel/Slot.html)`
`[getSlot](#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)`
Returns existing of creates a new Slot for the given property
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValueBySlot](#getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))([Slot](../../magicdraw/classes/mdkernel/Slot.html) slot)`
Retrieves values of slots as object, not as ValueSpecifications.
`static boolean`
`[isInstanceSpecificationCompatibleWithType](#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance)`
Checks if given instance specification is compatible with given Type.
`static boolean`
`[isInstanceSpecificationCompatibleWithType](#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean checkInherited)`
Checks if given instance specification is compatible with given Type.
`static boolean`
`[isLink](#isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance)`
Checks if InstanceSpecification is Link.
`static void`
`[setClassifierForInstanceSpecification](#setClassifierForInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createSlots)`
Set classifier for instance
`static void`
`[setClassifierForInstanceSpecification](#setClassifierForInstanceSpecification(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createSlots)`
Set classifiers for instance
`static void`
`[setSlotValue](#setSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,java.lang.String))([Slot](../../magicdraw/classes/mdkernel/Slot.html) slot,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Set slot value from a given string.
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[ClassifierHelper](ClassifierHelper.html)
`[areEqualParameterTypes](ClassifierHelper.html#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)), [areEqualParameterTypes](ClassifierHelper.html#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)), [associations](ClassifierHelper.html#associations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [associationsIncludingInherited](ClassifierHelper.html#associationsIncludingInherited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [attributes](ClassifierHelper.html#attributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [checkForDerivedClassifier](ClassifierHelper.html#checkForDerivedClassifier(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [collectBaseClassInheritableAttributes](ClassifierHelper.html#collectBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)), [collectCommonAssociations](ClassifierHelper.html#collectCommonAssociations(java.util.Collection,java.util.Collection)), [collectDerivedClassifiersRecursively](ClassifierHelper.html#collectDerivedClassifiersRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [collectGeneralClassifiersAndRealizedInterfacesRecursively](ClassifierHelper.html#collectGeneralClassifiersAndRealizedInterfacesRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)), [collectGeneralClassifiersRecursively](ClassifierHelper.html#collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)), [collectInheritedAttributes](ClassifierHelper.html#collectInheritedAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)), [collectInheritedBehaviors](ClassifierHelper.html#collectInheritedBehaviors(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean,boolean)), [collectInheritedEnumerationLiterals](ClassifierHelper.html#collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean)), [collectInheritedExtensionPoints](ClassifierHelper.html#collectInheritedExtensionPoints(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,java.util.Collection,boolean,boolean)), [collectInheritedOperations](ClassifierHelper.html#collectInheritedOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)), [collectInheritedPorts](ClassifierHelper.html#collectInheritedPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)), [collectInheritedPureAttributes](ClassifierHelper.html#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)), [collectInheritedPureAttributes](ClassifierHelper.html#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)), [collectInheritedRealizedInterfaces](ClassifierHelper.html#collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean)), [collectInheritedReceptions](ClassifierHelper.html#collectInheritedReceptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)), [collectInheritedRelations](ClassifierHelper.html#collectInheritedRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)), [collectRealizedInterfaces](ClassifierHelper.html#collectRealizedInterfaces(java.util.Collection,java.util.Collection)), [findAssociationEndForType](ClassifierHelper.html#findAssociationEndForType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String)), [findGeneralization](ClassifierHelper.html#findGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [findInterfaceRealization](ClassifierHelper.html#findInterfaceRealization(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [getAllLiterals](ClassifierHelper.html#getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)), [getAssociationEndOwnedByAssociation](ClassifierHelper.html#getAssociationEndOwnedByAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getClassifiersIncludingDerived](ClassifierHelper.html#getClassifiersIncludingDerived(java.util.Collection)), [getClassifiersIncludingDerivedRecursively](ClassifierHelper.html#getClassifiersIncludingDerivedRecursively(java.util.Collection)), [getClassifiersIncludingGeneralRecursively](ClassifierHelper.html#getClassifiersIncludingGeneralRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getClassifiersIncludingGeneralRecursively](ClassifierHelper.html#getClassifiersIncludingGeneralRecursively(java.util.Collection)), [getDerivedClassifiers](ClassifierHelper.html#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getDerivedClassifiersRecursively](ClassifierHelper.html#getDerivedClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getGeneralClassifiers](ClassifierHelper.html#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getGeneralClassifiersRecursively](ClassifierHelper.html#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getImplementedClasses](ClassifierHelper.html#getImplementedClasses(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [getInheritanceDeep](ClassifierHelper.html#getInheritanceDeep(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getParameters](ClassifierHelper.html#getParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)), [getPropertiesWithoutRedefined](ClassifierHelper.html#getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [getProvided](ClassifierHelper.html#getProvided(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)), [getRealizedInterfaces](ClassifierHelper.html#getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)), [getReturnParameter](ClassifierHelper.html#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)), [getReturnParameter](ClassifierHelper.html#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)), [getReturnParameter](ClassifierHelper.html#getReturnParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean)), [getReturnParameters](ClassifierHelper.html#getReturnParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)), [isBehavioralFeatureEqual](ClassifierHelper.html#isBehavioralFeatureEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)), [isClassifierOfType](ClassifierHelper.html#isClassifierOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [isClassifierOfType](ClassifierHelper.html#isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [isDerivedClassifier](ClassifierHelper.html#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [isDerivedOrRealizes](ClassifierHelper.html#isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [isLegalInheritance](ClassifierHelper.html#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [isLegalInheritance](ClassifierHelper.html#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)), [isOperationEqual](ClassifierHelper.html#isOperationEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)), [isReturnParameter](ClassifierHelper.html#isReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)), [isSameOrDerivedClassifier](ClassifierHelper.html#isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [isSameOrRedefined](ClassifierHelper.html#isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [isSecondTypeCompatibleToFirst](ClassifierHelper.html#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean)), [isSecondTypeCompatibleToFirst](ClassifierHelper.html#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.util.Collection,boolean)), [operations](ClassifierHelper.html#operations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [ports](ClassifierHelper.html#ports(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [pureAttributes](ClassifierHelper.html#pureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [receptions](ClassifierHelper.html#receptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [removeDerivedClassifiers](ClassifierHelper.html#removeDerivedClassifiers(java.util.Collection)), [removeRedefined](ClassifierHelper.html#removeRedefined(java.util.Collection,java.util.Collection...))`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[ValueSpecificationHelper](ValueSpecificationHelper.html)
`[cloneValueSpecification](ValueSpecificationHelper.html#cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)), [createValueSpecification](ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)), [getValueSpecificationClass](ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)), [getValueSpecificationClass](ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)), [getValueSpecificationValue](ValueSpecificationHelper.html#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [getValueString](ValueSpecificationHelper.html#getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [isValueSpecificationClassElementValue](ValueSpecificationHelper.html#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)), [setValueDisposeIfNeeded](ValueSpecificationHelper.html#setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setValueSpecificationValue](ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)), [setValueSpecificationValue](ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean)), [setValueSpecificationValue](ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object))`
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[CoreHelper](CoreHelper.html)
`[areElementsEditable](CoreHelper.html#areElementsEditable(java.util.Collection)), [canAddChild](CoreHelper.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)), [canMoveChildInto](CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [canMoveChildInto](CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [collectRelationships](CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [collectRelationships](CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)), [collectRelationshipsByType](CoreHelper.html#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [collectRelationshipsIncludeIndirect](CoreHelper.html#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [dispose](CoreHelper.html#dispose(java.util.Collection)), [findAcceptableParentFor](CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [findAcceptableParentFor](CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [findOwnerOfStrictType](CoreHelper.html#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfStrictTypeIncludingItself](CoreHelper.html#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfType](CoreHelper.html#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfTypeIncludingItself](CoreHelper.html#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findParent](CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [findParent](CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getAdditionalElementsIterator](CoreHelper.html#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getClientElement](CoreHelper.html#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getComment](CoreHelper.html#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getCommentElement](CoreHelper.html#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getCommentElementOrCreate](CoreHelper.html#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getDependentClients](CoreHelper.html#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)), [getDependentSuppliers](CoreHelper.html#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)), [getFirstMemberEnd](CoreHelper.html#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [getMultiplicity](CoreHelper.html#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [getName](CoreHelper.html#getName(com.nomagic.magicdraw.uml.BaseElement)), [getOppositeEnd](CoreHelper.html#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getOwnedElementsIncludingAdditional](CoreHelper.html#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getSecondMemberEnd](CoreHelper.html#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [getSupplierElement](CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getSupplierElement](CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getSupplierElements](CoreHelper.html#getSupplierElements(java.util.Collection)), [hasParentIn](CoreHelper.html#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [isChildOf](CoreHelper.html#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDocumentationComment](CoreHelper.html#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)), [isMultiplicityMany](CoreHelper.html#isMultiplicityMany(int)), [isParentOf](CoreHelper.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](CoreHelper.html#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isRelationship](CoreHelper.html#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isRelationshipAlwaysInClient](CoreHelper.html#isRelationshipAlwaysInClient(java.lang.Class)), [parseMultiplicityString](CoreHelper.html#parseMultiplicityString(java.lang.String)), [setClientElement](CoreHelper.html#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setComment](CoreHelper.html#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [setCommentElement](CoreHelper.html#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)), [setConstraintText](CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)), [setConstraintText](CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)), [setMultiplicity](CoreHelper.html#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setMultiplicity](CoreHelper.html#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setSupplierElement](CoreHelper.html#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
InstanceSpecificationHelper
public InstanceSpecificationHelper()
 ============ METHOD DETAIL ========== 
Method Details
findSlot
@CheckForNullpublic static [Slot](../../magicdraw/classes/mdkernel/Slot.html) findSlot([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property)
Looks for existing slot for a given property in given instance.
Parameters:
`instanceSpecification` - instance
`property` - definingFeature of slot
Returns:
found slot or null
getSlot
@CheckForNullpublic static [Slot](../../magicdraw/classes/mdkernel/Slot.html) getSlot([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean createSlotIfNotExists)
Returns existing of creates a new Slot for the given property. If new Slot is created, it will be filled with value from the property default values.
Parameters:
`instance` - instance specification
`property` - feature
`createSlotIfNotExists` - create a new slot if needed
Returns:
slot
getSlot
@CheckForNullpublic static [Slot](../../magicdraw/classes/mdkernel/Slot.html) getSlot([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)
Returns existing of creates a new Slot for the given property
Parameters:
`instance` - instance specification
`property` - feature
`createSlotIfNotExists` - create a new slot if needed
`createDefaultValue` - fill slot value from property default value
Returns:
slot
createSlotsForDefaultValues
public static void createSlotsForDefaultValues([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createAll)
Creates slots for properties of all assigned classifiers to instance.
Parameters:
`instance` - instance
`createAll` - true, to create slots for all properties(even without default value)
createSlotsForDefaultValues
public static void createSlotsForDefaultValues([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 boolean createAll)
Creates slots for properties of given classifier.
Parameters:
`instance` - instance
`classifier` - classifier
`createAll` - true, to create slots for all properties (even without default value)
createSlot
@CheckForNullpublic static [Slot](../../magicdraw/classes/mdkernel/Slot.html) createSlot([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean createDefaultValue)
Creates slot for property
Parameters:
`instance` - instance
`property` - property
`createDefaultValue` - fill slot value from property default value
Returns:
slot for property
setSlotValue
public static void setSlotValue([Slot](../../magicdraw/classes/mdkernel/Slot.html) slot,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Set slot value from a given string. Given string will by parsed by the slot type. For example if slot values are booleans, string should be "true".
Parameters:
`slot` - slot
`value` - value string representation.
getValueBySlot
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValueBySlot(@CheckForNull
 [Slot](../../magicdraw/classes/mdkernel/Slot.html) slot)
Retrieves values of slots as object, not as ValueSpecifications.
 Takes into account multiplicity of slot's defining feature. Collection is returned if slot multiplicity is many.
Parameters:
`slot` - slot
Returns:
value of slot
setClassifierForInstanceSpecification
public static void setClassifierForInstanceSpecification(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createSlots)
Set classifier for instance
Parameters:
`classifier` - classifier
`instance` - instance
`createSlots` - true if slots needs to be created
setClassifierForInstanceSpecification
public static void setClassifierForInstanceSpecification(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createSlots)
Set classifiers for instance
Parameters:
`classifiers` - classifiers
`instance` - instance
`createSlots` - true if slots needs to be created
See Also:
[`createSlotsForDefaultValues(InstanceSpecification, boolean)`](#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))
getAssignableAssociationsForLink
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)> getAssignableAssociationsForLink([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) clientInstance,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) supplierInstance)
Gets available associations which are allowed to assign for a link.
Parameters:
`clientInstance` - client instance specification
`supplierInstance` - supplier instance specification
Returns:
a list of assignable associations for a link
isLink
public static boolean isLink(@CheckForNull
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance)
Checks if InstanceSpecification is Link.
Parameters:
`instance` - instance to check
Returns:
true if it is Link element - it has Association as classifier or has a Link symbol in diagram
collectAllInstances
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html)> collectAllInstances([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html)> result)
Collect all instances of given classifier. Instances of derived classifiers are also collected.
Parameters:
`classifier` - classifier
`result` - result collection
Returns:
result collection
isInstanceSpecificationCompatibleWithType
public static boolean isInstanceSpecificationCompatibleWithType([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance)
Checks if given instance specification is compatible with given Type. Instance is compatible if its classifiers
 are compatible with given type.
Parameters:
`type` - instance compatibility will be checked against this type
`instance` - instance to check
Returns:
true if instance is compatible with given type
isInstanceSpecificationCompatibleWithType
public static boolean isInstanceSpecificationCompatibleWithType([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) type,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean checkInherited)
Checks if given instance specification is compatible with given Type. Instance is compatible if its classifiers
 are compatible with given type.
Parameters:
`type` - instance compatibility will be checked against this type
`instance` - instance to check
`checkInherited` - if set to true, parent type will be treated as compatible.
Returns:
true if instance is compatible with given type
getAssociationOfLink
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Association](../../magicdraw/classes/mdkernel/Association.html)> getAssociationOfLink([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instance)
Gets Association classifier from Link InstanceSpecification, if exists.
Parameters:
`instance` - Link instance
Returns:
Associations or empty collection
getLinksBetweenInstances
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html)> getLinksBetweenInstances([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) client,
 [InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) supplier)
Returns links found between client and supplier instances
Parameters:
`client` - instance
`supplier` - instance
Returns:
links
getNestedSlot
@CheckForNullpublic static [Slot](../../magicdraw/classes/mdkernel/Slot.html) getNestedSlot([InstanceSpecification](../../magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../magicdraw/classes/mdkernel/Property.html) property,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../magicdraw/classes/mdkernel/Property.html)> path,
 int index)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class InstanceSpecificationHelper">Class InstanceSpecificationHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.CoreHelper</a>
<div class="inheritance"><a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper</a>
<div class="inheritance"><a href="ClassifierHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.InstanceSpecificationHelper</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ModelHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ModelHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">InstanceSpecificationHelper</span>
<span class="extends-implements">extends <a href="ClassifierHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ClassifierHelper</a></span></div>
<div class="block">An utility class with utility methods operating on InstanceSpecification domain elements</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">InstanceSpecificationHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectAllInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectAllInstances</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all instances of given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">createSlot</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createDefaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates slot for  property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">createSlotsForDefaultValues</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates slots for properties of all assigned classifiers to instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean)">createSlotsForDefaultValues</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 boolean createAll)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates slots for properties of given classifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">findSlot</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for existing slot for a given property in given instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssignableAssociationsForLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getAssignableAssociationsForLink</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> clientInstance,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> supplierInstance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets available associations which are allowed to assign for a link.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getAssociationOfLink</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets Association classifier from Link InstanceSpecification, if exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getLinksBetweenInstances</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> client,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> supplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns links found between client and supplier instances</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int)">getNestedSlot</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; path,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getSlot</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createSlotIfNotExists)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns existing of creates a new Slot for the given property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">getSlot</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns existing of creates a new Slot for the given property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">getValueBySlot</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves values of slots as object, not as ValueSpecifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">isInstanceSpecificationCompatibleWithType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given instance specification is compatible with given Type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">isInstanceSpecificationCompatibleWithType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean checkInherited)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given instance specification is compatible with given Type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">isLink</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if InstanceSpecification is Link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassifierForInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">setClassifierForInstanceSpecification</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createSlots)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set classifier for instance</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassifierForInstanceSpecification(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">setClassifierForInstanceSpecification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createSlots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set classifiers for instance</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,java.lang.String)">setSlotValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set slot value from a given string.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="ClassifierHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ClassifierHelper</a></h3>
<code><a href="ClassifierHelper.html#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">areEqualParameterTypes</a>, <a href="ClassifierHelper.html#areEqualParameterTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">areEqualParameterTypes</a>, <a href="ClassifierHelper.html#associations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">associations</a>, <a href="ClassifierHelper.html#associationsIncludingInherited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">associationsIncludingInherited</a>, <a href="ClassifierHelper.html#attributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">attributes</a>, <a href="ClassifierHelper.html#checkForDerivedClassifier(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">checkForDerivedClassifier</a>, <a href="ClassifierHelper.html#collectBaseClassInheritableAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectBaseClassInheritableAttributes</a>, <a href="ClassifierHelper.html#collectCommonAssociations(java.util.Collection,java.util.Collection)">collectCommonAssociations</a>, <a href="ClassifierHelper.html#collectDerivedClassifiersRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">collectDerivedClassifiersRecursively</a>, <a href="ClassifierHelper.html#collectGeneralClassifiersAndRealizedInterfacesRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectGeneralClassifiersAndRealizedInterfacesRecursively</a>, <a href="ClassifierHelper.html#collectGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectGeneralClassifiersRecursively</a>, <a href="ClassifierHelper.html#collectInheritedAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedAttributes</a>, <a href="ClassifierHelper.html#collectInheritedBehaviors(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean,boolean)">collectInheritedBehaviors</a>, <a href="ClassifierHelper.html#collectInheritedEnumerationLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration,java.util.Collection,boolean,boolean)">collectInheritedEnumerationLiterals</a>, <a href="ClassifierHelper.html#collectInheritedExtensionPoints(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,java.util.Collection,boolean,boolean)">collectInheritedExtensionPoints</a>, <a href="ClassifierHelper.html#collectInheritedOperations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedOperations</a>, <a href="ClassifierHelper.html#collectInheritedPorts(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedPorts</a>, <a href="ClassifierHelper.html#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)">collectInheritedPureAttributes</a>, <a href="ClassifierHelper.html#collectInheritedPureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedPureAttributes</a>, <a href="ClassifierHelper.html#collectInheritedRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,java.util.Collection,boolean)">collectInheritedRealizedInterfaces</a>, <a href="ClassifierHelper.html#collectInheritedReceptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean,boolean)">collectInheritedReceptions</a>, <a href="ClassifierHelper.html#collectInheritedRelations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection,boolean)">collectInheritedRelations</a>, <a href="ClassifierHelper.html#collectRealizedInterfaces(java.util.Collection,java.util.Collection)">collectRealizedInterfaces</a>, <a href="ClassifierHelper.html#findAssociationEndForType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.lang.String)">findAssociationEndForType</a>, <a href="ClassifierHelper.html#findGeneralization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">findGeneralization</a>, <a href="ClassifierHelper.html#findInterfaceRealization(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier,com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">findInterfaceRealization</a>, <a href="ClassifierHelper.html#getAllLiterals(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration)">getAllLiterals</a>, <a href="ClassifierHelper.html#getAssociationEndOwnedByAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getAssociationEndOwnedByAssociation</a>, <a href="ClassifierHelper.html#getClassifiersIncludingDerived(java.util.Collection)">getClassifiersIncludingDerived</a>, <a href="ClassifierHelper.html#getClassifiersIncludingDerivedRecursively(java.util.Collection)">getClassifiersIncludingDerivedRecursively</a>, <a href="ClassifierHelper.html#getClassifiersIncludingGeneralRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getClassifiersIncludingGeneralRecursively</a>, <a href="ClassifierHelper.html#getClassifiersIncludingGeneralRecursively(java.util.Collection)">getClassifiersIncludingGeneralRecursively</a>, <a href="ClassifierHelper.html#getDerivedClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDerivedClassifiers</a>, <a href="ClassifierHelper.html#getDerivedClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getDerivedClassifiersRecursively</a>, <a href="ClassifierHelper.html#getGeneralClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getGeneralClassifiers</a>, <a href="ClassifierHelper.html#getGeneralClassifiersRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getGeneralClassifiersRecursively</a>, <a href="ClassifierHelper.html#getImplementedClasses(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">getImplementedClasses</a>, <a href="ClassifierHelper.html#getInheritanceDeep(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getInheritanceDeep</a>, <a href="ClassifierHelper.html#getParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">getParameters</a>, <a href="ClassifierHelper.html#getPropertiesWithoutRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getPropertiesWithoutRedefined</a>, <a href="ClassifierHelper.html#getProvided(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">getProvided</a>, <a href="ClassifierHelper.html#getRealizedInterfaces(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">getRealizedInterfaces</a>, <a href="ClassifierHelper.html#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">getReturnParameter</a>, <a href="ClassifierHelper.html#getReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">getReturnParameter</a>, <a href="ClassifierHelper.html#getReturnParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,boolean)">getReturnParameter</a>, <a href="ClassifierHelper.html#getReturnParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">getReturnParameters</a>, <a href="ClassifierHelper.html#isBehavioralFeatureEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature,boolean)">isBehavioralFeatureEqual</a>, <a href="ClassifierHelper.html#isClassifierOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isClassifierOfType</a>, <a href="ClassifierHelper.html#isClassifierOfType(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isClassifierOfType</a>, <a href="ClassifierHelper.html#isDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedClassifier</a>, <a href="ClassifierHelper.html#isDerivedOrRealizes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isDerivedOrRealizes</a>, <a href="ClassifierHelper.html#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isLegalInheritance</a>, <a href="ClassifierHelper.html#isLegalInheritance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">isLegalInheritance</a>, <a href="ClassifierHelper.html#isOperationEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">isOperationEqual</a>, <a href="ClassifierHelper.html#isReturnParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">isReturnParameter</a>, <a href="ClassifierHelper.html#isSameOrDerivedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">isSameOrDerivedClassifier</a>, <a href="ClassifierHelper.html#isSameOrRedefined(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isSameOrRedefined</a>, <a href="ClassifierHelper.html#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean)">isSecondTypeCompatibleToFirst</a>, <a href="ClassifierHelper.html#isSecondTypeCompatibleToFirst(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.util.Collection,boolean)">isSecondTypeCompatibleToFirst</a>, <a href="ClassifierHelper.html#operations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">operations</a>, <a href="ClassifierHelper.html#ports(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">ports</a>, <a href="ClassifierHelper.html#pureAttributes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">pureAttributes</a>, <a href="ClassifierHelper.html#receptions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">receptions</a>, <a href="ClassifierHelper.html#removeDerivedClassifiers(java.util.Collection)">removeDerivedClassifiers</a>, <a href="ClassifierHelper.html#removeRedefined(java.util.Collection,java.util.Collection...)">removeRedefined</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ValueSpecificationHelper</a></h3>
<code><a href="ValueSpecificationHelper.html#cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">cloneValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)">createValueSpecification</a>, <a href="ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">getValueSpecificationClass</a>, <a href="ValueSpecificationHelper.html#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">getValueSpecificationClass</a>, <a href="ValueSpecificationHelper.html#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueSpecificationValue</a>, <a href="ValueSpecificationHelper.html#getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueString</a>, <a href="ValueSpecificationHelper.html#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">isValueSpecificationClassElementValue</a>, <a href="ValueSpecificationHelper.html#setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setValueDisposeIfNeeded</a>, <a href="ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">setValueSpecificationValue</a>, <a href="ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean)">setValueSpecificationValue</a>, <a href="ValueSpecificationHelper.html#setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object)">setValueSpecificationValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.CoreHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">CoreHelper</a></h3>
<code><a href="CoreHelper.html#areElementsEditable(java.util.Collection)">areElementsEditable</a>, <a href="CoreHelper.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">canAssignName</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)">canAssignName</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)">canAssignName</a>, <a href="CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canMoveChildInto</a>, <a href="CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">canMoveChildInto</a>, <a href="CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationships</a>, <a href="CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)">collectRelationships</a>, <a href="CoreHelper.html#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">collectRelationshipsByType</a>, <a href="CoreHelper.html#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationshipsIncludeIndirect</a>, <a href="CoreHelper.html#dispose(java.util.Collection)">dispose</a>, <a href="CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findAcceptableParentFor</a>, <a href="CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findAcceptableParentFor</a>, <a href="CoreHelper.html#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictType</a>, <a href="CoreHelper.html#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictTypeIncludingItself</a>, <a href="CoreHelper.html#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfType</a>, <a href="CoreHelper.html#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfTypeIncludingItself</a>, <a href="CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findParent</a>, <a href="CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findParent</a>, <a href="CoreHelper.html#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAdditionalElementsIterator</a>, <a href="CoreHelper.html#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClientElement</a>, <a href="CoreHelper.html#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComment</a>, <a href="CoreHelper.html#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElement</a>, <a href="CoreHelper.html#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElementOrCreate</a>, <a href="CoreHelper.html#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentClients</a>, <a href="CoreHelper.html#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentSuppliers</a>, <a href="CoreHelper.html#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getFirstMemberEnd</a>, <a href="CoreHelper.html#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">getMultiplicity</a>, <a href="CoreHelper.html#getName(com.nomagic.magicdraw.uml.BaseElement)">getName</a>, <a href="CoreHelper.html#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOppositeEnd</a>, <a href="CoreHelper.html#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getOwnedElementsIncludingAdditional</a>, <a href="CoreHelper.html#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getSecondMemberEnd</a>, <a href="CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSupplierElement</a>, <a href="CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getSupplierElement</a>, <a href="CoreHelper.html#getSupplierElements(java.util.Collection)">getSupplierElements</a>, <a href="CoreHelper.html#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">hasParentIn</a>, <a href="CoreHelper.html#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isChildOf</a>, <a href="CoreHelper.html#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">isDocumentationComment</a>, <a href="CoreHelper.html#isMultiplicityMany(int)">isMultiplicityMany</a>, <a href="CoreHelper.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="CoreHelper.html#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isParentOf</a>, <a href="CoreHelper.html#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRelationship</a>, <a href="CoreHelper.html#isRelationshipAlwaysInClient(java.lang.Class)">isRelationshipAlwaysInClient</a>, <a href="CoreHelper.html#parseMultiplicityString(java.lang.String)">parseMultiplicityString</a>, <a href="CoreHelper.html#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setClientElement</a>, <a href="CoreHelper.html#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setComment</a>, <a href="CoreHelper.html#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">setCommentElement</a>, <a href="CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)">setConstraintText</a>, <a href="CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)">setConstraintText</a>, <a href="CoreHelper.html#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a>, <a href="CoreHelper.html#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a>, <a href="CoreHelper.html#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSupplierElement</a></code></div>
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
<h3>InstanceSpecificationHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">InstanceSpecificationHelper</span>()</div>
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
<section class="detail" id="findSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>findSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">findSlot</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Looks for existing slot for a given property in given instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instanceSpecification</code> - instance</dd>
<dd><code>property</code> - definingFeature of slot</dd>
<dt>Returns:</dt>
<dd>found slot or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>getSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getSlot</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createSlotIfNotExists)</span></div>
<div class="block">Returns existing of creates a new Slot for the given property. If new Slot is created, it will be filled with value from the property default values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance specification</dd>
<dd><code>property</code> - feature</dd>
<dd><code>createSlotIfNotExists</code> - create a new slot if needed</dd>
<dt>Returns:</dt>
<dd>slot</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">
<h3>getSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getSlot</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)</span></div>
<div class="block">Returns existing of creates a new Slot for the given property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance specification</dd>
<dd><code>property</code> - feature</dd>
<dd><code>createSlotIfNotExists</code> - create a new slot if needed</dd>
<dd><code>createDefaultValue</code> - fill slot value from property default value</dd>
<dt>Returns:</dt>
<dd>slot</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">
<h3>createSlotsForDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createSlotsForDefaultValues</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createAll)</span></div>
<div class="block">Creates slots for properties of all assigned classifiers to instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance</dd>
<dd><code>createAll</code> - true, to create slots for all properties(even without default value)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean)">
<h3>createSlotsForDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createSlotsForDefaultValues</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 boolean createAll)</span></div>
<div class="block">Creates slots for properties of given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance</dd>
<dd><code>classifier</code> - classifier</dd>
<dd><code>createAll</code> - true, to create slots for all properties (even without default value)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>createSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">createSlot</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createDefaultValue)</span></div>
<div class="block">Creates slot for  property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance</dd>
<dd><code>property</code> - property</dd>
<dd><code>createDefaultValue</code> - fill slot value from property default value</dd>
<dt>Returns:</dt>
<dd>slot for property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,java.lang.String)">
<h3>setSlotValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSlotValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set slot value from a given string. Given string will by parsed by the slot type. For example if slot values are booleans, string should be "true".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - slot</dd>
<dd><code>value</code> - value string representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">
<h3>getValueBySlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValueBySlot</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</span></div>
<div class="block">Retrieves values of slots as object, not as ValueSpecifications.
 Takes into account multiplicity of slot's defining feature. Collection is returned if slot multiplicity is many.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - slot</dd>
<dt>Returns:</dt>
<dd>value of slot</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassifierForInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">
<h3>setClassifierForInstanceSpecification</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClassifierForInstanceSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createSlots)</span></div>
<div class="block">Set classifier for instance</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dd><code>instance</code> - instance</dd>
<dd><code>createSlots</code> - true if slots needs to be created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassifierForInstanceSpecification(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">
<h3>setClassifierForInstanceSpecification</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClassifierForInstanceSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createSlots)</span></div>
<div class="block">Set classifiers for instance</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifiers</code> - classifiers</dd>
<dd><code>instance</code> - instance</dd>
<dd><code>createSlots</code> - true if slots needs to be created</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)"><code>createSlotsForDefaultValues(InstanceSpecification, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssignableAssociationsForLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getAssignableAssociationsForLink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</span> <span class="element-name">getAssignableAssociationsForLink</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> clientInstance,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> supplierInstance)</span></div>
<div class="block">Gets available associations which are allowed to assign for a link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clientInstance</code> - client instance specification</dd>
<dd><code>supplierInstance</code> - supplier instance specification</dd>
<dt>Returns:</dt>
<dd>a list of assignable associations for a link</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>isLink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLink</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</span></div>
<div class="block">Checks if InstanceSpecification is Link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance to check</dd>
<dt>Returns:</dt>
<dd>true if it is Link element - it has Association as classifier or has a Link symbol in diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectAllInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>collectAllInstances</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">collectAllInstances</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt; result)</span></div>
<div class="block">Collect all instances of given classifier. Instances of derived classifiers are also collected.</div>
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
<section class="detail" id="isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>isInstanceSpecificationCompatibleWithType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstanceSpecificationCompatibleWithType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</span></div>
<div class="block">Checks if given instance specification is compatible with given Type. Instance is compatible if its classifiers
 are compatible with given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - instance compatibility will be checked against this type</dd>
<dd><code>instance</code> - instance to check</dd>
<dt>Returns:</dt>
<dd>true if instance is compatible with given type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">
<h3>isInstanceSpecificationCompatibleWithType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstanceSpecificationCompatibleWithType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean checkInherited)</span></div>
<div class="block">Checks if given instance specification is compatible with given Type. Instance is compatible if its classifiers
 are compatible with given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - instance compatibility will be checked against this type</dd>
<dd><code>instance</code> - instance to check</dd>
<dd><code>checkInherited</code> - if set to true, parent type will be treated as compatible.</dd>
<dt>Returns:</dt>
<dd>true if instance is compatible with given type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getAssociationOfLink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</span> <span class="element-name">getAssociationOfLink</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</span></div>
<div class="block">Gets Association classifier from Link InstanceSpecification, if exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - Link instance</dd>
<dt>Returns:</dt>
<dd>Associations or empty collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getLinksBetweenInstances</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">getLinksBetweenInstances</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> client,
 <a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> supplier)</span></div>
<div class="block">Returns links found between client and supplier instances</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>client</code> - instance</dd>
<dd><code>supplier</code> - instance</dd>
<dt>Returns:</dt>
<dd>links</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int)">
<h3>getNestedSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getNestedSlot</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; path,
 int index)</span></div>
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
