# JAVA OPENAPI: Dependency (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mddependencies/Dependency.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mddependencies/Dependency.html`
- source_sha256: `f6161559b1d6851bd92741499e6c1665a6e842f6c5aa14dd04ab6bf1a94f6fb0`
- captured_utc: `2026-07-14T16:52:49.667376+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mddependencies](package-summary.html)

## Interface Dependency

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[DirectedRelationship](../mdkernel/DirectedRelationship.html)`, `[Element](../mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Relationship](../mdkernel/Relationship.html)`

All Known Subinterfaces:
`[Abstraction](Abstraction.html)`, `[ComponentRealization](../../components/mdbasiccomponents/ComponentRealization.html)`, `[Deployment](../../deployments/mdnodes/Deployment.html)`, `[InterfaceRealization](../mdinterfaces/InterfaceRealization.html)`, `[Manifestation](../../deployments/mdartifacts/Manifestation.html)`, `[Realization](Realization.html)`, `[Substitution](Substitution.html)`, `[Usage](Usage.html)`

public interfaceDependencyextends [PackageableElement](../mdkernel/PackageableElement.html), [DirectedRelationship](../mdkernel/DirectedRelationship.html)

begin-user-doc 
 A representation of the model object '***Dependency***'.
 end-user-doc 
begin-model-doc 
 A Dependency is a Relationship that signifies that a single model Element or a set of model Elements requires other model Elements for their specification or
 implementation. This means that the complete semantics of the client Element(s) are either semantically or structurally dependent on the definition of the supplier
 Element(s).
 end-model-doc 
The following features are supported:
 [`*Client*`](#getClient())
[`*Supplier*`](#getSupplier())
[`*collaboration Use Of Role Binding*`](#get_collaborationUseOfRoleBinding())

See Also:
[`UMLPackage.getDependency()`](../../metadata/UMLPackage.html#getDependency())
Model:
annotation="MOF package='classes.mddependencies'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html)`
`[get_collaborationUseOfRoleBinding](#get_collaborationUseOfRoleBinding())()`
Returns the value of the '***collaboration Use Of Role Binding***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[NamedElement](../mdkernel/NamedElement.html)>`
`[getClient](#getClient())()`
Returns the value of the '***Client***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[NamedElement](../mdkernel/NamedElement.html)>`
`[getSupplier](#getSupplier())()`
Returns the value of the '***Supplier***' reference list.
`boolean`
`[hasClient](#hasClient())()`

`boolean`
`[hasSupplier](#hasSupplier())()`

`void`
`[set_collaborationUseOfRoleBinding](#set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse))([CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html) value)`
Sets the value of the
 '[`*collaboration Use Of Role Binding*`](#get_collaborationUseOfRoleBinding())' container
 reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[DirectedRelationship](../mdkernel/DirectedRelationship.html)
`[getSource](../mdkernel/DirectedRelationship.html#getSource()), [getTarget](../mdkernel/DirectedRelationship.html#getTarget()), [hasSource](../mdkernel/DirectedRelationship.html#hasSource()), [hasTarget](../mdkernel/DirectedRelationship.html#hasTarget())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../mdkernel/Element.html#getOwnedElement()), [getOwner](../mdkernel/Element.html#getOwner()), [getSyncElement](../mdkernel/Element.html#getSyncElement()), [getTaggedValue](../mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../mdkernel/Element.html#hasTaggedValue()), [setOwner](../mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../mdkernel/NamedElement.html#getClientDependency()), [getName](../mdkernel/NamedElement.html#getName()), [getNameExpression](../mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../mdkernel/NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](../mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](../mdkernel/PackageableElement.html)
`[get_componentOfPackagedElement](../mdkernel/PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](../mdkernel/PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](../mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](../mdkernel/PackageableElement.html#getOwningPackage()), [getVisibility](../mdkernel/PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](../mdkernel/PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](../mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](../mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](../mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](../mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [getTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Relationship](../mdkernel/Relationship.html)
`[get_abstraction](../mdkernel/Relationship.html#get_abstraction()), [getRelatedElement](../mdkernel/Relationship.html#getRelatedElement()), [has_abstraction](../mdkernel/Relationship.html#has_abstraction()), [hasRelatedElement](../mdkernel/Relationship.html#hasRelatedElement())`

============ METHOD DETAIL ========== 
Method Details
get_collaborationUseOfRoleBinding
@CheckForNull[CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html) get_collaborationUseOfRoleBinding()
Returns the value of the '***collaboration Use Of Role Binding***' container reference.
 It is bidirectional and its opposite is
 '[`*Role Binding*`](../../compositestructures/mdcollaborations/CollaborationUse.html#getRoleBinding())'.
 begin-user-doc 
If the meaning of the '*collaboration Use Of Role Binding*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*collaboration Use Of Role Binding*' container reference.
See Also:
[`set_collaborationUseOfRoleBinding(CollaborationUse)`](#set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse))
[`UMLPackage.getDependency__collaborationUseOfRoleBinding()`](../../metadata/UMLPackage.html#getDependency__collaborationUseOfRoleBinding())
[`CollaborationUse.getRoleBinding()`](../../compositestructures/mdcollaborations/CollaborationUse.html#getRoleBinding())
Model:
opposite="roleBinding" transient="false" ordered="false"
Generated:
set_collaborationUseOfRoleBinding
void set_collaborationUseOfRoleBinding(@CheckForNull
 [CollaborationUse](../../compositestructures/mdcollaborations/CollaborationUse.html) value)
Sets the value of the
 '[`*collaboration Use Of Role Binding*`](#get_collaborationUseOfRoleBinding())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*collaboration Use Of Role Binding*' container reference.
See Also:
[`get_collaborationUseOfRoleBinding()`](#get_collaborationUseOfRoleBinding())
Generated:
getSupplier
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[NamedElement](../mdkernel/NamedElement.html)> getSupplier()
Returns the value of the '***Supplier***' reference list.
 The list contents are of type [`NamedElement`](../mdkernel/NamedElement.html).
 It is bidirectional and its opposite is '[`*Supplier Dependency*`](../mdkernel/NamedElement.html#getSupplierDependency())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Element(s) on which the client Element(s) depend in some respect. The modeler may stipulate a sense of Dependency direction suitable for their domain.
 end-model-doc
Returns:
the value of the '*Supplier*' reference list.
See Also:
[`UMLPackage.getDependency_Supplier()`](../../metadata/UMLPackage.html#getDependency_Supplier())
[`NamedElement.getSupplierDependency()`](../mdkernel/NamedElement.html#getSupplierDependency())
Model:
opposite="supplierDependency" required="true" ordered="false"
Generated:
getClient
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[NamedElement](../mdkernel/NamedElement.html)> getClient()
Returns the value of the '***Client***' reference list.
 The list contents are of type [`NamedElement`](../mdkernel/NamedElement.html).
 It is bidirectional and its opposite is '[`*Client Dependency*`](../mdkernel/NamedElement.html#getClientDependency())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Element(s) dependent on the supplier Element(s). In some cases (such as a trace Abstraction) the assignment of direction (that is, the designation of the
 client Element) is at the discretion of the modeler and is a stipulation.
 end-model-doc
Returns:
the value of the '*Client*' reference list.
See Also:
[`UMLPackage.getDependency_Client()`](../../metadata/UMLPackage.html#getDependency_Client())
[`NamedElement.getClientDependency()`](../mdkernel/NamedElement.html#getClientDependency())
Model:
opposite="clientDependency" required="true" ordered="false"
Generated:
hasSupplier
boolean hasSupplier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasClient
boolean hasClient()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mddependencies</a></div>
<h1 class="title" title="Interface Dependency">Interface Dependency</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="../mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code>, <code><a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code>, <code><a href="../../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code>, <code><a href="../mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code>, <code><a href="../../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code>, <code><a href="Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code>, <code><a href="Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code>, <code><a href="Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Dependency</span><span class="extends-implements">
extends <a href="../mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>, <a href="../mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Dependency</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Dependency is a Relationship that signifies that a single model Element or a set of model Elements requires other model Elements for their specification or
 implementation. This means that the complete semantics of the client Element(s) are either semantically or structurally dependent on the definition of the supplier
 Element(s).
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getClient()"><code><em>Client</em></code></a></li>
<li><a href="#getSupplier()"><code><em>Supplier</em></code></a></li>
<li><a href="#get_collaborationUseOfRoleBinding()"><code><em>collaboration Use Of Role Binding</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getDependency()"><code>UMLPackage.getDependency()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='classes.mddependencies'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_collaborationUseOfRoleBinding()">get_collaborationUseOfRoleBinding</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>collaboration Use Of Role Binding</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClient()">getClient</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Client</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSupplier()">getSupplier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Supplier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasClient()">hasClient</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSupplier()">hasSupplier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">set_collaborationUseOfRoleBinding</a><wbr/>(<a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_collaborationUseOfRoleBinding()"><code><em>collaboration Use Of Role Binding</em></code></a>' container
 reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></h3>
<code><a href="../mdkernel/DirectedRelationship.html#getSource()">getSource</a>, <a href="../mdkernel/DirectedRelationship.html#getTarget()">getTarget</a>, <a href="../mdkernel/DirectedRelationship.html#hasSource()">hasSource</a>, <a href="../mdkernel/DirectedRelationship.html#hasTarget()">hasTarget</a></code></div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../mdkernel/NamedElement.html#getName()">getName</a>, <a href="../mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="../mdkernel/PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="../mdkernel/PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="../mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="../mdkernel/PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="../mdkernel/PackageableElement.html#getVisibility()">getVisibility</a>, <a href="../mdkernel/PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="../mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="../mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="../mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="../mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></h3>
<code><a href="../mdkernel/Relationship.html#get_abstraction()">get_abstraction</a>, <a href="../mdkernel/Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="../mdkernel/Relationship.html#has_abstraction()">has_abstraction</a>, <a href="../mdkernel/Relationship.html#hasRelatedElement()">hasRelatedElement</a></code></div>
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
<section class="detail" id="get_collaborationUseOfRoleBinding()">
<h3>get_collaborationUseOfRoleBinding</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a></span> <span class="element-name">get_collaborationUseOfRoleBinding</span>()</div>
<div class="block">Returns the value of the '<em><b>collaboration Use Of Role Binding</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../compositestructures/mdcollaborations/CollaborationUse.html#getRoleBinding()"><code><em>Role Binding</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>collaboration Use Of Role Binding</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>collaboration Use Of Role Binding</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)"><code>set_collaborationUseOfRoleBinding(CollaborationUse)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getDependency__collaborationUseOfRoleBinding()"><code>UMLPackage.getDependency__collaborationUseOfRoleBinding()</code></a></li>
<li><a href="../../compositestructures/mdcollaborations/CollaborationUse.html#getRoleBinding()"><code>CollaborationUse.getRoleBinding()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="roleBinding" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">
<h3>set_collaborationUseOfRoleBinding</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_collaborationUseOfRoleBinding</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../compositestructures/mdcollaborations/CollaborationUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">CollaborationUse</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_collaborationUseOfRoleBinding()"><code><em>collaboration Use Of Role Binding</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>collaboration Use Of Role Binding</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_collaborationUseOfRoleBinding()"><code>get_collaborationUseOfRoleBinding()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplier()">
<h3>getSupplier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getSupplier</span>()</div>
<div class="block">Returns the value of the '<em><b>Supplier</b></em>' reference list.
 The list contents are of type <a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.
 It is bidirectional and its opposite is '<a href="../mdkernel/NamedElement.html#getSupplierDependency()"><code><em>Supplier Dependency</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Element(s) on which the client Element(s) depend in some respect. The modeler may stipulate a sense of Dependency direction suitable for their domain.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Supplier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getDependency_Supplier()"><code>UMLPackage.getDependency_Supplier()</code></a></li>
<li><a href="../mdkernel/NamedElement.html#getSupplierDependency()"><code>NamedElement.getSupplierDependency()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="supplierDependency" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClient()">
<h3>getClient</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getClient</span>()</div>
<div class="block">Returns the value of the '<em><b>Client</b></em>' reference list.
 The list contents are of type <a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.
 It is bidirectional and its opposite is '<a href="../mdkernel/NamedElement.html#getClientDependency()"><code><em>Client Dependency</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Element(s) dependent on the supplier Element(s). In some cases (such as a trace Abstraction) the assignment of direction (that is, the designation of the
 client Element) is at the discretion of the modeler and is a stipulation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Client</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getDependency_Client()"><code>UMLPackage.getDependency_Client()</code></a></li>
<li><a href="../mdkernel/NamedElement.html#getClientDependency()"><code>NamedElement.getClientDependency()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="clientDependency" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSupplier()">
<h3>hasSupplier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSupplier</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasClient()">
<h3>hasClient</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasClient</span>()
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
