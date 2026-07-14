# JAVA OPENAPI: Connector (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/compositestructures/mdinternalstructures/Connector.html
- source_path: `com/nomagic/uml2/ext/magicdraw/compositestructures/mdinternalstructures/Connector.html`
- source_sha256: `e3f9f951282f39b8920d75de69259db4d92bfb0e1eb09c4f1da49cc2d6a2085e`
- captured_utc: `2026-07-14T16:52:59.286485+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures](package-summary.html)

## Interface Connector

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](../../classes/mdkernel/Feature.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceConnectorextends [Feature](../../classes/mdkernel/Feature.html)

begin-user-doc 
 A representation of the model object '***Connector***'.
 end-user-doc 
begin-model-doc 
 A Connector specifies links that enables communication between two or more instances. In contrast to Associations, which specify links between any instance of the
 associated Classifiers, Connectors specify links between instances playing the connected parts only.
 end-model-doc 
The following features are supported:
 [`*Contract*`](#getContract())
[`*End*`](#getEnd())
[`*Kind*`](#getKind())
[`*Redefined Connector*`](#getRedefinedConnector())
[`*connector Of Redefined Connector*`](#get_connectorOfRedefinedConnector())
[`*Type*`](#getType())
[`*message Of Connector*`](#get_messageOfConnector())
[`*information Flow Of Realizing Connector*`](#get_informationFlowOfRealizingConnector())
[`*structured Classifier Of Owned Connector*`](#get_structuredClassifierOfOwnedConnector())

See Also:
[`UMLPackage.getConnector()`](../../metadata/UMLPackage.html#getConnector())
Model:
annotation="MOF package='compositestructures.mdinternalstructures'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Connector](Connector.html)>`
`[get_connectorOfRedefinedConnector](#get_connectorOfRedefinedConnector())()`
Returns the value of the '***connector Of Redefined Connector***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)>`
`[get_informationFlowOfRealizingConnector](#get_informationFlowOfRealizingConnector())()`
Returns the value of the '***information Flow Of Realizing Connector***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Message](../../interactions/mdbasicinteractions/Message.html)>`
`[get_messageOfConnector](#get_messageOfConnector())()`
Returns the value of the '***message Of Connector***' reference list.
`[StructuredClassifier](StructuredClassifier.html)`
`[get_structuredClassifierOfOwnedConnector](#get_structuredClassifierOfOwnedConnector())()`
Returns the value of the '***structured Classifier Of Owned Connector***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)>`
`[getContract](#getContract())()`
Returns the value of the '***Contract***' reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ConnectorEnd](ConnectorEnd.html)>`
`[getEnd](#getEnd())()`
Returns the value of the '***End***' containment reference list.
`[ConnectorKind](../../components/mdbasiccomponents/ConnectorKind.html)`
`[getKind](#getKind())()`
Returns the value of the '***Kind***' attribute.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Connector](Connector.html)>`
`[getRedefinedConnector](#getRedefinedConnector())()`
Returns the value of the '***Redefined Connector***' reference list.
`[Association](../../classes/mdkernel/Association.html)`
`[getType](#getType())()`
Returns the value of the '***Type***' reference.
`boolean`
`[has_connectorOfRedefinedConnector](#has_connectorOfRedefinedConnector())()`

`boolean`
`[has_informationFlowOfRealizingConnector](#has_informationFlowOfRealizingConnector())()`

`boolean`
`[has_messageOfConnector](#has_messageOfConnector())()`

`boolean`
`[hasContract](#hasContract())()`

`boolean`
`[hasEnd](#hasEnd())()`

`boolean`
`[hasRedefinedConnector](#hasRedefinedConnector())()`

`void`
`[set_structuredClassifierOfOwnedConnector](#set_structuredClassifierOfOwnedConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier))([StructuredClassifier](StructuredClassifier.html) value)`
Sets the value of the '[`*structured Classifier Of Owned Connector*`](#get_structuredClassifierOfOwnedConnector())' container reference.
`void`
`[setType](#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../classes/mdkernel/Association.html) value)`
Sets the value of the '[`*Type*`](#getType())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Feature](../../classes/mdkernel/Feature.html)
`[getFeaturingClassifier](../../classes/mdkernel/Feature.html#getFeaturingClassifier()), [isStatic](../../classes/mdkernel/Feature.html#isStatic()), [setFeaturingClassifier](../../classes/mdkernel/Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setStatic](../../classes/mdkernel/Feature.html#setStatic(boolean))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getType
@CheckForNull[Association](../../classes/mdkernel/Association.html) getType()
Returns the value of the '***Type***' reference.
 It is bidirectional and its opposite is '[`*connector Of Type*`](../../classes/mdkernel/Association.html#get_connectorOfType())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional Association that classifies links corresponding to this Connector.
 end-model-doc
Returns:
the value of the '*Type*' reference.
See Also:
[`setType(Association)`](#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))
[`UMLPackage.getConnector_Type()`](../../metadata/UMLPackage.html#getConnector_Type())
[`Association.get_connectorOfType()`](../../classes/mdkernel/Association.html#get_connectorOfType())
Model:
opposite="_connectorOfType" ordered="false"
Generated:
setType
void setType(@CheckForNull
 [Association](../../classes/mdkernel/Association.html) value)
Sets the value of the '[`*Type*`](#getType())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Type*' reference.
See Also:
[`getType()`](#getType())
Generated:
get_messageOfConnector
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Message](../../interactions/mdbasicinteractions/Message.html)> get_messageOfConnector()
Returns the value of the '***message Of Connector***' reference list.
 The list contents are of type [`Message`](../../interactions/mdbasicinteractions/Message.html).
 It is bidirectional and its opposite is '[`*Connector*`](../../interactions/mdbasicinteractions/Message.html#getConnector())'.
 begin-user-doc 
If the meaning of the '*message Of Connector*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message Of Connector*' reference list.
See Also:
[`UMLPackage.getConnector__messageOfConnector()`](../../metadata/UMLPackage.html#getConnector__messageOfConnector())
[`Message.getConnector()`](../../interactions/mdbasicinteractions/Message.html#getConnector())
Model:
opposite="connector" ordered="false"
Generated:
get_informationFlowOfRealizingConnector
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)> get_informationFlowOfRealizingConnector()
Returns the value of the '***information Flow Of Realizing Connector***' reference list.
 The list contents are of type [`InformationFlow`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html).
 It is bidirectional and its opposite is
 '[`*Realizing Connector*`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingConnector())'.
 begin-user-doc 
If the meaning of the '*information Flow Of Realizing Connector*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Flow Of Realizing Connector*' reference list.
See Also:
[`UMLPackage.getConnector__informationFlowOfRealizingConnector()`](../../metadata/UMLPackage.html#getConnector__informationFlowOfRealizingConnector())
[`InformationFlow.getRealizingConnector()`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingConnector())
Model:
opposite="realizingConnector" ordered="false"
Generated:
getContract
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)> getContract()
Returns the value of the '***Contract***' reference list.
 The list contents are of type [`Behavior`](../../commonbehaviors/mdbasicbehaviors/Behavior.html).
 It is bidirectional and its opposite is
 '[`*connector Of Contract*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_connectorOfContract())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of Behaviors that specify the valid interaction patterns across the Connector.
 end-model-doc
Returns:
the value of the '*Contract*' reference list.
See Also:
[`UMLPackage.getConnector_Contract()`](../../metadata/UMLPackage.html#getConnector_Contract())
[`Behavior.get_connectorOfContract()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_connectorOfContract())
Model:
opposite="_connectorOfContract" ordered="false"
Generated:
getRedefinedConnector
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Connector](Connector.html)> getRedefinedConnector()
Returns the value of the '***Redefined Connector***' reference list.
 The list contents are of type [`Connector`](Connector.html).
 It is bidirectional and its opposite is '`.mdinternalstructures.Connector#get_connectorOfRedefinedConnector *connector Of Redefined Connector*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A Connector may be redefined when its containing Classifier is specialized. The redefining Connector may have a type that specializes the type of the redefined
 Connector. The types of the ConnectorEnds of the redefining Connector may specialize the types of the ConnectorEnds of the redefined Connector. The properties of
 the ConnectorEnds of the redefining Connector may be replaced.
 end-model-doc
Returns:
the value of the '*Redefined Connector*' reference list.
See Also:
[`UMLPackage.getConnector_RedefinedConnector()`](../../metadata/UMLPackage.html#getConnector_RedefinedConnector())
[`get_connectorOfRedefinedConnector()`](#get_connectorOfRedefinedConnector())
Model:
opposite="_connectorOfRedefinedConnector" ordered="false"
Generated:
get_connectorOfRedefinedConnector
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Connector](Connector.html)> get_connectorOfRedefinedConnector()
Returns the value of the '***connector Of Redefined Connector***' reference list.
 The list contents are of type [`Connector`](Connector.html).
 It is bidirectional and its opposite is
 '[`*Redefined Connector*`](#getRedefinedConnector())'.
 begin-user-doc 
If the meaning of the '*connector Of Redefined Connector*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*connector Of Redefined Connector*' reference list.
See Also:
[`UMLPackage.getConnector__connectorOfRedefinedConnector()`](../../metadata/UMLPackage.html#getConnector__connectorOfRedefinedConnector())
[`getRedefinedConnector()`](#getRedefinedConnector())
Model:
opposite="redefinedConnector" ordered="false"
Generated:
getEnd
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ConnectorEnd](ConnectorEnd.html)> getEnd()
Returns the value of the '***End***' containment reference list.
 The list contents are of type [`ConnectorEnd`](ConnectorEnd.html).
 It is bidirectional and its opposite is
 '[`*connector Of End*`](ConnectorEnd.html#get_connectorOfEnd())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A Connector has at least two ConnectorEnds, each representing the participation of instances of the Classifiers typing the ConnectableElements attached to the
 end. The set of ConnectorEnds is ordered.
 end-model-doc
Returns:
the value of the '*End*' containment reference list.
See Also:
[`UMLPackage.getConnector_End()`](../../metadata/UMLPackage.html#getConnector_End())
[`ConnectorEnd.get_connectorOfEnd()`](ConnectorEnd.html#get_connectorOfEnd())
Model:
opposite="_connectorOfEnd" containment="true" resolveProxies="true" lower="2"
Generated:
getKind
@CheckForNull[ConnectorKind](../../components/mdbasiccomponents/ConnectorKind.html) getKind()
Returns the value of the '***Kind***' attribute.
 The literals are from the enumeration [`ConnectorKind`](../../components/mdbasiccomponents/ConnectorKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates the kind of Connector. This is derived: a Connector with one or more ends connected to a Port which is not on a Part and which is not a behavior port
 is a delegation; otherwise it is an assembly.
 end-model-doc
Returns:
the value of the '*Kind*' attribute.
See Also:
[`ConnectorKind`](../../components/mdbasiccomponents/ConnectorKind.html)
[`UMLPackage.getConnector_Kind()`](../../metadata/UMLPackage.html#getConnector_Kind())
Model:
required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
get_structuredClassifierOfOwnedConnector
@CheckForNull[StructuredClassifier](StructuredClassifier.html) get_structuredClassifierOfOwnedConnector()
Returns the value of the '***structured Classifier Of Owned Connector***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Connector*`](StructuredClassifier.html#getOwnedConnector())'.
 begin-user-doc 
If the meaning of the '*structured Classifier Of Owned Connector*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*structured Classifier Of Owned Connector*' container reference.
See Also:
[`set_structuredClassifierOfOwnedConnector(StructuredClassifier)`](#set_structuredClassifierOfOwnedConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier))
[`UMLPackage.getConnector__structuredClassifierOfOwnedConnector()`](../../metadata/UMLPackage.html#getConnector__structuredClassifierOfOwnedConnector())
[`StructuredClassifier.getOwnedConnector()`](StructuredClassifier.html#getOwnedConnector())
Model:
opposite="ownedConnector" transient="false" ordered="false"
Generated:
set_structuredClassifierOfOwnedConnector
void set_structuredClassifierOfOwnedConnector(@CheckForNull
 [StructuredClassifier](StructuredClassifier.html) value)
Sets the value of the '[`*structured Classifier Of Owned Connector*`](#get_structuredClassifierOfOwnedConnector())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*structured Classifier Of Owned Connector*' container reference.
See Also:
[`get_structuredClassifierOfOwnedConnector()`](#get_structuredClassifierOfOwnedConnector())
Generated:
has_messageOfConnector
boolean has_messageOfConnector()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationFlowOfRealizingConnector
boolean has_informationFlowOfRealizingConnector()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasContract
boolean hasContract()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedConnector
boolean hasRedefinedConnector()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_connectorOfRedefinedConnector
boolean has_connectorOfRedefinedConnector()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasEnd
boolean hasEnd()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures</a></div>
<h1 class="title" title="Interface Connector">Interface Connector</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Connector</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Connector</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Connector specifies links that enables communication between two or more instances. In contrast to Associations, which specify links between any instance of the
 associated Classifiers, Connectors specify links between instances playing the connected parts only.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getContract()"><code><em>Contract</em></code></a></li>
<li><a href="#getEnd()"><code><em>End</em></code></a></li>
<li><a href="#getKind()"><code><em>Kind</em></code></a></li>
<li><a href="#getRedefinedConnector()"><code><em>Redefined Connector</em></code></a></li>
<li><a href="#get_connectorOfRedefinedConnector()"><code><em>connector Of Redefined Connector</em></code></a></li>
<li><a href="#getType()"><code><em>Type</em></code></a></li>
<li><a href="#get_messageOfConnector()"><code><em>message Of Connector</em></code></a></li>
<li><a href="#get_informationFlowOfRealizingConnector()"><code><em>information Flow Of Realizing Connector</em></code></a></li>
<li><a href="#get_structuredClassifierOfOwnedConnector()"><code><em>structured Classifier Of Owned Connector</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getConnector()"><code>UMLPackage.getConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='compositestructures.mdinternalstructures'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_connectorOfRedefinedConnector()">get_connectorOfRedefinedConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>connector Of Redefined Connector</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationFlowOfRealizingConnector()">get_informationFlowOfRealizingConnector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Flow Of Realizing Connector</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageOfConnector()">get_messageOfConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message Of Connector</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_structuredClassifierOfOwnedConnector()">get_structuredClassifierOfOwnedConnector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>structured Classifier Of Owned Connector</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContract()">getContract</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Contract</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEnd()">getEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>End</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../components/mdbasiccomponents/ConnectorKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ConnectorKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Kind</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedConnector()">getRedefinedConnector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Connector</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Type</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_connectorOfRedefinedConnector()">has_connectorOfRedefinedConnector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationFlowOfRealizingConnector()">has_informationFlowOfRealizingConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_messageOfConnector()">has_messageOfConnector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasContract()">hasContract</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEnd()">hasEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedConnector()">hasRedefinedConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_structuredClassifierOfOwnedConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">set_structuredClassifierOfOwnedConnector</a><wbr/>(<a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_structuredClassifierOfOwnedConnector()"><code><em>structured Classifier Of Owned Connector</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">setType</a><wbr/>(<a href="../../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getType()"><code><em>Type</em></code></a>' reference.</div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
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
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns the value of the '<em><b>Type</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/Association.html#get_connectorOfType()"><code><em>connector Of Type</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional Association that classifies links corresponding to this Connector.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Type</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)"><code>setType(Association)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConnector_Type()"><code>UMLPackage.getConnector_Type()</code></a></li>
<li><a href="../../classes/mdkernel/Association.html#get_connectorOfType()"><code>Association.get_connectorOfType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_connectorOfType" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>setType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getType()"><code><em>Type</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Type</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getType()"><code>getType()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageOfConnector()">
<h3>get_messageOfConnector</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</span> <span class="element-name">get_messageOfConnector</span>()</div>
<div class="block">Returns the value of the '<em><b>message Of Connector</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Message.html#getConnector()"><code><em>Connector</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message Of Connector</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message Of Connector</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnector__messageOfConnector()"><code>UMLPackage.getConnector__messageOfConnector()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Message.html#getConnector()"><code>Message.getConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="connector" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationFlowOfRealizingConnector()">
<h3>get_informationFlowOfRealizingConnector</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</span> <span class="element-name">get_informationFlowOfRealizingConnector</span>()</div>
<div class="block">Returns the value of the '<em><b>information Flow Of Realizing Connector</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingConnector()"><code><em>Realizing Connector</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Flow Of Realizing Connector</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Flow Of Realizing Connector</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnector__informationFlowOfRealizingConnector()"><code>UMLPackage.getConnector__informationFlowOfRealizingConnector()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingConnector()"><code>InformationFlow.getRealizingConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="realizingConnector" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContract()">
<h3>getContract</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt;</span> <span class="element-name">getContract</span>()</div>
<div class="block">Returns the value of the '<em><b>Contract</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_connectorOfContract()"><code><em>connector Of Contract</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of Behaviors that specify the valid interaction patterns across the Connector.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Contract</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnector_Contract()"><code>UMLPackage.getConnector_Contract()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_connectorOfContract()"><code>Behavior.get_connectorOfContract()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_connectorOfContract" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedConnector()">
<h3>getRedefinedConnector</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</span> <span class="element-name">getRedefinedConnector</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Connector</b></em>' reference list.
 The list contents are of type <a href="Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.
 It is bidirectional and its opposite is '<code>.mdinternalstructures.Connector#get_connectorOfRedefinedConnector <em>connector Of Redefined Connector</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A Connector may be redefined when its containing Classifier is specialized. The redefining Connector may have a type that specializes the type of the redefined
 Connector. The types of the ConnectorEnds of the redefining Connector may specialize the types of the ConnectorEnds of the redefined Connector. The properties of
 the ConnectorEnds of the redefining Connector may be replaced.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Connector</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnector_RedefinedConnector()"><code>UMLPackage.getConnector_RedefinedConnector()</code></a></li>
<li><a href="#get_connectorOfRedefinedConnector()"><code>get_connectorOfRedefinedConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_connectorOfRedefinedConnector" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_connectorOfRedefinedConnector()">
<h3>get_connectorOfRedefinedConnector</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</span> <span class="element-name">get_connectorOfRedefinedConnector</span>()</div>
<div class="block">Returns the value of the '<em><b>connector Of Redefined Connector</b></em>' reference list.
 The list contents are of type <a href="Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getRedefinedConnector()"><code><em>Redefined Connector</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>connector Of Redefined Connector</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>connector Of Redefined Connector</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnector__connectorOfRedefinedConnector()"><code>UMLPackage.getConnector__connectorOfRedefinedConnector()</code></a></li>
<li><a href="#getRedefinedConnector()"><code>getRedefinedConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedConnector" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnd()">
<h3>getEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a>&gt;</span> <span class="element-name">getEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>End</b></em>' containment reference list.
 The list contents are of type <a href="ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.
 It is bidirectional and its opposite is
 '<a href="ConnectorEnd.html#get_connectorOfEnd()"><code><em>connector Of End</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A Connector has at least two ConnectorEnds, each representing the participation of instances of the Classifiers typing the ConnectableElements attached to the
 end. The set of ConnectorEnds is ordered.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>End</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnector_End()"><code>UMLPackage.getConnector_End()</code></a></li>
<li><a href="ConnectorEnd.html#get_connectorOfEnd()"><code>ConnectorEnd.get_connectorOfEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_connectorOfEnd" containment="true" resolveProxies="true" lower="2"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../components/mdbasiccomponents/ConnectorKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ConnectorKind</a></span> <span class="element-name">getKind</span>()</div>
<div class="block">Returns the value of the '<em><b>Kind</b></em>' attribute.
 The literals are from the enumeration <a href="../../components/mdbasiccomponents/ConnectorKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ConnectorKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates the kind of Connector. This is derived: a Connector with one or more ends connected to a Port which is not on a Part and which is not a behavior port
 is a delegation; otherwise it is an assembly.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Kind</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../components/mdbasiccomponents/ConnectorKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents"><code>ConnectorKind</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConnector_Kind()"><code>UMLPackage.getConnector_Kind()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_structuredClassifierOfOwnedConnector()">
<h3>get_structuredClassifierOfOwnedConnector</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></span> <span class="element-name">get_structuredClassifierOfOwnedConnector</span>()</div>
<div class="block">Returns the value of the '<em><b>structured Classifier Of Owned Connector</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="StructuredClassifier.html#getOwnedConnector()"><code><em>Owned Connector</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>structured Classifier Of Owned Connector</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>structured Classifier Of Owned Connector</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_structuredClassifierOfOwnedConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)"><code>set_structuredClassifierOfOwnedConnector(StructuredClassifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConnector__structuredClassifierOfOwnedConnector()"><code>UMLPackage.getConnector__structuredClassifierOfOwnedConnector()</code></a></li>
<li><a href="StructuredClassifier.html#getOwnedConnector()"><code>StructuredClassifier.getOwnedConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedConnector" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_structuredClassifierOfOwnedConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier)">
<h3>set_structuredClassifierOfOwnedConnector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_structuredClassifierOfOwnedConnector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_structuredClassifierOfOwnedConnector()"><code><em>structured Classifier Of Owned Connector</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>structured Classifier Of Owned Connector</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_structuredClassifierOfOwnedConnector()"><code>get_structuredClassifierOfOwnedConnector()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_messageOfConnector()">
<h3>has_messageOfConnector</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_messageOfConnector</span>()
                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationFlowOfRealizingConnector()">
<h3>has_informationFlowOfRealizingConnector</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationFlowOfRealizingConnector</span>()
                                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasContract()">
<h3>hasContract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasContract</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedConnector()">
<h3>hasRedefinedConnector</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedConnector</span>()
                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_connectorOfRedefinedConnector()">
<h3>has_connectorOfRedefinedConnector</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_connectorOfRedefinedConnector</span>()
                                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasEnd()">
<h3>hasEnd</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasEnd</span>()
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
