# JAVA OPENAPI: Element (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Element.html`
- source_sha256: `31ad3e35eb2f1c3aefb6557b2a32abd02e95c3b3b236505dd15b181594fdc34f`
- captured_utc: `2026-07-14T16:44:49.118856+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Element

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`

All Known Subinterfaces:
`[AcceptActionUsage](../../../sysml/model/sysml/AcceptActionUsage.html)`, `[ActionDefinition](../../../sysml/model/sysml/ActionDefinition.html)`, `[ActionUsage](../../../sysml/model/sysml/ActionUsage.html)`, `[ActorMembership](../../../sysml/model/sysml/ActorMembership.html)`, `[AllocationDefinition](../../../sysml/model/sysml/AllocationDefinition.html)`, `[AllocationUsage](../../../sysml/model/sysml/AllocationUsage.html)`, `[AnalysisCaseDefinition](../../../sysml/model/sysml/AnalysisCaseDefinition.html)`, `[AnalysisCaseUsage](../../../sysml/model/sysml/AnalysisCaseUsage.html)`, `[AnnotatingElement](AnnotatingElement.html)`, `[Annotation](Annotation.html)`, `[AssertConstraintUsage](../../../sysml/model/sysml/AssertConstraintUsage.html)`, `[AssignmentActionUsage](../../../sysml/model/sysml/AssignmentActionUsage.html)`, `[Association](Association.html)`, `[AssociationStructure](AssociationStructure.html)`, `[AttributeDefinition](../../../sysml/model/sysml/AttributeDefinition.html)`, `[AttributeUsage](../../../sysml/model/sysml/AttributeUsage.html)`, `[Behavior](Behavior.html)`, `[BindingConnector](BindingConnector.html)`, `[BindingConnectorAsUsage](../../../sysml/model/sysml/BindingConnectorAsUsage.html)`, `[BooleanExpression](BooleanExpression.html)`, `[CalculationDefinition](../../../sysml/model/sysml/CalculationDefinition.html)`, `[CalculationUsage](../../../sysml/model/sysml/CalculationUsage.html)`, `[CaseDefinition](../../../sysml/model/sysml/CaseDefinition.html)`, `[CaseUsage](../../../sysml/model/sysml/CaseUsage.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[CollectExpression](CollectExpression.html)`, `[Comment](Comment.html)`, `[ConcernDefinition](../../../sysml/model/sysml/ConcernDefinition.html)`, `[ConcernUsage](../../../sysml/model/sysml/ConcernUsage.html)`, `[ConjugatedPortDefinition](../../../sysml/model/sysml/ConjugatedPortDefinition.html)`, `[ConjugatedPortTyping](../../../sysml/model/sysml/ConjugatedPortTyping.html)`, `[Conjugation](Conjugation.html)`, `[ConnectionDefinition](../../../sysml/model/sysml/ConnectionDefinition.html)`, `[ConnectionUsage](../../../sysml/model/sysml/ConnectionUsage.html)`, `[Connector](Connector.html)`, `[ConnectorAsUsage](../../../sysml/model/sysml/ConnectorAsUsage.html)`, `[ConstraintDefinition](../../../sysml/model/sysml/ConstraintDefinition.html)`, `[ConstraintUsage](../../../sysml/model/sysml/ConstraintUsage.html)`, `[ConstructorExpression](ConstructorExpression.html)`, `[ControlNode](../../../sysml/model/sysml/ControlNode.html)`, `[CrossSubsetting](CrossSubsetting.html)`, `[DataType](DataType.html)`, `[DecisionNode](../../../sysml/model/sysml/DecisionNode.html)`, `[Definition](../../../sysml/model/sysml/Definition.html)`, `[Dependency](Dependency.html)`, `[Differencing](Differencing.html)`, `[Disjoining](Disjoining.html)`, `[Documentation](Documentation.html)`, `[ElementFilterMembership](ElementFilterMembership.html)`, `[EndFeatureMembership](EndFeatureMembership.html)`, `[EnumerationDefinition](../../../sysml/model/sysml/EnumerationDefinition.html)`, `[EnumerationUsage](../../../sysml/model/sysml/EnumerationUsage.html)`, `[EventOccurrenceUsage](../../../sysml/model/sysml/EventOccurrenceUsage.html)`, `[ExhibitStateUsage](../../../sysml/model/sysml/ExhibitStateUsage.html)`, `[Expose](../../../sysml/model/sysml/Expose.html)`, `[Expression](Expression.html)`, `[Feature](Feature.html)`, `[FeatureChainExpression](FeatureChainExpression.html)`, `[FeatureChaining](FeatureChaining.html)`, `[FeatureInverting](FeatureInverting.html)`, `[FeatureMembership](FeatureMembership.html)`, `[FeatureReferenceExpression](FeatureReferenceExpression.html)`, `[FeatureTyping](FeatureTyping.html)`, `[FeatureValue](FeatureValue.html)`, `[Flow](Flow.html)`, `[FlowDefinition](../../../sysml/model/sysml/FlowDefinition.html)`, `[FlowEnd](FlowEnd.html)`, `[FlowUsage](../../../sysml/model/sysml/FlowUsage.html)`, `[ForkNode](../../../sysml/model/sysml/ForkNode.html)`, `[ForLoopActionUsage](../../../sysml/model/sysml/ForLoopActionUsage.html)`, `[FramedConcernMembership](../../../sysml/model/sysml/FramedConcernMembership.html)`, `[Function](Function.html)`, `[IfActionUsage](../../../sysml/model/sysml/IfActionUsage.html)`, `[Import](Import.html)`, `[IncludeUseCaseUsage](../../../sysml/model/sysml/IncludeUseCaseUsage.html)`, `[IndexExpression](IndexExpression.html)`, `[InstantiationExpression](InstantiationExpression.html)`, `[Interaction](Interaction.html)`, `[InterfaceDefinition](../../../sysml/model/sysml/InterfaceDefinition.html)`, `[InterfaceUsage](../../../sysml/model/sysml/InterfaceUsage.html)`, `[Intersecting](Intersecting.html)`, `[Invariant](Invariant.html)`, `[InvocationExpression](InvocationExpression.html)`, `[ItemDefinition](../../../sysml/model/sysml/ItemDefinition.html)`, `[ItemUsage](../../../sysml/model/sysml/ItemUsage.html)`, `[JoinNode](../../../sysml/model/sysml/JoinNode.html)`, `[LibraryPackage](LibraryPackage.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralExpression](LiteralExpression.html)`, `[LiteralInfinity](LiteralInfinity.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralRational](LiteralRational.html)`, `[LiteralString](LiteralString.html)`, `[LoopActionUsage](../../../sysml/model/sysml/LoopActionUsage.html)`, `[Membership](Membership.html)`, `[MembershipExpose](../../../sysml/model/sysml/MembershipExpose.html)`, `[MembershipImport](MembershipImport.html)`, `[MergeNode](../../../sysml/model/sysml/MergeNode.html)`, `[Metaclass](Metaclass.html)`, `[MetadataAccessExpression](MetadataAccessExpression.html)`, `[MetadataDefinition](../../../sysml/model/sysml/MetadataDefinition.html)`, `[MetadataFeature](MetadataFeature.html)`, `[MetadataUsage](../../../sysml/model/sysml/MetadataUsage.html)`, `[Multiplicity](Multiplicity.html)`, `[MultiplicityRange](MultiplicityRange.html)`, `[Namespace](Namespace.html)`, `[NamespaceExpose](../../../sysml/model/sysml/NamespaceExpose.html)`, `[NamespaceImport](NamespaceImport.html)`, `[NullExpression](NullExpression.html)`, `[ObjectiveMembership](../../../sysml/model/sysml/ObjectiveMembership.html)`, `[OccurrenceDefinition](../../../sysml/model/sysml/OccurrenceDefinition.html)`, `[OccurrenceUsage](../../../sysml/model/sysml/OccurrenceUsage.html)`, `[OperatorExpression](OperatorExpression.html)`, `[OwningMembership](OwningMembership.html)`, `[Package](Package.html)`, `[ParameterMembership](ParameterMembership.html)`, `[PartDefinition](../../../sysml/model/sysml/PartDefinition.html)`, `[PartUsage](../../../sysml/model/sysml/PartUsage.html)`, `[PayloadFeature](PayloadFeature.html)`, `[PerformActionUsage](../../../sysml/model/sysml/PerformActionUsage.html)`, `[PortConjugation](../../../sysml/model/sysml/PortConjugation.html)`, `[PortDefinition](../../../sysml/model/sysml/PortDefinition.html)`, `[PortUsage](../../../sysml/model/sysml/PortUsage.html)`, `[Predicate](Predicate.html)`, `[Redefinition](Redefinition.html)`, `[ReferenceSubsetting](ReferenceSubsetting.html)`, `[ReferenceUsage](../../../sysml/model/sysml/ReferenceUsage.html)`, `[Relationship](Relationship.html)`, `[RenderingDefinition](../../../sysml/model/sysml/RenderingDefinition.html)`, `[RenderingUsage](../../../sysml/model/sysml/RenderingUsage.html)`, `[RequirementConstraintMembership](../../../sysml/model/sysml/RequirementConstraintMembership.html)`, `[RequirementDefinition](../../../sysml/model/sysml/RequirementDefinition.html)`, `[RequirementUsage](../../../sysml/model/sysml/RequirementUsage.html)`, `[RequirementVerificationMembership](../../../sysml/model/sysml/RequirementVerificationMembership.html)`, `[ResultExpressionMembership](ResultExpressionMembership.html)`, `[ReturnParameterMembership](ReturnParameterMembership.html)`, `[SatisfyRequirementUsage](../../../sysml/model/sysml/SatisfyRequirementUsage.html)`, `[SelectExpression](SelectExpression.html)`, `[SendActionUsage](../../../sysml/model/sysml/SendActionUsage.html)`, `[Specialization](Specialization.html)`, `[StakeholderMembership](../../../sysml/model/sysml/StakeholderMembership.html)`, `[StateDefinition](../../../sysml/model/sysml/StateDefinition.html)`, `[StateSubactionMembership](../../../sysml/model/sysml/StateSubactionMembership.html)`, `[StateUsage](../../../sysml/model/sysml/StateUsage.html)`, `[Step](Step.html)`, `[Structure](Structure.html)`, `[Subclassification](Subclassification.html)`, `[SubjectMembership](../../../sysml/model/sysml/SubjectMembership.html)`, `[Subsetting](Subsetting.html)`, `[Succession](Succession.html)`, `[SuccessionAsUsage](../../../sysml/model/sysml/SuccessionAsUsage.html)`, `[SuccessionFlow](SuccessionFlow.html)`, `[SuccessionFlowUsage](../../../sysml/model/sysml/SuccessionFlowUsage.html)`, `[TerminateActionUsage](../../../sysml/model/sysml/TerminateActionUsage.html)`, `[TextualRepresentation](TextualRepresentation.html)`, `[TransitionFeatureMembership](../../../sysml/model/sysml/TransitionFeatureMembership.html)`, `[TransitionUsage](../../../sysml/model/sysml/TransitionUsage.html)`, `[TriggerInvocationExpression](../../../sysml/model/sysml/TriggerInvocationExpression.html)`, `[Type](Type.html)`, `[TypeFeaturing](TypeFeaturing.html)`, `[Unioning](Unioning.html)`, `[Usage](../../../sysml/model/sysml/Usage.html)`, `[UseCaseDefinition](../../../sysml/model/sysml/UseCaseDefinition.html)`, `[UseCaseUsage](../../../sysml/model/sysml/UseCaseUsage.html)`, `[VariantMembership](../../../sysml/model/sysml/VariantMembership.html)`, `[VerificationCaseDefinition](../../../sysml/model/sysml/VerificationCaseDefinition.html)`, `[VerificationCaseUsage](../../../sysml/model/sysml/VerificationCaseUsage.html)`, `[ViewDefinition](../../../sysml/model/sysml/ViewDefinition.html)`, `[ViewpointDefinition](../../../sysml/model/sysml/ViewpointDefinition.html)`, `[ViewpointUsage](../../../sysml/model/sysml/ViewpointUsage.html)`, `[ViewRenderingMembership](../../../sysml/model/sysml/ViewRenderingMembership.html)`, `[ViewUsage](../../../sysml/model/sysml/ViewUsage.html)`, `[WhileLoopActionUsage](../../../sysml/model/sysml/WhileLoopActionUsage.html)`

@OpenApiAllpublic interfaceElementextends [ModelElement](../../../foundation/model/ModelElement.html), com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject

An `Element` is a constituent of a model that is uniquely identified relative to all other `Elements`. It can have `Relationships` with other `Elements`. Some of these `Relationships` might imply ownership of other `Elements`, which means that if an `Element` is deleted from a model, then so are all the `Elements` that it owns.
 
 ownedElement = ownedRelationship.ownedRelatedElement
 owner = owningRelationship.owningRelatedElement
 qualifiedName =
 if owningNamespace = null then null
 else if name <> null and 
 owningNamespace.ownedMember->
 select(m | m.name = name).indexOf(self) <> 1 then null
 else if owningNamespace.owner = null then escapedName()
 else if owningNamespace.qualifiedName = null or 
 escapedName() = null then null
 else owningNamespace.qualifiedName + '::' + escapedName()
 endif endif endif endif
 documentation = ownedElement->selectByKind(Documentation)
 ownedAnnotation = ownedRelationship->
 selectByKind(Annotation)->
 select(a | a.annotatedElement = self)
 name = effectiveName()
 ownedRelationship->exists(isImplied) implies isImpliedIncluded
 isLibraryElement = libraryNamespace() <> null
 
 shortName = effectiveShortName()
 owningNamespace =
 if owningMembership = null then null
 else owningMembership.membershipOwningNamespace
 endif
 textualRepresentation = ownedElement->selectByKind(TextualRepresentation)

Model:
abstract=true

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[effectiveName](#effectiveName())()`
Return an effective `name` for this `Element`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[effectiveShortName](#effectiveShortName())()`
Return an effective `shortName` for this `Element`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[escapedName](#escapedName())()`
Return `name`, if that is not null, otherwise the `shortName`, if that is not null, otherwise null.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getAliasIds](#getAliasIds())()`
Various alternative identifiers for this Element.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDeclaredName](#getDeclaredName())()`
The declared name of this `Element`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDeclaredShortName](#getDeclaredShortName())()`
An optional alternative name for the `Element` that is intended to be shorter or in some way more succinct than its primary `name`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Documentation](Documentation.html)>`
`[getDocumentation](#getDocumentation())()`
The Documentation owned by this Element.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getElementId](#getElementId())()`
The globally unique identifier for this Element.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
The name to be used for this `Element` during name resolution within its `owningNamespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getOwnedAnnotation](#getOwnedAnnotation())()`
The `ownedRelationships` of this `Element` that are `Annotations`, for which this `Element` is the `annotatedElement`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getOwnedElement](#getOwnedElement())()`
The Elements owned by this Element, derived as the ownedRelatedElements of the ownedRelationships of this Element.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Relationship](Relationship.html)>`
`[getOwnedRelationship](#getOwnedRelationship())()`
The Relationships for which this Element is the owningRelatedElement.
`[Element](Element.html)`
`[getOwner](#getOwner())()`
The owner of this Element, derived as the `owningRelatedElement` of the `owningRelationship` of this Element, if any.
`[OwningMembership](OwningMembership.html)`
`[getOwningMembership](#getOwningMembership())()`
The `owningRelationship` of this `Element`, if that `Relationship` is a `Membership`.
`[Namespace](Namespace.html)`
`[getOwningNamespace](#getOwningNamespace())()`
The `Namespace` that owns this `Element`, which is the `membershipOwningNamespace` of the `owningMembership` of this `Element`, if any.
`[Relationship](Relationship.html)`
`[getOwningRelationship](#getOwningRelationship())()`
The Relationship for which this Element is an ownedRelatedElement, if any.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQualifiedName](#getQualifiedName())()`
The full ownership-qualified name of this `Element`, represented in a form that is valid according to the KerML textual concrete syntax for qualified names (including use of unrestricted name notation and escaped characters, as necessary).
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getShortName](#getShortName())()`
The short name to be used for this `Element` during name resolution within its `owningNamespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TextualRepresentation](TextualRepresentation.html)>`
`[getTextualRepresentation](#getTextualRepresentation())()`
The `TextualRepresentations` that annotate this `Element`.
`boolean`
`[isImpliedIncluded](#isImpliedIncluded())()`
Whether all necessary implied Relationships have been included in the `ownedRelationships` of this Element.
`boolean`
`[isLibraryElement](#isLibraryElement())()`
Whether this Element is contained in the ownership tree of a library model.
`[Namespace](Namespace.html)`
`[libraryNamespace](#libraryNamespace())()`
By default, return the library Namespace of the `owningRelationship` of this Element, if it has one.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[path](#path())()`
Return a unique description of the location of this `Element` in the containment structure rooted in a root `Namespace`.
`void`
`[setDeclaredName](#setDeclaredName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
The declared name of this `Element`.
`void`
`[setDeclaredShortName](#setDeclaredShortName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
An optional alternative name for the `Element` that is intended to be shorter or in some way more succinct than its primary `name`.
`void`
`[setElementId](#setElementId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
The globally unique identifier for this Element.
`void`
`[setIsImpliedIncluded](#setIsImpliedIncluded(boolean))(boolean value)`
Whether all necessary implied Relationships have been included in the `ownedRelationships` of this Element.
`void`
`[setOwner](#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) value)`
The owner of this Element, derived as the `owningRelatedElement` of the `owningRelationship` of this Element, if any.
`void`
`[setOwningMembership](#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership))([OwningMembership](OwningMembership.html) value)`
The `owningRelationship` of this `Element`, if that `Relationship` is a `Membership`.
`void`
`[setOwningRelationship](#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))([Relationship](Relationship.html) value)`
The Relationship for which this Element is an ownedRelatedElement, if any.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
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
getOwningMembership
@CheckForNull[OwningMembership](OwningMembership.html) getOwningMembership()
The `owningRelationship` of this `Element`, if that `Relationship` is a `Membership`.
Returns:
the owningMembership value
Model:
derived="true"
 transient="true"
 opposite=[`OwningMembership.getOwnedMemberElement()`](OwningMembership.html#getOwnedMemberElement())
 subsets=[`getOwningRelationship()`](#getOwningRelationship())
setOwningMembership
void setOwningMembership(@CheckForNull
 [OwningMembership](OwningMembership.html) value)
The `owningRelationship` of this `Element`, if that `Relationship` is a `Membership`.
Parameters:
`value` - the owningMembership value
Model:
derived="true"
 transient="true"
 opposite=[`OwningMembership.getOwnedMemberElement()`](OwningMembership.html#getOwnedMemberElement())
 subsets=[`getOwningRelationship()`](#getOwningRelationship())
getOwningRelationship
@CheckForNull[Relationship](Relationship.html) getOwningRelationship()
The Relationship for which this Element is an ownedRelatedElement, if any.
Returns:
the owningRelationship value
Model:
derived="false"
 transient="false"
 container="true"
 opposite=[`Relationship.getOwnedRelatedElement()`](Relationship.html#getOwnedRelatedElement())
setOwningRelationship
void setOwningRelationship(@CheckForNull
 [Relationship](Relationship.html) value)
The Relationship for which this Element is an ownedRelatedElement, if any.
Parameters:
`value` - the owningRelationship value
Model:
derived="false"
 transient="false"
 container="true"
 opposite=[`Relationship.getOwnedRelatedElement()`](Relationship.html#getOwnedRelatedElement())
getOwningNamespace
@CheckForNull[Namespace](Namespace.html) getOwningNamespace()
The `Namespace` that owns this `Element`, which is the `membershipOwningNamespace` of the `owningMembership` of this `Element`, if any.
Returns:
the owningNamespace value
Model:
derived="true"
 transient="true"
 opposite=[`Namespace.getOwnedMember()`](Namespace.html#getOwnedMember())
getElementId
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getElementId()
The globally unique identifier for this Element. This is intended to be set by tooling, and it must not change during the lifetime of the Element.
Returns:
the elementId value
Model:
derived="false"
 transient="false"
setElementId
void setElementId(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
The globally unique identifier for this Element. This is intended to be set by tooling, and it must not change during the lifetime of the Element.
Parameters:
`value` - the elementId value
Model:
derived="false"
 transient="false"
getOwnedRelationship
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Relationship](Relationship.html)> getOwnedRelationship()
The Relationships for which this Element is the owningRelatedElement.
Returns:
the ownedRelationship value
Model:
derived="false"
 transient="false"
 containment="true"
 opposite=[`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
getOwner
@CheckForNull[Element](Element.html) getOwner()
The owner of this Element, derived as the `owningRelatedElement` of the `owningRelationship` of this Element, if any.
Returns:
the owner value
Model:
derived="true"
 transient="true"
 opposite=[`getOwnedElement()`](#getOwnedElement())
setOwner
void setOwner(@CheckForNull
 [Element](Element.html) value)
The owner of this Element, derived as the `owningRelatedElement` of the `owningRelationship` of this Element, if any.
Parameters:
`value` - the owner value
Model:
derived="true"
 transient="true"
 opposite=[`getOwnedElement()`](#getOwnedElement())
getOwnedElement
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getOwnedElement()
The Elements owned by this Element, derived as the ownedRelatedElements of the ownedRelationships of this Element.
Returns:
the ownedElement value
Model:
derived="true"
 transient="true"
 opposite=[`getOwner()`](#getOwner())
getDocumentation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Documentation](Documentation.html)> getDocumentation()
The Documentation owned by this Element.
Returns:
the documentation value
Model:
derived="true"
 transient="true"
 opposite=[`Documentation.getDocumentedElement()`](Documentation.html#getDocumentedElement())
 subsets=[`getOwnedElement()`](#getOwnedElement())
getOwnedAnnotation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getOwnedAnnotation()
The `ownedRelationships` of this `Element` that are `Annotations`, for which this `Element` is the `annotatedElement`.
Returns:
the ownedAnnotation value
Model:
derived="true"
 transient="true"
 opposite=[`Annotation.getOwningAnnotatedElement()`](Annotation.html#getOwningAnnotatedElement())
 subsets=[`getOwnedRelationship()`](#getOwnedRelationship())
getTextualRepresentation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[TextualRepresentation](TextualRepresentation.html)> getTextualRepresentation()
The `TextualRepresentations` that annotate this `Element`.
Returns:
the textualRepresentation value
Model:
derived="true"
 transient="true"
 opposite=[`TextualRepresentation.getRepresentedElement()`](TextualRepresentation.html#getRepresentedElement())
 subsets=[`getOwnedElement()`](#getOwnedElement())
getAliasIds
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getAliasIds()
Various alternative identifiers for this Element. Generally, these will be set by tools.
Returns:
the aliasIds value
Model:
derived="false"
 transient="false"
getDeclaredShortName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDeclaredShortName()
An optional alternative name for the `Element` that is intended to be shorter or in some way more succinct than its primary `name`. It may act as a modeler-specified identifier for the `Element`, though it is then the responsibility of the modeler to maintain the uniqueness of this identifier within a model or relative to some other context.
Returns:
the declaredShortName value
Model:
derived="false"
 transient="false"
setDeclaredShortName
void setDeclaredShortName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
An optional alternative name for the `Element` that is intended to be shorter or in some way more succinct than its primary `name`. It may act as a modeler-specified identifier for the `Element`, though it is then the responsibility of the modeler to maintain the uniqueness of this identifier within a model or relative to some other context.
Parameters:
`value` - the declaredShortName value
Model:
derived="false"
 transient="false"
getDeclaredName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDeclaredName()
The declared name of this `Element`.
Returns:
the declaredName value
Model:
derived="false"
 transient="false"
setDeclaredName
void setDeclaredName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
The declared name of this `Element`.
Parameters:
`value` - the declaredName value
Model:
derived="false"
 transient="false"
getShortName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getShortName()
The short name to be used for this `Element` during name resolution within its `owningNamespace`. This is derived using the `effectiveShortName()` operation. By default, it is the same as the `declaredShortName`, but this is overridden for certain kinds of `Elements` to compute a `shortName` even when the `declaredName` is null.
Returns:
the shortName value
Model:
derived="true"
 transient="true"
getName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
The name to be used for this `Element` during name resolution within its `owningNamespace`. This is derived using the `effectiveName()` operation. By default, it is the same as the `declaredName`, but this is overridden for certain kinds of `Elements` to compute a `name` even when the `declaredName` is null.
Returns:
the name value
Model:
derived="true"
 transient="true"
getQualifiedName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQualifiedName()
The full ownership-qualified name of this `Element`, represented in a form that is valid according to the KerML textual concrete syntax for qualified names (including use of unrestricted name notation and escaped characters, as necessary). The `qualifiedName` is null if this `Element` has no `owningNamespace` or if there is not a complete ownership chain of named `Namespaces` from a root `Namespace` to this `Element`. If the `owningNamespace` has other `Elements` with the same name as this one, then the `qualifiedName` is null for all such `Elements` other than the first.
Returns:
the qualifiedName value
Model:
derived="true"
 transient="true"
isImpliedIncluded
boolean isImpliedIncluded()
Whether all necessary implied Relationships have been included in the `ownedRelationships` of this Element. This property may be true, even if there are not actually any `ownedRelationships` with `isImplied = true`, meaning that no such Relationships are actually implied for this Element. However, if it is false, then `ownedRelationships` may *not* contain any implied Relationships. That is, either *all* required implied Relationships must be included, or none of them.
Returns:
the isImpliedIncluded value
Model:
derived="false"
 transient="false"
setIsImpliedIncluded
void setIsImpliedIncluded(boolean value)
Whether all necessary implied Relationships have been included in the `ownedRelationships` of this Element. This property may be true, even if there are not actually any `ownedRelationships` with `isImplied = true`, meaning that no such Relationships are actually implied for this Element. However, if it is false, then `ownedRelationships` may *not* contain any implied Relationships. That is, either *all* required implied Relationships must be included, or none of them.
Parameters:
`value` - the isImpliedIncluded value
Model:
derived="false"
 transient="false"
isLibraryElement
boolean isLibraryElement()
Whether this Element is contained in the ownership tree of a library model.
Returns:
the isLibraryElement value
Model:
derived="true"
 transient="true"
escapedName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) escapedName()
Return `name`, if that is not null, otherwise the `shortName`, if that is not null, otherwise null. If the returned value is non-null, it is returned as-is if it has the form of a basic name, or, otherwise, represented as a restricted name according to the lexical structure of the KerML textual notation (i.e., surrounded by single quote characters and with special characters escaped).
effectiveShortName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) effectiveShortName()
Return an effective `shortName` for this `Element`. By default this is the same as its `declaredShortName`.
 declaredShortName
effectiveName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) effectiveName()
Return an effective `name` for this `Element`. By default this is the same as its `declaredName`.
 declaredName
libraryNamespace
[Namespace](Namespace.html) libraryNamespace()
By default, return the library Namespace of the `owningRelationship` of this Element, if it has one.
 if owningRelationship <> null then owningRelationship.libraryNamespace()
 else null endif
path
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) path()
Return a unique description of the location of this `Element` in the containment structure rooted in a root `Namespace`. If the `Element` has a non-null `qualifiedName`, then return that. Otherwise, if it has an `owningRelationship`, then return the string constructed by appending to the `path` of it's `owningRelationship` the character `/` followed by the string representation of its position in the list of `ownedRelatedElements` of the `owningRelationship` (indexed starting at 1). Otherwise, return the empty string.
(Note that this operation is overridden for `Relationships` to use `owningRelatedElement` when appropriate.)
 if qualifiedName <> null then qualifiedName
 else if owningRelationship <> null then
 owningRelationship.path() + '/' + 
 owningRelationship.ownedRelatedElement->indexOf(self).toString()
 -- A position index shall be converted to a decimal string representation 
 -- consisting of only decimal digits, with no sign, leading zeros or leading 
 -- or trailing whitespace.
 else ''
 endif endif

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Element">Interface Element</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/AcceptActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AcceptActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/ActionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a></code>, <code><a href="../../../sysml/model/sysml/AllocationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AllocationUsage</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AnalysisCaseUsage</a></code>, <code><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></code>, <code><a href="Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></code>, <code><a href="../../../sysml/model/sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssertConstraintUsage</a></code>, <code><a href="../../../sysml/model/sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a></code>, <code><a href="Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a></code>, <code><a href="AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></code>, <code><a href="../../../sysml/model/sysml/AttributeDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeDefinition</a></code>, <code><a href="../../../sysml/model/sysml/AttributeUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AttributeUsage</a></code>, <code><a href="Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></code>, <code><a href="BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code>, <code><a href="../../../sysml/model/sysml/BindingConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">BindingConnectorAsUsage</a></code>, <code><a href="BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></code>, <code><a href="../../../sysml/model/sysml/CalculationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CalculationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CalculationUsage</a></code>, <code><a href="../../../sysml/model/sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">CaseUsage</a></code>, <code><a href="Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a></code>, <code><a href="Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code>, <code><a href="CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></code>, <code><a href="Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a></code>, <code><a href="../../../sysml/model/sysml/ConcernDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConcernUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConcernUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConjugatedPortTyping.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortTyping</a></code>, <code><a href="Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectionUsage</a></code>, <code><a href="Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code>, <code><a href="../../../sysml/model/sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConnectorAsUsage</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a></code>, <code><a href="ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></code>, <code><a href="../../../sysml/model/sysml/ControlNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ControlNode</a></code>, <code><a href="CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a></code>, <code><a href="DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a></code>, <code><a href="../../../sysml/model/sysml/DecisionNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">DecisionNode</a></code>, <code><a href="../../../sysml/model/sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Definition</a></code>, <code><a href="Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a></code>, <code><a href="Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a></code>, <code><a href="Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a></code>, <code><a href="Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a></code>, <code><a href="ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a></code>, <code><a href="EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationDefinition</a></code>, <code><a href="../../../sysml/model/sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a></code>, <code><a href="../../../sysml/model/sysml/EventOccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EventOccurrenceUsage</a></code>, <code><a href="../../../sysml/model/sysml/ExhibitStateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ExhibitStateUsage</a></code>, <code><a href="../../../sysml/model/sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a></code>, <code><a href="Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code>, <code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code>, <code><a href="FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code>, <code><a href="FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a></code>, <code><a href="FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a></code>, <code><a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></code>, <code><a href="FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code>, <code><a href="FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></code>, <code><a href="FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code>, <code><a href="Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code>, <code><a href="../../../sysml/model/sysml/FlowDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowDefinition</a></code>, <code><a href="FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a></code>, <code><a href="../../../sysml/model/sysml/FlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/ForkNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForkNode</a></code>, <code><a href="../../../sysml/model/sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a></code>, <code><a href="Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></code>, <code><a href="../../../sysml/model/sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a></code>, <code><a href="Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a></code>, <code><a href="../../../sysml/model/sysml/IncludeUseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IncludeUseCaseUsage</a></code>, <code><a href="IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></code>, <code><a href="InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a></code>, <code><a href="Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/InterfaceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">InterfaceUsage</a></code>, <code><a href="Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a></code>, <code><a href="Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></code>, <code><a href="InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code>, <code><a href="../../../sysml/model/sysml/ItemDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ItemUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ItemUsage</a></code>, <code><a href="../../../sysml/model/sysml/JoinNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">JoinNode</a></code>, <code><a href="LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></code>, <code><a href="LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></code>, <code><a href="LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></code>, <code><a href="LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></code>, <code><a href="LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></code>, <code><a href="LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></code>, <code><a href="../../../sysml/model/sysml/LoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">LoopActionUsage</a></code>, <code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code>, <code><a href="../../../sysml/model/sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a></code>, <code><a href="MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a></code>, <code><a href="../../../sysml/model/sysml/MergeNode.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MergeNode</a></code>, <code><a href="Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></code>, <code><a href="MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code>, <code><a href="../../../sysml/model/sysml/MetadataDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataDefinition</a></code>, <code><a href="MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code>, <code><a href="../../../sysml/model/sysml/MetadataUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MetadataUsage</a></code>, <code><a href="Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code>, <code><a href="MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code><a href="../../../sysml/model/sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a></code>, <code><a href="NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a></code>, <code><a href="NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></code>, <code><a href="../../../sysml/model/sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceDefinition</a></code>, <code><a href="../../../sysml/model/sysml/OccurrenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">OccurrenceUsage</a></code>, <code><a href="OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code>, <code><a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code>, <code><a href="Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></code>, <code><a href="ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartDefinition</a></code>, <code><a href="../../../sysml/model/sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a></code>, <code><a href="PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></code>, <code><a href="../../../sysml/model/sysml/PerformActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PerformActionUsage</a></code>, <code><a href="../../../sysml/model/sysml/PortConjugation.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortConjugation</a></code>, <code><a href="../../../sysml/model/sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code>, <code><a href="../../../sysml/model/sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a></code>, <code><a href="Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a></code>, <code><a href="Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a></code>, <code><a href="ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a></code>, <code><a href="../../../sysml/model/sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ReferenceUsage</a></code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code>, <code><a href="../../../sysml/model/sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingDefinition</a></code>, <code><a href="../../../sysml/model/sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code>, <code><a href="../../../sysml/model/sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a></code>, <code><a href="../../../sysml/model/sysml/RequirementDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementDefinition</a></code>, <code><a href="../../../sysml/model/sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code>, <code><a href="../../../sysml/model/sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a></code>, <code><a href="ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a></code>, <code><a href="ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/SatisfyRequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SatisfyRequirementUsage</a></code>, <code><a href="SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></code>, <code><a href="../../../sysml/model/sysml/SendActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SendActionUsage</a></code>, <code><a href="Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></code>, <code><a href="../../../sysml/model/sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a></code>, <code><a href="../../../sysml/model/sysml/StateDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateDefinition</a></code>, <code><a href="../../../sysml/model/sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a></code>, <code><a href="../../../sysml/model/sysml/StateUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateUsage</a></code>, <code><a href="Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code>, <code><a href="Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a></code>, <code><a href="Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a></code>, <code><a href="../../../sysml/model/sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a></code>, <code><a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></code>, <code><a href="Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionAsUsage</a></code>, <code><a href="SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code>, <code><a href="../../../sysml/model/sysml/SuccessionFlowUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SuccessionFlowUsage</a></code>, <code><a href="../../../sysml/model/sysml/TerminateActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TerminateActionUsage</a></code>, <code><a href="TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a></code>, <code><a href="../../../sysml/model/sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a></code>, <code><a href="../../../sysml/model/sysml/TransitionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionUsage</a></code>, <code><a href="../../../sysml/model/sysml/TriggerInvocationExpression.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TriggerInvocationExpression</a></code>, <code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code>, <code><a href="TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a></code>, <code><a href="Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a></code>, <code><a href="../../../sysml/model/sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">UseCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseDefinition</a></code>, <code><a href="../../../sysml/model/sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VerificationCaseUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointDefinition</a></code>, <code><a href="../../../sysml/model/sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewpointUsage</a></code>, <code><a href="../../../sysml/model/sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a></code>, <code><a href="../../../sysml/model/sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewUsage</a></code>, <code><a href="../../../sysml/model/sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Element</span><span class="extends-implements">
extends <a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a>, com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</span></div>
<div class="block"><p>An <code>Element</code> is a constituent of a model that is uniquely identified relative to all other <code>Elements</code>. It can have <code>Relationships</code> with other <code>Elements</code>. Some of these <code>Relationships</code> might imply ownership of other <code>Elements</code>, which means that if an <code>Element</code> is deleted from a model, then so are all the <code>Elements</code> that it owns.</p>
 
 ownedElement = ownedRelationship.ownedRelatedElement
 owner = owningRelationship.owningRelatedElement
 qualifiedName =
     if owningNamespace = null then null
     else if name &lt;&gt; null and 
         owningNamespace.ownedMember-&gt;
         select(m | m.name = name).indexOf(self) &lt;&gt; 1 then null
     else if owningNamespace.owner = null then escapedName()
     else if owningNamespace.qualifiedName = null or 
             escapedName() = null then null
     else owningNamespace.qualifiedName + '::' + escapedName()
     endif endif endif endif
 documentation = ownedElement-&gt;selectByKind(Documentation)
 ownedAnnotation = ownedRelationship-&gt;
     selectByKind(Annotation)-&gt;
     select(a | a.annotatedElement = self)
 name = effectiveName()
 ownedRelationship-&gt;exists(isImplied) implies isImpliedIncluded
 isLibraryElement = libraryNamespace() &lt;&gt; null
 
 shortName = effectiveShortName()
 owningNamespace =
     if owningMembership = null then null
     else owningMembership.membershipOwningNamespace
     endif
 textualRepresentation = ownedElement-&gt;selectByKind(TextualRepresentation)</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#effectiveName()">effectiveName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return an effective <code>name</code> for this <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#effectiveShortName()">effectiveShortName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return an effective <code>shortName</code> for this <code>Element</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#escapedName()">escapedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return <code>name</code>, if that is not null, otherwise the <code>shortName</code>, if that is not null, otherwise null.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAliasIds()">getAliasIds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Various alternative identifiers for this Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDeclaredName()">getDeclaredName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The declared name of this <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDeclaredShortName()">getDeclaredShortName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">An optional alternative name for the <code>Element</code> that is intended to be shorter or in some way more succinct than its primary <code>name</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDocumentation()">getDocumentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Documentation owned by this Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementId()">getElementId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The globally unique identifier for this Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The name to be used for this <code>Element</code> during name resolution within its <code>owningNamespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAnnotation()">getOwnedAnnotation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>ownedRelationships</code> of this <code>Element</code> that are <code>Annotations</code>, for which this <code>Element</code> is the <code>annotatedElement</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedElement()">getOwnedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Elements owned by this Element, derived as the <tt>ownedRelatedElements</tt> of the <tt>ownedRelationships</tt> of this Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedRelationship()">getOwnedRelationship</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Relationships for which this Element is the <tt>owningRelatedElement</tt>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwner()">getOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The owner of this Element, derived as the <code>owningRelatedElement</code> of the <code>owningRelationship</code> of this Element, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningMembership()">getOwningMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>owningRelationship</code> of this <code>Element</code>, if that <code>Relationship</code> is a <code>Membership</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningNamespace()">getOwningNamespace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Namespace</code> that owns this <code>Element</code>, which is the <code>membershipOwningNamespace</code> of the <code>owningMembership</code> of this <code>Element</code>, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningRelationship()">getOwningRelationship</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Relationship for which this Element is an <tt>ownedRelatedElement</tt>, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getQualifiedName()">getQualifiedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The full ownership-qualified name of this <code>Element</code>, represented in a form that is valid according to the KerML textual concrete syntax for qualified names (including use of unrestricted name notation and escaped characters, as necessary).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getShortName()">getShortName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The short name to be used for this <code>Element</code> during name resolution within its <code>owningNamespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTextualRepresentation()">getTextualRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>TextualRepresentations</code> that annotate this <code>Element</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isImpliedIncluded()">isImpliedIncluded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether all necessary implied Relationships have been included in the <code>ownedRelationships</code> of this Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLibraryElement()">isLibraryElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this Element is contained in the ownership tree of a library model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#libraryNamespace()">libraryNamespace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">By default, return the library Namespace of the <code>owningRelationship</code> of this Element, if it has one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#path()">path</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a unique description of the location of this <code>Element</code> in the containment structure rooted in a root <code>Namespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDeclaredName(java.lang.String)">setDeclaredName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The declared name of this <code>Element</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">An optional alternative name for the <code>Element</code> that is intended to be shorter or in some way more succinct than its primary <code>name</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setElementId(java.lang.String)">setElementId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The globally unique identifier for this Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether all necessary implied Relationships have been included in the <code>ownedRelationships</code> of this Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The owner of this Element, derived as the <code>owningRelatedElement</code> of the <code>owningRelationship</code> of this Element, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a><wbr/>(<a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>owningRelationship</code> of this <code>Element</code>, if that <code>Relationship</code> is a <code>Membership</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a><wbr/>(<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Relationship for which this Element is an <tt>ownedRelatedElement</tt>, if any.</div>
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
<section class="detail" id="getOwningMembership()">
<h3>getOwningMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></span> <span class="element-name">getOwningMembership</span>()</div>
<div class="block"><p>The <code>owningRelationship</code> of this <code>Element</code>, if that <code>Relationship</code> is a <code>Membership</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="OwningMembership.html#getOwnedMemberElement()"><code>OwningMembership.getOwnedMemberElement()</code></a>
        subsets=<a href="#getOwningRelationship()"><code>getOwningRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">
<h3>setOwningMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningMembership</span><wbr/><span class="parameters">(@CheckForNull
 <a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> value)</span></div>
<div class="block"><p>The <code>owningRelationship</code> of this <code>Element</code>, if that <code>Relationship</code> is a <code>Membership</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the owningMembership value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="OwningMembership.html#getOwnedMemberElement()"><code>OwningMembership.getOwnedMemberElement()</code></a>
        subsets=<a href="#getOwningRelationship()"><code>getOwningRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningRelationship()">
<h3>getOwningRelationship</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span> <span class="element-name">getOwningRelationship</span>()</div>
<div class="block"><p>The Relationship for which this Element is an <tt>ownedRelatedElement</tt>, if any.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningRelationship value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        container="true"
        opposite=<a href="Relationship.html#getOwnedRelatedElement()"><code>Relationship.getOwnedRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">
<h3>setOwningRelationship</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningRelationship</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> value)</span></div>
<div class="block"><p>The Relationship for which this Element is an <tt>ownedRelatedElement</tt>, if any.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the owningRelationship value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        container="true"
        opposite=<a href="Relationship.html#getOwnedRelatedElement()"><code>Relationship.getOwnedRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningNamespace()">
<h3>getOwningNamespace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">getOwningNamespace</span>()</div>
<div class="block"><p>The <code>Namespace</code> that owns this <code>Element</code>, which is the <code>membershipOwningNamespace</code> of the <code>owningMembership</code> of this <code>Element</code>, if any.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningNamespace value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Namespace.html#getOwnedMember()"><code>Namespace.getOwnedMember()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementId()">
<h3>getElementId</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementId</span>()</div>
<div class="block"><p>The globally unique identifier for this Element. This is intended to be set by tooling, and it must not change during the lifetime of the Element.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the elementId value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementId(java.lang.String)">
<h3>setElementId</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setElementId</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>The globally unique identifier for this Element. This is intended to be set by tooling, and it must not change during the lifetime of the Element.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the elementId value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRelationship()">
<h3>getOwnedRelationship</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="element-name">getOwnedRelationship</span>()</div>
<div class="block"><p>The Relationships for which this Element is the <tt>owningRelatedElement</tt>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedRelationship value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        containment="true"
        opposite=<a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwner()">
<h3>getOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getOwner</span>()</div>
<div class="block"><p>The owner of this Element, derived as the <code>owningRelatedElement</code> of the <code>owningRelationship</code> of this Element, if any.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owner value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="#getOwnedElement()"><code>getOwnedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setOwner</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwner</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</span></div>
<div class="block"><p>The owner of this Element, derived as the <code>owningRelatedElement</code> of the <code>owningRelationship</code> of this Element, if any.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the owner value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="#getOwnedElement()"><code>getOwnedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedElement()">
<h3>getOwnedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">getOwnedElement</span>()</div>
<div class="block"><p>The Elements owned by this Element, derived as the <tt>ownedRelatedElements</tt> of the <tt>ownedRelationships</tt> of this Element.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="#getOwner()"><code>getOwner()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentation()">
<h3>getDocumentation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a>&gt;</span> <span class="element-name">getDocumentation</span>()</div>
<div class="block"><p>The Documentation owned by this Element.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the documentation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Documentation.html#getDocumentedElement()"><code>Documentation.getDocumentedElement()</code></a>
        subsets=<a href="#getOwnedElement()"><code>getOwnedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAnnotation()">
<h3>getOwnedAnnotation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a>&gt;</span> <span class="element-name">getOwnedAnnotation</span>()</div>
<div class="block"><p>The <code>ownedRelationships</code> of this <code>Element</code> that are <code>Annotations</code>, for which this <code>Element</code> is the <code>annotatedElement</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedAnnotation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Annotation.html#getOwningAnnotatedElement()"><code>Annotation.getOwningAnnotatedElement()</code></a>
        subsets=<a href="#getOwnedRelationship()"><code>getOwnedRelationship()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTextualRepresentation()">
<h3>getTextualRepresentation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a>&gt;</span> <span class="element-name">getTextualRepresentation</span>()</div>
<div class="block"><p>The <code>TextualRepresentations</code> that annotate this <code>Element</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the textualRepresentation value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="TextualRepresentation.html#getRepresentedElement()"><code>TextualRepresentation.getRepresentedElement()</code></a>
        subsets=<a href="#getOwnedElement()"><code>getOwnedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAliasIds()">
<h3>getAliasIds</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAliasIds</span>()</div>
<div class="block"><p>Various alternative identifiers for this Element. Generally, these will be set by tools.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the aliasIds value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeclaredShortName()">
<h3>getDeclaredShortName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDeclaredShortName</span>()</div>
<div class="block"><p>An optional alternative name for the <code>Element</code> that is intended to be shorter or in some way more succinct than its primary <code>name</code>. It may act as a modeler-specified identifier for the <code>Element</code>, though it is then the responsibility of the modeler to maintain the uniqueness of this identifier within a model or relative to some other context.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the declaredShortName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDeclaredShortName(java.lang.String)">
<h3>setDeclaredShortName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDeclaredShortName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>An optional alternative name for the <code>Element</code> that is intended to be shorter or in some way more succinct than its primary <code>name</code>. It may act as a modeler-specified identifier for the <code>Element</code>, though it is then the responsibility of the modeler to maintain the uniqueness of this identifier within a model or relative to some other context.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the declaredShortName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeclaredName()">
<h3>getDeclaredName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDeclaredName</span>()</div>
<div class="block"><p>The declared name of this <code>Element</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the declaredName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDeclaredName(java.lang.String)">
<h3>setDeclaredName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDeclaredName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>The declared name of this <code>Element</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the declaredName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShortName()">
<h3>getShortName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShortName</span>()</div>
<div class="block"><p>The short name to be used for this <code>Element</code> during name resolution within its <code>owningNamespace</code>. This is derived using the <code>effectiveShortName()</code> operation. By default, it is the same as the <code>declaredShortName</code>, but this is overridden for certain kinds of <code>Elements</code> to compute a <code>shortName</code> even when the <code>declaredName</code> is null.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the shortName value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block"><p>The name to be used for this <code>Element</code> during name resolution within its <code>owningNamespace</code>. This is derived using the <code>effectiveName()</code> operation. By default, it is the same as the <code>declaredName</code>, but this is overridden for certain kinds of <code>Elements</code> to compute a <code>name</code> even when the <code>declaredName</code> is null.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedName()">
<h3>getQualifiedName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedName</span>()</div>
<div class="block"><p>The full ownership-qualified name of this <code>Element</code>, represented in a form that is valid according to the KerML textual concrete syntax for qualified names (including use of unrestricted name notation and escaped characters, as necessary). The <code>qualifiedName</code> is null if this <code>Element</code> has no <code>owningNamespace</code> or if there is not a complete ownership chain of named <code>Namespaces</code> from a root <code>Namespace</code> to this <code>Element</code>. If the <code>owningNamespace</code> has other <code>Elements</code> with the same name as this one, then the <code>qualifiedName</code> is null for all such <code>Elements</code> other than the first.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the qualifiedName value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImpliedIncluded()">
<h3>isImpliedIncluded</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isImpliedIncluded</span>()</div>
<div class="block"><p>Whether all necessary implied Relationships have been included in the <code>ownedRelationships</code> of this Element. This property may be true, even if there are not actually any <code>ownedRelationships</code> with <code>isImplied = true</code>, meaning that no such Relationships are actually implied for this Element. However, if it is false, then <code>ownedRelationships</code> may <em>not</em> contain any implied Relationships. That is, either <em>all</em> required implied Relationships must be included, or none of them.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isImpliedIncluded value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsImpliedIncluded(boolean)">
<h3>setIsImpliedIncluded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsImpliedIncluded</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether all necessary implied Relationships have been included in the <code>ownedRelationships</code> of this Element. This property may be true, even if there are not actually any <code>ownedRelationships</code> with <code>isImplied = true</code>, meaning that no such Relationships are actually implied for this Element. However, if it is false, then <code>ownedRelationships</code> may <em>not</em> contain any implied Relationships. That is, either <em>all</em> required implied Relationships must be included, or none of them.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isImpliedIncluded value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLibraryElement()">
<h3>isLibraryElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLibraryElement</span>()</div>
<div class="block"><p>Whether this Element is contained in the ownership tree of a library model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isLibraryElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="escapedName()">
<h3>escapedName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">escapedName</span>()</div>
<div class="block"><p>Return <code>name</code>, if that is not null, otherwise the <code>shortName</code>, if that is not null, otherwise null. If the returned value is non-null, it is returned as-is if it has the form of a basic name, or, otherwise, represented as a restricted name according to the lexical structure of the KerML textual notation (i.e., surrounded by single quote characters and with special characters escaped).</p></div>
</section>
</li>
<li>
<section class="detail" id="effectiveShortName()">
<h3>effectiveShortName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">effectiveShortName</span>()</div>
<div class="block"><p>Return an effective <code>shortName</code> for this <code>Element</code>. By default this is the same as its <code>declaredShortName</code>.</p>
 declaredShortName</div>
</section>
</li>
<li>
<section class="detail" id="effectiveName()">
<h3>effectiveName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">effectiveName</span>()</div>
<div class="block"><p>Return an effective <code>name</code> for this <code>Element</code>. By default this is the same as its <code>declaredName</code>.</p>
 declaredName</div>
</section>
</li>
<li>
<section class="detail" id="libraryNamespace()">
<h3>libraryNamespace</h3>
<div class="member-signature"><span class="return-type"><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">libraryNamespace</span>()</div>
<div class="block"><p>By default, return the library Namespace of the <code>owningRelationship</code> of this Element, if it has one.</p>
 if owningRelationship &lt;&gt; null then owningRelationship.libraryNamespace()
 else null endif</div>
</section>
</li>
<li>
<section class="detail" id="path()">
<h3>path</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">path</span>()</div>
<div class="block"><p>Return a unique description of the location of this <code>Element</code> in the containment structure rooted in a root <code>Namespace</code>. If the <code>Element</code> has a non-null <code>qualifiedName</code>, then return that. Otherwise, if it has an <code>owningRelationship</code>, then return the string constructed by appending to the <code>path</code> of it's <code>owningRelationship</code> the character <code>/</code> followed by the string representation of its position in the list of <code>ownedRelatedElements</code> of the <code>owningRelationship</code> (indexed starting at 1). Otherwise, return the empty string.</p>
<p>(Note that this operation is overridden for <code>Relationships</code> to use <code>owningRelatedElement</code> when appropriate.)</p>
 if qualifiedName &lt;&gt; null then qualifiedName
 else if owningRelationship &lt;&gt; null then
     owningRelationship.path() + '/' + 
     owningRelationship.ownedRelatedElement-&gt;indexOf(self).toString()
     -- A position index shall be converted to a decimal string representation 
     -- consisting of only decimal digits, with no sign, leading zeros or leading 
     -- or trailing whitespace.
 else ''
 endif endif</div>
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
