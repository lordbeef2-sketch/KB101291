# JAVA OPENAPI: ModelHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/ModelHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/ModelHelper.html`
- source_sha256: `08f25006b894ede009b1379380ea3ea6c96f34c99c57304b637477abdd204036`
- captured_utc: `2026-07-14T16:52:46.463336+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class ModelHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.CoreHelper](CoreHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper](ValueSpecificationHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper](ClassifierHelper.html)
[com.nomagic.uml2.ext.jmi.helpers.InstanceSpecificationHelper](InstanceSpecificationHelper.html)
com.nomagic.uml2.ext.jmi.helpers.ModelHelper

@OpenApiAllpublic classModelHelper
extends [InstanceSpecificationHelper](InstanceSpecificationHelper.html)
Model Utility class.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModelHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[canAssignType](#canAssignType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([TypedElement](../../magicdraw/classes/mdkernel/TypedElement.html) typedElement,
 [Type](../../magicdraw/classes/mdkernel/Type.html) type)`
Check if given Type can be assigned to a given TypedElement.
`static boolean`
`[canChangeNavigability](#canChangeNavigability(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../magicdraw/classes/mdkernel/Property.html) property)`
Checks if navigability of the association end property can be inverted - navigable to
 non-navigable and vice versa.
`static boolean`
`[canChangeOwnerTo](#canChangeOwnerTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean toAssociation)`
Checks if association end can be owned by association or connected element.
`static void`
`[changeOwnerTo](#changeOwnerTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean toAssociation)`
Changes ownership of the association end.
`static [Image](../../magicdraw/mdprofiles/Image.html)`
`[createImage](#createImage(com.nomagic.uml2.impl.ElementsFactory,java.io.File))([ElementsFactory](../../../impl/ElementsFactory.html) factory,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Creates image model element from a given image found in a file.
`static [Image](../../magicdraw/mdprofiles/Image.html)`
`[createImage](#createImage(com.nomagic.uml2.impl.ElementsFactory,java.lang.String))([ElementsFactory](../../../impl/ElementsFactory.html) factory,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url)`
Creates image model element from a given image found at url.
`static [Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[findBehaviorFor](#findBehaviorFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Finds a defining behavior for a given element.
`static [Deployment](../../magicdraw/deployments/mdnodes/Deployment.html)`
`[findDeployment](#findDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget,com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact))([DeploymentTarget](../../magicdraw/deployments/mdnodes/DeploymentTarget.html) deploymentTarget,
 [DeployedArtifact](../../magicdraw/deployments/mdnodes/DeployedArtifact.html) artifact)`
Find existing deployment among target and artifact
`static [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html)`
`[findOwner](#findOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean association)`
Finds preferred owner element for the association end.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActivityParameterNode](../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html)>`
`[getActivityParameterNodes](#getActivityParameterNodes(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))([Activity](../../magicdraw/activities/mdfundamentalactivities/Activity.html) activity)`
Gets activity parameter nodes from a given activity.
`static [BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`
`[getContext](#getContext(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior)`
The classifier that is the context for the execution of the behavior.
`static [ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html)`
`[getFirstEnd](#getFirstEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector))([Connector](../../magicdraw/compositestructures/mdinternalstructures/Connector.html) connector)`
Return a first connector end
`static [ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html)`
`[getOppositeEnd](#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd))([ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) end)`
Gets opposite connector end for a given connector end.
`static [ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html)`
`[getSecondEnd](#getSecondEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector))([Connector](../../magicdraw/compositestructures/mdinternalstructures/Connector.html) connector)`
Return a second connector end
`static boolean`
`[isAggregation](#isAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind))([Association](../../magicdraw/classes/mdkernel/Association.html) association,
 [AggregationKind](../../magicdraw/classes/mdkernel/AggregationKind.html) aggregationKind)`
Determines if association is of specified aggregation kind.
`static boolean`
`[isDirectedAssociation](#isDirectedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../magicdraw/classes/mdkernel/Association.html) association)`
Check if association is directed
`static boolean`
`[isNonNavigableAssociation](#isNonNavigableAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../magicdraw/classes/mdkernel/Association.html) association)`
Check if association is non-navigable
`static boolean`
`[isPropertyEqual](#isPropertyEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../magicdraw/classes/mdkernel/Property.html) p1,
 [Property](../../magicdraw/classes/mdkernel/Property.html) p2)`
Compare the two given Property.
`static void`
`[setNavigable](#setNavigable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean))([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean navigable)`
Sets navigability of the specified association end.
`static void`
`[setNavigable](#setNavigable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean))([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean navigable,
 boolean automaticOwnership)`
Sets navigability of the specified association end.
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[InstanceSpecificationHelper](InstanceSpecificationHelper.html)
`[collectAllInstances](InstanceSpecificationHelper.html#collectAllInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)), [createSlot](InstanceSpecificationHelper.html#createSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [createSlotsForDefaultValues](InstanceSpecificationHelper.html#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)), [createSlotsForDefaultValues](InstanceSpecificationHelper.html#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean)), [findSlot](InstanceSpecificationHelper.html#findSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [getAssignableAssociationsForLink](InstanceSpecificationHelper.html#getAssignableAssociationsForLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [getAssociationOfLink](InstanceSpecificationHelper.html#getAssociationOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [getLinksBetweenInstances](InstanceSpecificationHelper.html#getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [getNestedSlot](InstanceSpecificationHelper.html#getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int)), [getSlot](InstanceSpecificationHelper.html#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)), [getSlot](InstanceSpecificationHelper.html#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)), [getValueBySlot](InstanceSpecificationHelper.html#getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)), [isInstanceSpecificationCompatibleWithType](InstanceSpecificationHelper.html#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [isInstanceSpecificationCompatibleWithType](InstanceSpecificationHelper.html#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)), [isLink](InstanceSpecificationHelper.html#isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [setClassifierForInstanceSpecification](InstanceSpecificationHelper.html#setClassifierForInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)), [setClassifierForInstanceSpecification](InstanceSpecificationHelper.html#setClassifierForInstanceSpecification(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)), [setSlotValue](InstanceSpecificationHelper.html#setSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,java.lang.String))`
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
ModelHelper
public ModelHelper()
 ============ METHOD DETAIL ========== 
Method Details
getActivityParameterNodes
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActivityParameterNode](../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html)> getActivityParameterNodes([Activity](../../magicdraw/activities/mdfundamentalactivities/Activity.html) activity)
Gets activity parameter nodes from a given activity.
Parameters:
`activity` - activity from which parameter nodes must be returned.
Returns:
a list of activity parameter nodes of a given activity.
createImage
public static [Image](../../magicdraw/mdprofiles/Image.html) createImage([ElementsFactory](../../../impl/ElementsFactory.html) factory,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Creates image model element from a given image found in a file.
 The method does not start or check sessions.
Parameters:
`file` - file in which to look for an image.
Returns:
created image model element.
createImage
public static [Image](../../magicdraw/mdprofiles/Image.html) createImage([ElementsFactory](../../../impl/ElementsFactory.html) factory,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url)
Creates image model element from a given image found at url.
 The method does not start or check sessions.
Parameters:
`url` - url
Returns:
created image model element.
isPropertyEqual
public static boolean isPropertyEqual([Property](../../magicdraw/classes/mdkernel/Property.html) p1,
 [Property](../../magicdraw/classes/mdkernel/Property.html) p2)
Compare the two given Property.
Parameters:
`p1` - First property
`p2` - Second property
Returns:
boolean
canChangeNavigability
public static boolean canChangeNavigability([Property](../../magicdraw/classes/mdkernel/Property.html) property)
Checks if navigability of the association end property can be inverted - navigable to
 non-navigable and vice versa.
 Navigability can not be changed when association of association end (property) is not editable
 or when connected element is not editable, and it owns association end.
 We do not check connected element is can own an association end when it's non-navigable,
 because association end can be explicitly navigable without changing ownership.
Parameters:
`property` - association end, can not be null
Returns:
false if association is read-only or connected element owns association end, and it's read-only, otherwise returns true
setNavigable
public static void setNavigable([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean navigable)
Sets navigability of the specified association end. It automatically
 changes ownership if possible.
 Example:
 Association assoc = ...;
 Property secondMemberEnd = ModelHelper.getSecondMemberEnd(assoc);
 ModelHelper.setNavigable(secondMemberEnd, secondMemberEnd.isNavigable());
Parameters:
`property` - association end. Can not be null
`navigable` - flag
setNavigable
public static void setNavigable([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean navigable,
 boolean automaticOwnership)
Sets navigability of the specified association end. It may change ownership of
 the association end when:
 - association end changes to non-navigable, and it's owned by connected element.
 The association becomes an owner of the association end.
 - association end changes to navigable and automaticOwnership is set to true and
 connected element is editable and can own association end. The connected element
 becomes an owner of the association end.
 At least association has to be editable in order to change association end navigability.
Parameters:
`property` - association end. Can not be null
`navigable` - flag
`automaticOwnership` - indicates if it should change association end ownership to connected element when it's possible
canChangeOwnerTo
public static boolean canChangeOwnerTo([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean toAssociation)
Checks if association end can be owned by association or connected element.
Parameters:
`property` - association end. Can not be null
`toAssociation` - indicates what kind of ownership shall be checked - true for association and false for connected element
Returns:
true according to toAssociation argument: if association can own the association end or connected element can own the association end. Returns false if preferred owner is null
changeOwnerTo
public static void changeOwnerTo([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean toAssociation)
Changes ownership of the association end. It can change owner of the
 property to association or connected element.
Parameters:
`property` - association end. Can not be null
`toAssociation` - preferred owner: true for association and false for connected element
findOwner
@CheckForNullpublic static [NamedElement](../../magicdraw/classes/mdkernel/NamedElement.html) findOwner([Property](../../magicdraw/classes/mdkernel/Property.html) property,
 boolean association)
Finds preferred owner element for the association end.
Parameters:
`property` - association end. Can not be null
`association` - preferred owner: true for association and false for connected element
Returns:
model element or null if such element does not exist
findBehaviorFor
@CheckForNullpublic static [Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) findBehaviorFor([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Finds a defining behavior for a given element. Only BehaviorClassifier and BehaviorFeature are taken into account
Parameters:
`element` - element
Returns:
behavior
isAggregation
public static boolean isAggregation([Association](../../magicdraw/classes/mdkernel/Association.html) association,
 [AggregationKind](../../magicdraw/classes/mdkernel/AggregationKind.html) aggregationKind)
Determines if association is of specified aggregation kind.
Parameters:
`association` - association model element.
`aggregationKind` - AggregationKindEnum.SHARED - aggregation, AggregationKindEnum.COMPOSITE - composition.
Returns:
true if one of association ends has set specified aggregation kind
isDirectedAssociation
public static boolean isDirectedAssociation([Association](../../magicdraw/classes/mdkernel/Association.html) association)
Check if association is directed
Parameters:
`association` - association
Returns:
true if at least one end is navigable
isNonNavigableAssociation
public static boolean isNonNavigableAssociation([Association](../../magicdraw/classes/mdkernel/Association.html) association)
Check if association is non-navigable
Parameters:
`association` - association
Returns:
true if both ends are not navigable
findDeployment
@CheckForNullpublic static [Deployment](../../magicdraw/deployments/mdnodes/Deployment.html) findDeployment([DeploymentTarget](../../magicdraw/deployments/mdnodes/DeploymentTarget.html) deploymentTarget,
 [DeployedArtifact](../../magicdraw/deployments/mdnodes/DeployedArtifact.html) artifact)
Find existing deployment among target and artifact
Parameters:
`deploymentTarget` - target
`artifact` - artifact
Returns:
existing deployment or null
getContext
@CheckForNullpublic static [BehavioredClassifier](../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) getContext([Behavior](../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior)
The classifier that is the context for the execution of the behavior. A Behavior that is directly owned as a
 nestedClassifier does not have a context. Otherwise, to determine the context of a Behavior, find the first
 BehavioredClassifier reached by following the chain of owner relationships from the Behavior, if any.
 If there is such a BehavioredClassifier, then it is the context, unless it is itself a Behavior with a
 non-empty context, in which case that is also the context for the original Behavior. For example, following
 this algorithm, the context of an entry action in a state machine is the classifier that owns the state machine.
 The features of the context classifier as well as the elements visible to the context classifier are visible
 to the behavior.
 (Subsets RedefinableElement::redefinitionContext)
Parameters:
`behavior` - behavior for which to get the context.
canAssignType
public static boolean canAssignType([TypedElement](../../magicdraw/classes/mdkernel/TypedElement.html) typedElement,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) type)
Check if given Type can be assigned to a given TypedElement. For example Property owned by Stereotype (Tag definition)
 can be typed just by Stereotype, DataType or metaclass.
Parameters:
`typedElement` - typed element
`type` - type
Returns:
true if type can be changed
getFirstEnd
@CheckForNullpublic static [ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) getFirstEnd([Connector](../../magicdraw/compositestructures/mdinternalstructures/Connector.html) connector)
Return a first connector end
Parameters:
`connector` - connector
Returns:
end
getSecondEnd
@CheckForNullpublic static [ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) getSecondEnd([Connector](../../magicdraw/compositestructures/mdinternalstructures/Connector.html) connector)
Return a second connector end
Parameters:
`connector` - connector
Returns:
end
getOppositeEnd
@CheckForNullpublic static [ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) getOppositeEnd([ConnectorEnd](../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html) end)
Gets opposite connector end for a given connector end.
Parameters:
`end` - connector end for which to get opposite end
Returns:
opposite connector end for a given connector end

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class ModelHelper">Class ModelHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.CoreHelper</a>
<div class="inheritance"><a href="ValueSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper</a>
<div class="inheritance"><a href="ClassifierHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.ClassifierHelper</a>
<div class="inheritance"><a href="InstanceSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.InstanceSpecificationHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.ModelHelper</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ModelHelper</span>
<span class="extends-implements">extends <a href="InstanceSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">InstanceSpecificationHelper</a></span></div>
<div class="block">Model Utility class.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ModelHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAssignType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">canAssignType</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> typedElement,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given Type can be assigned to a given TypedElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeNavigability(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">canChangeNavigability</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if navigability of the association end property can be inverted - navigable to
 non-navigable and vice versa.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeOwnerTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">canChangeOwnerTo</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean toAssociation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if association end can be owned by association or connected element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#changeOwnerTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">changeOwnerTo</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean toAssociation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Changes ownership of the association end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createImage(com.nomagic.uml2.impl.ElementsFactory,java.io.File)">createImage</a><wbr/>(<a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates image model element from a given image found in a file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createImage(com.nomagic.uml2.impl.ElementsFactory,java.lang.String)">createImage</a><wbr/>(<a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates image model element from a given image found at url.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findBehaviorFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findBehaviorFor</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds a defining behavior for a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget,com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact)">findDeployment</a><wbr/>(<a href="../../magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a> deploymentTarget,
 <a href="../../magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a> artifact)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find existing deployment among target and artifact</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">findOwner</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds preferred owner element for the association end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivityParameterNodes(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">getActivityParameterNodes</a><wbr/>(<a href="../../magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> activity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets activity parameter nodes from a given activity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getContext(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">getContext</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">The classifier that is the context for the execution of the behavior.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">getFirstEnd</a><wbr/>(<a href="../../magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a first connector end</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd)">getOppositeEnd</a><wbr/>(<a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets opposite connector end for a given connector end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSecondEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">getSecondEnd</a><wbr/>(<a href="../../magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a second connector end</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">isAggregation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a href="../../magicdraw/classes/mdkernel/AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> aggregationKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines if association is of specified aggregation kind.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirectedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">isDirectedAssociation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if association is directed</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNonNavigableAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">isNonNavigableAssociation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if association is non-navigable</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPropertyEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isPropertyEqual</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> p1,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> p2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare the two given Property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setNavigable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">setNavigable</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean navigable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets navigability of the specified association end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setNavigable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">setNavigable</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean navigable,
 boolean automaticOwnership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets navigability of the specified association end.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.InstanceSpecificationHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="InstanceSpecificationHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">InstanceSpecificationHelper</a></h3>
<code><a href="InstanceSpecificationHelper.html#collectAllInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectAllInstances</a>, <a href="InstanceSpecificationHelper.html#createSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">createSlot</a>, <a href="InstanceSpecificationHelper.html#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">createSlotsForDefaultValues</a>, <a href="InstanceSpecificationHelper.html#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean)">createSlotsForDefaultValues</a>, <a href="InstanceSpecificationHelper.html#findSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">findSlot</a>, <a href="InstanceSpecificationHelper.html#getAssignableAssociationsForLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getAssignableAssociationsForLink</a>, <a href="InstanceSpecificationHelper.html#getAssociationOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getAssociationOfLink</a>, <a href="InstanceSpecificationHelper.html#getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getLinksBetweenInstances</a>, <a href="InstanceSpecificationHelper.html#getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int)">getNestedSlot</a>, <a href="InstanceSpecificationHelper.html#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">getSlot</a>, <a href="InstanceSpecificationHelper.html#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">getSlot</a>, <a href="InstanceSpecificationHelper.html#getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">getValueBySlot</a>, <a href="InstanceSpecificationHelper.html#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">isInstanceSpecificationCompatibleWithType</a>, <a href="InstanceSpecificationHelper.html#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">isInstanceSpecificationCompatibleWithType</a>, <a href="InstanceSpecificationHelper.html#isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">isLink</a>, <a href="InstanceSpecificationHelper.html#setClassifierForInstanceSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">setClassifierForInstanceSpecification</a>, <a href="InstanceSpecificationHelper.html#setClassifierForInstanceSpecification(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">setClassifierForInstanceSpecification</a>, <a href="InstanceSpecificationHelper.html#setSlotValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot,java.lang.String)">setSlotValue</a></code></div>
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
<h3>ModelHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModelHelper</span>()</div>
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
<section class="detail" id="getActivityParameterNodes(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">
<h3>getActivityParameterNodes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a>&gt;</span> <span class="element-name">getActivityParameterNodes</span><wbr/><span class="parameters">(<a href="../../magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> activity)</span></div>
<div class="block">Gets activity parameter nodes from a given activity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activity</code> - activity from which parameter nodes must be returned.</dd>
<dt>Returns:</dt>
<dd>a list of activity parameter nodes of a given activity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImage(com.nomagic.uml2.impl.ElementsFactory,java.io.File)">
<h3>createImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></span> <span class="element-name">createImage</span><wbr/><span class="parameters">(<a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Creates image model element from a given image found in a file.
 The method does not start or check sessions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - file in which to look for an image.</dd>
<dt>Returns:</dt>
<dd>created image model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImage(com.nomagic.uml2.impl.ElementsFactory,java.lang.String)">
<h3>createImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a></span> <span class="element-name">createImage</span><wbr/><span class="parameters">(<a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</span></div>
<div class="block">Creates image model element from a given image found at url.
 The method does not start or check sessions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dt>Returns:</dt>
<dd>created image model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPropertyEqual(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>isPropertyEqual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPropertyEqual</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> p1,
 <a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> p2)</span></div>
<div class="block">Compare the two given Property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p1</code> - First property</dd>
<dd><code>p2</code> - Second property</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeNavigability(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>canChangeNavigability</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canChangeNavigability</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Checks if navigability of the association end property can be inverted - navigable to
 non-navigable and vice versa.
 Navigability can not be changed when association of association end (property) is not editable
 or when connected element is not editable, and it owns association end.
 We do not check connected element is can own an association end when it's non-navigable,
 because association end can be explicitly navigable without changing ownership.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - association end, can not be null</dd>
<dt>Returns:</dt>
<dd>false if association is read-only or connected element owns association end, and it's read-only, otherwise returns true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNavigable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>setNavigable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setNavigable</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean navigable)</span></div>
<div class="block">Sets navigability of the specified association end. It automatically
 changes ownership if possible.
 <pre>
 Example:
  Association assoc = ...;
  Property secondMemberEnd = ModelHelper.getSecondMemberEnd(assoc);
  ModelHelper.setNavigable(secondMemberEnd, secondMemberEnd.isNavigable());
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - association end. Can not be null</dd>
<dd><code>navigable</code> - flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNavigable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">
<h3>setNavigable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setNavigable</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean navigable,
 boolean automaticOwnership)</span></div>
<div class="block">Sets navigability of the specified association end. It may change ownership of
 the association end when:
 - association end changes to non-navigable, and it's owned by connected element.
 The association becomes an owner of the association end.
 - association end changes to navigable and automaticOwnership is set to true and
 connected element is editable and can own association end. The connected element
 becomes an owner of the association end.
 At least association has to be editable in order to change association end navigability.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - association end. Can not be null</dd>
<dd><code>navigable</code> - flag</dd>
<dd><code>automaticOwnership</code> - indicates if it should change association end ownership to connected element when it's possible</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeOwnerTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>canChangeOwnerTo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canChangeOwnerTo</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean toAssociation)</span></div>
<div class="block">Checks if association end can be owned by association or connected element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - association end. Can not be null</dd>
<dd><code>toAssociation</code> - indicates what kind of ownership shall be checked - true for association and false for connected element</dd>
<dt>Returns:</dt>
<dd>true according to toAssociation argument: if association can own the association end or connected element can own the association end. Returns false if preferred owner is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeOwnerTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>changeOwnerTo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">changeOwnerTo</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean toAssociation)</span></div>
<div class="block">Changes ownership of the association end. It can change owner of the
 property to association or connected element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - association end. Can not be null</dd>
<dd><code>toAssociation</code> - preferred owner: true for association and false for connected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean)">
<h3>findOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span> <span class="element-name">findOwner</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean association)</span></div>
<div class="block">Finds preferred owner element for the association end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - association end. Can not be null</dd>
<dd><code>association</code> - preferred owner: true for association and false for connected element</dd>
<dt>Returns:</dt>
<dd>model element or null if such element does not exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findBehaviorFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>findBehaviorFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">findBehaviorFor</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Finds a defining behavior for a given element. Only BehaviorClassifier and BehaviorFeature are taken into account</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>behavior</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">
<h3>isAggregation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAggregation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a href="../../magicdraw/classes/mdkernel/AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> aggregationKind)</span></div>
<div class="block">Determines if association is of specified aggregation kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association model element.</dd>
<dd><code>aggregationKind</code> - AggregationKindEnum.SHARED - aggregation, AggregationKindEnum.COMPOSITE - composition.</dd>
<dt>Returns:</dt>
<dd>true if one of association ends has set specified aggregation kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirectedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>isDirectedAssociation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDirectedAssociation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block">Check if association is directed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association</dd>
<dt>Returns:</dt>
<dd>true if at least one end is navigable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNonNavigableAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>isNonNavigableAssociation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNonNavigableAssociation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block">Check if association is non-navigable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association</dd>
<dt>Returns:</dt>
<dd>true if both ends are not navigable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findDeployment(com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget,com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeployedArtifact)">
<h3>findDeployment</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></span> <span class="element-name">findDeployment</span><wbr/><span class="parameters">(<a href="../../magicdraw/deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a> deploymentTarget,
 <a href="../../magicdraw/deployments/mdnodes/DeployedArtifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeployedArtifact</a> artifact)</span></div>
<div class="block">Find existing deployment among target and artifact</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>deploymentTarget</code> - target</dd>
<dd><code>artifact</code> - artifact</dd>
<dt>Returns:</dt>
<dd>existing deployment or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>getContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></span> <span class="element-name">getContext</span><wbr/><span class="parameters">(<a href="../../magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior)</span></div>
<div class="block">The classifier that is the context for the execution of the behavior. A Behavior that is directly owned as a
 nestedClassifier does not have a context. Otherwise, to determine the context of a Behavior, find the first
 BehavioredClassifier reached by following the chain of owner relationships from the Behavior, if any.
 If there is such a BehavioredClassifier, then it is the context, unless it is itself a Behavior with a
 non-empty context, in which case that is also the context for the original Behavior. For example, following
 this algorithm, the context of an entry action in a state machine is the classifier that owns the state machine.
 The features of the context classifier as well as the elements visible to the context classifier are visible
 to the behavior.
 (Subsets RedefinableElement::redefinitionContext)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - behavior for which to get the context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAssignType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>canAssignType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAssignType</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> typedElement,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="block">Check if given Type can be assigned to a given TypedElement. For example Property owned by Stereotype (Tag definition)
 can be typed just by Stereotype, DataType or metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>typedElement</code> - typed element</dd>
<dd><code>type</code> - type</dd>
<dt>Returns:</dt>
<dd>true if type can be changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">
<h3>getFirstEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></span> <span class="element-name">getFirstEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> connector)</span></div>
<div class="block">Return a first connector end</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - connector</dd>
<dt>Returns:</dt>
<dd>end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSecondEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">
<h3>getSecondEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></span> <span class="element-name">getSecondEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> connector)</span></div>
<div class="block">Return a second connector end</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - connector</dd>
<dt>Returns:</dt>
<dd>end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOppositeEnd(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectorEnd)">
<h3>getOppositeEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></span> <span class="element-name">getOppositeEnd</span><wbr/><span class="parameters">(<a href="../../magicdraw/compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a> end)</span></div>
<div class="block">Gets opposite connector end for a given connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - connector end for which to get opposite end</dd>
<dt>Returns:</dt>
<dd>opposite connector end for a given connector end</dd>
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
