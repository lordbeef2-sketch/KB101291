# JAVA OPENAPI: KerMLModelHierarchyVisitor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/KerMLModelHierarchyVisitor.html
- source_path: `com/dassault_systemes/modeler/kerml/model/KerMLModelHierarchyVisitor.html`
- source_sha256: `68faf1107b23cc13470fb40cd89e0494fe1b0a3150b898a67b6ff7c316f1c0ab`
- captured_utc: `2026-07-14T16:44:48.246846+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Interface KerMLModelHierarchyVisitor<C extends [KerMLVisitorContext](KerMLVisitorContext.html)>

Type Parameters:
`C` - The type of the visitor context, which must extend [`KerMLVisitorContext`](KerMLVisitorContext.html).

All Superinterfaces:
`[AbstractVisitor](../../../../nomagic/magicdraw/uml/AbstractVisitor.html)`, `[KerMLModelVisitor](KerMLModelVisitor.html)<C>`

All Known Subinterfaces:
`[SysMLModelHierarchyVisitor](../../sysml/model/SysMLModelHierarchyVisitor.html)<C>`

@OpenApiAllpublic interfaceKerMLModelHierarchyVisitor<C extends [KerMLVisitorContext](KerMLVisitorContext.html)>extends [KerMLModelVisitor](KerMLModelVisitor.html)<C>

A visitor interface for traversing the KerML model hierarchy.
 This interface extends [`KerMLModelVisitor`](KerMLModelVisitor.html) and provides methods to visit various elements
 in the KerML model, including classes, packages, relationships, and more. It also includes
 methods to check the EPackage and determine if elements are acceptable for the visitor.

See Also:
[`KerMLModelVisitor`](KerMLModelVisitor.html)
[`KerMLVisitorContext`](KerMLVisitorContext.html)
[`KerMLPackage`](kerml/KerMLPackage.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default org.eclipse.emf.ecore.EPackage`
`[getEPackage](#getEPackage())()`
Gets the EPackage visitor is suited for.
`default boolean`
`[isAcceptable](#isAcceptable(org.eclipse.emf.ecore.EPackage))(org.eclipse.emf.ecore.EPackage ePackage)`
Checks if given EPackage elements are acceptable by the visitor.
`default void`
`[visitAnnotatingElement](#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C))([AnnotatingElement](kerml/AnnotatingElement.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an AnnotatingElement in the KerML model.
`default void`
`[visitAnnotation](#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C))([Annotation](kerml/Annotation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Annotation in the KerML model.
`default void`
`[visitAssociation](#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C))([Association](kerml/Association.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Association in the KerML model.
`default void`
`[visitAssociationStructure](#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C))([AssociationStructure](kerml/AssociationStructure.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an AssociationStructure in the KerML model.
`default void`
`[visitBehavior](#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C))([Behavior](kerml/Behavior.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Behavior in the KerML model.
`default void`
`[visitBindingConnector](#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C))([BindingConnector](kerml/BindingConnector.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a BindingConnector in the KerML model.
`default void`
`[visitBooleanExpression](#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C))([BooleanExpression](kerml/BooleanExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a BooleanExpression in the KerML model.
`default void`
`[visitClass](#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C))([Class](kerml/Class.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Class in the KerML model.
`default void`
`[visitClassifier](#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C))([Classifier](kerml/Classifier.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Classifier in the KerML model.
`default void`
`[visitCollectExpression](#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C))([CollectExpression](kerml/CollectExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a CollectExpression in the KerML model.
`default void`
`[visitComment](#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C))([Comment](kerml/Comment.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Comment in the KerML model.
`default void`
`[visitConjugation](#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C))([Conjugation](kerml/Conjugation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Conjugation in the KerML model.
`default void`
`[visitConnector](#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C))([Connector](kerml/Connector.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Connector in the KerML model.
`default void`
`[visitConstructorExpression](#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C))([ConstructorExpression](kerml/ConstructorExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a ConstructorExpression in the KerML model.
`default void`
`[visitCrossSubsetting](#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C))([CrossSubsetting](kerml/CrossSubsetting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a CrossSubsetting in the KerML model.
`default void`
`[visitDataType](#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C))([DataType](kerml/DataType.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a DataType in the KerML model.
`default void`
`[visitDependency](#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C))([Dependency](kerml/Dependency.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Dependency in the KerML model.
`default void`
`[visitDifferencing](#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C))([Differencing](kerml/Differencing.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Differencing in the KerML model.
`default void`
`[visitDisjoining](#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C))([Disjoining](kerml/Disjoining.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Disjoining in the KerML model.
`default void`
`[visitDocumentation](#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C))([Documentation](kerml/Documentation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Documentation in the KerML model.
`default void`
`[visitElement](#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C))([Element](kerml/Element.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Element in the KerML model.
`default void`
`[visitElementFilterMembership](#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C))([ElementFilterMembership](kerml/ElementFilterMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an ElementFilterMembership in the KerML model.
`default void`
`[visitEndFeatureMembership](#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C))([EndFeatureMembership](kerml/EndFeatureMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an EndFeatureMembership in the KerML model.
`default void`
`[visitExpression](#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C))([Expression](kerml/Expression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Expression in the KerML model.
`default void`
`[visitFeature](#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C))([Feature](kerml/Feature.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Feature in the KerML model.
`default void`
`[visitFeatureChainExpression](#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C))([FeatureChainExpression](kerml/FeatureChainExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureChainExpression in the KerML model.
`default void`
`[visitFeatureChaining](#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C))([FeatureChaining](kerml/FeatureChaining.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureChaining in the KerML model.
`default void`
`[visitFeatureInverting](#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C))([FeatureInverting](kerml/FeatureInverting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureInverting in the KerML model.
`default void`
`[visitFeatureMembership](#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C))([FeatureMembership](kerml/FeatureMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureMembership in the KerML model.
`default void`
`[visitFeatureReferenceExpression](#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C))([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureReferenceExpression in the KerML model.
`default void`
`[visitFeatureTyping](#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C))([FeatureTyping](kerml/FeatureTyping.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureTyping in the KerML model.
`default void`
`[visitFeatureValue](#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C))([FeatureValue](kerml/FeatureValue.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FeatureValue in the KerML model.
`default void`
`[visitFlow](#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C))([Flow](kerml/Flow.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Flow in the KerML model.
`default void`
`[visitFlowEnd](#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C))([FlowEnd](kerml/FlowEnd.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a FlowEnd in the KerML model.
`default void`
`[visitFunction](#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C))([Function](kerml/Function.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Function in the KerML model.
`default void`
`[visitImport](#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C))([Import](kerml/Import.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Import in the KerML model.
`default void`
`[visitIndexExpression](#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C))([IndexExpression](kerml/IndexExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an IndexExpression in the KerML model.
`default void`
`[visitInstantiationExpression](#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C))([InstantiationExpression](kerml/InstantiationExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an InstantiationExpression in the KerML model.
`default void`
`[visitInteraction](#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C))([Interaction](kerml/Interaction.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Interaction in the KerML model.
`default void`
`[visitIntersecting](#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C))([Intersecting](kerml/Intersecting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Intersecting in the KerML model.
`default void`
`[visitInvariant](#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C))([Invariant](kerml/Invariant.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an Invariant in the KerML model.
`default void`
`[visitInvocationExpression](#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C))([InvocationExpression](kerml/InvocationExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an InvocationExpression in the KerML model.
`default void`
`[visitLibraryPackage](#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C))([LibraryPackage](kerml/LibraryPackage.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LibraryPackage in the KerML model.
`default void`
`[visitLiteralBoolean](#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C))([LiteralBoolean](kerml/LiteralBoolean.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LiteralBoolean in the KerML model.
`default void`
`[visitLiteralExpression](#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C))([LiteralExpression](kerml/LiteralExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LiteralExpression in the KerML model.
`default void`
`[visitLiteralInfinity](#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C))([LiteralInfinity](kerml/LiteralInfinity.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LiteralInfinity in the KerML model.
`default void`
`[visitLiteralInteger](#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C))([LiteralInteger](kerml/LiteralInteger.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LiteralInteger in the KerML model.
`default void`
`[visitLiteralRational](#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C))([LiteralRational](kerml/LiteralRational.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LiteralRational in the KerML model.
`default void`
`[visitLiteralString](#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C))([LiteralString](kerml/LiteralString.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a LiteralString in the KerML model.
`default void`
`[visitMembership](#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C))([Membership](kerml/Membership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Membership in the KerML model.
`default void`
`[visitMembershipImport](#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C))([MembershipImport](kerml/MembershipImport.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a MembershipImport in the KerML model.
`default void`
`[visitMetaclass](#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C))([Metaclass](kerml/Metaclass.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Metaclass in the KerML model.
`default void`
`[visitMetadataAccessExpression](#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C))([MetadataAccessExpression](kerml/MetadataAccessExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a MetadataAccessExpression in the KerML model.
`default void`
`[visitMetadataFeature](#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C))([MetadataFeature](kerml/MetadataFeature.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a MetadataFeature in the KerML model.
`default void`
`[visitMultiplicity](#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C))([Multiplicity](kerml/Multiplicity.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Multiplicity in the KerML model.
`default void`
`[visitMultiplicityRange](#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C))([MultiplicityRange](kerml/MultiplicityRange.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a MultiplicityRange in the KerML model.
`default void`
`[visitNamespace](#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C))([Namespace](kerml/Namespace.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Namespace in the KerML model.
`default void`
`[visitNamespaceImport](#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C))([NamespaceImport](kerml/NamespaceImport.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a NamespaceImport in the KerML model.
`default void`
`[visitNullExpression](#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C))([NullExpression](kerml/NullExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a NullExpression in the KerML model.
`default void`
`[visitOperatorExpression](#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C))([OperatorExpression](kerml/OperatorExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an OperatorExpression in the KerML model.
`default void`
`[visitOwningMembership](#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C))([OwningMembership](kerml/OwningMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits an OwningMembership in the KerML model.
`default void`
`[visitPackage](#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C))([Package](kerml/Package.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Package in the KerML model.
`default void`
`[visitParameterMembership](#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C))([ParameterMembership](kerml/ParameterMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a ParameterMembership in the KerML model.
`default void`
`[visitPayloadFeature](#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C))([PayloadFeature](kerml/PayloadFeature.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a PayloadFeature in the KerML model.
`default void`
`[visitPredicate](#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C))([Predicate](kerml/Predicate.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Predicate in the KerML model.
`default void`
`[visitRedefinition](#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C))([Redefinition](kerml/Redefinition.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Redefinition in the KerML model.
`default void`
`[visitReferenceSubsetting](#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C))([ReferenceSubsetting](kerml/ReferenceSubsetting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a ReferenceSubsetting in the KerML model.
`default void`
`[visitRelationship](#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C))([Relationship](kerml/Relationship.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Relationship in the KerML model.
`default void`
`[visitResultExpressionMembership](#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C))([ResultExpressionMembership](kerml/ResultExpressionMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a ResultExpressionMembership in the KerML model.
`default void`
`[visitReturnParameterMembership](#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C))([ReturnParameterMembership](kerml/ReturnParameterMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a ReturnParameterMembership in the KerML model.
`default void`
`[visitSelectExpression](#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C))([SelectExpression](kerml/SelectExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a SelectExpression in the KerML model.
`default void`
`[visitSpecialization](#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C))([Specialization](kerml/Specialization.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Specialization in the KerML model.
`default void`
`[visitStep](#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C))([Step](kerml/Step.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Step in the KerML model.
`default void`
`[visitStructure](#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C))([Structure](kerml/Structure.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Structure in the KerML model.
`default void`
`[visitSubclassification](#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C))([Subclassification](kerml/Subclassification.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Subclassification in the KerML model.
`default void`
`[visitSubsetting](#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C))([Subsetting](kerml/Subsetting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Subsetting in the KerML model.
`default void`
`[visitSuccession](#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C))([Succession](kerml/Succession.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Succession in the KerML model.
`default void`
`[visitSuccessionFlow](#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C))([SuccessionFlow](kerml/SuccessionFlow.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a SuccessionFlow in the KerML model.
`default void`
`[visitTextualRepresentation](#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C))([TextualRepresentation](kerml/TextualRepresentation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a TextualRepresentation in the KerML model.
`default void`
`[visitType](#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C))([Type](kerml/Type.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Type in the KerML model.
`default void`
`[visitTypeFeaturing](#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C))([TypeFeaturing](kerml/TypeFeaturing.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a TypeFeaturing in the KerML model.
`default void`
`[visitUnioning](#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C))([Unioning](kerml/Unioning.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)`
Visits a Unioning in the KerML model.
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLModelVisitor](KerMLModelVisitor.html)
`[createVisitorContext](KerMLModelVisitor.html#createVisitorContext())`

============ METHOD DETAIL ========== 
Method Details
getEPackage
default org.eclipse.emf.ecore.EPackage getEPackage()
Gets the EPackage visitor is suited for.
Returns:
The EPackage instance.
isAcceptable
default boolean isAcceptable(org.eclipse.emf.ecore.EPackage ePackage)
Checks if given EPackage elements are acceptable by the visitor.
Parameters:
`ePackage` - The EPackage to check.
Returns:
True if the EPackage is acceptable, false otherwise.
visitAnnotatingElement
default void visitAnnotatingElement([AnnotatingElement](kerml/AnnotatingElement.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an AnnotatingElement in the KerML model.
Specified by:
`[visitAnnotatingElement](KerMLModelVisitor.html#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The AnnotatingElement to visit.
`context` - The visitor context.
visitAnnotation
default void visitAnnotation([Annotation](kerml/Annotation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Annotation in the KerML model.
Specified by:
`[visitAnnotation](KerMLModelVisitor.html#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Annotation to visit.
`context` - The visitor context.
visitAssociation
default void visitAssociation([Association](kerml/Association.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Association in the KerML model.
Specified by:
`[visitAssociation](KerMLModelVisitor.html#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Association to visit.
`context` - The visitor context.
visitAssociationStructure
default void visitAssociationStructure([AssociationStructure](kerml/AssociationStructure.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an AssociationStructure in the KerML model.
Specified by:
`[visitAssociationStructure](KerMLModelVisitor.html#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The AssociationStructure to visit.
`context` - The visitor context.
visitBehavior
default void visitBehavior([Behavior](kerml/Behavior.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Behavior in the KerML model.
Specified by:
`[visitBehavior](KerMLModelVisitor.html#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Behavior to visit.
`context` - The visitor context.
visitBindingConnector
default void visitBindingConnector([BindingConnector](kerml/BindingConnector.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a BindingConnector in the KerML model.
Specified by:
`[visitBindingConnector](KerMLModelVisitor.html#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The BindingConnector to visit.
`context` - The visitor context.
visitBooleanExpression
default void visitBooleanExpression([BooleanExpression](kerml/BooleanExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a BooleanExpression in the KerML model.
Specified by:
`[visitBooleanExpression](KerMLModelVisitor.html#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The BooleanExpression to visit.
`context` - The visitor context.
visitClass
default void visitClass([Class](kerml/Class.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Class in the KerML model.
Specified by:
`[visitClass](KerMLModelVisitor.html#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Class to visit.
`context` - The visitor context.
visitClassifier
default void visitClassifier([Classifier](kerml/Classifier.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Classifier in the KerML model.
Specified by:
`[visitClassifier](KerMLModelVisitor.html#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Classifier to visit.
`context` - The visitor context.
visitCollectExpression
default void visitCollectExpression([CollectExpression](kerml/CollectExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a CollectExpression in the KerML model.
Specified by:
`[visitCollectExpression](KerMLModelVisitor.html#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The CollectExpression to visit.
`context` - The visitor context.
visitComment
default void visitComment([Comment](kerml/Comment.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Comment in the KerML model.
Specified by:
`[visitComment](KerMLModelVisitor.html#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Comment to visit.
`context` - The visitor context.
visitConjugation
default void visitConjugation([Conjugation](kerml/Conjugation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Conjugation in the KerML model.
Specified by:
`[visitConjugation](KerMLModelVisitor.html#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Conjugation to visit.
`context` - The visitor context.
visitConnector
default void visitConnector([Connector](kerml/Connector.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Connector in the KerML model.
Specified by:
`[visitConnector](KerMLModelVisitor.html#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Connector to visit.
`context` - The visitor context.
visitConstructorExpression
default void visitConstructorExpression([ConstructorExpression](kerml/ConstructorExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a ConstructorExpression in the KerML model.
Specified by:
`[visitConstructorExpression](KerMLModelVisitor.html#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The ConstructorExpression to visit.
`context` - The visitor context.
visitCrossSubsetting
default void visitCrossSubsetting([CrossSubsetting](kerml/CrossSubsetting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a CrossSubsetting in the KerML model.
Specified by:
`[visitCrossSubsetting](KerMLModelVisitor.html#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The CrossSubsetting to visit.
`context` - The visitor context.
visitDataType
default void visitDataType([DataType](kerml/DataType.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a DataType in the KerML model.
Specified by:
`[visitDataType](KerMLModelVisitor.html#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The DataType to visit.
`context` - The visitor context.
visitDependency
default void visitDependency([Dependency](kerml/Dependency.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Dependency in the KerML model.
Specified by:
`[visitDependency](KerMLModelVisitor.html#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Dependency to visit.
`context` - The visitor context.
visitDifferencing
default void visitDifferencing([Differencing](kerml/Differencing.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Differencing in the KerML model.
Specified by:
`[visitDifferencing](KerMLModelVisitor.html#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Differencing to visit.
`context` - The visitor context.
visitDisjoining
default void visitDisjoining([Disjoining](kerml/Disjoining.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Disjoining in the KerML model.
Specified by:
`[visitDisjoining](KerMLModelVisitor.html#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Disjoining to visit.
`context` - The visitor context.
visitDocumentation
default void visitDocumentation([Documentation](kerml/Documentation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Documentation in the KerML model.
Specified by:
`[visitDocumentation](KerMLModelVisitor.html#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Documentation to visit.
`context` - The visitor context.
visitElement
default void visitElement([Element](kerml/Element.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Element in the KerML model.
Specified by:
`[visitElement](KerMLModelVisitor.html#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Element to visit.
`context` - The visitor context.
visitElementFilterMembership
default void visitElementFilterMembership([ElementFilterMembership](kerml/ElementFilterMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an ElementFilterMembership in the KerML model.
Specified by:
`[visitElementFilterMembership](KerMLModelVisitor.html#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The ElementFilterMembership to visit.
`context` - The visitor context.
visitEndFeatureMembership
default void visitEndFeatureMembership([EndFeatureMembership](kerml/EndFeatureMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an EndFeatureMembership in the KerML model.
Specified by:
`[visitEndFeatureMembership](KerMLModelVisitor.html#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The EndFeatureMembership to visit.
`context` - The visitor context.
visitExpression
default void visitExpression([Expression](kerml/Expression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Expression in the KerML model.
Specified by:
`[visitExpression](KerMLModelVisitor.html#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Expression to visit.
`context` - The visitor context.
visitFeature
default void visitFeature([Feature](kerml/Feature.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Feature in the KerML model.
Specified by:
`[visitFeature](KerMLModelVisitor.html#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Feature to visit.
`context` - The visitor context.
visitFeatureChainExpression
default void visitFeatureChainExpression([FeatureChainExpression](kerml/FeatureChainExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureChainExpression in the KerML model.
Specified by:
`[visitFeatureChainExpression](KerMLModelVisitor.html#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureChainExpression to visit.
`context` - The visitor context.
visitFeatureChaining
default void visitFeatureChaining([FeatureChaining](kerml/FeatureChaining.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureChaining in the KerML model.
Specified by:
`[visitFeatureChaining](KerMLModelVisitor.html#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureChaining to visit.
`context` - The visitor context.
visitFeatureInverting
default void visitFeatureInverting([FeatureInverting](kerml/FeatureInverting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureInverting in the KerML model.
Specified by:
`[visitFeatureInverting](KerMLModelVisitor.html#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureInverting to visit.
`context` - The visitor context.
visitFeatureMembership
default void visitFeatureMembership([FeatureMembership](kerml/FeatureMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureMembership in the KerML model.
Specified by:
`[visitFeatureMembership](KerMLModelVisitor.html#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureMembership to visit.
`context` - The visitor context.
visitFeatureReferenceExpression
default void visitFeatureReferenceExpression([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureReferenceExpression in the KerML model.
Specified by:
`[visitFeatureReferenceExpression](KerMLModelVisitor.html#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureReferenceExpression to visit.
`context` - The visitor context.
visitFeatureTyping
default void visitFeatureTyping([FeatureTyping](kerml/FeatureTyping.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureTyping in the KerML model.
Specified by:
`[visitFeatureTyping](KerMLModelVisitor.html#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureTyping to visit.
`context` - The visitor context.
visitFeatureValue
default void visitFeatureValue([FeatureValue](kerml/FeatureValue.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FeatureValue in the KerML model.
Specified by:
`[visitFeatureValue](KerMLModelVisitor.html#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FeatureValue to visit.
`context` - The visitor context.
visitFlow
default void visitFlow([Flow](kerml/Flow.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Flow in the KerML model.
Specified by:
`[visitFlow](KerMLModelVisitor.html#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Flow to visit.
`context` - The visitor context.
visitFlowEnd
default void visitFlowEnd([FlowEnd](kerml/FlowEnd.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a FlowEnd in the KerML model.
Specified by:
`[visitFlowEnd](KerMLModelVisitor.html#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The FlowEnd to visit.
`context` - The visitor context.
visitFunction
default void visitFunction([Function](kerml/Function.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Function in the KerML model.
Specified by:
`[visitFunction](KerMLModelVisitor.html#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Function to visit.
`context` - The visitor context.
visitImport
default void visitImport([Import](kerml/Import.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Import in the KerML model.
Specified by:
`[visitImport](KerMLModelVisitor.html#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Import to visit.
`context` - The visitor context.
visitIndexExpression
default void visitIndexExpression([IndexExpression](kerml/IndexExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an IndexExpression in the KerML model.
Specified by:
`[visitIndexExpression](KerMLModelVisitor.html#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The IndexExpression to visit.
`context` - The visitor context.
visitInstantiationExpression
default void visitInstantiationExpression([InstantiationExpression](kerml/InstantiationExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an InstantiationExpression in the KerML model.
Specified by:
`[visitInstantiationExpression](KerMLModelVisitor.html#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The InstantiationExpression to visit.
`context` - The visitor context.
visitInteraction
default void visitInteraction([Interaction](kerml/Interaction.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Interaction in the KerML model.
Specified by:
`[visitInteraction](KerMLModelVisitor.html#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Interaction to visit.
`context` - The visitor context.
visitIntersecting
default void visitIntersecting([Intersecting](kerml/Intersecting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Intersecting in the KerML model.
Specified by:
`[visitIntersecting](KerMLModelVisitor.html#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Intersecting to visit.
`context` - The visitor context.
visitInvariant
default void visitInvariant([Invariant](kerml/Invariant.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an Invariant in the KerML model.
Specified by:
`[visitInvariant](KerMLModelVisitor.html#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Invariant to visit.
`context` - The visitor context.
visitInvocationExpression
default void visitInvocationExpression([InvocationExpression](kerml/InvocationExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an InvocationExpression in the KerML model.
Specified by:
`[visitInvocationExpression](KerMLModelVisitor.html#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The InvocationExpression to visit.
`context` - The visitor context.
visitLibraryPackage
default void visitLibraryPackage([LibraryPackage](kerml/LibraryPackage.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LibraryPackage in the KerML model.
Specified by:
`[visitLibraryPackage](KerMLModelVisitor.html#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LibraryPackage to visit.
`context` - The visitor context.
visitLiteralBoolean
default void visitLiteralBoolean([LiteralBoolean](kerml/LiteralBoolean.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LiteralBoolean in the KerML model.
Specified by:
`[visitLiteralBoolean](KerMLModelVisitor.html#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LiteralBoolean to visit.
`context` - The visitor context.
visitLiteralExpression
default void visitLiteralExpression([LiteralExpression](kerml/LiteralExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LiteralExpression in the KerML model.
Specified by:
`[visitLiteralExpression](KerMLModelVisitor.html#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LiteralExpression to visit.
`context` - The visitor context.
visitLiteralInfinity
default void visitLiteralInfinity([LiteralInfinity](kerml/LiteralInfinity.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LiteralInfinity in the KerML model.
Specified by:
`[visitLiteralInfinity](KerMLModelVisitor.html#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LiteralInfinity to visit.
`context` - The visitor context.
visitLiteralInteger
default void visitLiteralInteger([LiteralInteger](kerml/LiteralInteger.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LiteralInteger in the KerML model.
Specified by:
`[visitLiteralInteger](KerMLModelVisitor.html#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LiteralInteger to visit.
`context` - The visitor context.
visitLiteralRational
default void visitLiteralRational([LiteralRational](kerml/LiteralRational.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LiteralRational in the KerML model.
Specified by:
`[visitLiteralRational](KerMLModelVisitor.html#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LiteralRational to visit.
`context` - The visitor context.
visitLiteralString
default void visitLiteralString([LiteralString](kerml/LiteralString.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a LiteralString in the KerML model.
Specified by:
`[visitLiteralString](KerMLModelVisitor.html#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The LiteralString to visit.
`context` - The visitor context.
visitMembership
default void visitMembership([Membership](kerml/Membership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Membership in the KerML model.
Specified by:
`[visitMembership](KerMLModelVisitor.html#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Membership to visit.
`context` - The visitor context.
visitMembershipImport
default void visitMembershipImport([MembershipImport](kerml/MembershipImport.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a MembershipImport in the KerML model.
Specified by:
`[visitMembershipImport](KerMLModelVisitor.html#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The MembershipImport to visit.
`context` - The visitor context.
visitMetaclass
default void visitMetaclass([Metaclass](kerml/Metaclass.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Metaclass in the KerML model.
Specified by:
`[visitMetaclass](KerMLModelVisitor.html#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Metaclass to visit.
`context` - The visitor context.
visitMetadataAccessExpression
default void visitMetadataAccessExpression([MetadataAccessExpression](kerml/MetadataAccessExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a MetadataAccessExpression in the KerML model.
Specified by:
`[visitMetadataAccessExpression](KerMLModelVisitor.html#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The MetadataAccessExpression to visit.
`context` - The visitor context.
visitMetadataFeature
default void visitMetadataFeature([MetadataFeature](kerml/MetadataFeature.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a MetadataFeature in the KerML model.
Specified by:
`[visitMetadataFeature](KerMLModelVisitor.html#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The MetadataFeature to visit.
`context` - The visitor context.
visitMultiplicity
default void visitMultiplicity([Multiplicity](kerml/Multiplicity.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Multiplicity in the KerML model.
Specified by:
`[visitMultiplicity](KerMLModelVisitor.html#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Multiplicity to visit.
`context` - The visitor context.
visitMultiplicityRange
default void visitMultiplicityRange([MultiplicityRange](kerml/MultiplicityRange.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a MultiplicityRange in the KerML model.
Specified by:
`[visitMultiplicityRange](KerMLModelVisitor.html#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The MultiplicityRange to visit.
`context` - The visitor context.
visitNamespace
default void visitNamespace([Namespace](kerml/Namespace.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Namespace in the KerML model.
Specified by:
`[visitNamespace](KerMLModelVisitor.html#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Namespace to visit.
`context` - The visitor context.
visitNamespaceImport
default void visitNamespaceImport([NamespaceImport](kerml/NamespaceImport.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a NamespaceImport in the KerML model.
Specified by:
`[visitNamespaceImport](KerMLModelVisitor.html#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The NamespaceImport to visit.
`context` - The visitor context.
visitNullExpression
default void visitNullExpression([NullExpression](kerml/NullExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a NullExpression in the KerML model.
Specified by:
`[visitNullExpression](KerMLModelVisitor.html#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The NullExpression to visit.
`context` - The visitor context.
visitOperatorExpression
default void visitOperatorExpression([OperatorExpression](kerml/OperatorExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an OperatorExpression in the KerML model.
Specified by:
`[visitOperatorExpression](KerMLModelVisitor.html#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The OperatorExpression to visit.
`context` - The visitor context.
visitOwningMembership
default void visitOwningMembership([OwningMembership](kerml/OwningMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits an OwningMembership in the KerML model.
Specified by:
`[visitOwningMembership](KerMLModelVisitor.html#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The OwningMembership to visit.
`context` - The visitor context.
visitPackage
default void visitPackage([Package](kerml/Package.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Package in the KerML model.
Specified by:
`[visitPackage](KerMLModelVisitor.html#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Package to visit.
`context` - The visitor context.
visitParameterMembership
default void visitParameterMembership([ParameterMembership](kerml/ParameterMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a ParameterMembership in the KerML model.
Specified by:
`[visitParameterMembership](KerMLModelVisitor.html#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The ParameterMembership to visit.
`context` - The visitor context.
visitPayloadFeature
default void visitPayloadFeature([PayloadFeature](kerml/PayloadFeature.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a PayloadFeature in the KerML model.
Specified by:
`[visitPayloadFeature](KerMLModelVisitor.html#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The PayloadFeature to visit.
`context` - The visitor context.
visitPredicate
default void visitPredicate([Predicate](kerml/Predicate.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Predicate in the KerML model.
Specified by:
`[visitPredicate](KerMLModelVisitor.html#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Predicate to visit.
`context` - The visitor context.
visitRedefinition
default void visitRedefinition([Redefinition](kerml/Redefinition.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Redefinition in the KerML model.
Specified by:
`[visitRedefinition](KerMLModelVisitor.html#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Redefinition to visit.
`context` - The visitor context.
visitReferenceSubsetting
default void visitReferenceSubsetting([ReferenceSubsetting](kerml/ReferenceSubsetting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a ReferenceSubsetting in the KerML model.
Specified by:
`[visitReferenceSubsetting](KerMLModelVisitor.html#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The ReferenceSubsetting to visit.
`context` - The visitor context.
visitRelationship
default void visitRelationship([Relationship](kerml/Relationship.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Relationship in the KerML model.
Specified by:
`[visitRelationship](KerMLModelVisitor.html#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Relationship to visit.
`context` - The visitor context.
visitResultExpressionMembership
default void visitResultExpressionMembership([ResultExpressionMembership](kerml/ResultExpressionMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a ResultExpressionMembership in the KerML model.
Specified by:
`[visitResultExpressionMembership](KerMLModelVisitor.html#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The ResultExpressionMembership to visit.
`context` - The visitor context.
visitReturnParameterMembership
default void visitReturnParameterMembership([ReturnParameterMembership](kerml/ReturnParameterMembership.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a ReturnParameterMembership in the KerML model.
Specified by:
`[visitReturnParameterMembership](KerMLModelVisitor.html#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The ReturnParameterMembership to visit.
`context` - The visitor context.
visitSelectExpression
default void visitSelectExpression([SelectExpression](kerml/SelectExpression.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a SelectExpression in the KerML model.
Specified by:
`[visitSelectExpression](KerMLModelVisitor.html#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The SelectExpression to visit.
`context` - The visitor context.
visitSpecialization
default void visitSpecialization([Specialization](kerml/Specialization.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Specialization in the KerML model.
Specified by:
`[visitSpecialization](KerMLModelVisitor.html#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Specialization to visit.
`context` - The visitor context.
visitStep
default void visitStep([Step](kerml/Step.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Step in the KerML model.
Specified by:
`[visitStep](KerMLModelVisitor.html#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Step to visit.
`context` - The visitor context.
visitStructure
default void visitStructure([Structure](kerml/Structure.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Structure in the KerML model.
Specified by:
`[visitStructure](KerMLModelVisitor.html#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Structure to visit.
`context` - The visitor context.
visitSubclassification
default void visitSubclassification([Subclassification](kerml/Subclassification.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Subclassification in the KerML model.
Specified by:
`[visitSubclassification](KerMLModelVisitor.html#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Subclassification to visit.
`context` - The visitor context.
visitSubsetting
default void visitSubsetting([Subsetting](kerml/Subsetting.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Subsetting in the KerML model.
Specified by:
`[visitSubsetting](KerMLModelVisitor.html#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Subsetting to visit.
`context` - The visitor context.
visitSuccession
default void visitSuccession([Succession](kerml/Succession.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Succession in the KerML model.
Specified by:
`[visitSuccession](KerMLModelVisitor.html#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Succession to visit.
`context` - The visitor context.
visitSuccessionFlow
default void visitSuccessionFlow([SuccessionFlow](kerml/SuccessionFlow.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a SuccessionFlow in the KerML model.
Specified by:
`[visitSuccessionFlow](KerMLModelVisitor.html#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The SuccessionFlow to visit.
`context` - The visitor context.
visitTextualRepresentation
default void visitTextualRepresentation([TextualRepresentation](kerml/TextualRepresentation.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a TextualRepresentation in the KerML model.
Specified by:
`[visitTextualRepresentation](KerMLModelVisitor.html#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The TextualRepresentation to visit.
`context` - The visitor context.
visitType
default void visitType([Type](kerml/Type.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Type in the KerML model.
Specified by:
`[visitType](KerMLModelVisitor.html#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Type to visit.
`context` - The visitor context.
visitTypeFeaturing
default void visitTypeFeaturing([TypeFeaturing](kerml/TypeFeaturing.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a TypeFeaturing in the KerML model.
Specified by:
`[visitTypeFeaturing](KerMLModelVisitor.html#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The TypeFeaturing to visit.
`context` - The visitor context.
visitUnioning
default void visitUnioning([Unioning](kerml/Unioning.html) element,
 [C](KerMLModelHierarchyVisitor.html) context)
Visits a Unioning in the KerML model.
Specified by:
`[visitUnioning](KerMLModelVisitor.html#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C))` in interface `[KerMLModelVisitor](KerMLModelVisitor.html)<[C](KerMLModelHierarchyVisitor.html) extends [KerMLVisitorContext](KerMLVisitorContext.html)>`
Parameters:
`element` - The Unioning to visit.
`context` - The visitor context.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Interface KerMLModelHierarchyVisitor">Interface KerMLModelHierarchyVisitor&lt;C extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>C</code> - The type of the visitor context, which must extend <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLVisitorContext</code></a>.</dd>
</dl>
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../nomagic/magicdraw/uml/AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code>, <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;C&gt;</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../sysml/model/SysMLModelHierarchyVisitor.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLModelHierarchyVisitor</a>&lt;C&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">KerMLModelHierarchyVisitor&lt;C extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</span><span class="extends-implements">
extends <a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;C&gt;</span></div>
<div class="block">A visitor interface for traversing the KerML model hierarchy.
 <p>
 This interface extends <a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLModelVisitor</code></a> and provides methods to visit various elements
 in the KerML model, including classes, packages, relationships, and more. It also includes
 methods to check the EPackage and determine if elements are acceptable for the visitor.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLModelVisitor</code></a></li>
<li><a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>KerMLVisitorContext</code></a></li>
<li><a href="kerml/KerMLPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>KerMLPackage</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default org.eclipse.emf.ecore.EPackage</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getEPackage()">getEPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Gets the EPackage visitor is suited for.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isAcceptable(org.eclipse.emf.ecore.EPackage)">isAcceptable</a><wbr/>(org.eclipse.emf.ecore.EPackage ePackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Checks if given EPackage elements are acceptable by the visitor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">visitAnnotatingElement</a><wbr/>(<a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AnnotatingElement in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">visitAnnotation</a><wbr/>(<a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Annotation in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">visitAssociation</a><wbr/>(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Association in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">visitAssociationStructure</a><wbr/>(<a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an AssociationStructure in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">visitBehavior</a><wbr/>(<a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Behavior in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">visitBindingConnector</a><wbr/>(<a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a BindingConnector in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">visitBooleanExpression</a><wbr/>(<a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a BooleanExpression in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">visitClass</a><wbr/>(<a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Class in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">visitClassifier</a><wbr/>(<a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Classifier in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">visitCollectExpression</a><wbr/>(<a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a CollectExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">visitComment</a><wbr/>(<a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Comment in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">visitConjugation</a><wbr/>(<a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Conjugation in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">visitConnector</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Connector in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">visitConstructorExpression</a><wbr/>(<a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ConstructorExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">visitCrossSubsetting</a><wbr/>(<a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a CrossSubsetting in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">visitDataType</a><wbr/>(<a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a DataType in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">visitDependency</a><wbr/>(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Dependency in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">visitDifferencing</a><wbr/>(<a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Differencing in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">visitDisjoining</a><wbr/>(<a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Disjoining in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">visitDocumentation</a><wbr/>(<a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Documentation in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">visitElement</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Element in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">visitElementFilterMembership</a><wbr/>(<a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an ElementFilterMembership in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">visitEndFeatureMembership</a><wbr/>(<a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an EndFeatureMembership in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">visitExpression</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Expression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">visitFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Feature in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">visitFeatureChainExpression</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureChainExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">visitFeatureChaining</a><wbr/>(<a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureChaining in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">visitFeatureInverting</a><wbr/>(<a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureInverting in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">visitFeatureMembership</a><wbr/>(<a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureMembership in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">visitFeatureReferenceExpression</a><wbr/>(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureReferenceExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">visitFeatureTyping</a><wbr/>(<a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureTyping in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">visitFeatureValue</a><wbr/>(<a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FeatureValue in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">visitFlow</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Flow in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">visitFlowEnd</a><wbr/>(<a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a FlowEnd in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">visitFunction</a><wbr/>(<a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Function in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">visitImport</a><wbr/>(<a href="kerml/Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Import in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">visitIndexExpression</a><wbr/>(<a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an IndexExpression in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">visitInstantiationExpression</a><wbr/>(<a href="kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an InstantiationExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">visitInteraction</a><wbr/>(<a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Interaction in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">visitIntersecting</a><wbr/>(<a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Intersecting in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">visitInvariant</a><wbr/>(<a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an Invariant in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">visitInvocationExpression</a><wbr/>(<a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an InvocationExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">visitLibraryPackage</a><wbr/>(<a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LibraryPackage in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">visitLiteralBoolean</a><wbr/>(<a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LiteralBoolean in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">visitLiteralExpression</a><wbr/>(<a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LiteralExpression in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">visitLiteralInfinity</a><wbr/>(<a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LiteralInfinity in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">visitLiteralInteger</a><wbr/>(<a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LiteralInteger in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">visitLiteralRational</a><wbr/>(<a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LiteralRational in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">visitLiteralString</a><wbr/>(<a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a LiteralString in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">visitMembership</a><wbr/>(<a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Membership in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">visitMembershipImport</a><wbr/>(<a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MembershipImport in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">visitMetaclass</a><wbr/>(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Metaclass in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">visitMetadataAccessExpression</a><wbr/>(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MetadataAccessExpression in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">visitMetadataFeature</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MetadataFeature in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">visitMultiplicity</a><wbr/>(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Multiplicity in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">visitMultiplicityRange</a><wbr/>(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a MultiplicityRange in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">visitNamespace</a><wbr/>(<a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Namespace in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">visitNamespaceImport</a><wbr/>(<a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a NamespaceImport in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">visitNullExpression</a><wbr/>(<a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a NullExpression in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">visitOperatorExpression</a><wbr/>(<a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an OperatorExpression in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">visitOwningMembership</a><wbr/>(<a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits an OwningMembership in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">visitPackage</a><wbr/>(<a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Package in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">visitParameterMembership</a><wbr/>(<a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ParameterMembership in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">visitPayloadFeature</a><wbr/>(<a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a PayloadFeature in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">visitPredicate</a><wbr/>(<a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Predicate in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">visitRedefinition</a><wbr/>(<a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Redefinition in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">visitReferenceSubsetting</a><wbr/>(<a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ReferenceSubsetting in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">visitRelationship</a><wbr/>(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Relationship in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">visitResultExpressionMembership</a><wbr/>(<a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ResultExpressionMembership in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">visitReturnParameterMembership</a><wbr/>(<a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a ReturnParameterMembership in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">visitSelectExpression</a><wbr/>(<a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SelectExpression in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">visitSpecialization</a><wbr/>(<a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Specialization in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">visitStep</a><wbr/>(<a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Step in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">visitStructure</a><wbr/>(<a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Structure in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">visitSubclassification</a><wbr/>(<a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Subclassification in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">visitSubsetting</a><wbr/>(<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Subsetting in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">visitSuccession</a><wbr/>(<a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Succession in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">visitSuccessionFlow</a><wbr/>(<a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a SuccessionFlow in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">visitTextualRepresentation</a><wbr/>(<a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a TextualRepresentation in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">visitType</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Type in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">visitTypeFeaturing</a><wbr/>(<a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a TypeFeaturing in the KerML model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">visitUnioning</a><wbr/>(<a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visits a Unioning in the KerML model.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLModelVisitor">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a></h3>
<code><a href="KerMLModelVisitor.html#createVisitorContext()">createVisitorContext</a></code></div>
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
<section class="detail" id="getEPackage()">
<h3>getEPackage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">org.eclipse.emf.ecore.EPackage</span> <span class="element-name">getEPackage</span>()</div>
<div class="block">Gets the EPackage visitor is suited for.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The EPackage instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAcceptable(org.eclipse.emf.ecore.EPackage)">
<h3>isAcceptable</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isAcceptable</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EPackage ePackage)</span></div>
<div class="block">Checks if given EPackage elements are acceptable by the visitor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ePackage</code> - The EPackage to check.</dd>
<dt>Returns:</dt>
<dd>True if the EPackage is acceptable, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">
<h3 id="visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAnnotatingElement</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAnnotatingElement</span><wbr/><span class="parameters">(<a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AnnotatingElement in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement,C)">visitAnnotatingElement</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The AnnotatingElement to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">
<h3 id="visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAnnotation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAnnotation</span><wbr/><span class="parameters">(<a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Annotation in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitAnnotation(com.dassault_systemes.modeler.kerml.model.kerml.Annotation,C)">visitAnnotation</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Annotation to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">
<h3 id="visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAssociation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssociation</span><wbr/><span class="parameters">(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Association in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitAssociation(com.dassault_systemes.modeler.kerml.model.kerml.Association,C)">visitAssociation</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Association to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">
<h3 id="visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitAssociationStructure</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAssociationStructure</span><wbr/><span class="parameters">(<a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an AssociationStructure in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitAssociationStructure(com.dassault_systemes.modeler.kerml.model.kerml.AssociationStructure,C)">visitAssociationStructure</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The AssociationStructure to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">
<h3 id="visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitBehavior</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBehavior</span><wbr/><span class="parameters">(<a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Behavior in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Behavior,C)">visitBehavior</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Behavior to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">
<h3 id="visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitBindingConnector</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBindingConnector</span><wbr/><span class="parameters">(<a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a BindingConnector in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitBindingConnector(com.dassault_systemes.modeler.kerml.model.kerml.BindingConnector,C)">visitBindingConnector</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The BindingConnector to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">
<h3 id="visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitBooleanExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitBooleanExpression</span><wbr/><span class="parameters">(<a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a BooleanExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitBooleanExpression(com.dassault_systemes.modeler.kerml.model.kerml.BooleanExpression,C)">visitBooleanExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The BooleanExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">
<h3 id="visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitClass</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClass</span><wbr/><span class="parameters">(<a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Class in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitClass(com.dassault_systemes.modeler.kerml.model.kerml.Class,C)">visitClass</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Class to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">
<h3 id="visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitClassifier</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitClassifier</span><wbr/><span class="parameters">(<a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Classifier in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitClassifier(com.dassault_systemes.modeler.kerml.model.kerml.Classifier,C)">visitClassifier</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Classifier to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">
<h3 id="visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitCollectExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCollectExpression</span><wbr/><span class="parameters">(<a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a CollectExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitCollectExpression(com.dassault_systemes.modeler.kerml.model.kerml.CollectExpression,C)">visitCollectExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The CollectExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">
<h3 id="visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitComment</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitComment</span><wbr/><span class="parameters">(<a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Comment in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitComment(com.dassault_systemes.modeler.kerml.model.kerml.Comment,C)">visitComment</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Comment to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">
<h3 id="visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitConjugation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConjugation</span><wbr/><span class="parameters">(<a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Conjugation in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitConjugation(com.dassault_systemes.modeler.kerml.model.kerml.Conjugation,C)">visitConjugation</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Conjugation to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">
<h3 id="visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitConnector</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConnector</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Connector in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitConnector(com.dassault_systemes.modeler.kerml.model.kerml.Connector,C)">visitConnector</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Connector to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">
<h3 id="visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitConstructorExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitConstructorExpression</span><wbr/><span class="parameters">(<a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ConstructorExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitConstructorExpression(com.dassault_systemes.modeler.kerml.model.kerml.ConstructorExpression,C)">visitConstructorExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The ConstructorExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">
<h3 id="visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitCrossSubsetting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitCrossSubsetting</span><wbr/><span class="parameters">(<a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a CrossSubsetting in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitCrossSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.CrossSubsetting,C)">visitCrossSubsetting</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The CrossSubsetting to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">
<h3 id="visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDataType</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDataType</span><wbr/><span class="parameters">(<a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a DataType in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitDataType(com.dassault_systemes.modeler.kerml.model.kerml.DataType,C)">visitDataType</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The DataType to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">
<h3 id="visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDependency</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDependency</span><wbr/><span class="parameters">(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Dependency in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitDependency(com.dassault_systemes.modeler.kerml.model.kerml.Dependency,C)">visitDependency</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Dependency to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">
<h3 id="visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDifferencing</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDifferencing</span><wbr/><span class="parameters">(<a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Differencing in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitDifferencing(com.dassault_systemes.modeler.kerml.model.kerml.Differencing,C)">visitDifferencing</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Differencing to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">
<h3 id="visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDisjoining</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDisjoining</span><wbr/><span class="parameters">(<a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Disjoining in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitDisjoining(com.dassault_systemes.modeler.kerml.model.kerml.Disjoining,C)">visitDisjoining</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Disjoining to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">
<h3 id="visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitDocumentation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDocumentation</span><wbr/><span class="parameters">(<a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Documentation in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitDocumentation(com.dassault_systemes.modeler.kerml.model.kerml.Documentation,C)">visitDocumentation</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Documentation to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">
<h3 id="visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitElement</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElement</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Element in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,C)">visitElement</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Element to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">
<h3 id="visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitElementFilterMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitElementFilterMembership</span><wbr/><span class="parameters">(<a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an ElementFilterMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitElementFilterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ElementFilterMembership,C)">visitElementFilterMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The ElementFilterMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">
<h3 id="visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitEndFeatureMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitEndFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an EndFeatureMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitEndFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.EndFeatureMembership,C)">visitEndFeatureMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The EndFeatureMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">
<h3 id="visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitExpression</span><wbr/><span class="parameters">(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Expression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,C)">visitExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Expression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">
<h3 id="visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeature</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Feature in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,C)">visitFeature</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Feature to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">
<h3 id="visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureChainExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureChainExpression</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureChainExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureChainExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,C)">visitFeatureChainExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureChainExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">
<h3 id="visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureChaining</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureChaining</span><wbr/><span class="parameters">(<a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureChaining in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChaining,C)">visitFeatureChaining</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureChaining to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">
<h3 id="visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureInverting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureInverting</span><wbr/><span class="parameters">(<a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureInverting in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureInverting(com.dassault_systemes.modeler.kerml.model.kerml.FeatureInverting,C)">visitFeatureInverting</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureInverting to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">
<h3 id="visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership,C)">visitFeatureMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">
<h3 id="visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureReferenceExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureReferenceExpression</span><wbr/><span class="parameters">(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureReferenceExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureReferenceExpression(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,C)">visitFeatureReferenceExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureReferenceExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">
<h3 id="visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureTyping</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureTyping</span><wbr/><span class="parameters">(<a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureTyping in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureTyping(com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping,C)">visitFeatureTyping</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureTyping to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">
<h3 id="visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFeatureValue</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFeatureValue</span><wbr/><span class="parameters">(<a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FeatureValue in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureValue,C)">visitFeatureValue</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FeatureValue to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">
<h3 id="visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFlow</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFlow</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Flow in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFlow(com.dassault_systemes.modeler.kerml.model.kerml.Flow,C)">visitFlow</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Flow to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">
<h3 id="visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFlowEnd</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFlowEnd</span><wbr/><span class="parameters">(<a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a FlowEnd in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.FlowEnd,C)">visitFlowEnd</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The FlowEnd to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">
<h3 id="visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitFunction</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitFunction</span><wbr/><span class="parameters">(<a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Function in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitFunction(com.dassault_systemes.modeler.kerml.model.kerml.Function,C)">visitFunction</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Function to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">
<h3 id="visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitImport</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitImport</span><wbr/><span class="parameters">(<a href="kerml/Import.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Import</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Import in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitImport(com.dassault_systemes.modeler.kerml.model.kerml.Import,C)">visitImport</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Import to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">
<h3 id="visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitIndexExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitIndexExpression</span><wbr/><span class="parameters">(<a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an IndexExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitIndexExpression(com.dassault_systemes.modeler.kerml.model.kerml.IndexExpression,C)">visitIndexExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The IndexExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">
<h3 id="visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInstantiationExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInstantiationExpression</span><wbr/><span class="parameters">(<a href="kerml/InstantiationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InstantiationExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an InstantiationExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitInstantiationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InstantiationExpression,C)">visitInstantiationExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The InstantiationExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">
<h3 id="visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInteraction</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInteraction</span><wbr/><span class="parameters">(<a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Interaction in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitInteraction(com.dassault_systemes.modeler.kerml.model.kerml.Interaction,C)">visitInteraction</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Interaction to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">
<h3 id="visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitIntersecting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitIntersecting</span><wbr/><span class="parameters">(<a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Intersecting in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitIntersecting(com.dassault_systemes.modeler.kerml.model.kerml.Intersecting,C)">visitIntersecting</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Intersecting to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">
<h3 id="visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInvariant</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInvariant</span><wbr/><span class="parameters">(<a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an Invariant in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitInvariant(com.dassault_systemes.modeler.kerml.model.kerml.Invariant,C)">visitInvariant</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Invariant to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">
<h3 id="visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitInvocationExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitInvocationExpression</span><wbr/><span class="parameters">(<a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an InvocationExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.InvocationExpression,C)">visitInvocationExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The InvocationExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">
<h3 id="visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLibraryPackage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLibraryPackage</span><wbr/><span class="parameters">(<a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LibraryPackage in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLibraryPackage(com.dassault_systemes.modeler.kerml.model.kerml.LibraryPackage,C)">visitLibraryPackage</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LibraryPackage to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">
<h3 id="visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralBoolean</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLiteralBoolean</span><wbr/><span class="parameters">(<a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LiteralBoolean in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLiteralBoolean(com.dassault_systemes.modeler.kerml.model.kerml.LiteralBoolean,C)">visitLiteralBoolean</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LiteralBoolean to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">
<h3 id="visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLiteralExpression</span><wbr/><span class="parameters">(<a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LiteralExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLiteralExpression(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression,C)">visitLiteralExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LiteralExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">
<h3 id="visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralInfinity</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLiteralInfinity</span><wbr/><span class="parameters">(<a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LiteralInfinity in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLiteralInfinity(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInfinity,C)">visitLiteralInfinity</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LiteralInfinity to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">
<h3 id="visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralInteger</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLiteralInteger</span><wbr/><span class="parameters">(<a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LiteralInteger in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLiteralInteger(com.dassault_systemes.modeler.kerml.model.kerml.LiteralInteger,C)">visitLiteralInteger</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LiteralInteger to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">
<h3 id="visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralRational</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLiteralRational</span><wbr/><span class="parameters">(<a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LiteralRational in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLiteralRational(com.dassault_systemes.modeler.kerml.model.kerml.LiteralRational,C)">visitLiteralRational</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LiteralRational to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">
<h3 id="visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitLiteralString</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitLiteralString</span><wbr/><span class="parameters">(<a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a LiteralString in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitLiteralString(com.dassault_systemes.modeler.kerml.model.kerml.LiteralString,C)">visitLiteralString</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The LiteralString to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">
<h3 id="visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMembership</span><wbr/><span class="parameters">(<a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Membership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMembership(com.dassault_systemes.modeler.kerml.model.kerml.Membership,C)">visitMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Membership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">
<h3 id="visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMembershipImport</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMembershipImport</span><wbr/><span class="parameters">(<a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MembershipImport in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMembershipImport(com.dassault_systemes.modeler.kerml.model.kerml.MembershipImport,C)">visitMembershipImport</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The MembershipImport to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">
<h3 id="visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMetaclass</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMetaclass</span><wbr/><span class="parameters">(<a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Metaclass in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMetaclass(com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,C)">visitMetaclass</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Metaclass to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">
<h3 id="visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMetadataAccessExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMetadataAccessExpression</span><wbr/><span class="parameters">(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MetadataAccessExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,C)">visitMetadataAccessExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The MetadataAccessExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">
<h3 id="visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMetadataFeature</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMetadataFeature</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MetadataFeature in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMetadataFeature(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,C)">visitMetadataFeature</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The MetadataFeature to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">
<h3 id="visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMultiplicity</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMultiplicity</span><wbr/><span class="parameters">(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Multiplicity in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity,C)">visitMultiplicity</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Multiplicity to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">
<h3 id="visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitMultiplicityRange</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitMultiplicityRange</span><wbr/><span class="parameters">(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a MultiplicityRange in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange,C)">visitMultiplicityRange</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The MultiplicityRange to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">
<h3 id="visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitNamespace</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNamespace</span><wbr/><span class="parameters">(<a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Namespace in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace,C)">visitNamespace</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Namespace to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">
<h3 id="visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitNamespaceImport</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNamespaceImport</span><wbr/><span class="parameters">(<a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a NamespaceImport in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitNamespaceImport(com.dassault_systemes.modeler.kerml.model.kerml.NamespaceImport,C)">visitNamespaceImport</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The NamespaceImport to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">
<h3 id="visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitNullExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitNullExpression</span><wbr/><span class="parameters">(<a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a NullExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitNullExpression(com.dassault_systemes.modeler.kerml.model.kerml.NullExpression,C)">visitNullExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The NullExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">
<h3 id="visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOperatorExpression</span><wbr/><span class="parameters">(<a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an OperatorExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression,C)">visitOperatorExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The OperatorExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">
<h3 id="visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitOwningMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitOwningMembership</span><wbr/><span class="parameters">(<a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits an OwningMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership,C)">visitOwningMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The OwningMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">
<h3 id="visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitPackage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPackage</span><wbr/><span class="parameters">(<a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Package in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitPackage(com.dassault_systemes.modeler.kerml.model.kerml.Package,C)">visitPackage</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Package to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">
<h3 id="visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitParameterMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitParameterMembership</span><wbr/><span class="parameters">(<a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ParameterMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ParameterMembership,C)">visitParameterMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The ParameterMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">
<h3 id="visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitPayloadFeature</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPayloadFeature</span><wbr/><span class="parameters">(<a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a PayloadFeature in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitPayloadFeature(com.dassault_systemes.modeler.kerml.model.kerml.PayloadFeature,C)">visitPayloadFeature</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The PayloadFeature to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">
<h3 id="visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitPredicate</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPredicate</span><wbr/><span class="parameters">(<a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Predicate in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitPredicate(com.dassault_systemes.modeler.kerml.model.kerml.Predicate,C)">visitPredicate</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Predicate to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">
<h3 id="visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitRedefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRedefinition</span><wbr/><span class="parameters">(<a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Redefinition in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitRedefinition(com.dassault_systemes.modeler.kerml.model.kerml.Redefinition,C)">visitRedefinition</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Redefinition to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">
<h3 id="visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitReferenceSubsetting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitReferenceSubsetting</span><wbr/><span class="parameters">(<a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ReferenceSubsetting in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitReferenceSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.ReferenceSubsetting,C)">visitReferenceSubsetting</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The ReferenceSubsetting to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">
<h3 id="visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitRelationship</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitRelationship</span><wbr/><span class="parameters">(<a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Relationship in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,C)">visitRelationship</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Relationship to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">
<h3 id="visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitResultExpressionMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitResultExpressionMembership</span><wbr/><span class="parameters">(<a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ResultExpressionMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitResultExpressionMembership(com.dassault_systemes.modeler.kerml.model.kerml.ResultExpressionMembership,C)">visitResultExpressionMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The ResultExpressionMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">
<h3 id="visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitReturnParameterMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitReturnParameterMembership</span><wbr/><span class="parameters">(<a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a ReturnParameterMembership in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitReturnParameterMembership(com.dassault_systemes.modeler.kerml.model.kerml.ReturnParameterMembership,C)">visitReturnParameterMembership</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The ReturnParameterMembership to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">
<h3 id="visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSelectExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSelectExpression</span><wbr/><span class="parameters">(<a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SelectExpression in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitSelectExpression(com.dassault_systemes.modeler.kerml.model.kerml.SelectExpression,C)">visitSelectExpression</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The SelectExpression to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">
<h3 id="visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSpecialization</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSpecialization</span><wbr/><span class="parameters">(<a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Specialization in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitSpecialization(com.dassault_systemes.modeler.kerml.model.kerml.Specialization,C)">visitSpecialization</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Specialization to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">
<h3 id="visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitStep</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStep</span><wbr/><span class="parameters">(<a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Step in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitStep(com.dassault_systemes.modeler.kerml.model.kerml.Step,C)">visitStep</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Step to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">
<h3 id="visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitStructure</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitStructure</span><wbr/><span class="parameters">(<a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Structure in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitStructure(com.dassault_systemes.modeler.kerml.model.kerml.Structure,C)">visitStructure</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Structure to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">
<h3 id="visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSubclassification</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSubclassification</span><wbr/><span class="parameters">(<a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Subclassification in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitSubclassification(com.dassault_systemes.modeler.kerml.model.kerml.Subclassification,C)">visitSubclassification</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Subclassification to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">
<h3 id="visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSubsetting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSubsetting</span><wbr/><span class="parameters">(<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Subsetting in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Subsetting,C)">visitSubsetting</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Subsetting to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">
<h3 id="visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSuccession</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSuccession</span><wbr/><span class="parameters">(<a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Succession in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitSuccession(com.dassault_systemes.modeler.kerml.model.kerml.Succession,C)">visitSuccession</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Succession to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">
<h3 id="visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitSuccessionFlow</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitSuccessionFlow</span><wbr/><span class="parameters">(<a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a SuccessionFlow in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitSuccessionFlow(com.dassault_systemes.modeler.kerml.model.kerml.SuccessionFlow,C)">visitSuccessionFlow</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The SuccessionFlow to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">
<h3 id="visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitTextualRepresentation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTextualRepresentation</span><wbr/><span class="parameters">(<a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a TextualRepresentation in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitTextualRepresentation(com.dassault_systemes.modeler.kerml.model.kerml.TextualRepresentation,C)">visitTextualRepresentation</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The TextualRepresentation to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">
<h3 id="visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitType</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitType</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Type in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitType(com.dassault_systemes.modeler.kerml.model.kerml.Type,C)">visitType</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Type to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">
<h3 id="visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitTypeFeaturing</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitTypeFeaturing</span><wbr/><span class="parameters">(<a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a TypeFeaturing in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitTypeFeaturing(com.dassault_systemes.modeler.kerml.model.kerml.TypeFeaturing,C)">visitTypeFeaturing</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The TypeFeaturing to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">
<h3 id="visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext)">visitUnioning</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitUnioning</span><wbr/><span class="parameters">(<a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a> element,
 <a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> context)</span></div>
<div class="block">Visits a Unioning in the KerML model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="KerMLModelVisitor.html#visitUnioning(com.dassault_systemes.modeler.kerml.model.kerml.Unioning,C)">visitUnioning</a></code> in interface <code><a href="KerMLModelVisitor.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLModelVisitor</a>&lt;<a href="KerMLModelHierarchyVisitor.html" title="type parameter in KerMLModelHierarchyVisitor">C</a> extends <a href="KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - The Unioning to visit.</dd>
<dd><code>context</code> - The visitor context.</dd>
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
