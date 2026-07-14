# JAVA OPENAPI: Profile (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/mdprofiles/Profile.html
- source_path: `com/nomagic/uml2/ext/magicdraw/mdprofiles/Profile.html`
- source_sha256: `4142a5febd0d8f591e0f198672b4fba64446522ef00093ef3351727acc5804a6`
- captured_utc: `2026-07-14T16:53:13.346643+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.mdprofiles](package-summary.html)

## Interface Profile

All Superinterfaces:
`[BaseElement](../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../base/ModelObject.html)`, `[NamedElement](../classes/mdkernel/NamedElement.html)`, `[Namespace](../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Package](../classes/mdkernel/Package.html)`, `[PackageableElement](../classes/mdkernel/PackageableElement.html)`, `[ParameterableElement](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TemplateableElement](../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`

public interfaceProfileextends [Package](../classes/mdkernel/Package.html)

begin-user-doc 
 A representation of the model object '***Profile***'.
 end-user-doc 
begin-model-doc 
 A profile defines limited extensions to a reference metamodel with the purpose of adapting the metamodel to a specific platform or domain.
 end-model-doc 
The following features are supported:
 [`*profile Application Of Applied Profile*`](#get_profileApplicationOfAppliedProfile())
[`*Metamodel Reference*`](#getMetamodelReference())
[`*Metaclass Reference*`](#getMetaclassReference())

See Also:
[`UMLPackage.getProfile()`](../metadata/UMLPackage.html#getProfile())
Model:
annotation="MOF package='mdprofiles'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProfileApplication](ProfileApplication.html)>`
`[get_profileApplicationOfAppliedProfile](#get_profileApplicationOfAppliedProfile())()`
Returns the value of the '***profile Application Of Applied Profile***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementImport](../classes/mdkernel/ElementImport.html)>`
`[getMetaclassReference](#getMetaclassReference())()`
Returns the value of the '***Metaclass Reference***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PackageImport](../classes/mdkernel/PackageImport.html)>`
`[getMetamodelReference](#getMetamodelReference())()`
Returns the value of the '***Metamodel Reference***' reference list.
`boolean`
`[has_profileApplicationOfAppliedProfile](#has_profileApplicationOfAppliedProfile())()`

`boolean`
`[hasMetaclassReference](#hasMetaclassReference())()`

`boolean`
`[hasMetamodelReference](#hasMetamodelReference())()`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../base/ModelObject.html)
`[get_representationText](../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../classes/mdkernel/NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../classes/mdkernel/Namespace.html)
`[getElementImport](../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../classes/mdkernel/Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Package](../classes/mdkernel/Package.html)
`[get_packageImportOfImportedPackage](../classes/mdkernel/Package.html#get_packageImportOfImportedPackage()), [get_packageMergeOfMergedPackage](../classes/mdkernel/Package.html#get_packageMergeOfMergedPackage()), [getNestedPackage](../classes/mdkernel/Package.html#getNestedPackage()), [getNestingPackage](../classes/mdkernel/Package.html#getNestingPackage()), [getOwnedStereotype](../classes/mdkernel/Package.html#getOwnedStereotype()), [getOwnedType](../classes/mdkernel/Package.html#getOwnedType()), [getPackagedElement](../classes/mdkernel/Package.html#getPackagedElement()), [getPackageMerge](../classes/mdkernel/Package.html#getPackageMerge()), [getProfileApplication](../classes/mdkernel/Package.html#getProfileApplication()), [getURI](../classes/mdkernel/Package.html#getURI()), [has_packageImportOfImportedPackage](../classes/mdkernel/Package.html#has_packageImportOfImportedPackage()), [has_packageMergeOfMergedPackage](../classes/mdkernel/Package.html#has_packageMergeOfMergedPackage()), [hasNestedPackage](../classes/mdkernel/Package.html#hasNestedPackage()), [hasOwnedStereotype](../classes/mdkernel/Package.html#hasOwnedStereotype()), [hasOwnedType](../classes/mdkernel/Package.html#hasOwnedType()), [hasPackagedElement](../classes/mdkernel/Package.html#hasPackagedElement()), [hasPackageMerge](../classes/mdkernel/Package.html#hasPackageMerge()), [hasProfileApplication](../classes/mdkernel/Package.html#hasProfileApplication()), [setURI](../classes/mdkernel/Package.html#setURI(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](../classes/mdkernel/PackageableElement.html)
`[get_componentOfPackagedElement](../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](../classes/mdkernel/PackageableElement.html#getOwningPackage()), [getVisibility](../classes/mdkernel/PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [getTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()), [has_templateParameterOfDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getOwnedTemplateSignature](../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getOwnedTemplateSignature()), [getTemplateBinding](../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`

============ METHOD DETAIL ========== 
Method Details
get_profileApplicationOfAppliedProfile
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProfileApplication](ProfileApplication.html)> get_profileApplicationOfAppliedProfile()
Returns the value of the '***profile Application Of Applied Profile***' reference list.
 The list contents are of type [`ProfileApplication`](ProfileApplication.html).
 It is bidirectional and its opposite is '[`*Applied Profile*`](ProfileApplication.html#getAppliedProfile())'.
 begin-user-doc 
If the meaning of the '*profile Application Of Applied Profile*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*profile Application Of Applied Profile*' reference list.
See Also:
[`UMLPackage.getProfile__profileApplicationOfAppliedProfile()`](../metadata/UMLPackage.html#getProfile__profileApplicationOfAppliedProfile())
[`ProfileApplication.getAppliedProfile()`](ProfileApplication.html#getAppliedProfile())
Model:
opposite="appliedProfile" ordered="false"
Generated:
getMetamodelReference
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PackageImport](../classes/mdkernel/PackageImport.html)> getMetamodelReference()
Returns the value of the '***Metamodel Reference***' reference list.
 The list contents are of type [`PackageImport`](../classes/mdkernel/PackageImport.html).
 It is bidirectional and its opposite is
 '[`*profile Of Metamodel Reference*`](../classes/mdkernel/PackageImport.html#get_profileOfMetamodelReference())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References a package containing (directly or indirectly) metaclasses that may be extended.
 end-model-doc
Returns:
the value of the '*Metamodel Reference*' reference list.
See Also:
[`UMLPackage.getProfile_MetamodelReference()`](../metadata/UMLPackage.html#getProfile_MetamodelReference())
[`PackageImport.get_profileOfMetamodelReference()`](../classes/mdkernel/PackageImport.html#get_profileOfMetamodelReference())
Model:
opposite="_profileOfMetamodelReference" ordered="false"
Generated:
getMetaclassReference
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementImport](../classes/mdkernel/ElementImport.html)> getMetaclassReference()
Returns the value of the '***Metaclass Reference***' reference list.
 The list contents are of type [`ElementImport`](../classes/mdkernel/ElementImport.html).
 It is bidirectional and its opposite is
 '[`*profile Of Metaclass Reference*`](../classes/mdkernel/ElementImport.html#get_profileOfMetaclassReference())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References a metaclass that may be extended.
 end-model-doc
Returns:
the value of the '*Metaclass Reference*' reference list.
See Also:
[`UMLPackage.getProfile_MetaclassReference()`](../metadata/UMLPackage.html#getProfile_MetaclassReference())
[`ElementImport.get_profileOfMetaclassReference()`](../classes/mdkernel/ElementImport.html#get_profileOfMetaclassReference())
Model:
opposite="_profileOfMetaclassReference" ordered="false"
Generated:
has_profileApplicationOfAppliedProfile
boolean has_profileApplicationOfAppliedProfile()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasMetamodelReference
boolean hasMetamodelReference()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasMetaclassReference
boolean hasMetaclassReference()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.mdprofiles</a></div>
<h1 class="title" title="Interface Profile">Interface Profile</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code>, <code><a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Profile</span><span class="extends-implements">
extends <a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Profile</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A profile defines limited extensions to a reference metamodel with the purpose of adapting the metamodel to a specific platform or domain.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_profileApplicationOfAppliedProfile()"><code><em>profile Application Of Applied Profile</em></code></a></li>
<li><a href="#getMetamodelReference()"><code><em>Metamodel Reference</em></code></a></li>
<li><a href="#getMetaclassReference()"><code><em>Metaclass Reference</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../metadata/UMLPackage.html#getProfile()"><code>UMLPackage.getProfile()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='mdprofiles'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_profileApplicationOfAppliedProfile()">get_profileApplicationOfAppliedProfile</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>profile Application Of Applied Profile</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMetaclassReference()">getMetaclassReference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Metaclass Reference</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMetamodelReference()">getMetamodelReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Metamodel Reference</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_profileApplicationOfAppliedProfile()">has_profileApplicationOfAppliedProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasMetaclassReference()">hasMetaclassReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasMetamodelReference()">hasMetamodelReference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></h3>
<code><a href="../classes/mdkernel/Package.html#get_packageImportOfImportedPackage()">get_packageImportOfImportedPackage</a>, <a href="../classes/mdkernel/Package.html#get_packageMergeOfMergedPackage()">get_packageMergeOfMergedPackage</a>, <a href="../classes/mdkernel/Package.html#getNestedPackage()">getNestedPackage</a>, <a href="../classes/mdkernel/Package.html#getNestingPackage()">getNestingPackage</a>, <a href="../classes/mdkernel/Package.html#getOwnedStereotype()">getOwnedStereotype</a>, <a href="../classes/mdkernel/Package.html#getOwnedType()">getOwnedType</a>, <a href="../classes/mdkernel/Package.html#getPackagedElement()">getPackagedElement</a>, <a href="../classes/mdkernel/Package.html#getPackageMerge()">getPackageMerge</a>, <a href="../classes/mdkernel/Package.html#getProfileApplication()">getProfileApplication</a>, <a href="../classes/mdkernel/Package.html#getURI()">getURI</a>, <a href="../classes/mdkernel/Package.html#has_packageImportOfImportedPackage()">has_packageImportOfImportedPackage</a>, <a href="../classes/mdkernel/Package.html#has_packageMergeOfMergedPackage()">has_packageMergeOfMergedPackage</a>, <a href="../classes/mdkernel/Package.html#hasNestedPackage()">hasNestedPackage</a>, <a href="../classes/mdkernel/Package.html#hasOwnedStereotype()">hasOwnedStereotype</a>, <a href="../classes/mdkernel/Package.html#hasOwnedType()">hasOwnedType</a>, <a href="../classes/mdkernel/Package.html#hasPackagedElement()">hasPackagedElement</a>, <a href="../classes/mdkernel/Package.html#hasPackageMerge()">hasPackageMerge</a>, <a href="../classes/mdkernel/Package.html#hasProfileApplication()">hasProfileApplication</a>, <a href="../classes/mdkernel/Package.html#setURI(java.lang.String)">setURI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="../classes/mdkernel/PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="../classes/mdkernel/PackageableElement.html#getVisibility()">getVisibility</a>, <a href="../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></h3>
<code><a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()">getTemplateBinding</a>, <a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()">hasTemplateBinding</a>, <a href="../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">setOwnedTemplateSignature</a></code></div>
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
<section class="detail" id="get_profileApplicationOfAppliedProfile()">
<h3>get_profileApplicationOfAppliedProfile</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ProfileApplication</a>&gt;</span> <span class="element-name">get_profileApplicationOfAppliedProfile</span>()</div>
<div class="block">Returns the value of the '<em><b>profile Application Of Applied Profile</b></em>' reference list.
 The list contents are of type <a href="ProfileApplication.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>ProfileApplication</code></a>.
 It is bidirectional and its opposite is '<a href="ProfileApplication.html#getAppliedProfile()"><code><em>Applied Profile</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>profile Application Of Applied Profile</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>profile Application Of Applied Profile</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../metadata/UMLPackage.html#getProfile__profileApplicationOfAppliedProfile()"><code>UMLPackage.getProfile__profileApplicationOfAppliedProfile()</code></a></li>
<li><a href="ProfileApplication.html#getAppliedProfile()"><code>ProfileApplication.getAppliedProfile()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="appliedProfile" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetamodelReference()">
<h3>getMetamodelReference</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a>&gt;</span> <span class="element-name">getMetamodelReference</span>()</div>
<div class="block">Returns the value of the '<em><b>Metamodel Reference</b></em>' reference list.
 The list contents are of type <a href="../classes/mdkernel/PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a>.
 It is bidirectional and its opposite is
 '<a href="../classes/mdkernel/PackageImport.html#get_profileOfMetamodelReference()"><code><em>profile Of Metamodel Reference</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References a package containing (directly or indirectly) metaclasses that may be extended.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Metamodel Reference</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../metadata/UMLPackage.html#getProfile_MetamodelReference()"><code>UMLPackage.getProfile_MetamodelReference()</code></a></li>
<li><a href="../classes/mdkernel/PackageImport.html#get_profileOfMetamodelReference()"><code>PackageImport.get_profileOfMetamodelReference()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_profileOfMetamodelReference" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaclassReference()">
<h3>getMetaclassReference</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a>&gt;</span> <span class="element-name">getMetaclassReference</span>()</div>
<div class="block">Returns the value of the '<em><b>Metaclass Reference</b></em>' reference list.
 The list contents are of type <a href="../classes/mdkernel/ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a>.
 It is bidirectional and its opposite is
 '<a href="../classes/mdkernel/ElementImport.html#get_profileOfMetaclassReference()"><code><em>profile Of Metaclass Reference</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References a metaclass that may be extended.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Metaclass Reference</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../metadata/UMLPackage.html#getProfile_MetaclassReference()"><code>UMLPackage.getProfile_MetaclassReference()</code></a></li>
<li><a href="../classes/mdkernel/ElementImport.html#get_profileOfMetaclassReference()"><code>ElementImport.get_profileOfMetaclassReference()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_profileOfMetaclassReference" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_profileApplicationOfAppliedProfile()">
<h3>has_profileApplicationOfAppliedProfile</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_profileApplicationOfAppliedProfile</span>()
                                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasMetamodelReference()">
<h3>hasMetamodelReference</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasMetamodelReference</span>()
                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasMetaclassReference()">
<h3>hasMetaclassReference</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasMetaclassReference</span>()
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
