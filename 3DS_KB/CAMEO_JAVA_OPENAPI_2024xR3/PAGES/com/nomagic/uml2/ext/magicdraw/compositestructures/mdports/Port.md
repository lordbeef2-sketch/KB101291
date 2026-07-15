# JAVA OPENAPI: Port (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/compositestructures/mdports/Port.html
- source_path: `com/nomagic/uml2/ext/magicdraw/compositestructures/mdports/Port.html`
- source_sha256: `f3f5320d176201778d80bec480536339590d3e3664e3f0f40d3fd0de8e4d228a`
- captured_utc: `2026-07-14T16:56:24.494784+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.compositestructures.mdports](package-summary.html)

## Interface Port

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[ConnectableElement](../mdinternalstructures/ConnectableElement.html)`, `[DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](../../classes/mdkernel/Feature.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[MultiplicityElement](../../classes/mdkernel/MultiplicityElement.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[Property](../../classes/mdkernel/Property.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuralFeature](../../classes/mdkernel/StructuralFeature.html)`, `[TypedElement](../../classes/mdkernel/TypedElement.html)`

public interfacePortextends [Property](../../classes/mdkernel/Property.html)

begin-user-doc 
 A representation of the model object '***Port***'.
 end-user-doc 
begin-model-doc 
 A Port is a property of an EncapsulatedClassifier that specifies a distinct interaction point between that EncapsulatedClassifier and its environment or between the
 (behavior of the) EncapsulatedClassifier and its internal parts. Ports are connected to Properties of the EncapsulatedClassifier by Connectors through which
 requests can be made to invoke BehavioralFeatures. A Port may specify the services an EncapsulatedClassifier provides (offers) to its environment as well as the
 services that an EncapsulatedClassifier expects (requires) of its environment. A Port may have an associated ProtocolStateMachine.
 end-model-doc 
The following features are supported:
 [`*Behavior*`](#isBehavior())
[`*Conjugated*`](#isConjugated())
[`*Service*`](#isService())
[`*Protocol*`](#getProtocol())
[`*Provided*`](#getProvided())
[`*Redefined Port*`](#getRedefinedPort())
[`*port Of Redefined Port*`](#get_portOfRedefinedPort())
[`*Required*`](#getRequired())
[`*invocation Action Of On Port*`](#get_invocationActionOfOnPort())
[`*trigger Of Port*`](#get_triggerOfPort())

See Also:
[`UMLPackage.getPort()`](../../metadata/UMLPackage.html#getPort())
Model:
annotation="MOF package='compositestructures.mdports'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InvocationAction](../../actions/mdbasicactions/InvocationAction.html)>`
`[get_invocationActionOfOnPort](#get_invocationActionOfOnPort())()`
Returns the value of the '***invocation Action Of On Port***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Port](Port.html)>`
`[get_portOfRedefinedPort](#get_portOfRedefinedPort())()`
Returns the value of the '***port Of Redefined Port***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)>`
`[get_triggerOfPort](#get_triggerOfPort())()`
Returns the value of the '***trigger Of Port***' reference list.
`[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`
`[getProtocol](#getProtocol())()`
Returns the value of the '***Protocol***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)>`
`[getProvided](#getProvided())()`
Returns the value of the '***Provided***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Port](Port.html)>`
`[getRedefinedPort](#getRedefinedPort())()`
Returns the value of the '***Redefined Port***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)>`
`[getRequired](#getRequired())()`
Returns the value of the '***Required***' reference list.
`boolean`
`[has_invocationActionOfOnPort](#has_invocationActionOfOnPort())()`

`boolean`
`[has_portOfRedefinedPort](#has_portOfRedefinedPort())()`

`boolean`
`[has_triggerOfPort](#has_triggerOfPort())()`

`boolean`
`[hasProvided](#hasProvided())()`

`boolean`
`[hasRedefinedPort](#hasRedefinedPort())()`

`boolean`
`[hasRequired](#hasRequired())()`

`boolean`
`[isBehavior](#isBehavior())()`
Returns the value of the '***Behavior***' attribute.
`boolean`
`[isConjugated](#isConjugated())()`
Returns the value of the '***Conjugated***' attribute.
`boolean`
`[isService](#isService())()`
Returns the value of the '***Service***' attribute.
`void`
`[setBehavior](#setBehavior(boolean))(boolean value)`
Sets the value of the '[`*Behavior*`](#isBehavior())' attribute.
`void`
`[setConjugated](#setConjugated(boolean))(boolean value)`
Sets the value of the '[`*Conjugated*`](#isConjugated())' attribute.
`void`
`[setProtocol](#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine))([ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) value)`
Sets the value of the '[`*Protocol*`](#getProtocol())' reference.
`void`
`[setService](#setService(boolean))(boolean value)`
Sets the value of the '[`*Service*`](#isService())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[ConnectableElement](../mdinternalstructures/ConnectableElement.html)
`[get_collaborationOfCollaborationRole](../mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()), [get_lifelineOfRepresents](../mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()), [get_structuredClassifierOfRole](../mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()), [getEnd](../mdinternalstructures/ConnectableElement.html#getEnd()), [getTemplateParameter](../mdinternalstructures/ConnectableElement.html#getTemplateParameter()), [has_collaborationOfCollaborationRole](../mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()), [has_lifelineOfRepresents](../mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()), [has_structuredClassifierOfRole](../mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()), [hasEnd](../mdinternalstructures/ConnectableElement.html#hasEnd()), [setTemplateParameter](../mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.[DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)
`[getDeployedElement](../../deployments/mdnodes/DeploymentTarget.html#getDeployedElement()), [getDeployment](../../deployments/mdnodes/DeploymentTarget.html#getDeployment()), [hasDeployedElement](../../deployments/mdnodes/DeploymentTarget.html#hasDeployedElement()), [hasDeployment](../../deployments/mdnodes/DeploymentTarget.html#hasDeployment())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Feature](../../classes/mdkernel/Feature.html)
`[getFeaturingClassifier](../../classes/mdkernel/Feature.html#getFeaturingClassifier()), [isStatic](../../classes/mdkernel/Feature.html#isStatic()), [setFeaturingClassifier](../../classes/mdkernel/Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setStatic](../../classes/mdkernel/Feature.html#setStatic(boolean))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[MultiplicityElement](../../classes/mdkernel/MultiplicityElement.html)
`[getLower](../../classes/mdkernel/MultiplicityElement.html#getLower()), [getLowerValue](../../classes/mdkernel/MultiplicityElement.html#getLowerValue()), [getUpper](../../classes/mdkernel/MultiplicityElement.html#getUpper()), [getUpperValue](../../classes/mdkernel/MultiplicityElement.html#getUpperValue()), [isOrdered](../../classes/mdkernel/MultiplicityElement.html#isOrdered()), [isUnique](../../classes/mdkernel/MultiplicityElement.html#isUnique()), [setLowerValue](../../classes/mdkernel/MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setOrdered](../../classes/mdkernel/MultiplicityElement.html#setOrdered(boolean)), [setUnique](../../classes/mdkernel/MultiplicityElement.html#setUnique(boolean)), [setUpperValue](../../classes/mdkernel/MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Property](../../classes/mdkernel/Property.html)
`[get_artifactOfOwnedAttribute](../../classes/mdkernel/Property.html#get_artifactOfOwnedAttribute()), [get_associationOfNavigableOwnedEnd](../../classes/mdkernel/Property.html#get_associationOfNavigableOwnedEnd()), [get_connectorEndOfPartWithPort](../../classes/mdkernel/Property.html#get_connectorEndOfPartWithPort()), [get_definedTaggedValue](../../classes/mdkernel/Property.html#get_definedTaggedValue()), [get_interactionUseOfReturnValueRecipient](../../classes/mdkernel/Property.html#get_interactionUseOfReturnValueRecipient()), [get_linkEndDataOfEnd](../../classes/mdkernel/Property.html#get_linkEndDataOfEnd()), [get_propertyOfRedefinedProperty](../../classes/mdkernel/Property.html#get_propertyOfRedefinedProperty()), [get_propertyOfSubsettedProperty](../../classes/mdkernel/Property.html#get_propertyOfSubsettedProperty()), [get_qualifierValueOfQualifier](../../classes/mdkernel/Property.html#get_qualifierValueOfQualifier()), [get_readLinkObjectEndActionOfEnd](../../classes/mdkernel/Property.html#get_readLinkObjectEndActionOfEnd()), [get_readLinkObjectEndQualifierActionOfQualifier](../../classes/mdkernel/Property.html#get_readLinkObjectEndQualifierActionOfQualifier()), [get_structuredClassifierOfOwnedAttribute](../../classes/mdkernel/Property.html#get_structuredClassifierOfOwnedAttribute()), [getAggregation](../../classes/mdkernel/Property.html#getAggregation()), [getAssociation](../../classes/mdkernel/Property.html#getAssociation()), [getAssociationEnd](../../classes/mdkernel/Property.html#getAssociationEnd()), [getClassifier](../../classes/mdkernel/Property.html#getClassifier()), [getDatatype](../../classes/mdkernel/Property.html#getDatatype()), [getDefaultValue](../../classes/mdkernel/Property.html#getDefaultValue()), [getInterface](../../classes/mdkernel/Property.html#getInterface()), [getOpposite](../../classes/mdkernel/Property.html#getOpposite()), [getOwningAssociation](../../classes/mdkernel/Property.html#getOwningAssociation()), [getOwningSignal](../../classes/mdkernel/Property.html#getOwningSignal()), [getQualifier](../../classes/mdkernel/Property.html#getQualifier()), [getRedefinedProperty](../../classes/mdkernel/Property.html#getRedefinedProperty()), [getSubsettedProperty](../../classes/mdkernel/Property.html#getSubsettedProperty()), [getUMLClass](../../classes/mdkernel/Property.html#getUMLClass()), [has_connectorEndOfPartWithPort](../../classes/mdkernel/Property.html#has_connectorEndOfPartWithPort()), [has_definedTaggedValue](../../classes/mdkernel/Property.html#has_definedTaggedValue()), [has_interactionUseOfReturnValueRecipient](../../classes/mdkernel/Property.html#has_interactionUseOfReturnValueRecipient()), [has_linkEndDataOfEnd](../../classes/mdkernel/Property.html#has_linkEndDataOfEnd()), [has_propertyOfRedefinedProperty](../../classes/mdkernel/Property.html#has_propertyOfRedefinedProperty()), [has_propertyOfSubsettedProperty](../../classes/mdkernel/Property.html#has_propertyOfSubsettedProperty()), [has_qualifierValueOfQualifier](../../classes/mdkernel/Property.html#has_qualifierValueOfQualifier()), [has_readLinkObjectEndActionOfEnd](../../classes/mdkernel/Property.html#has_readLinkObjectEndActionOfEnd()), [has_readLinkObjectEndQualifierActionOfQualifier](../../classes/mdkernel/Property.html#has_readLinkObjectEndQualifierActionOfQualifier()), [hasQualifier](../../classes/mdkernel/Property.html#hasQualifier()), [hasRedefinedProperty](../../classes/mdkernel/Property.html#hasRedefinedProperty()), [hasSubsettedProperty](../../classes/mdkernel/Property.html#hasSubsettedProperty()), [isComposite](../../classes/mdkernel/Property.html#isComposite()), [isDerived](../../classes/mdkernel/Property.html#isDerived()), [isDerivedUnion](../../classes/mdkernel/Property.html#isDerivedUnion()), [isID](../../classes/mdkernel/Property.html#isID()), [isNavigable](../../classes/mdkernel/Property.html#isNavigable()), [set_artifactOfOwnedAttribute](../../classes/mdkernel/Property.html#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)), [set_associationOfNavigableOwnedEnd](../../classes/mdkernel/Property.html#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [set_structuredClassifierOfOwnedAttribute](../../classes/mdkernel/Property.html#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)), [setAggregation](../../classes/mdkernel/Property.html#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)), [setAssociation](../../classes/mdkernel/Property.html#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [setAssociationEnd](../../classes/mdkernel/Property.html#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [setClassifier](../../classes/mdkernel/Property.html#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setDatatype](../../classes/mdkernel/Property.html#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)), [setDefaultValue](../../classes/mdkernel/Property.html#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setDerived](../../classes/mdkernel/Property.html#setDerived(boolean)), [setDerivedUnion](../../classes/mdkernel/Property.html#setDerivedUnion(boolean)), [setID](../../classes/mdkernel/Property.html#setID(boolean)), [setInterface](../../classes/mdkernel/Property.html#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setOwningAssociation](../../classes/mdkernel/Property.html#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [setOwningSignal](../../classes/mdkernel/Property.html#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)), [setUMLClass](../../classes/mdkernel/Property.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[StructuralFeature](../../classes/mdkernel/StructuralFeature.html)
`[get_slotOfDefiningFeature](../../classes/mdkernel/StructuralFeature.html#get_slotOfDefiningFeature()), [get_structuralFeatureActionOfStructuralFeature](../../classes/mdkernel/StructuralFeature.html#get_structuralFeatureActionOfStructuralFeature()), [has_slotOfDefiningFeature](../../classes/mdkernel/StructuralFeature.html#has_slotOfDefiningFeature()), [has_structuralFeatureActionOfStructuralFeature](../../classes/mdkernel/StructuralFeature.html#has_structuralFeatureActionOfStructuralFeature()), [isReadOnly](../../classes/mdkernel/StructuralFeature.html#isReadOnly()), [setReadOnly](../../classes/mdkernel/StructuralFeature.html#setReadOnly(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](../../classes/mdkernel/TypedElement.html)
`[getType](../../classes/mdkernel/TypedElement.html#getType()), [setType](../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
isBehavior
boolean isBehavior()
Returns the value of the '***Behavior***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether requests arriving at this Port are sent to the classifier behavior of this EncapsulatedClassifier. Such a Port is referred to as a behavior
 Port. Any invocation of a BehavioralFeature targeted at a behavior Port will be handled by the instance of the owning EncapsulatedClassifier itself, rather than
 by any instances that it may contain.
 end-model-doc
Returns:
the value of the '*Behavior*' attribute.
See Also:
[`setBehavior(boolean)`](#setBehavior(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getPort_Behavior()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setBehavior
void setBehavior(boolean value)
Sets the value of the '[`*Behavior*`](#isBehavior())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Behavior*' attribute.
See Also:
[`isBehavior()`](#isBehavior())
Generated:
isConjugated
boolean isConjugated()
Returns the value of the '***Conjugated***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the way that the provided and required Interfaces are derived from the Port’s Type.
 end-model-doc
Returns:
the value of the '*Conjugated*' attribute.
See Also:
[`setConjugated(boolean)`](#setConjugated(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getPort_Conjugated()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setConjugated
void setConjugated(boolean value)
Sets the value of the '[`*Conjugated*`](#isConjugated())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Conjugated*' attribute.
See Also:
[`isConjugated()`](#isConjugated())
Generated:
isService
boolean isService()
Returns the value of the '***Service***' attribute.
 The default value is `"true"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, indicates that this Port is used to provide the published functionality of an EncapsulatedClassifier. If false, this Port is used to implement the
 EncapsulatedClassifier but is not part of the essential externally-visible functionality of the EncapsulatedClassifier and can, therefore, be altered or deleted
 along with the internal implementation of the EncapsulatedClassifier and other properties that are considered part of its implementation.
 end-model-doc
Returns:
the value of the '*Service*' attribute.
See Also:
[`setService(boolean)`](#setService(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getPort_Service()`
Model:
default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setService
void setService(boolean value)
Sets the value of the '[`*Service*`](#isService())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Service*' attribute.
See Also:
[`isService()`](#isService())
Generated:
getRequired
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)> getRequired()
Returns the value of the '***Required***' reference list.
 The list contents are of type [`Interface`](../../classes/mdinterfaces/Interface.html).
 It is bidirectional and its opposite is '`*port Of Required*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Interfaces specifying the set of Operations and Receptions that the EncapsulatedCassifier expects its environment to handle via this port. This association
 is derived according to the value of isConjugated. If isConjugated is false, required is derived as the union of the sets of Interfaces used by the type of the
 Port and its supertypes. If isConjugated is true, it is derived as the union of the sets of Interfaces realized by the type of the Port and its supertypes, or
 directly from the type of the Port if the Port is typed by an Interface.
 end-model-doc
Returns:
the value of the '*Required*' reference list.
See Also:
[`UMLPackage.getPort_Required()`](../../metadata/UMLPackage.html#getPort_Required())
`com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_portOfRequired`
Model:
opposite="_portOfRequired" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
get_invocationActionOfOnPort
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InvocationAction](../../actions/mdbasicactions/InvocationAction.html)> get_invocationActionOfOnPort()
Returns the value of the '***invocation Action Of On Port***' reference list.
 The list contents are of type [`InvocationAction`](../../actions/mdbasicactions/InvocationAction.html).
 It is bidirectional and its opposite is '[`*On Port*`](../../actions/mdbasicactions/InvocationAction.html#getOnPort())'.
 begin-user-doc 
If the meaning of the '*invocation Action Of On Port*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*invocation Action Of On Port*' reference list.
See Also:
[`UMLPackage.getPort__invocationActionOfOnPort()`](../../metadata/UMLPackage.html#getPort__invocationActionOfOnPort())
[`InvocationAction.getOnPort()`](../../actions/mdbasicactions/InvocationAction.html#getOnPort())
Model:
opposite="onPort" ordered="false"
Generated:
getProtocol
@CheckForNull[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) getProtocol()
Returns the value of the '***Protocol***' reference.
 It is bidirectional and its opposite is
 '[`*port Of Protocol*`](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#get_portOfProtocol())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional ProtocolStateMachine which describes valid interactions at this interaction point.
 end-model-doc
Returns:
the value of the '*Protocol*' reference.
See Also:
[`setProtocol(ProtocolStateMachine)`](#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine))
[`UMLPackage.getPort_Protocol()`](../../metadata/UMLPackage.html#getPort_Protocol())
[`ProtocolStateMachine.get_portOfProtocol()`](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#get_portOfProtocol())
Model:
opposite="_portOfProtocol" ordered="false"
Generated:
setProtocol
void setProtocol(@CheckForNull
 [ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html) value)
Sets the value of the '[`*Protocol*`](#getProtocol())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Protocol*' reference.
See Also:
[`getProtocol()`](#getProtocol())
Generated:
getProvided
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interface](../../classes/mdinterfaces/Interface.html)> getProvided()
Returns the value of the '***Provided***' reference list.
 The list contents are of type [`Interface`](../../classes/mdinterfaces/Interface.html).
 It is bidirectional and its opposite is '`*port Of Provided*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Interfaces specifying the set of Operations and Receptions that the EncapsulatedCclassifier offers to its environment via this Port, and which it will handle
 either directly or by forwarding it to a part of its internal structure. This association is derived according to the value of isConjugated. If isConjugated is
 false, provided is derived as the union of the sets of Interfaces realized by the type of the port and its supertypes, or directly from the type of the Port if
 the Port is typed by an Interface. If isConjugated is true, it is derived as the union of the sets of Interfaces used by the type of the Port and its supertypes.
 end-model-doc
Returns:
the value of the '*Provided*' reference list.
See Also:
[`UMLPackage.getPort_Provided()`](../../metadata/UMLPackage.html#getPort_Provided())
`com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_portOfProvided`
Model:
opposite="_portOfProvided" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getRedefinedPort
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Port](Port.html)> getRedefinedPort()
Returns the value of the '***Redefined Port***' reference list.
 The list contents are of type [`Port`](Port.html).
 It is bidirectional and its opposite is
 '[`*port Of Redefined Port*`](#get_portOfRedefinedPort())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A Port may be redefined when its containing EncapsulatedClassifier is specialized. The redefining Port may have additional Interfaces to those that are
 associated with the redefined Port or it may replace an Interface by one of its subtypes.
 end-model-doc
Returns:
the value of the '*Redefined Port*' reference list.
See Also:
[`UMLPackage.getPort_RedefinedPort()`](../../metadata/UMLPackage.html#getPort_RedefinedPort())
[`get_portOfRedefinedPort()`](#get_portOfRedefinedPort())
Model:
opposite="_portOfRedefinedPort" ordered="false"
Generated:
get_portOfRedefinedPort
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Port](Port.html)> get_portOfRedefinedPort()
Returns the value of the '***port Of Redefined Port***' reference list.
 The list contents are of type [`Port`](Port.html).
 It is bidirectional and its opposite is '[`*Redefined Port*`](#getRedefinedPort())'.
 begin-user-doc 
If the meaning of the '*port Of Redefined Port*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*port Of Redefined Port*' reference list.
See Also:
[`UMLPackage.getPort__portOfRedefinedPort()`](../../metadata/UMLPackage.html#getPort__portOfRedefinedPort())
[`getRedefinedPort()`](#getRedefinedPort())
Model:
opposite="redefinedPort" ordered="false"
Generated:
get_triggerOfPort
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)> get_triggerOfPort()
Returns the value of the '***trigger Of Port***' reference list.
 The list contents are of type [`Trigger`](../../commonbehaviors/mdcommunications/Trigger.html).
 It is bidirectional and its opposite is '[`*Port*`](../../commonbehaviors/mdcommunications/Trigger.html#getPort())'.
 begin-user-doc 
If the meaning of the '*trigger Of Port*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*trigger Of Port*' reference list.
See Also:
[`UMLPackage.getPort__triggerOfPort()`](../../metadata/UMLPackage.html#getPort__triggerOfPort())
[`Trigger.getPort()`](../../commonbehaviors/mdcommunications/Trigger.html#getPort())
Model:
opposite="port" ordered="false"
Generated:
hasRequired
boolean hasRequired()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_invocationActionOfOnPort
boolean has_invocationActionOfOnPort()
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
hasRedefinedPort
boolean hasRedefinedPort()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_portOfRedefinedPort
boolean has_portOfRedefinedPort()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_triggerOfPort
boolean has_triggerOfPort()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.compositestructures.mdports</a></div>
<h1 class="title" title="Interface Port">Interface Port</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Port</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Port</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Port is a property of an EncapsulatedClassifier that specifies a distinct interaction point between that EncapsulatedClassifier and its environment or between the
 (behavior of the) EncapsulatedClassifier and its internal parts. Ports are connected to Properties of the EncapsulatedClassifier by Connectors through which
 requests can be made to invoke BehavioralFeatures. A Port may specify the services an EncapsulatedClassifier provides (offers) to its environment as well as the
 services that an EncapsulatedClassifier expects (requires) of its environment.  A Port may have an associated ProtocolStateMachine.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isBehavior()"><code><em>Behavior</em></code></a></li>
<li><a href="#isConjugated()"><code><em>Conjugated</em></code></a></li>
<li><a href="#isService()"><code><em>Service</em></code></a></li>
<li><a href="#getProtocol()"><code><em>Protocol</em></code></a></li>
<li><a href="#getProvided()"><code><em>Provided</em></code></a></li>
<li><a href="#getRedefinedPort()"><code><em>Redefined Port</em></code></a></li>
<li><a href="#get_portOfRedefinedPort()"><code><em>port Of Redefined Port</em></code></a></li>
<li><a href="#getRequired()"><code><em>Required</em></code></a></li>
<li><a href="#get_invocationActionOfOnPort()"><code><em>invocation Action Of On Port</em></code></a></li>
<li><a href="#get_triggerOfPort()"><code><em>trigger Of Port</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getPort()"><code>UMLPackage.getPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='compositestructures.mdports'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_invocationActionOfOnPort()">get_invocationActionOfOnPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>invocation Action Of On Port</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_portOfRedefinedPort()">get_portOfRedefinedPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>port Of Redefined Port</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_triggerOfPort()">get_triggerOfPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>trigger Of Port</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProtocol()">getProtocol</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Protocol</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProvided()">getProvided</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Provided</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedPort()">getRedefinedPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Port</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRequired()">getRequired</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Required</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_invocationActionOfOnPort()">has_invocationActionOfOnPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_portOfRedefinedPort()">has_portOfRedefinedPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_triggerOfPort()">has_triggerOfPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasProvided()">hasProvided</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedPort()">hasRedefinedPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRequired()">hasRequired</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isBehavior()">isBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Behavior</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isConjugated()">isConjugated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Conjugated</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isService()">isService</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Service</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBehavior(boolean)">setBehavior</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isBehavior()"><code><em>Behavior</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setConjugated(boolean)">setConjugated</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isConjugated()"><code><em>Conjugated</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)">setProtocol</a><wbr/>(<a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getProtocol()"><code><em>Protocol</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setService(boolean)">setService</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isService()"><code><em>Service</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#atInsert()">atInsert</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#clone()">clone</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></h3>
<code><a href="../mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()">get_collaborationOfCollaborationRole</a>, <a href="../mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()">get_lifelineOfRepresents</a>, <a href="../mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()">get_structuredClassifierOfRole</a>, <a href="../mdinternalstructures/ConnectableElement.html#getEnd()">getEnd</a>, <a href="../mdinternalstructures/ConnectableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()">has_collaborationOfCollaborationRole</a>, <a href="../mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()">has_lifelineOfRepresents</a>, <a href="../mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()">has_structuredClassifierOfRole</a>, <a href="../mdinternalstructures/ConnectableElement.html#hasEnd()">hasEnd</a>, <a href="../mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.<a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></h3>
<code><a href="../../deployments/mdnodes/DeploymentTarget.html#getDeployedElement()">getDeployedElement</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html#getDeployment()">getDeployment</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html#hasDeployedElement()">hasDeployedElement</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html#hasDeployment()">hasDeployment</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></h3>
<code><a href="../../classes/mdkernel/Feature.html#getFeaturingClassifier()">getFeaturingClassifier</a>, <a href="../../classes/mdkernel/Feature.html#isStatic()">isStatic</a>, <a href="../../classes/mdkernel/Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setFeaturingClassifier</a>, <a href="../../classes/mdkernel/Feature.html#setStatic(boolean)">setStatic</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></h3>
<code><a href="../../classes/mdkernel/MultiplicityElement.html#getLower()">getLower</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#getLowerValue()">getLowerValue</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#getUpper()">getUpper</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#getUpperValue()">getUpperValue</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#isOrdered()">isOrdered</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#isUnique()">isUnique</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setLowerValue</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setOrdered(boolean)">setOrdered</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setUnique(boolean)">setUnique</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></h3>
<code><a href="../../classes/mdkernel/Property.html#get_artifactOfOwnedAttribute()">get_artifactOfOwnedAttribute</a>, <a href="../../classes/mdkernel/Property.html#get_associationOfNavigableOwnedEnd()">get_associationOfNavigableOwnedEnd</a>, <a href="../../classes/mdkernel/Property.html#get_connectorEndOfPartWithPort()">get_connectorEndOfPartWithPort</a>, <a href="../../classes/mdkernel/Property.html#get_definedTaggedValue()">get_definedTaggedValue</a>, <a href="../../classes/mdkernel/Property.html#get_interactionUseOfReturnValueRecipient()">get_interactionUseOfReturnValueRecipient</a>, <a href="../../classes/mdkernel/Property.html#get_linkEndDataOfEnd()">get_linkEndDataOfEnd</a>, <a href="../../classes/mdkernel/Property.html#get_propertyOfRedefinedProperty()">get_propertyOfRedefinedProperty</a>, <a href="../../classes/mdkernel/Property.html#get_propertyOfSubsettedProperty()">get_propertyOfSubsettedProperty</a>, <a href="../../classes/mdkernel/Property.html#get_qualifierValueOfQualifier()">get_qualifierValueOfQualifier</a>, <a href="../../classes/mdkernel/Property.html#get_readLinkObjectEndActionOfEnd()">get_readLinkObjectEndActionOfEnd</a>, <a href="../../classes/mdkernel/Property.html#get_readLinkObjectEndQualifierActionOfQualifier()">get_readLinkObjectEndQualifierActionOfQualifier</a>, <a href="../../classes/mdkernel/Property.html#get_structuredClassifierOfOwnedAttribute()">get_structuredClassifierOfOwnedAttribute</a>, <a href="../../classes/mdkernel/Property.html#getAggregation()">getAggregation</a>, <a href="../../classes/mdkernel/Property.html#getAssociation()">getAssociation</a>, <a href="../../classes/mdkernel/Property.html#getAssociationEnd()">getAssociationEnd</a>, <a href="../../classes/mdkernel/Property.html#getClassifier()">getClassifier</a>, <a href="../../classes/mdkernel/Property.html#getDatatype()">getDatatype</a>, <a href="../../classes/mdkernel/Property.html#getDefaultValue()">getDefaultValue</a>, <a href="../../classes/mdkernel/Property.html#getInterface()">getInterface</a>, <a href="../../classes/mdkernel/Property.html#getOpposite()">getOpposite</a>, <a href="../../classes/mdkernel/Property.html#getOwningAssociation()">getOwningAssociation</a>, <a href="../../classes/mdkernel/Property.html#getOwningSignal()">getOwningSignal</a>, <a href="../../classes/mdkernel/Property.html#getQualifier()">getQualifier</a>, <a href="../../classes/mdkernel/Property.html#getRedefinedProperty()">getRedefinedProperty</a>, <a href="../../classes/mdkernel/Property.html#getSubsettedProperty()">getSubsettedProperty</a>, <a href="../../classes/mdkernel/Property.html#getUMLClass()">getUMLClass</a>, <a href="../../classes/mdkernel/Property.html#has_connectorEndOfPartWithPort()">has_connectorEndOfPartWithPort</a>, <a href="../../classes/mdkernel/Property.html#has_definedTaggedValue()">has_definedTaggedValue</a>, <a href="../../classes/mdkernel/Property.html#has_interactionUseOfReturnValueRecipient()">has_interactionUseOfReturnValueRecipient</a>, <a href="../../classes/mdkernel/Property.html#has_linkEndDataOfEnd()">has_linkEndDataOfEnd</a>, <a href="../../classes/mdkernel/Property.html#has_propertyOfRedefinedProperty()">has_propertyOfRedefinedProperty</a>, <a href="../../classes/mdkernel/Property.html#has_propertyOfSubsettedProperty()">has_propertyOfSubsettedProperty</a>, <a href="../../classes/mdkernel/Property.html#has_qualifierValueOfQualifier()">has_qualifierValueOfQualifier</a>, <a href="../../classes/mdkernel/Property.html#has_readLinkObjectEndActionOfEnd()">has_readLinkObjectEndActionOfEnd</a>, <a href="../../classes/mdkernel/Property.html#has_readLinkObjectEndQualifierActionOfQualifier()">has_readLinkObjectEndQualifierActionOfQualifier</a>, <a href="../../classes/mdkernel/Property.html#hasQualifier()">hasQualifier</a>, <a href="../../classes/mdkernel/Property.html#hasRedefinedProperty()">hasRedefinedProperty</a>, <a href="../../classes/mdkernel/Property.html#hasSubsettedProperty()">hasSubsettedProperty</a>, <a href="../../classes/mdkernel/Property.html#isComposite()">isComposite</a>, <a href="../../classes/mdkernel/Property.html#isDerived()">isDerived</a>, <a href="../../classes/mdkernel/Property.html#isDerivedUnion()">isDerivedUnion</a>, <a href="../../classes/mdkernel/Property.html#isID()">isID</a>, <a href="../../classes/mdkernel/Property.html#isNavigable()">isNavigable</a>, <a href="../../classes/mdkernel/Property.html#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">set_artifactOfOwnedAttribute</a>, <a href="../../classes/mdkernel/Property.html#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">set_associationOfNavigableOwnedEnd</a>, <a href="../../classes/mdkernel/Property.html#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">set_structuredClassifierOfOwnedAttribute</a>, <a href="../../classes/mdkernel/Property.html#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">setAggregation</a>, <a href="../../classes/mdkernel/Property.html#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setAssociation</a>, <a href="../../classes/mdkernel/Property.html#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setAssociationEnd</a>, <a href="../../classes/mdkernel/Property.html#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setClassifier</a>, <a href="../../classes/mdkernel/Property.html#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">setDatatype</a>, <a href="../../classes/mdkernel/Property.html#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setDefaultValue</a>, <a href="../../classes/mdkernel/Property.html#setDerived(boolean)">setDerived</a>, <a href="../../classes/mdkernel/Property.html#setDerivedUnion(boolean)">setDerivedUnion</a>, <a href="../../classes/mdkernel/Property.html#setID(boolean)">setID</a>, <a href="../../classes/mdkernel/Property.html#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">setInterface</a>, <a href="../../classes/mdkernel/Property.html#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setOwningAssociation</a>, <a href="../../classes/mdkernel/Property.html#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">setOwningSignal</a>, <a href="../../classes/mdkernel/Property.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></h3>
<code><a href="../../classes/mdkernel/StructuralFeature.html#get_slotOfDefiningFeature()">get_slotOfDefiningFeature</a>, <a href="../../classes/mdkernel/StructuralFeature.html#get_structuralFeatureActionOfStructuralFeature()">get_structuralFeatureActionOfStructuralFeature</a>, <a href="../../classes/mdkernel/StructuralFeature.html#has_slotOfDefiningFeature()">has_slotOfDefiningFeature</a>, <a href="../../classes/mdkernel/StructuralFeature.html#has_structuralFeatureActionOfStructuralFeature()">has_structuralFeatureActionOfStructuralFeature</a>, <a href="../../classes/mdkernel/StructuralFeature.html#isReadOnly()">isReadOnly</a>, <a href="../../classes/mdkernel/StructuralFeature.html#setReadOnly(boolean)">setReadOnly</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></h3>
<code><a href="../../classes/mdkernel/TypedElement.html#getType()">getType</a>, <a href="../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a></code></div>
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
<section class="detail" id="isBehavior()">
<h3>isBehavior</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>Behavior</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether requests arriving at this Port are sent to the classifier behavior of this EncapsulatedClassifier. Such a Port is referred to as a behavior
 Port. Any invocation of a BehavioralFeature targeted at a behavior Port will be handled by the instance of the owning EncapsulatedClassifier itself, rather than
 by any instances that it may contain.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Behavior</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setBehavior(boolean)"><code>setBehavior(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getPort_Behavior()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBehavior(boolean)">
<h3>setBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBehavior</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isBehavior()"><code><em>Behavior</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Behavior</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isBehavior()"><code>isBehavior()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConjugated()">
<h3>isConjugated</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isConjugated</span>()</div>
<div class="block">Returns the value of the '<em><b>Conjugated</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the way that the provided and required Interfaces are derived from the Port’s Type.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Conjugated</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setConjugated(boolean)"><code>setConjugated(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getPort_Conjugated()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConjugated(boolean)">
<h3>setConjugated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setConjugated</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isConjugated()"><code><em>Conjugated</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Conjugated</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isConjugated()"><code>isConjugated()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isService()">
<h3>isService</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isService</span>()</div>
<div class="block">Returns the value of the '<em><b>Service</b></em>' attribute.
 The default value is <code>"true"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, indicates that this Port is used to provide the published functionality of an EncapsulatedClassifier.  If false, this Port is used to implement the
 EncapsulatedClassifier but is not part of the essential externally-visible functionality of the EncapsulatedClassifier and can, therefore, be altered or deleted
 along with the internal implementation of the EncapsulatedClassifier and other properties that are considered part of its implementation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Service</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setService(boolean)"><code>setService(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getPort_Service()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setService(boolean)">
<h3>setService</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setService</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isService()"><code><em>Service</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Service</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isService()"><code>isService()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequired()">
<h3>getRequired</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getRequired</span>()</div>
<div class="block">Returns the value of the '<em><b>Required</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.
 It is bidirectional and its opposite is '<code><em>port Of Required</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Interfaces specifying the set of Operations and Receptions that the EncapsulatedCassifier expects its environment to handle via this port. This association
 is derived according to the value of isConjugated. If isConjugated is false, required is derived as the union of the sets of Interfaces used by the type of the
 Port and its supertypes. If isConjugated is true, it is derived as the union of the sets of Interfaces realized by the type of the Port and its supertypes, or
 directly from the type of the Port if the Port is typed by an Interface.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Required</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getPort_Required()"><code>UMLPackage.getPort_Required()</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_portOfRequired</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_portOfRequired" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_invocationActionOfOnPort()">
<h3>get_invocationActionOfOnPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a>&gt;</span> <span class="element-name">get_invocationActionOfOnPort</span>()</div>
<div class="block">Returns the value of the '<em><b>invocation Action Of On Port</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InvocationAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/InvocationAction.html#getOnPort()"><code><em>On Port</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>invocation Action Of On Port</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>invocation Action Of On Port</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getPort__invocationActionOfOnPort()"><code>UMLPackage.getPort__invocationActionOfOnPort()</code></a></li>
<li><a href="../../actions/mdbasicactions/InvocationAction.html#getOnPort()"><code>InvocationAction.getOnPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="onPort" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProtocol()">
<h3>getProtocol</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></span> <span class="element-name">getProtocol</span>()</div>
<div class="block">Returns the value of the '<em><b>Protocol</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#get_portOfProtocol()"><code><em>port Of Protocol</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional ProtocolStateMachine which describes valid interactions at this interaction point.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Protocol</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)"><code>setProtocol(ProtocolStateMachine)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getPort_Protocol()"><code>UMLPackage.getPort_Protocol()</code></a></li>
<li><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html#get_portOfProtocol()"><code>ProtocolStateMachine.get_portOfProtocol()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_portOfProtocol" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProtocol(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolStateMachine)">
<h3>setProtocol</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setProtocol</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getProtocol()"><code><em>Protocol</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Protocol</em>' reference.</dd>
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
<section class="detail" id="getProvided()">
<h3>getProvided</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a>&gt;</span> <span class="element-name">getProvided</span>()</div>
<div class="block">Returns the value of the '<em><b>Provided</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces"><code>Interface</code></a>.
 It is bidirectional and its opposite is '<code><em>port Of Provided</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Interfaces specifying the set of Operations and Receptions that the EncapsulatedCclassifier offers to its environment via this Port, and which it will handle
 either directly or by forwarding it to a part of its internal structure. This association is derived according to the value of isConjugated. If isConjugated is
 false, provided is derived as the union of the sets of Interfaces realized by the type of the port and its supertypes, or directly from the type of the Port if
 the Port is typed by an Interface. If isConjugated is true, it is derived as the union of the sets of Interfaces used by the type of the Port and its supertypes.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Provided</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getPort_Provided()"><code>UMLPackage.getPort_Provided()</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface#get_portOfProvided</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_portOfProvided" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedPort()">
<h3>getRedefinedPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</span> <span class="element-name">getRedefinedPort</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Port</b></em>' reference list.
 The list contents are of type <a href="Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_portOfRedefinedPort()"><code><em>port Of Redefined Port</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A Port may be redefined when its containing EncapsulatedClassifier is specialized. The redefining Port may have additional Interfaces to those that are
 associated with the redefined Port or it may replace an Interface by one of its subtypes.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Port</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getPort_RedefinedPort()"><code>UMLPackage.getPort_RedefinedPort()</code></a></li>
<li><a href="#get_portOfRedefinedPort()"><code>get_portOfRedefinedPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_portOfRedefinedPort" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_portOfRedefinedPort()">
<h3>get_portOfRedefinedPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</span> <span class="element-name">get_portOfRedefinedPort</span>()</div>
<div class="block">Returns the value of the '<em><b>port Of Redefined Port</b></em>' reference list.
 The list contents are of type <a href="Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.
 It is bidirectional and its opposite is '<a href="#getRedefinedPort()"><code><em>Redefined Port</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>port Of Redefined Port</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>port Of Redefined Port</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getPort__portOfRedefinedPort()"><code>UMLPackage.getPort__portOfRedefinedPort()</code></a></li>
<li><a href="#getRedefinedPort()"><code>getRedefinedPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedPort" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_triggerOfPort()">
<h3>get_triggerOfPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt;</span> <span class="element-name">get_triggerOfPort</span>()</div>
<div class="block">Returns the value of the '<em><b>trigger Of Port</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdcommunications/Trigger.html#getPort()"><code><em>Port</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>trigger Of Port</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>trigger Of Port</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getPort__triggerOfPort()"><code>UMLPackage.getPort__triggerOfPort()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/Trigger.html#getPort()"><code>Trigger.getPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="port" ordered="false"</dd>
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
<li>
<section class="detail" id="has_invocationActionOfOnPort()">
<h3>has_invocationActionOfOnPort</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_invocationActionOfOnPort</span>()
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
<section class="detail" id="hasRedefinedPort()">
<h3>hasRedefinedPort</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedPort</span>()
                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_portOfRedefinedPort()">
<h3>has_portOfRedefinedPort</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_portOfRedefinedPort</span>()
                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_triggerOfPort()">
<h3>has_triggerOfPort</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_triggerOfPort</span>()
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
