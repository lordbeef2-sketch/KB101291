# JAVA OPENAPI: Classifier (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Classifier.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Classifier.html`
- source_sha256: `e718c1e6afd29a8ad2b311794c6d3437b117f0cc67fce7470170ebf9f02feac0`
- captured_utc: `2026-07-14T16:58:53.044459+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Classifier

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[Actor](../../mdusecases/Actor.html)`, `[Artifact](../../deployments/mdartifacts/Artifact.html)`, `[Association](Association.html)`, `[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[Class](Class.html)`, `[Collaboration](../../compositestructures/mdcollaborations/Collaboration.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[DataType](DataType.html)`, `[DeploymentSpecification](../../deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](Enumeration.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[Extension](../../mdprofiles/Extension.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[Interface](../mdinterfaces/Interface.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[PrimitiveType](PrimitiveType.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[Signal](../../commonbehaviors/mdcommunications/Signal.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[UseCase](../../mdusecases/UseCase.html)`

public interfaceClassifierextends [Type](Type.html), [Namespace](Namespace.html), [RedefinableElement](RedefinableElement.html), [TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)

begin-user-doc 
 A representation of the model object '***Classifier***'.
 end-user-doc 
begin-model-doc 
 A Classifier represents a classification of instances according to their Features.
 end-model-doc 
The following features are supported:
 [`*redefinable Element Of Redefinition Context*`](#get_redefinableElementOfRedefinitionContext())
[`*Use Case*`](#getUseCase())
[`*Owned Use Case*`](#getOwnedUseCase())
[`*Feature*`](#getFeature())
[`*interface Of Nested Classifier*`](#get_interfaceOfNestedClassifier())
[`*read Extent Action Of Classifier*`](#get_readExtentActionOfClassifier())
[`*create Object Action Of Classifier*`](#get_createObjectActionOfClassifier())
[`*unmarshall Action Of Unmarshall Type*`](#get_unmarshallActionOfUnmarshallType())
[`*read Is Classified Object Action Of Classifier*`](#get_readIsClassifiedObjectActionOfClassifier())
[`*Representation*`](#getRepresentation())
[`*Collaboration Use*`](#getCollaborationUse())
[`*component Realization Of Realizing Classifier*`](#get_componentRealizationOfRealizingClassifier())
[`*Attribute*`](#getAttribute())
[`*exception Handler Of Exception Type*`](#get_exceptionHandlerOfExceptionType())
[`*reclassify Object Action Of New Classifier*`](#get_reclassifyObjectActionOfNewClassifier())
[`*reclassify Object Action Of Old Classifier*`](#get_reclassifyObjectActionOfOldClassifier())
[`*UML Class*`](#getUMLClass())
[`*General*`](#getGeneral())
[`*Generalization*`](#getGeneralization())
[`*generalization Of General*`](#get_generalizationOfGeneral())
[`*Powertype Extent*`](#getPowertypeExtent())
[`*Inherited Member*`](#getInheritedMember())
[`*Abstract*`](#isAbstract())
[`*Final Specialization*`](#isFinalSpecialization())
[`*Redefined Classifier*`](#getRedefinedClassifier())
[`*classifier Of Redefined Classifier*`](#get_classifierOfRedefinedClassifier())
[`*Substitution*`](#getSubstitution())
[`*substitution Of Contract*`](#get_substitutionOfContract())
[`*classifier Template Parameter Of Constraining Classifier*`](#get_classifierTemplateParameterOfConstrainingClassifier())
[`*information Item Of Represented*`](#get_informationItemOfRepresented())
[`*instance Specification Of Classifier*`](#get_instanceSpecificationOfClassifier())
[`*information Flow Of Conveyed*`](#get_informationFlowOfConveyed())

See Also:
[`UMLPackage.getClassifier()`](../../metadata/UMLPackage.html#getClassifier())
Model:
abstract="true"
 annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)>`
`[get_classifierOfRedefinedClassifier](#get_classifierOfRedefinedClassifier())()`
Returns the value of the '***classifier Of Redefined Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)>`
`[get_classifierTemplateParameterOfConstrainingClassifier](#get_classifierTemplateParameterOfConstrainingClassifier())()`
Returns the value of the '***classifier Template Parameter Of Constraining Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ComponentRealization](../../components/mdbasiccomponents/ComponentRealization.html)>`
`[get_componentRealizationOfRealizingClassifier](#get_componentRealizationOfRealizingClassifier())()`
Returns the value of the '***component Realization Of Realizing Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[CreateObjectAction](../../actions/mdintermediateactions/CreateObjectAction.html)>`
`[get_createObjectActionOfClassifier](#get_createObjectActionOfClassifier())()`
Returns the value of the '***create Object Action Of Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../../activities/mdextrastructuredactivities/ExceptionHandler.html)>`
`[get_exceptionHandlerOfExceptionType](#get_exceptionHandlerOfExceptionType())()`
Returns the value of the '***exception Handler Of Exception Type***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Generalization](Generalization.html)>`
`[get_generalizationOfGeneral](#get_generalizationOfGeneral())()`
Returns the value of the '***generalization Of General***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)>`
`[get_informationFlowOfConveyed](#get_informationFlowOfConveyed())()`
Returns the value of the '***information Flow Of Conveyed***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)>`
`[get_informationItemOfRepresented](#get_informationItemOfRepresented())()`
Returns the value of the '***information Item Of Represented***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](InstanceSpecification.html)>`
`[get_instanceSpecificationOfClassifier](#get_instanceSpecificationOfClassifier())()`
Returns the value of the '***instance Specification Of Classifier***' reference list.
`[Interface](../mdinterfaces/Interface.html)`
`[get_interfaceOfNestedClassifier](#get_interfaceOfNestedClassifier())()`
Returns the value of the '***interface Of Nested Classifier***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReadExtentAction](../../actions/mdcompleteactions/ReadExtentAction.html)>`
`[get_readExtentActionOfClassifier](#get_readExtentActionOfClassifier())()`
Returns the value of the '***read Extent Action Of Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReadIsClassifiedObjectAction](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)>`
`[get_readIsClassifiedObjectActionOfClassifier](#get_readIsClassifiedObjectActionOfClassifier())()`
Returns the value of the '***read Is Classified Object Action Of Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)>`
`[get_reclassifyObjectActionOfNewClassifier](#get_reclassifyObjectActionOfNewClassifier())()`
Returns the value of the '***reclassify Object Action Of New Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)>`
`[get_reclassifyObjectActionOfOldClassifier](#get_reclassifyObjectActionOfOldClassifier())()`
Returns the value of the '***reclassify Object Action Of Old Classifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RedefinableElement](RedefinableElement.html)>`
`[get_redefinableElementOfRedefinitionContext](#get_redefinableElementOfRedefinitionContext())()`
Returns the value of the '***redefinable Element Of Redefinition Context***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Substitution](../mddependencies/Substitution.html)>`
`[get_substitutionOfContract](#get_substitutionOfContract())()`
Returns the value of the '***substitution Of Contract***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[UnmarshallAction](../../actions/mdcompleteactions/UnmarshallAction.html)>`
`[get_unmarshallActionOfUnmarshallType](#get_unmarshallActionOfUnmarshallType())()`
Returns the value of the '***unmarshall Action Of Unmarshall Type***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getAttribute](#getAttribute())()`
Returns the value of the '***Attribute***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html)>`
`[getCollaborationUse](#getCollaborationUse())()`
Returns the value of the '***Collaboration Use***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](Feature.html)>`
`[getFeature](#getFeature())()`
Returns the value of the '***Feature***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)>`
`[getGeneral](#getGeneral())()`
Returns the value of the '***General***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Generalization](Generalization.html)>`
`[getGeneralization](#getGeneralization())()`
Returns the value of the '***Generalization***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[NamedElement](NamedElement.html)>`
`[getInheritedMember](#getInheritedMember())()`
Returns the value of the '***Inherited Member***' reference list.
`[RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`
`[getOwnedTemplateSignature](#getOwnedTemplateSignature())()`
Returns the value of the '***Owned Template Signature***' containment reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[UseCase](../../mdusecases/UseCase.html)>`
`[getOwnedUseCase](#getOwnedUseCase())()`
Returns the value of the '***Owned Use Case***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[GeneralizationSet](../mdpowertypes/GeneralizationSet.html)>`
`[getPowertypeExtent](#getPowertypeExtent())()`
Returns the value of the '***Powertype Extent***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)>`
`[getRedefinedClassifier](#getRedefinedClassifier())()`
Returns the value of the '***Redefined Classifier***' reference list.
`[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html)`
`[getRepresentation](#getRepresentation())()`
Returns the value of the '***Representation***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Substitution](../mddependencies/Substitution.html)>`
`[getSubstitution](#getSubstitution())()`
Returns the value of the '***Substitution***' containment reference list.
`[ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)`
`[getTemplateParameter](#getTemplateParameter())()`
Returns the value of the '***Template Parameter***' reference.
`[Class](Class.html)`
`[getUMLClass](#getUMLClass())()`
Returns the value of the '***UML Class***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[UseCase](../../mdusecases/UseCase.html)>`
`[getUseCase](#getUseCase())()`
Returns the value of the '***Use Case***' reference list.
`boolean`
`[has_classifierOfRedefinedClassifier](#has_classifierOfRedefinedClassifier())()`

`boolean`
`[has_classifierTemplateParameterOfConstrainingClassifier](#has_classifierTemplateParameterOfConstrainingClassifier())()`

`boolean`
`[has_componentRealizationOfRealizingClassifier](#has_componentRealizationOfRealizingClassifier())()`

`boolean`
`[has_createObjectActionOfClassifier](#has_createObjectActionOfClassifier())()`

`boolean`
`[has_exceptionHandlerOfExceptionType](#has_exceptionHandlerOfExceptionType())()`

`boolean`
`[has_generalizationOfGeneral](#has_generalizationOfGeneral())()`

`boolean`
`[has_informationFlowOfConveyed](#has_informationFlowOfConveyed())()`

`boolean`
`[has_informationItemOfRepresented](#has_informationItemOfRepresented())()`

`boolean`
`[has_instanceSpecificationOfClassifier](#has_instanceSpecificationOfClassifier())()`

`boolean`
`[has_readExtentActionOfClassifier](#has_readExtentActionOfClassifier())()`

`boolean`
`[has_readIsClassifiedObjectActionOfClassifier](#has_readIsClassifiedObjectActionOfClassifier())()`

`boolean`
`[has_reclassifyObjectActionOfNewClassifier](#has_reclassifyObjectActionOfNewClassifier())()`

`boolean`
`[has_reclassifyObjectActionOfOldClassifier](#has_reclassifyObjectActionOfOldClassifier())()`

`boolean`
`[has_redefinableElementOfRedefinitionContext](#has_redefinableElementOfRedefinitionContext())()`

`boolean`
`[has_substitutionOfContract](#has_substitutionOfContract())()`

`boolean`
`[has_unmarshallActionOfUnmarshallType](#has_unmarshallActionOfUnmarshallType())()`

`boolean`
`[hasAttribute](#hasAttribute())()`

`boolean`
`[hasCollaborationUse](#hasCollaborationUse())()`

`boolean`
`[hasFeature](#hasFeature())()`

`boolean`
`[hasGeneral](#hasGeneral())()`

`boolean`
`[hasGeneralization](#hasGeneralization())()`

`boolean`
`[hasInheritedMember](#hasInheritedMember())()`

`boolean`
`[hasOwnedUseCase](#hasOwnedUseCase())()`

`boolean`
`[hasPowertypeExtent](#hasPowertypeExtent())()`

`boolean`
`[hasRedefinedClassifier](#hasRedefinedClassifier())()`

`boolean`
`[hasSubstitution](#hasSubstitution())()`

`boolean`
`[hasUseCase](#hasUseCase())()`

`boolean`
`[isAbstract](#isAbstract())()`
Returns the value of the '***Abstract***' attribute.
`boolean`
`[isFinalSpecialization](#isFinalSpecialization())()`
Returns the value of the '***Final Specialization***' attribute.
`void`
`[set_interfaceOfNestedClassifier](#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([Interface](../mdinterfaces/Interface.html) value)`
Sets the value of the
 '[`*interface Of Nested Classifier*`](#get_interfaceOfNestedClassifier())' container reference.
`void`
`[setAbstract](#setAbstract(boolean))(boolean value)`
Sets the value of the '[`*Abstract*`](#isAbstract())' attribute.
`void`
`[setFinalSpecialization](#setFinalSpecialization(boolean))(boolean value)`
Sets the value of the '[`*Final Specialization*`](#isFinalSpecialization())' attribute.
`void`
`[setOwnedTemplateSignature](#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature))([RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) value)`
Sets the value of the '[`*Owned Template Signature*`](#getOwnedTemplateSignature())'
 containment reference.
`void`
`[setRepresentation](#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse))([CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html) value)`
Sets the value of the '[`*Representation*`](#getRepresentation())' reference.
`void`
`[setTemplateParameter](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter))([ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) value)`
Sets the value of the '[`*Template Parameter*`](#getTemplateParameter())' reference.
`void`
`[setUMLClass](#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](Class.html) value)`
Sets the value of the '[`*UML Class*`](#getUMLClass())' container reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](NamedElement.html#getClientDependency()), [getName](NamedElement.html#getName()), [getNameExpression](NamedElement.html#getNameExpression()), [getNamespace](NamedElement.html#getNamespace()), [getQualifiedName](NamedElement.html#getQualifiedName()), [getSupplierDependency](NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](NamedElement.html#hasClientDependency()), [hasSupplierDependency](NamedElement.html#hasSupplierDependency()), [setName](NamedElement.html#setName(java.lang.String)), [setNameExpression](NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](Namespace.html)
`[getElementImport](Namespace.html#getElementImport()), [getImportedMember](Namespace.html#getImportedMember()), [getMember](Namespace.html#getMember()), [getOwnedDiagram](Namespace.html#getOwnedDiagram()), [getOwnedMember](Namespace.html#getOwnedMember()), [getOwnedRule](Namespace.html#getOwnedRule()), [getPackageImport](Namespace.html#getPackageImport()), [hasElementImport](Namespace.html#hasElementImport()), [hasImportedMember](Namespace.html#hasImportedMember()), [hasMember](Namespace.html#hasMember()), [hasOwnedDiagram](Namespace.html#hasOwnedDiagram()), [hasOwnedMember](Namespace.html#hasOwnedMember()), [hasOwnedRule](Namespace.html#hasOwnedRule()), [hasPackageImport](Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](PackageableElement.html)
`[get_componentOfPackagedElement](PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](PackageableElement.html#getOwningPackage()), [getVisibility](PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](RedefinableElement.html#hasRedefinitionContext()), [isLeaf](RedefinableElement.html#isLeaf()), [setLeaf](RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](Type.html)
`[get_associationOfEndType](Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](Type.html#get_operationOfRaisedException()), [get_typedElementOfType](Type.html#get_typedElementOfType()), [getPackage](Type.html#getPackage()), [has_associationOfEndType](Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](Type.html#has_operationOfRaisedException()), [has_typedElementOfType](Type.html#has_typedElementOfType()), [setPackage](Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
getGeneralization
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Generalization](Generalization.html)> getGeneralization()
Returns the value of the '***Generalization***' containment reference list.
 The list contents are of type [`Generalization`](Generalization.html).
 It is bidirectional and its opposite is '[`*Specific*`](Generalization.html#getSpecific())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Generalization relationships for this Classifier. These Generalizations navigate to more general Classifiers in the generalization hierarchy.
 end-model-doc
Returns:
the value of the '*Generalization*' containment reference list.
See Also:
[`UMLPackage.getClassifier_Generalization()`](../../metadata/UMLPackage.html#getClassifier_Generalization())
[`Generalization.getSpecific()`](Generalization.html#getSpecific())
Model:
opposite="specific" containment="true" resolveProxies="true" ordered="false"
Generated:
get_generalizationOfGeneral
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Generalization](Generalization.html)> get_generalizationOfGeneral()
Returns the value of the '***generalization Of General***' reference list.
 The list contents are of type [`Generalization`](Generalization.html).
 It is bidirectional and its opposite is '[`*General*`](Generalization.html#getGeneral())'.
 begin-user-doc 
If the meaning of the '*generalization Of General*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*generalization Of General*' reference list.
See Also:
[`UMLPackage.getClassifier__generalizationOfGeneral()`](../../metadata/UMLPackage.html#getClassifier__generalizationOfGeneral())
[`Generalization.getGeneral()`](Generalization.html#getGeneral())
Model:
opposite="general" ordered="false"
Generated:
getPowertypeExtent
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[GeneralizationSet](../mdpowertypes/GeneralizationSet.html)> getPowertypeExtent()
Returns the value of the '***Powertype Extent***' reference list.
 The list contents are of type [`GeneralizationSet`](../mdpowertypes/GeneralizationSet.html).
 It is bidirectional and its opposite is '[`*Powertype*`](../mdpowertypes/GeneralizationSet.html#getPowertype())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The GeneralizationSet of which this Classifier is a power type.
 end-model-doc
Returns:
the value of the '*Powertype Extent*' reference list.
See Also:
[`UMLPackage.getClassifier_PowertypeExtent()`](../../metadata/UMLPackage.html#getClassifier_PowertypeExtent())
[`GeneralizationSet.getPowertype()`](../mdpowertypes/GeneralizationSet.html#getPowertype())
Model:
opposite="powertype" ordered="false"
Generated:
getFeature
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](Feature.html)> getFeature()
Returns the value of the '***Feature***' reference list.
 The list contents are of type [`Feature`](Feature.html).
 It is bidirectional and its opposite is '[`*Featuring Classifier*`](Feature.html#getFeaturingClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies each Feature directly defined in the classifier. Note that there may be members of the Classifier that are of the type Feature but are not included, e
 .g., inherited features.
 end-model-doc
Returns:
the value of the '*Feature*' reference list.
See Also:
[`UMLPackage.getClassifier_Feature()`](../../metadata/UMLPackage.html#getClassifier_Feature())
[`Feature.getFeaturingClassifier()`](Feature.html#getFeaturingClassifier())
Model:
opposite="featuringClassifier" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getInheritedMember
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[NamedElement](NamedElement.html)> getInheritedMember()
Returns the value of the '***Inherited Member***' reference list.
 The list contents are of type [`NamedElement`](NamedElement.html).
 It is bidirectional and its opposite is
 '
invalid reference
`*classifier Of Inherited Member*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 All elements inherited by this Classifier from its general Classifiers.
 end-model-doc
Returns:
the value of the '*Inherited Member*' reference list.
See Also:
[`UMLPackage.getClassifier_InheritedMember()`](../../metadata/UMLPackage.html#getClassifier_InheritedMember())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement#get_classifierOfInheritedMember`
Model:
opposite="_classifierOfInheritedMember" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isAbstract
boolean isAbstract()
Returns the value of the '***Abstract***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, the Classifier can only be instantiated by instantiating one of its specializations. An abstract Classifier is intended to be used by other Classifiers
 e.g., as the target of Associations or Generalizations.
 end-model-doc
Returns:
the value of the '*Abstract*' attribute.
See Also:
[`setAbstract(boolean)`](#setAbstract(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getClassifier_Abstract()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setAbstract
void setAbstract(boolean value)
Sets the value of the '[`*Abstract*`](#isAbstract())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Abstract*' attribute.
See Also:
[`isAbstract()`](#isAbstract())
Generated:
isFinalSpecialization
boolean isFinalSpecialization()
Returns the value of the '***Final Specialization***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, the Classifier cannot be specialized.
 end-model-doc
Returns:
the value of the '*Final Specialization*' attribute.
See Also:
[`setFinalSpecialization(boolean)`](#setFinalSpecialization(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getClassifier_FinalSpecialization()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setFinalSpecialization
void setFinalSpecialization(boolean value)
Sets the value of the '[`*Final Specialization*`](#isFinalSpecialization())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Final Specialization*' attribute.
See Also:
[`isFinalSpecialization()`](#isFinalSpecialization())
Generated:
getAttribute
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getAttribute()
Returns the value of the '***Attribute***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*Classifier*`](Property.html#getClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 All of the Properties that are direct (i.e., not inherited or imported) attributes of the Classifier.
 end-model-doc
Returns:
the value of the '*Attribute*' reference list.
See Also:
[`UMLPackage.getClassifier_Attribute()`](../../metadata/UMLPackage.html#getClassifier_Attribute())
[`Property.getClassifier()`](Property.html#getClassifier())
Model:
opposite="classifier" transient="true" volatile="true" derived="true"
Generated:
getRedefinedClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)> getRedefinedClassifier()
Returns the value of the '***Redefined Classifier***' reference list.
 The list contents are of type [`Classifier`](Classifier.html).
 It is bidirectional and its opposite is
 '[`*classifier Of Redefined Classifier*`](#get_classifierOfRedefinedClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Classifiers redefined by this Classifier.
 end-model-doc
Returns:
the value of the '*Redefined Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier_RedefinedClassifier()`](../../metadata/UMLPackage.html#getClassifier_RedefinedClassifier())
[`get_classifierOfRedefinedClassifier()`](#get_classifierOfRedefinedClassifier())
Model:
opposite="_classifierOfRedefinedClassifier" ordered="false"
Generated:
get_classifierOfRedefinedClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)> get_classifierOfRedefinedClassifier()
Returns the value of the '***classifier Of Redefined Classifier***' reference list.
 The list contents are of type [`Classifier`](Classifier.html).
 It is bidirectional and its opposite is '[`*Redefined Classifier*`](#getRedefinedClassifier())'.
 begin-user-doc 
If the meaning of the '*classifier Of Redefined Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*classifier Of Redefined Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__classifierOfRedefinedClassifier()`](../../metadata/UMLPackage.html#getClassifier__classifierOfRedefinedClassifier())
[`getRedefinedClassifier()`](#getRedefinedClassifier())
Model:
opposite="redefinedClassifier" ordered="false"
Generated:
getGeneral
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)> getGeneral()
Returns the value of the '***General***' reference list.
 The list contents are of type [`Classifier`](Classifier.html).
 It is bidirectional and its opposite is
 '
invalid reference
`*classifier Of General*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The generalizing Classifiers for this Classifier.
 end-model-doc
Returns:
the value of the '*General*' reference list.
See Also:
[`UMLPackage.getClassifier_General()`](../../metadata/UMLPackage.html#getClassifier_General())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_classifierOfGeneral`
Model:
opposite="_classifierOfGeneral" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getSubstitution
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Substitution](../mddependencies/Substitution.html)> getSubstitution()
Returns the value of the '***Substitution***' containment reference list.
 The list contents are of type [`Substitution`](../mddependencies/Substitution.html).
 It is bidirectional and its opposite is
 '[`*Substituting Classifier*`](../mddependencies/Substitution.html#getSubstitutingClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Substitutions owned by this Classifier.
 end-model-doc
Returns:
the value of the '*Substitution*' containment reference list.
See Also:
[`UMLPackage.getClassifier_Substitution()`](../../metadata/UMLPackage.html#getClassifier_Substitution())
[`Substitution.getSubstitutingClassifier()`](../mddependencies/Substitution.html#getSubstitutingClassifier())
Model:
opposite="substitutingClassifier" containment="true" resolveProxies="true" ordered="false"
Generated:
get_substitutionOfContract
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Substitution](../mddependencies/Substitution.html)> get_substitutionOfContract()
Returns the value of the '***substitution Of Contract***' reference list.
 The list contents are of type [`Substitution`](../mddependencies/Substitution.html).
 It is bidirectional and its opposite is '[`*Contract*`](../mddependencies/Substitution.html#getContract())'.
 begin-user-doc 
If the meaning of the '*substitution Of Contract*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*substitution Of Contract*' reference list.
See Also:
[`UMLPackage.getClassifier__substitutionOfContract()`](../../metadata/UMLPackage.html#getClassifier__substitutionOfContract())
[`Substitution.getContract()`](../mddependencies/Substitution.html#getContract())
Model:
opposite="contract" ordered="false"
Generated:
getOwnedUseCase
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[UseCase](../../mdusecases/UseCase.html)> getOwnedUseCase()
Returns the value of the '***Owned Use Case***' containment reference list.
 The list contents are of type [`UseCase`](../../mdusecases/UseCase.html).
 It is bidirectional and its opposite is
 '[`*classifier Of Owned Use Case*`](../../mdusecases/UseCase.html#get_classifierOfOwnedUseCase())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The UseCases owned by this classifier.
 end-model-doc
Returns:
the value of the '*Owned Use Case*' containment reference list.
See Also:
[`UMLPackage.getClassifier_OwnedUseCase()`](../../metadata/UMLPackage.html#getClassifier_OwnedUseCase())
[`UseCase.get_classifierOfOwnedUseCase()`](../../mdusecases/UseCase.html#get_classifierOfOwnedUseCase())
Model:
opposite="_classifierOfOwnedUseCase" containment="true" resolveProxies="true" ordered="false"
Generated:
get_interfaceOfNestedClassifier
@CheckForNull[Interface](../mdinterfaces/Interface.html) get_interfaceOfNestedClassifier()
Returns the value of the '***interface Of Nested Classifier***' container reference.
 It is bidirectional and its opposite is '[`*Nested Classifier*`](../mdinterfaces/Interface.html#getNestedClassifier())'.
 begin-user-doc 
If the meaning of the '*interface Of Nested Classifier*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interface Of Nested Classifier*' container reference.
See Also:
[`set_interfaceOfNestedClassifier(Interface)`](#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))
[`UMLPackage.getClassifier__interfaceOfNestedClassifier()`](../../metadata/UMLPackage.html#getClassifier__interfaceOfNestedClassifier())
[`Interface.getNestedClassifier()`](../mdinterfaces/Interface.html#getNestedClassifier())
Model:
opposite="nestedClassifier" transient="false" ordered="false"
Generated:
set_interfaceOfNestedClassifier
void set_interfaceOfNestedClassifier(@CheckForNull
 [Interface](../mdinterfaces/Interface.html) value)
Sets the value of the
 '[`*interface Of Nested Classifier*`](#get_interfaceOfNestedClassifier())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interface Of Nested Classifier*' container reference.
See Also:
[`get_interfaceOfNestedClassifier()`](#get_interfaceOfNestedClassifier())
Generated:
get_informationItemOfRepresented
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)> get_informationItemOfRepresented()
Returns the value of the '***information Item Of Represented***' reference list.
 The list contents are of type [`InformationItem`](../../auxiliaryconstructs/mdinformationflows/InformationItem.html).
 It is bidirectional and its opposite is
 '[`*Represented*`](../../auxiliaryconstructs/mdinformationflows/InformationItem.html#getRepresented())'.
 begin-user-doc 
If the meaning of the '*information Item Of Represented*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Item Of Represented*' reference list.
See Also:
[`UMLPackage.getClassifier__informationItemOfRepresented()`](../../metadata/UMLPackage.html#getClassifier__informationItemOfRepresented())
[`InformationItem.getRepresented()`](../../auxiliaryconstructs/mdinformationflows/InformationItem.html#getRepresented())
Model:
opposite="represented" ordered="false"
Generated:
get_informationFlowOfConveyed
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)> get_informationFlowOfConveyed()
Returns the value of the '***information Flow Of Conveyed***' reference list.
 The list contents are of type [`InformationFlow`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html).
 It is bidirectional and its opposite is
 '[`*Conveyed*`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getConveyed())'.
 begin-user-doc 
If the meaning of the '*information Flow Of Conveyed*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Flow Of Conveyed*' reference list.
See Also:
[`UMLPackage.getClassifier__informationFlowOfConveyed()`](../../metadata/UMLPackage.html#getClassifier__informationFlowOfConveyed())
[`InformationFlow.getConveyed()`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getConveyed())
Model:
opposite="conveyed" ordered="false"
Generated:
get_exceptionHandlerOfExceptionType
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../../activities/mdextrastructuredactivities/ExceptionHandler.html)> get_exceptionHandlerOfExceptionType()
Returns the value of the '***exception Handler Of Exception Type***' reference list.
 The list contents are of type [`ExceptionHandler`](../../activities/mdextrastructuredactivities/ExceptionHandler.html).
 It is bidirectional and its opposite is
 '[`*Exception Type*`](../../activities/mdextrastructuredactivities/ExceptionHandler.html#getExceptionType())'.
 begin-user-doc 
If the meaning of the '*exception Handler Of Exception Type*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*exception Handler Of Exception Type*' reference list.
See Also:
[`UMLPackage.getClassifier__exceptionHandlerOfExceptionType()`](../../metadata/UMLPackage.html#getClassifier__exceptionHandlerOfExceptionType())
[`ExceptionHandler.getExceptionType()`](../../activities/mdextrastructuredactivities/ExceptionHandler.html#getExceptionType())
Model:
opposite="exceptionType" ordered="false"
Generated:
get_readIsClassifiedObjectActionOfClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReadIsClassifiedObjectAction](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)> get_readIsClassifiedObjectActionOfClassifier()
Returns the value of the '***read Is Classified Object Action Of Classifier***' reference list.
 The list contents are of type [`ReadIsClassifiedObjectAction`](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html).
 It is bidirectional and its opposite is
 '[`*Classifier*`](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html#getClassifier())'.
 begin-user-doc 
If the meaning of the '*read Is Classified Object Action Of Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Is Classified Object Action Of Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__readIsClassifiedObjectActionOfClassifier()`](../../metadata/UMLPackage.html#getClassifier__readIsClassifiedObjectActionOfClassifier())
[`ReadIsClassifiedObjectAction.getClassifier()`](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html#getClassifier())
Model:
opposite="classifier" ordered="false"
Generated:
get_readExtentActionOfClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReadExtentAction](../../actions/mdcompleteactions/ReadExtentAction.html)> get_readExtentActionOfClassifier()
Returns the value of the '***read Extent Action Of Classifier***' reference list.
 The list contents are of type [`ReadExtentAction`](../../actions/mdcompleteactions/ReadExtentAction.html).
 It is bidirectional and its opposite is '[`*Classifier*`](../../actions/mdcompleteactions/ReadExtentAction.html#getClassifier())'.
 begin-user-doc 
If the meaning of the '*read Extent Action Of Classifier*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Extent Action Of Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__readExtentActionOfClassifier()`](../../metadata/UMLPackage.html#getClassifier__readExtentActionOfClassifier())
[`ReadExtentAction.getClassifier()`](../../actions/mdcompleteactions/ReadExtentAction.html#getClassifier())
Model:
opposite="classifier" ordered="false"
Generated:
get_reclassifyObjectActionOfOldClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)> get_reclassifyObjectActionOfOldClassifier()
Returns the value of the '***reclassify Object Action Of Old Classifier***' reference list.
 The list contents are of type [`ReclassifyObjectAction`](../../actions/mdcompleteactions/ReclassifyObjectAction.html).
 It is bidirectional and its opposite is
 '[`*Old Classifier*`](../../actions/mdcompleteactions/ReclassifyObjectAction.html#getOldClassifier())'.
 begin-user-doc 
If the meaning of the '*reclassify Object Action Of Old Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reclassify Object Action Of Old Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__reclassifyObjectActionOfOldClassifier()`](../../metadata/UMLPackage.html#getClassifier__reclassifyObjectActionOfOldClassifier())
[`ReclassifyObjectAction.getOldClassifier()`](../../actions/mdcompleteactions/ReclassifyObjectAction.html#getOldClassifier())
Model:
opposite="oldClassifier" ordered="false"
Generated:
get_reclassifyObjectActionOfNewClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)> get_reclassifyObjectActionOfNewClassifier()
Returns the value of the '***reclassify Object Action Of New Classifier***' reference list.
 The list contents are of type [`ReclassifyObjectAction`](../../actions/mdcompleteactions/ReclassifyObjectAction.html).
 It is bidirectional and its opposite is
 '[`*New Classifier*`](../../actions/mdcompleteactions/ReclassifyObjectAction.html#getNewClassifier())'.
 begin-user-doc 
If the meaning of the '*reclassify Object Action Of New Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reclassify Object Action Of New Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__reclassifyObjectActionOfNewClassifier()`](../../metadata/UMLPackage.html#getClassifier__reclassifyObjectActionOfNewClassifier())
[`ReclassifyObjectAction.getNewClassifier()`](../../actions/mdcompleteactions/ReclassifyObjectAction.html#getNewClassifier())
Model:
opposite="newClassifier" ordered="false"
Generated:
get_unmarshallActionOfUnmarshallType
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[UnmarshallAction](../../actions/mdcompleteactions/UnmarshallAction.html)> get_unmarshallActionOfUnmarshallType()
Returns the value of the '***unmarshall Action Of Unmarshall Type***' reference list.
 The list contents are of type [`UnmarshallAction`](../../actions/mdcompleteactions/UnmarshallAction.html).
 It is bidirectional and its opposite is
 '[`*Unmarshall Type*`](../../actions/mdcompleteactions/UnmarshallAction.html#getUnmarshallType())'.
 begin-user-doc 
If the meaning of the '*unmarshall Action Of Unmarshall Type*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*unmarshall Action Of Unmarshall Type*' reference list.
See Also:
[`UMLPackage.getClassifier__unmarshallActionOfUnmarshallType()`](../../metadata/UMLPackage.html#getClassifier__unmarshallActionOfUnmarshallType())
[`UnmarshallAction.getUnmarshallType()`](../../actions/mdcompleteactions/UnmarshallAction.html#getUnmarshallType())
Model:
opposite="unmarshallType" ordered="false"
Generated:
get_createObjectActionOfClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[CreateObjectAction](../../actions/mdintermediateactions/CreateObjectAction.html)> get_createObjectActionOfClassifier()
Returns the value of the '***create Object Action Of Classifier***' reference list.
 The list contents are of type [`CreateObjectAction`](../../actions/mdintermediateactions/CreateObjectAction.html).
 It is bidirectional and its opposite is
 '[`*Classifier*`](../../actions/mdintermediateactions/CreateObjectAction.html#getClassifier())'.
 begin-user-doc 
If the meaning of the '*create Object Action Of Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*create Object Action Of Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__createObjectActionOfClassifier()`](../../metadata/UMLPackage.html#getClassifier__createObjectActionOfClassifier())
[`CreateObjectAction.getClassifier()`](../../actions/mdintermediateactions/CreateObjectAction.html#getClassifier())
Model:
opposite="classifier" ordered="false"
Generated:
getUMLClass
@CheckForNull[Class](Class.html) getUMLClass()
Returns the value of the '***UML Class***' container reference.
 It is bidirectional and its opposite is '[`*Nested Classifier*`](Class.html#getNestedClassifier())'.
 begin-user-doc 
If the meaning of the '*UML Class*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*UML Class*' container reference.
See Also:
[`setUMLClass(Class)`](#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))
[`UMLPackage.getClassifier_UMLClass()`](../../metadata/UMLPackage.html#getClassifier_UMLClass())
[`Class.getNestedClassifier()`](Class.html#getNestedClassifier())
Model:
opposite="nestedClassifier" transient="false" ordered="false"
Generated:
setUMLClass
void setUMLClass(@CheckForNull
 [Class](Class.html) value)
Sets the value of the '[`*UML Class*`](#getUMLClass())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*UML Class*' container reference.
See Also:
[`getUMLClass()`](#getUMLClass())
Generated:
get_componentRealizationOfRealizingClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ComponentRealization](../../components/mdbasiccomponents/ComponentRealization.html)> get_componentRealizationOfRealizingClassifier()
Returns the value of the '***component Realization Of Realizing Classifier***' reference list.
 The list contents are of type [`ComponentRealization`](../../components/mdbasiccomponents/ComponentRealization.html).
 It is bidirectional and its opposite is
 '[`*Realizing Classifier*`](../../components/mdbasiccomponents/ComponentRealization.html#getRealizingClassifier())'.
 begin-user-doc 
If the meaning of the '*component Realization Of Realizing Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*component Realization Of Realizing Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__componentRealizationOfRealizingClassifier()`](../../metadata/UMLPackage.html#getClassifier__componentRealizationOfRealizingClassifier())
[`ComponentRealization.getRealizingClassifier()`](../../components/mdbasiccomponents/ComponentRealization.html#getRealizingClassifier())
Model:
opposite="realizingClassifier" ordered="false"
Generated:
getCollaborationUse
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html)> getCollaborationUse()
Returns the value of the '***Collaboration Use***' containment reference list.
 The list contents are of type [`CollaborationUse`](../../compositestructures/mdcollaborations/CollaborationUse.html).
 It is bidirectional and its opposite is '
invalid reference
`.mdcollaborations.CollaborationUse#get_classifierOfCollaborationUse *classifier Of Collaboration Use*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The CollaborationUses owned by the Classifier.
 end-model-doc
Returns:
the value of the '*Collaboration Use*' containment reference list.
See Also:
[`UMLPackage.getClassifier_CollaborationUse()`](../../metadata/UMLPackage.html#getClassifier_CollaborationUse())
[`CollaborationUse.get_classifierOfCollaborationUse()`](../../compositestructures/mdcollaborations/CollaborationUse.html#get_classifierOfCollaborationUse())
Model:
opposite="_classifierOfCollaborationUse" containment="true" resolveProxies="true" ordered="false"
Generated:
getRepresentation
@CheckForNull[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html) getRepresentation()
Returns the value of the '***Representation***' reference.
 It is bidirectional and its opposite is '
invalid reference
`.mdcollaborations.CollaborationUse#get_classifierOfRepresentation *classifier Of Representation*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A CollaborationUse which indicates the Collaboration that represents this Classifier.
 end-model-doc
Returns:
the value of the '*Representation*' reference.
See Also:
[`setRepresentation(CollaborationUse)`](#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse))
[`UMLPackage.getClassifier_Representation()`](../../metadata/UMLPackage.html#getClassifier_Representation())
[`CollaborationUse.get_classifierOfRepresentation()`](../../compositestructures/mdcollaborations/CollaborationUse.html#get_classifierOfRepresentation())
Model:
opposite="_classifierOfRepresentation" ordered="false"
Generated:
setRepresentation
void setRepresentation(@CheckForNull
 [CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html) value)
Sets the value of the '[`*Representation*`](#getRepresentation())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Representation*' reference.
See Also:
[`getRepresentation()`](#getRepresentation())
Generated:
getUseCase
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[UseCase](../../mdusecases/UseCase.html)> getUseCase()
Returns the value of the '***Use Case***' reference list.
 The list contents are of type [`UseCase`](../../mdusecases/UseCase.html).
 It is bidirectional and its opposite is '[`*Subject*`](../../mdusecases/UseCase.html#getSubject())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of UseCases for which this Classifier is the subject.
 end-model-doc
Returns:
the value of the '*Use Case*' reference list.
See Also:
[`UMLPackage.getClassifier_UseCase()`](../../metadata/UMLPackage.html#getClassifier_UseCase())
[`UseCase.getSubject()`](../../mdusecases/UseCase.html#getSubject())
Model:
opposite="subject" ordered="false"
Generated:
get_classifierTemplateParameterOfConstrainingClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html)> get_classifierTemplateParameterOfConstrainingClassifier()
Returns the value of the '***classifier Template Parameter Of Constraining Classifier***' reference list.
 The list contents are of type [`ClassifierTemplateParameter`](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html).
 It is bidirectional and its opposite is '
invalid reference
`.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter#getConstrainingClassifier *Constraining Classifier*`
'.
 begin-user-doc 
If the meaning of the '*classifier Template Parameter Of Constraining Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*classifier Template Parameter Of Constraining Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__classifierTemplateParameterOfConstrainingClassifier()`](../../metadata/UMLPackage.html#getClassifier__classifierTemplateParameterOfConstrainingClassifier())
[`ClassifierTemplateParameter.getConstrainingClassifier()`](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html#getConstrainingClassifier())
Model:
opposite="constrainingClassifier" ordered="false"
Generated:
get_instanceSpecificationOfClassifier
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](InstanceSpecification.html)> get_instanceSpecificationOfClassifier()
Returns the value of the '***instance Specification Of Classifier***' reference list.
 The list contents are of type [`InstanceSpecification`](InstanceSpecification.html).
 It is bidirectional and its opposite is '[`*Classifier*`](InstanceSpecification.html#getClassifier())'.
 begin-user-doc 
If the meaning of the '*instance Specification Of Classifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*instance Specification Of Classifier*' reference list.
See Also:
[`UMLPackage.getClassifier__instanceSpecificationOfClassifier()`](../../metadata/UMLPackage.html#getClassifier__instanceSpecificationOfClassifier())
[`InstanceSpecification.getClassifier()`](InstanceSpecification.html#getClassifier())
Model:
opposite="classifier" ordered="false"
Generated:
get_redefinableElementOfRedefinitionContext
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RedefinableElement](RedefinableElement.html)> get_redefinableElementOfRedefinitionContext()
Returns the value of the '***redefinable Element Of Redefinition Context***' reference list.
 The list contents are of type [`RedefinableElement`](RedefinableElement.html).
 It is bidirectional and its opposite is
 '[`*Redefinition Context*`](RedefinableElement.html#getRedefinitionContext())'.
 begin-user-doc 
If the meaning of the '*redefinable Element Of Redefinition Context*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*redefinable Element Of Redefinition Context*' reference list.
See Also:
[`UMLPackage.getClassifier__redefinableElementOfRedefinitionContext()`](../../metadata/UMLPackage.html#getClassifier__redefinableElementOfRedefinitionContext())
[`RedefinableElement.getRedefinitionContext()`](RedefinableElement.html#getRedefinitionContext())
Model:
opposite="redefinitionContext" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getOwnedTemplateSignature
@CheckForNull[RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) getOwnedTemplateSignature()
Returns the value of the '***Owned Template Signature***' containment reference.
 It is bidirectional and its opposite is
 '[`*Classifier*`](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html#getClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The optional RedefinableTemplateSignature specifying the formal template parameters.
 end-model-doc
Specified by:
`[getOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getOwnedTemplateSignature())` in interface `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`
Returns:
the value of the '*Owned Template Signature*' containment reference.
See Also:
[`setOwnedTemplateSignature(RedefinableTemplateSignature)`](#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature))
[`UMLPackage.getClassifier_OwnedTemplateSignature()`](../../metadata/UMLPackage.html#getClassifier_OwnedTemplateSignature())
[`RedefinableTemplateSignature.getClassifier()`](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html#getClassifier())
Model:
opposite="classifier" containment="true" resolveProxies="true" ordered="false"
Generated:
setOwnedTemplateSignature
void setOwnedTemplateSignature(@CheckForNull
 [RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html) value)
Sets the value of the '[`*Owned Template Signature*`](#getOwnedTemplateSignature())'
 containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owned Template Signature*' containment reference.
See Also:
[`getOwnedTemplateSignature()`](#getOwnedTemplateSignature())
Generated:
getTemplateParameter
@CheckForNull[ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) getTemplateParameter()
Returns the value of the '***Template Parameter***' reference.
 It is bidirectional and its opposite is
 '[`*Parametered Element*`](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html#getParameteredElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 TheClassifierTemplateParameter that exposes this element as a formal parameter.
 end-model-doc
Specified by:
`[getTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter())` in interface `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`
Returns:
the value of the '*Template Parameter*' reference.
See Also:
[`setTemplateParameter(ClassifierTemplateParameter)`](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter))
[`UMLPackage.getClassifier_TemplateParameter()`](../../metadata/UMLPackage.html#getClassifier_TemplateParameter())
[`ClassifierTemplateParameter.getParameteredElement()`](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html#getParameteredElement())
Model:
opposite="parameteredElement" ordered="false"
Generated:
setTemplateParameter
void setTemplateParameter(@CheckForNull
 [ClassifierTemplateParameter](../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html) value)
Sets the value of the '[`*Template Parameter*`](#getTemplateParameter())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Template Parameter*' reference.
See Also:
[`getTemplateParameter()`](#getTemplateParameter())
Generated:
hasGeneralization
boolean hasGeneralization()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_generalizationOfGeneral
boolean has_generalizationOfGeneral()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPowertypeExtent
boolean hasPowertypeExtent()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasFeature
boolean hasFeature()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasInheritedMember
boolean hasInheritedMember()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasAttribute
boolean hasAttribute()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedClassifier
boolean hasRedefinedClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_classifierOfRedefinedClassifier
boolean has_classifierOfRedefinedClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasGeneral
boolean hasGeneral()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasSubstitution
boolean hasSubstitution()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_substitutionOfContract
boolean has_substitutionOfContract()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedUseCase
boolean hasOwnedUseCase()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_readExtentActionOfClassifier
boolean has_readExtentActionOfClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationItemOfRepresented
boolean has_informationItemOfRepresented()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationFlowOfConveyed
boolean has_informationFlowOfConveyed()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_exceptionHandlerOfExceptionType
boolean has_exceptionHandlerOfExceptionType()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_readIsClassifiedObjectActionOfClassifier
boolean has_readIsClassifiedObjectActionOfClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_reclassifyObjectActionOfOldClassifier
boolean has_reclassifyObjectActionOfOldClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_reclassifyObjectActionOfNewClassifier
boolean has_reclassifyObjectActionOfNewClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_unmarshallActionOfUnmarshallType
boolean has_unmarshallActionOfUnmarshallType()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_createObjectActionOfClassifier
boolean has_createObjectActionOfClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_componentRealizationOfRealizingClassifier
boolean has_componentRealizationOfRealizingClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasCollaborationUse
boolean hasCollaborationUse()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasUseCase
boolean hasUseCase()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_classifierTemplateParameterOfConstrainingClassifier
boolean has_classifierTemplateParameterOfConstrainingClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_instanceSpecificationOfClassifier
boolean has_instanceSpecificationOfClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_redefinableElementOfRedefinitionContext
boolean has_redefinableElementOfRedefinitionContext()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface Classifier">Interface Classifier</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="../../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Classifier</span><span class="extends-implements">
extends <a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>, <a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>, <a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Classifier</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Classifier represents a classification of instances according to their Features.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_redefinableElementOfRedefinitionContext()"><code><em>redefinable Element Of Redefinition Context</em></code></a></li>
<li><a href="#getUseCase()"><code><em>Use Case</em></code></a></li>
<li><a href="#getOwnedUseCase()"><code><em>Owned Use Case</em></code></a></li>
<li><a href="#getFeature()"><code><em>Feature</em></code></a></li>
<li><a href="#get_interfaceOfNestedClassifier()"><code><em>interface Of Nested Classifier</em></code></a></li>
<li><a href="#get_readExtentActionOfClassifier()"><code><em>read Extent Action Of Classifier</em></code></a></li>
<li><a href="#get_createObjectActionOfClassifier()"><code><em>create Object Action Of Classifier</em></code></a></li>
<li><a href="#get_unmarshallActionOfUnmarshallType()"><code><em>unmarshall Action Of Unmarshall Type</em></code></a></li>
<li><a href="#get_readIsClassifiedObjectActionOfClassifier()"><code><em>read Is Classified Object Action Of Classifier</em></code></a></li>
<li><a href="#getRepresentation()"><code><em>Representation</em></code></a></li>
<li><a href="#getCollaborationUse()"><code><em>Collaboration Use</em></code></a></li>
<li><a href="#get_componentRealizationOfRealizingClassifier()"><code><em>component Realization Of Realizing Classifier</em></code></a></li>
<li><a href="#getAttribute()"><code><em>Attribute</em></code></a></li>
<li><a href="#get_exceptionHandlerOfExceptionType()"><code><em>exception Handler Of Exception Type</em></code></a></li>
<li><a href="#get_reclassifyObjectActionOfNewClassifier()"><code><em>reclassify Object Action Of New Classifier</em></code></a></li>
<li><a href="#get_reclassifyObjectActionOfOldClassifier()"><code><em>reclassify Object Action Of Old Classifier</em></code></a></li>
<li><a href="#getUMLClass()"><code><em>UML Class</em></code></a></li>
<li><a href="#getGeneral()"><code><em>General</em></code></a></li>
<li><a href="#getGeneralization()"><code><em>Generalization</em></code></a></li>
<li><a href="#get_generalizationOfGeneral()"><code><em>generalization Of General</em></code></a></li>
<li><a href="#getPowertypeExtent()"><code><em>Powertype Extent</em></code></a></li>
<li><a href="#getInheritedMember()"><code><em>Inherited Member</em></code></a></li>
<li><a href="#isAbstract()"><code><em>Abstract</em></code></a></li>
<li><a href="#isFinalSpecialization()"><code><em>Final Specialization</em></code></a></li>
<li><a href="#getRedefinedClassifier()"><code><em>Redefined Classifier</em></code></a></li>
<li><a href="#get_classifierOfRedefinedClassifier()"><code><em>classifier Of Redefined Classifier</em></code></a></li>
<li><a href="#getSubstitution()"><code><em>Substitution</em></code></a></li>
<li><a href="#get_substitutionOfContract()"><code><em>substitution Of Contract</em></code></a></li>
<li><a href="#get_classifierTemplateParameterOfConstrainingClassifier()"><code><em>classifier Template Parameter Of Constraining Classifier</em></code></a></li>
<li><a href="#get_informationItemOfRepresented()"><code><em>information Item Of Represented</em></code></a></li>
<li><a href="#get_instanceSpecificationOfClassifier()"><code><em>instance Specification Of Classifier</em></code></a></li>
<li><a href="#get_informationFlowOfConveyed()"><code><em>information Flow Of Conveyed</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getClassifier()"><code>UMLPackage.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='classes.mdkernel'"</dd>
<dt>Generated:</dt>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>classifier Of Redefined Classifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>classifier Template Parameter Of Constraining Classifier</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>component Realization Of Realizing Classifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>create Object Action Of Classifier</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>exception Handler Of Exception Type</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>generalization Of General</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Flow Of Conveyed</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Item Of Represented</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>instance Specification Of Classifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interface Of Nested Classifier</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Extent Action Of Classifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Is Classified Object Action Of Classifier</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reclassify Object Action Of New Classifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reclassify Object Action Of Old Classifier</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>redefinable Element Of Redefinition Context</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_substitutionOfContract()">get_substitutionOfContract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>substitution Of Contract</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>unmarshall Action Of Unmarshall Type</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAttribute()">getAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Attribute</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCollaborationUse()">getCollaborationUse</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Collaboration Use</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeature()">getFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Feature</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGeneral()">getGeneral</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>General</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGeneralization()">getGeneralization</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Generalization</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInheritedMember()">getInheritedMember</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Inherited Member</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Template Signature</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedUseCase()">getOwnedUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Use Case</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPowertypeExtent()">getPowertypeExtent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Powertype Extent</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedClassifier()">getRedefinedClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Classifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresentation()">getRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Representation</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSubstitution()">getSubstitution</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Substitution</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTemplateParameter()">getTemplateParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUMLClass()">getUMLClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>UML Class</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUseCase()">getUseCase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Use Case</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_substitutionOfContract()">has_substitutionOfContract</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasAttribute()">hasAttribute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasCollaborationUse()">hasCollaborationUse</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasFeature()">hasFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasGeneral()">hasGeneral</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasGeneralization()">hasGeneralization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasInheritedMember()">hasInheritedMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedUseCase()">hasOwnedUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPowertypeExtent()">hasPowertypeExtent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedClassifier()">hasRedefinedClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSubstitution()">hasSubstitution</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasUseCase()">hasUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isAbstract()">isAbstract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Abstract</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isFinalSpecialization()">isFinalSpecialization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Final Specialization</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a><wbr/>(<a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_interfaceOfNestedClassifier()"><code><em>interface Of Nested Classifier</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAbstract(boolean)">setAbstract</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isAbstract()"><code><em>Abstract</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFinalSpecialization(boolean)">setFinalSpecialization</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isFinalSpecialization()"><code><em>Final Specialization</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a><wbr/>(<a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwnedTemplateSignature()"><code><em>Owned Template Signature</em></code></a>'
 containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a><wbr/>(<a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getRepresentation()"><code><em>Representation</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a><wbr/>(<a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a><wbr/>(<a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUMLClass()"><code><em>UML Class</em></code></a>' container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="NamedElement.html#getName()">getName</a>, <a href="NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="NamedElement.html#getNamespace()">getNamespace</a>, <a href="NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="NamedElement.html#setName(java.lang.String)">setName</a>, <a href="NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="Namespace.html#getElementImport()">getElementImport</a>, <a href="Namespace.html#getImportedMember()">getImportedMember</a>, <a href="Namespace.html#getMember()">getMember</a>, <a href="Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="Namespace.html#getPackageImport()">getPackageImport</a>, <a href="Namespace.html#hasElementImport()">hasElementImport</a>, <a href="Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="Namespace.html#hasMember()">hasMember</a>, <a href="Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="PackageableElement.html#getVisibility()">getVisibility</a>, <a href="PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()">getTemplateBinding</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()">hasTemplateBinding</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">setOwnedTemplateSignature</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></h3>
<code><a href="Type.html#get_associationOfEndType()">get_associationOfEndType</a>, <a href="Type.html#get_behavioralFeatureOfRaisedException()">get_behavioralFeatureOfRaisedException</a>, <a href="Type.html#get_operationOfRaisedException()">get_operationOfRaisedException</a>, <a href="Type.html#get_typedElementOfType()">get_typedElementOfType</a>, <a href="Type.html#getPackage()">getPackage</a>, <a href="Type.html#has_associationOfEndType()">has_associationOfEndType</a>, <a href="Type.html#has_behavioralFeatureOfRaisedException()">has_behavioralFeatureOfRaisedException</a>, <a href="Type.html#has_operationOfRaisedException()">has_operationOfRaisedException</a>, <a href="Type.html#has_typedElementOfType()">has_typedElementOfType</a>, <a href="Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setPackage</a></code></div>
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
<section class="detail" id="getGeneralization()">
<h3>getGeneralization</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a>&gt;</span> <span class="element-name">getGeneralization</span>()</div>
<div class="block">Returns the value of the '<em><b>Generalization</b></em>' containment reference list.
 The list contents are of type <a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a>.
 It is bidirectional and its opposite is '<a href="Generalization.html#getSpecific()"><code><em>Specific</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Generalization relationships for this Classifier. These Generalizations navigate to more general Classifiers in the generalization hierarchy.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Generalization</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_Generalization()"><code>UMLPackage.getClassifier_Generalization()</code></a></li>
<li><a href="Generalization.html#getSpecific()"><code>Generalization.getSpecific()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="specific" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_generalizationOfGeneral()">
<h3>get_generalizationOfGeneral</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Generalization</a>&gt;</span> <span class="element-name">get_generalizationOfGeneral</span>()</div>
<div class="block">Returns the value of the '<em><b>generalization Of General</b></em>' reference list.
 The list contents are of type <a href="Generalization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Generalization</code></a>.
 It is bidirectional and its opposite is '<a href="Generalization.html#getGeneral()"><code><em>General</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>generalization Of General</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>generalization Of General</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__generalizationOfGeneral()"><code>UMLPackage.getClassifier__generalizationOfGeneral()</code></a></li>
<li><a href="Generalization.html#getGeneral()"><code>Generalization.getGeneral()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="general" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPowertypeExtent()">
<h3>getPowertypeExtent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a>&gt;</span> <span class="element-name">getPowertypeExtent</span>()</div>
<div class="block">Returns the value of the '<em><b>Powertype Extent</b></em>' reference list.
 The list contents are of type <a href="../mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes"><code>GeneralizationSet</code></a>.
 It is bidirectional and its opposite is '<a href="../mdpowertypes/GeneralizationSet.html#getPowertype()"><code><em>Powertype</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The GeneralizationSet of which this Classifier is a power type.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Powertype Extent</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_PowertypeExtent()"><code>UMLPackage.getClassifier_PowertypeExtent()</code></a></li>
<li><a href="../mdpowertypes/GeneralizationSet.html#getPowertype()"><code>GeneralizationSet.getPowertype()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="powertype" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeature()">
<h3>getFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a>&gt;</span> <span class="element-name">getFeature</span>()</div>
<div class="block">Returns the value of the '<em><b>Feature</b></em>' reference list.
 The list contents are of type <a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Feature</code></a>.
 It is bidirectional and its opposite is '<a href="Feature.html#getFeaturingClassifier()"><code><em>Featuring Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies each Feature directly defined in the classifier. Note that there may be members of the Classifier that are of the type Feature but are not included, e
 .g., inherited features.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Feature</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_Feature()"><code>UMLPackage.getClassifier_Feature()</code></a></li>
<li><a href="Feature.html#getFeaturingClassifier()"><code>Feature.getFeaturingClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="featuringClassifier" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritedMember()">
<h3>getInheritedMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getInheritedMember</span>()</div>
<div class="block">Returns the value of the '<em><b>Inherited Member</b></em>' reference list.
 The list contents are of type <a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.
 It is bidirectional and its opposite is
 '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>classifier Of Inherited Member</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 All elements inherited by this Classifier from its general Classifiers.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Inherited Member</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_InheritedMember()"><code>UMLPackage.getClassifier_InheritedMember()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement#get_classifierOfInheritedMember</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classifierOfInheritedMember" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAbstract()">
<h3>isAbstract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isAbstract</span>()</div>
<div class="block">Returns the value of the '<em><b>Abstract</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, the Classifier can only be instantiated by instantiating one of its specializations. An abstract Classifier is intended to be used by other Classifiers
 e.g., as the target of Associations or Generalizations.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Abstract</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setAbstract(boolean)"><code>setAbstract(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getClassifier_Abstract()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAbstract(boolean)">
<h3>setAbstract</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAbstract</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isAbstract()"><code><em>Abstract</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Abstract</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isAbstract()"><code>isAbstract()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFinalSpecialization()">
<h3>isFinalSpecialization</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isFinalSpecialization</span>()</div>
<div class="block">Returns the value of the '<em><b>Final Specialization</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, the Classifier cannot be specialized.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Final Specialization</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setFinalSpecialization(boolean)"><code>setFinalSpecialization(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getClassifier_FinalSpecialization()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFinalSpecialization(boolean)">
<h3>setFinalSpecialization</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFinalSpecialization</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isFinalSpecialization()"><code><em>Final Specialization</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Final Specialization</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isFinalSpecialization()"><code>isFinalSpecialization()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttribute()">
<h3>getAttribute</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getAttribute</span>()</div>
<div class="block">Returns the value of the '<em><b>Attribute</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="Property.html#getClassifier()"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 All of the Properties that are direct (i.e., not inherited or imported) attributes of the Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Attribute</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_Attribute()"><code>UMLPackage.getClassifier_Attribute()</code></a></li>
<li><a href="Property.html#getClassifier()"><code>Property.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifier" transient="true" volatile="true" derived="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedClassifier()">
<h3>getRedefinedClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getRedefinedClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Classifier</b></em>' reference list.
 The list contents are of type <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_classifierOfRedefinedClassifier()"><code><em>classifier Of Redefined Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Classifiers redefined by this Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_RedefinedClassifier()"><code>UMLPackage.getClassifier_RedefinedClassifier()</code></a></li>
<li><a href="#get_classifierOfRedefinedClassifier()"><code>get_classifierOfRedefinedClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classifierOfRedefinedClassifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_classifierOfRedefinedClassifier()">
<h3>get_classifierOfRedefinedClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">get_classifierOfRedefinedClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>classifier Of Redefined Classifier</b></em>' reference list.
 The list contents are of type <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is '<a href="#getRedefinedClassifier()"><code><em>Redefined Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>classifier Of Redefined Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>classifier Of Redefined Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__classifierOfRedefinedClassifier()"><code>UMLPackage.getClassifier__classifierOfRedefinedClassifier()</code></a></li>
<li><a href="#getRedefinedClassifier()"><code>getRedefinedClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedClassifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneral()">
<h3>getGeneral</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getGeneral</span>()</div>
<div class="block">Returns the value of the '<em><b>General</b></em>' reference list.
 The list contents are of type <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is
 '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>classifier Of General</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The generalizing Classifiers for this Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>General</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_General()"><code>UMLPackage.getClassifier_General()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_classifierOfGeneral</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classifierOfGeneral" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubstitution()">
<h3>getSubstitution</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a>&gt;</span> <span class="element-name">getSubstitution</span>()</div>
<div class="block">Returns the value of the '<em><b>Substitution</b></em>' containment reference list.
 The list contents are of type <a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mddependencies/Substitution.html#getSubstitutingClassifier()"><code><em>Substituting Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Substitutions owned by this Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Substitution</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_Substitution()"><code>UMLPackage.getClassifier_Substitution()</code></a></li>
<li><a href="../mddependencies/Substitution.html#getSubstitutingClassifier()"><code>Substitution.getSubstitutingClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="substitutingClassifier" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_substitutionOfContract()">
<h3>get_substitutionOfContract</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a>&gt;</span> <span class="element-name">get_substitutionOfContract</span>()</div>
<div class="block">Returns the value of the '<em><b>substitution Of Contract</b></em>' reference list.
 The list contents are of type <a href="../mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies"><code>Substitution</code></a>.
 It is bidirectional and its opposite is '<a href="../mddependencies/Substitution.html#getContract()"><code><em>Contract</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>substitution Of Contract</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>substitution Of Contract</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__substitutionOfContract()"><code>UMLPackage.getClassifier__substitutionOfContract()</code></a></li>
<li><a href="../mddependencies/Substitution.html#getContract()"><code>Substitution.getContract()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="contract" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedUseCase()">
<h3>getOwnedUseCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a>&gt;</span> <span class="element-name">getOwnedUseCase</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Use Case</b></em>' containment reference list.
 The list contents are of type <a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../mdusecases/UseCase.html#get_classifierOfOwnedUseCase()"><code><em>classifier Of Owned Use Case</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The UseCases owned by this classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Use Case</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_OwnedUseCase()"><code>UMLPackage.getClassifier_OwnedUseCase()</code></a></li>
<li><a href="../../mdusecases/UseCase.html#get_classifierOfOwnedUseCase()"><code>UseCase.get_classifierOfOwnedUseCase()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classifierOfOwnedUseCase" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interfaceOfNestedClassifier()">
<h3>get_interfaceOfNestedClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></span> <span class="element-name">get_interfaceOfNestedClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>interface Of Nested Classifier</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdinterfaces/Interface.html#getNestedClassifier()"><code><em>Nested Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interface Of Nested Classifier</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interface Of Nested Classifier</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)"><code>set_interfaceOfNestedClassifier(Interface)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClassifier__interfaceOfNestedClassifier()"><code>UMLPackage.getClassifier__interfaceOfNestedClassifier()</code></a></li>
<li><a href="../mdinterfaces/Interface.html#getNestedClassifier()"><code>Interface.getNestedClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="nestedClassifier" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>set_interfaceOfNestedClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interfaceOfNestedClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_interfaceOfNestedClassifier()"><code><em>interface Of Nested Classifier</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interface Of Nested Classifier</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_interfaceOfNestedClassifier()"><code>get_interfaceOfNestedClassifier()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationItemOfRepresented()">
<h3>get_informationItemOfRepresented</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a>&gt;</span> <span class="element-name">get_informationItemOfRepresented</span>()</div>
<div class="block">Returns the value of the '<em><b>information Item Of Represented</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationItem</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html#getRepresented()"><code><em>Represented</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Item Of Represented</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Item Of Represented</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__informationItemOfRepresented()"><code>UMLPackage.getClassifier__informationItemOfRepresented()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html#getRepresented()"><code>InformationItem.getRepresented()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="represented" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationFlowOfConveyed()">
<h3>get_informationFlowOfConveyed</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</span> <span class="element-name">get_informationFlowOfConveyed</span>()</div>
<div class="block">Returns the value of the '<em><b>information Flow Of Conveyed</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getConveyed()"><code><em>Conveyed</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Flow Of Conveyed</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Flow Of Conveyed</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__informationFlowOfConveyed()"><code>UMLPackage.getClassifier__informationFlowOfConveyed()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getConveyed()"><code>InformationFlow.getConveyed()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="conveyed" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_exceptionHandlerOfExceptionType()">
<h3>get_exceptionHandlerOfExceptionType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</span> <span class="element-name">get_exceptionHandlerOfExceptionType</span>()</div>
<div class="block">Returns the value of the '<em><b>exception Handler Of Exception Type</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdextrastructuredactivities/ExceptionHandler.html#getExceptionType()"><code><em>Exception Type</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>exception Handler Of Exception Type</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>exception Handler Of Exception Type</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__exceptionHandlerOfExceptionType()"><code>UMLPackage.getClassifier__exceptionHandlerOfExceptionType()</code></a></li>
<li><a href="../../activities/mdextrastructuredactivities/ExceptionHandler.html#getExceptionType()"><code>ExceptionHandler.getExceptionType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="exceptionType" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readIsClassifiedObjectActionOfClassifier()">
<h3>get_readIsClassifiedObjectActionOfClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a>&gt;</span> <span class="element-name">get_readIsClassifiedObjectActionOfClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>read Is Classified Object Action Of Classifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadIsClassifiedObjectAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html#getClassifier()"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Is Classified Object Action Of Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Is Classified Object Action Of Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__readIsClassifiedObjectActionOfClassifier()"><code>UMLPackage.getClassifier__readIsClassifiedObjectActionOfClassifier()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html#getClassifier()"><code>ReadIsClassifiedObjectAction.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readExtentActionOfClassifier()">
<h3>get_readExtentActionOfClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a>&gt;</span> <span class="element-name">get_readExtentActionOfClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>read Extent Action Of Classifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadExtentAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdcompleteactions/ReadExtentAction.html#getClassifier()"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Extent Action Of Classifier</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Extent Action Of Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__readExtentActionOfClassifier()"><code>UMLPackage.getClassifier__readExtentActionOfClassifier()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReadExtentAction.html#getClassifier()"><code>ReadExtentAction.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_reclassifyObjectActionOfOldClassifier()">
<h3>get_reclassifyObjectActionOfOldClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a>&gt;</span> <span class="element-name">get_reclassifyObjectActionOfOldClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>reclassify Object Action Of Old Classifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html#getOldClassifier()"><code><em>Old Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reclassify Object Action Of Old Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reclassify Object Action Of Old Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__reclassifyObjectActionOfOldClassifier()"><code>UMLPackage.getClassifier__reclassifyObjectActionOfOldClassifier()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html#getOldClassifier()"><code>ReclassifyObjectAction.getOldClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="oldClassifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_reclassifyObjectActionOfNewClassifier()">
<h3>get_reclassifyObjectActionOfNewClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a>&gt;</span> <span class="element-name">get_reclassifyObjectActionOfNewClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>reclassify Object Action Of New Classifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReclassifyObjectAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html#getNewClassifier()"><code><em>New Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reclassify Object Action Of New Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reclassify Object Action Of New Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__reclassifyObjectActionOfNewClassifier()"><code>UMLPackage.getClassifier__reclassifyObjectActionOfNewClassifier()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html#getNewClassifier()"><code>ReclassifyObjectAction.getNewClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="newClassifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_unmarshallActionOfUnmarshallType()">
<h3>get_unmarshallActionOfUnmarshallType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a>&gt;</span> <span class="element-name">get_unmarshallActionOfUnmarshallType</span>()</div>
<div class="block">Returns the value of the '<em><b>unmarshall Action Of Unmarshall Type</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>UnmarshallAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdcompleteactions/UnmarshallAction.html#getUnmarshallType()"><code><em>Unmarshall Type</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>unmarshall Action Of Unmarshall Type</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>unmarshall Action Of Unmarshall Type</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__unmarshallActionOfUnmarshallType()"><code>UMLPackage.getClassifier__unmarshallActionOfUnmarshallType()</code></a></li>
<li><a href="../../actions/mdcompleteactions/UnmarshallAction.html#getUnmarshallType()"><code>UnmarshallAction.getUnmarshallType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="unmarshallType" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_createObjectActionOfClassifier()">
<h3>get_createObjectActionOfClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a>&gt;</span> <span class="element-name">get_createObjectActionOfClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>create Object Action Of Classifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>CreateObjectAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdintermediateactions/CreateObjectAction.html#getClassifier()"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>create Object Action Of Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>create Object Action Of Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__createObjectActionOfClassifier()"><code>UMLPackage.getClassifier__createObjectActionOfClassifier()</code></a></li>
<li><a href="../../actions/mdintermediateactions/CreateObjectAction.html#getClassifier()"><code>CreateObjectAction.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLClass()">
<h3>getUMLClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getUMLClass</span>()</div>
<div class="block">Returns the value of the '<em><b>UML Class</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Class.html#getNestedClassifier()"><code><em>Nested Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>UML Class</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>UML Class</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)"><code>setUMLClass(Class)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClassifier_UMLClass()"><code>UMLPackage.getClassifier_UMLClass()</code></a></li>
<li><a href="Class.html#getNestedClassifier()"><code>Class.getNestedClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="nestedClassifier" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>setUMLClass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUMLClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUMLClass()"><code><em>UML Class</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>UML Class</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getUMLClass()"><code>getUMLClass()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_componentRealizationOfRealizingClassifier()">
<h3>get_componentRealizationOfRealizingClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a>&gt;</span> <span class="element-name">get_componentRealizationOfRealizingClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>component Realization Of Realizing Classifier</b></em>' reference list.
 The list contents are of type <a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../components/mdbasiccomponents/ComponentRealization.html#getRealizingClassifier()"><code><em>Realizing Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>component Realization Of Realizing Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>component Realization Of Realizing Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__componentRealizationOfRealizingClassifier()"><code>UMLPackage.getClassifier__componentRealizationOfRealizingClassifier()</code></a></li>
<li><a href="../../components/mdbasiccomponents/ComponentRealization.html#getRealizingClassifier()"><code>ComponentRealization.getRealizingClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="realizingClassifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCollaborationUse()">
<h3>getCollaborationUse</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a>&gt;</span> <span class="element-name">getCollaborationUse</span>()</div>
<div class="block">Returns the value of the '<em><b>Collaboration Use</b></em>' containment reference list.
 The list contents are of type <a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>CollaborationUse</code></a>.
 It is bidirectional and its opposite is '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>.mdcollaborations.CollaborationUse#get_classifierOfCollaborationUse <em>classifier Of Collaboration Use</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The CollaborationUses owned by the Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Collaboration Use</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_CollaborationUse()"><code>UMLPackage.getClassifier_CollaborationUse()</code></a></li>
<li><a href="../../compositestructures/mdcollaborations/CollaborationUse.html#get_classifierOfCollaborationUse()"><code>CollaborationUse.get_classifierOfCollaborationUse()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classifierOfCollaborationUse" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentation()">
<h3>getRepresentation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></span> <span class="element-name">getRepresentation</span>()</div>
<div class="block">Returns the value of the '<em><b>Representation</b></em>' reference.
 It is bidirectional and its opposite is '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>.mdcollaborations.CollaborationUse#get_classifierOfRepresentation <em>classifier Of Representation</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A CollaborationUse which indicates the Collaboration that represents this Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Representation</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)"><code>setRepresentation(CollaborationUse)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClassifier_Representation()"><code>UMLPackage.getClassifier_Representation()</code></a></li>
<li><a href="../../compositestructures/mdcollaborations/CollaborationUse.html#get_classifierOfRepresentation()"><code>CollaborationUse.get_classifierOfRepresentation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classifierOfRepresentation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">
<h3>setRepresentation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRepresentation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getRepresentation()"><code><em>Representation</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Representation</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getRepresentation()"><code>getRepresentation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseCase()">
<h3>getUseCase</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a>&gt;</span> <span class="element-name">getUseCase</span>()</div>
<div class="block">Returns the value of the '<em><b>Use Case</b></em>' reference list.
 The list contents are of type <a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>UseCase</code></a>.
 It is bidirectional and its opposite is '<a href="../../mdusecases/UseCase.html#getSubject()"><code><em>Subject</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of UseCases for which this Classifier is the subject.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Use Case</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier_UseCase()"><code>UMLPackage.getClassifier_UseCase()</code></a></li>
<li><a href="../../mdusecases/UseCase.html#getSubject()"><code>UseCase.getSubject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="subject" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_classifierTemplateParameterOfConstrainingClassifier()">
<h3>get_classifierTemplateParameterOfConstrainingClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a>&gt;</span> <span class="element-name">get_classifierTemplateParameterOfConstrainingClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>classifier Template Parameter Of Constraining Classifier</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>ClassifierTemplateParameter</code></a>.
 It is bidirectional and its opposite is '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter#getConstrainingClassifier <em>Constraining Classifier</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>classifier Template Parameter Of Constraining Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>classifier Template Parameter Of Constraining Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__classifierTemplateParameterOfConstrainingClassifier()"><code>UMLPackage.getClassifier__classifierTemplateParameterOfConstrainingClassifier()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html#getConstrainingClassifier()"><code>ClassifierTemplateParameter.getConstrainingClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="constrainingClassifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_instanceSpecificationOfClassifier()">
<h3>get_instanceSpecificationOfClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">get_instanceSpecificationOfClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>instance Specification Of Classifier</b></em>' reference list.
 The list contents are of type <a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>InstanceSpecification</code></a>.
 It is bidirectional and its opposite is '<a href="InstanceSpecification.html#getClassifier()"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>instance Specification Of Classifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>instance Specification Of Classifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__instanceSpecificationOfClassifier()"><code>UMLPackage.getClassifier__instanceSpecificationOfClassifier()</code></a></li>
<li><a href="InstanceSpecification.html#getClassifier()"><code>InstanceSpecification.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_redefinableElementOfRedefinitionContext()">
<h3>get_redefinableElementOfRedefinitionContext</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;</span> <span class="element-name">get_redefinableElementOfRedefinitionContext</span>()</div>
<div class="block">Returns the value of the '<em><b>redefinable Element Of Redefinition Context</b></em>' reference list.
 The list contents are of type <a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.
 It is bidirectional and its opposite is
 '<a href="RedefinableElement.html#getRedefinitionContext()"><code><em>Redefinition Context</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>redefinable Element Of Redefinition Context</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>redefinable Element Of Redefinition Context</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClassifier__redefinableElementOfRedefinitionContext()"><code>UMLPackage.getClassifier__redefinableElementOfRedefinitionContext()</code></a></li>
<li><a href="RedefinableElement.html#getRedefinitionContext()"><code>RedefinableElement.getRedefinitionContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinitionContext" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedTemplateSignature()">
<h3>getOwnedTemplateSignature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></span> <span class="element-name">getOwnedTemplateSignature</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Template Signature</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html#getClassifier()"><code><em>Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The optional RedefinableTemplateSignature specifying the formal template parameters.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a></code> in interface <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Template Signature</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)"><code>setOwnedTemplateSignature(RedefinableTemplateSignature)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClassifier_OwnedTemplateSignature()"><code>UMLPackage.getClassifier_OwnedTemplateSignature()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html#getClassifier()"><code>RedefinableTemplateSignature.getClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifier" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">
<h3>setOwnedTemplateSignature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnedTemplateSignature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwnedTemplateSignature()"><code><em>Owned Template Signature</em></code></a>'
 containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owned Template Signature</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getOwnedTemplateSignature()"><code>getOwnedTemplateSignature()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameter()">
<h3>getTemplateParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></span> <span class="element-name">getTemplateParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html#getParameteredElement()"><code><em>Parametered Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 TheClassifierTemplateParameter that exposes this element as a formal parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()">getTemplateParameter</a></code> in interface <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)"><code>setTemplateParameter(ClassifierTemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClassifier_TemplateParameter()"><code>UMLPackage.getClassifier_TemplateParameter()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html#getParameteredElement()"><code>ClassifierTemplateParameter.getParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameteredElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">
<h3>setTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTemplateParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../auxiliaryconstructs/mdtemplates/ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getTemplateParameter()"><code>getTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasGeneralization()">
<h3>hasGeneralization</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasGeneralization</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_generalizationOfGeneral()">
<h3>has_generalizationOfGeneral</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_generalizationOfGeneral</span>()
                             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPowertypeExtent()">
<h3>hasPowertypeExtent</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPowertypeExtent</span>()
                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasFeature()">
<h3>hasFeature</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasFeature</span>()
            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasInheritedMember()">
<h3>hasInheritedMember</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasInheritedMember</span>()
                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasAttribute()">
<h3>hasAttribute</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasAttribute</span>()
              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedClassifier()">
<h3>hasRedefinedClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedClassifier</span>()
                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_classifierOfRedefinedClassifier()">
<h3>has_classifierOfRedefinedClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_classifierOfRedefinedClassifier</span>()
                                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasGeneral()">
<h3>hasGeneral</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasGeneral</span>()
            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSubstitution()">
<h3>hasSubstitution</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSubstitution</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_substitutionOfContract()">
<h3>has_substitutionOfContract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_substitutionOfContract</span>()
                            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedUseCase()">
<h3>hasOwnedUseCase</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedUseCase</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_readExtentActionOfClassifier()">
<h3>has_readExtentActionOfClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_readExtentActionOfClassifier</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationItemOfRepresented()">
<h3>has_informationItemOfRepresented</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationItemOfRepresented</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationFlowOfConveyed()">
<h3>has_informationFlowOfConveyed</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationFlowOfConveyed</span>()
                               throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_exceptionHandlerOfExceptionType()">
<h3>has_exceptionHandlerOfExceptionType</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_exceptionHandlerOfExceptionType</span>()
                                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_readIsClassifiedObjectActionOfClassifier()">
<h3>has_readIsClassifiedObjectActionOfClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_readIsClassifiedObjectActionOfClassifier</span>()
                                              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_reclassifyObjectActionOfOldClassifier()">
<h3>has_reclassifyObjectActionOfOldClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_reclassifyObjectActionOfOldClassifier</span>()
                                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_reclassifyObjectActionOfNewClassifier()">
<h3>has_reclassifyObjectActionOfNewClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_reclassifyObjectActionOfNewClassifier</span>()
                                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_unmarshallActionOfUnmarshallType()">
<h3>has_unmarshallActionOfUnmarshallType</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_unmarshallActionOfUnmarshallType</span>()
                                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_createObjectActionOfClassifier()">
<h3>has_createObjectActionOfClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_createObjectActionOfClassifier</span>()
                                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_componentRealizationOfRealizingClassifier()">
<h3>has_componentRealizationOfRealizingClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_componentRealizationOfRealizingClassifier</span>()
                                               throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasCollaborationUse()">
<h3>hasCollaborationUse</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasCollaborationUse</span>()
                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasUseCase()">
<h3>hasUseCase</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasUseCase</span>()
            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_classifierTemplateParameterOfConstrainingClassifier()">
<h3>has_classifierTemplateParameterOfConstrainingClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_classifierTemplateParameterOfConstrainingClassifier</span>()
                                                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_instanceSpecificationOfClassifier()">
<h3>has_instanceSpecificationOfClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_instanceSpecificationOfClassifier</span>()
                                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_redefinableElementOfRedefinitionContext()">
<h3>has_redefinableElementOfRedefinitionContext</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_redefinableElementOfRedefinitionContext</span>()
                                             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
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
