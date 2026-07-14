# JAVA OPENAPI: Signal (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html
- source_path: `com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html`
- source_sha256: `2091aa0d474e64928a9e46368c202b1b8b1692ef771d3eed2b4bf3259f074b5d`
- captured_utc: `2026-07-14T16:56:23.890776+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications](package-summary.html)

## Interface Signal

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Classifier](../../classes/mdkernel/Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../../classes/mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](../../classes/mdkernel/Type.html)`

public interfaceSignalextends [Classifier](../../classes/mdkernel/Classifier.html)

begin-user-doc 
 A representation of the model object '***Signal***'.
 end-user-doc 
begin-model-doc 
 A Signal is a specification of a kind of communication between objects in which a reaction is asynchronously triggered in the receiver without a reply.
 end-model-doc 
The following features are supported:
 [`*Owned Attribute*`](#getOwnedAttribute())
[`*signal Event Of Signal*`](#get_signalEventOfSignal())
[`*send Signal Action Of Signal*`](#get_sendSignalActionOfSignal())
[`*broadcast Signal Action Of Signal*`](#get_broadcastSignalActionOfSignal())
[`*reception Of Signal*`](#get_receptionOfSignal())

See Also:
[`UMLPackage.getSignal()`](../../metadata/UMLPackage.html#getSignal())
Model:
annotation="MOF package='commonbehaviors.mdcommunications'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BroadcastSignalAction](../../actions/mdintermediateactions/BroadcastSignalAction.html)>`
`[get_broadcastSignalActionOfSignal](#get_broadcastSignalActionOfSignal())()`
Returns the value of the '***broadcast Signal Action Of Signal***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Reception](Reception.html)>`
`[get_receptionOfSignal](#get_receptionOfSignal())()`
Returns the value of the '***reception Of Signal***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SendSignalAction](../../actions/mdbasicactions/SendSignalAction.html)>`
`[get_sendSignalActionOfSignal](#get_sendSignalActionOfSignal())()`
Returns the value of the '***send Signal Action Of Signal***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SignalEvent](SignalEvent.html)>`
`[get_signalEventOfSignal](#get_signalEventOfSignal())()`
Returns the value of the '***signal Event Of Signal***' reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../classes/mdkernel/Property.html)>`
`[getOwnedAttribute](#getOwnedAttribute())()`
Returns the value of the '***Owned Attribute***' containment reference list.
`boolean`
`[has_broadcastSignalActionOfSignal](#has_broadcastSignalActionOfSignal())()`

`boolean`
`[has_receptionOfSignal](#has_receptionOfSignal())()`

`boolean`
`[has_sendSignalActionOfSignal](#has_sendSignalActionOfSignal())()`

`boolean`
`[has_signalEventOfSignal](#has_signalEventOfSignal())()`

`boolean`
`[hasOwnedAttribute](#hasOwnedAttribute())()`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](../../classes/mdkernel/Classifier.html)
`[get_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](../../classes/mdkernel/Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](../../classes/mdkernel/Classifier.html#getAttribute()), [getCollaborationUse](../../classes/mdkernel/Classifier.html#getCollaborationUse()), [getFeature](../../classes/mdkernel/Classifier.html#getFeature()), [getGeneral](../../classes/mdkernel/Classifier.html#getGeneral()), [getGeneralization](../../classes/mdkernel/Classifier.html#getGeneralization()), [getInheritedMember](../../classes/mdkernel/Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](../../classes/mdkernel/Classifier.html#getOwnedUseCase()), [getPowertypeExtent](../../classes/mdkernel/Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](../../classes/mdkernel/Classifier.html#getRedefinedClassifier()), [getRepresentation](../../classes/mdkernel/Classifier.html#getRepresentation()), [getSubstitution](../../classes/mdkernel/Classifier.html#getSubstitution()), [getTemplateParameter](../../classes/mdkernel/Classifier.html#getTemplateParameter()), [getUMLClass](../../classes/mdkernel/Classifier.html#getUMLClass()), [getUseCase](../../classes/mdkernel/Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](../../classes/mdkernel/Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](../../classes/mdkernel/Classifier.html#hasAttribute()), [hasCollaborationUse](../../classes/mdkernel/Classifier.html#hasCollaborationUse()), [hasFeature](../../classes/mdkernel/Classifier.html#hasFeature()), [hasGeneral](../../classes/mdkernel/Classifier.html#hasGeneral()), [hasGeneralization](../../classes/mdkernel/Classifier.html#hasGeneralization()), [hasInheritedMember](../../classes/mdkernel/Classifier.html#hasInheritedMember()), [hasOwnedUseCase](../../classes/mdkernel/Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](../../classes/mdkernel/Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()), [hasSubstitution](../../classes/mdkernel/Classifier.html#hasSubstitution()), [hasUseCase](../../classes/mdkernel/Classifier.html#hasUseCase()), [isAbstract](../../classes/mdkernel/Classifier.html#isAbstract()), [isFinalSpecialization](../../classes/mdkernel/Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setAbstract](../../classes/mdkernel/Classifier.html#setAbstract(boolean)), [setFinalSpecialization](../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](../../classes/mdkernel/PackageableElement.html)
`[get_componentOfPackagedElement](../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](../../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](../../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](../../classes/mdkernel/PackageableElement.html#getOwningPackage()), [getVisibility](../../classes/mdkernel/PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](../../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](../../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](../../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](../../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](../../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](../../classes/mdkernel/Type.html)
`[get_associationOfEndType](../../classes/mdkernel/Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](../../classes/mdkernel/Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](../../classes/mdkernel/Type.html#get_operationOfRaisedException()), [get_typedElementOfType](../../classes/mdkernel/Type.html#get_typedElementOfType()), [getPackage](../../classes/mdkernel/Type.html#getPackage()), [has_associationOfEndType](../../classes/mdkernel/Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](../../classes/mdkernel/Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](../../classes/mdkernel/Type.html#has_operationOfRaisedException()), [has_typedElementOfType](../../classes/mdkernel/Type.html#has_typedElementOfType()), [setPackage](../../classes/mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
getOwnedAttribute
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../classes/mdkernel/Property.html)> getOwnedAttribute()
Returns the value of the '***Owned Attribute***' containment reference list.
 The list contents are of type [`Property`](../../classes/mdkernel/Property.html).
 It is bidirectional and its opposite is '[`*Owning Signal*`](../../classes/mdkernel/Property.html#getOwningSignal())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The attributes owned by the Signal.
 end-model-doc
Returns:
the value of the '*Owned Attribute*' containment reference list.
See Also:
[`UMLPackage.getSignal_OwnedAttribute()`](../../metadata/UMLPackage.html#getSignal_OwnedAttribute())
[`Property.getOwningSignal()`](../../classes/mdkernel/Property.html#getOwningSignal())
Model:
opposite="owningSignal" containment="true" resolveProxies="true"
Generated:
get_signalEventOfSignal
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SignalEvent](SignalEvent.html)> get_signalEventOfSignal()
Returns the value of the '***signal Event Of Signal***' reference list.
 The list contents are of type [`SignalEvent`](SignalEvent.html).
 It is bidirectional and its opposite is '[`*Signal*`](SignalEvent.html#getSignal())'.
 begin-user-doc 
If the meaning of the '*signal Event Of Signal*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*signal Event Of Signal*' reference list.
See Also:
[`UMLPackage.getSignal__signalEventOfSignal()`](../../metadata/UMLPackage.html#getSignal__signalEventOfSignal())
[`SignalEvent.getSignal()`](SignalEvent.html#getSignal())
Model:
opposite="signal" ordered="false"
Generated:
get_broadcastSignalActionOfSignal
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BroadcastSignalAction](../../actions/mdintermediateactions/BroadcastSignalAction.html)> get_broadcastSignalActionOfSignal()
Returns the value of the '***broadcast Signal Action Of Signal***' reference list.
 The list contents are of type [`BroadcastSignalAction`](../../actions/mdintermediateactions/BroadcastSignalAction.html).
 It is bidirectional and its opposite is '[`*Signal*`](../../actions/mdintermediateactions/BroadcastSignalAction.html#getSignal())'.
 begin-user-doc 
If the meaning of the '*broadcast Signal Action Of Signal*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*broadcast Signal Action Of Signal*' reference list.
See Also:
[`UMLPackage.getSignal__broadcastSignalActionOfSignal()`](../../metadata/UMLPackage.html#getSignal__broadcastSignalActionOfSignal())
[`BroadcastSignalAction.getSignal()`](../../actions/mdintermediateactions/BroadcastSignalAction.html#getSignal())
Model:
opposite="signal" ordered="false"
Generated:
get_sendSignalActionOfSignal
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SendSignalAction](../../actions/mdbasicactions/SendSignalAction.html)> get_sendSignalActionOfSignal()
Returns the value of the '***send Signal Action Of Signal***' reference list.
 The list contents are of type [`SendSignalAction`](../../actions/mdbasicactions/SendSignalAction.html).
 It is bidirectional and its opposite is '[`*Signal*`](../../actions/mdbasicactions/SendSignalAction.html#getSignal())'.
 begin-user-doc 
If the meaning of the '*send Signal Action Of Signal*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*send Signal Action Of Signal*' reference list.
See Also:
[`UMLPackage.getSignal__sendSignalActionOfSignal()`](../../metadata/UMLPackage.html#getSignal__sendSignalActionOfSignal())
[`SendSignalAction.getSignal()`](../../actions/mdbasicactions/SendSignalAction.html#getSignal())
Model:
opposite="signal" ordered="false"
Generated:
get_receptionOfSignal
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Reception](Reception.html)> get_receptionOfSignal()
Returns the value of the '***reception Of Signal***' reference list.
 The list contents are of type [`Reception`](Reception.html).
 It is bidirectional and its opposite is '[`*Signal*`](Reception.html#getSignal())'.
 begin-user-doc 
If the meaning of the '*reception Of Signal*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reception Of Signal*' reference list.
See Also:
[`UMLPackage.getSignal__receptionOfSignal()`](../../metadata/UMLPackage.html#getSignal__receptionOfSignal())
[`Reception.getSignal()`](Reception.html#getSignal())
Model:
opposite="signal" ordered="false"
Generated:
hasOwnedAttribute
boolean hasOwnedAttribute()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_signalEventOfSignal
boolean has_signalEventOfSignal()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_broadcastSignalActionOfSignal
boolean has_broadcastSignalActionOfSignal()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_sendSignalActionOfSignal
boolean has_sendSignalActionOfSignal()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_receptionOfSignal
boolean has_receptionOfSignal()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications</a></div>
<h1 class="title" title="Interface Signal">Interface Signal</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Signal</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Signal</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Signal is a specification of a kind of communication between objects in which a reaction is asynchronously triggered in the receiver without a reply.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a></li>
<li><a href="#get_signalEventOfSignal()"><code><em>signal Event Of Signal</em></code></a></li>
<li><a href="#get_sendSignalActionOfSignal()"><code><em>send Signal Action Of Signal</em></code></a></li>
<li><a href="#get_broadcastSignalActionOfSignal()"><code><em>broadcast Signal Action Of Signal</em></code></a></li>
<li><a href="#get_receptionOfSignal()"><code><em>reception Of Signal</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getSignal()"><code>UMLPackage.getSignal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='commonbehaviors.mdcommunications'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_broadcastSignalActionOfSignal()">get_broadcastSignalActionOfSignal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>broadcast Signal Action Of Signal</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_receptionOfSignal()">get_receptionOfSignal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reception Of Signal</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_sendSignalActionOfSignal()">get_sendSignalActionOfSignal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>send Signal Action Of Signal</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_signalEventOfSignal()">get_signalEventOfSignal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>signal Event Of Signal</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAttribute()">getOwnedAttribute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Attribute</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_broadcastSignalActionOfSignal()">has_broadcastSignalActionOfSignal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_receptionOfSignal()">has_receptionOfSignal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_sendSignalActionOfSignal()">has_sendSignalActionOfSignal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_signalEventOfSignal()">has_signalEventOfSignal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedAttribute()">hasOwnedAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#atInsert()">atInsert</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#clone()">clone</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#getAttribute()">getAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#getFeature()">getFeature</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneral()">getGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneralization()">getGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#getRepresentation()">getRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#getSubstitution()">getSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#getUMLClass()">getUMLClass</a>, <a href="../../classes/mdkernel/Classifier.html#getUseCase()">getUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#hasAttribute()">hasAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#hasFeature()">hasFeature</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneral()">hasGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#hasUseCase()">hasUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#isAbstract()">isAbstract</a>, <a href="../../classes/mdkernel/Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#setAbstract(boolean)">setAbstract</a>, <a href="../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="../../classes/mdkernel/PackageableElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="../../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></h3>
<code><a href="../../classes/mdkernel/Type.html#get_associationOfEndType()">get_associationOfEndType</a>, <a href="../../classes/mdkernel/Type.html#get_behavioralFeatureOfRaisedException()">get_behavioralFeatureOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#get_operationOfRaisedException()">get_operationOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#get_typedElementOfType()">get_typedElementOfType</a>, <a href="../../classes/mdkernel/Type.html#getPackage()">getPackage</a>, <a href="../../classes/mdkernel/Type.html#has_associationOfEndType()">has_associationOfEndType</a>, <a href="../../classes/mdkernel/Type.html#has_behavioralFeatureOfRaisedException()">has_behavioralFeatureOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#has_operationOfRaisedException()">has_operationOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#has_typedElementOfType()">has_typedElementOfType</a>, <a href="../../classes/mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setPackage</a></code></div>
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
<section class="detail" id="getOwnedAttribute()">
<h3>getOwnedAttribute</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getOwnedAttribute</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Attribute</b></em>' containment reference list.
 The list contents are of type <a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/Property.html#getOwningSignal()"><code><em>Owning Signal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The attributes owned by the Signal.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Attribute</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getSignal_OwnedAttribute()"><code>UMLPackage.getSignal_OwnedAttribute()</code></a></li>
<li><a href="../../classes/mdkernel/Property.html#getOwningSignal()"><code>Property.getOwningSignal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningSignal" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_signalEventOfSignal()">
<h3>get_signalEventOfSignal</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a>&gt;</span> <span class="element-name">get_signalEventOfSignal</span>()</div>
<div class="block">Returns the value of the '<em><b>signal Event Of Signal</b></em>' reference list.
 The list contents are of type <a href="SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>SignalEvent</code></a>.
 It is bidirectional and its opposite is '<a href="SignalEvent.html#getSignal()"><code><em>Signal</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>signal Event Of Signal</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>signal Event Of Signal</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getSignal__signalEventOfSignal()"><code>UMLPackage.getSignal__signalEventOfSignal()</code></a></li>
<li><a href="SignalEvent.html#getSignal()"><code>SignalEvent.getSignal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="signal" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_broadcastSignalActionOfSignal()">
<h3>get_broadcastSignalActionOfSignal</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a>&gt;</span> <span class="element-name">get_broadcastSignalActionOfSignal</span>()</div>
<div class="block">Returns the value of the '<em><b>broadcast Signal Action Of Signal</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>BroadcastSignalAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdintermediateactions/BroadcastSignalAction.html#getSignal()"><code><em>Signal</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>broadcast Signal Action Of Signal</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>broadcast Signal Action Of Signal</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getSignal__broadcastSignalActionOfSignal()"><code>UMLPackage.getSignal__broadcastSignalActionOfSignal()</code></a></li>
<li><a href="../../actions/mdintermediateactions/BroadcastSignalAction.html#getSignal()"><code>BroadcastSignalAction.getSignal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="signal" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_sendSignalActionOfSignal()">
<h3>get_sendSignalActionOfSignal</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a>&gt;</span> <span class="element-name">get_sendSignalActionOfSignal</span>()</div>
<div class="block">Returns the value of the '<em><b>send Signal Action Of Signal</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>SendSignalAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/SendSignalAction.html#getSignal()"><code><em>Signal</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>send Signal Action Of Signal</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>send Signal Action Of Signal</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getSignal__sendSignalActionOfSignal()"><code>UMLPackage.getSignal__sendSignalActionOfSignal()</code></a></li>
<li><a href="../../actions/mdbasicactions/SendSignalAction.html#getSignal()"><code>SendSignalAction.getSignal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="signal" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_receptionOfSignal()">
<h3>get_receptionOfSignal</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</span> <span class="element-name">get_receptionOfSignal</span>()</div>
<div class="block">Returns the value of the '<em><b>reception Of Signal</b></em>' reference list.
 The list contents are of type <a href="Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.
 It is bidirectional and its opposite is '<a href="Reception.html#getSignal()"><code><em>Signal</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reception Of Signal</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reception Of Signal</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getSignal__receptionOfSignal()"><code>UMLPackage.getSignal__receptionOfSignal()</code></a></li>
<li><a href="Reception.html#getSignal()"><code>Reception.getSignal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="signal" ordered="false"</dd>
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
<section class="detail" id="has_signalEventOfSignal()">
<h3>has_signalEventOfSignal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_signalEventOfSignal</span>()
                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_broadcastSignalActionOfSignal()">
<h3>has_broadcastSignalActionOfSignal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_broadcastSignalActionOfSignal</span>()
                                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_sendSignalActionOfSignal()">
<h3>has_sendSignalActionOfSignal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_sendSignalActionOfSignal</span>()
                              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_receptionOfSignal()">
<h3>has_receptionOfSignal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_receptionOfSignal</span>()
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
