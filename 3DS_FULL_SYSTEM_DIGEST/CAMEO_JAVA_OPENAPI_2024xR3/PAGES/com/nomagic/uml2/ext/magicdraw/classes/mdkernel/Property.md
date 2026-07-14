# JAVA OPENAPI: Property (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Property.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Property.html`
- source_sha256: `8a747424eaf3d90ed6324f62d0c394feb89e7af43f3bfc6705d08352eed5f7c2`
- captured_utc: `2026-07-14T16:56:22.659761+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Property

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)`, `[DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](Feature.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[MultiplicityElement](MultiplicityElement.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuralFeature](StructuralFeature.html)`, `[TypedElement](TypedElement.html)`

All Known Subinterfaces:
`[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[Port](../../compositestructures/mdports/Port.html)`

public interfacePropertyextends [StructuralFeature](StructuralFeature.html), [ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html), [DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)

begin-user-doc 
 A representation of the model object '***Property***'.
 end-user-doc 
begin-model-doc 
 A Property is a StructuralFeature. A Property related by ownedAttribute to a Classifier (other than an association) represents an attribute and might also represent
 an association end. It relates an instance of the Classifier to a value or set of values of the type of the attribute. A Property related by memberEnd to an
 Association represents an end of the Association. The type of the Property is the type of the end of the Association. A Property has the capability of being a
 DeploymentTarget in a Deployment relationship. This enables modeling the deployment to hierarchical nodes that have Properties functioning as internal parts.
 Property specializes ParameterableElement to specify that a Property can be exposed as a formal template parameter, and provided as an actual parameter in a binding
 of a template.
 end-model-doc 
The following features are supported:
 [`*Aggregation*`](#getAggregation())
[`*Association End*`](#getAssociationEnd())
[`*Qualifier*`](#getQualifier())
[`*UML Class*`](#getUMLClass())
[`*Datatype*`](#getDatatype())
[`*Default Value*`](#getDefaultValue())
[`*Interface*`](#getInterface())
[`*Owning Signal*`](#getOwningSignal())
[`*structured Classifier Of Owned Attribute*`](#get_structuredClassifierOfOwnedAttribute())
[`*connector End Of Part With Port*`](#get_connectorEndOfPartWithPort())
[`*link End Data Of End*`](#get_linkEndDataOfEnd())
[`*qualifier Value Of Qualifier*`](#get_qualifierValueOfQualifier())
[`*read Link Object End Action Of End*`](#get_readLinkObjectEndActionOfEnd())
[`*read Link Object End Qualifier Action Of Qualifier*`](#get_readLinkObjectEndQualifierActionOfQualifier())
[`*Composite*`](#isComposite())
[`*Derived*`](#isDerived())
[`*Derived Union*`](#isDerivedUnion())
[`*ID*`](#isID())
[`*Opposite*`](#getOpposite())
[`*Owning Association*`](#getOwningAssociation())
[`*Redefined Property*`](#getRedefinedProperty())
[`*property Of Redefined Property*`](#get_propertyOfRedefinedProperty())
[`*Subsetted Property*`](#getSubsettedProperty())
[`*property Of Subsetted Property*`](#get_propertyOfSubsettedProperty())
[`*association Of Navigable Owned End*`](#get_associationOfNavigableOwnedEnd())
[`*artifact Of Owned Attribute*`](#get_artifactOfOwnedAttribute())
[`*Classifier*`](#getClassifier())
[`*interaction Use Of Return Value Recipient*`](#get_interactionUseOfReturnValueRecipient())
[`*Association*`](#getAssociation())

See Also:
[`UMLPackage.getProperty()`](../../metadata/UMLPackage.html#getProperty())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Artifact](../../deployments/mdartifacts/Artifact.html)`
`[get_artifactOfOwnedAttribute](#get_artifactOfOwnedAttribute())()`
Returns the value of the '***artifact Of Owned Attribute***' container reference.
`[Association](Association.html)`
`[get_associationOfNavigableOwnedEnd](#get_associationOfNavigableOwnedEnd())()`
Returns the value of the '***association Of Navigable Owned End***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ConnectorEnd](../../compositestructures/mdinternalstructures/ConnectorEnd.html)>`
`[get_connectorEndOfPartWithPort](#get_connectorEndOfPartWithPort())()`
Returns the value of the '***connector End Of Part With Port***' reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[TaggedValue](TaggedValue.html)>`
`[get_definedTaggedValue](#get_definedTaggedValue())()`
Returns the value of the '***Defined Tagged Value***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionUse](../../interactions/mdfragments/InteractionUse.html)>`
`[get_interactionUseOfReturnValueRecipient](#get_interactionUseOfReturnValueRecipient())()`
Returns the value of the '***interaction Use Of Return Value Recipient***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[LinkEndData](../../actions/mdintermediateactions/LinkEndData.html)>`
`[get_linkEndDataOfEnd](#get_linkEndDataOfEnd())()`
Returns the value of the '***link End Data Of End***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)>`
`[get_propertyOfRedefinedProperty](#get_propertyOfRedefinedProperty())()`
Returns the value of the '***property Of Redefined Property***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)>`
`[get_propertyOfSubsettedProperty](#get_propertyOfSubsettedProperty())()`
Returns the value of the '***property Of Subsetted Property***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[QualifierValue](../../actions/mdcompleteactions/QualifierValue.html)>`
`[get_qualifierValueOfQualifier](#get_qualifierValueOfQualifier())()`
Returns the value of the '***qualifier Value Of Qualifier***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ReadLinkObjectEndAction](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html)>`
`[get_readLinkObjectEndActionOfEnd](#get_readLinkObjectEndActionOfEnd())()`
Returns the value of the '***read Link Object End Action Of End***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ReadLinkObjectEndQualifierAction](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)>`
`[get_readLinkObjectEndQualifierActionOfQualifier](#get_readLinkObjectEndQualifierActionOfQualifier())()`
Returns the value of the '***read Link Object End Qualifier Action Of Qualifier***' reference list.
`[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`
`[get_structuredClassifierOfOwnedAttribute](#get_structuredClassifierOfOwnedAttribute())()`
Returns the value of the '***structured Classifier Of Owned Attribute***' container reference.
`[AggregationKind](AggregationKind.html)`
`[getAggregation](#getAggregation())()`
Returns the value of the '***Aggregation***' attribute.
`[Association](Association.html)`
`[getAssociation](#getAssociation())()`
Returns the value of the '***Association***' reference.
`[Property](Property.html)`
`[getAssociationEnd](#getAssociationEnd())()`
Returns the value of the '***Association End***' container reference.
`[Classifier](Classifier.html)`
`[getClassifier](#getClassifier())()`
Returns the value of the '***Classifier***' reference.
`[DataType](DataType.html)`
`[getDatatype](#getDatatype())()`
Returns the value of the '***Datatype***' container reference.
`[ValueSpecification](ValueSpecification.html)`
`[getDefaultValue](#getDefaultValue())()`
Returns the value of the '***Default Value***' containment reference.
`[Interface](../mdinterfaces/Interface.html)`
`[getInterface](#getInterface())()`
Returns the value of the '***Interface***' container reference.
`[Property](Property.html)`
`[getOpposite](#getOpposite())()`
Returns the value of the '***Opposite***' reference.
`[Association](Association.html)`
`[getOwningAssociation](#getOwningAssociation())()`
Returns the value of the '***Owning Association***' container reference.
`[Signal](../../commonbehaviors/mdcommunications/Signal.html)`
`[getOwningSignal](#getOwningSignal())()`
Returns the value of the '***Owning Signal***' container reference.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getQualifier](#getQualifier())()`
Returns the value of the '***Qualifier***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)>`
`[getRedefinedProperty](#getRedefinedProperty())()`
Returns the value of the '***Redefined Property***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)>`
`[getSubsettedProperty](#getSubsettedProperty())()`
Returns the value of the '***Subsetted Property***' reference list.
`[Class](Class.html)`
`[getUMLClass](#getUMLClass())()`
Returns the value of the '***UML Class***' container reference.
`boolean`
`[has_connectorEndOfPartWithPort](#has_connectorEndOfPartWithPort())()`

`boolean`
`[has_definedTaggedValue](#has_definedTaggedValue())()`

`boolean`
`[has_interactionUseOfReturnValueRecipient](#has_interactionUseOfReturnValueRecipient())()`

`boolean`
`[has_linkEndDataOfEnd](#has_linkEndDataOfEnd())()`

`boolean`
`[has_propertyOfRedefinedProperty](#has_propertyOfRedefinedProperty())()`

`boolean`
`[has_propertyOfSubsettedProperty](#has_propertyOfSubsettedProperty())()`

`boolean`
`[has_qualifierValueOfQualifier](#has_qualifierValueOfQualifier())()`

`boolean`
`[has_readLinkObjectEndActionOfEnd](#has_readLinkObjectEndActionOfEnd())()`

`boolean`
`[has_readLinkObjectEndQualifierActionOfQualifier](#has_readLinkObjectEndQualifierActionOfQualifier())()`

`boolean`
`[hasQualifier](#hasQualifier())()`

`boolean`
`[hasRedefinedProperty](#hasRedefinedProperty())()`

`boolean`
`[hasSubsettedProperty](#hasSubsettedProperty())()`

`boolean`
`[isComposite](#isComposite())()`
Returns the value of the '***Composite***' attribute.
`boolean`
`[isDerived](#isDerived())()`
Returns the value of the '***Derived***' attribute.
`boolean`
`[isDerivedUnion](#isDerivedUnion())()`
Returns the value of the '***Derived Union***' attribute.
`boolean`
`[isID](#isID())()`
Returns the value of the '***ID***' attribute.
`boolean`
`[isNavigable](#isNavigable())()`
The query isNavigable() indicates whether it is possible to navigate across the property.
`void`
`[set_artifactOfOwnedAttribute](#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact))([Artifact](../../deployments/mdartifacts/Artifact.html) value)`
Sets the value of the '[`*artifact Of Owned Attribute*`](#get_artifactOfOwnedAttribute())'
 container reference.
`void`
`[set_associationOfNavigableOwnedEnd](#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](Association.html) value)`
Sets the value of the
 '[`*association Of Navigable Owned End*`](#get_associationOfNavigableOwnedEnd())' reference.
`void`
`[set_structuredClassifierOfOwnedAttribute](#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier))([StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html) value)`
Sets the value of the '[`*structured Classifier Of
 Owned Attribute*`](#get_structuredClassifierOfOwnedAttribute())' container reference.
`void`
`[setAggregation](#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind))([AggregationKind](AggregationKind.html) value)`
Sets the value of the '[`*Aggregation*`](#getAggregation())' attribute.
`void`
`[setAssociation](#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](Association.html) value)`
Sets the value of the '[`*Association*`](#getAssociation())' reference.
`void`
`[setAssociationEnd](#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](Property.html) value)`
Sets the value of the '[`*Association End*`](#getAssociationEnd())' container reference.
`void`
`[setClassifier](#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](Classifier.html) value)`
Sets the value of the '[`*Classifier*`](#getClassifier())' reference.
`void`
`[setDatatype](#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType))([DataType](DataType.html) value)`
Sets the value of the '[`*Datatype*`](#getDatatype())' container reference.
`void`
`[setDefaultValue](#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](ValueSpecification.html) value)`
Sets the value of the '[`*Default Value*`](#getDefaultValue())' containment reference.
`void`
`[setDerived](#setDerived(boolean))(boolean value)`
Sets the value of the '[`*Derived*`](#isDerived())' attribute.
`void`
`[setDerivedUnion](#setDerivedUnion(boolean))(boolean value)`
Sets the value of the '[`*Derived Union*`](#isDerivedUnion())' attribute.
`void`
`[setID](#setID(boolean))(boolean value)`
Sets the value of the '[`*ID*`](#isID())' attribute.
`void`
`[setInterface](#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([Interface](../mdinterfaces/Interface.html) value)`
Sets the value of the '[`*Interface*`](#getInterface())' container reference.
`void`
`[setOwningAssociation](#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](Association.html) value)`
Sets the value of the '[`*Owning Association*`](#getOwningAssociation())' container reference.
`void`
`[setOwningSignal](#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal))([Signal](../../commonbehaviors/mdcommunications/Signal.html) value)`
Sets the value of the '[`*Owning Signal*`](#getOwningSignal())' container reference.
`void`
`[setUMLClass](#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](Class.html) value)`
Sets the value of the '[`*UML Class*`](#getUMLClass())' container reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)
`[get_collaborationOfCollaborationRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()), [get_lifelineOfRepresents](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()), [get_structuredClassifierOfRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()), [getEnd](../../compositestructures/mdinternalstructures/ConnectableElement.html#getEnd()), [getTemplateParameter](../../compositestructures/mdinternalstructures/ConnectableElement.html#getTemplateParameter()), [has_collaborationOfCollaborationRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()), [has_lifelineOfRepresents](../../compositestructures/mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()), [has_structuredClassifierOfRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()), [hasEnd](../../compositestructures/mdinternalstructures/ConnectableElement.html#hasEnd()), [setTemplateParameter](../../compositestructures/mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.[DeploymentTarget](../../deployments/mdnodes/DeploymentTarget.html)
`[getDeployedElement](../../deployments/mdnodes/DeploymentTarget.html#getDeployedElement()), [getDeployment](../../deployments/mdnodes/DeploymentTarget.html#getDeployment()), [hasDeployedElement](../../deployments/mdnodes/DeploymentTarget.html#hasDeployedElement()), [hasDeployment](../../deployments/mdnodes/DeploymentTarget.html#hasDeployment())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Feature](Feature.html)
`[getFeaturingClassifier](Feature.html#getFeaturingClassifier()), [isStatic](Feature.html#isStatic()), [setFeaturingClassifier](Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setStatic](Feature.html#setStatic(boolean))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[MultiplicityElement](MultiplicityElement.html)
`[getLower](MultiplicityElement.html#getLower()), [getLowerValue](MultiplicityElement.html#getLowerValue()), [getUpper](MultiplicityElement.html#getUpper()), [getUpperValue](MultiplicityElement.html#getUpperValue()), [isOrdered](MultiplicityElement.html#isOrdered()), [isUnique](MultiplicityElement.html#isUnique()), [setLowerValue](MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setOrdered](MultiplicityElement.html#setOrdered(boolean)), [setUnique](MultiplicityElement.html#setUnique(boolean)), [setUpperValue](MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](NamedElement.html#getClientDependency()), [getName](NamedElement.html#getName()), [getNameExpression](NamedElement.html#getNameExpression()), [getNamespace](NamedElement.html#getNamespace()), [getQualifiedName](NamedElement.html#getQualifiedName()), [getSupplierDependency](NamedElement.html#getSupplierDependency()), [getVisibility](NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](NamedElement.html#hasClientDependency()), [hasSupplierDependency](NamedElement.html#hasSupplierDependency()), [setName](NamedElement.html#setName(java.lang.String)), [setNameExpression](NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[StructuralFeature](StructuralFeature.html)
`[get_slotOfDefiningFeature](StructuralFeature.html#get_slotOfDefiningFeature()), [get_structuralFeatureActionOfStructuralFeature](StructuralFeature.html#get_structuralFeatureActionOfStructuralFeature()), [has_slotOfDefiningFeature](StructuralFeature.html#has_slotOfDefiningFeature()), [has_structuralFeatureActionOfStructuralFeature](StructuralFeature.html#has_structuralFeatureActionOfStructuralFeature()), [isReadOnly](StructuralFeature.html#isReadOnly()), [setReadOnly](StructuralFeature.html#setReadOnly(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](TypedElement.html)
`[getType](TypedElement.html#getType()), [setType](TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
getClassifier
@CheckForNull[Classifier](Classifier.html) getClassifier()
Returns the value of the '***Classifier***' reference.
 It is bidirectional and its opposite is '[`*Attribute*`](Classifier.html#getAttribute())'.
 begin-user-doc 
If the meaning of the '*Classifier*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Classifier*' reference.
See Also:
[`setClassifier(Classifier)`](#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
[`UMLPackage.getProperty_Classifier()`](../../metadata/UMLPackage.html#getProperty_Classifier())
[`Classifier.getAttribute()`](Classifier.html#getAttribute())
Model:
opposite="attribute" transient="true" volatile="true" derived="true" ordered="false"
Generated:
setClassifier
void setClassifier(@CheckForNull
 [Classifier](Classifier.html) value)
Sets the value of the '[`*Classifier*`](#getClassifier())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Classifier*' reference.
See Also:
[`getClassifier()`](#getClassifier())
Generated:
get_structuredClassifierOfOwnedAttribute
@CheckForNull[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html) get_structuredClassifierOfOwnedAttribute()
Returns the value of the '***structured Classifier Of Owned Attribute***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Attribute*`](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedAttribute())'.
 begin-user-doc 
If the meaning of the '*structured Classifier Of Owned Attribute*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*structured Classifier Of Owned Attribute*' container reference.
See Also:
[`set_structuredClassifierOfOwnedAttribute(StructuredClassifier)`](#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier))
[`UMLPackage.getProperty__structuredClassifierOfOwnedAttribute()`](../../metadata/UMLPackage.html#getProperty__structuredClassifierOfOwnedAttribute())
[`StructuredClassifier.getOwnedAttribute()`](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedAttribute())
Model:
opposite="ownedAttribute" transient="false" ordered="false"
Generated:
set_structuredClassifierOfOwnedAttribute
void set_structuredClassifierOfOwnedAttribute(@CheckForNull
 [StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html) value)
Sets the value of the '[`*structured Classifier Of
 Owned Attribute*`](#get_structuredClassifierOfOwnedAttribute())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*structured Classifier Of Owned Attribute*' container reference.
See Also:
[`get_structuredClassifierOfOwnedAttribute()`](#get_structuredClassifierOfOwnedAttribute())
Generated:
getOwningAssociation
@CheckForNull[Association](Association.html) getOwningAssociation()
Returns the value of the '***Owning Association***' container reference.
 It is bidirectional and its opposite is '[`*Owned End*`](Association.html#getOwnedEnd())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The owning association of this property, if any.
 end-model-doc
Returns:
the value of the '*Owning Association*' container reference.
See Also:
[`setOwningAssociation(Association)`](#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))
[`UMLPackage.getProperty_OwningAssociation()`](../../metadata/UMLPackage.html#getProperty_OwningAssociation())
[`Association.getOwnedEnd()`](Association.html#getOwnedEnd())
Model:
opposite="ownedEnd" transient="false" ordered="false"
Generated:
setOwningAssociation
void setOwningAssociation(@CheckForNull
 [Association](Association.html) value)
Sets the value of the '[`*Owning Association*`](#getOwningAssociation())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Association*' container reference.
See Also:
[`getOwningAssociation()`](#getOwningAssociation())
Generated:
getAssociation
@CheckForNull[Association](Association.html) getAssociation()
Returns the value of the '***Association***' reference.
 It is bidirectional and its opposite is '[`*Member End*`](Association.html#getMemberEnd())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Association of which this Property is a member, if any.
 end-model-doc
Returns:
the value of the '*Association*' reference.
See Also:
[`setAssociation(Association)`](#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))
[`UMLPackage.getProperty_Association()`](../../metadata/UMLPackage.html#getProperty_Association())
[`Association.getMemberEnd()`](Association.html#getMemberEnd())
Model:
opposite="memberEnd" ordered="false"
Generated:
setAssociation
void setAssociation(@CheckForNull
 [Association](Association.html) value)
Sets the value of the '[`*Association*`](#getAssociation())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Association*' reference.
See Also:
[`getAssociation()`](#getAssociation())
Generated:
get_associationOfNavigableOwnedEnd
@CheckForNull[Association](Association.html) get_associationOfNavigableOwnedEnd()
Returns the value of the '***association Of Navigable Owned End***' reference.
 It is bidirectional and its opposite is '[`*Navigable Owned End*`](Association.html#getNavigableOwnedEnd())'.
 begin-user-doc 
If the meaning of the '*association Of Navigable Owned End*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*association Of Navigable Owned End*' reference.
See Also:
[`set_associationOfNavigableOwnedEnd(Association)`](#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))
[`UMLPackage.getProperty__associationOfNavigableOwnedEnd()`](../../metadata/UMLPackage.html#getProperty__associationOfNavigableOwnedEnd())
[`Association.getNavigableOwnedEnd()`](Association.html#getNavigableOwnedEnd())
Model:
opposite="navigableOwnedEnd" ordered="false"
Generated:
set_associationOfNavigableOwnedEnd
void set_associationOfNavigableOwnedEnd(@CheckForNull
 [Association](Association.html) value)
Sets the value of the
 '[`*association Of Navigable Owned End*`](#get_associationOfNavigableOwnedEnd())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*association Of Navigable Owned End*' reference.
See Also:
[`get_associationOfNavigableOwnedEnd()`](#get_associationOfNavigableOwnedEnd())
Generated:
getOwningSignal
@CheckForNull[Signal](../../commonbehaviors/mdcommunications/Signal.html) getOwningSignal()
Returns the value of the '***Owning Signal***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Attribute*`](../../commonbehaviors/mdcommunications/Signal.html#getOwnedAttribute())'.
 begin-user-doc 
If the meaning of the '*Owning Signal*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Signal*' container reference.
See Also:
[`setOwningSignal(Signal)`](#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal))
[`UMLPackage.getProperty_OwningSignal()`](../../metadata/UMLPackage.html#getProperty_OwningSignal())
[`Signal.getOwnedAttribute()`](../../commonbehaviors/mdcommunications/Signal.html#getOwnedAttribute())
Model:
opposite="ownedAttribute" transient="false" ordered="false"
Generated:
setOwningSignal
void setOwningSignal(@CheckForNull
 [Signal](../../commonbehaviors/mdcommunications/Signal.html) value)
Sets the value of the '[`*Owning Signal*`](#getOwningSignal())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Signal*' container reference.
See Also:
[`getOwningSignal()`](#getOwningSignal())
Generated:
get_readLinkObjectEndActionOfEnd
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ReadLinkObjectEndAction](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html)> get_readLinkObjectEndActionOfEnd()
Returns the value of the '***read Link Object End Action Of End***' reference list.
 The list contents are of type [`ReadLinkObjectEndAction`](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html).
 It is bidirectional and its opposite is '[`*End*`](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html#getEnd())'.
 begin-user-doc 
If the meaning of the '*read Link Object End Action Of End*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Object End Action Of End*' reference list.
See Also:
[`UMLPackage.getProperty__readLinkObjectEndActionOfEnd()`](../../metadata/UMLPackage.html#getProperty__readLinkObjectEndActionOfEnd())
[`ReadLinkObjectEndAction.getEnd()`](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html#getEnd())
Model:
opposite="end" ordered="false"
Generated:
get_qualifierValueOfQualifier
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[QualifierValue](../../actions/mdcompleteactions/QualifierValue.html)> get_qualifierValueOfQualifier()
Returns the value of the '***qualifier Value Of Qualifier***' reference list.
 The list contents are of type [`QualifierValue`](../../actions/mdcompleteactions/QualifierValue.html).
 It is bidirectional and its opposite is '[`*Qualifier*`](../../actions/mdcompleteactions/QualifierValue.html#getQualifier())'.
 begin-user-doc 
If the meaning of the '*qualifier Value Of Qualifier*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*qualifier Value Of Qualifier*' reference list.
See Also:
[`UMLPackage.getProperty__qualifierValueOfQualifier()`](../../metadata/UMLPackage.html#getProperty__qualifierValueOfQualifier())
[`QualifierValue.getQualifier()`](../../actions/mdcompleteactions/QualifierValue.html#getQualifier())
Model:
opposite="qualifier" ordered="false"
Generated:
get_linkEndDataOfEnd
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[LinkEndData](../../actions/mdintermediateactions/LinkEndData.html)> get_linkEndDataOfEnd()
Returns the value of the '***link End Data Of End***' reference list.
 The list contents are of type [`LinkEndData`](../../actions/mdintermediateactions/LinkEndData.html).
 It is bidirectional and its opposite is '[`*End*`](../../actions/mdintermediateactions/LinkEndData.html#getEnd())'.
 begin-user-doc 
If the meaning of the '*link End Data Of End*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*link End Data Of End*' reference list.
See Also:
[`UMLPackage.getProperty__linkEndDataOfEnd()`](../../metadata/UMLPackage.html#getProperty__linkEndDataOfEnd())
[`LinkEndData.getEnd()`](../../actions/mdintermediateactions/LinkEndData.html#getEnd())
Model:
opposite="end" ordered="false"
Generated:
get_readLinkObjectEndQualifierActionOfQualifier
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ReadLinkObjectEndQualifierAction](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)> get_readLinkObjectEndQualifierActionOfQualifier()
Returns the value of the '***read Link Object End Qualifier Action Of Qualifier***' reference list.
 The list contents are of type [`ReadLinkObjectEndQualifierAction`](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html).
 It is bidirectional and its opposite is
 '[`*Qualifier*`](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getQualifier())'.
 begin-user-doc 
If the meaning of the '*read Link Object End Qualifier Action Of Qualifier*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Object End Qualifier Action Of Qualifier*' reference list.
See Also:
[`UMLPackage.getProperty__readLinkObjectEndQualifierActionOfQualifier()`](../../metadata/UMLPackage.html#getProperty__readLinkObjectEndQualifierActionOfQualifier())
[`ReadLinkObjectEndQualifierAction.getQualifier()`](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getQualifier())
Model:
opposite="qualifier" ordered="false"
Generated:
getUMLClass
@CheckForNull[Class](Class.html) getUMLClass()
Returns the value of the '***UML Class***' container reference.
 It is bidirectional and its opposite is '[`*Owned Attribute*`](Class.html#getOwnedAttribute())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Class that owns this Property, if any.
 end-model-doc
Returns:
the value of the '*UML Class*' container reference.
See Also:
[`setUMLClass(Class)`](#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))
[`UMLPackage.getProperty_UMLClass()`](../../metadata/UMLPackage.html#getProperty_UMLClass())
[`Class.getOwnedAttribute()`](Class.html#getOwnedAttribute())
Model:
opposite="ownedAttribute" volatile="true" ordered="false"
Generated:
setUMLClass
void setUMLClass(@CheckForNull
 [Class](Class.html) value)
Sets the value of the '[`*UML Class*`](#getUMLClass())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*UML Class*' container reference.
See Also:
[`getUMLClass()`](#getUMLClass())
Generated:
get_connectorEndOfPartWithPort
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ConnectorEnd](../../compositestructures/mdinternalstructures/ConnectorEnd.html)> get_connectorEndOfPartWithPort()
Returns the value of the '***connector End Of Part With Port***' reference list.
 The list contents are of type [`ConnectorEnd`](../../compositestructures/mdinternalstructures/ConnectorEnd.html).
 It is bidirectional and its opposite is
 '[`*Part With Port*`](../../compositestructures/mdinternalstructures/ConnectorEnd.html#getPartWithPort())'.
 begin-user-doc 
If the meaning of the '*connector End Of Part With Port*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*connector End Of Part With Port*' reference list.
See Also:
[`UMLPackage.getProperty__connectorEndOfPartWithPort()`](../../metadata/UMLPackage.html#getProperty__connectorEndOfPartWithPort())
[`ConnectorEnd.getPartWithPort()`](../../compositestructures/mdinternalstructures/ConnectorEnd.html#getPartWithPort())
Model:
opposite="partWithPort" ordered="false"
Generated:
getDatatype
@CheckForNull[DataType](DataType.html) getDatatype()
Returns the value of the '***Datatype***' container reference.
 It is bidirectional and its opposite is '[`*Owned Attribute*`](DataType.html#getOwnedAttribute())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The DataType that owns this Property, if any.
 end-model-doc
Returns:
the value of the '*Datatype*' container reference.
See Also:
[`setDatatype(DataType)`](#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType))
[`UMLPackage.getProperty_Datatype()`](../../metadata/UMLPackage.html#getProperty_Datatype())
[`DataType.getOwnedAttribute()`](DataType.html#getOwnedAttribute())
Model:
opposite="ownedAttribute" transient="false" ordered="false"
Generated:
setDatatype
void setDatatype(@CheckForNull
 [DataType](DataType.html) value)
Sets the value of the '[`*Datatype*`](#getDatatype())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Datatype*' container reference.
See Also:
[`getDatatype()`](#getDatatype())
Generated:
getInterface
@CheckForNull[Interface](../mdinterfaces/Interface.html) getInterface()
Returns the value of the '***Interface***' container reference.
 It is bidirectional and its opposite is '[`*Owned Attribute*`](../mdinterfaces/Interface.html#getOwnedAttribute())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Interface that owns this Property, if any.
 end-model-doc
Returns:
the value of the '*Interface*' container reference.
See Also:
[`setInterface(Interface)`](#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))
[`UMLPackage.getProperty_Interface()`](../../metadata/UMLPackage.html#getProperty_Interface())
[`Interface.getOwnedAttribute()`](../mdinterfaces/Interface.html#getOwnedAttribute())
Model:
opposite="ownedAttribute" transient="false" ordered="false"
Generated:
setInterface
void setInterface(@CheckForNull
 [Interface](../mdinterfaces/Interface.html) value)
Sets the value of the '[`*Interface*`](#getInterface())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Interface*' container reference.
See Also:
[`getInterface()`](#getInterface())
Generated:
get_artifactOfOwnedAttribute
@CheckForNull[Artifact](../../deployments/mdartifacts/Artifact.html) get_artifactOfOwnedAttribute()
Returns the value of the '***artifact Of Owned Attribute***' container reference.
 It is bidirectional and its opposite is '[`*Owned Attribute*`](../../deployments/mdartifacts/Artifact.html#getOwnedAttribute())'.
 begin-user-doc 
If the meaning of the '*artifact Of Owned Attribute*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*artifact Of Owned Attribute*' container reference.
See Also:
[`set_artifactOfOwnedAttribute(Artifact)`](#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact))
[`UMLPackage.getProperty__artifactOfOwnedAttribute()`](../../metadata/UMLPackage.html#getProperty__artifactOfOwnedAttribute())
[`Artifact.getOwnedAttribute()`](../../deployments/mdartifacts/Artifact.html#getOwnedAttribute())
Model:
opposite="ownedAttribute" transient="false" ordered="false"
Generated:
set_artifactOfOwnedAttribute
void set_artifactOfOwnedAttribute(@CheckForNull
 [Artifact](../../deployments/mdartifacts/Artifact.html) value)
Sets the value of the '[`*artifact Of Owned Attribute*`](#get_artifactOfOwnedAttribute())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*artifact Of Owned Attribute*' container reference.
See Also:
[`get_artifactOfOwnedAttribute()`](#get_artifactOfOwnedAttribute())
Generated:
get_interactionUseOfReturnValueRecipient
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InteractionUse](../../interactions/mdfragments/InteractionUse.html)> get_interactionUseOfReturnValueRecipient()
Returns the value of the '***interaction Use Of Return Value Recipient***' reference list.
 The list contents are of type [`InteractionUse`](../../interactions/mdfragments/InteractionUse.html).
 It is bidirectional and its opposite is
 '[`*Return Value Recipient*`](../../interactions/mdfragments/InteractionUse.html#getReturnValueRecipient())'.

 begin-user-doc 
If the meaning of the '*interaction Use Of Return Value Recipient*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Use Of Return Value Recipient*' reference list.
See Also:
[`UMLPackage.getProperty__interactionUseOfReturnValueRecipient()`](../../metadata/UMLPackage.html#getProperty__interactionUseOfReturnValueRecipient())
[`InteractionUse.getReturnValueRecipient()`](../../interactions/mdfragments/InteractionUse.html#getReturnValueRecipient())
Model:
opposite="returnValueRecipient" ordered="false"
Generated:
getAggregation
@CheckForNull[AggregationKind](AggregationKind.html) getAggregation()
Returns the value of the '***Aggregation***' attribute.
 The default value is `"none"`.
 The literals are from the enumeration [`AggregationKind`](AggregationKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the kind of aggregation that applies to the Property.
 end-model-doc
Returns:
the value of the '*Aggregation*' attribute.
See Also:
[`AggregationKind`](AggregationKind.html)
[`setAggregation(AggregationKind)`](#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind))
[`UMLPackage.getProperty_Aggregation()`](../../metadata/UMLPackage.html#getProperty_Aggregation())
Model:
default="none" required="true" ordered="false"
Generated:
setAggregation
void setAggregation(@CheckForNull
 [AggregationKind](AggregationKind.html) value)
Sets the value of the '[`*Aggregation*`](#getAggregation())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Aggregation*' attribute.
See Also:
[`AggregationKind`](AggregationKind.html)
[`getAggregation()`](#getAggregation())
Generated:
getRedefinedProperty
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> getRedefinedProperty()
Returns the value of the '***Redefined Property***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is
 '[`*property Of Redefined Property*`](#get_propertyOfRedefinedProperty())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The properties that are redefined by this property, if any.
 end-model-doc
Returns:
the value of the '*Redefined Property*' reference list.
See Also:
[`UMLPackage.getProperty_RedefinedProperty()`](../../metadata/UMLPackage.html#getProperty_RedefinedProperty())
[`get_propertyOfRedefinedProperty()`](#get_propertyOfRedefinedProperty())
Model:
opposite="_propertyOfRedefinedProperty" ordered="false"
Generated:
get_propertyOfRedefinedProperty
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> get_propertyOfRedefinedProperty()
Returns the value of the '***property Of Redefined Property***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*Redefined Property*`](#getRedefinedProperty())'.
 begin-user-doc 
If the meaning of the '*property Of Redefined Property*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*property Of Redefined Property*' reference list.
See Also:
[`UMLPackage.getProperty__propertyOfRedefinedProperty()`](../../metadata/UMLPackage.html#getProperty__propertyOfRedefinedProperty())
[`getRedefinedProperty()`](#getRedefinedProperty())
Model:
opposite="redefinedProperty" ordered="false"
Generated:
getDefaultValue
@CheckForNull[ValueSpecification](ValueSpecification.html) getDefaultValue()
Returns the value of the '***Default Value***' containment reference.
 It is bidirectional and its opposite is '[`*Owning Property*`](ValueSpecification.html#getOwningProperty())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A ValueSpecification that is evaluated to give a default value for the Property when an instance of the owning Classifier is instantiated.
 end-model-doc
Returns:
the value of the '*Default Value*' containment reference.
See Also:
[`setDefaultValue(ValueSpecification)`](#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getProperty_DefaultValue()`](../../metadata/UMLPackage.html#getProperty_DefaultValue())
[`ValueSpecification.getOwningProperty()`](ValueSpecification.html#getOwningProperty())
Model:
opposite="owningProperty" containment="true" resolveProxies="true" ordered="false"
Generated:
setDefaultValue
void setDefaultValue(@CheckForNull
 [ValueSpecification](ValueSpecification.html) value)
Sets the value of the '[`*Default Value*`](#getDefaultValue())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Default Value*' containment reference.
See Also:
[`getDefaultValue()`](#getDefaultValue())
Generated:
isComposite
boolean isComposite()
Returns the value of the '***Composite***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If isComposite is true, the object containing the attribute is a container for the object or value contained in the attribute. This is a derived value,
 indicating whether the aggregation of the Property is composite or not.
 end-model-doc
Returns:
the value of the '*Composite*' attribute.
See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_Composite()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true"
 ordered="false"
Generated:
isDerived
boolean isDerived()
Returns the value of the '***Derived***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether the Property is derived, i.e., whether its value or values can be computed from other information.
 end-model-doc
Returns:
the value of the '*Derived*' attribute.
See Also:
[`setDerived(boolean)`](#setDerived(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_Derived()`
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
isDerivedUnion
boolean isDerivedUnion()
Returns the value of the '***Derived Union***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether the property is derived as the union of all of the Properties that are constrained to subset it.
 end-model-doc
Returns:
the value of the '*Derived Union*' attribute.
See Also:
[`setDerivedUnion(boolean)`](#setDerivedUnion(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_DerivedUnion()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setDerivedUnion
void setDerivedUnion(boolean value)
Sets the value of the '[`*Derived Union*`](#isDerivedUnion())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Derived Union*' attribute.
See Also:
[`isDerivedUnion()`](#isDerivedUnion())
Generated:
isID
boolean isID()
Returns the value of the '***ID***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 True indicates this property can be used to uniquely identify an instance of the containing Class.
 end-model-doc
Returns:
the value of the '*ID*' attribute.
See Also:
[`setID(boolean)`](#setID(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_ID()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setID
void setID(boolean value)
Sets the value of the '[`*ID*`](#isID())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*ID*' attribute.
See Also:
[`isID()`](#isID())
Generated:
getOpposite
@CheckForNull[Property](Property.html) getOpposite()
Returns the value of the '***Opposite***' reference.
 It is bidirectional and its opposite is '`*property Of Opposite*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 In the case where the Property is one end of a binary association this gives the other end.
 end-model-doc
Returns:
the value of the '*Opposite*' reference.
See Also:
[`UMLPackage.getProperty_Opposite()`](../../metadata/UMLPackage.html#getProperty_Opposite())
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property#get_propertyOfOpposite`
Model:
opposite="_propertyOfOpposite" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getSubsettedProperty
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> getSubsettedProperty()
Returns the value of the '***Subsetted Property***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is
 '[`*property Of Subsetted Property*`](#get_propertyOfSubsettedProperty())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The properties of which this Property is constrained to be a subset, if any.
 end-model-doc
Returns:
the value of the '*Subsetted Property*' reference list.
See Also:
[`UMLPackage.getProperty_SubsettedProperty()`](../../metadata/UMLPackage.html#getProperty_SubsettedProperty())
[`get_propertyOfSubsettedProperty()`](#get_propertyOfSubsettedProperty())
Model:
opposite="_propertyOfSubsettedProperty" ordered="false"
Generated:
get_propertyOfSubsettedProperty
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> get_propertyOfSubsettedProperty()
Returns the value of the '***property Of Subsetted Property***' reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*Subsetted Property*`](#getSubsettedProperty())'.
 begin-user-doc 
If the meaning of the '*property Of Subsetted Property*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*property Of Subsetted Property*' reference list.
See Also:
[`UMLPackage.getProperty__propertyOfSubsettedProperty()`](../../metadata/UMLPackage.html#getProperty__propertyOfSubsettedProperty())
[`getSubsettedProperty()`](#getSubsettedProperty())
Model:
opposite="subsettedProperty" ordered="false"
Generated:
getQualifier
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getQualifier()
Returns the value of the '***Qualifier***' containment reference list.
 The list contents are of type [`Property`](Property.html).
 It is bidirectional and its opposite is '[`*Association End*`](#getAssociationEnd())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional list of ordered qualifier attributes for the end.
 end-model-doc
Returns:
the value of the '*Qualifier*' containment reference list.
See Also:
[`UMLPackage.getProperty_Qualifier()`](../../metadata/UMLPackage.html#getProperty_Qualifier())
[`getAssociationEnd()`](#getAssociationEnd())
Model:
opposite="associationEnd" containment="true" resolveProxies="true"
Generated:
getAssociationEnd
@CheckForNull[Property](Property.html) getAssociationEnd()
Returns the value of the '***Association End***' container reference.
 It is bidirectional and its opposite is '[`*Qualifier*`](#getQualifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Designates the optional association end that owns a qualifier attribute.
 end-model-doc
Returns:
the value of the '*Association End*' container reference.
See Also:
[`setAssociationEnd(Property)`](#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))
[`UMLPackage.getProperty_AssociationEnd()`](../../metadata/UMLPackage.html#getProperty_AssociationEnd())
[`getQualifier()`](#getQualifier())
Model:
opposite="qualifier" transient="false" ordered="false"
Generated:
setAssociationEnd
void setAssociationEnd(@CheckForNull
 [Property](Property.html) value)
Sets the value of the '[`*Association End*`](#getAssociationEnd())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Association End*' container reference.
See Also:
[`getAssociationEnd()`](#getAssociationEnd())
Generated:
get_definedTaggedValue
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[TaggedValue](TaggedValue.html)> get_definedTaggedValue()
Returns the value of the '***Defined Tagged Value***' reference list.
 The list contents are of type [`TaggedValue`](TaggedValue.html).
 It is bidirectional and its opposite is '[`*Tag Definition*`](TaggedValue.html#getTagDefinition())'.
 begin-user-doc 
 end-user-doc
Returns:
the value of the '*Defined Tagged Value*' reference list.
See Also:
[`UMLPackage.getProperty__definedTaggedValue()`](../../metadata/UMLPackage.html#getProperty__definedTaggedValue())
[`TaggedValue.getTagDefinition()`](TaggedValue.html#getTagDefinition())
Model:
opposite="tagDefinition"
Generated:
has_definedTaggedValue
boolean has_definedTaggedValue()
isNavigable
boolean isNavigable()
begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The query isNavigable() indicates whether it is possible to navigate across the property.
 end-model-doc
Model:
kind="operation" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
has_qualifierValueOfQualifier
boolean has_qualifierValueOfQualifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_readLinkObjectEndActionOfEnd
boolean has_readLinkObjectEndActionOfEnd()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_readLinkObjectEndQualifierActionOfQualifier
boolean has_readLinkObjectEndQualifierActionOfQualifier()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_interactionUseOfReturnValueRecipient
boolean has_interactionUseOfReturnValueRecipient()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_linkEndDataOfEnd
boolean has_linkEndDataOfEnd()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_connectorEndOfPartWithPort
boolean has_connectorEndOfPartWithPort()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedProperty
boolean hasRedefinedProperty()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_propertyOfRedefinedProperty
boolean has_propertyOfRedefinedProperty()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasSubsettedProperty
boolean hasSubsettedProperty()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_propertyOfSubsettedProperty
boolean has_propertyOfSubsettedProperty()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasQualifier
boolean hasQualifier()
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
<h1 class="title" title="Interface Property">Interface Property</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Property</span><span class="extends-implements">
extends <a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Property</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Property is a StructuralFeature. A Property related by ownedAttribute to a Classifier (other than an association) represents an attribute and might also represent
 an association end. It relates an instance of the Classifier to a value or set of values of the type of the attribute. A Property related by memberEnd to an
 Association represents an end of the Association. The type of the Property is the type of the end of the Association. A Property has the capability of being a
 DeploymentTarget in a Deployment relationship. This enables modeling the deployment to hierarchical nodes that have Properties functioning as internal parts.
 Property specializes ParameterableElement to specify that a Property can be exposed as a formal template parameter, and provided as an actual parameter in a binding
 of a template.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getAggregation()"><code><em>Aggregation</em></code></a></li>
<li><a href="#getAssociationEnd()"><code><em>Association End</em></code></a></li>
<li><a href="#getQualifier()"><code><em>Qualifier</em></code></a></li>
<li><a href="#getUMLClass()"><code><em>UML Class</em></code></a></li>
<li><a href="#getDatatype()"><code><em>Datatype</em></code></a></li>
<li><a href="#getDefaultValue()"><code><em>Default Value</em></code></a></li>
<li><a href="#getInterface()"><code><em>Interface</em></code></a></li>
<li><a href="#getOwningSignal()"><code><em>Owning Signal</em></code></a></li>
<li><a href="#get_structuredClassifierOfOwnedAttribute()"><code><em>structured Classifier Of Owned Attribute</em></code></a></li>
<li><a href="#get_connectorEndOfPartWithPort()"><code><em>connector End Of Part With Port</em></code></a></li>
<li><a href="#get_linkEndDataOfEnd()"><code><em>link End Data Of End</em></code></a></li>
<li><a href="#get_qualifierValueOfQualifier()"><code><em>qualifier Value Of Qualifier</em></code></a></li>
<li><a href="#get_readLinkObjectEndActionOfEnd()"><code><em>read Link Object End Action Of End</em></code></a></li>
<li><a href="#get_readLinkObjectEndQualifierActionOfQualifier()"><code><em>read Link Object End Qualifier Action Of Qualifier</em></code></a></li>
<li><a href="#isComposite()"><code><em>Composite</em></code></a></li>
<li><a href="#isDerived()"><code><em>Derived</em></code></a></li>
<li><a href="#isDerivedUnion()"><code><em>Derived Union</em></code></a></li>
<li><a href="#isID()"><code><em>ID</em></code></a></li>
<li><a href="#getOpposite()"><code><em>Opposite</em></code></a></li>
<li><a href="#getOwningAssociation()"><code><em>Owning Association</em></code></a></li>
<li><a href="#getRedefinedProperty()"><code><em>Redefined Property</em></code></a></li>
<li><a href="#get_propertyOfRedefinedProperty()"><code><em>property Of Redefined Property</em></code></a></li>
<li><a href="#getSubsettedProperty()"><code><em>Subsetted Property</em></code></a></li>
<li><a href="#get_propertyOfSubsettedProperty()"><code><em>property Of Subsetted Property</em></code></a></li>
<li><a href="#get_associationOfNavigableOwnedEnd()"><code><em>association Of Navigable Owned End</em></code></a></li>
<li><a href="#get_artifactOfOwnedAttribute()"><code><em>artifact Of Owned Attribute</em></code></a></li>
<li><a href="#getClassifier()"><code><em>Classifier</em></code></a></li>
<li><a href="#get_interactionUseOfReturnValueRecipient()"><code><em>interaction Use Of Return Value Recipient</em></code></a></li>
<li><a href="#getAssociation()"><code><em>Association</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getProperty()"><code>UMLPackage.getProperty()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_artifactOfOwnedAttribute()">get_artifactOfOwnedAttribute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>artifact Of Owned Attribute</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_associationOfNavigableOwnedEnd()">get_associationOfNavigableOwnedEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>association Of Navigable Owned End</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_connectorEndOfPartWithPort()">get_connectorEndOfPartWithPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>connector End Of Part With Port</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_definedTaggedValue()">get_definedTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Defined Tagged Value</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionUseOfReturnValueRecipient()">get_interactionUseOfReturnValueRecipient</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Use Of Return Value Recipient</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_linkEndDataOfEnd()">get_linkEndDataOfEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>link End Data Of End</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_propertyOfRedefinedProperty()">get_propertyOfRedefinedProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>property Of Redefined Property</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_propertyOfSubsettedProperty()">get_propertyOfSubsettedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>property Of Subsetted Property</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_qualifierValueOfQualifier()">get_qualifierValueOfQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>qualifier Value Of Qualifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkObjectEndActionOfEnd()">get_readLinkObjectEndActionOfEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Object End Action Of End</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkObjectEndQualifierActionOfQualifier()">get_readLinkObjectEndQualifierActionOfQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Object End Qualifier Action Of Qualifier</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_structuredClassifierOfOwnedAttribute()">get_structuredClassifierOfOwnedAttribute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>structured Classifier Of Owned Attribute</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAggregation()">getAggregation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Aggregation</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAssociation()">getAssociation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Association</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAssociationEnd()">getAssociationEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Association End</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClassifier()">getClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Classifier</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDatatype()">getDatatype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Datatype</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultValue()">getDefaultValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Default Value</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInterface()">getInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Interface</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOpposite()">getOpposite</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Opposite</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningAssociation()">getOwningAssociation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Association</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningSignal()">getOwningSignal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Signal</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getQualifier()">getQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Qualifier</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedProperty()">getRedefinedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Property</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSubsettedProperty()">getSubsettedProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Subsetted Property</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUMLClass()">getUMLClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>UML Class</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_connectorEndOfPartWithPort()">has_connectorEndOfPartWithPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_definedTaggedValue()">has_definedTaggedValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_interactionUseOfReturnValueRecipient()">has_interactionUseOfReturnValueRecipient</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_linkEndDataOfEnd()">has_linkEndDataOfEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_propertyOfRedefinedProperty()">has_propertyOfRedefinedProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_propertyOfSubsettedProperty()">has_propertyOfSubsettedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_qualifierValueOfQualifier()">has_qualifierValueOfQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_readLinkObjectEndActionOfEnd()">has_readLinkObjectEndActionOfEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_readLinkObjectEndQualifierActionOfQualifier()">has_readLinkObjectEndQualifierActionOfQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasQualifier()">hasQualifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedProperty()">hasRedefinedProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSubsettedProperty()">hasSubsettedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isComposite()">isComposite</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Composite</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDerived()">isDerived</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Derived</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDerivedUnion()">isDerivedUnion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Derived Union</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isID()">isID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>ID</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isNavigable()">isNavigable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The query isNavigable() indicates whether it is possible to navigate across the property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">set_artifactOfOwnedAttribute</a><wbr/>(<a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_artifactOfOwnedAttribute()"><code><em>artifact Of Owned Attribute</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">set_associationOfNavigableOwnedEnd</a><wbr/>(<a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_associationOfNavigableOwnedEnd()"><code><em>association Of Navigable Owned End</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">set_structuredClassifierOfOwnedAttribute</a><wbr/>(<a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_structuredClassifierOfOwnedAttribute()"><code><em>structured Classifier Of
 Owned Attribute</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">setAggregation</a><wbr/>(<a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getAggregation()"><code><em>Aggregation</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setAssociation</a><wbr/>(<a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getAssociation()"><code><em>Association</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setAssociationEnd</a><wbr/>(<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getAssociationEnd()"><code><em>Association End</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setClassifier</a><wbr/>(<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getClassifier()"><code><em>Classifier</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">setDatatype</a><wbr/>(<a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDatatype()"><code><em>Datatype</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setDefaultValue</a><wbr/>(<a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDefaultValue()"><code><em>Default Value</em></code></a>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDerived(boolean)">setDerived</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isDerived()"><code><em>Derived</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDerivedUnion(boolean)">setDerivedUnion</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isDerivedUnion()"><code><em>Derived Union</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setID(boolean)">setID</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isID()"><code><em>ID</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">setInterface</a><wbr/>(<a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInterface()"><code><em>Interface</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setOwningAssociation</a><wbr/>(<a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningAssociation()"><code><em>Owning Association</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">setOwningSignal</a><wbr/>(<a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningSignal()"><code><em>Owning Signal</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a><wbr/>(<a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUMLClass()"><code><em>UML Class</em></code></a>' container reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></h3>
<code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()">get_collaborationOfCollaborationRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()">get_lifelineOfRepresents</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()">get_structuredClassifierOfRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#getEnd()">getEnd</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()">has_collaborationOfCollaborationRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()">has_lifelineOfRepresents</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()">has_structuredClassifierOfRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#hasEnd()">hasEnd</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.DeploymentTarget">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.deployments.mdnodes.<a href="../../deployments/mdnodes/DeploymentTarget.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">DeploymentTarget</a></h3>
<code><a href="../../deployments/mdnodes/DeploymentTarget.html#getDeployedElement()">getDeployedElement</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html#getDeployment()">getDeployment</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html#hasDeployedElement()">hasDeployedElement</a>, <a href="../../deployments/mdnodes/DeploymentTarget.html#hasDeployment()">hasDeployment</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></h3>
<code><a href="Feature.html#getFeaturingClassifier()">getFeaturingClassifier</a>, <a href="Feature.html#isStatic()">isStatic</a>, <a href="Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setFeaturingClassifier</a>, <a href="Feature.html#setStatic(boolean)">setStatic</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></h3>
<code><a href="MultiplicityElement.html#getLower()">getLower</a>, <a href="MultiplicityElement.html#getLowerValue()">getLowerValue</a>, <a href="MultiplicityElement.html#getUpper()">getUpper</a>, <a href="MultiplicityElement.html#getUpperValue()">getUpperValue</a>, <a href="MultiplicityElement.html#isOrdered()">isOrdered</a>, <a href="MultiplicityElement.html#isUnique()">isUnique</a>, <a href="MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setLowerValue</a>, <a href="MultiplicityElement.html#setOrdered(boolean)">setOrdered</a>, <a href="MultiplicityElement.html#setUnique(boolean)">setUnique</a>, <a href="MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="NamedElement.html#getName()">getName</a>, <a href="NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="NamedElement.html#getNamespace()">getNamespace</a>, <a href="NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="NamedElement.html#getVisibility()">getVisibility</a>, <a href="NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="NamedElement.html#setName(java.lang.String)">setName</a>, <a href="NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></h3>
<code><a href="StructuralFeature.html#get_slotOfDefiningFeature()">get_slotOfDefiningFeature</a>, <a href="StructuralFeature.html#get_structuralFeatureActionOfStructuralFeature()">get_structuralFeatureActionOfStructuralFeature</a>, <a href="StructuralFeature.html#has_slotOfDefiningFeature()">has_slotOfDefiningFeature</a>, <a href="StructuralFeature.html#has_structuralFeatureActionOfStructuralFeature()">has_structuralFeatureActionOfStructuralFeature</a>, <a href="StructuralFeature.html#isReadOnly()">isReadOnly</a>, <a href="StructuralFeature.html#setReadOnly(boolean)">setReadOnly</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></h3>
<code><a href="TypedElement.html#getType()">getType</a>, <a href="TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a></code></div>
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
<section class="detail" id="getClassifier()">
<h3>getClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Classifier</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Classifier.html#getAttribute()"><code><em>Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Classifier</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Classifier</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>setClassifier(Classifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_Classifier()"><code>UMLPackage.getProperty_Classifier()</code></a></li>
<li><a href="Classifier.html#getAttribute()"><code>Classifier.getAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="attribute" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>setClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getClassifier()"><code><em>Classifier</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Classifier</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getClassifier()"><code>getClassifier()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_structuredClassifierOfOwnedAttribute()">
<h3>get_structuredClassifierOfOwnedAttribute</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></span> <span class="element-name">get_structuredClassifierOfOwnedAttribute</span>()</div>
<div class="block">Returns the value of the '<em><b>structured Classifier Of Owned Attribute</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>structured Classifier Of Owned Attribute</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>structured Classifier Of Owned Attribute</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)"><code>set_structuredClassifierOfOwnedAttribute(StructuredClassifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty__structuredClassifierOfOwnedAttribute()"><code>UMLPackage.getProperty__structuredClassifierOfOwnedAttribute()</code></a></li>
<li><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedAttribute()"><code>StructuredClassifier.getOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedAttribute" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_structuredClassifierOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">
<h3>set_structuredClassifierOfOwnedAttribute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_structuredClassifierOfOwnedAttribute</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_structuredClassifierOfOwnedAttribute()"><code><em>structured Classifier Of
 Owned Attribute</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>structured Classifier Of Owned Attribute</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_structuredClassifierOfOwnedAttribute()"><code>get_structuredClassifierOfOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningAssociation()">
<h3>getOwningAssociation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">getOwningAssociation</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Association</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Association.html#getOwnedEnd()"><code><em>Owned End</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The owning association of this property, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Association</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)"><code>setOwningAssociation(Association)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_OwningAssociation()"><code>UMLPackage.getProperty_OwningAssociation()</code></a></li>
<li><a href="Association.html#getOwnedEnd()"><code>Association.getOwnedEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedEnd" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>setOwningAssociation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningAssociation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningAssociation()"><code><em>Owning Association</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Association</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningAssociation()"><code>getOwningAssociation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociation()">
<h3>getAssociation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">getAssociation</span>()</div>
<div class="block">Returns the value of the '<em><b>Association</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Association.html#getMemberEnd()"><code><em>Member End</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Association of which this Property is a member, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Association</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)"><code>setAssociation(Association)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_Association()"><code>UMLPackage.getProperty_Association()</code></a></li>
<li><a href="Association.html#getMemberEnd()"><code>Association.getMemberEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="memberEnd" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>setAssociation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAssociation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getAssociation()"><code><em>Association</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Association</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getAssociation()"><code>getAssociation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_associationOfNavigableOwnedEnd()">
<h3>get_associationOfNavigableOwnedEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">get_associationOfNavigableOwnedEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>association Of Navigable Owned End</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Association.html#getNavigableOwnedEnd()"><code><em>Navigable Owned End</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>association Of Navigable Owned End</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>association Of Navigable Owned End</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)"><code>set_associationOfNavigableOwnedEnd(Association)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty__associationOfNavigableOwnedEnd()"><code>UMLPackage.getProperty__associationOfNavigableOwnedEnd()</code></a></li>
<li><a href="Association.html#getNavigableOwnedEnd()"><code>Association.getNavigableOwnedEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="navigableOwnedEnd" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_associationOfNavigableOwnedEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>set_associationOfNavigableOwnedEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_associationOfNavigableOwnedEnd</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_associationOfNavigableOwnedEnd()"><code><em>association Of Navigable Owned End</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>association Of Navigable Owned End</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_associationOfNavigableOwnedEnd()"><code>get_associationOfNavigableOwnedEnd()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningSignal()">
<h3>getOwningSignal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">getOwningSignal</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Signal</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdcommunications/Signal.html#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Signal</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Signal</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)"><code>setOwningSignal(Signal)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_OwningSignal()"><code>UMLPackage.getProperty_OwningSignal()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/Signal.html#getOwnedAttribute()"><code>Signal.getOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedAttribute" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">
<h3>setOwningSignal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningSignal</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningSignal()"><code><em>Owning Signal</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Signal</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningSignal()"><code>getOwningSignal()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkObjectEndActionOfEnd()">
<h3>get_readLinkObjectEndActionOfEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a>&gt;</span> <span class="element-name">get_readLinkObjectEndActionOfEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Object End Action Of End</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html#getEnd()"><code><em>End</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Object End Action Of End</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Object End Action Of End</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__readLinkObjectEndActionOfEnd()"><code>UMLPackage.getProperty__readLinkObjectEndActionOfEnd()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html#getEnd()"><code>ReadLinkObjectEndAction.getEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="end" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_qualifierValueOfQualifier()">
<h3>get_qualifierValueOfQualifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a>&gt;</span> <span class="element-name">get_qualifierValueOfQualifier</span>()</div>
<div class="block">Returns the value of the '<em><b>qualifier Value Of Qualifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdcompleteactions/QualifierValue.html#getQualifier()"><code><em>Qualifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>qualifier Value Of Qualifier</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>qualifier Value Of Qualifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__qualifierValueOfQualifier()"><code>UMLPackage.getProperty__qualifierValueOfQualifier()</code></a></li>
<li><a href="../../actions/mdcompleteactions/QualifierValue.html#getQualifier()"><code>QualifierValue.getQualifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="qualifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_linkEndDataOfEnd()">
<h3>get_linkEndDataOfEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a>&gt;</span> <span class="element-name">get_linkEndDataOfEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>link End Data Of End</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions"><code>LinkEndData</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdintermediateactions/LinkEndData.html#getEnd()"><code><em>End</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>link End Data Of End</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>link End Data Of End</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__linkEndDataOfEnd()"><code>UMLPackage.getProperty__linkEndDataOfEnd()</code></a></li>
<li><a href="../../actions/mdintermediateactions/LinkEndData.html#getEnd()"><code>LinkEndData.getEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="end" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkObjectEndQualifierActionOfQualifier()">
<h3>get_readLinkObjectEndQualifierActionOfQualifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a>&gt;</span> <span class="element-name">get_readLinkObjectEndQualifierActionOfQualifier</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Object End Qualifier Action Of Qualifier</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReadLinkObjectEndQualifierAction</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getQualifier()"><code><em>Qualifier</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Object End Qualifier Action Of Qualifier</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Object End Qualifier Action Of Qualifier</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__readLinkObjectEndQualifierActionOfQualifier()"><code>UMLPackage.getProperty__readLinkObjectEndQualifierActionOfQualifier()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getQualifier()"><code>ReadLinkObjectEndQualifierAction.getQualifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="qualifier" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLClass()">
<h3>getUMLClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getUMLClass</span>()</div>
<div class="block">Returns the value of the '<em><b>UML Class</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Class.html#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Class that owns this Property, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>UML Class</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)"><code>setUMLClass(Class)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_UMLClass()"><code>UMLPackage.getProperty_UMLClass()</code></a></li>
<li><a href="Class.html#getOwnedAttribute()"><code>Class.getOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedAttribute" volatile="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>setUMLClass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUMLClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUMLClass()"><code><em>UML Class</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>UML Class</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getUMLClass()"><code>getUMLClass()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_connectorEndOfPartWithPort()">
<h3>get_connectorEndOfPartWithPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a>&gt;</span> <span class="element-name">get_connectorEndOfPartWithPort</span>()</div>
<div class="block">Returns the value of the '<em><b>connector End Of Part With Port</b></em>' reference list.
 The list contents are of type <a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html#getPartWithPort()"><code><em>Part With Port</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>connector End Of Part With Port</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>connector End Of Part With Port</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__connectorEndOfPartWithPort()"><code>UMLPackage.getProperty__connectorEndOfPartWithPort()</code></a></li>
<li><a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html#getPartWithPort()"><code>ConnectorEnd.getPartWithPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="partWithPort" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDatatype()">
<h3>getDatatype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">getDatatype</span>()</div>
<div class="block">Returns the value of the '<em><b>Datatype</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="DataType.html#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The DataType that owns this Property, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Datatype</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)"><code>setDatatype(DataType)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_Datatype()"><code>UMLPackage.getProperty_Datatype()</code></a></li>
<li><a href="DataType.html#getOwnedAttribute()"><code>DataType.getOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedAttribute" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">
<h3>setDatatype</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDatatype</span><wbr/><span class="parameters">(@CheckForNull
 <a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDatatype()"><code><em>Datatype</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Datatype</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getDatatype()"><code>getDatatype()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterface()">
<h3>getInterface</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></span> <span class="element-name">getInterface</span>()</div>
<div class="block">Returns the value of the '<em><b>Interface</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdinterfaces/Interface.html#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Interface that owns this Property, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Interface</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)"><code>setInterface(Interface)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_Interface()"><code>UMLPackage.getProperty_Interface()</code></a></li>
<li><a href="../mdinterfaces/Interface.html#getOwnedAttribute()"><code>Interface.getOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedAttribute" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>setInterface</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInterface</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInterface()"><code><em>Interface</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Interface</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getInterface()"><code>getInterface()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_artifactOfOwnedAttribute()">
<h3>get_artifactOfOwnedAttribute</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></span> <span class="element-name">get_artifactOfOwnedAttribute</span>()</div>
<div class="block">Returns the value of the '<em><b>artifact Of Owned Attribute</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../deployments/mdartifacts/Artifact.html#getOwnedAttribute()"><code><em>Owned Attribute</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>artifact Of Owned Attribute</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>artifact Of Owned Attribute</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)"><code>set_artifactOfOwnedAttribute(Artifact)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty__artifactOfOwnedAttribute()"><code>UMLPackage.getProperty__artifactOfOwnedAttribute()</code></a></li>
<li><a href="../../deployments/mdartifacts/Artifact.html#getOwnedAttribute()"><code>Artifact.getOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedAttribute" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_artifactOfOwnedAttribute(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">
<h3>set_artifactOfOwnedAttribute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_artifactOfOwnedAttribute</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_artifactOfOwnedAttribute()"><code><em>artifact Of Owned Attribute</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>artifact Of Owned Attribute</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_artifactOfOwnedAttribute()"><code>get_artifactOfOwnedAttribute()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionUseOfReturnValueRecipient()">
<h3>get_interactionUseOfReturnValueRecipient</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a>&gt;</span> <span class="element-name">get_interactionUseOfReturnValueRecipient</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Use Of Return Value Recipient</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>InteractionUse</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../interactions/mdfragments/InteractionUse.html#getReturnValueRecipient()"><code><em>Return Value Recipient</em></code></a>'.

 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Use Of Return Value Recipient</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Use Of Return Value Recipient</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__interactionUseOfReturnValueRecipient()"><code>UMLPackage.getProperty__interactionUseOfReturnValueRecipient()</code></a></li>
<li><a href="../../interactions/mdfragments/InteractionUse.html#getReturnValueRecipient()"><code>InteractionUse.getReturnValueRecipient()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="returnValueRecipient" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAggregation()">
<h3>getAggregation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a></span> <span class="element-name">getAggregation</span>()</div>
<div class="block">Returns the value of the '<em><b>Aggregation</b></em>' attribute.
 The default value is <code>"none"</code>.
 The literals are from the enumeration <a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>AggregationKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the kind of aggregation that applies to the Property.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Aggregation</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>AggregationKind</code></a></li>
<li><a href="#setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)"><code>setAggregation(AggregationKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_Aggregation()"><code>UMLPackage.getProperty_Aggregation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="none" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">
<h3>setAggregation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAggregation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getAggregation()"><code><em>Aggregation</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Aggregation</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>AggregationKind</code></a></li>
<li><a href="#getAggregation()"><code>getAggregation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedProperty()">
<h3>getRedefinedProperty</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getRedefinedProperty</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Property</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_propertyOfRedefinedProperty()"><code><em>property Of Redefined Property</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The properties that are redefined by this property, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Property</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty_RedefinedProperty()"><code>UMLPackage.getProperty_RedefinedProperty()</code></a></li>
<li><a href="#get_propertyOfRedefinedProperty()"><code>get_propertyOfRedefinedProperty()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_propertyOfRedefinedProperty" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_propertyOfRedefinedProperty()">
<h3>get_propertyOfRedefinedProperty</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">get_propertyOfRedefinedProperty</span>()</div>
<div class="block">Returns the value of the '<em><b>property Of Redefined Property</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="#getRedefinedProperty()"><code><em>Redefined Property</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>property Of Redefined Property</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>property Of Redefined Property</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__propertyOfRedefinedProperty()"><code>UMLPackage.getProperty__propertyOfRedefinedProperty()</code></a></li>
<li><a href="#getRedefinedProperty()"><code>getRedefinedProperty()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedProperty" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultValue()">
<h3>getDefaultValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getDefaultValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Default Value</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="ValueSpecification.html#getOwningProperty()"><code><em>Owning Property</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A ValueSpecification that is evaluated to give a default value for the Property when an instance of the owning Classifier is instantiated.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Default Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setDefaultValue(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_DefaultValue()"><code>UMLPackage.getProperty_DefaultValue()</code></a></li>
<li><a href="ValueSpecification.html#getOwningProperty()"><code>ValueSpecification.getOwningProperty()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningProperty" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setDefaultValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDefaultValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDefaultValue()"><code><em>Default Value</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Default Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getDefaultValue()"><code>getDefaultValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isComposite()">
<h3>isComposite</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isComposite</span>()</div>
<div class="block">Returns the value of the '<em><b>Composite</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If isComposite is true, the object containing the attribute is a container for the object or value contained in the attribute. This is a derived value,
 indicating whether the aggregation of the Property is composite or not.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Composite</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_Composite()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true"
 ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerived()">
<h3>isDerived</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDerived</span>()</div>
<div class="block">Returns the value of the '<em><b>Derived</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether the Property is derived, i.e., whether its value or values can be computed from other information.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Derived</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDerived(boolean)"><code>setDerived(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_Derived()</code></li>
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
<ul class="see-list">
<li><a href="#isDerived()"><code>isDerived()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDerivedUnion()">
<h3>isDerivedUnion</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDerivedUnion</span>()</div>
<div class="block">Returns the value of the '<em><b>Derived Union</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether the property is derived as the union of all of the Properties that are constrained to subset it.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Derived Union</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDerivedUnion(boolean)"><code>setDerivedUnion(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_DerivedUnion()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDerivedUnion(boolean)">
<h3>setDerivedUnion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDerivedUnion</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isDerivedUnion()"><code><em>Derived Union</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Derived Union</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isDerivedUnion()"><code>isDerivedUnion()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isID()">
<h3>isID</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isID</span>()</div>
<div class="block">Returns the value of the '<em><b>ID</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 True indicates this property can be used to uniquely identify an instance of the containing Class.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>ID</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setID(boolean)"><code>setID(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProperty_ID()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(boolean)">
<h3>setID</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isID()"><code><em>ID</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>ID</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isID()"><code>isID()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpposite()">
<h3>getOpposite</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getOpposite</span>()</div>
<div class="block">Returns the value of the '<em><b>Opposite</b></em>' reference.
 It is bidirectional and its opposite is '<code><em>property Of Opposite</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 In the case where the Property is one end of a binary association this gives the other end.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Opposite</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty_Opposite()"><code>UMLPackage.getProperty_Opposite()</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property#get_propertyOfOpposite</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_propertyOfOpposite" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubsettedProperty()">
<h3>getSubsettedProperty</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getSubsettedProperty</span>()</div>
<div class="block">Returns the value of the '<em><b>Subsetted Property</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_propertyOfSubsettedProperty()"><code><em>property Of Subsetted Property</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The properties of which this Property is constrained to be a subset, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Subsetted Property</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty_SubsettedProperty()"><code>UMLPackage.getProperty_SubsettedProperty()</code></a></li>
<li><a href="#get_propertyOfSubsettedProperty()"><code>get_propertyOfSubsettedProperty()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_propertyOfSubsettedProperty" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_propertyOfSubsettedProperty()">
<h3>get_propertyOfSubsettedProperty</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">get_propertyOfSubsettedProperty</span>()</div>
<div class="block">Returns the value of the '<em><b>property Of Subsetted Property</b></em>' reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="#getSubsettedProperty()"><code><em>Subsetted Property</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>property Of Subsetted Property</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>property Of Subsetted Property</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__propertyOfSubsettedProperty()"><code>UMLPackage.getProperty__propertyOfSubsettedProperty()</code></a></li>
<li><a href="#getSubsettedProperty()"><code>getSubsettedProperty()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="subsettedProperty" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifier()">
<h3>getQualifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt;</span> <span class="element-name">getQualifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Qualifier</b></em>' containment reference list.
 The list contents are of type <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Property</code></a>.
 It is bidirectional and its opposite is '<a href="#getAssociationEnd()"><code><em>Association End</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional list of ordered qualifier attributes for the end.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Qualifier</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty_Qualifier()"><code>UMLPackage.getProperty_Qualifier()</code></a></li>
<li><a href="#getAssociationEnd()"><code>getAssociationEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="associationEnd" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationEnd()">
<h3>getAssociationEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAssociationEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>Association End</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="#getQualifier()"><code><em>Qualifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Designates the optional association end that owns a qualifier attribute.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Association End</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)"><code>setAssociationEnd(Property)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getProperty_AssociationEnd()"><code>UMLPackage.getProperty_AssociationEnd()</code></a></li>
<li><a href="#getQualifier()"><code>getQualifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="qualifier" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAssociationEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>setAssociationEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAssociationEnd</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getAssociationEnd()"><code><em>Association End</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Association End</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getAssociationEnd()"><code>getAssociationEnd()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_definedTaggedValue()">
<h3>get_definedTaggedValue</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TaggedValue</a>&gt;</span> <span class="element-name">get_definedTaggedValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Defined Tagged Value</b></em>' reference list.
 The list contents are of type <a href="TaggedValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TaggedValue</code></a>.
 It is bidirectional and its opposite is '<a href="TaggedValue.html#getTagDefinition()"><code><em>Tag Definition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Defined Tagged Value</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getProperty__definedTaggedValue()"><code>UMLPackage.getProperty__definedTaggedValue()</code></a></li>
<li><a href="TaggedValue.html#getTagDefinition()"><code>TaggedValue.getTagDefinition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="tagDefinition"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_definedTaggedValue()">
<h3>has_definedTaggedValue</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_definedTaggedValue</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isNavigable()">
<h3>isNavigable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isNavigable</span>()</div>
<div class="block"><!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The query isNavigable() indicates whether it is possible to navigate across the property.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Model:</dt>
<dd>kind="operation" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_qualifierValueOfQualifier()">
<h3>has_qualifierValueOfQualifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_qualifierValueOfQualifier</span>()
                               throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_readLinkObjectEndActionOfEnd()">
<h3>has_readLinkObjectEndActionOfEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_readLinkObjectEndActionOfEnd</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_readLinkObjectEndQualifierActionOfQualifier()">
<h3>has_readLinkObjectEndQualifierActionOfQualifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_readLinkObjectEndQualifierActionOfQualifier</span>()
                                                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_interactionUseOfReturnValueRecipient()">
<h3>has_interactionUseOfReturnValueRecipient</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_interactionUseOfReturnValueRecipient</span>()
                                          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_linkEndDataOfEnd()">
<h3>has_linkEndDataOfEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_linkEndDataOfEnd</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_connectorEndOfPartWithPort()">
<h3>has_connectorEndOfPartWithPort</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_connectorEndOfPartWithPort</span>()
                                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedProperty()">
<h3>hasRedefinedProperty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedProperty</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_propertyOfRedefinedProperty()">
<h3>has_propertyOfRedefinedProperty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_propertyOfRedefinedProperty</span>()
                                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSubsettedProperty()">
<h3>hasSubsettedProperty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSubsettedProperty</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_propertyOfSubsettedProperty()">
<h3>has_propertyOfSubsettedProperty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_propertyOfSubsettedProperty</span>()
                                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasQualifier()">
<h3>hasQualifier</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasQualifier</span>()
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
