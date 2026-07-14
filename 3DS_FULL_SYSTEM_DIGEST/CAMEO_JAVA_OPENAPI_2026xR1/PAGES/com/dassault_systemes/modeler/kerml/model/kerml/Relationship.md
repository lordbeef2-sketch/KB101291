# JAVA OPENAPI: Relationship (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Relationship.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Relationship.html`
- source_sha256: `07293e1f736e10271085a312ac89051986b84e1e82f50650514eab044f771ce8`
- captured_utc: `2026-07-14T16:44:50.295879+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Relationship

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`

All Known Subinterfaces:
`[ActorMembership](../../../sysml/model/sysml/ActorMembership.html)`, `[AllocationDefinition](../../../sysml/model/sysml/AllocationDefinition.html)`, `[AllocationUsage](../../../sysml/model/sysml/AllocationUsage.html)`, `[Annotation](Annotation.html)`, `[Association](Association.html)`, `[AssociationStructure](AssociationStructure.html)`, `[BindingConnector](BindingConnector.html)`, `[BindingConnectorAsUsage](../../../sysml/model/sysml/BindingConnectorAsUsage.html)`, `[ConjugatedPortTyping](../../../sysml/model/sysml/ConjugatedPortTyping.html)`, `[Conjugation](Conjugation.html)`, `[ConnectionDefinition](../../../sysml/model/sysml/ConnectionDefinition.html)`, `[ConnectionUsage](../../../sysml/model/sysml/ConnectionUsage.html)`, `[Connector](Connector.html)`, `[ConnectorAsUsage](../../../sysml/model/sysml/ConnectorAsUsage.html)`, `[CrossSubsetting](CrossSubsetting.html)`, `[Dependency](Dependency.html)`, `[Differencing](Differencing.html)`, `[Disjoining](Disjoining.html)`, `[ElementFilterMembership](ElementFilterMembership.html)`, `[EndFeatureMembership](EndFeatureMembership.html)`, `[Expose](../../../sysml/model/sysml/Expose.html)`, `[FeatureChaining](FeatureChaining.html)`, `[FeatureInverting](FeatureInverting.html)`, `[FeatureMembership](FeatureMembership.html)`, `[FeatureTyping](FeatureTyping.html)`, `[FeatureValue](FeatureValue.html)`, `[Flow](Flow.html)`, `[FlowDefinition](../../../sysml/model/sysml/FlowDefinition.html)`, `[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[FramedConcernMembership](../../../sysml/model/sysml/FramedConcernMembership.html)`, `[Import](Import.html)`, `[Interaction](Interaction.html)`, `[InterfaceDefinition](../../../sysml/model/sysml/InterfaceDefinition.html)`, `[InterfaceUsage](../../../sysml/model/sysml/InterfaceUsage.html)`, `[Intersecting](Intersecting.html)`, `[Membership](Membership.html)`, `[MembershipExpose](../../../sysml/model/sysml/MembershipExpose.html)`, `[MembershipImport](MembershipImport.html)`, `[NamespaceExpose](../../../sysml/model/sysml/NamespaceExpose.html)`, `[NamespaceImport](NamespaceImport.html)`, `[ObjectiveMembership](../../../sysml/model/sysml/ObjectiveMembership.html)`, `[OwningMembership](OwningMembership.html)`, `[ParameterMembership](ParameterMembership.html)`, `[PortConjugation](../../../sysml/model/sysml/PortConjugation.html)`, `[Redefinition](Redefinition.html)`, `[ReferenceSubsetting](ReferenceSubsetting.html)`, `[RequirementConstraintMembership](../../../sysml/model/sysml/RequirementConstraintMembership.html)`, `[RequirementVerificationMembership](../../../sysml/model/sysml/RequirementVerificationMembership.html)`, `[ResultExpressionMembership](ResultExpressionMembership.html)`, `[ReturnParameterMembership](ReturnParameterMembership.html)`, `[Specialization](Specialization.html)`, `[StakeholderMembership](../../../sysml/model/sysml/StakeholderMembership.html)`, `[StateSubactionMembership](../../../sysml/model/sysml/StateSubactionMembership.html)`, `[Subclassification](Subclassification.html)`, `[SubjectMembership](../../../sysml/model/sysml/SubjectMembership.html)`, `[Subsetting](Subsetting.html)`, `[Succession](Succession.html)`, `[SuccessionAsUsage](../../../sysml/model/sysml/SuccessionAsUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`, `[TransitionFeatureMembership](../../../sysml/model/sysml/TransitionFeatureMembership.html)`, `[TypeFeaturing](TypeFeaturing.html)`, `[Unioning](Unioning.html)`, `[VariantMembership](../../../sysml/model/sysml/VariantMembership.html)`, `[ViewRenderingMembership](../../../sysml/model/sysml/ViewRenderingMembership.html)`

@OpenApiAllpublic interfaceRelationshipextends [Element](Element.html)

A `Relationship` is an `Element` that relates other `Element`. Some of its `relatedElements` may be owned, in which case those `ownedRelatedElements` will be deleted from a model if their `owningRelationship` is. A `Relationship` may also be owned by another `Element`, in which case the `ownedRelatedElements` of the `Relationship` are also considered to be transitively owned by the `owningRelatedElement` of the `Relationship`.
The `relatedElements` of a `Relationship` are divided into `source` and `target` `Elements`. The `Relationship` is considered to be directed from the `source` to the `target` `Elements`. An undirected `Relationship` may have either all `source` or all `target` `Elements`.
A "relationship `Element`" in the abstract syntax is generically any `Element` that is an instance of either `Relationship` or a direct or indirect specialization of `Relationship`. Any other kind of `Element` is a "non-relationship `Element`". It is a convention of that non-relationship `Elements` are *only* related via reified relationship `Elements`. Any meta-associations directly between non-relationship `Elements` must be derived from underlying reified `Relationship`.
 
 relatedElement = source->union(target)

Model:
abstract=true

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getOwnedRelatedElement](#getOwnedRelatedElement())()`
The relatedElements of this Relationship that are owned by the Relationship.
`[Element](Element.html)`
`[getOwningRelatedElement](#getOwningRelatedElement())()`
The relatedElement of this Relationship that owns the Relationship, if any.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getRelatedElement](#getRelatedElement())()`
The Elements that are related by this Relationship, derived as the union of the `source` and `target` Elements of the Relationship.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getSource](#getSource())()`
The `relatedElementsinvalid input: '<'/c ode> from which this Relationship is considered to be directed.`
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getTarget](#getTarget())()`
The `relatedElements` to which this Relationship is considered to be directed.
`boolean`
`[isImplied](#isImplied())()`
Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.
`[Namespace](Namespace.html)`
`[libraryNamespace](#libraryNamespace())()`
Return whether this Relationship has either an `owningRelatedElement` or `owningRelationship` that is a library element.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[path](#path())()`
If the `owningRelationship` of the `Relationship` is null but its `owningRelatedElement` is non-null, construct the `path` using the position of the `Relationship` in the list of `ownedRelationships` of its `owningRelatedElement`.
`void`
`[setIsImplied](#setIsImplied(boolean))(boolean value)`
Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.
`void`
`[setOwningRelatedElement](#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) value)`
The relatedElement of this Relationship that owns the Relationship, if any.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
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
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getRelatedElement
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getRelatedElement()
The Elements that are related by this Relationship, derived as the union of the `source` and `target` Elements of the Relationship.
Returns:
the relatedElement value
Model:
derived="true"
 transient="true"
 oppositeRoleName="relationship"
getTarget
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getTarget()
The `relatedElements` to which this Relationship is considered to be directed.
Returns:
the target value
Model:
derived="false"
 transient="false"
 oppositeRoleName="targetRelationship"
 subsets=[`getRelatedElement()`](#getRelatedElement())
getSource
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getSource()
The `relatedElementsinvalid input: '<'/c ode> from which this Relationship is considered to be directed.`
Returns:
the source value
Model:
derived="false"
 transient="false"
 oppositeRoleName="sourceRelationship"
 subsets=[`getRelatedElement()`](#getRelatedElement())
getOwningRelatedElement
@CheckForNull[Element](Element.html) getOwningRelatedElement()
The relatedElement of this Relationship that owns the Relationship, if any.
Returns:
the owningRelatedElement value
Model:
derived="false"
 transient="false"
 container="true"
 opposite=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
 subsets=[`getRelatedElement()`](#getRelatedElement())
setOwningRelatedElement
void setOwningRelatedElement(@CheckForNull
 [Element](Element.html) value)
The relatedElement of this Relationship that owns the Relationship, if any.
Parameters:
`value` - the owningRelatedElement value
Model:
derived="false"
 transient="false"
 container="true"
 opposite=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
 subsets=[`getRelatedElement()`](#getRelatedElement())
getOwnedRelatedElement
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getOwnedRelatedElement()
The relatedElements of this Relationship that are owned by the Relationship.
Returns:
the ownedRelatedElement value
Model:
derived="false"
 transient="false"
 containment="true"
 opposite=[`Element.getOwningRelationship()`](Element.html#getOwningRelationship())
 subsets=[`getRelatedElement()`](#getRelatedElement())
isImplied
boolean isImplied()
Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.
Returns:
the isImplied value
Model:
derived="false"
 transient="false"
setIsImplied
void setIsImplied(boolean value)
Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.
Parameters:
`value` - the isImplied value
Model:
derived="false"
 transient="false"
libraryNamespace
[Namespace](Namespace.html) libraryNamespace()
Return whether this Relationship has either an `owningRelatedElement` or `owningRelationship` that is a library element.
 if owningRelatedElement <> null then owningRelatedElement.libraryNamespace()
 else if owningRelationship <> null then owningRelationship.libraryNamespace() 
 else null endif endif
Specified by:
`[libraryNamespace](Element.html#libraryNamespace())` in interface `[Element](Element.html)`
path
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) path()
If the `owningRelationship` of the `Relationship` is null but its `owningRelatedElement` is non-null, construct the `path` using the position of the `Relationship` in the list of `ownedRelationships` of its `owningRelatedElement`. Otherwise, return the `path` of the `Relationship` as specified for an `Element` in general.
 if owningRelationship = null and owningRelatedElement <> null then
 owningRelatedElement.path() + '/' + 
 owningRelatedElement.ownedRelationship->indexOf(self).toString()
 -- A position index shall be converted to a decimal string representation 
 -- consisting of only decimal digits, with no sign, leading zeros or leading 
 -- or trailing whitespace.
 else self.oclAsType(Element).path()
 endif
Specified by:
`[path](Element.html#path())` in interface `[Element](Element.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Relationship">Interface Relationship</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a></code>, <code><a href="../../../sysml/model/sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></code>, <code><a href="Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a></code>, <code><a href="AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></code>, <code><a href="BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code>, <code><a href="../../../sysml/model/sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a></code>, <code><a href="Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code>, <code><a href="../../../sysml/model/sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a></code>, <code><a href="Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a></code>, <code><a href="Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a></code>, <code><a href="Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a></code>, <code><a href="ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a></code>, <code><a href="EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a></code>, <code><a href="../../../sysml/model/sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a></code>, <code><a href="FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a></code>, <code><a href="FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a></code>, <code><a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></code>, <code><a href="FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></code>, <code><a href="FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code>, <code><a href="Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code>, <code><a href="../../../sysml/model/sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code>, <code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a></code>, <code><a href="Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a></code>, <code><a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a></code>, <code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code>, <code><a href="../../../sysml/model/sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a></code>, <code><a href="MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a></code>, <code><a href="../../../sysml/model/sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a></code>, <code><a href="NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a></code>, <code><a href="../../../sysml/model/sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a></code>, <code><a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code>, <code><a href="ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a></code>, <code><a href="Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a></code>, <code><a href="ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a></code>, <code><a href="../../../sysml/model/sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a></code>, <code><a href="../../../sysml/model/sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a></code>, <code><a href="ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a></code>, <code><a href="ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a></code>, <code><a href="Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></code>, <code><a href="../../../sysml/model/sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a></code>, <code><a href="../../../sysml/model/sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a></code>, <code><a href="Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a></code>, <code><a href="../../../sysml/model/sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a></code>, <code><a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></code>, <code><a href="Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a></code>, <code><a href="TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a></code>, <code><a href="Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a></code>, <code><a href="../../../sysml/model/sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a></code>, <code><a href="../../../sysml/model/sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Relationship</span><span class="extends-implements">
extends <a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span></div>
<div class="block"><p>A <code>Relationship</code> is an <code>Element</code> that relates other <code>Element</code>. Some of its <code>relatedElements</code> may be owned, in which case those <code>ownedRelatedElements</code> will be deleted from a model if their <code>owningRelationship</code> is. A <code>Relationship</code> may also be owned by another <code>Element</code>, in which case the <code>ownedRelatedElements</code> of the <code>Relationship</code> are also considered to be transitively owned by the <code>owningRelatedElement</code> of the <code>Relationship</code>.</p>
<p>The <code>relatedElements</code> of a <code>Relationship</code> are divided into <code>source</code> and <code>target</code> <code>Elements</code>. The <code>Relationship</code> is considered to be directed from the <code>source</code> to the <code>target</code> <code>Elements</code>. An undirected <code>Relationship</code> may have either all <code>source</code> or all <code>target</code> <code>Elements</code>.</p>
<p>A "relationship <code>Element</code>" in the abstract syntax is generically any <code>Element</code> that is an instance of either <code>Relationship</code> or a direct or indirect specialization of <code>Relationship</code>. Any other kind of <code>Element</code> is a "non-relationship <code>Element</code>". It is a convention of that non-relationship <code>Elements</code> are <em>only</em> related via reified relationship <code>Elements</code>. Any meta-associations directly between non-relationship <code>Elements</code> must be derived from underlying reified <code>Relationship</code>.</p>
 
 relatedElement = source-&gt;union(target)</div>
<dl class="notes">
<dt>Model:</dt>
<dd>abstract=true</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedRelatedElement()">getOwnedRelatedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <tt>relatedElements</tt> of this Relationship that are owned by the Relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningRelatedElement()">getOwningRelatedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <tt>relatedElement</tt> of this Relationship that owns the Relationship, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRelatedElement()">getRelatedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Elements that are related by this Relationship, derived as the union of the <code>source</code> and <code>target</code> Elements of the Relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>relatedElements<span class="invalid-tag">invalid input: '&lt;'</span>/c ode&gt; from which this Relationship is considered to be directed.</code></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>relatedElements</code> to which this Relationship is considered to be directed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isImplied()">isImplied</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#libraryNamespace()">libraryNamespace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return whether this Relationship has either an <code>owningRelatedElement</code> or <code>owningRelationship</code> that is a library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#path()">path</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If the <code>owningRelationship</code> of the <code>Relationship</code> is null but its <code>owningRelatedElement</code> is non-null, construct the <code>path</code> using the position of the <code>Relationship</code> in the list of <code>ownedRelationships</code> of its <code>owningRelatedElement</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsImplied(boolean)">setIsImplied</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <tt>relatedElement</tt> of this Relationship that owns the Relationship, if any.</div>
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
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
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
<section class="detail" id="getRelatedElement()">
<h3>getRelatedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getRelatedElement</span>()</div>
<div class="block"><p>The Elements that are related by this Relationship, derived as the union of the <code>source</code> and <code>target</code> Elements of the Relationship.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the relatedElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="relationship"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTarget()">
<h3>getTarget</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getTarget</span>()</div>
<div class="block"><p>The <code>relatedElements</code> to which this Relationship is considered to be directed.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the target value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="targetRelationship"
        subsets=<a href="#getRelatedElement()"><code>getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getSource</span>()</div>
<div class="block"><p>The <code>relatedElements<span class="invalid-tag">invalid input: '&lt;'</span>/c ode&gt; from which this Relationship is considered to be directed.</code></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the source value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="sourceRelationship"
        subsets=<a href="#getRelatedElement()"><code>getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningRelatedElement()">
<h3>getOwningRelatedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getOwningRelatedElement</span>()</div>
<div class="block"><p>The <tt>relatedElement</tt> of this Relationship that owns the Relationship, if any.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningRelatedElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        container="true"
        opposite=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a>
        subsets=<a href="#getRelatedElement()"><code>getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setOwningRelatedElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningRelatedElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</span></div>
<div class="block"><p>The <tt>relatedElement</tt> of this Relationship that owns the Relationship, if any.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the owningRelatedElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        container="true"
        opposite=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a>
        subsets=<a href="#getRelatedElement()"><code>getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRelatedElement()">
<h3>getOwnedRelatedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getOwnedRelatedElement</span>()</div>
<div class="block"><p>The <tt>relatedElements</tt> of this Relationship that are owned by the Relationship.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedRelatedElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        containment="true"
        opposite=<a href="Element.html#getOwningRelationship()"><code>Element.getOwningRelationship()</code></a>
        subsets=<a href="#getRelatedElement()"><code>getRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImplied()">
<h3>isImplied</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isImplied</span>()</div>
<div class="block"><p>Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isImplied value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsImplied(boolean)">
<h3>setIsImplied</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsImplied</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether this Relationship was generated by tooling to meet semantic rules, rather than being directly created by a modeler.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isImplied value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="libraryNamespace()">
<h3>libraryNamespace</h3>
<div class="member-signature"><span class="return-type"><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">libraryNamespace</span>()</div>
<div class="block"><p>Return whether this Relationship has either an <code>owningRelatedElement</code> or <code>owningRelationship</code> that is a library element.</p>
 if owningRelatedElement &lt;&gt; null then owningRelatedElement.libraryNamespace()
 else if owningRelationship &lt;&gt; null then owningRelationship.libraryNamespace() 
 else null endif endif</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Element.html#libraryNamespace()">libraryNamespace</a></code> in interface <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="path()">
<h3>path</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">path</span>()</div>
<div class="block"><p>If the <code>owningRelationship</code> of the <code>Relationship</code> is null but its <code>owningRelatedElement</code> is non-null, construct the <code>path</code> using the position of the <code>Relationship</code> in the list of <code>ownedRelationships</code> of its <code>owningRelatedElement</code>. Otherwise, return the <code>path</code> of the <code>Relationship</code> as specified for an <code>Element</code> in general.</p>
 if owningRelationship = null and owningRelatedElement &lt;&gt; null then
     owningRelatedElement.path() + '/' + 
     owningRelatedElement.ownedRelationship-&gt;indexOf(self).toString()
     -- A position index shall be converted to a decimal string representation 
     -- consisting of only decimal digits, with no sign, leading zeros or leading 
     -- or trailing whitespace.
 else self.oclAsType(Element).path()
 endif</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Element.html#path()">path</a></code> in interface <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></dd>
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
