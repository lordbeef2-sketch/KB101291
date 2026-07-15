# JAVA OPENAPI: Class (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Class.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Class.html`
- source_sha256: `7af0439700a2104cf83cd611cb9775e5c9da2158b77f43e178e9380135d82d8c`
- captured_utc: `2026-07-14T16:46:28.365176+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Class

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[Classifier](Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](Type.html)`

All Known Subinterfaces:
`[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`

public interfaceClassextends [EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html), [BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)

begin-user-doc 
 A representation of the model object '***Class***'.
 end-user-doc 
begin-model-doc 
 A Class classifies a set of objects and specifies the features that characterize the structure and behavior of those objects. A Class may have an internal
 structure and Ports.
 end-model-doc 
The following features are supported:
 [`*Owned Reception*`](#getOwnedReception())
[`*Owned Operation*`](#getOwnedOperation())
[`*Extension*`](#getExtension())
[`*Active*`](#isActive())
[`*Nested Classifier*`](#getNestedClassifier())
[`*Super Class*`](#getSuperClass())

See Also:
[`UMLPackage.getClass_()`](../../metadata/UMLPackage.html#getClass_())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Extension](../../mdprofiles/Extension.html)>`
`[getExtension](#getExtension())()`
Returns the value of the '***Extension***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](Classifier.html)>`
`[getNestedClassifier](#getNestedClassifier())()`
Returns the value of the '***Nested Classifier***' containment reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getOwnedAttribute](#getOwnedAttribute())()`
Returns the value of the '***Owned Attribute***' containment reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Operation](Operation.html)>`
`[getOwnedOperation](#getOwnedOperation())()`
Returns the value of the '***Owned Operation***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Reception](../../commonbehaviors/mdcommunications/Reception.html)>`
`[getOwnedReception](#getOwnedReception())()`
Returns the value of the '***Owned Reception***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](Class.html)>`
`[getSuperClass](#getSuperClass())()`
Returns the value of the '***Super Class***' reference list.
`boolean`
`[hasExtension](#hasExtension())()`

`boolean`
`[hasNestedClassifier](#hasNestedClassifier())()`

`boolean`
`[hasOwnedOperation](#hasOwnedOperation())()`

`boolean`
`[hasOwnedReception](#hasOwnedReception())()`

`boolean`
`[hasSuperClass](#hasSuperClass())()`

`boolean`
`[isAbstract](#isAbstract())()`
Returns the value of the '***Abstract***' attribute.
`boolean`
`[isActive](#isActive())()`
Returns the value of the '***Active***' attribute.
`void`
`[setAbstract](#setAbstract(boolean))(boolean value)`
Sets the value of the '[`*Abstract*`](#isAbstract())' attribute.
`void`
`[setActive](#setActive(boolean))(boolean value)`
Sets the value of the '[`*Active*`](#isActive())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)
`[getClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getClassifierBehavior()), [getInterfaceRealization](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()), [getOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getOwnedBehavior()), [hasInterfaceRealization](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasInterfaceRealization()), [hasOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasOwnedBehavior()), [setClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](Classifier.html)
`[get_classifierOfRedefinedClassifier](Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](Classifier.html#getAttribute()), [getCollaborationUse](Classifier.html#getCollaborationUse()), [getFeature](Classifier.html#getFeature()), [getGeneral](Classifier.html#getGeneral()), [getGeneralization](Classifier.html#getGeneralization()), [getInheritedMember](Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](Classifier.html#getOwnedUseCase()), [getPowertypeExtent](Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](Classifier.html#getRedefinedClassifier()), [getRepresentation](Classifier.html#getRepresentation()), [getSubstitution](Classifier.html#getSubstitution()), [getTemplateParameter](Classifier.html#getTemplateParameter()), [getUMLClass](Classifier.html#getUMLClass()), [getUseCase](Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](Classifier.html#hasAttribute()), [hasCollaborationUse](Classifier.html#hasCollaborationUse()), [hasFeature](Classifier.html#hasFeature()), [hasGeneral](Classifier.html#hasGeneral()), [hasGeneralization](Classifier.html#hasGeneralization()), [hasInheritedMember](Classifier.html#hasInheritedMember()), [hasOwnedUseCase](Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](Classifier.html#hasRedefinedClassifier()), [hasSubstitution](Classifier.html#hasSubstitution()), [hasUseCase](Classifier.html#hasUseCase()), [isFinalSpecialization](Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setFinalSpecialization](Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)
`[getOwnedConnector](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedConnector()), [getPart](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getPart()), [getRole](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getRole()), [hasOwnedAttribute](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedAttribute()), [hasOwnedConnector](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedConnector()), [hasPart](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasPart()), [hasRole](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasRole())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](Type.html)
`[get_associationOfEndType](Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](Type.html#get_operationOfRaisedException()), [get_typedElementOfType](Type.html#get_typedElementOfType()), [getPackage](Type.html#getPackage()), [has_associationOfEndType](Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](Type.html#has_operationOfRaisedException()), [has_typedElementOfType](Type.html#has_typedElementOfType()), [setPackage](Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
getExtension
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Extension](../../mdprofiles/Extension.html)> getExtension()
Returns the value of the '***Extension***' reference list.
 The list contents are of type [`Extension`](../../mdprofiles/Extension.html).
 It is bidirectional and its opposite is '[`*Metaclass*`](../../mdprofiles/Extension.html#getMetaclass())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This property is used when the Class is acting as a metaclass. It references the Extensions that specify additional properties of the metaclass. The property is
 derived from the Extensions whose memberEnds are typed by the Class.
 end-model-doc
Returns:
the value of the '*Extension*' reference list.
See Also:
[`UMLPackage.getClass_Extension()`](../../metadata/UMLPackage.html#getClass_Extension())
[`Extension.getMetaclass()`](../../mdprofiles/Extension.html#getMetaclass())
Model:
opposite="metaclass" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isActive
boolean isActive()
Returns the value of the '***Active***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Determines whether an object specified by this Class is active or not. If true, then the owning Class is referred to as an active Class. If false, then such a
 Class is referred to as a passive Class.
 end-model-doc
Returns:
the value of the '*Active*' attribute.
See Also:
[`setActive(boolean)`](#setActive(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getClass_Active()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setActive
void setActive(boolean value)
Sets the value of the '[`*Active*`](#isActive())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Active*' attribute.
See Also:
[`isActive()`](#isActive())
Generated:
getNestedClassifier
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](Classifier.html)> getNestedClassifier()
Returns the value of the '***Nested Classifier***' containment reference list.
 The list contents are of type [`Classifier`](Classifier.html).
 It is bidirectional and its opposite is '[`*UML Class*`](Classifier.html#getUMLClass())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Classifiers owned by the Class that are not ownedBehaviors.
 end-model-doc
Returns:
the value of the '*Nested Classifier*' containment reference list.
See Also:
[`UMLPackage.getClass_NestedClassifier()`](../../metadata/UMLPackage.html#getClass_NestedClassifier())
[`Classifier.getUMLClass()`](Classifier.html#getUMLClass())
Model:
opposite="UMLClass" containment="true" resolveProxies="true"
Generated:
getOwnedOperation
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Operation](Operation.html)> getOwnedOperation()
Returns the value of the '***Owned Operation***' containment reference list.
 The list contents are of type [`Operation`](Operation.html).
 It is bidirectional and its opposite is '[`*UML Class*`](Operation.html#getUMLClass())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Operations owned by the Class.
 end-model-doc
Returns:
the value of the '*Owned Operation*' containment reference list.
See Also:
[`UMLPackage.getClass_OwnedOperation()`](../../metadata/UMLPackage.html#getClass_OwnedOperation())
[`Operation.getUMLClass()`](Operation.html#getUMLClass())
Model:
opposite="UMLClass" containment="true" resolveProxies="true"
Generated:
getSuperClass
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](Class.html)> getSuperClass()
Returns the value of the '***Super Class***' reference list.
 The list contents are of type [`Class`](Class.html).
 It is bidirectional and its opposite is '
invalid reference
`*class Of Super Class*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The superclasses of a Class, derived from its Generalizations.
 end-model-doc
Returns:
the value of the '*Super Class*' reference list.
See Also:
[`UMLPackage.getClass_SuperClass()`](../../metadata/UMLPackage.html#getClass_SuperClass())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class#get_classOfSuperClass`
Model:
opposite="_classOfSuperClass" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getOwnedReception
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Reception](../../commonbehaviors/mdcommunications/Reception.html)> getOwnedReception()
Returns the value of the '***Owned Reception***' containment reference list.
 The list contents are of type [`Reception`](../../commonbehaviors/mdcommunications/Reception.html).
 It is bidirectional and its opposite is
 '[`*class Of Owned Reception*`](../../commonbehaviors/mdcommunications/Reception.html#get_classOfOwnedReception())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Receptions owned by the Class.
 end-model-doc
Returns:
the value of the '*Owned Reception*' containment reference list.
See Also:
[`UMLPackage.getClass_OwnedReception()`](../../metadata/UMLPackage.html#getClass_OwnedReception())
[`Reception.get_classOfOwnedReception()`](../../commonbehaviors/mdcommunications/Reception.html#get_classOfOwnedReception())
Model:
opposite="_classOfOwnedReception" containment="true" resolveProxies="true" ordered="false"
Generated:
getOwnedAttribute
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getOwnedAttribute()
Returns the value of the '***Owned Attribute***' containment reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*UML Class*`](Property.html#getUMLClass())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The attributes (i.e., the Properties) owned by the Class.
 end-model-doc
Specified by:
`[getOwnedAttribute](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedAttribute())` in interface `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`
Returns:
the value of the '*Owned Attribute*' containment reference list.
See Also:
[`UMLPackage.getClass_OwnedAttribute()`](../../metadata/UMLPackage.html#getClass_OwnedAttribute())
[`Property.getUMLClass()`](Property.html#getUMLClass())
Model:
opposite="UMLClass" containment="true" resolveProxies="true"
Generated:
isAbstract
boolean isAbstract()
Returns the value of the '***Abstract***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, the Class does not provide a complete declaration and cannot be instantiated. An abstract Class is typically used as a target of Associations or
 Generalizations.
 end-model-doc
Specified by:
`[isAbstract](Classifier.html#isAbstract())` in interface `[Classifier](Classifier.html)`
Returns:
the value of the '*Abstract*' attribute.
See Also:
[`setAbstract(boolean)`](#setAbstract(boolean))
[`UMLPackage.getClass_Abstract()`](../../metadata/UMLPackage.html#getClass_Abstract())
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setAbstract
void setAbstract(boolean value)
Sets the value of the '[`*Abstract*`](#isAbstract())' attribute.
 begin-user-doc 
 end-user-doc
Specified by:
`[setAbstract](Classifier.html#setAbstract(boolean))` in interface `[Classifier](Classifier.html)`
Parameters:
`value` - the new value of the '*Abstract*' attribute.
See Also:
[`isAbstract()`](#isAbstract())
Generated:
hasExtension
boolean hasExtension()
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
hasOwnedOperation
boolean hasOwnedOperation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasSuperClass
boolean hasSuperClass()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface Class">Interface Class</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Class</span><span class="extends-implements">
extends <a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Class</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Class classifies a set of objects and specifies the features that characterize the structure and behavior of those objects.  A Class may have an internal
 structure and Ports.
 <p>
<!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getOwnedReception()"><code><em>Owned Reception</em></code></a></li>
<li><a href="#getOwnedOperation()"><code><em>Owned Operation</em></code></a></li>
<li><a href="#getExtension()"><code><em>Extension</em></code></a></li>
<li><a href="#isActive()"><code><em>Active</em></code></a></li>
<li><a href="#getNestedClassifier()"><code><em>Nested Classifier</em></code></a></li>
<li><a href="#getSuperClass()"><code><em>Super Class</em></code></a></li>
</ul>
</p></p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getClass_()"><code>UMLPackage.getClass_()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtension()">getExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Extension</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNestedClassifier()">getNestedClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Nested Classifier</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAttribute()">getOwnedAttribute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Attribute</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedOperation()">getOwnedOperation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Operation</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedReception()">getOwnedReception</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Reception</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSuperClass()">getSuperClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Super Class</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasExtension()">hasExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasNestedClassifier()">hasNestedClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedOperation()">hasOwnedOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedReception()">hasOwnedReception</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSuperClass()">hasSuperClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isAbstract()">isAbstract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Abstract</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isActive()">isActive</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Active</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAbstract(boolean)">setAbstract</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isAbstract()"><code><em>Abstract</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setActive(boolean)">setActive</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isActive()"><code><em>Active</em></code></a>' attribute.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="Classifier.html#getAttribute()">getAttribute</a>, <a href="Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="Classifier.html#getFeature()">getFeature</a>, <a href="Classifier.html#getGeneral()">getGeneral</a>, <a href="Classifier.html#getGeneralization()">getGeneralization</a>, <a href="Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="Classifier.html#getRepresentation()">getRepresentation</a>, <a href="Classifier.html#getSubstitution()">getSubstitution</a>, <a href="Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="Classifier.html#getUMLClass()">getUMLClass</a>, <a href="Classifier.html#getUseCase()">getUseCase</a>, <a href="Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="Classifier.html#hasAttribute()">hasAttribute</a>, <a href="Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="Classifier.html#hasFeature()">hasFeature</a>, <a href="Classifier.html#hasGeneral()">hasGeneral</a>, <a href="Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="Classifier.html#hasUseCase()">hasUseCase</a>, <a href="Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></h3>
<code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedConnector()">getOwnedConnector</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getPart()">getPart</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getRole()">getRole</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedAttribute()">hasOwnedAttribute</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedConnector()">hasOwnedConnector</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasPart()">hasPart</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasRole()">hasRole</a></code></div>
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
<section class="detail" id="getExtension()">
<h3>getExtension</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a>&gt;</span> <span class="element-name">getExtension</span>()</div>
<div class="block">Returns the value of the '<em><b>Extension</b></em>' reference list.
 The list contents are of type <a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Extension</code></a>.
 It is bidirectional and its opposite is '<a href="../../mdprofiles/Extension.html#getMetaclass()"><code><em>Metaclass</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This property is used when the Class is acting as a metaclass. It references the Extensions that specify additional properties of the metaclass. The property is
 derived from the Extensions whose memberEnds are typed by the Class.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Extension</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClass_Extension()"><code>UMLPackage.getClass_Extension()</code></a></li>
<li><a href="../../mdprofiles/Extension.html#getMetaclass()"><code>Extension.getMetaclass()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="metaclass" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActive()">
<h3>isActive</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isActive</span>()</div>
<div class="block">Returns the value of the '<em><b>Active</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Determines whether an object specified by this Class is active or not. If true, then the owning Class is referred to as an active Class. If false, then such a
 Class is referred to as a passive Class.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Active</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setActive(boolean)"><code>setActive(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getClass_Active()</code></pre>
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
<section class="detail" id="setActive(boolean)">
<h3>setActive</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setActive</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isActive()"><code><em>Active</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Active</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isActive()"><code>isActive()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedClassifier()">
<h3>getNestedClassifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getNestedClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Nested Classifier</b></em>' containment reference list.
 The list contents are of type <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is '<a href="Classifier.html#getUMLClass()"><code><em>UML Class</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Classifiers owned by the Class that are not ownedBehaviors.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Nested Classifier</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClass_NestedClassifier()"><code>UMLPackage.getClass_NestedClassifier()</code></a></li>
<li><a href="Classifier.html#getUMLClass()"><code>Classifier.getUMLClass()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="UMLClass" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOperation()">
<h3>getOwnedOperation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getOwnedOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Operation</b></em>' containment reference list.
 The list contents are of type <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.
 It is bidirectional and its opposite is '<a href="Operation.html#getUMLClass()"><code><em>UML Class</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Operations owned by the Class.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Operation</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClass_OwnedOperation()"><code>UMLPackage.getClass_OwnedOperation()</code></a></li>
<li><a href="Operation.html#getUMLClass()"><code>Operation.getUMLClass()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="UMLClass" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuperClass()">
<h3>getSuperClass</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a>&gt;</span> <span class="element-name">getSuperClass</span>()</div>
<div class="block">Returns the value of the '<em><b>Super Class</b></em>' reference list.
 The list contents are of type <a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a>.
 It is bidirectional and its opposite is '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>class Of Super Class</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The superclasses of a Class, derived from its Generalizations.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Super Class</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClass_SuperClass()"><code>UMLPackage.getClass_SuperClass()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class#get_classOfSuperClass</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classOfSuperClass" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReception()">
<h3>getOwnedReception</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a>&gt;</span> <span class="element-name">getOwnedReception</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Reception</b></em>' containment reference list.
 The list contents are of type <a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Reception</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdcommunications/Reception.html#get_classOfOwnedReception()"><code><em>class Of Owned Reception</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Receptions owned by the Class.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Reception</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClass_OwnedReception()"><code>UMLPackage.getClass_OwnedReception()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/Reception.html#get_classOfOwnedReception()"><code>Reception.get_classOfOwnedReception()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_classOfOwnedReception" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAttribute()">
<h3>getOwnedAttribute</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getOwnedAttribute</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Attribute</b></em>' containment reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="Property.html#getUMLClass()"><code><em>UML Class</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The attributes (i.e., the Properties) owned by the Class.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedAttribute()">getOwnedAttribute</a></code> in interface <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Attribute</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getClass_OwnedAttribute()"><code>UMLPackage.getClass_OwnedAttribute()</code></a></li>
<li><a href="Property.html#getUMLClass()"><code>Property.getUMLClass()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="UMLClass" containment="true" resolveProxies="true"</dd>
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
 If true, the Class does not provide a complete declaration and cannot be instantiated. An abstract Class is typically used as a target of Associations or
 Generalizations.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Classifier.html#isAbstract()">isAbstract</a></code> in interface <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Abstract</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#setAbstract(boolean)"><code>setAbstract(boolean)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClass_Abstract()"><code>UMLPackage.getClass_Abstract()</code></a></li>
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
<dt>Specified by:</dt>
<dd><code><a href="Classifier.html#setAbstract(boolean)">setAbstract</a></code> in interface <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></dd>
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
<section class="detail" id="hasExtension()">
<h3>hasExtension</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasExtension</span>()
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
<section class="detail" id="hasSuperClass()">
<h3>hasSuperClass</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSuperClass</span>()
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
