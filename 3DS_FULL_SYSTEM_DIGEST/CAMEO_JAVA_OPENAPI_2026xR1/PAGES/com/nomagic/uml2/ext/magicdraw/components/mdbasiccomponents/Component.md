# JAVA OPENAPI: Component (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/components/mdbasiccomponents/Component.html
- source_path: `com/nomagic/uml2/ext/magicdraw/components/mdbasiccomponents/Component.html`
- source_sha256: `1d431260a2d80d07d17df12ee48b99e72a07cbd98f0af68bc5633029b85b0d3a`
- captured_utc: `2026-07-14T16:46:31.508219+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents](package-summary.html)

## Interface Component

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[Class](../../classes/mdkernel/Class.html)`, `[Classifier](../../classes/mdkernel/Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../../classes/mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](../../classes/mdkernel/Type.html)`

public interfaceComponentextends [Class](../../classes/mdkernel/Class.html)

begin-user-doc 
 A representation of the model object '***Component***'.
 end-user-doc 
begin-model-doc 
 A Component represents a modular part of a system that encapsulates its contents and whose manifestation is replaceable within its environment.
 end-model-doc 
The following features are supported:
 [`*Indirectly Instantiated*`](#isIndirectlyInstantiated())
[`*Packaged Element*`](#getPackagedElement())
[`*Realization*`](#getRealization())
[`*Required*`](#getRequired())
[`*Provided*`](#getProvided())

See Also:
[`UMLPackage.getComponent()`](../../metadata/UMLPackage.html#getComponent())
Model:
annotation="MOF package='components.mdbasiccomponents'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PackageableElement](../../classes/mdkernel/PackageableElement.html)>`
`[getPackagedElement](#getPackagedElement())()`
Returns the value of the '***Packaged Element***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)>`
`[getProvided](#getProvided())()`
Returns the value of the '***Provided***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ComponentRealization](ComponentRealization.html)>`
`[getRealization](#getRealization())()`
Returns the value of the '***Realization***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)>`
`[getRequired](#getRequired())()`
Returns the value of the '***Required***' reference list.
`boolean`
`[hasPackagedElement](#hasPackagedElement())()`

`boolean`
`[hasProvided](#hasProvided())()`

`boolean`
`[hasRealization](#hasRealization())()`

`boolean`
`[hasRequired](#hasRequired())()`

`boolean`
`[isIndirectlyInstantiated](#isIndirectlyInstantiated())()`
Returns the value of the '***Indirectly Instantiated***' attribute.
`void`
`[setIndirectlyInstantiated](#setIndirectlyInstantiated(boolean))(boolean value)`
Sets the value of the '[`*Indirectly Instantiated*`](#isIndirectlyInstantiated())'
 attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)
`[getClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getClassifierBehavior()), [getInterfaceRealization](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()), [getOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getOwnedBehavior()), [hasInterfaceRealization](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasInterfaceRealization()), [hasOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasOwnedBehavior()), [setClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Class](../../classes/mdkernel/Class.html)
`[getExtension](../../classes/mdkernel/Class.html#getExtension()), [getNestedClassifier](../../classes/mdkernel/Class.html#getNestedClassifier()), [getOwnedAttribute](../../classes/mdkernel/Class.html#getOwnedAttribute()), [getOwnedOperation](../../classes/mdkernel/Class.html#getOwnedOperation()), [getOwnedReception](../../classes/mdkernel/Class.html#getOwnedReception()), [getSuperClass](../../classes/mdkernel/Class.html#getSuperClass()), [hasExtension](../../classes/mdkernel/Class.html#hasExtension()), [hasNestedClassifier](../../classes/mdkernel/Class.html#hasNestedClassifier()), [hasOwnedOperation](../../classes/mdkernel/Class.html#hasOwnedOperation()), [hasOwnedReception](../../classes/mdkernel/Class.html#hasOwnedReception()), [hasSuperClass](../../classes/mdkernel/Class.html#hasSuperClass()), [isAbstract](../../classes/mdkernel/Class.html#isAbstract()), [isActive](../../classes/mdkernel/Class.html#isActive()), [setAbstract](../../classes/mdkernel/Class.html#setAbstract(boolean)), [setActive](../../classes/mdkernel/Class.html#setActive(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](../../classes/mdkernel/Classifier.html)
`[get_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](../../classes/mdkernel/Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](../../classes/mdkernel/Classifier.html#getAttribute()), [getCollaborationUse](../../classes/mdkernel/Classifier.html#getCollaborationUse()), [getFeature](../../classes/mdkernel/Classifier.html#getFeature()), [getGeneral](../../classes/mdkernel/Classifier.html#getGeneral()), [getGeneralization](../../classes/mdkernel/Classifier.html#getGeneralization()), [getInheritedMember](../../classes/mdkernel/Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](../../classes/mdkernel/Classifier.html#getOwnedUseCase()), [getPowertypeExtent](../../classes/mdkernel/Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](../../classes/mdkernel/Classifier.html#getRedefinedClassifier()), [getRepresentation](../../classes/mdkernel/Classifier.html#getRepresentation()), [getSubstitution](../../classes/mdkernel/Classifier.html#getSubstitution()), [getTemplateParameter](../../classes/mdkernel/Classifier.html#getTemplateParameter()), [getUMLClass](../../classes/mdkernel/Classifier.html#getUMLClass()), [getUseCase](../../classes/mdkernel/Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](../../classes/mdkernel/Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](../../classes/mdkernel/Classifier.html#hasAttribute()), [hasCollaborationUse](../../classes/mdkernel/Classifier.html#hasCollaborationUse()), [hasFeature](../../classes/mdkernel/Classifier.html#hasFeature()), [hasGeneral](../../classes/mdkernel/Classifier.html#hasGeneral()), [hasGeneralization](../../classes/mdkernel/Classifier.html#hasGeneralization()), [hasInheritedMember](../../classes/mdkernel/Classifier.html#hasInheritedMember()), [hasOwnedUseCase](../../classes/mdkernel/Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](../../classes/mdkernel/Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()), [hasSubstitution](../../classes/mdkernel/Classifier.html#hasSubstitution()), [hasUseCase](../../classes/mdkernel/Classifier.html#hasUseCase()), [isFinalSpecialization](../../classes/mdkernel/Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setFinalSpecialization](../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)
`[getOwnedPort](../../compositestructures/mdports/EncapsulatedClassifier.html#getOwnedPort()), [hasOwnedPort](../../compositestructures/mdports/EncapsulatedClassifier.html#hasOwnedPort())`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)
`[getOwnedConnector](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedConnector()), [getPart](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getPart()), [getRole](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getRole()), [hasOwnedAttribute](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedAttribute()), [hasOwnedConnector](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedConnector()), [hasPart](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasPart()), [hasRole](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasRole())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](../../classes/mdkernel/Type.html)
`[get_associationOfEndType](../../classes/mdkernel/Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](../../classes/mdkernel/Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](../../classes/mdkernel/Type.html#get_operationOfRaisedException()), [get_typedElementOfType](../../classes/mdkernel/Type.html#get_typedElementOfType()), [getPackage](../../classes/mdkernel/Type.html#getPackage()), [has_associationOfEndType](../../classes/mdkernel/Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](../../classes/mdkernel/Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](../../classes/mdkernel/Type.html#has_operationOfRaisedException()), [has_typedElementOfType](../../classes/mdkernel/Type.html#has_typedElementOfType()), [setPackage](../../classes/mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
isIndirectlyInstantiated
boolean isIndirectlyInstantiated()
Returns the value of the '***Indirectly Instantiated***' attribute.
 The default value is `"true"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, the Component is defined at design-time, but at run-time (or execution-time) an object specified by the Component does not exist, that is, the Component
 is instantiated indirectly, through the instantiation of its realizing Classifiers or parts.
 end-model-doc
Returns:
the value of the '*Indirectly Instantiated*' attribute.
See Also:
[`setIndirectlyInstantiated(boolean)`](#setIndirectlyInstantiated(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getComponent_IndirectlyInstantiated()`
Model:
default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setIndirectlyInstantiated
void setIndirectlyInstantiated(boolean value)
Sets the value of the '[`*Indirectly Instantiated*`](#isIndirectlyInstantiated())'
 attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Indirectly Instantiated*' attribute.
See Also:
[`isIndirectlyInstantiated()`](#isIndirectlyInstantiated())
Generated:
getRealization
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ComponentRealization](ComponentRealization.html)> getRealization()
Returns the value of the '***Realization***' containment reference list.
 The list contents are of type [`ComponentRealization`](ComponentRealization.html).
 It is bidirectional and its opposite is
 '[`*Abstraction*`](ComponentRealization.html#getAbstraction())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of Realizations owned by the Component. Realizations reference the Classifiers of which the Component is an abstraction; i.e., that realize its behavior.
 end-model-doc
Returns:
the value of the '*Realization*' containment reference list.
See Also:
[`UMLPackage.getComponent_Realization()`](../../metadata/UMLPackage.html#getComponent_Realization())
[`ComponentRealization.getAbstraction()`](ComponentRealization.html#getAbstraction())
Model:
opposite="abstraction2" containment="true" resolveProxies="true" ordered="false"
Generated:
getProvided
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)> getProvided()
Returns the value of the '***Provided***' reference list.
 The list contents are of type [`Interface`](../../classes/mdinterfaces/Interface.html).
 It is bidirectional and its opposite is
 '
invalid reference
`*component Of Provided*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Interfaces that the Component exposes to its environment. These Interfaces may be Realized by the Component or any of its realizingClassifiers, or they may
 be the Interfaces that are provided by its public Ports.
 end-model-doc
Returns:
the value of the '*Provided*' reference list.
See Also:
[`UMLPackage.getComponent_Provided()`](../../metadata/UMLPackage.html#getComponent_Provided())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_componentOfProvided`
Model:
opposite="_componentOfProvided" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getPackagedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PackageableElement](../../classes/mdkernel/PackageableElement.html)> getPackagedElement()
Returns the value of the '***Packaged Element***' containment reference list.
 The list contents are of type [`PackageableElement`](../../classes/mdkernel/PackageableElement.html).
 It is bidirectional and its opposite is
 '[`*component Of Packaged Element*`](../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of PackageableElements that a Component owns. In the namespace of a Component, all model elements that are involved in or related to its definition may
 be owned or imported explicitly. These may include e.g., Classes, Interfaces, Components, Packages, UseCases, Dependencies (e.g., mappings), and Artifacts.
 end-model-doc
Returns:
the value of the '*Packaged Element*' containment reference list.
See Also:
[`UMLPackage.getComponent_PackagedElement()`](../../metadata/UMLPackage.html#getComponent_PackagedElement())
[`PackageableElement.get_componentOfPackagedElement()`](../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement())
Model:
opposite="_componentOfPackagedElement" containment="true" resolveProxies="true" ordered="false"
Generated:
getRequired
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)> getRequired()
Returns the value of the '***Required***' reference list.
 The list contents are of type [`Interface`](../../classes/mdinterfaces/Interface.html).
 It is bidirectional and its opposite is
 '
invalid reference
`*component Of Required*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Interfaces that the Component requires from other Components in its environment in order to be able to offer its full set of provided functionality. These
 Interfaces may be used by the Component or any of its realizingClassifiers, or they may be the Interfaces that are required by its public Ports.
 end-model-doc
Returns:
the value of the '*Required*' reference list.
See Also:
[`UMLPackage.getComponent_Required()`](../../metadata/UMLPackage.html#getComponent_Required())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_componentOfRequired`
Model:
opposite="_componentOfRequired" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
hasRealization
boolean hasRealization()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasProvided
boolean hasProvided()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPackagedElement
boolean hasPackagedElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRequired
boolean hasRequired()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents</a></div>
<h1 class="title" title="Interface Component">Interface Component</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Component</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Component</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Component represents a modular part of a system that encapsulates its contents and whose manifestation is replaceable within its environment.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isIndirectlyInstantiated()"><code><em>Indirectly Instantiated</em></code></a></li>
<li><a href="#getPackagedElement()"><code><em>Packaged Element</em></code></a></li>
<li><a href="#getRealization()"><code><em>Realization</em></code></a></li>
<li><a href="#getRequired()"><code><em>Required</em></code></a></li>
<li><a href="#getProvided()"><code><em>Provided</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getComponent()"><code>UMLPackage.getComponent()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='components.mdbasiccomponents'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagedElement()">getPackagedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Packaged Element</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProvided()">getProvided</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Provided</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRealization()">getRealization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Realization</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRequired()">getRequired</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Required</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPackagedElement()">hasPackagedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasProvided()">hasProvided</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRealization()">hasRealization</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRequired()">hasRequired</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isIndirectlyInstantiated()">isIndirectlyInstantiated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Indirectly Instantiated</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIndirectlyInstantiated(boolean)">setIndirectlyInstantiated</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isIndirectlyInstantiated()"><code><em>Indirectly Instantiated</em></code></a>'
 attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.<a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></h3>
<code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getClassifierBehavior()">getClassifierBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()">getInterfaceRealization</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getOwnedBehavior()">getOwnedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasInterfaceRealization()">hasInterfaceRealization</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasOwnedBehavior()">hasOwnedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setClassifierBehavior</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></h3>
<code><a href="../../classes/mdkernel/Class.html#getExtension()">getExtension</a>, <a href="../../classes/mdkernel/Class.html#getNestedClassifier()">getNestedClassifier</a>, <a href="../../classes/mdkernel/Class.html#getOwnedAttribute()">getOwnedAttribute</a>, <a href="../../classes/mdkernel/Class.html#getOwnedOperation()">getOwnedOperation</a>, <a href="../../classes/mdkernel/Class.html#getOwnedReception()">getOwnedReception</a>, <a href="../../classes/mdkernel/Class.html#getSuperClass()">getSuperClass</a>, <a href="../../classes/mdkernel/Class.html#hasExtension()">hasExtension</a>, <a href="../../classes/mdkernel/Class.html#hasNestedClassifier()">hasNestedClassifier</a>, <a href="../../classes/mdkernel/Class.html#hasOwnedOperation()">hasOwnedOperation</a>, <a href="../../classes/mdkernel/Class.html#hasOwnedReception()">hasOwnedReception</a>, <a href="../../classes/mdkernel/Class.html#hasSuperClass()">hasSuperClass</a>, <a href="../../classes/mdkernel/Class.html#isAbstract()">isAbstract</a>, <a href="../../classes/mdkernel/Class.html#isActive()">isActive</a>, <a href="../../classes/mdkernel/Class.html#setAbstract(boolean)">setAbstract</a>, <a href="../../classes/mdkernel/Class.html#setActive(boolean)">setActive</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#getAttribute()">getAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#getFeature()">getFeature</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneral()">getGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneralization()">getGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#getRepresentation()">getRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#getSubstitution()">getSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#getUMLClass()">getUMLClass</a>, <a href="../../classes/mdkernel/Classifier.html#getUseCase()">getUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#hasAttribute()">hasAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#hasFeature()">hasFeature</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneral()">hasGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#hasUseCase()">hasUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.<a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></h3>
<code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html#getOwnedPort()">getOwnedPort</a>, <a href="../../compositestructures/mdports/EncapsulatedClassifier.html#hasOwnedPort()">hasOwnedPort</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></h3>
<code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedConnector()">getOwnedConnector</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getPart()">getPart</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getRole()">getRole</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedAttribute()">hasOwnedAttribute</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedConnector()">hasOwnedConnector</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasPart()">hasPart</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasRole()">hasRole</a></code></div>
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
<section class="detail" id="isIndirectlyInstantiated()">
<h3>isIndirectlyInstantiated</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isIndirectlyInstantiated</span>()</div>
<div class="block">Returns the value of the '<em><b>Indirectly Instantiated</b></em>' attribute.
 The default value is <code>"true"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, the Component is defined at design-time, but at run-time (or execution-time) an object specified by the Component does not exist, that is, the Component
 is instantiated indirectly, through the instantiation of its realizing Classifiers or parts.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Indirectly Instantiated</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setIndirectlyInstantiated(boolean)"><code>setIndirectlyInstantiated(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getComponent_IndirectlyInstantiated()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndirectlyInstantiated(boolean)">
<h3>setIndirectlyInstantiated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIndirectlyInstantiated</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isIndirectlyInstantiated()"><code><em>Indirectly Instantiated</em></code></a>'
 attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Indirectly Instantiated</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isIndirectlyInstantiated()"><code>isIndirectlyInstantiated()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealization()">
<h3>getRealization</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a>&gt;</span> <span class="element-name">getRealization</span>()</div>
<div class="block">Returns the value of the '<em><b>Realization</b></em>' containment reference list.
 The list contents are of type <a href="ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ComponentRealization</code></a>.
 It is bidirectional and its opposite is
 '<a href="ComponentRealization.html#getAbstraction()"><code><em>Abstraction</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of Realizations owned by the Component. Realizations reference the Classifiers of which the Component is an abstraction; i.e., that realize its behavior.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Realization</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getComponent_Realization()"><code>UMLPackage.getComponent_Realization()</code></a></li>
<li><a href="ComponentRealization.html#getAbstraction()"><code>ComponentRealization.getAbstraction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="abstraction2" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProvided()">
<h3>getProvided</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getProvided</span>()</div>
<div class="block">Returns the value of the '<em><b>Provided</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.
 It is bidirectional and its opposite is
 '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>component Of Provided</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Interfaces that the Component exposes to its environment. These Interfaces may be Realized by the Component or any of its realizingClassifiers, or they may
 be the Interfaces that are provided by its public Ports.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Provided</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getComponent_Provided()"><code>UMLPackage.getComponent_Provided()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_componentOfProvided</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_componentOfProvided" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackagedElement()">
<h3>getPackagedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>&gt;</span> <span class="element-name">getPackagedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Packaged Element</b></em>' containment reference list.
 The list contents are of type <a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()"><code><em>component Of Packaged Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of PackageableElements that a Component owns. In the namespace of a Component, all model elements that are involved in or related to its definition may
 be owned or imported explicitly. These may include e.g., Classes, Interfaces, Components, Packages, UseCases, Dependencies (e.g., mappings), and Artifacts.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Packaged Element</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getComponent_PackagedElement()"><code>UMLPackage.getComponent_PackagedElement()</code></a></li>
<li><a href="../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()"><code>PackageableElement.get_componentOfPackagedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_componentOfPackagedElement" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequired()">
<h3>getRequired</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getRequired</span>()</div>
<div class="block">Returns the value of the '<em><b>Required</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.
 It is bidirectional and its opposite is
 '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>component Of Required</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Interfaces that the Component requires from other Components in its environment in order to be able to offer its full set of provided functionality. These
 Interfaces may be used by the Component or any of its realizingClassifiers, or they may be the Interfaces that are required by its public Ports.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Required</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getComponent_Required()"><code>UMLPackage.getComponent_Required()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_componentOfRequired</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_componentOfRequired" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRealization()">
<h3>hasRealization</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRealization</span>()
                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasProvided()">
<h3>hasProvided</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasProvided</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPackagedElement()">
<h3>hasPackagedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPackagedElement</span>()
                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRequired()">
<h3>hasRequired</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRequired</span>()
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
