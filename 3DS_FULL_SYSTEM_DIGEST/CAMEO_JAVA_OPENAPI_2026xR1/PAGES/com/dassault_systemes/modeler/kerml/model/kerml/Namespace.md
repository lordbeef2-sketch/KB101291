# JAVA OPENAPI: Namespace (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Namespace.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Namespace.html`
- source_sha256: `d7c307ccfbfee30f482202ae18b78af695741280c7e9087bc64ab1c75cf7ba3b`
- captured_utc: `2026-07-14T16:44:50.795880+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Namespace

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`

All Known Subinterfaces:
`[AcceptActionUsage](../../../sysml/model/sysml/AcceptActionUsage.html)`, `[ActionDefinition](../../../sysml/model/sysml/ActionDefinition.html)`, `[ActionUsage](../../../sysml/model/sysml/ActionUsage.html)`, `[AllocationDefinition](../../../sysml/model/sysml/AllocationDefinition.html)`, `[AllocationUsage](../../../sysml/model/sysml/AllocationUsage.html)`, `[AnalysisCaseDefinition](../../../sysml/model/sysml/AnalysisCaseDefinition.html)`, `[AnalysisCaseUsage](../../../sysml/model/sysml/AnalysisCaseUsage.html)`, `[AssertConstraintUsage](../../../sysml/model/sysml/AssertConstraintUsage.html)`, `[AssignmentActionUsage](../../../sysml/model/sysml/AssignmentActionUsage.html)`, `[Association](Association.html)`, `[AssociationStructure](AssociationStructure.html)`, `[AttributeDefinition](../../../sysml/model/sysml/AttributeDefinition.html)`, `[AttributeUsage](../../../sysml/model/sysml/AttributeUsage.html)`, `[Behavior](Behavior.html)`, `[BindingConnector](BindingConnector.html)`, `[BindingConnectorAsUsage](../../../sysml/model/sysml/BindingConnectorAsUsage.html)`, `[BooleanExpression](BooleanExpression.html)`, `[CalculationDefinition](../../../sysml/model/sysml/CalculationDefinition.html)`, `[CalculationUsage](../../../sysml/model/sysml/CalculationUsage.html)`, `[CaseDefinition](../../../sysml/model/sysml/CaseDefinition.html)`, `[CaseUsage](../../../sysml/model/sysml/CaseUsage.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[CollectExpression](CollectExpression.html)`, `[ConcernDefinition](../../../sysml/model/sysml/ConcernDefinition.html)`, `[ConcernUsage](../../../sysml/model/sysml/ConcernUsage.html)`, `[ConjugatedPortDefinition](../../../sysml/model/sysml/ConjugatedPortDefinition.html)`, `[ConnectionDefinition](../../../sysml/model/sysml/ConnectionDefinition.html)`, `[ConnectionUsage](../../../sysml/model/sysml/ConnectionUsage.html)`, `[Connector](Connector.html)`, `[ConnectorAsUsage](../../../sysml/model/sysml/ConnectorAsUsage.html)`, `[ConstraintDefinition](../../../sysml/model/sysml/ConstraintDefinition.html)`, `[ConstraintUsage](../../../sysml/model/sysml/ConstraintUsage.html)`, `[ConstructorExpression](ConstructorExpression.html)`, `[ControlNode](../../../sysml/model/sysml/ControlNode.html)`, `[DataType](DataType.html)`, `[DecisionNode](../../../sysml/model/sysml/DecisionNode.html)`, `[Definition](../../../sysml/model/sysml/Definition.html)`, `[EnumerationDefinition](../../../sysml/model/sysml/EnumerationDefinition.html)`, `[EnumerationUsage](../../../sysml/model/sysml/EnumerationUsage.html)`, `[EventOccurrenceUsage](../../../sysml/model/sysml/EventOccurrenceUsage.html)`, `[ExhibitStateUsage](../../../sysml/model/sysml/ExhibitStateUsage.html)`, `[Expression](Expression.html)`, `[Feature](Feature.html)`, `[FeatureChainExpression](FeatureChainExpression.html)`, `[FeatureReferenceExpression](FeatureReferenceExpression.html)`, `[Flow](Flow.html)`, `[FlowDefinition](../../../sysml/model/sysml/FlowDefinition.html)`, `[FlowEnd](FlowEnd.html)`, `[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[ForkNode](../../../sysml/model/sysml/ForkNode.html)`, `[ForLoopActionUsage](../../../sysml/model/sysml/ForLoopActionUsage.html)`, `[Function](Function.html)`, `[IfActionUsage](../../../sysml/model/sysml/IfActionUsage.html)`, `[IncludeUseCaseUsage](../../../sysml/model/sysml/IncludeUseCaseUsage.html)`, `[IndexExpression](IndexExpression.html)`, `[InstantiationExpression](InstantiationExpression.html)`, `[Interaction](Interaction.html)`, `[InterfaceDefinition](../../../sysml/model/sysml/InterfaceDefinition.html)`, `[InterfaceUsage](../../../sysml/model/sysml/InterfaceUsage.html)`, `[Invariant](Invariant.html)`, `[InvocationExpression](InvocationExpression.html)`, `[ItemDefinition](../../../sysml/model/sysml/ItemDefinition.html)`, `[ItemUsage](../../../sysml/model/sysml/ItemUsage.html)`, `[JoinNode](../../../sysml/model/sysml/JoinNode.html)`, `[LibraryPackage](LibraryPackage.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralExpression](LiteralExpression.html)`, `[LiteralInfinity](LiteralInfinity.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralRational](LiteralRational.html)`, `[LiteralString](LiteralString.html)`, `[LoopActionUsage](../../../sysml/model/sysml/LoopActionUsage.html)`, `[MergeNode](../../../sysml/model/sysml/MergeNode.html)`, `[Metaclass](Metaclass.html)`, `[MetadataAccessExpression](MetadataAccessExpression.html)`, `[MetadataDefinition](../../../sysml/model/sysml/MetadataDefinition.html)`, `[MetadataFeature](MetadataFeature.html)`, `[MetadataUsage](../../../sysml/model/sysml/MetadataUsage.html)`, `[Multiplicity](Multiplicity.html)`, `[MultiplicityRange](MultiplicityRange.html)`, `[NullExpression](NullExpression.html)`, `[OccurrenceDefinition](../../../sysml/model/sysml/OccurrenceDefinition.html)`, `[OccurrenceUsage](../../../sysml/model/sysml/OccurrenceUsage.html)`, `[OperatorExpression](OperatorExpression.html)`, `[Package](Package.html)`, `[PartDefinition](../../../sysml/model/sysml/PartDefinition.html)`, `[PartUsage](../../../sysml/model/sysml/PartUsage.html)`, `[PayloadFeature](PayloadFeature.html)`, `[PerformActionUsage](../../../sysml/model/sysml/PerformActionUsage.html)`, `[PortDefinition](../../../sysml/model/sysml/PortDefinition.html)`, `[PortUsage](../../../sysml/model/sysml/PortUsage.html)`, `[Predicate](Predicate.html)`, `[ReferenceUsage](../../../sysml/model/sysml/ReferenceUsage.html)`, `[RenderingDefinition](../../../sysml/model/sysml/RenderingDefinition.html)`, `[RenderingUsage](../../../sysml/model/sysml/RenderingUsage.html)`, `[RequirementDefinition](../../../sysml/model/sysml/RequirementDefinition.html)`, `[RequirementUsage](../../../sysml/model/sysml/RequirementUsage.html)`, `[SatisfyRequirementUsage](../../../sysml/model/sysml/SatisfyRequirementUsage.html)`, `[SelectExpression](SelectExpression.html)`, `[SendActionUsage](../../../sysml/model/sysml/SendActionUsage.html)`, `[StateDefinition](../../../sysml/model/sysml/StateDefinition.html)`, `[StateUsage](../../../sysml/model/sysml/StateUsage.html)`, `[Step](Step.html)`, `[Structure](Structure.html)`, `[Succession](Succession.html)`, `[SuccessionAsUsage](../../../sysml/model/sysml/SuccessionAsUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`, `[TerminateActionUsage](../../../sysml/model/sysml/TerminateActionUsage.html)`, `[TransitionUsage](../../../sysml/model/sysml/TransitionUsage.html)`, `[TriggerInvocationExpression](../../../sysml/model/sysml/TriggerInvocationExpression.html)`, `[Type](Type.html)`, `[Usage](../../../sysml/model/sysml/Usage.html)`, `[UseCaseDefinition](../../../sysml/model/sysml/UseCaseDefinition.html)`, `[UseCaseUsage](../../../sysml/model/sysml/UseCaseUsage.html)`, `[VerificationCaseDefinition](../../../sysml/model/sysml/VerificationCaseDefinition.html)`, `[VerificationCaseUsage](../../../sysml/model/sysml/VerificationCaseUsage.html)`, `[ViewDefinition](../../../sysml/model/sysml/ViewDefinition.html)`, `[ViewpointDefinition](../../../sysml/model/sysml/ViewpointDefinition.html)`, `[ViewpointUsage](../../../sysml/model/sysml/ViewpointUsage.html)`, `[ViewUsage](../../../sysml/model/sysml/ViewUsage.html)`, `[WhileLoopActionUsage](../../../sysml/model/sysml/WhileLoopActionUsage.html)`

@OpenApiAllpublic interfaceNamespaceextends [Element](Element.html)

A `Namespace` is an `Element` that contains other `Elements`, known as its `members`, via `Membership` `Relationships` with those `Elements`. The `members` of a `Namespace` may be owned by the `Namespace`, aliased in the `Namespace`, or imported into the `Namespace` via `Import` `Relationships`.
A `Namespace` can provide names for its `members` via the `memberNames` and `memberShortNames` specified by the `Memberships` in the `Namespace`. If a `Membership` specifies a `memberName` and/or `memberShortName`, then those are names of the corresponding `memberElement` relative to the `Namespace`. For an `OwningMembership`, the `ownedMemberName` and `ownedMemberShortName` are given by the `Element` `name` and `shortName`. Note that the same `Element` may be the `memberElement` of multiple `Memberships` in a `Namespace` (though it may be owned at most once), each of which may define a separate alias for the `Element` relative to the `Namespace`.
 
 membership->forAll(m1 | 
 membership->forAll(m2 | 
 m1 <> m2 implies m1.isDistinguishableFrom(m2)))
 member = membership.memberElement
 ownedMember = ownedMembership->selectByKind(OwningMembership).ownedMemberElement
 importedMembership = importedMemberships(Set{})
 ownedImport = ownedRelationship->selectByKind(Import)
 ownedMembership = ownedRelationship->selectByKind(Membership)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[getImportedMembership](#getImportedMembership())()`
The `Memberships` in this `Namespace` that result from the `ownedImports` of this `Namespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getMember](#getMember())()`
The set of all member `Elements` of this `Namespace`, which are the `memberElements` of all `memberships` of the `Namespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[getMembership](#getMembership())()`
All `Memberships` in this `Namespace`, including (at least) the union of `ownedMemberships` and `importedMemberships`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Import](Import.html)>`
`[getOwnedImport](#getOwnedImport())()`
The `ownedRelationships` of this `Namespace` that are `Imports`, for which the `Namespace` is the `importOwningNamespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getOwnedMember](#getOwnedMember())()`
The owned `members` of this `Namespace`, which are the `ownedMemberElements` of the `ownedMemberships` of the `Namespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[getOwnedMembership](#getOwnedMembership())()`
The `ownedRelationships` of this `Namespace` that are `Memberships`, for which the `Namespace` is the `membershipOwningNamespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[importedMemberships](#importedMemberships(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded)`
Derive the imported `Memberships` of this `Namespace` as the `importedMembership` of all `ownedImports`, excluding those Imports whose `importOwningNamespace` is in the `excluded` set, and excluding `Memberships` that have distinguisibility collisions with each other or with any `ownedMembership`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[membershipsOfVisibility](#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List))([VisibilityKind](VisibilityKind.html) visibility,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded)`
If `visibility` is not null, return the `Memberships` of this `Namespace` with the given `visibility`, including `ownedMemberships` with the given `visibility` and `Memberships` imported with the given `visibility`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[namesOf](#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) element)`
Return the names of the given `element` as it is known in this `Namespace`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[qualificationOf](#qualificationOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Return a string with valid KerML syntax representing the qualification part of a given `qualifiedName`, that is, a qualified name with all the segment names of the given name except the last.
`[Membership](Membership.html)`
`[resolve](#resolve(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Resolve the given qualified name to the named `Membership` (if any), starting with this `Namespace` as the local scope.
`[Membership](Membership.html)`
`[resolveGlobal](#resolveGlobal(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Resolve the given qualified name to the named `Membership` (if any) in the effective global `Namespace` that is the outermost naming scope.
`[Membership](Membership.html)`
`[resolveLocal](#resolveLocal(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Resolve a simple `name` starting with this `Namespace` as the local scope, and continuing with containing outer scopes as necessary.
`[Membership](Membership.html)`
`[resolveVisible](#resolveVisible(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Resolve a simple name from the visible `Memberships` of this `Namespace`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[unqualifiedNameOf](#unqualifiedNameOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Return the simple name that is the last segment name of the given `qualifiedName`.
`[VisibilityKind](VisibilityKind.html)`
`[visibilityOf](#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership))([Membership](Membership.html) mem)`
Returns this visibility of `mem` relative to this `Namespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[visibleMemberships](#visibleMemberships(java.util.List,boolean,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded,
 boolean isRecursive,
 boolean includeAll)`
If `includeAll = true`, then return all the `Memberships` of this `Namespace`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [libraryNamespace](Element.html#libraryNamespace()), [path](Element.html#path()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
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
getMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> getMembership()
All `Memberships` in this `Namespace`, including (at least) the union of `ownedMemberships` and `importedMemberships`.
Returns:
the membership value
Model:
derived="true"
 transient="true"
 oppositeRoleName="membershipNamespace"
getOwnedImport
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Import](Import.html)> getOwnedImport()
The `ownedRelationships` of this `Namespace` that are `Imports`, for which the `Namespace` is the `importOwningNamespace`.
Returns:
the ownedImport value
Model:
derived="true"
 transient="true"
 opposite=[`Import.getImportOwningNamespace()`](Import.html#getImportOwningNamespace())
 subsets=[`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getMember
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getMember()
The set of all member `Elements` of this `Namespace`, which are the `memberElements` of all `memberships` of the `Namespace`.
Returns:
the member value
Model:
derived="true"
 transient="true"
 oppositeRoleName="namespace"
getOwnedMember
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getOwnedMember()
The owned `members` of this `Namespace`, which are the `ownedMemberElements` of the `ownedMemberships` of the `Namespace`.
Returns:
the ownedMember value
Model:
derived="true"
 transient="true"
 opposite=[`Element.getOwningNamespace()`](Element.html#getOwningNamespace())
 subsets=[`getMember()`](#getMember())
getOwnedMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> getOwnedMembership()
The `ownedRelationships` of this `Namespace` that are `Memberships`, for which the `Namespace` is the `membershipOwningNamespace`.
Returns:
the ownedMembership value
Model:
derived="true"
 transient="true"
 opposite=[`Membership.getMembershipOwningNamespace()`](Membership.html#getMembershipOwningNamespace())
 subsets=[`getMembership()`](#getMembership()), [`Element.getOwnedRelationship()`](Element.html#getOwnedRelationship())
getImportedMembership
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> getImportedMembership()
The `Memberships` in this `Namespace` that result from the `ownedImports` of this `Namespace`.
Returns:
the importedMembership value
Model:
derived="true"
 transient="true"
 oppositeRoleName="importingNamespace"
 subsets=[`getMembership()`](#getMembership())
namesOf
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> namesOf([Element](Element.html) element)
Return the names of the given `element` as it is known in this `Namespace`.
 
 let elementMemberships : Sequence(Membership) = 
 memberships->select(memberElement = element) in
 memberships.memberShortName->
 union(memberships.memberName)->
 asSet()
visibilityOf
[VisibilityKind](VisibilityKind.html) visibilityOf([Membership](Membership.html) mem)
Returns this visibility of `mem` relative to this `Namespace`. If `mem` is an `importedMembership`, this is the `visibility` of its Import. Otherwise it is the `visibility` of the `Membership` itself.
 
 if importedMembership->includes(mem) then
 ownedImport->
 select(importedMemberships(Set{})->includes(mem)).
 first().visibility
 else if memberships->includes(mem) then
 mem.visibility
 else
 VisibilityKind::private
 endif
visibleMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> visibleMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded,
 boolean isRecursive,
 boolean includeAll)
If `includeAll = true`, then return all the `Memberships` of this `Namespace`. Otherwise, return only the publicly visible `Memberships` of this `Namespace`, including `ownedMemberships` that have a `visibility` of `public` and `Memberships` imported with a `visibility` of `public`. If `isRecursive = true`, also recursively include all visible `Memberships` of any `public` owned `Namespaces`, or, if `IncludeAll = true`, all `Memberships` of all owned `Namespaces`. When computing imported `Memberships`, ignore this `Namespace` and any `Namespaces` in the given `excluded` set.
 
 let visibleMemberships : OrderedSet(Membership) = 
 if includeAll then membershipsOfVisibility(null, excluded)
 else membershipsOfVisibility(VisibilityKind::public, excluded)
 endif in
 if not isRecursive then visibleMemberships
 else visibleMemberships->union(ownedMember->
 selectAsKind(Namespace).
 select(includeAll or owningMembership.visibility = VisibilityKind::public)->
 visibleMemberships(excluded->including(self), true, includeAll))
 endif
importedMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> importedMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded)
Derive the imported `Memberships` of this `Namespace` as the `importedMembership` of all `ownedImports`, excluding those Imports whose `importOwningNamespace` is in the `excluded` set, and excluding `Memberships` that have distinguisibility collisions with each other or with any `ownedMembership`.
 
 ownedImport.importedMemberships(excluded->including(self))
membershipsOfVisibility
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> membershipsOfVisibility([VisibilityKind](VisibilityKind.html) visibility,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded)
If `visibility` is not null, return the `Memberships` of this `Namespace` with the given `visibility`, including `ownedMemberships` with the given `visibility` and `Memberships` imported with the given `visibility`. If `visibility` is null, return all `ownedMemberships` and imported `Memberships` regardless of visibility. When computing imported `Memberships`, ignore this `Namespace` and any `Namespaces` in the given `excluded` set.
 ownedMembership->
 select(mem | visibility = null or mem.visibility = visibility)->
 union(ownedImport->
 select(imp | visibility = null or imp.visibility = visibility).
 importedMemberships(excluded->including(self)))
resolve
[Membership](Membership.html) resolve([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
Resolve the given qualified name to the named `Membership` (if any), starting with this `Namespace` as the local scope. The qualified name string must conform to the concrete syntax of the KerML textual notation. According to the KerML name resolution rules every qualified name will resolve to either a single `Membership`, or to none.
 
 let qualification : String = qualificationOf(qualifiedName) in
 let name : String = unqualifiedNameOf(qualifiedName) in
 if qualification = null then resolveLocal(name)
 else if qualification = '$' then resolveGlobal(name)
 else 
 let namespaceMembership : Membership = resolve(qualification) in
 if namespaceMembership = null or 
 not namespaceMembership.memberElement.oclIsKindOf(Namespace) 
 then null
 else 
 namespaceMembership.memberElement.oclAsType(Namespace).
 resolveVisible(name) 
 endif
 endif endif
resolveGlobal
[Membership](Membership.html) resolveGlobal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
Resolve the given qualified name to the named `Membership` (if any) in the effective global `Namespace` that is the outermost naming scope. The qualified name string must conform to the concrete syntax of the KerML textual notation.
 
 No OCL
resolveLocal
[Membership](Membership.html) resolveLocal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Resolve a simple `name` starting with this `Namespace` as the local scope, and continuing with containing outer scopes as necessary. However, if this `Namespace` is a root `Namespace`, then the resolution is done directly in global scope.
 
 if owningNamespace = null then resolveGlobal(name)
 else
 let memberships : Membership = membership->
 select(memberShortName = name or memberName = name) in
 if memberships->notEmpty() then memberships->first()
 else owningNamspace.resolveLocal(name)
 endif
 endif
resolveVisible
[Membership](Membership.html) resolveVisible([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Resolve a simple name from the visible `Memberships` of this `Namespace`.
 
 let memberships : Sequence(Membership) =
 visibleMemberships(Set{}, false, false)->
 select(memberShortName = name or memberName = name) in
 if memberships->isEmpty() then null
 else memberships->first()
 endif
qualificationOf
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualificationOf([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
Return a string with valid KerML syntax representing the qualification part of a given `qualifiedName`, that is, a qualified name with all the segment names of the given name except the last. If the given `qualifiedName` has only one segment, then return null.
 No OCL
unqualifiedNameOf
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) unqualifiedNameOf([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
Return the simple name that is the last segment name of the given `qualifiedName`. If this segment name has the form of a KerML unrestricted name, then "unescape" it by removing the surrounding single quotes and replacing all escape sequences with the specified character.
 No OCL

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Namespace">Interface Namespace</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></code>, <code><a href="Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a></code>, <code><a href="AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></code>, <code><a href="../../../sysml/model/sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></code>, <code><a href="Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></code>, <code><a href="BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code>, <code><a href="../../../sysml/model/sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></code>, <code><a href="../../../sysml/model/sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code>, <code><a href="../../../sysml/model/sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code>, <code><a href="Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a></code>, <code><a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code>, <code><a href="CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></code>, <code><a href="../../../sysml/model/sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code>, <code><a href="../../../sysml/model/sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code>, <code><a href="ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></code>, <code><a href="../../../sysml/model/sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a></code>, <code><a href="DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a></code>, <code><a href="../../../sysml/model/sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></code>, <code><a href="../../../sysml/model/sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></code>, <code><a href="../../../sysml/model/sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></code>, <code><a href="Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code>, <code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code>, <code><a href="FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code>, <code><a href="Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code>, <code><a href="../../../sysml/model/sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code>, <code><a href="FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a></code>, <code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></code>, <code><a href="../../../sysml/model/sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></code>, <code><a href="Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></code>, <code><a href="../../../sysml/model/sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code>, <code><a href="IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></code>, <code><a href="InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code>, <code><a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></code>, <code><a href="InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></code>, <code><a href="../../../sysml/model/sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></code>, <code><a href="LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></code>, <code><a href="LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></code>, <code><a href="LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></code>, <code><a href="LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></code>, <code><a href="LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></code>, <code><a href="LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></code>, <code><a href="../../../sysml/model/sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></code>, <code><a href="Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></code>, <code><a href="MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code>, <code><a href="../../../sysml/model/sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a></code>, <code><a href="MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code>, <code><a href="../../../sysml/model/sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></code>, <code><a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code>, <code><a href="MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code>, <code><a href="NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></code>, <code><a href="OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code>, <code><a href="Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></code>, <code><a href="../../../sysml/model/sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a></code>, <code><a href="../../../sysml/model/sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></code>, <code><a href="PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></code>, <code><a href="../../../sysml/model/sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code>, <code><a href="../../../sysml/model/sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></code>, <code><a href="Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a></code>, <code><a href="../../../sysml/model/sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a></code>, <code><a href="../../../sysml/model/sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code>, <code><a href="../../../sysml/model/sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></code>, <code><a href="../../../sysml/model/sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code>, <code><a href="../../../sysml/model/sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code>, <code><a href="SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></code>, <code><a href="../../../sysml/model/sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a></code>, <code><a href="../../../sysml/model/sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></code>, <code><a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a></code>, <code><a href="Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code>, <code><a href="../../../sysml/model/sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></code>, <code><a href="../../../sysml/model/sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Namespace</span><span class="extends-implements">
extends <a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span></div>
<div class="block"><p>A <code>Namespace</code> is an <code>Element</code> that contains other <code>Elements</code>, known as its <code>members</code>, via <code>Membership</code> <code>Relationships</code> with those <code>Elements</code>. The <code>members</code> of a <code>Namespace</code> may be owned by the <code>Namespace</code>, aliased in the <code>Namespace</code>, or imported into the <code>Namespace</code> via <code>Import</code> <code>Relationships</code>.</p>
<p>A <code>Namespace</code> can provide names for its <code>members</code> via the <code>memberNames</code> and <code>memberShortNames</code> specified by the <code>Memberships</code> in the <code>Namespace</code>. If a <code>Membership</code> specifies a <code>memberName</code> and/or <code>memberShortName</code>, then those are names of the corresponding <code>memberElement</code> relative to the <code>Namespace</code>. For an <code>OwningMembership</code>, the <code>ownedMemberName</code> and <code>ownedMemberShortName</code> are given by the <code>Element</code> <code>name</code> and <code>shortName</code>. Note that the same <code>Element</code> may be the <code>memberElement</code> of multiple <code>Memberships</code> in a <code>Namespace</code> (though it may be owned at most once), each of which may define a separate alias for the <code>Element</code> relative to the <code>Namespace</code>.</p>
 
 membership-&gt;forAll(m1 | 
     membership-&gt;forAll(m2 | 
         m1 &lt;&gt; m2 implies m1.isDistinguishableFrom(m2)))
 member = membership.memberElement
 ownedMember = ownedMembership-&gt;selectByKind(OwningMembership).ownedMemberElement
 importedMembership = importedMemberships(Set{})
 ownedImport = ownedRelationship-&gt;selectByKind(Import)
 ownedMembership = ownedRelationship-&gt;selectByKind(Membership)</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportedMembership()">getImportedMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Memberships</code> in this <code>Namespace</code> that result from the <code>ownedImports</code> of this <code>Namespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMember()">getMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The set of all member <code>Elements</code> of this <code>Namespace</code>, which are the <code>memberElements</code> of all <code>memberships</code> of the <code>Namespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMembership()">getMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">All <code>Memberships</code> in this <code>Namespace</code>, including (at least) the union of <code>ownedMemberships</code> and <code>importedMemberships</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedImport()">getOwnedImport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Namespace</code> that are <code>Imports</code>, for which the <code>Namespace</code> is the <code>importOwningNamespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedMember()">getOwnedMember</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The owned <code>members</code> of this <code>Namespace</code>, which are the <cpde><code>ownedMemberElements</code> of the <code>ownedMemberships</code> of the <code>Namespace</code>.</cpde></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedMembership()">getOwnedMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Namespace</code> that are <code>Memberships</code>, for which the <code>Namespace</code> is the <code>membershipOwningNamespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importedMemberships(java.util.List)">importedMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Derive the imported <code>Memberships</code> of this <code>Namespace</code> as the <code>importedMembership</code> of all <code>ownedImports</code>, excluding those Imports whose <code>importOwningNamespace</code> is in the <code>excluded</code> set, and excluding <code>Memberships</code> that have distinguisibility collisions with each other or with any <code>ownedMembership</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">membershipsOfVisibility</a><wbr/>(<a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a> visibility,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If <code>visibility</code> is not null, return the <code>Memberships</code> of this <code>Namespace</code> with the given <code>visibility</code>, including <code>ownedMemberships</code> with the given <code>visibility</code> and <code>Memberships</code> imported with the given <code>visibility</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">namesOf</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the names of the given <code>element</code> as it is known in this <code>Namespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#qualificationOf(java.lang.String)">qualificationOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a string with valid KerML syntax representing the qualification part of a given <code>qualifiedName</code>, that is, a qualified name with all the segment names of the given name except the last.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#resolve(java.lang.String)">resolve</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Resolve the given qualified name to the named <code>Membership</code> (if any), starting with this <code>Namespace</code> as the local scope.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#resolveGlobal(java.lang.String)">resolveGlobal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Resolve the given qualified name to the named <code>Membership</code> (if any) in the effective global <code>Namespace</code> that is the outermost naming scope.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#resolveLocal(java.lang.String)">resolveLocal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Resolve a simple <code>name</code> starting with this <code>Namespace</code> as the local scope, and continuing with containing outer scopes as necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#resolveVisible(java.lang.String)">resolveVisible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Resolve a simple name from the visible <code>Memberships</code> of this <code>Namespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unqualifiedNameOf(java.lang.String)">unqualifiedNameOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the simple name that is the last segment name of the given <code>qualifiedName</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">visibilityOf</a><wbr/>(<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> mem)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns this visibility of <code>mem</code> relative to this <code>Namespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded,
 boolean isRecursive,
 boolean includeAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If <code>includeAll = true</code>, then return all the <code>Memberships</code> of this <code>Namespace</code>.</div>
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
<code><a href="Element.html#effectiveName()">effectiveName</a>, <a href="Element.html#effectiveShortName()">effectiveShortName</a>, <a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#libraryNamespace()">libraryNamespace</a>, <a href="Element.html#path()">path</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
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
<section class="detail" id="getMembership()">
<h3>getMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">getMembership</span>()</div>
<div class="block"><p>All <code>Memberships</code> in this <code>Namespace</code>, including (at least) the union of <code>ownedMemberships</code> and <code>importedMemberships</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the membership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="membershipNamespace"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedImport()">
<h3>getOwnedImport</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a>&gt;</span> <span class="element-name">getOwnedImport</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Namespace</code> that are <code>Imports</code>, for which the <code>Namespace</code> is the <code>importOwningNamespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedImport value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Import.html#getImportOwningNamespace()"><code>Import.getImportOwningNamespace()</code></a>
        subsets=<a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMember()">
<h3>getMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getMember</span>()</div>
<div class="block"><p>The set of all member <code>Elements</code> of this <code>Namespace</code>, which are the <code>memberElements</code> of all <code>memberships</code> of the <code>Namespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the member value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="namespace"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMember()">
<h3>getOwnedMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getOwnedMember</span>()</div>
<div class="block"><p>The owned <code>members</code> of this <code>Namespace</code>, which are the <cpde><code>ownedMemberElements</code> of the <code>ownedMemberships</code> of the <code>Namespace</code>.</cpde></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedMember value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Element.html#getOwningNamespace()"><code>Element.getOwningNamespace()</code></a>
        subsets=<a href="#getMember()"><code>getMember()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMembership()">
<h3>getOwnedMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">getOwnedMembership</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Namespace</code> that are <code>Memberships</code>, for which the <code>Namespace</code> is the <code>membershipOwningNamespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Membership.html#getMembershipOwningNamespace()"><code>Membership.getMembershipOwningNamespace()</code></a>
        subsets=<a href="#getMembership()"><code>getMembership()</code></a>, <a href="Element.html#getOwnedRelationship()"><code>Element.getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImportedMembership()">
<h3>getImportedMembership</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">getImportedMembership</span>()</div>
<div class="block"><p>The <code>Memberships</code> in this <code>Namespace</code> that result from the <code>ownedImports</code> of this <code>Namespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the importedMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="importingNamespace"
        subsets=<a href="#getMembership()"><code>getMembership()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>namesOf</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">namesOf</span><wbr/><span class="parameters">(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block"><p>Return the names of the given <code>element</code> as it is known in this <code>Namespace</code>.</p>
 
 let elementMemberships : Sequence(Membership) = 
     memberships-&gt;select(memberElement = element) in
 memberships.memberShortName-&gt;
     union(memberships.memberName)-&gt;
     asSet()</div>
</section>
</li>
<li>
<section class="detail" id="visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">
<h3>visibilityOf</h3>
<div class="member-signature"><span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">visibilityOf</span><wbr/><span class="parameters">(<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> mem)</span></div>
<div class="block"><p>Returns this visibility of <code>mem</code> relative to this <code>Namespace</code>. If <code>mem</code> is an <code>importedMembership</code>, this is the <code>visibility</code> of its Import. Otherwise it is the <code>visibility</code> of the <code>Membership</code> itself.</p>
 
 if importedMembership-&gt;includes(mem) then
     ownedImport-&gt;
         select(importedMemberships(Set{})-&gt;includes(mem)).
         first().visibility
 else if memberships-&gt;includes(mem) then
     mem.visibility
 else
     VisibilityKind::private
 endif</div>
</section>
</li>
<li>
<section class="detail" id="visibleMemberships(java.util.List,boolean,boolean)">
<h3>visibleMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">visibleMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded,
 boolean isRecursive,
 boolean includeAll)</span></div>
<div class="block"><p>If <code>includeAll = true</code>, then return all the <code>Memberships</code> of this <code>Namespace</code>. Otherwise, return only the publicly visible <code>Memberships</code> of this <code>Namespace</code>, including <code>ownedMemberships</code> that have a <code>visibility</code> of <code>public</code> and <code>Memberships</code> imported with a <code>visibility</code> of <code>public</code>. If <code>isRecursive = true</code>, also recursively include all visible <code>Memberships</code> of any <code>public</code> owned <code>Namespaces</code>, or, if <code>IncludeAll = true</code>, all <code>Memberships</code> of all owned <code>Namespaces</code>. When computing imported <code>Memberships</code>, ignore this <code>Namespace</code> and any <code>Namespaces</code> in the given <code>excluded</code> set.</p>
 
 let visibleMemberships : OrderedSet(Membership) = 
     if includeAll then membershipsOfVisibility(null, excluded)
     else membershipsOfVisibility(VisibilityKind::public, excluded)
     endif in
 if not isRecursive then visibleMemberships
 else visibleMemberships-&gt;union(ownedMember-&gt;
     selectAsKind(Namespace).
     select(includeAll or owningMembership.visibility = VisibilityKind::public)-&gt;
     visibleMemberships(excluded-&gt;including(self), true, includeAll))
 endif</div>
</section>
</li>
<li>
<section class="detail" id="importedMemberships(java.util.List)">
<h3>importedMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">importedMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded)</span></div>
<div class="block"><p>Derive the imported <code>Memberships</code> of this <code>Namespace</code> as the <code>importedMembership</code> of all <code>ownedImports</code>, excluding those Imports whose <code>importOwningNamespace</code> is in the <code>excluded</code> set, and excluding <code>Memberships</code> that have distinguisibility collisions with each other or with any <code>ownedMembership</code>.</p>
 
 ownedImport.importedMemberships(excluded-&gt;including(self))</div>
</section>
</li>
<li>
<section class="detail" id="membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">
<h3>membershipsOfVisibility</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">membershipsOfVisibility</span><wbr/><span class="parameters">(<a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a> visibility,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded)</span></div>
<div class="block"><p>If <code>visibility</code> is not null, return the <code>Memberships</code> of this <code>Namespace</code> with the given <code>visibility</code>, including <code>ownedMemberships</code> with the given <code>visibility</code> and <code>Memberships</code> imported with the given <code>visibility</code>. If <code>visibility</code> is null, return all <code>ownedMemberships</code> and imported <code>Memberships</code> regardless of visibility. When computing imported <code>Memberships</code>, ignore this <code>Namespace</code> and any <code>Namespaces</code> in the given <code>excluded</code> set.</p>
 ownedMembership-&gt;
     select(mem | visibility = null or mem.visibility = visibility)-&gt;
     union(ownedImport-&gt;
         select(imp | visibility = null or imp.visibility = visibility).
         importedMemberships(excluded-&gt;including(self)))</div>
</section>
</li>
<li>
<section class="detail" id="resolve(java.lang.String)">
<h3>resolve</h3>
<div class="member-signature"><span class="return-type"><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">resolve</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block"><p>Resolve the given qualified name to the named <code>Membership</code> (if any), starting with this <code>Namespace</code> as the local scope. The qualified name string must conform to the concrete syntax of the KerML textual notation. According to the KerML name resolution rules every qualified name will resolve to either a single <code>Membership</code>, or to none.</p>
 
 let qualification : String = qualificationOf(qualifiedName) in
 let name : String = unqualifiedNameOf(qualifiedName) in
 if qualification = null then resolveLocal(name)
 else if qualification = '$' then  resolveGlobal(name)
 else 
     let namespaceMembership : Membership = resolve(qualification) in
     if namespaceMembership = null or 
        not namespaceMembership.memberElement.oclIsKindOf(Namespace) 
     then null
     else 
         namespaceMembership.memberElement.oclAsType(Namespace).
         resolveVisible(name) 
     endif
 endif endif</div>
</section>
</li>
<li>
<section class="detail" id="resolveGlobal(java.lang.String)">
<h3>resolveGlobal</h3>
<div class="member-signature"><span class="return-type"><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">resolveGlobal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block"><p>Resolve the given qualified name to the named <code>Membership</code> (if any) in the effective global <code>Namespace</code> that is the outermost naming scope. The qualified name string must conform to the concrete syntax of the KerML textual notation.</p>
 
 No OCL</div>
</section>
</li>
<li>
<section class="detail" id="resolveLocal(java.lang.String)">
<h3>resolveLocal</h3>
<div class="member-signature"><span class="return-type"><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">resolveLocal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Resolve a simple <code>name</code> starting with this <code>Namespace</code> as the local scope, and continuing with containing outer scopes as necessary. However, if this <code>Namespace</code> is a root <code>Namespace</code>, then the resolution is done directly in global scope.</p>
 
 if owningNamespace = null then resolveGlobal(name)
 else
     let memberships : Membership = membership-&gt;
         select(memberShortName = name or memberName = name) in
     if memberships-&gt;notEmpty() then memberships-&gt;first()
     else owningNamspace.resolveLocal(name)
     endif
 endif</div>
</section>
</li>
<li>
<section class="detail" id="resolveVisible(java.lang.String)">
<h3>resolveVisible</h3>
<div class="member-signature"><span class="return-type"><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">resolveVisible</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Resolve a simple name from the visible <code>Memberships</code> of this <code>Namespace</code>.</p>
 
 let memberships : Sequence(Membership) =
     visibleMemberships(Set{}, false, false)-&gt;
     select(memberShortName = name or memberName = name) in
 if memberships-&gt;isEmpty() then null
 else memberships-&gt;first()
 endif</div>
</section>
</li>
<li>
<section class="detail" id="qualificationOf(java.lang.String)">
<h3>qualificationOf</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">qualificationOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block"><p>Return a string with valid KerML syntax representing the qualification part of a given <code>qualifiedName</code>, that is, a qualified name with all the segment names of the given name except the last. If the given <code>qualifiedName</code> has only one segment, then return null.</p>
 No OCL</div>
</section>
</li>
<li>
<section class="detail" id="unqualifiedNameOf(java.lang.String)">
<h3>unqualifiedNameOf</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">unqualifiedNameOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block"><p>Return the simple name that is the last segment name of the given <code>qualifiedName</code>. If this segment name has the form of a KerML unrestricted name, then "unescape" it by removing the surrounding single quotes and replacing all escape sequences with the specified character.</p>
 No OCL</div>
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
