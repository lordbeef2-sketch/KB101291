# JAVA OPENAPI: ConnectableElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html
- source_path: `com/nomagic/uml2/ext/magicdraw/compositestructures/mdinternalstructures/ConnectableElement.html`
- source_sha256: `afb9e137b144594888578b17e1281cf5fed3369f4f23d9b58b9926c3ecb452fb`
- captured_utc: `2026-07-14T16:56:24.141780+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures](package-summary.html)

## Interface ConnectableElement

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](../../classes/mdkernel/TypedElement.html)`

All Known Subinterfaces:
`[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[Parameter](../../classes/mdkernel/Parameter.html)`, `[Port](../mdports/Port.html)`, `[Property](../../classes/mdkernel/Property.html)`, `[Variable](../../activities/mdstructuredactivities/Variable.html)`

public interfaceConnectableElementextends [TypedElement](../../classes/mdkernel/TypedElement.html), [ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)

begin-user-doc 
 A representation of the model object '***Connectable Element***'.
 end-user-doc 
begin-model-doc 
 ConnectableElement is an abstract metaclass representing a set of instances that play roles of a StructuredClassifier. ConnectableElements may be joined by attached
 Connectors and specify configurations of linked instances to be created within an instance of the containing StructuredClassifier.
 end-model-doc 
The following features are supported:
 [`*End*`](#getEnd())
[`*structured Classifier Of Role*`](#get_structuredClassifierOfRole())
[`*collaboration Of Collaboration Role*`](#get_collaborationOfCollaborationRole())
[`*lifeline Of Represents*`](#get_lifelineOfRepresents())

See Also:
[`UMLPackage.getConnectableElement()`](../../metadata/UMLPackage.html#getConnectableElement())
Model:
abstract="true"
 annotation="MOF package='compositestructures.mdinternalstructures'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Collaboration](../mdcollaborations/Collaboration.html)>`
`[get_collaborationOfCollaborationRole](#get_collaborationOfCollaborationRole())()`
Returns the value of the '***collaboration Of Collaboration Role***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Lifeline](../../interactions/mdbasicinteractions/Lifeline.html)>`
`[get_lifelineOfRepresents](#get_lifelineOfRepresents())()`
Returns the value of the '***lifeline Of Represents***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[StructuredClassifier](StructuredClassifier.html)>`
`[get_structuredClassifierOfRole](#get_structuredClassifierOfRole())()`
Returns the value of the '***structured Classifier Of Role***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ConnectorEnd](ConnectorEnd.html)>`
`[getEnd](#getEnd())()`
Returns the value of the '***End***' reference list.
`[ConnectableElementTemplateParameter](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)`
`[getTemplateParameter](#getTemplateParameter())()`
Returns the value of the '***Template Parameter***' reference.
`boolean`
`[has_collaborationOfCollaborationRole](#has_collaborationOfCollaborationRole())()`

`boolean`
`[has_lifelineOfRepresents](#has_lifelineOfRepresents())()`

`boolean`
`[has_structuredClassifierOfRole](#has_structuredClassifierOfRole())()`

`boolean`
`[hasEnd](#hasEnd())()`

`void`
`[setTemplateParameter](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))([ConnectableElementTemplateParameter](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) value)`
Sets the value of the
 '[`*Template Parameter*`](#getTemplateParameter())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
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
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](../../classes/mdkernel/TypedElement.html)
`[getType](../../classes/mdkernel/TypedElement.html#getType()), [setType](../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
get_structuredClassifierOfRole
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[StructuredClassifier](StructuredClassifier.html)> get_structuredClassifierOfRole()
Returns the value of the '***structured Classifier Of Role***' reference list.
 The list contents are of type [`StructuredClassifier`](StructuredClassifier.html).
 It is bidirectional and its opposite is
 '[`*Role*`](StructuredClassifier.html#getRole())'.
 begin-user-doc 
If the meaning of the '*structured Classifier Of Role*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*structured Classifier Of Role*' reference list.
See Also:
[`UMLPackage.getConnectableElement__structuredClassifierOfRole()`](../../metadata/UMLPackage.html#getConnectableElement__structuredClassifierOfRole())
[`StructuredClassifier.getRole()`](StructuredClassifier.html#getRole())
Model:
opposite="role" transient="true" volatile="true" derived="true" ordered="false"
Generated:
get_lifelineOfRepresents
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Lifeline](../../interactions/mdbasicinteractions/Lifeline.html)> get_lifelineOfRepresents()
Returns the value of the '***lifeline Of Represents***' reference list.
 The list contents are of type [`Lifeline`](../../interactions/mdbasicinteractions/Lifeline.html).
 It is bidirectional and its opposite is '[`*Represents*`](../../interactions/mdbasicinteractions/Lifeline.html#getRepresents())'.
 begin-user-doc 
If the meaning of the '*lifeline Of Represents*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*lifeline Of Represents*' reference list.
See Also:
[`UMLPackage.getConnectableElement__lifelineOfRepresents()`](../../metadata/UMLPackage.html#getConnectableElement__lifelineOfRepresents())
[`Lifeline.getRepresents()`](../../interactions/mdbasicinteractions/Lifeline.html#getRepresents())
Model:
opposite="represents" ordered="false"
Generated:
getEnd
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ConnectorEnd](ConnectorEnd.html)> getEnd()
Returns the value of the '***End***' reference list.
 The list contents are of type [`ConnectorEnd`](ConnectorEnd.html).
 It is bidirectional and its opposite is '[`*Role*`](ConnectorEnd.html#getRole())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A set of ConnectorEnds that attach to this ConnectableElement.
 end-model-doc
Returns:
the value of the '*End*' reference list.
See Also:
[`UMLPackage.getConnectableElement_End()`](../../metadata/UMLPackage.html#getConnectableElement_End())
[`ConnectorEnd.getRole()`](ConnectorEnd.html#getRole())
Model:
opposite="role" ordered="false"
Generated:
get_collaborationOfCollaborationRole
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Collaboration](../mdcollaborations/Collaboration.html)> get_collaborationOfCollaborationRole()
Returns the value of the '***collaboration Of Collaboration Role***' reference list.
 The list contents are of type [`Collaboration`](../mdcollaborations/Collaboration.html).
 It is bidirectional and its opposite is
 '[`*Collaboration Role*`](../mdcollaborations/Collaboration.html#getCollaborationRole())'.
 begin-user-doc 
If the meaning of the '*collaboration Of Collaboration Role*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*collaboration Of Collaboration Role*' reference list.
See Also:
[`UMLPackage.getConnectableElement__collaborationOfCollaborationRole()`](../../metadata/UMLPackage.html#getConnectableElement__collaborationOfCollaborationRole())
[`Collaboration.getCollaborationRole()`](../mdcollaborations/Collaboration.html#getCollaborationRole())
Model:
opposite="collaborationRole" ordered="false"
Generated:
getTemplateParameter
@CheckForNull[ConnectableElementTemplateParameter](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) getTemplateParameter()
Returns the value of the '***Template Parameter***' reference.
 It is bidirectional and its opposite is '[`#getParameteredElement *Parametered Element*`](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html)'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ConnectableElementTemplateParameter for this ConnectableElement parameter.
 end-model-doc
Specified by:
`[getTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter())` in interface `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`
Returns:
the value of the '*Template Parameter*' reference.
See Also:
[`setTemplateParameter(ConnectableElementTemplateParameter)`](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))
[`UMLPackage.getConnectableElement_TemplateParameter()`](../../metadata/UMLPackage.html#getConnectableElement_TemplateParameter())
[`ConnectableElementTemplateParameter.getParameteredElement()`](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html#getParameteredElement())
Model:
opposite="parameteredElement" ordered="false"
Generated:
setTemplateParameter
void setTemplateParameter(@CheckForNull
 [ConnectableElementTemplateParameter](../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html) value)
Sets the value of the
 '[`*Template Parameter*`](#getTemplateParameter())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Template Parameter*' reference.
See Also:
[`getTemplateParameter()`](#getTemplateParameter())
Generated:
has_structuredClassifierOfRole
boolean has_structuredClassifierOfRole()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_lifelineOfRepresents
boolean has_lifelineOfRepresents()
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
has_collaborationOfCollaborationRole
boolean has_collaborationOfCollaborationRole()
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
<h1 class="title" title="Interface ConnectableElement">Interface ConnectableElement</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code>, <code><a href="../mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ConnectableElement</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Connectable Element</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 ConnectableElement is an abstract metaclass representing a set of instances that play roles of a StructuredClassifier. ConnectableElements may be joined by attached
 Connectors and specify configurations of linked instances to be created within an instance of the containing StructuredClassifier.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getEnd()"><code><em>End</em></code></a></li>
<li><a href="#get_structuredClassifierOfRole()"><code><em>structured Classifier Of Role</em></code></a></li>
<li><a href="#get_collaborationOfCollaborationRole()"><code><em>collaboration Of Collaboration Role</em></code></a></li>
<li><a href="#get_lifelineOfRepresents()"><code><em>lifeline Of Represents</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnectableElement()"><code>UMLPackage.getConnectableElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='compositestructures.mdinternalstructures'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_collaborationOfCollaborationRole()">get_collaborationOfCollaborationRole</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>collaboration Of Collaboration Role</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_lifelineOfRepresents()">get_lifelineOfRepresents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>lifeline Of Represents</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_structuredClassifierOfRole()">get_structuredClassifierOfRole</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>structured Classifier Of Role</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEnd()">getEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>End</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTemplateParameter()">getTemplateParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_collaborationOfCollaborationRole()">has_collaborationOfCollaborationRole</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_lifelineOfRepresents()">has_lifelineOfRepresents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_structuredClassifierOfRole()">has_structuredClassifierOfRole</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEnd()">hasEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">setTemplateParameter</a><wbr/>(<a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.</div>
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
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
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
<section class="detail" id="get_structuredClassifierOfRole()">
<h3>get_structuredClassifierOfRole</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a>&gt;</span> <span class="element-name">get_structuredClassifierOfRole</span>()</div>
<div class="block">Returns the value of the '<em><b>structured Classifier Of Role</b></em>' reference list.
 The list contents are of type <a href="StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>StructuredClassifier</code></a>.
 It is bidirectional and its opposite is
 '<a href="StructuredClassifier.html#getRole()"><code><em>Role</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>structured Classifier Of Role</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>structured Classifier Of Role</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnectableElement__structuredClassifierOfRole()"><code>UMLPackage.getConnectableElement__structuredClassifierOfRole()</code></a></li>
<li><a href="StructuredClassifier.html#getRole()"><code>StructuredClassifier.getRole()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="role" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_lifelineOfRepresents()">
<h3>get_lifelineOfRepresents</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a>&gt;</span> <span class="element-name">get_lifelineOfRepresents</span>()</div>
<div class="block">Returns the value of the '<em><b>lifeline Of Represents</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Lifeline</code></a>.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Lifeline.html#getRepresents()"><code><em>Represents</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>lifeline Of Represents</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>lifeline Of Represents</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnectableElement__lifelineOfRepresents()"><code>UMLPackage.getConnectableElement__lifelineOfRepresents()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Lifeline.html#getRepresents()"><code>Lifeline.getRepresents()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="represents" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnd()">
<h3>getEnd</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a>&gt;</span> <span class="element-name">getEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>End</b></em>' reference list.
 The list contents are of type <a href="ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>ConnectorEnd</code></a>.
 It is bidirectional and its opposite is '<a href="ConnectorEnd.html#getRole()"><code><em>Role</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A set of ConnectorEnds that attach to this ConnectableElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>End</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnectableElement_End()"><code>UMLPackage.getConnectableElement_End()</code></a></li>
<li><a href="ConnectorEnd.html#getRole()"><code>ConnectorEnd.getRole()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="role" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_collaborationOfCollaborationRole()">
<h3>get_collaborationOfCollaborationRole</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a>&gt;</span> <span class="element-name">get_collaborationOfCollaborationRole</span>()</div>
<div class="block">Returns the value of the '<em><b>collaboration Of Collaboration Role</b></em>' reference list.
 The list contents are of type <a href="../mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations"><code>Collaboration</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdcollaborations/Collaboration.html#getCollaborationRole()"><code><em>Collaboration Role</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>collaboration Of Collaboration Role</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>collaboration Of Collaboration Role</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConnectableElement__collaborationOfCollaborationRole()"><code>UMLPackage.getConnectableElement__collaborationOfCollaborationRole()</code></a></li>
<li><a href="../mdcollaborations/Collaboration.html#getCollaborationRole()"><code>Collaboration.getCollaborationRole()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="collaborationRole" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameter()">
<h3>getTemplateParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></span> <span class="element-name">getTemplateParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>#getParameteredElement <em>Parametered Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ConnectableElementTemplateParameter for this ConnectableElement parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()">getTemplateParameter</a></code> in interface <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)"><code>setTemplateParameter(ConnectableElementTemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConnectableElement_TemplateParameter()"><code>UMLPackage.getConnectableElement_TemplateParameter()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html#getParameteredElement()"><code>ConnectableElementTemplateParameter.getParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameteredElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">
<h3>setTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTemplateParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../auxiliaryconstructs/mdtemplates/ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getTemplateParameter()"><code>getTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_structuredClassifierOfRole()">
<h3>has_structuredClassifierOfRole</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_structuredClassifierOfRole</span>()
                                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_lifelineOfRepresents()">
<h3>has_lifelineOfRepresents</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_lifelineOfRepresents</span>()
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
<li>
<section class="detail" id="has_collaborationOfCollaborationRole()">
<h3>has_collaborationOfCollaborationRole</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_collaborationOfCollaborationRole</span>()
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
