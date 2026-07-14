# JAVA OPENAPI: Connector (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Connector.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Connector.html`
- source_sha256: `73ca7d5af12e599f9a6e4679a3d2d224af7dbbb7c0bf89848c88366f885e772f`
- captured_utc: `2026-07-14T16:44:48.720853+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Connector

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](Feature.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[AllocationUsage](../../../sysml/model/sysml/AllocationUsage.html)`, `[BindingConnector](BindingConnector.html)`, `[BindingConnectorAsUsage](../../../sysml/model/sysml/BindingConnectorAsUsage.html)`, `[ConnectionUsage](../../../sysml/model/sysml/ConnectionUsage.html)`, `[ConnectorAsUsage](../../../sysml/model/sysml/ConnectorAsUsage.html)`, `[Flow](Flow.html)`, `[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[InterfaceUsage](../../../sysml/model/sysml/InterfaceUsage.html)`, `[Succession](Succession.html)`, `[SuccessionAsUsage](../../../sysml/model/sysml/SuccessionAsUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`

@OpenApiAllpublic interfaceConnectorextends [Feature](Feature.html), [Relationship](Relationship.html)

A `Connector` is a usage of `Associations`, with links restricted according to instances of the `Type` in which they are used (domain of the `Connector`). The `associations` of the `Connector` restrict what kinds of things might be linked. The `Connector` further restricts these links to be between values of `Features` on instances of its domain.
 
 relatedFeature = connectorEnd.ownedReferenceSubsetting->
 select(s | s <> null).subsettedFeature
 relatedFeature->forAll(f | 
 if featuringType->isEmpty() then f.isFeaturedWithin(null)
 else featuringType->forAll(t | f.isFeaturedWithin(t))
 endif)
 sourceFeature = 
 if relatedFeature->isEmpty() then null 
 else relatedFeature->first() 
 endif
 targetFeature =
 if relatedFeature->size() < 2 then OrderedSet{}
 else 
 relatedFeature->
 subSequence(2, relatedFeature->size())->
 asOrderedSet()
 endif
 not isAbstract implies relatedFeature->size() >= 2
 specializesFromLibrary('Links::links')
 association->exists(oclIsKindOf(AssociationStructure)) implies
 specializesFromLibrary('Objects::linkObjects')
 connectorEnds->size() = 2 and
 association->exists(oclIsKindOf(AssociationStructure)) implies
 specializesFromLibrary('Objects::binaryLinkObjects')
 connectorEnd->size() = 2 implies
 specializesFromLibrary('Links::binaryLinks')
 connectorEnds->size() > 2 implies
 not specializesFromLibrary('Links::BinaryLink')
 let commonFeaturingTypes : OrderedSet(Type) = 
 relatedFeature->closure(featuringType)->select(t | 
 relatedFeature->forAll(f | f.isFeaturedWithin(t))
 ) in
 let nearestCommonFeaturingTypes : OrderedSet(Type) =
 commonFeaturingTypes->reject(t1 | 
 commonFeaturingTypes->exists(t2 | 
 t2 <> t1 and t2->closure(featuringType)->contains(t1)
 )) in
 if nearestCommonFeaturingTypes->isEmpty() then null
 else nearestCommonFeaturingTypes->first()
 endif

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Association](Association.html)>`
`[getAssociation](#getAssociation())()`
The `Associations` that type the `Connector`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getConnectorEnd](#getConnectorEnd())()`
The `endFeatures` of a `Connector`, which redefine the `endFeatures` of the `associations` of the `Connector`.
`[Type](Type.html)`
`[getDefaultFeaturingType](#getDefaultFeaturingType())()`
The innermost `Type` that is a common direct or indirect `featuringType` of the `relatedFeatures`, such that, if it exists and was the `featuringType` of this `Connector`, the `Connector` would satisfy the `checkConnectorTypeFeaturing` constraint.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getRelatedFeature](#getRelatedFeature())()`
The `Features` that are related by this `Connector` considered as a `Relationship` and that restrict the links it identifies, given by the referenced `Features` of the `connectorEnds` of the `Connector`.
`[Feature](Feature.html)`
`[getSourceFeature](#getSourceFeature())()`
The source `relatedFeature` for this `Connector`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getTargetFeature](#getTargetFeature())()`
The target `relatedFeatures` for this `Connector`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Feature](Feature.html)
`[allRedefinedFeatures](Feature.html#allRedefinedFeatures()), [asCartesianProduct](Feature.html#asCartesianProduct()), [canAccess](Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionFor](Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [effectiveName](Feature.html#effectiveName()), [effectiveShortName](Feature.html#effectiveShortName()), [getChainingFeature](Feature.html#getChainingFeature()), [getCrossFeature](Feature.html#getCrossFeature()), [getDirection](Feature.html#getDirection()), [getEndOwningType](Feature.html#getEndOwningType()), [getFeatureTarget](Feature.html#getFeatureTarget()), [getFeaturingType](Feature.html#getFeaturingType()), [getOwnedCrossSubsetting](Feature.html#getOwnedCrossSubsetting()), [getOwnedFeatureChaining](Feature.html#getOwnedFeatureChaining()), [getOwnedFeatureInverting](Feature.html#getOwnedFeatureInverting()), [getOwnedRedefinition](Feature.html#getOwnedRedefinition()), [getOwnedReferenceSubsetting](Feature.html#getOwnedReferenceSubsetting()), [getOwnedSubsetting](Feature.html#getOwnedSubsetting()), [getOwnedTypeFeaturing](Feature.html#getOwnedTypeFeaturing()), [getOwnedTyping](Feature.html#getOwnedTyping()), [getOwningFeatureMembership](Feature.html#getOwningFeatureMembership()), [getOwningType](Feature.html#getOwningType()), [getType](Feature.html#getType()), [isCartesianProduct](Feature.html#isCartesianProduct()), [isCompatibleWith](Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isComposite](Feature.html#isComposite()), [isConstant](Feature.html#isConstant()), [isDerived](Feature.html#isDerived()), [isEnd](Feature.html#isEnd()), [isFeaturedWithin](Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isFeaturingType](Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isOrdered](Feature.html#isOrdered()), [isOwnedCrossFeature](Feature.html#isOwnedCrossFeature()), [isPortion](Feature.html#isPortion()), [isUnique](Feature.html#isUnique()), [isVariable](Feature.html#isVariable()), [namingFeature](Feature.html#namingFeature()), [ownedCrossFeature](Feature.html#ownedCrossFeature()), [redefines](Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [redefinesFromLibrary](Feature.html#redefinesFromLibrary(java.lang.String)), [setDirection](Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)), [setIsComposite](Feature.html#setIsComposite(boolean)), [setIsConstant](Feature.html#setIsConstant(boolean)), [setIsDerived](Feature.html#setIsDerived(boolean)), [setIsEnd](Feature.html#setIsEnd(boolean)), [setIsOrdered](Feature.html#setIsOrdered(boolean)), [setIsPortion](Feature.html#setIsPortion(boolean)), [setIsUnique](Feature.html#setIsUnique(boolean)), [setIsVariable](Feature.html#setIsVariable(boolean)), [subsetsChain](Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [supertypes](Feature.html#supertypes(boolean)), [typingFeatures](Feature.html#typingFeatures())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](Namespace.html)
`[getImportedMembership](Namespace.html#getImportedMembership()), [getMember](Namespace.html#getMember()), [getMembership](Namespace.html#getMembership()), [getOwnedImport](Namespace.html#getOwnedImport()), [getOwnedMember](Namespace.html#getOwnedMember()), [getOwnedMembership](Namespace.html#getOwnedMembership()), [importedMemberships](Namespace.html#importedMemberships(java.util.List)), [membershipsOfVisibility](Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](Namespace.html#qualificationOf(java.lang.String)), [resolve](Namespace.html#resolve(java.lang.String)), [resolveGlobal](Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Relationship](Relationship.html)
`[getOwnedRelatedElement](Relationship.html#getOwnedRelatedElement()), [getOwningRelatedElement](Relationship.html#getOwningRelatedElement()), [getRelatedElement](Relationship.html#getRelatedElement()), [getSource](Relationship.html#getSource()), [getTarget](Relationship.html#getTarget()), [isImplied](Relationship.html#isImplied()), [libraryNamespace](Relationship.html#libraryNamespace()), [path](Relationship.html#path()), [setIsImplied](Relationship.html#setIsImplied(boolean)), [setOwningRelatedElement](Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](Type.html)
`[allRedefinedFeaturesOf](Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](Type.html#allSupertypes()), [directionOf](Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](Type.html#getDifferencingType()), [getDirectedFeature](Type.html#getDirectedFeature()), [getEndFeature](Type.html#getEndFeature()), [getFeature](Type.html#getFeature()), [getFeatureMembership](Type.html#getFeatureMembership()), [getInheritedFeature](Type.html#getInheritedFeature()), [getInheritedMembership](Type.html#getInheritedMembership()), [getInput](Type.html#getInput()), [getIntersectingType](Type.html#getIntersectingType()), [getMultiplicity](Type.html#getMultiplicity()), [getOutput](Type.html#getOutput()), [getOwnedConjugator](Type.html#getOwnedConjugator()), [getOwnedDifferencing](Type.html#getOwnedDifferencing()), [getOwnedDisjoining](Type.html#getOwnedDisjoining()), [getOwnedEndFeature](Type.html#getOwnedEndFeature()), [getOwnedFeature](Type.html#getOwnedFeature()), [getOwnedFeatureMembership](Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](Type.html#getOwnedIntersecting()), [getOwnedSpecialization](Type.html#getOwnedSpecialization()), [getOwnedUnioning](Type.html#getOwnedUnioning()), [getUnioningType](Type.html#getUnioningType()), [inheritableMemberships](Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](Type.html#isAbstract()), [isConjugated](Type.html#isConjugated()), [isSufficient](Type.html#isSufficient()), [multiplicities](Type.html#multiplicities()), [nonPrivateMemberships](Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](Type.html#setIsAbstract(boolean)), [setIsSufficient](Type.html#setIsSufficient(boolean)), [specializes](Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](Type.html#specializesFromLibrary(java.lang.String)), [visibleMemberships](Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getRelatedFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getRelatedFeature()
The `Features` that are related by this `Connector` considered as a `Relationship` and that restrict the links it identifies, given by the referenced `Features` of the `connectorEnds` of the `Connector`.
Returns:
the relatedFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="connector"
 redefines=[`Relationship.getRelatedElement()`](Relationship.html#getRelatedElement())
getAssociation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Association](Association.html)> getAssociation()
The `Associations` that type the `Connector`.
Returns:
the association value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typedConnector"
 redefines=[`Feature.getType()`](Feature.html#getType())
getConnectorEnd
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getConnectorEnd()
The `endFeatures` of a `Connector`, which redefine the `endFeatures` of the `associations` of the `Connector`. The `connectorEnds` determine via `ReferenceSubsetting` `Relationships` which `Features` are related by the `Connector`.
Returns:
the connectorEnd value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featuringConnector"
 redefines=[`Type.getEndFeature()`](Type.html#getEndFeature())
getSourceFeature
@CheckForNull[Feature](Feature.html) getSourceFeature()
The source `relatedFeature` for this `Connector`. It is the first `relatedFeature`.
Returns:
the sourceFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="sourceConnector"
 subsets=[`getRelatedFeature()`](#getRelatedFeature())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
getTargetFeature
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getTargetFeature()
The target `relatedFeatures` for this `Connector`. This includes all the `relatedFeatures` other than the `sourceFeature`.
Returns:
the targetFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="targetConnector"
 subsets=[`getRelatedFeature()`](#getRelatedFeature())
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
getDefaultFeaturingType
@CheckForNull[Type](Type.html) getDefaultFeaturingType()
The innermost `Type` that is a common direct or indirect `featuringType` of the `relatedFeatures`, such that, if it exists and was the `featuringType` of this `Connector`, the `Connector` would satisfy the `checkConnectorTypeFeaturing` constraint.
Returns:
the defaultFeaturingType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featuredConnector"

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Connector">Interface Connector</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code>, <code><a href="../../../sysml/model/sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code>, <code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Connector</span><span class="extends-implements">
extends <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>, <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span></div>
<div class="block"><p>A <code>Connector</code> is a usage of <code>Associations</code>, with links restricted according to instances of the <code>Type</code> in which they are used (domain of the <code>Connector</code>). The <code>associations</code> of the <code>Connector</code> restrict what kinds of things might be linked. The <code>Connector</code> further restricts these links to be between values of <code>Features</code> on instances of its domain.</p>
 
 relatedFeature = connectorEnd.ownedReferenceSubsetting-&gt;
     select(s | s &lt;&gt; null).subsettedFeature
 relatedFeature-&gt;forAll(f | 
     if featuringType-&gt;isEmpty() then f.isFeaturedWithin(null)
     else featuringType-&gt;forAll(t | f.isFeaturedWithin(t))
     endif)
 sourceFeature = 
     if relatedFeature-&gt;isEmpty() then null 
     else relatedFeature-&gt;first() 
     endif
 targetFeature =
     if relatedFeature-&gt;size() &lt; 2 then OrderedSet{}
     else 
         relatedFeature-&gt;
             subSequence(2, relatedFeature-&gt;size())-&gt;
             asOrderedSet()
     endif
 not isAbstract implies relatedFeature-&gt;size() &gt;= 2
 specializesFromLibrary('Links::links')
 association-&gt;exists(oclIsKindOf(AssociationStructure)) implies
     specializesFromLibrary('Objects::linkObjects')
 connectorEnds-&gt;size() = 2 and
 association-&gt;exists(oclIsKindOf(AssociationStructure)) implies
     specializesFromLibrary('Objects::binaryLinkObjects')
 connectorEnd-&gt;size() = 2 implies
     specializesFromLibrary('Links::binaryLinks')
 connectorEnds-&gt;size() &gt; 2 implies
     not specializesFromLibrary('Links::BinaryLink')
 let commonFeaturingTypes : OrderedSet(Type) = 
     relatedFeature-&gt;closure(featuringType)-&gt;select(t | 
         relatedFeature-&gt;forAll(f | f.isFeaturedWithin(t))
     ) in
 let nearestCommonFeaturingTypes : OrderedSet(Type) =
     commonFeaturingTypes-&gt;reject(t1 | 
         commonFeaturingTypes-&gt;exists(t2 | 
             t2 &lt;&gt; t1 and t2-&gt;closure(featuringType)-&gt;contains(t1)
     )) in
 if nearestCommonFeaturingTypes-&gt;isEmpty() then null
 else nearestCommonFeaturingTypes-&gt;first()
 endif</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAssociation()">getAssociation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Associations</code> that type the <code>Connector</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConnectorEnd()">getConnectorEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>endFeatures</code> of a <code>Connector</code>, which redefine the <code>endFeatures</code> of the <code>associations</code> of the <code>Connector</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultFeaturingType()">getDefaultFeaturingType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The innermost <code>Type</code> that is a common direct or indirect <code>featuringType</code> of the <code>relatedFeatures</code>, such that, if it exists and was the <code>featuringType</code> of this <code>Connector</code>, the <code>Connector</code> would satisfy the <code>checkConnectorTypeFeaturing</code> constraint.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRelatedFeature()">getRelatedFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Features</code> that are related by this <code>Connector</code> considered as a <code>Relationship</code> and that restrict the links it identifies, given by the referenced <code>Features</code> of the <code>connectorEnds</code> of the <code>Connector</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSourceFeature()">getSourceFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The source <code>relatedFeature</code> for this <code>Connector</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTargetFeature()">getTargetFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The target <code>relatedFeatures</code> for this <code>Connector</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Feature">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></h3>
<code><a href="Feature.html#allRedefinedFeatures()">allRedefinedFeatures</a>, <a href="Feature.html#asCartesianProduct()">asCartesianProduct</a>, <a href="Feature.html#canAccess(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">canAccess</a>, <a href="Feature.html#directionFor(com.dassault_systemes.modeler.kerml.model.kerml.Type)">directionFor</a>, <a href="Feature.html#effectiveName()">effectiveName</a>, <a href="Feature.html#effectiveShortName()">effectiveShortName</a>, <a href="Feature.html#getChainingFeature()">getChainingFeature</a>, <a href="Feature.html#getCrossFeature()">getCrossFeature</a>, <a href="Feature.html#getDirection()">getDirection</a>, <a href="Feature.html#getEndOwningType()">getEndOwningType</a>, <a href="Feature.html#getFeatureTarget()">getFeatureTarget</a>, <a href="Feature.html#getFeaturingType()">getFeaturingType</a>, <a href="Feature.html#getOwnedCrossSubsetting()">getOwnedCrossSubsetting</a>, <a href="Feature.html#getOwnedFeatureChaining()">getOwnedFeatureChaining</a>, <a href="Feature.html#getOwnedFeatureInverting()">getOwnedFeatureInverting</a>, <a href="Feature.html#getOwnedRedefinition()">getOwnedRedefinition</a>, <a href="Feature.html#getOwnedReferenceSubsetting()">getOwnedReferenceSubsetting</a>, <a href="Feature.html#getOwnedSubsetting()">getOwnedSubsetting</a>, <a href="Feature.html#getOwnedTypeFeaturing()">getOwnedTypeFeaturing</a>, <a href="Feature.html#getOwnedTyping()">getOwnedTyping</a>, <a href="Feature.html#getOwningFeatureMembership()">getOwningFeatureMembership</a>, <a href="Feature.html#getOwningType()">getOwningType</a>, <a href="Feature.html#getType()">getType</a>, <a href="Feature.html#isCartesianProduct()">isCartesianProduct</a>, <a href="Feature.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="Feature.html#isComposite()">isComposite</a>, <a href="Feature.html#isConstant()">isConstant</a>, <a href="Feature.html#isDerived()">isDerived</a>, <a href="Feature.html#isEnd()">isEnd</a>, <a href="Feature.html#isFeaturedWithin(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturedWithin</a>, <a href="Feature.html#isFeaturingType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeaturingType</a>, <a href="Feature.html#isOrdered()">isOrdered</a>, <a href="Feature.html#isOwnedCrossFeature()">isOwnedCrossFeature</a>, <a href="Feature.html#isPortion()">isPortion</a>, <a href="Feature.html#isUnique()">isUnique</a>, <a href="Feature.html#isVariable()">isVariable</a>, <a href="Feature.html#namingFeature()">namingFeature</a>, <a href="Feature.html#ownedCrossFeature()">ownedCrossFeature</a>, <a href="Feature.html#redefines(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">redefines</a>, <a href="Feature.html#redefinesFromLibrary(java.lang.String)">redefinesFromLibrary</a>, <a href="Feature.html#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">setDirection</a>, <a href="Feature.html#setIsComposite(boolean)">setIsComposite</a>, <a href="Feature.html#setIsConstant(boolean)">setIsConstant</a>, <a href="Feature.html#setIsDerived(boolean)">setIsDerived</a>, <a href="Feature.html#setIsEnd(boolean)">setIsEnd</a>, <a href="Feature.html#setIsOrdered(boolean)">setIsOrdered</a>, <a href="Feature.html#setIsPortion(boolean)">setIsPortion</a>, <a href="Feature.html#setIsUnique(boolean)">setIsUnique</a>, <a href="Feature.html#setIsVariable(boolean)">setIsVariable</a>, <a href="Feature.html#subsetsChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">subsetsChain</a>, <a href="Feature.html#supertypes(boolean)">supertypes</a>, <a href="Feature.html#typingFeatures()">typingFeatures</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject">Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</h3>
<code>getModelExtension, getModelExtension</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Namespace">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></h3>
<code><a href="Namespace.html#getImportedMembership()">getImportedMembership</a>, <a href="Namespace.html#getMember()">getMember</a>, <a href="Namespace.html#getMembership()">getMembership</a>, <a href="Namespace.html#getOwnedImport()">getOwnedImport</a>, <a href="Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="Namespace.html#getOwnedMembership()">getOwnedMembership</a>, <a href="Namespace.html#importedMemberships(java.util.List)">importedMemberships</a>, <a href="Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">membershipsOfVisibility</a>, <a href="Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">namesOf</a>, <a href="Namespace.html#qualificationOf(java.lang.String)">qualificationOf</a>, <a href="Namespace.html#resolve(java.lang.String)">resolve</a>, <a href="Namespace.html#resolveGlobal(java.lang.String)">resolveGlobal</a>, <a href="Namespace.html#resolveLocal(java.lang.String)">resolveLocal</a>, <a href="Namespace.html#resolveVisible(java.lang.String)">resolveVisible</a>, <a href="Namespace.html#unqualifiedNameOf(java.lang.String)">unqualifiedNameOf</a>, <a href="Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">visibilityOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Relationship">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></h3>
<code><a href="Relationship.html#getOwnedRelatedElement()">getOwnedRelatedElement</a>, <a href="Relationship.html#getOwningRelatedElement()">getOwningRelatedElement</a>, <a href="Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="Relationship.html#getSource()">getSource</a>, <a href="Relationship.html#getTarget()">getTarget</a>, <a href="Relationship.html#isImplied()">isImplied</a>, <a href="Relationship.html#libraryNamespace()">libraryNamespace</a>, <a href="Relationship.html#path()">path</a>, <a href="Relationship.html#setIsImplied(boolean)">setIsImplied</a>, <a href="Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Type">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></h3>
<code><a href="Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a>, <a href="Type.html#allSupertypes()">allSupertypes</a>, <a href="Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a>, <a href="Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a>, <a href="Type.html#getDifferencingType()">getDifferencingType</a>, <a href="Type.html#getDirectedFeature()">getDirectedFeature</a>, <a href="Type.html#getEndFeature()">getEndFeature</a>, <a href="Type.html#getFeature()">getFeature</a>, <a href="Type.html#getFeatureMembership()">getFeatureMembership</a>, <a href="Type.html#getInheritedFeature()">getInheritedFeature</a>, <a href="Type.html#getInheritedMembership()">getInheritedMembership</a>, <a href="Type.html#getInput()">getInput</a>, <a href="Type.html#getIntersectingType()">getIntersectingType</a>, <a href="Type.html#getMultiplicity()">getMultiplicity</a>, <a href="Type.html#getOutput()">getOutput</a>, <a href="Type.html#getOwnedConjugator()">getOwnedConjugator</a>, <a href="Type.html#getOwnedDifferencing()">getOwnedDifferencing</a>, <a href="Type.html#getOwnedDisjoining()">getOwnedDisjoining</a>, <a href="Type.html#getOwnedEndFeature()">getOwnedEndFeature</a>, <a href="Type.html#getOwnedFeature()">getOwnedFeature</a>, <a href="Type.html#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>, <a href="Type.html#getOwnedIntersecting()">getOwnedIntersecting</a>, <a href="Type.html#getOwnedSpecialization()">getOwnedSpecialization</a>, <a href="Type.html#getOwnedUnioning()">getOwnedUnioning</a>, <a href="Type.html#getUnioningType()">getUnioningType</a>, <a href="Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a>, <a href="Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a>, <a href="Type.html#isAbstract()">isAbstract</a>, <a href="Type.html#isConjugated()">isConjugated</a>, <a href="Type.html#isSufficient()">isSufficient</a>, <a href="Type.html#multiplicities()">multiplicities</a>, <a href="Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a>, <a href="Type.html#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a>, <a href="Type.html#setIsAbstract(boolean)">setIsAbstract</a>, <a href="Type.html#setIsSufficient(boolean)">setIsSufficient</a>, <a href="Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a>, <a href="Type.html#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a>, <a href="Type.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getRelatedFeature()">
<h3>getRelatedFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getRelatedFeature</span>()</div>
<div class="block"><p>The <code>Features</code> that are related by this <code>Connector</code> considered as a <code>Relationship</code> and that restrict the links it identifies, given by the referenced <code>Features</code> of the <code>connectorEnds</code> of the <code>Connector</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the relatedFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="connector"
        redefines=<a href="Relationship.html#getRelatedElement()"><code>Relationship.getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociation()">
<h3>getAssociation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a>&gt;</span> <span class="element-name">getAssociation</span>()</div>
<div class="block"><p>The <code>Associations</code> that type the <code>Connector</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the association value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typedConnector"
        redefines=<a href="Feature.html#getType()"><code>Feature.getType()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectorEnd()">
<h3>getConnectorEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getConnectorEnd</span>()</div>
<div class="block"><p>The <code>endFeatures</code> of a <code>Connector</code>, which redefine the <code>endFeatures</code> of the <code>associations</code> of the <code>Connector</code>. The <code>connectorEnds</code> determine via <code>ReferenceSubsetting</code> <code>Relationships</code> which <code>Features</code> are related by the <code>Connector</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the connectorEnd value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featuringConnector"
        redefines=<a href="Type.html#getEndFeature()"><code>Type.getEndFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceFeature()">
<h3>getSourceFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getSourceFeature</span>()</div>
<div class="block"><p>The source <code>relatedFeature</code> for this <code>Connector</code>. It is the first <code>relatedFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the sourceFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="sourceConnector"
        subsets=<a href="#getRelatedFeature()"><code>getRelatedFeature()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetFeature()">
<h3>getTargetFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getTargetFeature</span>()</div>
<div class="block"><p>The target <code>relatedFeatures</code> for this <code>Connector</code>. This includes all the <code>relatedFeatures</code> other than the <code>sourceFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the targetFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="targetConnector"
        subsets=<a href="#getRelatedFeature()"><code>getRelatedFeature()</code></a>
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultFeaturingType()">
<h3>getDefaultFeaturingType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getDefaultFeaturingType</span>()</div>
<div class="block"><p>The innermost <code>Type</code> that is a common direct or indirect <code>featuringType</code> of the <code>relatedFeatures</code>, such that, if it exists and was the <code>featuringType</code> of this <code>Connector</code>, the <code>Connector</code> would satisfy the <code>checkConnectorTypeFeaturing</code> constraint.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the defaultFeaturingType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featuredConnector"</dd>
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
