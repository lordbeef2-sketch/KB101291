# JAVA OPENAPI: ExtensionEnd (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html
- source_path: `com/nomagic/uml2/ext/magicdraw/mdprofiles/ExtensionEnd.html`
- source_sha256: `841d50633a1c3bc66cc796ba7bed9e8389f3b9635875f7479718063ef02f062e`
- captured_utc: `2026-07-14T16:58:57.142506+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.mdprofiles](package-summary.html)

## Interface ExtensionEnd

All Superinterfaces:
`[BaseElement](../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[ConnectableElement](../compositestructures/mdinternalstructures/ConnectableElement.html)`, `[DeploymentTarget](../deployments/mdnodes/DeploymentTarget.html)`, `[Element](../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](../classes/mdkernel/Feature.html)`, `[MDObject](../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../base/ModelObject.html)`, `[MultiplicityElement](../classes/mdkernel/MultiplicityElement.html)`, `[NamedElement](../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ParameterableElement](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[Property](../classes/mdkernel/Property.html)`, `[RedefinableElement](../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuralFeature](../classes/mdkernel/StructuralFeature.html)`, `[TypedElement](../classes/mdkernel/TypedElement.html)`

public interfaceExtensionEndextends [Property](../classes/mdkernel/Property.html)

begin-user-doc 
 A representation of the model object '***Extension End***'.
 end-user-doc 
begin-model-doc 
 An extension end is used to tie an extension to a stereotype when extending a metaclass.
 The default multiplicity of an extension end is 0..1.
 end-model-doc 
The following features are supported:
 [`*extension Of Owned End*`](#get_extensionOfOwnedEnd())

See Also:
[`UMLPackage.getExtensionEnd()`](../metadata/UMLPackage.html#getExtensionEnd())
Model:
annotation="MOF package='mdprofiles'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Extension](Extension.html)`
`[get_extensionOfOwnedEnd](#get_extensionOfOwnedEnd())()`
Returns the value of the '***extension Of Owned End***' container reference.
`int`
`[getLower](#getLower())()`
Returns the value of the '***Lower***' attribute.
`[Stereotype](Stereotype.html)`
`[getType](#getType())()`
Returns the value of the '***Type***' reference.
`void`
`[set_extensionOfOwnedEnd](#set_extensionOfOwnedEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))([Extension](Extension.html) value)`
Sets the value of the '[`*extension Of Owned End*`](#get_extensionOfOwnedEnd())' container
 reference.
`void`
`[setType](#setType(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](Stereotype.html) value)`
Sets the value of the '[`*Type*`](#getType())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[ConnectableElement](../compositestructures/mdinternalstructures/ConnectableElement.html)
`[get_collaborationOfCollaborationRole](../compositestructures/mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()), [get_lifelineOfRepresents](../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()), [get_structuredClassifierOfRole](../compositestructures/mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()), [getEnd](../compositestructures/mdinternalstructures/ConnectableElement.html#getEnd()), [getTemplateParameter](../compositestructures/mdinternalstructures/ConnectableElement.html#getTemplateParameter()), [has_collaborationOfCollaborationRole](../compositestructures/mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()), [has_lifelineOfRepresents](../compositestructures/mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()), [has_structuredClassifierOfRole](../compositestructures/mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()), [hasEnd](../compositestructures/mdinternalstructures/ConnectableElement.html#hasEnd()), [setTemplateParameter](../compositestructures/mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.[DeploymentTarget](../deployments/mdnodes/DeploymentTarget.html)
`[getDeployedElement](../deployments/mdnodes/DeploymentTarget.html#getDeployedElement()), [getDeployment](../deployments/mdnodes/DeploymentTarget.html#getDeployment()), [hasDeployedElement](../deployments/mdnodes/DeploymentTarget.html#hasDeployedElement()), [hasDeployment](../deployments/mdnodes/DeploymentTarget.html#hasDeployment())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Feature](../classes/mdkernel/Feature.html)
`[getFeaturingClassifier](../classes/mdkernel/Feature.html#getFeaturingClassifier()), [isStatic](../classes/mdkernel/Feature.html#isStatic()), [setFeaturingClassifier](../classes/mdkernel/Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setStatic](../classes/mdkernel/Feature.html#setStatic(boolean))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../base/ModelObject.html)
`[get_representationText](../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[MultiplicityElement](../classes/mdkernel/MultiplicityElement.html)
`[getLowerValue](../classes/mdkernel/MultiplicityElement.html#getLowerValue()), [getUpper](../classes/mdkernel/MultiplicityElement.html#getUpper()), [getUpperValue](../classes/mdkernel/MultiplicityElement.html#getUpperValue()), [isOrdered](../classes/mdkernel/MultiplicityElement.html#isOrdered()), [isUnique](../classes/mdkernel/MultiplicityElement.html#isUnique()), [setLowerValue](../classes/mdkernel/MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setOrdered](../classes/mdkernel/MultiplicityElement.html#setOrdered(boolean)), [setUnique](../classes/mdkernel/MultiplicityElement.html#setUnique(boolean)), [setUpperValue](../classes/mdkernel/MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Property](../classes/mdkernel/Property.html)
`[get_artifactOfOwnedAttribute](../classes/mdkernel/Property.html#get_artifactOfOwnedAttribute()), [get_associationOfNavigableOwnedEnd](../classes/mdkernel/Property.html#get_associationOfNavigableOwnedEnd()), [get_connectorEndOfPartWithPort](../classes/mdkernel/Property.html#get_connectorEndOfPartWithPort()), [get_definedTaggedValue](../classes/mdkernel/Property.html#get_definedTaggedValue()), [get_interactionUseOfReturnValueRecipient](../classes/mdkernel/Property.html#get_interactionUseOfReturnValueRecipient()), [get_linkEndDataOfEnd](../classes/mdkernel/Property.html#get_linkEndDataOfEnd()), [get_propertyOfRedefinedProperty](../classes/mdkernel/Property.html#get_propertyOfRedefinedProperty()), [get_propertyOfSubsettedProperty](../classes/mdkernel/Property.html#get_propertyOfSubsettedProperty()), [get_qualifierValueOfQualifier](../classes/mdkernel/Property.html#get_qualifierValueOfQualifier()), [get_readLinkObjectEndActionOfEnd](../classes/mdkernel/Property.html#get_readLinkObjectEndActionOfEnd()), [get_readLinkObjectEndQualifierActionOfQualifier](../classes/mdkernel/Property.html#get_readLinkObjectEndQualifierActionOfQualifier()), [get_structuredClassifierOfOwnedAttribute](../classes/mdkernel/Property.html#get_structuredClassifierOfOwnedAttribute()), [getAggregation](../classes/mdkernel/Property.html#getAggregation()), [getAssociation](../classes/mdkernel/Property.html#getAssociation()), [getAssociationEnd](../classes/mdkernel/Property.html#getAssociationEnd()), [getClassifier](../classes/mdkernel/Property.html#getClassifier()), [getDatatype](../classes/mdkernel/Property.html#getDatatype()), [getDefaultValue](../classes/mdkernel/Property.html#getDefaultValue()), [getInterface](../classes/mdkernel/Property.html#getInterface()), [getOpposite](../classes/mdkernel/Property.html#getOpposite()), [getOwningAssociation](../classes/mdkernel/Property.html#getOwningAssociation()), [getOwningSignal](../classes/mdkernel/Property.html#getOwningSignal()), [getQualifier](../classes/mdkernel/Property.html#getQualifier()), [getRedefinedProperty](../classes/mdkernel/Property.html#getRedefinedProperty()), [getSubsettedProperty](../classes/mdkernel/Property.html#getSubsettedProperty()), [getUMLClass](../classes/mdkernel/Property.html#getUMLClass()), [has_connectorEndOfPartWithPort](../classes/mdkernel/Property.html#has_connectorEndOfPartWithPort()), [has_definedTaggedValue](../classes/mdkernel/Property.html#has_definedTaggedValue()), [has_interactionUseOfReturnValueRecipient](../classes/mdkernel/Property.html#has_interactionUseOfReturnValueRecipient()), [has_linkEndDataOfEnd](../classes/mdkernel/Property.html#has_linkEndDataOfEnd()), [has_propertyOfRedefinedProperty](../classes/mdkernel/Property.html#has_propertyOfRedefinedProperty()), [has_propertyOfSubsettedProperty](../classes/mdkernel/Property.html#has_propertyOfSubsettedProperty()), [has_qualifierValueOfQualifier](../classes/mdkernel/Property.html#has_qualifierValueOfQualifier()), [has_readLinkObjectEndActionOfEnd](../classes/mdkernel/Property.html#has_readLinkObjectEndActionOfEnd()), [has_readLinkObjectEndQualifierActionOfQualifier](../classes/mdkernel/Property.html#has_readLinkObjectEndQualifierActionOfQualifier()), [hasQualifier](../classes/mdkernel/Property.html#hasQualifier()), [hasRedefinedProperty](../classes/mdkernel/Property.html#hasRedefinedProperty()), [hasSubsettedProperty](../classes/mdkernel/Property.html#hasSubsettedProperty()), [isComposite](../classes/mdkernel/Property.html#isComposite()), [isDerived](../classes/mdkernel/Property.html#isDerived()), [isDerivedUnion](../classes/mdkernel/Property.html#isDerivedUnion()), [isID](../classes/mdkernel/Property.html#isID()), [isNavigable](../classes/mdkernel/Property.html#isNavigable()), [set_artifactOfOwnedAttribute](../classes/mdkernel/Property.html#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)), [set_associationOfNavigableOwnedEnd](../classes/mdkernel/Property.html#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [set_structuredClassifierOfOwnedAttribute](../classes/mdkernel/Property.html#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)), [setAggregation](../classes/mdkernel/Property.html#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)), [setAssociation](../classes/mdkernel/Property.html#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [setAssociationEnd](../classes/mdkernel/Property.html#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [setClassifier](../classes/mdkernel/Property.html#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setDatatype](../classes/mdkernel/Property.html#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)), [setDefaultValue](../classes/mdkernel/Property.html#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setDerived](../classes/mdkernel/Property.html#setDerived(boolean)), [setDerivedUnion](../classes/mdkernel/Property.html#setDerivedUnion(boolean)), [setID](../classes/mdkernel/Property.html#setID(boolean)), [setInterface](../classes/mdkernel/Property.html#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setOwningAssociation](../classes/mdkernel/Property.html#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [setOwningSignal](../classes/mdkernel/Property.html#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)), [setUMLClass](../classes/mdkernel/Property.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[StructuralFeature](../classes/mdkernel/StructuralFeature.html)
`[get_slotOfDefiningFeature](../classes/mdkernel/StructuralFeature.html#get_slotOfDefiningFeature()), [get_structuralFeatureActionOfStructuralFeature](../classes/mdkernel/StructuralFeature.html#get_structuralFeatureActionOfStructuralFeature()), [has_slotOfDefiningFeature](../classes/mdkernel/StructuralFeature.html#has_slotOfDefiningFeature()), [has_structuralFeatureActionOfStructuralFeature](../classes/mdkernel/StructuralFeature.html#has_structuralFeatureActionOfStructuralFeature()), [isReadOnly](../classes/mdkernel/StructuralFeature.html#isReadOnly()), [setReadOnly](../classes/mdkernel/StructuralFeature.html#setReadOnly(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](../classes/mdkernel/TypedElement.html)
`[setType](../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
get_extensionOfOwnedEnd
@CheckForNull[Extension](Extension.html) get_extensionOfOwnedEnd()
Returns the value of the '***extension Of Owned End***' container reference.
 It is bidirectional and its opposite is '[`*Owned End*`](Extension.html#getOwnedEnd())'.
 begin-user-doc 
If the meaning of the '*extension Of Owned End*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*extension Of Owned End*' container reference.
See Also:
[`set_extensionOfOwnedEnd(Extension)`](#set_extensionOfOwnedEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension))
[`UMLPackage.getExtensionEnd__extensionOfOwnedEnd()`](../metadata/UMLPackage.html#getExtensionEnd__extensionOfOwnedEnd())
[`Extension.getOwnedEnd()`](Extension.html#getOwnedEnd())
Model:
opposite="ownedEnd" required="true" volatile="true" ordered="false"
Generated:
set_extensionOfOwnedEnd
void set_extensionOfOwnedEnd(@CheckForNull
 [Extension](Extension.html) value)
Sets the value of the '[`*extension Of Owned End*`](#get_extensionOfOwnedEnd())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*extension Of Owned End*' container reference.
See Also:
[`get_extensionOfOwnedEnd()`](#get_extensionOfOwnedEnd())
Generated:
getType
@CheckForNull[Stereotype](Stereotype.html) getType()
Returns the value of the '***Type***' reference.
 It is bidirectional and its opposite is '[`*extension End Of Type*`](Stereotype.html#get_extensionEndOfType())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the type of the ExtensionEnd. Note that this association restricts the possible types of an ExtensionEnd to only be Stereotypes.
 end-model-doc
Specified by:
`[getType](../classes/mdkernel/TypedElement.html#getType())` in interface `[TypedElement](../classes/mdkernel/TypedElement.html)`
Returns:
the value of the '*Type*' reference.
See Also:
[`setType(Stereotype)`](#setType(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
[`UMLPackage.getExtensionEnd_Type()`](../metadata/UMLPackage.html#getExtensionEnd_Type())
[`Stereotype.get_extensionEndOfType()`](Stereotype.html#get_extensionEndOfType())
Model:
opposite="_extensionEndOfType" ordered="false"
Generated:
setType
void setType(@CheckForNull
 [Stereotype](Stereotype.html) value)
Sets the value of the '[`*Type*`](#getType())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Type*' reference.
See Also:
[`getType()`](#getType())
Generated:
getLower
int getLower()
Returns the value of the '***Lower***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This redefinition changes the default multiplicity of association ends, since model elements are usually extended by 0 or 1 instance of the extension stereotype.
 end-model-doc
Specified by:
`[getLower](../classes/mdkernel/MultiplicityElement.html#getLower())` in interface `[MultiplicityElement](../classes/mdkernel/MultiplicityElement.html)`
Returns:
the value of the '*Lower*' attribute.
See Also:
[`UMLPackage.getExtensionEnd_Lower()`](../metadata/UMLPackage.html#getExtensionEnd_Lower())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Integer" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.mdprofiles</a></div>
<h1 class="title" title="Interface ExtensionEnd">Interface ExtensionEnd</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></code>, <code><a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ExtensionEnd</span><span class="extends-implements">
extends <a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Extension End</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An extension end is used to tie an extension to a stereotype when extending a metaclass.
 The default multiplicity of an extension end is 0..1.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_extensionOfOwnedEnd()"><code><em>extension Of Owned End</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../metadata/UMLPackage.html#getExtensionEnd()"><code>UMLPackage.getExtensionEnd()</code></a></li>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_extensionOfOwnedEnd()">get_extensionOfOwnedEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>extension Of Owned End</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLower()">getLower</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Lower</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Type</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_extensionOfOwnedEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">set_extensionOfOwnedEnd</a><wbr/>(<a href="Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_extensionOfOwnedEnd()"><code><em>extension Of Owned End</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setType(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">setType</a><wbr/>(<a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getType()"><code><em>Type</em></code></a>' reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></h3>
<code><a href="../compositestructures/mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()">get_collaborationOfCollaborationRole</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()">get_lifelineOfRepresents</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()">get_structuredClassifierOfRole</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#getEnd()">getEnd</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()">has_collaborationOfCollaborationRole</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()">has_lifelineOfRepresents</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()">has_structuredClassifierOfRole</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#hasEnd()">hasEnd</a>, <a href="../compositestructures/mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.<a href="../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></h3>
<code><a href="../deployments/mdnodes/DeploymentTarget.html#getDeployedElement()">getDeployedElement</a>, <a href="../deployments/mdnodes/DeploymentTarget.html#getDeployment()">getDeployment</a>, <a href="../deployments/mdnodes/DeploymentTarget.html#hasDeployedElement()">hasDeployedElement</a>, <a href="../deployments/mdnodes/DeploymentTarget.html#hasDeployment()">hasDeployment</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></h3>
<code><a href="../classes/mdkernel/Feature.html#getFeaturingClassifier()">getFeaturingClassifier</a>, <a href="../classes/mdkernel/Feature.html#isStatic()">isStatic</a>, <a href="../classes/mdkernel/Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setFeaturingClassifier</a>, <a href="../classes/mdkernel/Feature.html#setStatic(boolean)">setStatic</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></h3>
<code><a href="../classes/mdkernel/MultiplicityElement.html#getLowerValue()">getLowerValue</a>, <a href="../classes/mdkernel/MultiplicityElement.html#getUpper()">getUpper</a>, <a href="../classes/mdkernel/MultiplicityElement.html#getUpperValue()">getUpperValue</a>, <a href="../classes/mdkernel/MultiplicityElement.html#isOrdered()">isOrdered</a>, <a href="../classes/mdkernel/MultiplicityElement.html#isUnique()">isUnique</a>, <a href="../classes/mdkernel/MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setLowerValue</a>, <a href="../classes/mdkernel/MultiplicityElement.html#setOrdered(boolean)">setOrdered</a>, <a href="../classes/mdkernel/MultiplicityElement.html#setUnique(boolean)">setUnique</a>, <a href="../classes/mdkernel/MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></h3>
<code><a href="../classes/mdkernel/Property.html#get_artifactOfOwnedAttribute()">get_artifactOfOwnedAttribute</a>, <a href="../classes/mdkernel/Property.html#get_associationOfNavigableOwnedEnd()">get_associationOfNavigableOwnedEnd</a>, <a href="../classes/mdkernel/Property.html#get_connectorEndOfPartWithPort()">get_connectorEndOfPartWithPort</a>, <a href="../classes/mdkernel/Property.html#get_definedTaggedValue()">get_definedTaggedValue</a>, <a href="../classes/mdkernel/Property.html#get_interactionUseOfReturnValueRecipient()">get_interactionUseOfReturnValueRecipient</a>, <a href="../classes/mdkernel/Property.html#get_linkEndDataOfEnd()">get_linkEndDataOfEnd</a>, <a href="../classes/mdkernel/Property.html#get_propertyOfRedefinedProperty()">get_propertyOfRedefinedProperty</a>, <a href="../classes/mdkernel/Property.html#get_propertyOfSubsettedProperty()">get_propertyOfSubsettedProperty</a>, <a href="../classes/mdkernel/Property.html#get_qualifierValueOfQualifier()">get_qualifierValueOfQualifier</a>, <a href="../classes/mdkernel/Property.html#get_readLinkObjectEndActionOfEnd()">get_readLinkObjectEndActionOfEnd</a>, <a href="../classes/mdkernel/Property.html#get_readLinkObjectEndQualifierActionOfQualifier()">get_readLinkObjectEndQualifierActionOfQualifier</a>, <a href="../classes/mdkernel/Property.html#get_structuredClassifierOfOwnedAttribute()">get_structuredClassifierOfOwnedAttribute</a>, <a href="../classes/mdkernel/Property.html#getAggregation()">getAggregation</a>, <a href="../classes/mdkernel/Property.html#getAssociation()">getAssociation</a>, <a href="../classes/mdkernel/Property.html#getAssociationEnd()">getAssociationEnd</a>, <a href="../classes/mdkernel/Property.html#getClassifier()">getClassifier</a>, <a href="../classes/mdkernel/Property.html#getDatatype()">getDatatype</a>, <a href="../classes/mdkernel/Property.html#getDefaultValue()">getDefaultValue</a>, <a href="../classes/mdkernel/Property.html#getInterface()">getInterface</a>, <a href="../classes/mdkernel/Property.html#getOpposite()">getOpposite</a>, <a href="../classes/mdkernel/Property.html#getOwningAssociation()">getOwningAssociation</a>, <a href="../classes/mdkernel/Property.html#getOwningSignal()">getOwningSignal</a>, <a href="../classes/mdkernel/Property.html#getQualifier()">getQualifier</a>, <a href="../classes/mdkernel/Property.html#getRedefinedProperty()">getRedefinedProperty</a>, <a href="../classes/mdkernel/Property.html#getSubsettedProperty()">getSubsettedProperty</a>, <a href="../classes/mdkernel/Property.html#getUMLClass()">getUMLClass</a>, <a href="../classes/mdkernel/Property.html#has_connectorEndOfPartWithPort()">has_connectorEndOfPartWithPort</a>, <a href="../classes/mdkernel/Property.html#has_definedTaggedValue()">has_definedTaggedValue</a>, <a href="../classes/mdkernel/Property.html#has_interactionUseOfReturnValueRecipient()">has_interactionUseOfReturnValueRecipient</a>, <a href="../classes/mdkernel/Property.html#has_linkEndDataOfEnd()">has_linkEndDataOfEnd</a>, <a href="../classes/mdkernel/Property.html#has_propertyOfRedefinedProperty()">has_propertyOfRedefinedProperty</a>, <a href="../classes/mdkernel/Property.html#has_propertyOfSubsettedProperty()">has_propertyOfSubsettedProperty</a>, <a href="../classes/mdkernel/Property.html#has_qualifierValueOfQualifier()">has_qualifierValueOfQualifier</a>, <a href="../classes/mdkernel/Property.html#has_readLinkObjectEndActionOfEnd()">has_readLinkObjectEndActionOfEnd</a>, <a href="../classes/mdkernel/Property.html#has_readLinkObjectEndQualifierActionOfQualifier()">has_readLinkObjectEndQualifierActionOfQualifier</a>, <a href="../classes/mdkernel/Property.html#hasQualifier()">hasQualifier</a>, <a href="../classes/mdkernel/Property.html#hasRedefinedProperty()">hasRedefinedProperty</a>, <a href="../classes/mdkernel/Property.html#hasSubsettedProperty()">hasSubsettedProperty</a>, <a href="../classes/mdkernel/Property.html#isComposite()">isComposite</a>, <a href="../classes/mdkernel/Property.html#isDerived()">isDerived</a>, <a href="../classes/mdkernel/Property.html#isDerivedUnion()">isDerivedUnion</a>, <a href="../classes/mdkernel/Property.html#isID()">isID</a>, <a href="../classes/mdkernel/Property.html#isNavigable()">isNavigable</a>, <a href="../classes/mdkernel/Property.html#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">set_artifactOfOwnedAttribute</a>, <a href="../classes/mdkernel/Property.html#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">set_associationOfNavigableOwnedEnd</a>, <a href="../classes/mdkernel/Property.html#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">set_structuredClassifierOfOwnedAttribute</a>, <a href="../classes/mdkernel/Property.html#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">setAggregation</a>, <a href="../classes/mdkernel/Property.html#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setAssociation</a>, <a href="../classes/mdkernel/Property.html#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setAssociationEnd</a>, <a href="../classes/mdkernel/Property.html#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setClassifier</a>, <a href="../classes/mdkernel/Property.html#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">setDatatype</a>, <a href="../classes/mdkernel/Property.html#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setDefaultValue</a>, <a href="../classes/mdkernel/Property.html#setDerived(boolean)">setDerived</a>, <a href="../classes/mdkernel/Property.html#setDerivedUnion(boolean)">setDerivedUnion</a>, <a href="../classes/mdkernel/Property.html#setID(boolean)">setID</a>, <a href="../classes/mdkernel/Property.html#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">setInterface</a>, <a href="../classes/mdkernel/Property.html#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setOwningAssociation</a>, <a href="../classes/mdkernel/Property.html#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">setOwningSignal</a>, <a href="../classes/mdkernel/Property.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></h3>
<code><a href="../classes/mdkernel/StructuralFeature.html#get_slotOfDefiningFeature()">get_slotOfDefiningFeature</a>, <a href="../classes/mdkernel/StructuralFeature.html#get_structuralFeatureActionOfStructuralFeature()">get_structuralFeatureActionOfStructuralFeature</a>, <a href="../classes/mdkernel/StructuralFeature.html#has_slotOfDefiningFeature()">has_slotOfDefiningFeature</a>, <a href="../classes/mdkernel/StructuralFeature.html#has_structuralFeatureActionOfStructuralFeature()">has_structuralFeatureActionOfStructuralFeature</a>, <a href="../classes/mdkernel/StructuralFeature.html#isReadOnly()">isReadOnly</a>, <a href="../classes/mdkernel/StructuralFeature.html#setReadOnly(boolean)">setReadOnly</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></h3>
<code><a href="../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a></code></div>
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
<section class="detail" id="get_extensionOfOwnedEnd()">
<h3>get_extensionOfOwnedEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></span> <span class="element-name">get_extensionOfOwnedEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>extension Of Owned End</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Extension.html#getOwnedEnd()"><code><em>Owned End</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>extension Of Owned End</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>extension Of Owned End</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_extensionOfOwnedEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)"><code>set_extensionOfOwnedEnd(Extension)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getExtensionEnd__extensionOfOwnedEnd()"><code>UMLPackage.getExtensionEnd__extensionOfOwnedEnd()</code></a></li>
<li><a href="Extension.html#getOwnedEnd()"><code>Extension.getOwnedEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedEnd" required="true" volatile="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_extensionOfOwnedEnd(com.nomagic.uml2.ext.magicdraw.mdprofiles.Extension)">
<h3>set_extensionOfOwnedEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_extensionOfOwnedEnd</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_extensionOfOwnedEnd()"><code><em>extension Of Owned End</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>extension Of Owned End</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_extensionOfOwnedEnd()"><code>get_extensionOfOwnedEnd()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns the value of the '<em><b>Type</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Stereotype.html#get_extensionEndOfType()"><code><em>extension End Of Type</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the type of the ExtensionEnd. Note that this association restricts the possible types of an ExtensionEnd to only be Stereotypes.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../classes/mdkernel/TypedElement.html#getType()">getType</a></code> in interface <code><a href="../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Type</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setType(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>setType(Stereotype)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getExtensionEnd_Type()"><code>UMLPackage.getExtensionEnd_Type()</code></a></li>
<li><a href="Stereotype.html#get_extensionEndOfType()"><code>Stereotype.get_extensionEndOfType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_extensionEndOfType" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>setType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getType()"><code><em>Type</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Type</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getType()"><code>getType()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLower()">
<h3>getLower</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getLower</span>()</div>
<div class="block">Returns the value of the '<em><b>Lower</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This redefinition changes the default multiplicity of association ends, since model elements are usually extended by 0 or 1 instance of the extension stereotype.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../classes/mdkernel/MultiplicityElement.html#getLower()">getLower</a></code> in interface <code><a href="../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Lower</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../metadata/UMLPackage.html#getExtensionEnd_Lower()"><code>UMLPackage.getExtensionEnd_Lower()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Integer" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
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
