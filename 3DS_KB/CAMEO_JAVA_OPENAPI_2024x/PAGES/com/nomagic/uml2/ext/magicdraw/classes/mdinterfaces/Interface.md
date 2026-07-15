# JAVA OPENAPI: Interface (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/classes/mdinterfaces/Interface.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdinterfaces/Interface.html`
- source_sha256: `4b451cc70e3aaaf0f484d4abfac6464e01af39ca58d61d5e0d5a7829aab71c43`
- captured_utc: `2026-07-14T16:52:59.298484+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces](package-summary.html)

## Interface Interface

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Classifier](../mdkernel/Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../mdkernel/NamedElement.html)`, `[Namespace](../mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](../mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](../mdkernel/Type.html)`

public interfaceInterfaceextends [Classifier](../mdkernel/Classifier.html)

begin-user-doc 
 A representation of the model object '***Interface***'.
 end-user-doc 
begin-model-doc 
 Interfaces declare coherent services that are implemented by BehavioredClassifiers that implement the Interfaces via InterfaceRealizations.
 end-model-doc 
The following features are supported:
 [`*Nested Classifier*`](#getNestedClassifier())
[`*Owned Operation*`](#getOwnedOperation())
[`*Owned Reception*`](#getOwnedReception())
[`*Protocol*`](#getProtocol())
[`*Redefined Interface*`](#getRedefinedInterface())
[`*interface Of Redefined Interface*`](#get_interfaceOfRedefinedInterface())
[`*interface Realization Of Contract*`](#get_interfaceRealizationOfContract())
[`*Owned Attribute*`](#getOwnedAttribute())

See Also:
[`UMLPackage.getInterface()`](../../metadata/UMLPackage.html#getInterface())
Model:
annotation="MOF package='classes.mdinterfaces'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](Interface.html)>`
`[get_interfaceOfRedefinedInterface](#get_interfaceOfRedefinedInterface())()`
Returns the value of the '***interface Of Redefined Interface***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InterfaceRealization](InterfaceRealization.html)>`
`[get_interfaceRealizationOfContract](#get_interfaceRealizationOfContract())()`
Returns the value of the '***interface Realization Of Contract***' reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../mdkernel/Classifier.html)>`
`[getNestedClassifier](#getNestedClassifier())()`
Returns the value of the '***Nested Classifier***' containment reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../mdkernel/Property.html)>`
`[getOwnedAttribute](#getOwnedAttribute())()`
Returns the value of the '***Owned Attribute***' containment reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Operation](../mdkernel/Operation.html)>`
`[getOwnedOperation](#getOwnedOperation())()`
Returns the value of the '***Owned Operation***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Reception](../../commonbehaviors/mdcommunications/Reception.html)>`
`[getOwnedReception](#getOwnedReception())()`
Returns the value of the '***Owned Reception***' containment reference list.
`[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`
`[getProtocol](#getProtocol())()`
Returns the value of the '***Protocol***' containment reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](Interface.html)>`
`[getRedefinedInterface](#getRedefinedInterface())()`
Returns the value of the '***Redefined Interface***' reference list.
`boolean`
`[has_interfaceOfRedefinedInterface](#has_interfaceOfRedefinedInterface())()`

`boolean`
`[has_interfaceRealizationOfContract](#has_interfaceRealizationOfContract())()`

`boolean`
`[hasNestedClassifier](#hasNestedClassifier())()`

`boolean`
`[hasOwnedAttribute](#hasOwnedAttribute())()`

`boolean`
`[hasOwnedOperation](#hasOwnedOperation())()`

`boolean`
`[hasOwnedReception](#hasOwnedReception())()`

`boolean`
`[hasRedefinedInterface](#hasRedefinedInterface())()`

`void`
`[setProtocol](#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine))([ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) value)`
Sets the value of the '[`*Protocol*`](#getProtocol())' containment reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](../mdkernel/Classifier.html)
`[get_classifierOfRedefinedClassifier](../mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](../mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](../mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](../mdkernel/Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](../mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](../mdkernel/Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](../mdkernel/Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](../mdkernel/Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](../mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](../mdkernel/Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](../mdkernel/Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](../mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](../mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](../mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](../mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](../mdkernel/Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](../mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](../mdkernel/Classifier.html#getAttribute()), [getCollaborationUse](../mdkernel/Classifier.html#getCollaborationUse()), [getFeature](../mdkernel/Classifier.html#getFeature()), [getGeneral](../mdkernel/Classifier.html#getGeneral()), [getGeneralization](../mdkernel/Classifier.html#getGeneralization()), [getInheritedMember](../mdkernel/Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](../mdkernel/Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](../mdkernel/Classifier.html#getOwnedUseCase()), [getPowertypeExtent](../mdkernel/Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](../mdkernel/Classifier.html#getRedefinedClassifier()), [getRepresentation](../mdkernel/Classifier.html#getRepresentation()), [getSubstitution](../mdkernel/Classifier.html#getSubstitution()), [getTemplateParameter](../mdkernel/Classifier.html#getTemplateParameter()), [getUMLClass](../mdkernel/Classifier.html#getUMLClass()), [getUseCase](../mdkernel/Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](../mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](../mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](../mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](../mdkernel/Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](../mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](../mdkernel/Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](../mdkernel/Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](../mdkernel/Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](../mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](../mdkernel/Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](../mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](../mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](../mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](../mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](../mdkernel/Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](../mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](../mdkernel/Classifier.html#hasAttribute()), [hasCollaborationUse](../mdkernel/Classifier.html#hasCollaborationUse()), [hasFeature](../mdkernel/Classifier.html#hasFeature()), [hasGeneral](../mdkernel/Classifier.html#hasGeneral()), [hasGeneralization](../mdkernel/Classifier.html#hasGeneralization()), [hasInheritedMember](../mdkernel/Classifier.html#hasInheritedMember()), [hasOwnedUseCase](../mdkernel/Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](../mdkernel/Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](../mdkernel/Classifier.html#hasRedefinedClassifier()), [hasSubstitution](../mdkernel/Classifier.html#hasSubstitution()), [hasUseCase](../mdkernel/Classifier.html#hasUseCase()), [isAbstract](../mdkernel/Classifier.html#isAbstract()), [isFinalSpecialization](../mdkernel/Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](../mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setAbstract](../mdkernel/Classifier.html#setAbstract(boolean)), [setFinalSpecialization](../mdkernel/Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](../mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](../mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](../mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](../mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../mdkernel/Element.html#getOwnedElement()), [getOwner](../mdkernel/Element.html#getOwner()), [getSyncElement](../mdkernel/Element.html#getSyncElement()), [getTaggedValue](../mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../mdkernel/Element.html#hasTaggedValue()), [setOwner](../mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../mdkernel/NamedElement.html#getClientDependency()), [getName](../mdkernel/NamedElement.html#getName()), [getNameExpression](../mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../mdkernel/NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](../mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../mdkernel/Namespace.html)
`[getElementImport](../mdkernel/Namespace.html#getElementImport()), [getImportedMember](../mdkernel/Namespace.html#getImportedMember()), [getMember](../mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../mdkernel/Namespace.html#hasImportedMember()), [hasMember](../mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../mdkernel/Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](../mdkernel/PackageableElement.html)
`[get_componentOfPackagedElement](../mdkernel/PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](../mdkernel/PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](../mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](../mdkernel/PackageableElement.html#getOwningPackage()), [getVisibility](../mdkernel/PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](../mdkernel/PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](../mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](../mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](../mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](../mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](../mdkernel/Type.html)
`[get_associationOfEndType](../mdkernel/Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](../mdkernel/Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](../mdkernel/Type.html#get_operationOfRaisedException()), [get_typedElementOfType](../mdkernel/Type.html#get_typedElementOfType()), [getPackage](../mdkernel/Type.html#getPackage()), [has_associationOfEndType](../mdkernel/Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](../mdkernel/Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](../mdkernel/Type.html#has_operationOfRaisedException()), [has_typedElementOfType](../mdkernel/Type.html#has_typedElementOfType()), [setPackage](../mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
get_interfaceRealizationOfContract
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InterfaceRealization](InterfaceRealization.html)> get_interfaceRealizationOfContract()
Returns the value of the '***interface Realization Of Contract***' reference list.
 The list contents are of type [`InterfaceRealization`](InterfaceRealization.html).
 It is bidirectional and its opposite is '[`*Contract*`](InterfaceRealization.html#getContract())'.
 begin-user-doc 
If the meaning of the '*interface Realization Of Contract*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interface Realization Of Contract*' reference list.
See Also:
[`UMLPackage.getInterface__interfaceRealizationOfContract()`](../../metadata/UMLPackage.html#getInterface__interfaceRealizationOfContract())
[`InterfaceRealization.getContract()`](InterfaceRealization.html#getContract())
Model:
opposite="contract" ordered="false"
Generated:
getOwnedAttribute
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../mdkernel/Property.html)> getOwnedAttribute()
Returns the value of the '***Owned Attribute***' containment reference list.
 The list contents are of type [`Property`](../mdkernel/Property.html).
 It is bidirectional and its opposite is '[`*Interface*`](../mdkernel/Property.html#getInterface())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The attributes (i.e., the Properties) owned by the Interface.
 end-model-doc
Returns:
the value of the '*Owned Attribute*' containment reference list.
See Also:
[`UMLPackage.getInterface_OwnedAttribute()`](../../metadata/UMLPackage.html#getInterface_OwnedAttribute())
[`Property.getInterface()`](../mdkernel/Property.html#getInterface())
Model:
opposite="interface" containment="true" resolveProxies="true"
Generated:
getOwnedOperation
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Operation](../mdkernel/Operation.html)> getOwnedOperation()
Returns the value of the '***Owned Operation***' containment reference list.
 The list contents are of type [`Operation`](../mdkernel/Operation.html).
 It is bidirectional and its opposite is '[`*Interface*`](../mdkernel/Operation.html#getInterface())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Operations owned by the Interface.
 end-model-doc
Returns:
the value of the '*Owned Operation*' containment reference list.
See Also:
[`UMLPackage.getInterface_OwnedOperation()`](../../metadata/UMLPackage.html#getInterface_OwnedOperation())
[`Operation.getInterface()`](../mdkernel/Operation.html#getInterface())
Model:
opposite="interface" containment="true" resolveProxies="true"
Generated:
getNestedClassifier
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Classifier](../mdkernel/Classifier.html)> getNestedClassifier()
Returns the value of the '***Nested Classifier***' containment reference list.
 The list contents are of type [`Classifier`](../mdkernel/Classifier.html).
 It is bidirectional and its opposite is
 '[`*interface Of Nested Classifier*`](../mdkernel/Classifier.html#get_interfaceOfNestedClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References all the Classifiers that are defined (nested) within the Interface.
 end-model-doc
Returns:
the value of the '*Nested Classifier*' containment reference list.
See Also:
[`UMLPackage.getInterface_NestedClassifier()`](../../metadata/UMLPackage.html#getInterface_NestedClassifier())
[`Classifier.get_interfaceOfNestedClassifier()`](../mdkernel/Classifier.html#get_interfaceOfNestedClassifier())
Model:
opposite="_interfaceOfNestedClassifier" containment="true" resolveProxies="true"
Generated:
getRedefinedInterface
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](Interface.html)> getRedefinedInterface()
Returns the value of the '***Redefined Interface***' reference list.
 The list contents are of type [`Interface`](Interface.html).
 It is bidirectional and its opposite is
 '[`*interface Of Redefined Interface*`](#get_interfaceOfRedefinedInterface())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References all the Interfaces redefined by this Interface.
 end-model-doc
Returns:
the value of the '*Redefined Interface*' reference list.
See Also:
[`UMLPackage.getInterface_RedefinedInterface()`](../../metadata/UMLPackage.html#getInterface_RedefinedInterface())
[`get_interfaceOfRedefinedInterface()`](#get_interfaceOfRedefinedInterface())
Model:
opposite="_interfaceOfRedefinedInterface" ordered="false"
Generated:
get_interfaceOfRedefinedInterface
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](Interface.html)> get_interfaceOfRedefinedInterface()
Returns the value of the '***interface Of Redefined Interface***' reference list.
 The list contents are of type [`Interface`](Interface.html).
 It is bidirectional and its opposite is
 '[`*Redefined Interface*`](#getRedefinedInterface())'.
 begin-user-doc 
If the meaning of the '*interface Of Redefined Interface*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interface Of Redefined Interface*' reference list.
See Also:
[`UMLPackage.getInterface__interfaceOfRedefinedInterface()`](../../metadata/UMLPackage.html#getInterface__interfaceOfRedefinedInterface())
[`getRedefinedInterface()`](#getRedefinedInterface())
Model:
opposite="redefinedInterface" ordered="false"
Generated:
getOwnedReception
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Reception](../../commonbehaviors/mdcommunications/Reception.html)> getOwnedReception()
Returns the value of the '***Owned Reception***' containment reference list.
 The list contents are of type [`Reception`](../../commonbehaviors/mdcommunications/Reception.html).
 It is bidirectional and its opposite is
 '[`*interface Of Owned Reception*`](../../commonbehaviors/mdcommunications/Reception.html#get_interfaceOfOwnedReception())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Receptions that objects providing this Interface are willing to accept.
 end-model-doc
Returns:
the value of the '*Owned Reception*' containment reference list.
See Also:
[`UMLPackage.getInterface_OwnedReception()`](../../metadata/UMLPackage.html#getInterface_OwnedReception())
[`Reception.get_interfaceOfOwnedReception()`](../../commonbehaviors/mdcommunications/Reception.html#get_interfaceOfOwnedReception())
Model:
opposite="_interfaceOfOwnedReception" containment="true" resolveProxies="true" ordered="false"
Generated:
getProtocol
@CheckForNull[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) getProtocol()
Returns the value of the '***Protocol***' containment reference.
 It is bidirectional and its opposite is
 '[`*Interface*`](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#getInterface())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References a ProtocolStateMachine specifying the legal sequences of the invocation of the BehavioralFeatures described in the Interface.
 end-model-doc
Returns:
the value of the '*Protocol*' containment reference.
See Also:
[`setProtocol(ProtocolStateMachine)`](#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine))
[`UMLPackage.getInterface_Protocol()`](../../metadata/UMLPackage.html#getInterface_Protocol())
[`ProtocolStateMachine.getInterface()`](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#getInterface())
Model:
opposite="interface" containment="true" resolveProxies="true" ordered="false"
Generated:
setProtocol
void setProtocol(@CheckForNull
 [ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) value)
Sets the value of the '[`*Protocol*`](#getProtocol())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Protocol*' containment reference.
See Also:
[`getProtocol()`](#getProtocol())
Generated:
has_interfaceRealizationOfContract
boolean has_interfaceRealizationOfContract()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedAttribute
boolean hasOwnedAttribute()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedOperation
boolean hasOwnedOperation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasNestedClassifier
boolean hasNestedClassifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedInterface
boolean hasRedefinedInterface()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_interfaceOfRedefinedInterface
boolean has_interfaceOfRedefinedInterface()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedReception
boolean hasOwnedReception()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces</a></div>
<h1 class="title" title="Interface Interface">Interface Interface</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Interface</span><span class="extends-implements">
extends <a href="../mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Interface</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 Interfaces declare coherent services that are implemented by BehavioredClassifiers that implement the Interfaces via InterfaceRealizations.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getNestedClassifier()"><code><em>Nested Classifier</em></code></a></li>
<li><a href="#getOwnedOperation()"><code><em>Owned Operation</em></code></a></li>
<li><a href="#getOwnedReception()"><code><em>Owned Reception</em></code></a></li>
<li><a href="#getProtocol()"><code><em>Protocol</em></code></a></li>
<li><a href="#getRedefinedInterface()"><code><em>Redefined Interface</em></code></a></li>
<li><a href="#get_interfaceOfRedefinedInterface()"><code><em>interface Of Redefined Interface</em></code></a></li>
<li><a href="#get_interfaceRealizationOfContract()"><code><em>interface Realization Of Contract</em></code></a></li>
<li><a href="#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getInterface()"><code>UMLPackage.getInterface()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='classes.mdinterfaces'"</dd>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interfaceOfRedefinedInterface()">get_interfaceOfRedefinedInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interface Of Redefined Interface</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interfaceRealizationOfContract()">get_interfaceRealizationOfContract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interface Realization Of Contract</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedClassifier()">getNestedClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Nested Classifier</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAttribute()">getOwnedAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Attribute</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedOperation()">getOwnedOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Operation</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedReception()">getOwnedReception</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Reception</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProtocol()">getProtocol</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Protocol</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedInterface()">getRedefinedInterface</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Interface</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_interfaceOfRedefinedInterface()">has_interfaceOfRedefinedInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_interfaceRealizationOfContract()">has_interfaceRealizationOfContract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasNestedClassifier()">hasNestedClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedAttribute()">hasOwnedAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedOperation()">hasOwnedOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedReception()">hasOwnedReception</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedInterface()">hasRedefinedInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)">setProtocol</a><wbr/>(<a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getProtocol()"><code><em>Protocol</em></code></a>' containment reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="../mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="../mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="../mdkernel/Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="../mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="../mdkernel/Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="../mdkernel/Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="../mdkernel/Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="../mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="../mdkernel/Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="../mdkernel/Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="../mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="../mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="../mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="../mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="../mdkernel/Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="../mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="../mdkernel/Classifier.html#getAttribute()">getAttribute</a>, <a href="../mdkernel/Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="../mdkernel/Classifier.html#getFeature()">getFeature</a>, <a href="../mdkernel/Classifier.html#getGeneral()">getGeneral</a>, <a href="../mdkernel/Classifier.html#getGeneralization()">getGeneralization</a>, <a href="../mdkernel/Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="../mdkernel/Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../mdkernel/Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="../mdkernel/Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="../mdkernel/Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="../mdkernel/Classifier.html#getRepresentation()">getRepresentation</a>, <a href="../mdkernel/Classifier.html#getSubstitution()">getSubstitution</a>, <a href="../mdkernel/Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../mdkernel/Classifier.html#getUMLClass()">getUMLClass</a>, <a href="../mdkernel/Classifier.html#getUseCase()">getUseCase</a>, <a href="../mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="../mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="../mdkernel/Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="../mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="../mdkernel/Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="../mdkernel/Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="../mdkernel/Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="../mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="../mdkernel/Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="../mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="../mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="../mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="../mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="../mdkernel/Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="../mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="../mdkernel/Classifier.html#hasAttribute()">hasAttribute</a>, <a href="../mdkernel/Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="../mdkernel/Classifier.html#hasFeature()">hasFeature</a>, <a href="../mdkernel/Classifier.html#hasGeneral()">hasGeneral</a>, <a href="../mdkernel/Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="../mdkernel/Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="../mdkernel/Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="../mdkernel/Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="../mdkernel/Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="../mdkernel/Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="../mdkernel/Classifier.html#hasUseCase()">hasUseCase</a>, <a href="../mdkernel/Classifier.html#isAbstract()">isAbstract</a>, <a href="../mdkernel/Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="../mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="../mdkernel/Classifier.html#setAbstract(boolean)">setAbstract</a>, <a href="../mdkernel/Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="../mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="../mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="../mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="../mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../mdkernel/NamedElement.html#getName()">getName</a>, <a href="../mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="../mdkernel/PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="../mdkernel/PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="../mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="../mdkernel/PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="../mdkernel/PackageableElement.html#getVisibility()">getVisibility</a>, <a href="../mdkernel/PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="../mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="../mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="../mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="../mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="../mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></h3>
<code><a href="../mdkernel/Type.html#get_associationOfEndType()">get_associationOfEndType</a>, <a href="../mdkernel/Type.html#get_behavioralFeatureOfRaisedException()">get_behavioralFeatureOfRaisedException</a>, <a href="../mdkernel/Type.html#get_operationOfRaisedException()">get_operationOfRaisedException</a>, <a href="../mdkernel/Type.html#get_typedElementOfType()">get_typedElementOfType</a>, <a href="../mdkernel/Type.html#getPackage()">getPackage</a>, <a href="../mdkernel/Type.html#has_associationOfEndType()">has_associationOfEndType</a>, <a href="../mdkernel/Type.html#has_behavioralFeatureOfRaisedException()">has_behavioralFeatureOfRaisedException</a>, <a href="../mdkernel/Type.html#has_operationOfRaisedException()">has_operationOfRaisedException</a>, <a href="../mdkernel/Type.html#has_typedElementOfType()">has_typedElementOfType</a>, <a href="../mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setPackage</a></code></div>
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
<section class="detail" id="get_interfaceRealizationOfContract()">
<h3>get_interfaceRealizationOfContract</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a>&gt;</span> <span class="element-name">get_interfaceRealizationOfContract</span>()</div>
<div class="block">Returns the value of the '<em><b>interface Realization Of Contract</b></em>' reference list.
 The list contents are of type <a href="InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>InterfaceRealization</code></a>.
 It is bidirectional and its opposite is '<a href="InterfaceRealization.html#getContract()"><code><em>Contract</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interface Realization Of Contract</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interface Realization Of Contract</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface__interfaceRealizationOfContract()"><code>UMLPackage.getInterface__interfaceRealizationOfContract()</code></a></li>
<li><a href="InterfaceRealization.html#getContract()"><code>InterfaceRealization.getContract()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="contract" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAttribute()">
<h3>getOwnedAttribute</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getOwnedAttribute</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Attribute</b></em>' containment reference list.
 The list contents are of type <a href="../mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="../mdkernel/Property.html#getInterface()"><code><em>Interface</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The attributes (i.e., the Properties) owned by the Interface.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Attribute</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface_OwnedAttribute()"><code>UMLPackage.getInterface_OwnedAttribute()</code></a></li>
<li><a href="../mdkernel/Property.html#getInterface()"><code>Property.getInterface()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="interface" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOperation()">
<h3>getOwnedOperation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getOwnedOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Operation</b></em>' containment reference list.
 The list contents are of type <a href="../mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.
 It is bidirectional and its opposite is '<a href="../mdkernel/Operation.html#getInterface()"><code><em>Interface</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Operations owned by the Interface.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Operation</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface_OwnedOperation()"><code>UMLPackage.getInterface_OwnedOperation()</code></a></li>
<li><a href="../mdkernel/Operation.html#getInterface()"><code>Operation.getInterface()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="interface" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedClassifier()">
<h3>getNestedClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getNestedClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Nested Classifier</b></em>' containment reference list.
 The list contents are of type <a href="../mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdkernel/Classifier.html#get_interfaceOfNestedClassifier()"><code><em>interface Of Nested Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References all the Classifiers that are defined (nested) within the Interface.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Nested Classifier</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface_NestedClassifier()"><code>UMLPackage.getInterface_NestedClassifier()</code></a></li>
<li><a href="../mdkernel/Classifier.html#get_interfaceOfNestedClassifier()"><code>Classifier.get_interfaceOfNestedClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_interfaceOfNestedClassifier" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedInterface()">
<h3>getRedefinedInterface</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getRedefinedInterface</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Interface</b></em>' reference list.
 The list contents are of type <a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_interfaceOfRedefinedInterface()"><code><em>interface Of Redefined Interface</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References all the Interfaces redefined by this Interface.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Interface</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface_RedefinedInterface()"><code>UMLPackage.getInterface_RedefinedInterface()</code></a></li>
<li><a href="#get_interfaceOfRedefinedInterface()"><code>get_interfaceOfRedefinedInterface()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_interfaceOfRedefinedInterface" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interfaceOfRedefinedInterface()">
<h3>get_interfaceOfRedefinedInterface</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">get_interfaceOfRedefinedInterface</span>()</div>
<div class="block">Returns the value of the '<em><b>interface Of Redefined Interface</b></em>' reference list.
 The list contents are of type <a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getRedefinedInterface()"><code><em>Redefined Interface</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interface Of Redefined Interface</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interface Of Redefined Interface</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface__interfaceOfRedefinedInterface()"><code>UMLPackage.getInterface__interfaceOfRedefinedInterface()</code></a></li>
<li><a href="#getRedefinedInterface()"><code>getRedefinedInterface()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedInterface" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReception()">
<h3>getOwnedReception</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</span> <span class="element-name">getOwnedReception</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Reception</b></em>' containment reference list.
 The list contents are of type <a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdcommunications/Reception.html#get_interfaceOfOwnedReception()"><code><em>interface Of Owned Reception</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Receptions that objects providing this Interface are willing to accept.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Reception</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterface_OwnedReception()"><code>UMLPackage.getInterface_OwnedReception()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/Reception.html#get_interfaceOfOwnedReception()"><code>Reception.get_interfaceOfOwnedReception()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_interfaceOfOwnedReception" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProtocol()">
<h3>getProtocol</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></span> <span class="element-name">getProtocol</span>()</div>
<div class="block">Returns the value of the '<em><b>Protocol</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#getInterface()"><code><em>Interface</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References a ProtocolStateMachine specifying the legal sequences of the invocation of the BehavioralFeatures described in the Interface.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Protocol</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)"><code>setProtocol(ProtocolStateMachine)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInterface_Protocol()"><code>UMLPackage.getInterface_Protocol()</code></a></li>
<li><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#getInterface()"><code>ProtocolStateMachine.getInterface()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="interface" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)">
<h3>setProtocol</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setProtocol</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getProtocol()"><code><em>Protocol</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Protocol</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getProtocol()"><code>getProtocol()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_interfaceRealizationOfContract()">
<h3>has_interfaceRealizationOfContract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_interfaceRealizationOfContract</span>()
                                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedAttribute()">
<h3>hasOwnedAttribute</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedAttribute</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedOperation()">
<h3>hasOwnedOperation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedOperation</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNestedClassifier()">
<h3>hasNestedClassifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasNestedClassifier</span>()
                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedInterface()">
<h3>hasRedefinedInterface</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedInterface</span>()
                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_interfaceOfRedefinedInterface()">
<h3>has_interfaceOfRedefinedInterface</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_interfaceOfRedefinedInterface</span>()
                                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedReception()">
<h3>hasOwnedReception</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedReception</span>()
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
