# JAVA OPENAPI: Association (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Association.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Association.html`
- source_sha256: `243bdb8590c34713e38849a5f5899ba497051cd2e1c1add6c647bb57119cab7a`
- captured_utc: `2026-07-14T16:46:28.296177+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Association

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Classifier](Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Relationship](Relationship.html)`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Extension](../../mdprofiles/Extension.html)`

public interfaceAssociationextends [Classifier](Classifier.html), [Relationship](Relationship.html)

begin-user-doc 
 A representation of the model object '***Association***'.
 end-user-doc 
begin-model-doc 
 A link is a tuple of values that refer to typed objects. An Association classifies a set of links, each of which is an instance of the Association. Each value in
 the link refers to an instance of the type of the corresponding end of the Association.
 end-model-doc 
The following features are supported:
 [`*Derived*`](#isDerived())
[`*Member End*`](#getMemberEnd())
[`*connector Of Type*`](#get_connectorOfType())
[`*Owned End*`](#getOwnedEnd())
[`*Navigable Owned End*`](#getNavigableOwnedEnd())
[`*clear Association Action Of Association*`](#get_clearAssociationActionOfAssociation())
[`*End Type*`](#getEndType())

See Also:
[`UMLPackage.getAssociation()`](../../metadata/UMLPackage.html#getAssociation())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ClearAssociationAction](../../actions/mdintermediateactions/ClearAssociationAction.html)>`
`[get_clearAssociationActionOfAssociation](#get_clearAssociationActionOfAssociation())()`
Returns the value of the '***clear Association Action Of Association***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Connector](../../compositestructures/mdinternalstructures/Connector.html)>`
`[get_connectorOfType](#get_connectorOfType())()`
Returns the value of the '***connector Of Type***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](Type.html)>`
`[getEndType](#getEndType())()`
Returns the value of the '***End Type***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getMemberEnd](#getMemberEnd())()`
Returns the value of the '***Member End***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)>`
`[getNavigableOwnedEnd](#getNavigableOwnedEnd())()`
Returns the value of the '***Navigable Owned End***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getOwnedEnd](#getOwnedEnd())()`
Returns the value of the '***Owned End***' containment reference list.
`boolean`
`[has_clearAssociationActionOfAssociation](#has_clearAssociationActionOfAssociation())()`

`boolean`
`[has_connectorOfType](#has_connectorOfType())()`

`boolean`
`[hasEndType](#hasEndType())()`

`boolean`
`[hasMemberEnd](#hasMemberEnd())()`

`boolean`
`[hasNavigableOwnedEnd](#hasNavigableOwnedEnd())()`

`boolean`
`[hasOwnedEnd](#hasOwnedEnd())()`

`boolean`
`[isDerived](#isDerived())()`
Returns the value of the '***Derived***' attribute.
`void`
`[setDerived](#setDerived(boolean))(boolean value)`
Sets the value of the '[`*Derived*`](#isDerived())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](Classifier.html)
`[get_classifierOfRedefinedClassifier](Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](Classifier.html#getAttribute()), [getCollaborationUse](Classifier.html#getCollaborationUse()), [getFeature](Classifier.html#getFeature()), [getGeneral](Classifier.html#getGeneral()), [getGeneralization](Classifier.html#getGeneralization()), [getInheritedMember](Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](Classifier.html#getOwnedUseCase()), [getPowertypeExtent](Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](Classifier.html#getRedefinedClassifier()), [getRepresentation](Classifier.html#getRepresentation()), [getSubstitution](Classifier.html#getSubstitution()), [getTemplateParameter](Classifier.html#getTemplateParameter()), [getUMLClass](Classifier.html#getUMLClass()), [getUseCase](Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](Classifier.html#hasAttribute()), [hasCollaborationUse](Classifier.html#hasCollaborationUse()), [hasFeature](Classifier.html#hasFeature()), [hasGeneral](Classifier.html#hasGeneral()), [hasGeneralization](Classifier.html#hasGeneralization()), [hasInheritedMember](Classifier.html#hasInheritedMember()), [hasOwnedUseCase](Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](Classifier.html#hasRedefinedClassifier()), [hasSubstitution](Classifier.html#hasSubstitution()), [hasUseCase](Classifier.html#hasUseCase()), [isAbstract](Classifier.html#isAbstract()), [isFinalSpecialization](Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setAbstract](Classifier.html#setAbstract(boolean)), [setFinalSpecialization](Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Relationship](Relationship.html)
`[get_abstraction](Relationship.html#get_abstraction()), [getRelatedElement](Relationship.html#getRelatedElement()), [has_abstraction](Relationship.html#has_abstraction()), [hasRelatedElement](Relationship.html#hasRelatedElement())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](Type.html)
`[get_associationOfEndType](Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](Type.html#get_operationOfRaisedException()), [get_typedElementOfType](Type.html#get_typedElementOfType()), [getPackage](Type.html#getPackage()), [has_associationOfEndType](Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](Type.html#has_operationOfRaisedException()), [has_typedElementOfType](Type.html#has_typedElementOfType()), [setPackage](Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
isDerived
boolean isDerived()
Returns the value of the '***Derived***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether the Association is derived from other model elements such as other Associations.
 end-model-doc
Returns:
the value of the '*Derived*' attribute.
See Also:
[`setDerived(boolean)`](#setDerived(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getAssociation_Derived()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setDerived
void setDerived(boolean value)
Sets the value of the '[`*Derived*`](#isDerived())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Derived*' attribute.
See Also:
[`isDerived()`](#isDerived())
Generated:
get_connectorOfType
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Connector](../../compositestructures/mdinternalstructures/Connector.html)> get_connectorOfType()
Returns the value of the '***connector Of Type***' reference list.
 The list contents are of type [`Connector`](../../compositestructures/mdinternalstructures/Connector.html).
 It is bidirectional and its opposite is '[`*Type*`](../../compositestructures/mdinternalstructures/Connector.html#getType())'.
 begin-user-doc 
If the meaning of the '*connector Of Type*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*connector Of Type*' reference list.
See Also:
[`UMLPackage.getAssociation__connectorOfType()`](../../metadata/UMLPackage.html#getAssociation__connectorOfType())
[`Connector.getType()`](../../compositestructures/mdinternalstructures/Connector.html#getType())
Model:
opposite="type" ordered="false"
Generated:
get_clearAssociationActionOfAssociation
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ClearAssociationAction](../../actions/mdintermediateactions/ClearAssociationAction.html)> get_clearAssociationActionOfAssociation()
Returns the value of the '***clear Association Action Of Association***' reference list.
 The list contents are of type [`ClearAssociationAction`](../../actions/mdintermediateactions/ClearAssociationAction.html).
 It is bidirectional and its opposite is
 '[`*Association*`](../../actions/mdintermediateactions/ClearAssociationAction.html#getAssociation())'.
 begin-user-doc 
If the meaning of the '*clear Association Action Of Association*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clear Association Action Of Association*' reference list.
See Also:
[`UMLPackage.getAssociation__clearAssociationActionOfAssociation()`](../../metadata/UMLPackage.html#getAssociation__clearAssociationActionOfAssociation())
[`ClearAssociationAction.getAssociation()`](../../actions/mdintermediateactions/ClearAssociationAction.html#getAssociation())
Model:
opposite="association" ordered="false"
Generated:
getMemberEnd
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getMemberEnd()
Returns the value of the '***Member End***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*Association*`](Property.html#getAssociation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Each end represents participation of instances of the Classifier connected to the end in links of the Association.
 end-model-doc
Returns:
the value of the '*Member End*' reference list.
See Also:
[`UMLPackage.getAssociation_MemberEnd()`](../../metadata/UMLPackage.html#getAssociation_MemberEnd())
[`Property.getAssociation()`](Property.html#getAssociation())
Model:
opposite="association" lower="2"
Generated:
getOwnedEnd
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getOwnedEnd()
Returns the value of the '***Owned End***' containment reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*Owning Association*`](Property.html#getOwningAssociation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ends that are owned by the Association itself.
 end-model-doc
Returns:
the value of the '*Owned End*' containment reference list.
See Also:
[`UMLPackage.getAssociation_OwnedEnd()`](../../metadata/UMLPackage.html#getAssociation_OwnedEnd())
[`Property.getOwningAssociation()`](Property.html#getOwningAssociation())
Model:
opposite="owningAssociation" containment="true" resolveProxies="true"
Generated:
getNavigableOwnedEnd
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> getNavigableOwnedEnd()
Returns the value of the '***Navigable Owned End***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is
 '[`*association Of Navigable Owned End*`](Property.html#get_associationOfNavigableOwnedEnd())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The navigable ends that are owned by the Association itself.
 end-model-doc
Returns:
the value of the '*Navigable Owned End*' reference list.
See Also:
[`UMLPackage.getAssociation_NavigableOwnedEnd()`](../../metadata/UMLPackage.html#getAssociation_NavigableOwnedEnd())
[`Property.get_associationOfNavigableOwnedEnd()`](Property.html#get_associationOfNavigableOwnedEnd())
Model:
opposite="_associationOfNavigableOwnedEnd" ordered="false"
Generated:
getEndType
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](Type.html)> getEndType()
Returns the value of the '***End Type***' reference list.
 The list contents are of type [`Type`](Type.html).
 It is bidirectional and its opposite is '[`*association Of End Type*`](Type.html#get_associationOfEndType())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Classifiers that are used as types of the ends of the Association.
 end-model-doc
Returns:
the value of the '*End Type*' reference list.
See Also:
[`UMLPackage.getAssociation_EndType()`](../../metadata/UMLPackage.html#getAssociation_EndType())
[`Type.get_associationOfEndType()`](Type.html#get_associationOfEndType())
Model:
opposite="_associationOfEndType" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
has_connectorOfType
boolean has_connectorOfType()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasMemberEnd
boolean hasMemberEnd()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedEnd
boolean hasOwnedEnd()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_clearAssociationActionOfAssociation
boolean has_clearAssociationActionOfAssociation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasNavigableOwnedEnd
boolean hasNavigableOwnedEnd()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasEndType
boolean hasEndType()
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
<h1 class="title" title="Interface Association">Interface Association</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Association</span><span class="extends-implements">
extends <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>, <a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Association</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A link is a tuple of values that refer to typed objects.  An Association classifies a set of links, each of which is an instance of the Association.  Each value in
 the link refers to an instance of the type of the corresponding end of the Association.
 <p>
<!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isDerived()"><code><em>Derived</em></code></a></li>
<li><a href="#getMemberEnd()"><code><em>Member End</em></code></a></li>
<li><a href="#get_connectorOfType()"><code><em>connector Of Type</em></code></a></li>
<li><a href="#getOwnedEnd()"><code><em>Owned End</em></code></a></li>
<li><a href="#getNavigableOwnedEnd()"><code><em>Navigable Owned End</em></code></a></li>
<li><a href="#get_clearAssociationActionOfAssociation()"><code><em>clear Association Action Of Association</em></code></a></li>
<li><a href="#getEndType()"><code><em>End Type</em></code></a></li>
</ul>
</p></p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getAssociation()"><code>UMLPackage.getAssociation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='classes.mdkernel'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clearAssociationActionOfAssociation()">get_clearAssociationActionOfAssociation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clear Association Action Of Association</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_connectorOfType()">get_connectorOfType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>connector Of Type</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEndType()">getEndType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>End Type</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMemberEnd()">getMemberEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Member End</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNavigableOwnedEnd()">getNavigableOwnedEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Navigable Owned End</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedEnd()">getOwnedEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned End</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_clearAssociationActionOfAssociation()">has_clearAssociationActionOfAssociation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_connectorOfType()">has_connectorOfType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEndType()">hasEndType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasMemberEnd()">hasMemberEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasNavigableOwnedEnd()">hasNavigableOwnedEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedEnd()">hasOwnedEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDerived()">isDerived</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Derived</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDerived(boolean)">setDerived</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isDerived()"><code><em>Derived</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="Classifier.html#getAttribute()">getAttribute</a>, <a href="Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="Classifier.html#getFeature()">getFeature</a>, <a href="Classifier.html#getGeneral()">getGeneral</a>, <a href="Classifier.html#getGeneralization()">getGeneralization</a>, <a href="Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="Classifier.html#getRepresentation()">getRepresentation</a>, <a href="Classifier.html#getSubstitution()">getSubstitution</a>, <a href="Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="Classifier.html#getUMLClass()">getUMLClass</a>, <a href="Classifier.html#getUseCase()">getUseCase</a>, <a href="Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="Classifier.html#hasAttribute()">hasAttribute</a>, <a href="Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="Classifier.html#hasFeature()">hasFeature</a>, <a href="Classifier.html#hasGeneral()">hasGeneral</a>, <a href="Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="Classifier.html#hasUseCase()">hasUseCase</a>, <a href="Classifier.html#isAbstract()">isAbstract</a>, <a href="Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="Classifier.html#setAbstract(boolean)">setAbstract</a>, <a href="Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></h3>
<code><a href="Relationship.html#get_abstraction()">get_abstraction</a>, <a href="Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="Relationship.html#has_abstraction()">has_abstraction</a>, <a href="Relationship.html#hasRelatedElement()">hasRelatedElement</a></code></div>
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
<section class="detail" id="isDerived()">
<h3>isDerived</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDerived</span>()</div>
<div class="block">Returns the value of the '<em><b>Derived</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether the Association is derived from other model elements such as other Associations.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Derived</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDerived(boolean)"><code>setDerived(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getAssociation_Derived()</code></pre>
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
<section class="detail" id="setDerived(boolean)">
<h3>setDerived</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDerived</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isDerived()"><code><em>Derived</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Derived</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isDerived()"><code>isDerived()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_connectorOfType()">
<h3>get_connectorOfType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</span> <span class="element-name">get_connectorOfType</span>()</div>
<div class="block">Returns the value of the '<em><b>connector Of Type</b></em>' reference list.
 The list contents are of type <a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.
 It is bidirectional and its opposite is '<a href="../../compositestructures/mdinternalstructures/Connector.html#getType()"><code><em>Type</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>connector Of Type</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>connector Of Type</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAssociation__connectorOfType()"><code>UMLPackage.getAssociation__connectorOfType()</code></a></li>
<li><a href="../../compositestructures/mdinternalstructures/Connector.html#getType()"><code>Connector.getType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="type" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_clearAssociationActionOfAssociation()">
<h3>get_clearAssociationActionOfAssociation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a>&gt;</span> <span class="element-name">get_clearAssociationActionOfAssociation</span>()</div>
<div class="block">Returns the value of the '<em><b>clear Association Action Of Association</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>ClearAssociationAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdintermediateactions/ClearAssociationAction.html#getAssociation()"><code><em>Association</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clear Association Action Of Association</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clear Association Action Of Association</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAssociation__clearAssociationActionOfAssociation()"><code>UMLPackage.getAssociation__clearAssociationActionOfAssociation()</code></a></li>
<li><a href="../../actions/mdintermediateactions/ClearAssociationAction.html#getAssociation()"><code>ClearAssociationAction.getAssociation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="association" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMemberEnd()">
<h3>getMemberEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getMemberEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>Member End</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="Property.html#getAssociation()"><code><em>Association</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Each end represents participation of instances of the Classifier connected to the end in links of the Association.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Member End</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAssociation_MemberEnd()"><code>UMLPackage.getAssociation_MemberEnd()</code></a></li>
<li><a href="Property.html#getAssociation()"><code>Property.getAssociation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="association" lower="2"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedEnd()">
<h3>getOwnedEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getOwnedEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned End</b></em>' containment reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="Property.html#getOwningAssociation()"><code><em>Owning Association</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ends that are owned by the Association itself.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned End</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAssociation_OwnedEnd()"><code>UMLPackage.getAssociation_OwnedEnd()</code></a></li>
<li><a href="Property.html#getOwningAssociation()"><code>Property.getOwningAssociation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningAssociation" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNavigableOwnedEnd()">
<h3>getNavigableOwnedEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getNavigableOwnedEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>Navigable Owned End</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is
 '<a href="Property.html#get_associationOfNavigableOwnedEnd()"><code><em>association Of Navigable Owned End</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The navigable ends that are owned by the Association itself.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Navigable Owned End</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAssociation_NavigableOwnedEnd()"><code>UMLPackage.getAssociation_NavigableOwnedEnd()</code></a></li>
<li><a href="Property.html#get_associationOfNavigableOwnedEnd()"><code>Property.get_associationOfNavigableOwnedEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_associationOfNavigableOwnedEnd" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndType()">
<h3>getEndType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt;</span> <span class="element-name">getEndType</span>()</div>
<div class="block">Returns the value of the '<em><b>End Type</b></em>' reference list.
 The list contents are of type <a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a>.
 It is bidirectional and its opposite is '<a href="Type.html#get_associationOfEndType()"><code><em>association Of End Type</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Classifiers that are used as types of the ends of the Association.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>End Type</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAssociation_EndType()"><code>UMLPackage.getAssociation_EndType()</code></a></li>
<li><a href="Type.html#get_associationOfEndType()"><code>Type.get_associationOfEndType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_associationOfEndType" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_connectorOfType()">
<h3>has_connectorOfType</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_connectorOfType</span>()
                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasMemberEnd()">
<h3>hasMemberEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasMemberEnd</span>()
              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedEnd()">
<h3>hasOwnedEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedEnd</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_clearAssociationActionOfAssociation()">
<h3>has_clearAssociationActionOfAssociation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_clearAssociationActionOfAssociation</span>()
                                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNavigableOwnedEnd()">
<h3>hasNavigableOwnedEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasNavigableOwnedEnd</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasEndType()">
<h3>hasEndType</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasEndType</span>()
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
