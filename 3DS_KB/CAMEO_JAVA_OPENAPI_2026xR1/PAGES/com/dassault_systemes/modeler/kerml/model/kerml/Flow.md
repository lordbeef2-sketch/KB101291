# JAVA OPENAPI: Flow (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Flow.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Flow.html`
- source_sha256: `c9413782fa2b82d2e17e97f2a5c79a4a538223f0d04e5eb499b7cf7a9724c70b`
- captured_utc: `2026-07-14T16:44:49.702866+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Flow

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Connector](Connector.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](Feature.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`, `[Step](Step.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`

@OpenApiAllpublic interfaceFlowextends [Connector](Connector.html), [Step](Step.html)

An `Flow` is a `Step` that represents the transfer of values from one `Feature` to another. `Flows` can take non-zero time to complete.
 
 specializesFromLibrary('Transfers::transfers')
 payloadType =
 if payloadFeature = null then Sequence{}
 else payloadFeature.type
 endif
 sourceOutputFeature =
 if connectorEnd->isEmpty() or 
 connectorEnd.ownedFeature->isEmpty()
 then null
 else connectorEnd.ownedFeature->first()
 endif
 targetInputFeature =
 if connectorEnd->size() < 2 or 
 connectorEnd->at(2).ownedFeature->isEmpty()
 then null
 else connectorEnd->at(2).ownedFeature->first()
 endif
 flowEnd = connectorEnd->selectByKind(FlowEnd)
 payloadFeature =
 let payloadFeatures : Sequence(PayloadFeature) =
 ownedFeature->selectByKind(PayloadFeature) in
 if payloadFeatures->isEmpty() then null
 else payloadFeatures->first()
 endif
 ownedFeature->selectByKind(PayloadFeature)->size() <= 1
 ownedEndFeatures->notEmpty() implies
 specializesFromLibrary('Transfers::flowTransfers')

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FlowEnd](FlowEnd.html)>`
`[getFlowEnd](#getFlowEnd())()`
The `connectorEnds` of this `Flow` that are `FlowEnds`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Interaction](Interaction.html)>`
`[getInteraction](#getInteraction())()`
The `Interactions` that type this `Flow`.
`[PayloadFeature](PayloadFeature.html)`
`[getPayloadFeature](#getPayloadFeature())()`
The `ownedFeature` of the `Flow` that is a `PayloadFeature` (if any).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](Classifier.html)>`
`[getPayloadType](#getPayloadType())()`
The type of values transferred, which is the `type` of the `payloadFeature` of the `Flow`.
`[Feature](Feature.html)`
`[getSourceOutputFeature](#getSourceOutputFeature())()`
The `Feature` that provides the items carried by the `Flow`.
`[Feature](Feature.html)`
`[getTargetInputFeature](#getTargetInputFeature())()`
The `Feature` that receives the values carried by the `Flow`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Connector](Connector.html)
`[getAssociation](Connector.html#getAssociation()), [getConnectorEnd](Connector.html#getConnectorEnd()), [getDefaultFeaturingType](Connector.html#getDefaultFeaturingType()), [getRelatedFeature](Connector.html#getRelatedFeature()), [getSourceFeature](Connector.html#getSourceFeature()), [getTargetFeature](Connector.html#getTargetFeature())`
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
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Step](Step.html)
`[getBehavior](Step.html#getBehavior()), [getParameter](Step.html#getParameter())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Type](Type.html)
`[allRedefinedFeaturesOf](Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](Type.html#allSupertypes()), [directionOf](Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](Type.html#getDifferencingType()), [getDirectedFeature](Type.html#getDirectedFeature()), [getEndFeature](Type.html#getEndFeature()), [getFeature](Type.html#getFeature()), [getFeatureMembership](Type.html#getFeatureMembership()), [getInheritedFeature](Type.html#getInheritedFeature()), [getInheritedMembership](Type.html#getInheritedMembership()), [getInput](Type.html#getInput()), [getIntersectingType](Type.html#getIntersectingType()), [getMultiplicity](Type.html#getMultiplicity()), [getOutput](Type.html#getOutput()), [getOwnedConjugator](Type.html#getOwnedConjugator()), [getOwnedDifferencing](Type.html#getOwnedDifferencing()), [getOwnedDisjoining](Type.html#getOwnedDisjoining()), [getOwnedEndFeature](Type.html#getOwnedEndFeature()), [getOwnedFeature](Type.html#getOwnedFeature()), [getOwnedFeatureMembership](Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](Type.html#getOwnedIntersecting()), [getOwnedSpecialization](Type.html#getOwnedSpecialization()), [getOwnedUnioning](Type.html#getOwnedUnioning()), [getUnioningType](Type.html#getUnioningType()), [inheritableMemberships](Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](Type.html#isAbstract()), [isConjugated](Type.html#isConjugated()), [isSufficient](Type.html#isSufficient()), [multiplicities](Type.html#multiplicities()), [nonPrivateMemberships](Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](Type.html#setIsAbstract(boolean)), [setIsSufficient](Type.html#setIsSufficient(boolean)), [specializes](Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](Type.html#specializesFromLibrary(java.lang.String)), [visibleMemberships](Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getPayloadType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](Classifier.html)> getPayloadType()
The type of values transferred, which is the `type` of the `payloadFeature` of the `Flow`.
Returns:
the payloadType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="flowForPayloadType"
getTargetInputFeature
@CheckForNull[Feature](Feature.html) getTargetInputFeature()
The `Feature` that receives the values carried by the `Flow`. It must be a `feature` of the `target` of the `Flow`.
Returns:
the targetInputFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="flowToInput"
getSourceOutputFeature
@CheckForNull[Feature](Feature.html) getSourceOutputFeature()
The `Feature` that provides the items carried by the `Flow`. It must be a `feature` of the `source` of the `Flow`.
Returns:
the sourceOutputFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="flowFromOutput"
getFlowEnd
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FlowEnd](FlowEnd.html)> getFlowEnd()
The `connectorEnds` of this `Flow` that are `FlowEnds`.
Returns:
the flowEnd value
Model:
derived="true"
 transient="true"
 oppositeRoleName="featuringFlow"
 subsets=[`Connector.getConnectorEnd()`](Connector.html#getConnectorEnd())
getPayloadFeature
@CheckForNull[PayloadFeature](PayloadFeature.html) getPayloadFeature()
The `ownedFeature` of the `Flow` that is a `PayloadFeature` (if any).
Returns:
the payloadFeature value
Model:
derived="true"
 transient="true"
 oppositeRoleName="flowWithPayloadFeature"
 subsets=[`Type.getOwnedFeature()`](Type.html#getOwnedFeature())
getInteraction
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Interaction](Interaction.html)> getInteraction()
The `Interactions` that type this `Flow`. `Interactions` are both `Associations` and `Behaviors`, which can type `Connectors` and `Steps`, respectively.
Returns:
the interaction value
Model:
derived="true"
 transient="true"
 oppositeRoleName="typedFlow"
 redefines=[`Connector.getAssociation()`](Connector.html#getAssociation()), [`Step.getBehavior()`](Step.html#getBehavior())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Flow">Interface Flow</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code>, <code><a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Flow</span><span class="extends-implements">
extends <a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a>, <a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></span></div>
<div class="block"><p>An <code>Flow</code> is a <code>Step</code> that represents the transfer of values from one <code>Feature</code> to another. <code>Flows</code> can take non-zero time to complete.</p>
 
 specializesFromLibrary('Transfers::transfers')
 payloadType =
     if payloadFeature = null then Sequence{}
     else payloadFeature.type
     endif
 sourceOutputFeature =
     if connectorEnd-&gt;isEmpty() or 
         connectorEnd.ownedFeature-&gt;isEmpty()
     then null
     else connectorEnd.ownedFeature-&gt;first()
     endif
 targetInputFeature =
     if connectorEnd-&gt;size() &lt; 2 or 
         connectorEnd-&gt;at(2).ownedFeature-&gt;isEmpty()
     then null
     else connectorEnd-&gt;at(2).ownedFeature-&gt;first()
     endif
 flowEnd = connectorEnd-&gt;selectByKind(FlowEnd)
 payloadFeature =
     let payloadFeatures : Sequence(PayloadFeature) =
         ownedFeature-&gt;selectByKind(PayloadFeature) in
     if payloadFeatures-&gt;isEmpty() then null
     else payloadFeatures-&gt;first()
     endif
 ownedFeature-&gt;selectByKind(PayloadFeature)-&gt;size() &lt;= 1
 ownedEndFeatures-&gt;notEmpty() implies
     specializesFromLibrary('Transfers::flowTransfers')</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFlowEnd()">getFlowEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>connectorEnds</code> of this <code>Flow</code> that are <code>FlowEnds</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInteraction()">getInteraction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Interactions</code> that type this <code>Flow</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPayloadFeature()">getPayloadFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedFeature</code> of the <code>Flow</code> that is a <code>PayloadFeature</code> (if any).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPayloadType()">getPayloadType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The type of values transferred, which is the <code>type</code> of the <code>payloadFeature</code> of the <code>Flow</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSourceOutputFeature()">getSourceOutputFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that provides the items carried by the <code>Flow</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTargetInputFeature()">getTargetInputFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that receives the values carried by the <code>Flow</code>.</div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Connector">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></h3>
<code><a href="Connector.html#getAssociation()">getAssociation</a>, <a href="Connector.html#getConnectorEnd()">getConnectorEnd</a>, <a href="Connector.html#getDefaultFeaturingType()">getDefaultFeaturingType</a>, <a href="Connector.html#getRelatedFeature()">getRelatedFeature</a>, <a href="Connector.html#getSourceFeature()">getSourceFeature</a>, <a href="Connector.html#getTargetFeature()">getTargetFeature</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Step">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></h3>
<code><a href="Step.html#getBehavior()">getBehavior</a>, <a href="Step.html#getParameter()">getParameter</a></code></div>
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
<section class="detail" id="getPayloadType()">
<h3>getPayloadType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a>&gt;</span> <span class="element-name">getPayloadType</span>()</div>
<div class="block"><p>The type of values transferred, which is the <code>type</code> of the <code>payloadFeature</code> of the <code>Flow</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the payloadType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="flowForPayloadType"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetInputFeature()">
<h3>getTargetInputFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getTargetInputFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that receives the values carried by the <code>Flow</code>. It must be a <code>feature</code> of the <code>target</code> of the <code>Flow</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the targetInputFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="flowToInput"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceOutputFeature()">
<h3>getSourceOutputFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getSourceOutputFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that provides the items carried by the <code>Flow</code>. It must be a <code>feature</code> of the <code>source</code> of the <code>Flow</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the sourceOutputFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="flowFromOutput"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlowEnd()">
<h3>getFlowEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a>&gt;</span> <span class="element-name">getFlowEnd</span>()</div>
<div class="block"><p>The <code>connectorEnds</code> of this <code>Flow</code> that are <code>FlowEnds</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the flowEnd value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="featuringFlow"
        subsets=<a href="Connector.html#getConnectorEnd()"><code>Connector.getConnectorEnd()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPayloadFeature()">
<h3>getPayloadFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></span> <span class="element-name">getPayloadFeature</span>()</div>
<div class="block"><p>The <code>ownedFeature</code> of the <code>Flow</code> that is a <code>PayloadFeature</code> (if any).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the payloadFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="flowWithPayloadFeature"
        subsets=<a href="Type.html#getOwnedFeature()"><code>Type.getOwnedFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteraction()">
<h3>getInteraction</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a>&gt;</span> <span class="element-name">getInteraction</span>()</div>
<div class="block"><p>The <code>Interactions</code> that type this <code>Flow</code>. <code>Interactions</code> are both <code>Associations</code> and <code>Behaviors</code>, which can type <code>Connectors</code> and <code>Steps</code>, respectively.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the interaction value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="typedFlow"
        redefines=<a href="Connector.html#getAssociation()"><code>Connector.getAssociation()</code></a>, <a href="Step.html#getBehavior()"><code>Step.getBehavior()</code></a></dd>
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
