# JAVA OPENAPI: KerMLModelVisitor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/KerMLModelVisitor.html
- source_path: `com/dassault_systemes/modeler/kerml/model/KerMLModelVisitor.html`
- source_sha256: `4849c494000b7cd978811488fdf7ab9252d045173701beefe440e0c1e1461b10`
- captured_utc: `2026-07-14T16:44:48.330847+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Interface KerMLModelVisitor<C extends [KerMLVisitorContext](KerMLVisitorContext.html)>

Type Parameters:
`C` - The type of the visitor context, which must extend [`KerMLVisitorContext`](KerMLVisitorContext.html).

All Superinterfaces:
`[AbstractVisitor](../../../../nomagic/magicdraw/uml/AbstractVisitor.html)`

All Known Subinterfaces:
`[KerMLModelHierarchyVisitor](KerMLModelHierarchyVisitor.html)<C>`, `[SysMLModelHierarchyVisitor](../../sysml/model/SysMLModelHierarchyVisitor.html)<C>`, `[SysMLModelVisitor](../../sysml/model/SysMLModelVisitor.html)<C>`

@OpenApiAllpublic interfaceKerMLModelVisitor<C extends [KerMLVisitorContext](KerMLVisitorContext.html)>extends [AbstractVisitor](../../../../nomagic/magicdraw/uml/AbstractVisitor.html)

A visitor interface for traversing the KerML model.
 This interface extends [`AbstractVisitor`](../../../../nomagic/magicdraw/uml/AbstractVisitor.html) and provides methods to visit various elements
 in the KerML model, including classes, packages, relationships, and more. It is designed to
 work with a visitor context of type [`KerMLVisitorContext`](KerMLVisitorContext.html).

See Also:
[`AbstractVisitor`](../../../../nomagic/magicdraw/uml/AbstractVisitor.html)
[`KerMLVisitorContext`](KerMLVisitorContext.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default [C](KerMLModelVisitor.html)`
`[createVisitorContext](#createVisitorContext())()`
Creates a new visitor context.
`void`
`[visitAnnotatingElement](#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C))([AnnotatingElement](kerml/AnnotatingElement.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`AnnotatingElement`](kerml/AnnotatingElement.html).
`void`
`[visitAnnotation](#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C))([Annotation](kerml/Annotation.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Annotation`](kerml/Annotation.html).
`void`
`[visitAssociation](#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C))([Association](kerml/Association.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Association`](kerml/Association.html).
`void`
`[visitAssociationStructure](#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C))([AssociationStructure](kerml/AssociationStructure.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`AssociationStructure`](kerml/AssociationStructure.html).
`void`
`[visitBehavior](#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C))([Behavior](kerml/Behavior.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Behavior`](kerml/Behavior.html).
`void`
`[visitBindingConnector](#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C))([BindingConnector](kerml/BindingConnector.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`BindingConnector`](kerml/BindingConnector.html).
`void`
`[visitBooleanExpression](#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C))([BooleanExpression](kerml/BooleanExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`BooleanExpression`](kerml/BooleanExpression.html).
`void`
`[visitClass](#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C))([Class](kerml/Class.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Class`](kerml/Class.html).
`void`
`[visitClassifier](#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C))([Classifier](kerml/Classifier.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Classifier`](kerml/Classifier.html).
`void`
`[visitCollectExpression](#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C))([CollectExpression](kerml/CollectExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`CollectExpression`](kerml/CollectExpression.html).
`void`
`[visitComment](#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C))([Comment](kerml/Comment.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Comment`](kerml/Comment.html).
`void`
`[visitConjugation](#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C))([Conjugation](kerml/Conjugation.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Conjugation`](kerml/Conjugation.html).
`void`
`[visitConnector](#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C))([Connector](kerml/Connector.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Connector`](kerml/Connector.html).
`void`
`[visitConstructorExpression](#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C))([ConstructorExpression](kerml/ConstructorExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`ConstructorExpression`](kerml/ConstructorExpression.html).
`void`
`[visitCrossSubsetting](#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C))([CrossSubsetting](kerml/CrossSubsetting.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`CrossSubsetting`](kerml/CrossSubsetting.html).
`void`
`[visitDataType](#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C))([DataType](kerml/DataType.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`DataType`](kerml/DataType.html).
`void`
`[visitDependency](#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C))([Dependency](kerml/Dependency.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Dependency`](kerml/Dependency.html).
`void`
`[visitDifferencing](#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C))([Differencing](kerml/Differencing.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Differencing`](kerml/Differencing.html).
`void`
`[visitDisjoining](#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C))([Disjoining](kerml/Disjoining.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Disjoining`](kerml/Disjoining.html).
`void`
`[visitDocumentation](#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C))([Documentation](kerml/Documentation.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Documentation`](kerml/Documentation.html).
`void`
`[visitElement](#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C))([Element](kerml/Element.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Element`](kerml/Element.html).
`void`
`[visitElementFilterMembership](#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C))([ElementFilterMembership](kerml/ElementFilterMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`ElementFilterMembership`](kerml/ElementFilterMembership.html).
`void`
`[visitEndFeatureMembership](#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C))([EndFeatureMembership](kerml/EndFeatureMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`EndFeatureMembership`](kerml/EndFeatureMembership.html).
`void`
`[visitExpression](#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C))([Expression](kerml/Expression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Expression`](kerml/Expression.html).
`void`
`[visitFeature](#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C))([Feature](kerml/Feature.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Feature`](kerml/Feature.html).
`void`
`[visitFeatureChainExpression](#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C))([FeatureChainExpression](kerml/FeatureChainExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureChainExpression`](kerml/FeatureChainExpression.html).
`void`
`[visitFeatureChaining](#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C))([FeatureChaining](kerml/FeatureChaining.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureChaining`](kerml/FeatureChaining.html).
`void`
`[visitFeatureInverting](#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C))([FeatureInverting](kerml/FeatureInverting.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureInverting`](kerml/FeatureInverting.html).
`void`
`[visitFeatureMembership](#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C))([FeatureMembership](kerml/FeatureMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureMembership`](kerml/FeatureMembership.html).
`void`
`[visitFeatureReferenceExpression](#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C))([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html).
`void`
`[visitFeatureTyping](#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C))([FeatureTyping](kerml/FeatureTyping.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureTyping`](kerml/FeatureTyping.html).
`void`
`[visitFeatureValue](#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C))([FeatureValue](kerml/FeatureValue.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FeatureValue`](kerml/FeatureValue.html).
`void`
`[visitFlow](#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C))([Flow](kerml/Flow.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Flow`](kerml/Flow.html).
`void`
`[visitFlowEnd](#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C))([FlowEnd](kerml/FlowEnd.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`FlowEnd`](kerml/FlowEnd.html).
`void`
`[visitFunction](#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C))([Function](kerml/Function.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Function`](kerml/Function.html).
`void`
`[visitImport](#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C))([Import](kerml/Import.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Import`](kerml/Import.html).
`void`
`[visitIndexExpression](#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C))([IndexExpression](kerml/IndexExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`IndexExpression`](kerml/IndexExpression.html).
`void`
`[visitInstantiationExpression](#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C))([InstantiationExpression](kerml/InstantiationExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`InstantiationExpression`](kerml/InstantiationExpression.html).
`void`
`[visitInteraction](#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C))([Interaction](kerml/Interaction.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Interaction`](kerml/Interaction.html).
`void`
`[visitIntersecting](#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C))([Intersecting](kerml/Intersecting.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Intersecting`](kerml/Intersecting.html).
`void`
`[visitInvariant](#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C))([Invariant](kerml/Invariant.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Invariant`](kerml/Invariant.html).
`void`
`[visitInvocationExpression](#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C))([InvocationExpression](kerml/InvocationExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`InvocationExpression`](kerml/InvocationExpression.html).
`void`
`[visitLibraryPackage](#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C))([LibraryPackage](kerml/LibraryPackage.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LibraryPackage`](kerml/LibraryPackage.html).
`void`
`[visitLiteralBoolean](#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C))([LiteralBoolean](kerml/LiteralBoolean.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LiteralBoolean`](kerml/LiteralBoolean.html).
`void`
`[visitLiteralExpression](#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C))([LiteralExpression](kerml/LiteralExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LiteralExpression`](kerml/LiteralExpression.html).
`void`
`[visitLiteralInfinity](#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C))([LiteralInfinity](kerml/LiteralInfinity.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LiteralInfinity`](kerml/LiteralInfinity.html).
`void`
`[visitLiteralInteger](#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C))([LiteralInteger](kerml/LiteralInteger.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LiteralInteger`](kerml/LiteralInteger.html).
`void`
`[visitLiteralRational](#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C))([LiteralRational](kerml/LiteralRational.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LiteralRational`](kerml/LiteralRational.html).
`void`
`[visitLiteralString](#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C))([LiteralString](kerml/LiteralString.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`LiteralString`](kerml/LiteralString.html).
`void`
`[visitMembership](#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C))([Membership](kerml/Membership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Membership`](kerml/Membership.html).
`void`
`[visitMembershipImport](#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C))([MembershipImport](kerml/MembershipImport.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`MembershipImport`](kerml/MembershipImport.html).
`void`
`[visitMetaclass](#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C))([Metaclass](kerml/Metaclass.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Metaclass`](kerml/Metaclass.html).
`void`
`[visitMetadataAccessExpression](#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C))([MetadataAccessExpression](kerml/MetadataAccessExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`MetadataAccessExpression`](kerml/MetadataAccessExpression.html).
`void`
`[visitMetadataFeature](#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C))([MetadataFeature](kerml/MetadataFeature.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`MetadataFeature`](kerml/MetadataFeature.html).
`void`
`[visitMultiplicity](#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C))([Multiplicity](kerml/Multiplicity.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Multiplicity`](kerml/Multiplicity.html).
`void`
`[visitMultiplicityRange](#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C))([MultiplicityRange](kerml/MultiplicityRange.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`MultiplicityRange`](kerml/MultiplicityRange.html).
`void`
`[visitNamespace](#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C))([Namespace](kerml/Namespace.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Namespace`](kerml/Namespace.html).
`void`
`[visitNamespaceImport](#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C))([NamespaceImport](kerml/NamespaceImport.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`NamespaceImport`](kerml/NamespaceImport.html).
`void`
`[visitNullExpression](#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C))([NullExpression](kerml/NullExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`NullExpression`](kerml/NullExpression.html).
`void`
`[visitOperatorExpression](#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C))([OperatorExpression](kerml/OperatorExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`OperatorExpression`](kerml/OperatorExpression.html).
`void`
`[visitOwningMembership](#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C))([OwningMembership](kerml/OwningMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`OwningMembership`](kerml/OwningMembership.html).
`void`
`[visitPackage](#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C))([Package](kerml/Package.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Package`](kerml/Package.html).
`void`
`[visitParameterMembership](#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C))([ParameterMembership](kerml/ParameterMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`ParameterMembership`](kerml/ParameterMembership.html).
`void`
`[visitPayloadFeature](#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C))([PayloadFeature](kerml/PayloadFeature.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`PayloadFeature`](kerml/PayloadFeature.html).
`void`
`[visitPredicate](#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C))([Predicate](kerml/Predicate.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Predicate`](kerml/Predicate.html).
`void`
`[visitRedefinition](#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C))([Redefinition](kerml/Redefinition.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Redefinition`](kerml/Redefinition.html).
`void`
`[visitReferenceSubsetting](#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C))([ReferenceSubsetting](kerml/ReferenceSubsetting.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`ReferenceSubsetting`](kerml/ReferenceSubsetting.html).
`void`
`[visitRelationship](#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C))([Relationship](kerml/Relationship.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Relationship`](kerml/Relationship.html).
`void`
`[visitResultExpressionMembership](#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C))([ResultExpressionMembership](kerml/ResultExpressionMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`ResultExpressionMembership`](kerml/ResultExpressionMembership.html).
`void`
`[visitReturnParameterMembership](#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C))([ReturnParameterMembership](kerml/ReturnParameterMembership.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`ReturnParameterMembership`](kerml/ReturnParameterMembership.html).
`void`
`[visitSelectExpression](#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C))([SelectExpression](kerml/SelectExpression.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`SelectExpression`](kerml/SelectExpression.html).
`void`
`[visitSpecialization](#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C))([Specialization](kerml/Specialization.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Specialization`](kerml/Specialization.html).
`void`
`[visitStep](#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C))([Step](kerml/Step.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Step`](kerml/Step.html).
`void`
`[visitStructure](#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C))([Structure](kerml/Structure.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Structure`](kerml/Structure.html).
`void`
`[visitSubclassification](#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C))([Subclassification](kerml/Subclassification.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Subclassification`](kerml/Subclassification.html).
`void`
`[visitSubsetting](#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C))([Subsetting](kerml/Subsetting.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Subsetting`](kerml/Subsetting.html).
`void`
`[visitSuccession](#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C))([Succession](kerml/Succession.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Succession`](kerml/Succession.html).
`void`
`[visitSuccessionFlow](#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C))([SuccessionFlow](kerml/SuccessionFlow.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`SuccessionFlow`](kerml/SuccessionFlow.html).
`void`
`[visitTextualRepresentation](#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C))([TextualRepresentation](kerml/TextualRepresentation.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`TextualRepresentation`](kerml/TextualRepresentation.html).
`void`
`[visitType](#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C))([Type](kerml/Type.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Type`](kerml/Type.html).
`void`
`[visitTypeFeaturing](#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C))([TypeFeaturing](kerml/TypeFeaturing.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`TypeFeaturing`](kerml/TypeFeaturing.html).
`void`
`[visitUnioning](#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C))([Unioning](kerml/Unioning.html) element,
 [C](KerMLModelVisitor.html) context)`
Visitor method for [`Unioning`](kerml/Unioning.html).

============ METHOD DETAIL ========== 
Method Details
visitAnnotatingElement
void visitAnnotatingElement([AnnotatingElement](kerml/AnnotatingElement.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`AnnotatingElement`](kerml/AnnotatingElement.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAnnotation
void visitAnnotation([Annotation](kerml/Annotation.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Annotation`](kerml/Annotation.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAssociation
void visitAssociation([Association](kerml/Association.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Association`](kerml/Association.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitAssociationStructure
void visitAssociationStructure([AssociationStructure](kerml/AssociationStructure.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`AssociationStructure`](kerml/AssociationStructure.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitBehavior
void visitBehavior([Behavior](kerml/Behavior.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Behavior`](kerml/Behavior.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitBindingConnector
void visitBindingConnector([BindingConnector](kerml/BindingConnector.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`BindingConnector`](kerml/BindingConnector.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitBooleanExpression
void visitBooleanExpression([BooleanExpression](kerml/BooleanExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`BooleanExpression`](kerml/BooleanExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitClass
void visitClass([Class](kerml/Class.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Class`](kerml/Class.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitClassifier
void visitClassifier([Classifier](kerml/Classifier.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Classifier`](kerml/Classifier.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitCollectExpression
void visitCollectExpression([CollectExpression](kerml/CollectExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`CollectExpression`](kerml/CollectExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitComment
void visitComment([Comment](kerml/Comment.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Comment`](kerml/Comment.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConjugation
void visitConjugation([Conjugation](kerml/Conjugation.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Conjugation`](kerml/Conjugation.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConnector
void visitConnector([Connector](kerml/Connector.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Connector`](kerml/Connector.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitConstructorExpression
void visitConstructorExpression([ConstructorExpression](kerml/ConstructorExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`ConstructorExpression`](kerml/ConstructorExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitCrossSubsetting
void visitCrossSubsetting([CrossSubsetting](kerml/CrossSubsetting.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`CrossSubsetting`](kerml/CrossSubsetting.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDataType
void visitDataType([DataType](kerml/DataType.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`DataType`](kerml/DataType.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDependency
void visitDependency([Dependency](kerml/Dependency.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Dependency`](kerml/Dependency.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDifferencing
void visitDifferencing([Differencing](kerml/Differencing.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Differencing`](kerml/Differencing.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDisjoining
void visitDisjoining([Disjoining](kerml/Disjoining.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Disjoining`](kerml/Disjoining.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitDocumentation
void visitDocumentation([Documentation](kerml/Documentation.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Documentation`](kerml/Documentation.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitElement
void visitElement([Element](kerml/Element.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Element`](kerml/Element.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitElementFilterMembership
void visitElementFilterMembership([ElementFilterMembership](kerml/ElementFilterMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`ElementFilterMembership`](kerml/ElementFilterMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitEndFeatureMembership
void visitEndFeatureMembership([EndFeatureMembership](kerml/EndFeatureMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`EndFeatureMembership`](kerml/EndFeatureMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitExpression
void visitExpression([Expression](kerml/Expression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Expression`](kerml/Expression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeature
void visitFeature([Feature](kerml/Feature.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Feature`](kerml/Feature.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureChainExpression
void visitFeatureChainExpression([FeatureChainExpression](kerml/FeatureChainExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureChainExpression`](kerml/FeatureChainExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureChaining
void visitFeatureChaining([FeatureChaining](kerml/FeatureChaining.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureChaining`](kerml/FeatureChaining.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureInverting
void visitFeatureInverting([FeatureInverting](kerml/FeatureInverting.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureInverting`](kerml/FeatureInverting.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureMembership
void visitFeatureMembership([FeatureMembership](kerml/FeatureMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureMembership`](kerml/FeatureMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureReferenceExpression
void visitFeatureReferenceExpression([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureTyping
void visitFeatureTyping([FeatureTyping](kerml/FeatureTyping.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureTyping`](kerml/FeatureTyping.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFeatureValue
void visitFeatureValue([FeatureValue](kerml/FeatureValue.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FeatureValue`](kerml/FeatureValue.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFlow
void visitFlow([Flow](kerml/Flow.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Flow`](kerml/Flow.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFlowEnd
void visitFlowEnd([FlowEnd](kerml/FlowEnd.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`FlowEnd`](kerml/FlowEnd.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitFunction
void visitFunction([Function](kerml/Function.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Function`](kerml/Function.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitImport
void visitImport([Import](kerml/Import.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Import`](kerml/Import.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitIndexExpression
void visitIndexExpression([IndexExpression](kerml/IndexExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`IndexExpression`](kerml/IndexExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitInstantiationExpression
void visitInstantiationExpression([InstantiationExpression](kerml/InstantiationExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`InstantiationExpression`](kerml/InstantiationExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitInteraction
void visitInteraction([Interaction](kerml/Interaction.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Interaction`](kerml/Interaction.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitIntersecting
void visitIntersecting([Intersecting](kerml/Intersecting.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Intersecting`](kerml/Intersecting.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitInvariant
void visitInvariant([Invariant](kerml/Invariant.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Invariant`](kerml/Invariant.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitInvocationExpression
void visitInvocationExpression([InvocationExpression](kerml/InvocationExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`InvocationExpression`](kerml/InvocationExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLibraryPackage
void visitLibraryPackage([LibraryPackage](kerml/LibraryPackage.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LibraryPackage`](kerml/LibraryPackage.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLiteralBoolean
void visitLiteralBoolean([LiteralBoolean](kerml/LiteralBoolean.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LiteralBoolean`](kerml/LiteralBoolean.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLiteralExpression
void visitLiteralExpression([LiteralExpression](kerml/LiteralExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LiteralExpression`](kerml/LiteralExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLiteralInfinity
void visitLiteralInfinity([LiteralInfinity](kerml/LiteralInfinity.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LiteralInfinity`](kerml/LiteralInfinity.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLiteralInteger
void visitLiteralInteger([LiteralInteger](kerml/LiteralInteger.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LiteralInteger`](kerml/LiteralInteger.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLiteralRational
void visitLiteralRational([LiteralRational](kerml/LiteralRational.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LiteralRational`](kerml/LiteralRational.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitLiteralString
void visitLiteralString([LiteralString](kerml/LiteralString.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`LiteralString`](kerml/LiteralString.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMembership
void visitMembership([Membership](kerml/Membership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Membership`](kerml/Membership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMembershipImport
void visitMembershipImport([MembershipImport](kerml/MembershipImport.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`MembershipImport`](kerml/MembershipImport.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMetaclass
void visitMetaclass([Metaclass](kerml/Metaclass.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Metaclass`](kerml/Metaclass.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMetadataAccessExpression
void visitMetadataAccessExpression([MetadataAccessExpression](kerml/MetadataAccessExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`MetadataAccessExpression`](kerml/MetadataAccessExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMetadataFeature
void visitMetadataFeature([MetadataFeature](kerml/MetadataFeature.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`MetadataFeature`](kerml/MetadataFeature.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMultiplicity
void visitMultiplicity([Multiplicity](kerml/Multiplicity.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Multiplicity`](kerml/Multiplicity.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitMultiplicityRange
void visitMultiplicityRange([MultiplicityRange](kerml/MultiplicityRange.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`MultiplicityRange`](kerml/MultiplicityRange.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitNamespace
void visitNamespace([Namespace](kerml/Namespace.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Namespace`](kerml/Namespace.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitNamespaceImport
void visitNamespaceImport([NamespaceImport](kerml/NamespaceImport.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`NamespaceImport`](kerml/NamespaceImport.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitNullExpression
void visitNullExpression([NullExpression](kerml/NullExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`NullExpression`](kerml/NullExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitOperatorExpression
void visitOperatorExpression([OperatorExpression](kerml/OperatorExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`OperatorExpression`](kerml/OperatorExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitOwningMembership
void visitOwningMembership([OwningMembership](kerml/OwningMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`OwningMembership`](kerml/OwningMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPackage
void visitPackage([Package](kerml/Package.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Package`](kerml/Package.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitParameterMembership
void visitParameterMembership([ParameterMembership](kerml/ParameterMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`ParameterMembership`](kerml/ParameterMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPayloadFeature
void visitPayloadFeature([PayloadFeature](kerml/PayloadFeature.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`PayloadFeature`](kerml/PayloadFeature.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitPredicate
void visitPredicate([Predicate](kerml/Predicate.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Predicate`](kerml/Predicate.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRedefinition
void visitRedefinition([Redefinition](kerml/Redefinition.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Redefinition`](kerml/Redefinition.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitReferenceSubsetting
void visitReferenceSubsetting([ReferenceSubsetting](kerml/ReferenceSubsetting.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`ReferenceSubsetting`](kerml/ReferenceSubsetting.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitRelationship
void visitRelationship([Relationship](kerml/Relationship.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Relationship`](kerml/Relationship.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitResultExpressionMembership
void visitResultExpressionMembership([ResultExpressionMembership](kerml/ResultExpressionMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`ResultExpressionMembership`](kerml/ResultExpressionMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitReturnParameterMembership
void visitReturnParameterMembership([ReturnParameterMembership](kerml/ReturnParameterMembership.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`ReturnParameterMembership`](kerml/ReturnParameterMembership.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSelectExpression
void visitSelectExpression([SelectExpression](kerml/SelectExpression.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`SelectExpression`](kerml/SelectExpression.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSpecialization
void visitSpecialization([Specialization](kerml/Specialization.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Specialization`](kerml/Specialization.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitStep
void visitStep([Step](kerml/Step.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Step`](kerml/Step.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitStructure
void visitStructure([Structure](kerml/Structure.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Structure`](kerml/Structure.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSubclassification
void visitSubclassification([Subclassification](kerml/Subclassification.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Subclassification`](kerml/Subclassification.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSubsetting
void visitSubsetting([Subsetting](kerml/Subsetting.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Subsetting`](kerml/Subsetting.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSuccession
void visitSuccession([Succession](kerml/Succession.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Succession`](kerml/Succession.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitSuccessionFlow
void visitSuccessionFlow([SuccessionFlow](kerml/SuccessionFlow.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`SuccessionFlow`](kerml/SuccessionFlow.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitTextualRepresentation
void visitTextualRepresentation([TextualRepresentation](kerml/TextualRepresentation.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`TextualRepresentation`](kerml/TextualRepresentation.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitType
void visitType([Type](kerml/Type.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Type`](kerml/Type.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitTypeFeaturing
void visitTypeFeaturing([TypeFeaturing](kerml/TypeFeaturing.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`TypeFeaturing`](kerml/TypeFeaturing.html).
Parameters:
`element` - element to visit
`context` - context of visitor
visitUnioning
void visitUnioning([Unioning](kerml/Unioning.html) element,
 [C](KerMLModelVisitor.html) context)
Visitor method for [`Unioning`](kerml/Unioning.html).
Parameters:
`element` - element to visit
`context` - context of visitor
createVisitorContext
default [C](KerMLModelVisitor.html) createVisitorContext()
Creates a new visitor context.
Returns:
A new instance of `KerMLVisitorContextImpl`.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Interface KerMLModelVisitor">Interface KerMLModelVisitor&lt;C extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>C</code> - The type of the visitor context, which must extend <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLVisitorContext</code></a>.</dd>
</dl>
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="KerMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelHierarchyVisitor</a>&lt;C&gt;</code>, <code><a href="../../sysml/model/SysMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelHierarchyVisitor</a>&lt;C&gt;</code>, <code><a href="../../sysml/model/SysMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelVisitor</a>&lt;C&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">KerMLModelVisitor&lt;C extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</span><span class="extends-implements">
extends <a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></span></div>
<div class="block">A visitor interface for traversing the KerML model.
 <p>
 This interface extends <a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml"><code>AbstractVisitor</code></a> and provides methods to visit various elements
 in the KerML model, including classes, packages, relationships, and more. It is designed to
 work with a visitor context of type <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLVisitorContext</code></a>.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml"><code>AbstractVisitor</code></a></li>
<li><a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLVisitorContext</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createVisitorContext()">createVisitorContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Creates a new visitor context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">visitAnnotatingElement</a><wbr/>(<a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AnnotatingElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">visitAnnotation</a><wbr/>(<a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">visitAssociation</a><wbr/>(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Association</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">visitAssociationStructure</a><wbr/>(<a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AssociationStructure</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">visitBehavior</a><wbr/>(<a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">visitBindingConnector</a><wbr/>(<a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>BindingConnector</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">visitBooleanExpression</a><wbr/>(<a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>BooleanExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">visitClass</a><wbr/>(<a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Class</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">visitClassifier</a><wbr/>(<a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Classifier</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">visitCollectExpression</a><wbr/>(<a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>CollectExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">visitComment</a><wbr/>(<a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Comment</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">visitConjugation</a><wbr/>(<a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Conjugation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">visitConnector</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Connector</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">visitConstructorExpression</a><wbr/>(<a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ConstructorExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">visitCrossSubsetting</a><wbr/>(<a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>CrossSubsetting</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">visitDataType</a><wbr/>(<a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>DataType</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">visitDependency</a><wbr/>(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Dependency</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">visitDifferencing</a><wbr/>(<a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Differencing</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">visitDisjoining</a><wbr/>(<a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Disjoining</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">visitDocumentation</a><wbr/>(<a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Documentation</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">visitElement</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">visitElementFilterMembership</a><wbr/>(<a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ElementFilterMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">visitEndFeatureMembership</a><wbr/>(<a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>EndFeatureMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">visitExpression</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">visitFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">visitFeatureChainExpression</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChainExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">visitFeatureChaining</a><wbr/>(<a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChaining</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">visitFeatureInverting</a><wbr/>(<a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureInverting</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">visitFeatureMembership</a><wbr/>(<a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">visitFeatureReferenceExpression</a><wbr/>(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">visitFeatureTyping</a><wbr/>(<a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureTyping</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">visitFeatureValue</a><wbr/>(<a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureValue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">visitFlow</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Flow</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">visitFlowEnd</a><wbr/>(<a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FlowEnd</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">visitFunction</a><wbr/>(<a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Function</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">visitImport</a><wbr/>(<a href="kerml/Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Import</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">visitIndexExpression</a><wbr/>(<a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>IndexExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">visitInstantiationExpression</a><wbr/>(<a href="kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InstantiationExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">visitInteraction</a><wbr/>(<a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Interaction</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">visitIntersecting</a><wbr/>(<a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Intersecting</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">visitInvariant</a><wbr/>(<a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Invariant</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">visitInvocationExpression</a><wbr/>(<a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">visitLibraryPackage</a><wbr/>(<a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LibraryPackage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">visitLiteralBoolean</a><wbr/>(<a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralBoolean</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">visitLiteralExpression</a><wbr/>(<a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">visitLiteralInfinity</a><wbr/>(<a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralInfinity</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">visitLiteralInteger</a><wbr/>(<a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralInteger</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">visitLiteralRational</a><wbr/>(<a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralRational</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">visitLiteralString</a><wbr/>(<a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralString</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">visitMembership</a><wbr/>(<a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Membership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">visitMembershipImport</a><wbr/>(<a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MembershipImport</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">visitMetaclass</a><wbr/>(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Metaclass</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">visitMetadataAccessExpression</a><wbr/>(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataAccessExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">visitMetadataFeature</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">visitMultiplicity</a><wbr/>(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Multiplicity</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">visitMultiplicityRange</a><wbr/>(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MultiplicityRange</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">visitNamespace</a><wbr/>(<a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">visitNamespaceImport</a><wbr/>(<a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>NamespaceImport</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">visitNullExpression</a><wbr/>(<a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>NullExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">visitOperatorExpression</a><wbr/>(<a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OperatorExpression</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">visitOwningMembership</a><wbr/>(<a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OwningMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">visitPackage</a><wbr/>(<a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Package</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">visitParameterMembership</a><wbr/>(<a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ParameterMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">visitPayloadFeature</a><wbr/>(<a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>PayloadFeature</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">visitPredicate</a><wbr/>(<a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Predicate</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">visitRedefinition</a><wbr/>(<a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Redefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">visitReferenceSubsetting</a><wbr/>(<a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ReferenceSubsetting</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">visitRelationship</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Relationship</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">visitResultExpressionMembership</a><wbr/>(<a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ResultExpressionMembership</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">visitReturnParameterMembership</a><wbr/>(<a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ReturnParameterMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">visitSelectExpression</a><wbr/>(<a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>SelectExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">visitSpecialization</a><wbr/>(<a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Specialization</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">visitStep</a><wbr/>(<a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">visitStructure</a><wbr/>(<a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Structure</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">visitSubclassification</a><wbr/>(<a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subclassification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">visitSubsetting</a><wbr/>(<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">visitSuccession</a><wbr/>(<a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Succession</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">visitSuccessionFlow</a><wbr/>(<a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>SuccessionFlow</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">visitTextualRepresentation</a><wbr/>(<a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>TextualRepresentation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">visitType</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Type</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">visitTypeFeaturing</a><wbr/>(<a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>TypeFeaturing</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">visitUnioning</a><wbr/>(<a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Visitor method for <a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Unioning</code></a>.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">
<h3 id="visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAnnotatingElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAnnotatingElement</span><wbr/><span class="parameters">(<a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AnnotatingElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">
<h3 id="visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAnnotation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAnnotation</span><wbr/><span class="parameters">(<a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">
<h3 id="visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAssociation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAssociation</span><wbr/><span class="parameters">(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Association</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">
<h3 id="visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAssociationStructure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitAssociationStructure</span><wbr/><span class="parameters">(<a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AssociationStructure</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">
<h3 id="visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBehavior</span><wbr/><span class="parameters">(<a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">
<h3 id="visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitBindingConnector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBindingConnector</span><wbr/><span class="parameters">(<a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>BindingConnector</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">
<h3 id="visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitBooleanExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitBooleanExpression</span><wbr/><span class="parameters">(<a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>BooleanExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">
<h3 id="visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitClass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClass</span><wbr/><span class="parameters">(<a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Class</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">
<h3 id="visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitClassifier</span><wbr/><span class="parameters">(<a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Classifier</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">
<h3 id="visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitCollectExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCollectExpression</span><wbr/><span class="parameters">(<a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>CollectExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">
<h3 id="visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitComment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitComment</span><wbr/><span class="parameters">(<a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Comment</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">
<h3 id="visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitConjugation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConjugation</span><wbr/><span class="parameters">(<a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Conjugation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">
<h3 id="visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitConnector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConnector</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Connector</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">
<h3 id="visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitConstructorExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitConstructorExpression</span><wbr/><span class="parameters">(<a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ConstructorExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">
<h3 id="visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitCrossSubsetting</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitCrossSubsetting</span><wbr/><span class="parameters">(<a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>CrossSubsetting</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">
<h3 id="visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDataType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDataType</span><wbr/><span class="parameters">(<a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>DataType</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">
<h3 id="visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDependency</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDependency</span><wbr/><span class="parameters">(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Dependency</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">
<h3 id="visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDifferencing</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDifferencing</span><wbr/><span class="parameters">(<a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Differencing</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">
<h3 id="visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDisjoining</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDisjoining</span><wbr/><span class="parameters">(<a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Disjoining</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">
<h3 id="visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDocumentation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitDocumentation</span><wbr/><span class="parameters">(<a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Documentation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">
<h3 id="visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitElement</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">
<h3 id="visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitElementFilterMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitElementFilterMembership</span><wbr/><span class="parameters">(<a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ElementFilterMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">
<h3 id="visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitEndFeatureMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitEndFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>EndFeatureMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">
<h3 id="visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitExpression</span><wbr/><span class="parameters">(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">
<h3 id="visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">
<h3 id="visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureChainExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureChainExpression</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChainExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">
<h3 id="visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureChaining</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureChaining</span><wbr/><span class="parameters">(<a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChaining</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">
<h3 id="visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureInverting</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureInverting</span><wbr/><span class="parameters">(<a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureInverting</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">
<h3 id="visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">
<h3 id="visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureReferenceExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureReferenceExpression</span><wbr/><span class="parameters">(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">
<h3 id="visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureTyping</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureTyping</span><wbr/><span class="parameters">(<a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureTyping</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">
<h3 id="visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFeatureValue</span><wbr/><span class="parameters">(<a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">
<h3 id="visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFlow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFlow</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Flow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">
<h3 id="visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFlowEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFlowEnd</span><wbr/><span class="parameters">(<a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FlowEnd</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">
<h3 id="visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFunction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitFunction</span><wbr/><span class="parameters">(<a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Function</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">
<h3 id="visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitImport</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitImport</span><wbr/><span class="parameters">(<a href="kerml/Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Import</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">
<h3 id="visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitIndexExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitIndexExpression</span><wbr/><span class="parameters">(<a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>IndexExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">
<h3 id="visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInstantiationExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInstantiationExpression</span><wbr/><span class="parameters">(<a href="kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InstantiationExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">
<h3 id="visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInteraction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInteraction</span><wbr/><span class="parameters">(<a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Interaction</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">
<h3 id="visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitIntersecting</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitIntersecting</span><wbr/><span class="parameters">(<a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Intersecting</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">
<h3 id="visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInvariant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInvariant</span><wbr/><span class="parameters">(<a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Invariant</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">
<h3 id="visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInvocationExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitInvocationExpression</span><wbr/><span class="parameters">(<a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">
<h3 id="visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLibraryPackage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLibraryPackage</span><wbr/><span class="parameters">(<a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LibraryPackage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">
<h3 id="visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralBoolean</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralBoolean</span><wbr/><span class="parameters">(<a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralBoolean</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">
<h3 id="visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralExpression</span><wbr/><span class="parameters">(<a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">
<h3 id="visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralInfinity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralInfinity</span><wbr/><span class="parameters">(<a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralInfinity</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">
<h3 id="visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralInteger</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralInteger</span><wbr/><span class="parameters">(<a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralInteger</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">
<h3 id="visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralRational</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralRational</span><wbr/><span class="parameters">(<a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralRational</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">
<h3 id="visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralString</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitLiteralString</span><wbr/><span class="parameters">(<a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralString</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">
<h3 id="visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMembership</span><wbr/><span class="parameters">(<a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Membership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">
<h3 id="visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMembershipImport</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMembershipImport</span><wbr/><span class="parameters">(<a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MembershipImport</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">
<h3 id="visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMetaclass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMetaclass</span><wbr/><span class="parameters">(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Metaclass</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">
<h3 id="visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMetadataAccessExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMetadataAccessExpression</span><wbr/><span class="parameters">(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataAccessExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">
<h3 id="visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMetadataFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMetadataFeature</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">
<h3 id="visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMultiplicity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMultiplicity</span><wbr/><span class="parameters">(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Multiplicity</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">
<h3 id="visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMultiplicityRange</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitMultiplicityRange</span><wbr/><span class="parameters">(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MultiplicityRange</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">
<h3 id="visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNamespace</span><wbr/><span class="parameters">(<a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">
<h3 id="visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitNamespaceImport</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNamespaceImport</span><wbr/><span class="parameters">(<a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>NamespaceImport</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">
<h3 id="visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitNullExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitNullExpression</span><wbr/><span class="parameters">(<a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>NullExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">
<h3 id="visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitOperatorExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOperatorExpression</span><wbr/><span class="parameters">(<a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OperatorExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">
<h3 id="visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitOwningMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitOwningMembership</span><wbr/><span class="parameters">(<a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OwningMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">
<h3 id="visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitPackage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPackage</span><wbr/><span class="parameters">(<a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Package</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">
<h3 id="visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitParameterMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitParameterMembership</span><wbr/><span class="parameters">(<a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ParameterMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">
<h3 id="visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitPayloadFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPayloadFeature</span><wbr/><span class="parameters">(<a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>PayloadFeature</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">
<h3 id="visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitPredicate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitPredicate</span><wbr/><span class="parameters">(<a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Predicate</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">
<h3 id="visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitRedefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRedefinition</span><wbr/><span class="parameters">(<a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Redefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">
<h3 id="visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitReferenceSubsetting</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReferenceSubsetting</span><wbr/><span class="parameters">(<a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ReferenceSubsetting</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">
<h3 id="visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitRelationship</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitRelationship</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Relationship</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">
<h3 id="visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitResultExpressionMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitResultExpressionMembership</span><wbr/><span class="parameters">(<a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ResultExpressionMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">
<h3 id="visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitReturnParameterMembership</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitReturnParameterMembership</span><wbr/><span class="parameters">(<a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ReturnParameterMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">
<h3 id="visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSelectExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSelectExpression</span><wbr/><span class="parameters">(<a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>SelectExpression</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">
<h3 id="visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSpecialization</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSpecialization</span><wbr/><span class="parameters">(<a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Specialization</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">
<h3 id="visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitStep</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStep</span><wbr/><span class="parameters">(<a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">
<h3 id="visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitStructure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitStructure</span><wbr/><span class="parameters">(<a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Structure</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">
<h3 id="visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSubclassification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSubclassification</span><wbr/><span class="parameters">(<a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subclassification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">
<h3 id="visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSubsetting</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSubsetting</span><wbr/><span class="parameters">(<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">
<h3 id="visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSuccession</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSuccession</span><wbr/><span class="parameters">(<a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Succession</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">
<h3 id="visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSuccessionFlow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitSuccessionFlow</span><wbr/><span class="parameters">(<a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>SuccessionFlow</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">
<h3 id="visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitTextualRepresentation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTextualRepresentation</span><wbr/><span class="parameters">(<a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>TextualRepresentation</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">
<h3 id="visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitType</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Type</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">
<h3 id="visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitTypeFeaturing</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitTypeFeaturing</span><wbr/><span class="parameters">(<a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>TypeFeaturing</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">
<h3 id="visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitUnioning</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visitUnioning</span><wbr/><span class="parameters">(<a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a> element,
 <a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a> context)</span></div>
<div class="block">Visitor method for <a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Unioning</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to visit</dd>
<dd><code>context</code> - context of visitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createVisitorContext()">
<h3>createVisitorContext</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="KerMLModelVisitor.html" title="type parameter in KerMLModelVisitor">C</a></span> <span class="element-name">createVisitorContext</span>()</div>
<div class="block">Creates a new visitor context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>A new instance of <code>KerMLVisitorContextImpl</code>.</dd>
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
