# JAVA OPENAPI: InterfaceRealization (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdinterfaces/InterfaceRealization.html`
- source_sha256: `dc92829e892bfecae8f5442eea768ebcd1a724b8a54be3c26bfeca512486dd60`
- captured_utc: `2026-07-14T16:52:49.872379+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces](package-summary.html)

## Interface InterfaceRealization

All Superinterfaces:
`[Abstraction](../mddependencies/Abstraction.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Dependency](../mddependencies/Dependency.html)`, `[DirectedRelationship](../mdkernel/DirectedRelationship.html)`, `[Element](../mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[Realization](../mddependencies/Realization.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Relationship](../mdkernel/Relationship.html)`

public interfaceInterfaceRealizationextends [Realization](../mddependencies/Realization.html)

begin-user-doc 
 A representation of the model object '***Interface Realization***'.
 end-user-doc 
begin-model-doc 
 An InterfaceRealization is a specialized realization relationship between a BehavioredClassifier and an Interface. This relationship signifies that the realizing
 BehavioredClassifier conforms to the contract specified by the Interface.
 end-model-doc 
The following features are supported:
 [`*Implementing Classifier*`](#getImplementingClassifier())
[`*Contract*`](#getContract())

See Also:
[`UMLPackage.getInterfaceRealization()`](../../metadata/UMLPackage.html#getInterfaceRealization())
Model:
annotation="MOF package='classes.mdinterfaces'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Interface](Interface.html)`
`[getContract](#getContract())()`
Returns the value of the '***Contract***' reference.
`[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`
`[getImplementingClassifier](#getImplementingClassifier())()`
Returns the value of the '***Implementing Classifier***' container reference.
`void`
`[setContract](#setContract(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([Interface](Interface.html) value)`
Sets the value of the '[`*Contract*`](#getContract())' reference.
`void`
`[setImplementingClassifier](#setImplementingClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) value)`
Sets the value of the
 '[`*Implementing Classifier*`](#getImplementingClassifier())' container reference.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mddependencies.[Abstraction](../mddependencies/Abstraction.html)
`[getMapping](../mddependencies/Abstraction.html#getMapping()), [setMapping](../mddependencies/Abstraction.html#setMapping(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mddependencies.[Dependency](../mddependencies/Dependency.html)
`[get_collaborationUseOfRoleBinding](../mddependencies/Dependency.html#get_collaborationUseOfRoleBinding()), [getClient](../mddependencies/Dependency.html#getClient()), [getSupplier](../mddependencies/Dependency.html#getSupplier()), [hasClient](../mddependencies/Dependency.html#hasClient()), [hasSupplier](../mddependencies/Dependency.html#hasSupplier()), [set_collaborationUseOfRoleBinding](../mddependencies/Dependency.html#set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse))`
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
getContract
@CheckForNull[Interface](Interface.html) getContract()
Returns the value of the '***Contract***' reference.
 It is bidirectional and its opposite is
 '[`*interface Realization Of Contract*`](Interface.html#get_interfaceRealizationOfContract())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Interface specifying the conformance contract.
 end-model-doc
Returns:
the value of the '*Contract*' reference.
See Also:
[`setContract(Interface)`](#setContract(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))
[`UMLPackage.getInterfaceRealization_Contract()`](../../metadata/UMLPackage.html#getInterfaceRealization_Contract())
[`Interface.get_interfaceRealizationOfContract()`](Interface.html#get_interfaceRealizationOfContract())
Model:
opposite="_interfaceRealizationOfContract" required="true" ordered="false"
Generated:
setContract
void setContract(@CheckForNull
 [Interface](Interface.html) value)
Sets the value of the '[`*Contract*`](#getContract())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Contract*' reference.
See Also:
[`getContract()`](#getContract())
Generated:
getImplementingClassifier
@CheckForNull[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) getImplementingClassifier()
Returns the value of the '***Implementing Classifier***' container reference.
 It is bidirectional and its opposite is
 '[`*Interface Realization*`](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the BehavioredClassifier that owns this InterfaceRealization, i.e., the BehavioredClassifier that realizes the Interface to which it refers.
 end-model-doc
Returns:
the value of the '*Implementing Classifier*' container reference.
See Also:
[`setImplementingClassifier(BehavioredClassifier)`](#setImplementingClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))
[`UMLPackage.getInterfaceRealization_ImplementingClassifier()`](../../metadata/UMLPackage.html#getInterfaceRealization_ImplementingClassifier())
[`BehavioredClassifier.getInterfaceRealization()`](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization())
Model:
opposite="interfaceRealization" required="true" transient="false" ordered="false"
Generated:
setImplementingClassifier
void setImplementingClassifier(@CheckForNull
 [BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html) value)
Sets the value of the
 '[`*Implementing Classifier*`](#getImplementingClassifier())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Implementing Classifier*' container reference.
See Also:
[`getImplementingClassifier()`](#getImplementingClassifier())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces</a></div>
<h1 class="title" title="Interface InterfaceRealization">Interface InterfaceRealization</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code>, <code><a href="../mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="../mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">InterfaceRealization</span><span class="extends-implements">
extends <a href="../mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Interface Realization</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An InterfaceRealization is a specialized realization relationship between a BehavioredClassifier and an Interface. This relationship signifies that the realizing
 BehavioredClassifier conforms to the contract specified by the Interface.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getImplementingClassifier()"><code><em>Implementing Classifier</em></code></a></li>
<li><a href="#getContract()"><code><em>Contract</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getInterfaceRealization()"><code>UMLPackage.getInterfaceRealization()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContract()">getContract</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Contract</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImplementingClassifier()">getImplementingClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Implementing Classifier</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setContract(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">setContract</a><wbr/>(<a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getContract()"><code><em>Contract</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setImplementingClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">setImplementingClassifier</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#getImplementingClassifier()"><code><em>Implementing Classifier</em></code></a>' container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Abstraction">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mddependencies.<a href="../mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></h3>
<code><a href="../mddependencies/Abstraction.html#getMapping()">getMapping</a>, <a href="../mddependencies/Abstraction.html#setMapping(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">setMapping</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mddependencies.Dependency">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mddependencies.<a href="../mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></h3>
<code><a href="../mddependencies/Dependency.html#get_collaborationUseOfRoleBinding()">get_collaborationUseOfRoleBinding</a>, <a href="../mddependencies/Dependency.html#getClient()">getClient</a>, <a href="../mddependencies/Dependency.html#getSupplier()">getSupplier</a>, <a href="../mddependencies/Dependency.html#hasClient()">hasClient</a>, <a href="../mddependencies/Dependency.html#hasSupplier()">hasSupplier</a>, <a href="../mddependencies/Dependency.html#set_collaborationUseOfRoleBinding(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">set_collaborationUseOfRoleBinding</a></code></div>
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
<section class="detail" id="getContract()">
<h3>getContract</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></span> <span class="element-name">getContract</span>()</div>
<div class="block">Returns the value of the '<em><b>Contract</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="Interface.html#get_interfaceRealizationOfContract()"><code><em>interface Realization Of Contract</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Interface specifying the conformance contract.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Contract</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setContract(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)"><code>setContract(Interface)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInterfaceRealization_Contract()"><code>UMLPackage.getInterfaceRealization_Contract()</code></a></li>
<li><a href="Interface.html#get_interfaceRealizationOfContract()"><code>Interface.get_interfaceRealizationOfContract()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_interfaceRealizationOfContract" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContract(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>setContract</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setContract</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getContract()"><code><em>Contract</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Contract</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getContract()"><code>getContract()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImplementingClassifier()">
<h3>getImplementingClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></span> <span class="element-name">getImplementingClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Implementing Classifier</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()"><code><em>Interface Realization</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the BehavioredClassifier that owns this InterfaceRealization, i.e., the BehavioredClassifier that realizes the Interface to which it refers.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Implementing Classifier</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setImplementingClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)"><code>setImplementingClassifier(BehavioredClassifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInterfaceRealization_ImplementingClassifier()"><code>UMLPackage.getInterfaceRealization_ImplementingClassifier()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()"><code>BehavioredClassifier.getInterfaceRealization()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="interfaceRealization" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImplementingClassifier(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>setImplementingClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setImplementingClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#getImplementingClassifier()"><code><em>Implementing Classifier</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Implementing Classifier</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getImplementingClassifier()"><code>getImplementingClassifier()</code></a></li>
</ul>
</dd>
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
