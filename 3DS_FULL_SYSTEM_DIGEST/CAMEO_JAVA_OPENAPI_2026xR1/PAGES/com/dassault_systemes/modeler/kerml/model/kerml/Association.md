# JAVA OPENAPI: Association (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Association.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Association.html`
- source_sha256: `c2175264eb53e136b77d89a0ba36d55fc08e7401faa6512b34960e574b31fffd`
- captured_utc: `2026-07-14T16:44:48.556849+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Association

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Classifier](Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[AllocationDefinition](../../../sysml/model/sysml/AllocationDefinition.html)`, `[AssociationStructure](AssociationStructure.html)`, `[ConnectionDefinition](../../../sysml/model/sysml/ConnectionDefinition.html)`, `[FlowDefinition](../../../sysml/model/sysml/FlowDefinition.html)`, `[Interaction](Interaction.html)`, `[InterfaceDefinition](../../../sysml/model/sysml/InterfaceDefinition.html)`

@OpenApiAllpublic interfaceAssociationextends [Classifier](Classifier.html), [Relationship](Relationship.html)

An `Association` is a `Relationship` and a `Classifier` to enable classification of links between things (in the universe). The co-domains (`types`) of the `associationEnd` `Features` are the `relatedTypes`, as co-domain and participants (linked things) of an `Association` identify each other.
 
 relatedType = associationEnd.type
 specializesFromLibrary('Links::Link')
 oclIsKindOf(Structure) = oclIsKindOf(AssociationStructure)
 associationEnd->size() = 2 implies
 specializesFromLibrary('Links::BinaryLink')
 not isAbstract implies relatedType->size() >= 2
 associationEnds->size() > 2 implies
 not specializesFromLibrary('Links::BinaryLink')
 sourceType =
 if relatedType->isEmpty() then null
 else relatedType->first() endif
 targetType =
 if relatedType->size() < 2 then OrderedSet{}
 else 
 relatedType->
 subSequence(2, relatedType->size())->
 asOrderedSet() 
 endif
 ownedEndFeature->forAll(type->size() = 1)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)>`
`[getAssociationEnd](#getAssociationEnd())()`
The `features` of the `Association` that identify the things that can be related by it.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getRelatedType](#getRelatedType())()`
The `types` of the `associationEnds` of the `Association`, which are the `relatedElements` of the `Association` considered as a `Relationship`.
`[Type](Type.html)`
`[getSourceType](#getSourceType())()`
The source `relatedType` for this `Association`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)>`
`[getTargetType](#getTargetType())()`
The target `relatedTypes` for this `Association`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Classifier](Classifier.html)
`[getOwnedSubclassification](Classifier.html#getOwnedSubclassification())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
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
`[allRedefinedFeaturesOf](Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [allSupertypes](Type.html#allSupertypes()), [directionOf](Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [directionOfExcluding](Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)), [getDifferencingType](Type.html#getDifferencingType()), [getDirectedFeature](Type.html#getDirectedFeature()), [getEndFeature](Type.html#getEndFeature()), [getFeature](Type.html#getFeature()), [getFeatureMembership](Type.html#getFeatureMembership()), [getInheritedFeature](Type.html#getInheritedFeature()), [getInheritedMembership](Type.html#getInheritedMembership()), [getInput](Type.html#getInput()), [getIntersectingType](Type.html#getIntersectingType()), [getMultiplicity](Type.html#getMultiplicity()), [getOutput](Type.html#getOutput()), [getOwnedConjugator](Type.html#getOwnedConjugator()), [getOwnedDifferencing](Type.html#getOwnedDifferencing()), [getOwnedDisjoining](Type.html#getOwnedDisjoining()), [getOwnedEndFeature](Type.html#getOwnedEndFeature()), [getOwnedFeature](Type.html#getOwnedFeature()), [getOwnedFeatureMembership](Type.html#getOwnedFeatureMembership()), [getOwnedIntersecting](Type.html#getOwnedIntersecting()), [getOwnedSpecialization](Type.html#getOwnedSpecialization()), [getOwnedUnioning](Type.html#getOwnedUnioning()), [getUnioningType](Type.html#getUnioningType()), [inheritableMemberships](Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)), [inheritedMemberships](Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)), [isAbstract](Type.html#isAbstract()), [isCompatibleWith](Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [isConjugated](Type.html#isConjugated()), [isSufficient](Type.html#isSufficient()), [multiplicities](Type.html#multiplicities()), [nonPrivateMemberships](Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)), [removeRedefinedFeatures](Type.html#removeRedefinedFeatures(java.util.List)), [setIsAbstract](Type.html#setIsAbstract(boolean)), [setIsSufficient](Type.html#setIsSufficient(boolean)), [specializes](Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [specializesFromLibrary](Type.html#specializesFromLibrary(java.lang.String)), [supertypes](Type.html#supertypes(boolean)), [visibleMemberships](Type.html#visibleMemberships(java.util.List,boolean,boolean))`

============ METHOD DETAIL ========== 
Method Details
getRelatedType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getRelatedType()
The `types` of the `associationEnds` of the `Association`, which are the `relatedElements` of the `Association` considered as a `Relationship`.
Returns:
the relatedType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="association"
 redefines=[`Relationship.getRelatedElement()`](Relationship.html#getRelatedElement())
getSourceType
@CheckForNull[Type](Type.html) getSourceType()
The source `relatedType` for this `Association`. It is the first `relatedType` of the `Association`.
Returns:
the sourceType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="sourceAssociation"
 subsets=[`getRelatedType()`](#getRelatedType())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
getTargetType
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](Type.html)> getTargetType()
The target `relatedTypes` for this `Association`. This includes all the `relatedTypes` other than the `sourceType`.
Returns:
the targetType value
Model:
derived="true"
 transient="true"
 oppositeRoleName="targetAssociation"
 subsets=[`getRelatedType()`](#getRelatedType())
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
getAssociationEnd
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](Feature.html)> getAssociationEnd()
The `features` of the `Association` that identify the things that can be related by it. A concrete `Association` must have at least two `associationEnds`. When it has exactly two, the `Association` is called a *binary* `Association`.
Returns:
the associationEnd value
Model:
derived="true"
 transient="true"
 oppositeRoleName="associationWithEnd"
 redefines=[`Type.getEndFeature()`](Type.html#getEndFeature())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Association">Interface Association</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code>, <code><a href="AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code>, <code><a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Association</span><span class="extends-implements">
extends <a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a>, <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span></div>
<div class="block"><p>An <code>Association</code> is a <code>Relationship</code> and a <code>Classifier</code> to enable classification of links between things (in the universe). The co-domains (<code>types</code>) of the <code>associationEnd</code> <code>Features</code> are the <code>relatedTypes</code>, as co-domain and participants (linked things) of an <code>Association</code> identify each other.</p>
 
 relatedType = associationEnd.type
 specializesFromLibrary('Links::Link')
 oclIsKindOf(Structure) = oclIsKindOf(AssociationStructure)
 associationEnd-&gt;size() = 2 implies
     specializesFromLibrary('Links::BinaryLink')
 not isAbstract implies relatedType-&gt;size() &gt;= 2
 associationEnds-&gt;size() &gt; 2 implies
     not specializesFromLibrary('Links::BinaryLink')
 sourceType =
     if relatedType-&gt;isEmpty() then null
     else relatedType-&gt;first() endif
 targetType =
     if relatedType-&gt;size() &lt; 2 then OrderedSet{}
     else 
         relatedType-&gt;
             subSequence(2, relatedType-&gt;size())-&gt;
             asOrderedSet() 
     endif
 ownedEndFeature-&gt;forAll(type-&gt;size() = 1)</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAssociationEnd()">getAssociationEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>features</code> of the <code>Association</code> that identify the things that can be related by it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRelatedType()">getRelatedType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>types</code> of the <code>associationEnds</code> of the <code>Association</code>, which are the <code>relatedElements</code> of the <code>Association</code> considered as a <code>Relationship</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSourceType()">getSourceType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The source <code>relatedType</code> for this <code>Association</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTargetType()">getTargetType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The target <code>relatedTypes</code> for this <code>Association</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Classifier">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></h3>
<code><a href="Classifier.html#getOwnedSubclassification()">getOwnedSubclassification</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="Element.html#effectiveName()">effectiveName</a>, <a href="Element.html#effectiveShortName()">effectiveShortName</a>, <a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
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
<code><a href="Type.html#allRedefinedFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">allRedefinedFeaturesOf</a>, <a href="Type.html#allSupertypes()">allSupertypes</a>, <a href="Type.html#directionOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">directionOf</a>, <a href="Type.html#directionOfExcluding(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">directionOfExcluding</a>, <a href="Type.html#getDifferencingType()">getDifferencingType</a>, <a href="Type.html#getDirectedFeature()">getDirectedFeature</a>, <a href="Type.html#getEndFeature()">getEndFeature</a>, <a href="Type.html#getFeature()">getFeature</a>, <a href="Type.html#getFeatureMembership()">getFeatureMembership</a>, <a href="Type.html#getInheritedFeature()">getInheritedFeature</a>, <a href="Type.html#getInheritedMembership()">getInheritedMembership</a>, <a href="Type.html#getInput()">getInput</a>, <a href="Type.html#getIntersectingType()">getIntersectingType</a>, <a href="Type.html#getMultiplicity()">getMultiplicity</a>, <a href="Type.html#getOutput()">getOutput</a>, <a href="Type.html#getOwnedConjugator()">getOwnedConjugator</a>, <a href="Type.html#getOwnedDifferencing()">getOwnedDifferencing</a>, <a href="Type.html#getOwnedDisjoining()">getOwnedDisjoining</a>, <a href="Type.html#getOwnedEndFeature()">getOwnedEndFeature</a>, <a href="Type.html#getOwnedFeature()">getOwnedFeature</a>, <a href="Type.html#getOwnedFeatureMembership()">getOwnedFeatureMembership</a>, <a href="Type.html#getOwnedIntersecting()">getOwnedIntersecting</a>, <a href="Type.html#getOwnedSpecialization()">getOwnedSpecialization</a>, <a href="Type.html#getOwnedUnioning()">getOwnedUnioning</a>, <a href="Type.html#getUnioningType()">getUnioningType</a>, <a href="Type.html#inheritableMemberships(java.util.List,java.util.List,boolean)">inheritableMemberships</a>, <a href="Type.html#inheritedMemberships(java.util.List,java.util.List,boolean)">inheritedMemberships</a>, <a href="Type.html#isAbstract()">isAbstract</a>, <a href="Type.html#isCompatibleWith(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isCompatibleWith</a>, <a href="Type.html#isConjugated()">isConjugated</a>, <a href="Type.html#isSufficient()">isSufficient</a>, <a href="Type.html#multiplicities()">multiplicities</a>, <a href="Type.html#nonPrivateMemberships(java.util.List,java.util.List,boolean)">nonPrivateMemberships</a>, <a href="Type.html#removeRedefinedFeatures(java.util.List)">removeRedefinedFeatures</a>, <a href="Type.html#setIsAbstract(boolean)">setIsAbstract</a>, <a href="Type.html#setIsSufficient(boolean)">setIsSufficient</a>, <a href="Type.html#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a>, <a href="Type.html#specializesFromLibrary(java.lang.String)">specializesFromLibrary</a>, <a href="Type.html#supertypes(boolean)">supertypes</a>, <a href="Type.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
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
<section class="detail" id="getRelatedType()">
<h3>getRelatedType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getRelatedType</span>()</div>
<div class="block"><p>The <code>types</code> of the <code>associationEnds</code> of the <code>Association</code>, which are the <code>relatedElements</code> of the <code>Association</code> considered as a <code>Relationship</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the relatedType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="association"
        redefines=<a href="Relationship.html#getRelatedElement()"><code>Relationship.getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceType()">
<h3>getSourceType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getSourceType</span>()</div>
<div class="block"><p>The source <code>relatedType</code> for this <code>Association</code>. It is the first <code>relatedType</code> of the <code>Association</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the sourceType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="sourceAssociation"
        subsets=<a href="#getRelatedType()"><code>getRelatedType()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetType()">
<h3>getTargetType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getTargetType</span>()</div>
<div class="block"><p>The target <code>relatedTypes</code> for this <code>Association</code>. This includes all the <code>relatedTypes</code> other than the <code>sourceType</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the targetType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="targetAssociation"
        subsets=<a href="#getRelatedType()"><code>getRelatedType()</code></a>
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationEnd()">
<h3>getAssociationEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getAssociationEnd</span>()</div>
<div class="block"><p>The <code>features</code> of the <code>Association</code> that identify the things that can be related by it. A concrete <code>Association</code> must have at least two <code>associationEnds</code>. When it has exactly two, the <code>Association</code> is called a <em>binary</em> <code>Association</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the associationEnd value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="associationWithEnd"
        redefines=<a href="Type.html#getEndFeature()"><code>Type.getEndFeature()</code></a></dd>
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
