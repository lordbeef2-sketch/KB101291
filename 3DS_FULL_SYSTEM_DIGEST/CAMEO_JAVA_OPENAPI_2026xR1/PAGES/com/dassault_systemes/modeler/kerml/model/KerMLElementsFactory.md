# JAVA OPENAPI: KerMLElementsFactory (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/KerMLElementsFactory.html
- source_path: `com/dassault_systemes/modeler/kerml/model/KerMLElementsFactory.html`
- source_sha256: `c428533a9fa8e2b3f311aa5f9bccb1afc3f113bcb3351e531ef322b7c3a6dfb5`
- captured_utc: `2026-07-14T16:44:47.855841+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Interface KerMLElementsFactory

All Superinterfaces:
`com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory`

All Known Subinterfaces:
`[ElementsFactory](ElementsFactory.html)`, `[ElementsFactory](../../sysml/model/ElementsFactory.html)`, `[SysMLElementsFactory](../../sysml/model/SysMLElementsFactory.html)`

@OpenApiAllpublic interfaceKerMLElementsFactoryextends com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory

Core factory for creating KerML model elements.

Provides methods to instantiate all standard KerML element types.
 Each created element is automatically initialized and ready to be added to the model.

This is the low-level factory used by higher-level APIs (e.g., SysML).
 In most cases, you will obtain it via `ElementsFactory.get(project)`.

**Typical usage:**

````java
ElementsFactory factory = ElementsFactory.get(project);
 Class clazz = factory.createClass();
````

This API is available to Open API clients.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default <T extends [Element](kerml/Element.html)> 
T`
`[create](#create(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> aClass)`

`default [AnnotatingElement](kerml/AnnotatingElement.html)`
`[createAnnotatingElement](#createAnnotatingElement())()`
Returns a new object of class '*Annotating Element*'.
`default [Annotation](kerml/Annotation.html)`
`[createAnnotation](#createAnnotation())()`
Returns a new object of class '*Annotation*'.
`default [Association](kerml/Association.html)`
`[createAssociation](#createAssociation())()`
Returns a new object of class '*Association*'.
`default [AssociationStructure](kerml/AssociationStructure.html)`
`[createAssociationStructure](#createAssociationStructure())()`
Returns a new object of class '*Association Structure*'.
`default [Behavior](kerml/Behavior.html)`
`[createBehavior](#createBehavior())()`
Returns a new object of class '*Behavior*'.
`default [BindingConnector](kerml/BindingConnector.html)`
`[createBindingConnector](#createBindingConnector())()`
Returns a new object of class '*Binding Connector*'.
`default [BooleanExpression](kerml/BooleanExpression.html)`
`[createBooleanExpression](#createBooleanExpression())()`
Returns a new object of class '*Boolean Expression*'.
`default [Class](kerml/Class.html)`
`[createClass](#createClass())()`
Returns a new object of class '*Class*'.
`default [Classifier](kerml/Classifier.html)`
`[createClassifier](#createClassifier())()`
Returns a new object of class '*Classifier*'.
`default [CollectExpression](kerml/CollectExpression.html)`
`[createCollectExpression](#createCollectExpression())()`
Returns a new object of class '*Collect Expression*'.
`default [Comment](kerml/Comment.html)`
`[createComment](#createComment())()`
Returns a new object of class '*Comment*'.
`default [Conjugation](kerml/Conjugation.html)`
`[createConjugation](#createConjugation())()`
Returns a new object of class '*Conjugation*'.
`default [Connector](kerml/Connector.html)`
`[createConnector](#createConnector())()`
Returns a new object of class '*Connector*'.
`default [ConstructorExpression](kerml/ConstructorExpression.html)`
`[createConstructorExpression](#createConstructorExpression())()`
Returns a new object of class '*Constructor Expression*'.
`default [CrossSubsetting](kerml/CrossSubsetting.html)`
`[createCrossSubsetting](#createCrossSubsetting())()`
Returns a new object of class '*Cross Subsetting*'.
`default [DataType](kerml/DataType.html)`
`[createDataType](#createDataType())()`
Returns a new object of class '*Data Type*'.
`default [Dependency](kerml/Dependency.html)`
`[createDependency](#createDependency())()`
Returns a new object of class '*Dependency*'.
`default [Differencing](kerml/Differencing.html)`
`[createDifferencing](#createDifferencing())()`
Returns a new object of class '*Differencing*'.
`default [Disjoining](kerml/Disjoining.html)`
`[createDisjoining](#createDisjoining())()`
Returns a new object of class '*Disjoining*'.
`default [Documentation](kerml/Documentation.html)`
`[createDocumentation](#createDocumentation())()`
Returns a new object of class '*Documentation*'.
`default [ElementFilterMembership](kerml/ElementFilterMembership.html)`
`[createElementFilterMembership](#createElementFilterMembership())()`
Returns a new object of class '*Element Filter Membership*'.
`default [EndFeatureMembership](kerml/EndFeatureMembership.html)`
`[createEndFeatureMembership](#createEndFeatureMembership())()`
Returns a new object of class '*End Feature Membership*'.
`default [Expression](kerml/Expression.html)`
`[createExpression](#createExpression())()`
Returns a new object of class '*Expression*'.
`default [Feature](kerml/Feature.html)`
`[createFeature](#createFeature())()`
Returns a new object of class '*Feature*'.
`default [FeatureChainExpression](kerml/FeatureChainExpression.html)`
`[createFeatureChainExpression](#createFeatureChainExpression())()`
Returns a new object of class '*Feature Chain Expression*'.
`default [FeatureChaining](kerml/FeatureChaining.html)`
`[createFeatureChaining](#createFeatureChaining())()`
Returns a new object of class '*Feature Chaining*'.
`default [FeatureInverting](kerml/FeatureInverting.html)`
`[createFeatureInverting](#createFeatureInverting())()`
Returns a new object of class '*Feature Inverting*'.
`default [FeatureMembership](kerml/FeatureMembership.html)`
`[createFeatureMembership](#createFeatureMembership())()`
Returns a new object of class '*Feature Membership*'.
`default [FeatureReferenceExpression](kerml/FeatureReferenceExpression.html)`
`[createFeatureReferenceExpression](#createFeatureReferenceExpression())()`
Returns a new object of class '*Feature Reference Expression*'.
`default [FeatureTyping](kerml/FeatureTyping.html)`
`[createFeatureTyping](#createFeatureTyping())()`
Returns a new object of class '*Feature Typing*'.
`default [FeatureValue](kerml/FeatureValue.html)`
`[createFeatureValue](#createFeatureValue())()`
Returns a new object of class '*Feature Value*'.
`default [Flow](kerml/Flow.html)`
`[createFlow](#createFlow())()`
Returns a new object of class '*Flow*'.
`default [FlowEnd](kerml/FlowEnd.html)`
`[createFlowEnd](#createFlowEnd())()`
Returns a new object of class '*Flow End*'.
`default [Function](kerml/Function.html)`
`[createFunction](#createFunction())()`
Returns a new object of class '*Function*'.
`default [IndexExpression](kerml/IndexExpression.html)`
`[createIndexExpression](#createIndexExpression())()`
Returns a new object of class '*Index Expression*'.
`default [Interaction](kerml/Interaction.html)`
`[createInteraction](#createInteraction())()`
Returns a new object of class '*Interaction*'.
`default [Intersecting](kerml/Intersecting.html)`
`[createIntersecting](#createIntersecting())()`
Returns a new object of class '*Intersecting*'.
`default [Invariant](kerml/Invariant.html)`
`[createInvariant](#createInvariant())()`
Returns a new object of class '*Invariant*'.
`default [InvocationExpression](kerml/InvocationExpression.html)`
`[createInvocationExpression](#createInvocationExpression())()`
Returns a new object of class '*Invocation Expression*'.
`default [LibraryPackage](kerml/LibraryPackage.html)`
`[createLibraryPackage](#createLibraryPackage())()`
Returns a new object of class '*Library Package*'.
`default [LiteralBoolean](kerml/LiteralBoolean.html)`
`[createLiteralBoolean](#createLiteralBoolean())()`
Returns a new object of class '*Literal Boolean*'.
`default [LiteralExpression](kerml/LiteralExpression.html)`
`[createLiteralExpression](#createLiteralExpression())()`
Returns a new object of class '*Literal Expression*'.
`default [LiteralInfinity](kerml/LiteralInfinity.html)`
`[createLiteralInfinity](#createLiteralInfinity())()`
Returns a new object of class '*Literal Infinity*'.
`default [LiteralInteger](kerml/LiteralInteger.html)`
`[createLiteralInteger](#createLiteralInteger())()`
Returns a new object of class '*Literal Integer*'.
`default [LiteralRational](kerml/LiteralRational.html)`
`[createLiteralRational](#createLiteralRational())()`
Returns a new object of class '*Literal Rational*'.
`default [LiteralString](kerml/LiteralString.html)`
`[createLiteralString](#createLiteralString())()`
Returns a new object of class '*Literal String*'.
`default [Membership](kerml/Membership.html)`
`[createMembership](#createMembership())()`
Returns a new object of class '*Membership*'.
`default [MembershipImport](kerml/MembershipImport.html)`
`[createMembershipImport](#createMembershipImport())()`
Returns a new object of class '*Membership Import*'.
`default [Metaclass](kerml/Metaclass.html)`
`[createMetaclass](#createMetaclass())()`
Returns a new object of class '*Metaclass*'.
`default [MetadataAccessExpression](kerml/MetadataAccessExpression.html)`
`[createMetadataAccessExpression](#createMetadataAccessExpression())()`
Returns a new object of class '*Metadata Access Expression*'.
`default [MetadataFeature](kerml/MetadataFeature.html)`
`[createMetadataFeature](#createMetadataFeature())()`
Returns a new object of class '*Metadata Feature*'.
`default [Multiplicity](kerml/Multiplicity.html)`
`[createMultiplicity](#createMultiplicity())()`
Returns a new object of class '*Multiplicity*'.
`default [MultiplicityRange](kerml/MultiplicityRange.html)`
`[createMultiplicityRange](#createMultiplicityRange())()`
Returns a new object of class '*Multiplicity Range*'.
`default [Namespace](kerml/Namespace.html)`
`[createNamespace](#createNamespace())()`
Returns a new object of class '*Namespace*'.
`default [NamespaceImport](kerml/NamespaceImport.html)`
`[createNamespaceImport](#createNamespaceImport())()`
Returns a new object of class '*Namespace Import*'.
`default [NullExpression](kerml/NullExpression.html)`
`[createNullExpression](#createNullExpression())()`
Returns a new object of class '*Null Expression*'.
`default [OperatorExpression](kerml/OperatorExpression.html)`
`[createOperatorExpression](#createOperatorExpression())()`
Returns a new object of class '*Operator Expression*'.
`default [OwningMembership](kerml/OwningMembership.html)`
`[createOwningMembership](#createOwningMembership())()`
Returns a new object of class '*Owning Membership*'.
`default [Package](kerml/Package.html)`
`[createPackage](#createPackage())()`
Returns a new object of class '*Package*'.
`default [ParameterMembership](kerml/ParameterMembership.html)`
`[createParameterMembership](#createParameterMembership())()`
Returns a new object of class '*Parameter Membership*'.
`default [PayloadFeature](kerml/PayloadFeature.html)`
`[createPayloadFeature](#createPayloadFeature())()`
Returns a new object of class '*Payload Feature*'.
`default [Predicate](kerml/Predicate.html)`
`[createPredicate](#createPredicate())()`
Returns a new object of class '*Predicate*'.
`default [Redefinition](kerml/Redefinition.html)`
`[createRedefinition](#createRedefinition())()`
Returns a new object of class '*Redefinition*'.
`default [ReferenceSubsetting](kerml/ReferenceSubsetting.html)`
`[createReferenceSubsetting](#createReferenceSubsetting())()`
Returns a new object of class '*Reference Subsetting*'.
`default [ResultExpressionMembership](kerml/ResultExpressionMembership.html)`
`[createResultExpressionMembership](#createResultExpressionMembership())()`
Returns a new object of class '*Result Expression Membership*'.
`default [ReturnParameterMembership](kerml/ReturnParameterMembership.html)`
`[createReturnParameterMembership](#createReturnParameterMembership())()`
Returns a new object of class '*Return Parameter Membership*'.
`default [SelectExpression](kerml/SelectExpression.html)`
`[createSelectExpression](#createSelectExpression())()`
Returns a new object of class '*Select Expression*'.
`default [Specialization](kerml/Specialization.html)`
`[createSpecialization](#createSpecialization())()`
Returns a new object of class '*Specialization*'.
`default [Step](kerml/Step.html)`
`[createStep](#createStep())()`
Returns a new object of class '*Step*'.
`default [Structure](kerml/Structure.html)`
`[createStructure](#createStructure())()`
Returns a new object of class '*Structure*'.
`default [Subclassification](kerml/Subclassification.html)`
`[createSubclassification](#createSubclassification())()`
Returns a new object of class '*Subclassification*'.
`default [Subsetting](kerml/Subsetting.html)`
`[createSubsetting](#createSubsetting())()`
Returns a new object of class '*Subsetting*'.
`default [Succession](kerml/Succession.html)`
`[createSuccession](#createSuccession())()`
Returns a new object of class '*Succession*'.
`default [SuccessionFlow](kerml/SuccessionFlow.html)`
`[createSuccessionFlow](#createSuccessionFlow())()`
Returns a new object of class '*Succession Flow*'.
`default [TextualRepresentation](kerml/TextualRepresentation.html)`
`[createTextualRepresentation](#createTextualRepresentation())()`
Returns a new object of class '*Textual Representation*'.
`default [Type](kerml/Type.html)`
`[createType](#createType())()`
Returns a new object of class '*Type*'.
`default [TypeFeaturing](kerml/TypeFeaturing.html)`
`[createTypeFeaturing](#createTypeFeaturing())()`
Returns a new object of class '*Type Featuring*'.
`default [Unioning](kerml/Unioning.html)`
`[createUnioning](#createUnioning())()`
Returns a new object of class '*Unioning*'.
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory
`create, initializeElement`

============ METHOD DETAIL ========== 
Method Details
createAnnotatingElement
default [AnnotatingElement](kerml/AnnotatingElement.html) createAnnotatingElement()
Returns a new object of class '*Annotating Element*'.
Returns:
a new object of class '*Annotating Element*'.
createAnnotation
default [Annotation](kerml/Annotation.html) createAnnotation()
Returns a new object of class '*Annotation*'.
Returns:
a new object of class '*Annotation*'.
createAssociation
default [Association](kerml/Association.html) createAssociation()
Returns a new object of class '*Association*'.
Returns:
a new object of class '*Association*'.
createAssociationStructure
default [AssociationStructure](kerml/AssociationStructure.html) createAssociationStructure()
Returns a new object of class '*Association Structure*'.
Returns:
a new object of class '*Association Structure*'.
createBehavior
default [Behavior](kerml/Behavior.html) createBehavior()
Returns a new object of class '*Behavior*'.
Returns:
a new object of class '*Behavior*'.
createBindingConnector
default [BindingConnector](kerml/BindingConnector.html) createBindingConnector()
Returns a new object of class '*Binding Connector*'.
Returns:
a new object of class '*Binding Connector*'.
createBooleanExpression
default [BooleanExpression](kerml/BooleanExpression.html) createBooleanExpression()
Returns a new object of class '*Boolean Expression*'.
Returns:
a new object of class '*Boolean Expression*'.
createClass
default [Class](kerml/Class.html) createClass()
Returns a new object of class '*Class*'.
Returns:
a new object of class '*Class*'.
createClassifier
default [Classifier](kerml/Classifier.html) createClassifier()
Returns a new object of class '*Classifier*'.
Returns:
a new object of class '*Classifier*'.
createCollectExpression
default [CollectExpression](kerml/CollectExpression.html) createCollectExpression()
Returns a new object of class '*Collect Expression*'.
Returns:
a new object of class '*Collect Expression*'.
createComment
default [Comment](kerml/Comment.html) createComment()
Returns a new object of class '*Comment*'.
Returns:
a new object of class '*Comment*'.
createConjugation
default [Conjugation](kerml/Conjugation.html) createConjugation()
Returns a new object of class '*Conjugation*'.
Returns:
a new object of class '*Conjugation*'.
createConnector
default [Connector](kerml/Connector.html) createConnector()
Returns a new object of class '*Connector*'.
Returns:
a new object of class '*Connector*'.
createConstructorExpression
default [ConstructorExpression](kerml/ConstructorExpression.html) createConstructorExpression()
Returns a new object of class '*Constructor Expression*'.
Returns:
a new object of class '*Constructor Expression*'.
createCrossSubsetting
default [CrossSubsetting](kerml/CrossSubsetting.html) createCrossSubsetting()
Returns a new object of class '*Cross Subsetting*'.
Returns:
a new object of class '*Cross Subsetting*'.
createDataType
default [DataType](kerml/DataType.html) createDataType()
Returns a new object of class '*Data Type*'.
Returns:
a new object of class '*Data Type*'.
createDependency
default [Dependency](kerml/Dependency.html) createDependency()
Returns a new object of class '*Dependency*'.
Returns:
a new object of class '*Dependency*'.
createDifferencing
default [Differencing](kerml/Differencing.html) createDifferencing()
Returns a new object of class '*Differencing*'.
Returns:
a new object of class '*Differencing*'.
createDisjoining
default [Disjoining](kerml/Disjoining.html) createDisjoining()
Returns a new object of class '*Disjoining*'.
Returns:
a new object of class '*Disjoining*'.
createDocumentation
default [Documentation](kerml/Documentation.html) createDocumentation()
Returns a new object of class '*Documentation*'.
Returns:
a new object of class '*Documentation*'.
createElementFilterMembership
default [ElementFilterMembership](kerml/ElementFilterMembership.html) createElementFilterMembership()
Returns a new object of class '*Element Filter Membership*'.
Returns:
a new object of class '*Element Filter Membership*'.
createEndFeatureMembership
default [EndFeatureMembership](kerml/EndFeatureMembership.html) createEndFeatureMembership()
Returns a new object of class '*End Feature Membership*'.
Returns:
a new object of class '*End Feature Membership*'.
createExpression
default [Expression](kerml/Expression.html) createExpression()
Returns a new object of class '*Expression*'.
Returns:
a new object of class '*Expression*'.
createFeature
default [Feature](kerml/Feature.html) createFeature()
Returns a new object of class '*Feature*'.
Returns:
a new object of class '*Feature*'.
createFeatureChainExpression
default [FeatureChainExpression](kerml/FeatureChainExpression.html) createFeatureChainExpression()
Returns a new object of class '*Feature Chain Expression*'.
Returns:
a new object of class '*Feature Chain Expression*'.
createFeatureChaining
default [FeatureChaining](kerml/FeatureChaining.html) createFeatureChaining()
Returns a new object of class '*Feature Chaining*'.
Returns:
a new object of class '*Feature Chaining*'.
createFeatureInverting
default [FeatureInverting](kerml/FeatureInverting.html) createFeatureInverting()
Returns a new object of class '*Feature Inverting*'.
Returns:
a new object of class '*Feature Inverting*'.
createFeatureMembership
default [FeatureMembership](kerml/FeatureMembership.html) createFeatureMembership()
Returns a new object of class '*Feature Membership*'.
Returns:
a new object of class '*Feature Membership*'.
createFeatureReferenceExpression
default [FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) createFeatureReferenceExpression()
Returns a new object of class '*Feature Reference Expression*'.
Returns:
a new object of class '*Feature Reference Expression*'.
createFeatureTyping
default [FeatureTyping](kerml/FeatureTyping.html) createFeatureTyping()
Returns a new object of class '*Feature Typing*'.
Returns:
a new object of class '*Feature Typing*'.
createFeatureValue
default [FeatureValue](kerml/FeatureValue.html) createFeatureValue()
Returns a new object of class '*Feature Value*'.
Returns:
a new object of class '*Feature Value*'.
createFlow
default [Flow](kerml/Flow.html) createFlow()
Returns a new object of class '*Flow*'.
Returns:
a new object of class '*Flow*'.
createFlowEnd
default [FlowEnd](kerml/FlowEnd.html) createFlowEnd()
Returns a new object of class '*Flow End*'.
Returns:
a new object of class '*Flow End*'.
createFunction
default [Function](kerml/Function.html) createFunction()
Returns a new object of class '*Function*'.
Returns:
a new object of class '*Function*'.
createIndexExpression
default [IndexExpression](kerml/IndexExpression.html) createIndexExpression()
Returns a new object of class '*Index Expression*'.
Returns:
a new object of class '*Index Expression*'.
createInteraction
default [Interaction](kerml/Interaction.html) createInteraction()
Returns a new object of class '*Interaction*'.
Returns:
a new object of class '*Interaction*'.
createIntersecting
default [Intersecting](kerml/Intersecting.html) createIntersecting()
Returns a new object of class '*Intersecting*'.
Returns:
a new object of class '*Intersecting*'.
createInvariant
default [Invariant](kerml/Invariant.html) createInvariant()
Returns a new object of class '*Invariant*'.
Returns:
a new object of class '*Invariant*'.
createInvocationExpression
default [InvocationExpression](kerml/InvocationExpression.html) createInvocationExpression()
Returns a new object of class '*Invocation Expression*'.
Returns:
a new object of class '*Invocation Expression*'.
createLibraryPackage
default [LibraryPackage](kerml/LibraryPackage.html) createLibraryPackage()
Returns a new object of class '*Library Package*'.
Returns:
a new object of class '*Library Package*'.
createLiteralBoolean
default [LiteralBoolean](kerml/LiteralBoolean.html) createLiteralBoolean()
Returns a new object of class '*Literal Boolean*'.
Returns:
a new object of class '*Literal Boolean*'.
createLiteralExpression
default [LiteralExpression](kerml/LiteralExpression.html) createLiteralExpression()
Returns a new object of class '*Literal Expression*'.
Returns:
a new object of class '*Literal Expression*'.
createLiteralInfinity
default [LiteralInfinity](kerml/LiteralInfinity.html) createLiteralInfinity()
Returns a new object of class '*Literal Infinity*'.
Returns:
a new object of class '*Literal Infinity*'.
createLiteralInteger
default [LiteralInteger](kerml/LiteralInteger.html) createLiteralInteger()
Returns a new object of class '*Literal Integer*'.
Returns:
a new object of class '*Literal Integer*'.
createLiteralRational
default [LiteralRational](kerml/LiteralRational.html) createLiteralRational()
Returns a new object of class '*Literal Rational*'.
Returns:
a new object of class '*Literal Rational*'.
createLiteralString
default [LiteralString](kerml/LiteralString.html) createLiteralString()
Returns a new object of class '*Literal String*'.
Returns:
a new object of class '*Literal String*'.
createMembership
default [Membership](kerml/Membership.html) createMembership()
Returns a new object of class '*Membership*'.
Returns:
a new object of class '*Membership*'.
createMembershipImport
default [MembershipImport](kerml/MembershipImport.html) createMembershipImport()
Returns a new object of class '*Membership Import*'.
Returns:
a new object of class '*Membership Import*'.
createMetaclass
default [Metaclass](kerml/Metaclass.html) createMetaclass()
Returns a new object of class '*Metaclass*'.
Returns:
a new object of class '*Metaclass*'.
createMetadataAccessExpression
default [MetadataAccessExpression](kerml/MetadataAccessExpression.html) createMetadataAccessExpression()
Returns a new object of class '*Metadata Access Expression*'.
Returns:
a new object of class '*Metadata Access Expression*'.
createMetadataFeature
default [MetadataFeature](kerml/MetadataFeature.html) createMetadataFeature()
Returns a new object of class '*Metadata Feature*'.
Returns:
a new object of class '*Metadata Feature*'.
createMultiplicity
default [Multiplicity](kerml/Multiplicity.html) createMultiplicity()
Returns a new object of class '*Multiplicity*'.
Returns:
a new object of class '*Multiplicity*'.
createMultiplicityRange
default [MultiplicityRange](kerml/MultiplicityRange.html) createMultiplicityRange()
Returns a new object of class '*Multiplicity Range*'.
Returns:
a new object of class '*Multiplicity Range*'.
createNamespace
default [Namespace](kerml/Namespace.html) createNamespace()
Returns a new object of class '*Namespace*'.
Returns:
a new object of class '*Namespace*'.
createNamespaceImport
default [NamespaceImport](kerml/NamespaceImport.html) createNamespaceImport()
Returns a new object of class '*Namespace Import*'.
Returns:
a new object of class '*Namespace Import*'.
createNullExpression
default [NullExpression](kerml/NullExpression.html) createNullExpression()
Returns a new object of class '*Null Expression*'.
Returns:
a new object of class '*Null Expression*'.
createOperatorExpression
default [OperatorExpression](kerml/OperatorExpression.html) createOperatorExpression()
Returns a new object of class '*Operator Expression*'.
Returns:
a new object of class '*Operator Expression*'.
createOwningMembership
default [OwningMembership](kerml/OwningMembership.html) createOwningMembership()
Returns a new object of class '*Owning Membership*'.
Returns:
a new object of class '*Owning Membership*'.
createPackage
default [Package](kerml/Package.html) createPackage()
Returns a new object of class '*Package*'.
Returns:
a new object of class '*Package*'.
createParameterMembership
default [ParameterMembership](kerml/ParameterMembership.html) createParameterMembership()
Returns a new object of class '*Parameter Membership*'.
Returns:
a new object of class '*Parameter Membership*'.
createPayloadFeature
default [PayloadFeature](kerml/PayloadFeature.html) createPayloadFeature()
Returns a new object of class '*Payload Feature*'.
Returns:
a new object of class '*Payload Feature*'.
createPredicate
default [Predicate](kerml/Predicate.html) createPredicate()
Returns a new object of class '*Predicate*'.
Returns:
a new object of class '*Predicate*'.
createRedefinition
default [Redefinition](kerml/Redefinition.html) createRedefinition()
Returns a new object of class '*Redefinition*'.
Returns:
a new object of class '*Redefinition*'.
createReferenceSubsetting
default [ReferenceSubsetting](kerml/ReferenceSubsetting.html) createReferenceSubsetting()
Returns a new object of class '*Reference Subsetting*'.
Returns:
a new object of class '*Reference Subsetting*'.
createResultExpressionMembership
default [ResultExpressionMembership](kerml/ResultExpressionMembership.html) createResultExpressionMembership()
Returns a new object of class '*Result Expression Membership*'.
Returns:
a new object of class '*Result Expression Membership*'.
createReturnParameterMembership
default [ReturnParameterMembership](kerml/ReturnParameterMembership.html) createReturnParameterMembership()
Returns a new object of class '*Return Parameter Membership*'.
Returns:
a new object of class '*Return Parameter Membership*'.
createSelectExpression
default [SelectExpression](kerml/SelectExpression.html) createSelectExpression()
Returns a new object of class '*Select Expression*'.
Returns:
a new object of class '*Select Expression*'.
createSpecialization
default [Specialization](kerml/Specialization.html) createSpecialization()
Returns a new object of class '*Specialization*'.
Returns:
a new object of class '*Specialization*'.
createStep
default [Step](kerml/Step.html) createStep()
Returns a new object of class '*Step*'.
Returns:
a new object of class '*Step*'.
createStructure
default [Structure](kerml/Structure.html) createStructure()
Returns a new object of class '*Structure*'.
Returns:
a new object of class '*Structure*'.
createSubclassification
default [Subclassification](kerml/Subclassification.html) createSubclassification()
Returns a new object of class '*Subclassification*'.
Returns:
a new object of class '*Subclassification*'.
createSubsetting
default [Subsetting](kerml/Subsetting.html) createSubsetting()
Returns a new object of class '*Subsetting*'.
Returns:
a new object of class '*Subsetting*'.
createSuccession
default [Succession](kerml/Succession.html) createSuccession()
Returns a new object of class '*Succession*'.
Returns:
a new object of class '*Succession*'.
createSuccessionFlow
default [SuccessionFlow](kerml/SuccessionFlow.html) createSuccessionFlow()
Returns a new object of class '*Succession Flow*'.
Returns:
a new object of class '*Succession Flow*'.
createTextualRepresentation
default [TextualRepresentation](kerml/TextualRepresentation.html) createTextualRepresentation()
Returns a new object of class '*Textual Representation*'.
Returns:
a new object of class '*Textual Representation*'.
createType
default [Type](kerml/Type.html) createType()
Returns a new object of class '*Type*'.
Returns:
a new object of class '*Type*'.
createTypeFeaturing
default [TypeFeaturing](kerml/TypeFeaturing.html) createTypeFeaturing()
Returns a new object of class '*Type Featuring*'.
Returns:
a new object of class '*Type Featuring*'.
createUnioning
default [Unioning](kerml/Unioning.html) createUnioning()
Returns a new object of class '*Unioning*'.
Returns:
a new object of class '*Unioning*'.
create
default <T extends [Element](kerml/Element.html)> T create([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> aClass)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Interface KerMLElementsFactory">Interface KerMLElementsFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a></code>, <code><a href="../../sysml/model/ElementsFactory.html" title="interface in com.dassault_systemes.modeler.sysml.model">ElementsFactory</a></code>, <code><a href="../../sysml/model/SysMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLElementsFactory</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">KerMLElementsFactory</span><span class="extends-implements">
extends com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</span></div>
<div class="block">Core factory for creating KerML model elements.

 <p>Provides methods to instantiate all standard KerML element types.
 Each created element is automatically initialized and ready to be added to the model.</p>
<p>This is the low-level factory used by higher-level APIs (e.g., SysML).
 In most cases, you will obtain it via <code>ElementsFactory.get(project)</code>.</p>
<p><b>Typical usage:</b></p>
<pre><code>
 ElementsFactory factory = ElementsFactory.get(project);
 Class clazz = factory.createClass();
 </code></pre>
<p>This API is available to Open API clients.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default &lt;T extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#create(java.lang.Class)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; aClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAnnotatingElement()">createAnnotatingElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Annotating Element</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAnnotation()">createAnnotation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Annotation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAssociation()">createAssociation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Association</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAssociationStructure()">createAssociationStructure</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Association Structure</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createBehavior()">createBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Behavior</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createBindingConnector()">createBindingConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Binding Connector</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createBooleanExpression()">createBooleanExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Boolean Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createClass()">createClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Class</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createClassifier()">createClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Classifier</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createCollectExpression()">createCollectExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Collect Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createComment()">createComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Comment</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConjugation()">createConjugation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Conjugation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConnector()">createConnector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Connector</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createConstructorExpression()">createConstructorExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Constructor Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createCrossSubsetting()">createCrossSubsetting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Cross Subsetting</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDataType()">createDataType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Data Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDependency()">createDependency</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Dependency</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDifferencing()">createDifferencing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Differencing</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDisjoining()">createDisjoining</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Disjoining</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createDocumentation()">createDocumentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Documentation</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createElementFilterMembership()">createElementFilterMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Element Filter Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createEndFeatureMembership()">createEndFeatureMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>End Feature Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createExpression()">createExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeature()">createFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureChainExpression()">createFeatureChainExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Chain Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureChaining()">createFeatureChaining</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Chaining</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureInverting()">createFeatureInverting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Inverting</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureMembership()">createFeatureMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureReferenceExpression()">createFeatureReferenceExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Reference Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureTyping()">createFeatureTyping</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Typing</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFeatureValue()">createFeatureValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Feature Value</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFlow()">createFlow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Flow</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFlowEnd()">createFlowEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Flow End</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createFunction()">createFunction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Function</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createIndexExpression()">createIndexExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Index Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createInteraction()">createInteraction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Interaction</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createIntersecting()">createIntersecting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Intersecting</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createInvariant()">createInvariant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Invariant</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createInvocationExpression()">createInvocationExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Invocation Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLibraryPackage()">createLibraryPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Library Package</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLiteralBoolean()">createLiteralBoolean</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Literal Boolean</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLiteralExpression()">createLiteralExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Literal Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLiteralInfinity()">createLiteralInfinity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Literal Infinity</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLiteralInteger()">createLiteralInteger</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Literal Integer</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLiteralRational()">createLiteralRational</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Literal Rational</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createLiteralString()">createLiteralString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Literal String</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMembership()">createMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMembershipImport()">createMembershipImport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Membership Import</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMetaclass()">createMetaclass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Metaclass</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMetadataAccessExpression()">createMetadataAccessExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Metadata Access Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMetadataFeature()">createMetadataFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Metadata Feature</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMultiplicity()">createMultiplicity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Multiplicity</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createMultiplicityRange()">createMultiplicityRange</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Multiplicity Range</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createNamespace()">createNamespace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Namespace</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createNamespaceImport()">createNamespaceImport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Namespace Import</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createNullExpression()">createNullExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Null Expression</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createOperatorExpression()">createOperatorExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Operator Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createOwningMembership()">createOwningMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Owning Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPackage()">createPackage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Package</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createParameterMembership()">createParameterMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Parameter Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPayloadFeature()">createPayloadFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Payload Feature</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createPredicate()">createPredicate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Predicate</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createRedefinition()">createRedefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Redefinition</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createReferenceSubsetting()">createReferenceSubsetting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Reference Subsetting</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createResultExpressionMembership()">createResultExpressionMembership</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Result Expression Membership</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createReturnParameterMembership()">createReturnParameterMembership</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Return Parameter Membership</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSelectExpression()">createSelectExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Select Expression</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSpecialization()">createSpecialization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Specialization</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createStep()">createStep</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Step</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createStructure()">createStructure</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Structure</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSubclassification()">createSubclassification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Subclassification</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSubsetting()">createSubsetting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Subsetting</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSuccession()">createSuccession</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Succession</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createSuccessionFlow()">createSuccessionFlow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Succession Flow</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createTextualRepresentation()">createTextualRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Textual Representation</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createType()">createType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Type</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createTypeFeaturing()">createTypeFeaturing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Type Featuring</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createUnioning()">createUnioning</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a new object of class '<em>Unioning</em>'.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.InitializingElementsFactory</h3>
<code>create, initializeElement</code></div>
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
<section class="detail" id="createAnnotatingElement()">
<h3>createAnnotatingElement</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></span> <span class="element-name">createAnnotatingElement</span>()</div>
<div class="block">Returns a new object of class '<em>Annotating Element</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Annotating Element</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnnotation()">
<h3>createAnnotation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></span> <span class="element-name">createAnnotation</span>()</div>
<div class="block">Returns a new object of class '<em>Annotation</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Annotation</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociation()">
<h3>createAssociation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a></span> <span class="element-name">createAssociation</span>()</div>
<div class="block">Returns a new object of class '<em>Association</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Association</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAssociationStructure()">
<h3>createAssociationStructure</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/AssociationStructure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AssociationStructure</a></span> <span class="element-name">createAssociationStructure</span>()</div>
<div class="block">Returns a new object of class '<em>Association Structure</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Association Structure</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBehavior()">
<h3>createBehavior</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Behavior</a></span> <span class="element-name">createBehavior</span>()</div>
<div class="block">Returns a new object of class '<em>Behavior</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Behavior</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBindingConnector()">
<h3>createBindingConnector</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BindingConnector</a></span> <span class="element-name">createBindingConnector</span>()</div>
<div class="block">Returns a new object of class '<em>Binding Connector</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Binding Connector</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBooleanExpression()">
<h3>createBooleanExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/BooleanExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">BooleanExpression</a></span> <span class="element-name">createBooleanExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Boolean Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Boolean Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClass()">
<h3>createClass</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Class.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Class</a></span> <span class="element-name">createClass</span>()</div>
<div class="block">Returns a new object of class '<em>Class</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Class</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassifier()">
<h3>createClassifier</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Classifier.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Classifier</a></span> <span class="element-name">createClassifier</span>()</div>
<div class="block">Returns a new object of class '<em>Classifier</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Classifier</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollectExpression()">
<h3>createCollectExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/CollectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CollectExpression</a></span> <span class="element-name">createCollectExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Collect Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Collect Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComment()">
<h3>createComment</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Comment.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Comment</a></span> <span class="element-name">createComment</span>()</div>
<div class="block">Returns a new object of class '<em>Comment</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Comment</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConjugation()">
<h3>createConjugation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Conjugation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Conjugation</a></span> <span class="element-name">createConjugation</span>()</div>
<div class="block">Returns a new object of class '<em>Conjugation</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Conjugation</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConnector()">
<h3>createConnector</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a></span> <span class="element-name">createConnector</span>()</div>
<div class="block">Returns a new object of class '<em>Connector</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Connector</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConstructorExpression()">
<h3>createConstructorExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/ConstructorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ConstructorExpression</a></span> <span class="element-name">createConstructorExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Constructor Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Constructor Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCrossSubsetting()">
<h3>createCrossSubsetting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/CrossSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">CrossSubsetting</a></span> <span class="element-name">createCrossSubsetting</span>()</div>
<div class="block">Returns a new object of class '<em>Cross Subsetting</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Cross Subsetting</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataType()">
<h3>createDataType</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/DataType.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">DataType</a></span> <span class="element-name">createDataType</span>()</div>
<div class="block">Returns a new object of class '<em>Data Type</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Data Type</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDependency()">
<h3>createDependency</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a></span> <span class="element-name">createDependency</span>()</div>
<div class="block">Returns a new object of class '<em>Dependency</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Dependency</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDifferencing()">
<h3>createDifferencing</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Differencing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Differencing</a></span> <span class="element-name">createDifferencing</span>()</div>
<div class="block">Returns a new object of class '<em>Differencing</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Differencing</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDisjoining()">
<h3>createDisjoining</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Disjoining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Disjoining</a></span> <span class="element-name">createDisjoining</span>()</div>
<div class="block">Returns a new object of class '<em>Disjoining</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Disjoining</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDocumentation()">
<h3>createDocumentation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a></span> <span class="element-name">createDocumentation</span>()</div>
<div class="block">Returns a new object of class '<em>Documentation</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Documentation</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementFilterMembership()">
<h3>createElementFilterMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a></span> <span class="element-name">createElementFilterMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Element Filter Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Element Filter Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEndFeatureMembership()">
<h3>createEndFeatureMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a></span> <span class="element-name">createEndFeatureMembership</span>()</div>
<div class="block">Returns a new object of class '<em>End Feature Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>End Feature Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExpression()">
<h3>createExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">createExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeature()">
<h3>createFeature</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">createFeature</span>()</div>
<div class="block">Returns a new object of class '<em>Feature</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureChainExpression()">
<h3>createFeatureChainExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></span> <span class="element-name">createFeatureChainExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Chain Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Chain Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureChaining()">
<h3>createFeatureChaining</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a></span> <span class="element-name">createFeatureChaining</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Chaining</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Chaining</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureInverting()">
<h3>createFeatureInverting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureInverting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureInverting</a></span> <span class="element-name">createFeatureInverting</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Inverting</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Inverting</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureMembership()">
<h3>createFeatureMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></span> <span class="element-name">createFeatureMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureReferenceExpression()">
<h3>createFeatureReferenceExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></span> <span class="element-name">createFeatureReferenceExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Reference Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Reference Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureTyping()">
<h3>createFeatureTyping</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></span> <span class="element-name">createFeatureTyping</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Typing</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Typing</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureValue()">
<h3>createFeatureValue</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">createFeatureValue</span>()</div>
<div class="block">Returns a new object of class '<em>Feature Value</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Feature Value</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlow()">
<h3>createFlow</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a></span> <span class="element-name">createFlow</span>()</div>
<div class="block">Returns a new object of class '<em>Flow</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Flow</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFlowEnd()">
<h3>createFlowEnd</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/FlowEnd.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FlowEnd</a></span> <span class="element-name">createFlowEnd</span>()</div>
<div class="block">Returns a new object of class '<em>Flow End</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Flow End</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFunction()">
<h3>createFunction</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a></span> <span class="element-name">createFunction</span>()</div>
<div class="block">Returns a new object of class '<em>Function</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Function</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIndexExpression()">
<h3>createIndexExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/IndexExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">IndexExpression</a></span> <span class="element-name">createIndexExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Index Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Index Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteraction()">
<h3>createInteraction</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Interaction.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Interaction</a></span> <span class="element-name">createInteraction</span>()</div>
<div class="block">Returns a new object of class '<em>Interaction</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Interaction</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIntersecting()">
<h3>createIntersecting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Intersecting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Intersecting</a></span> <span class="element-name">createIntersecting</span>()</div>
<div class="block">Returns a new object of class '<em>Intersecting</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Intersecting</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInvariant()">
<h3>createInvariant</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Invariant.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Invariant</a></span> <span class="element-name">createInvariant</span>()</div>
<div class="block">Returns a new object of class '<em>Invariant</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Invariant</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInvocationExpression()">
<h3>createInvocationExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></span> <span class="element-name">createInvocationExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Invocation Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Invocation Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLibraryPackage()">
<h3>createLibraryPackage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LibraryPackage.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LibraryPackage</a></span> <span class="element-name">createLibraryPackage</span>()</div>
<div class="block">Returns a new object of class '<em>Library Package</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Library Package</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralBoolean()">
<h3>createLiteralBoolean</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LiteralBoolean.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralBoolean</a></span> <span class="element-name">createLiteralBoolean</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Boolean</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Boolean</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralExpression()">
<h3>createLiteralExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a></span> <span class="element-name">createLiteralExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralInfinity()">
<h3>createLiteralInfinity</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInfinity</a></span> <span class="element-name">createLiteralInfinity</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Infinity</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Infinity</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralInteger()">
<h3>createLiteralInteger</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LiteralInteger.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralInteger</a></span> <span class="element-name">createLiteralInteger</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Integer</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Integer</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralRational()">
<h3>createLiteralRational</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LiteralRational.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralRational</a></span> <span class="element-name">createLiteralRational</span>()</div>
<div class="block">Returns a new object of class '<em>Literal Rational</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal Rational</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLiteralString()">
<h3>createLiteralString</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/LiteralString.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralString</a></span> <span class="element-name">createLiteralString</span>()</div>
<div class="block">Returns a new object of class '<em>Literal String</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Literal String</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMembership()">
<h3>createMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">createMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMembershipImport()">
<h3>createMembershipImport</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a></span> <span class="element-name">createMembershipImport</span>()</div>
<div class="block">Returns a new object of class '<em>Membership Import</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Membership Import</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetaclass()">
<h3>createMetaclass</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a></span> <span class="element-name">createMetaclass</span>()</div>
<div class="block">Returns a new object of class '<em>Metaclass</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Metaclass</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetadataAccessExpression()">
<h3>createMetadataAccessExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></span> <span class="element-name">createMetadataAccessExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Metadata Access Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Metadata Access Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetadataFeature()">
<h3>createMetadataFeature</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">createMetadataFeature</span>()</div>
<div class="block">Returns a new object of class '<em>Metadata Feature</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Metadata Feature</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicity()">
<h3>createMultiplicity</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></span> <span class="element-name">createMultiplicity</span>()</div>
<div class="block">Returns a new object of class '<em>Multiplicity</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Multiplicity</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityRange()">
<h3>createMultiplicityRange</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></span> <span class="element-name">createMultiplicityRange</span>()</div>
<div class="block">Returns a new object of class '<em>Multiplicity Range</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Multiplicity Range</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNamespace()">
<h3>createNamespace</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">createNamespace</span>()</div>
<div class="block">Returns a new object of class '<em>Namespace</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Namespace</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNamespaceImport()">
<h3>createNamespaceImport</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a></span> <span class="element-name">createNamespaceImport</span>()</div>
<div class="block">Returns a new object of class '<em>Namespace Import</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Namespace Import</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNullExpression()">
<h3>createNullExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/NullExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NullExpression</a></span> <span class="element-name">createNullExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Null Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Null Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperatorExpression()">
<h3>createOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createOperatorExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Operator Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Operator Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOwningMembership()">
<h3>createOwningMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></span> <span class="element-name">createOwningMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Owning Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Owning Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackage()">
<h3>createPackage</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></span> <span class="element-name">createPackage</span>()</div>
<div class="block">Returns a new object of class '<em>Package</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Package</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameterMembership()">
<h3>createParameterMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a></span> <span class="element-name">createParameterMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Parameter Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Parameter Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPayloadFeature()">
<h3>createPayloadFeature</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">PayloadFeature</a></span> <span class="element-name">createPayloadFeature</span>()</div>
<div class="block">Returns a new object of class '<em>Payload Feature</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Payload Feature</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPredicate()">
<h3>createPredicate</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Predicate.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Predicate</a></span> <span class="element-name">createPredicate</span>()</div>
<div class="block">Returns a new object of class '<em>Predicate</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Predicate</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRedefinition()">
<h3>createRedefinition</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Redefinition</a></span> <span class="element-name">createRedefinition</span>()</div>
<div class="block">Returns a new object of class '<em>Redefinition</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Redefinition</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReferenceSubsetting()">
<h3>createReferenceSubsetting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/ReferenceSubsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReferenceSubsetting</a></span> <span class="element-name">createReferenceSubsetting</span>()</div>
<div class="block">Returns a new object of class '<em>Reference Subsetting</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Reference Subsetting</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createResultExpressionMembership()">
<h3>createResultExpressionMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a></span> <span class="element-name">createResultExpressionMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Result Expression Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Result Expression Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReturnParameterMembership()">
<h3>createReturnParameterMembership</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a></span> <span class="element-name">createReturnParameterMembership</span>()</div>
<div class="block">Returns a new object of class '<em>Return Parameter Membership</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Return Parameter Membership</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSelectExpression()">
<h3>createSelectExpression</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/SelectExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SelectExpression</a></span> <span class="element-name">createSelectExpression</span>()</div>
<div class="block">Returns a new object of class '<em>Select Expression</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Select Expression</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSpecialization()">
<h3>createSpecialization</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></span> <span class="element-name">createSpecialization</span>()</div>
<div class="block">Returns a new object of class '<em>Specialization</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Specialization</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStep()">
<h3>createStep</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Step</a></span> <span class="element-name">createStep</span>()</div>
<div class="block">Returns a new object of class '<em>Step</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Step</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStructure()">
<h3>createStructure</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Structure.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Structure</a></span> <span class="element-name">createStructure</span>()</div>
<div class="block">Returns a new object of class '<em>Structure</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Structure</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSubclassification()">
<h3>createSubclassification</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Subclassification.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subclassification</a></span> <span class="element-name">createSubclassification</span>()</div>
<div class="block">Returns a new object of class '<em>Subclassification</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Subclassification</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSubsetting()">
<h3>createSubsetting</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></span> <span class="element-name">createSubsetting</span>()</div>
<div class="block">Returns a new object of class '<em>Subsetting</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Subsetting</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSuccession()">
<h3>createSuccession</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Succession</a></span> <span class="element-name">createSuccession</span>()</div>
<div class="block">Returns a new object of class '<em>Succession</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Succession</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSuccessionFlow()">
<h3>createSuccessionFlow</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/SuccessionFlow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">SuccessionFlow</a></span> <span class="element-name">createSuccessionFlow</span>()</div>
<div class="block">Returns a new object of class '<em>Succession Flow</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Succession Flow</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTextualRepresentation()">
<h3>createTextualRepresentation</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/TextualRepresentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TextualRepresentation</a></span> <span class="element-name">createTextualRepresentation</span>()</div>
<div class="block">Returns a new object of class '<em>Textual Representation</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Textual Representation</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createType()">
<h3>createType</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">createType</span>()</div>
<div class="block">Returns a new object of class '<em>Type</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Type</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTypeFeaturing()">
<h3>createTypeFeaturing</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/TypeFeaturing.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">TypeFeaturing</a></span> <span class="element-name">createTypeFeaturing</span>()</div>
<div class="block">Returns a new object of class '<em>Type Featuring</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Type Featuring</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUnioning()">
<h3>createUnioning</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="kerml/Unioning.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Unioning</a></span> <span class="element-name">createUnioning</span>()</div>
<div class="block">Returns a new object of class '<em>Unioning</em>'.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Unioning</em>'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.Class)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="type-parameters">&lt;T extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; aClass)</span></div>
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
