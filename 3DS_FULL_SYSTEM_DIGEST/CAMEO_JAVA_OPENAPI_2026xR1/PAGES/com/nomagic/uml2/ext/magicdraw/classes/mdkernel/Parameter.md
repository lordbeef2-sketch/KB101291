# JAVA OPENAPI: Parameter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Parameter.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Parameter.html`
- source_sha256: `ffa5562d7327e1aafeaba2f7ea3903b498d5a342bfae56946bb80f9d17fc7816`
- captured_utc: `2026-07-14T16:46:29.742197+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Parameter

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[MultiplicityElement](MultiplicityElement.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](TypedElement.html)`

public interfaceParameterextends [ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html), [MultiplicityElement](MultiplicityElement.html)

begin-user-doc 
 A representation of the model object '***Parameter***'.
 end-user-doc 
begin-model-doc 
 A Parameter is a specification of an argument used to pass information into or out of an invocation of a BehavioralFeature. Parameters can be treated as
 ConnectableElements within Collaborations.
 end-model-doc 
The following features are supported:
 [`*Owner Formal Param*`](#getOwnerFormalParam())
[`*Parameter Set*`](#getParameterSet())
[`*Operation*`](#getOperation())
[`*Default Value*`](#getDefaultValue())
[`*Default*`](#getDefault())
[`*Direction*`](#getDirection())
[`*Effect*`](#getEffect())
[`*Exception*`](#isException())
[`*Stream*`](#isStream())
[`*activity Parameter Node Of Parameter*`](#get_activityParameterNodeOfParameter())
[`*behavior Of Owned Parameter*`](#get_behaviorOfOwnedParameter())

See Also:
[`UMLPackage.getParameter()`](../../metadata/UMLPackage.html#getParameter())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityParameterNode](../../activities/mdbasicactivities/ActivityParameterNode.html)>`
`[get_activityParameterNodeOfParameter](#get_activityParameterNodeOfParameter())()`
Returns the value of the '***activity Parameter Node Of Parameter***' reference list.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[get_behaviorOfOwnedParameter](#get_behaviorOfOwnedParameter())()`
Returns the value of the '***behavior Of Owned Parameter***' container reference.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDefault](#getDefault())()`
Returns the value of the '***Default***' attribute.
`[ValueSpecification](ValueSpecification.html)`
`[getDefaultValue](#getDefaultValue())()`
Returns the value of the '***Default Value***' containment reference.
`[ParameterDirectionKind](ParameterDirectionKind.html)`
`[getDirection](#getDirection())()`
Returns the value of the '***Direction***' attribute.
`[ParameterEffectKind](../../activities/mdcompleteactivities/ParameterEffectKind.html)`
`[getEffect](#getEffect())()`
Returns the value of the '***Effect***' attribute.
`[Operation](Operation.html)`
`[getOperation](#getOperation())()`
Returns the value of the '***Operation***' container reference.
`[BehavioralFeature](BehavioralFeature.html)`
`[getOwnerFormalParam](#getOwnerFormalParam())()`
Returns the value of the '***Owner Formal Param***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)>`
`[getParameterSet](#getParameterSet())()`
Returns the value of the '***Parameter Set***' reference list.
`boolean`
`[has_activityParameterNodeOfParameter](#has_activityParameterNodeOfParameter())()`

`boolean`
`[hasParameterSet](#hasParameterSet())()`

`boolean`
`[isException](#isException())()`
Returns the value of the '***Exception***' attribute.
`boolean`
`[isStream](#isStream())()`
Returns the value of the '***Stream***' attribute.
`void`
`[set_behaviorOfOwnedParameter](#set_behaviorOfOwnedParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*behavior Of Owned Parameter*`](#get_behaviorOfOwnedParameter())'
 container reference.
`void`
`[setDefaultValue](#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](ValueSpecification.html) value)`
Sets the value of the '[`*Default Value*`](#getDefaultValue())' containment reference.
`void`
`[setDirection](#setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind))([ParameterDirectionKind](ParameterDirectionKind.html) value)`
Sets the value of the '[`*Direction*`](#getDirection())' attribute.
`void`
`[setEffect](#setEffect(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind))([ParameterEffectKind](../../activities/mdcompleteactivities/ParameterEffectKind.html) value)`
Sets the value of the '[`*Effect*`](#getEffect())' attribute.
`void`
`[setException](#setException(boolean))(boolean value)`
Sets the value of the '[`*Exception*`](#isException())' attribute.
`void`
`[setOperation](#setOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](Operation.html) value)`
Sets the value of the '[`*Operation*`](#getOperation())' container reference.
`void`
`[setOwnerFormalParam](#setOwnerFormalParam(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](BehavioralFeature.html) value)`
Sets the value of the '[`*Owner Formal Param*`](#getOwnerFormalParam())' container reference.
`void`
`[setStream](#setStream(boolean))(boolean value)`
Sets the value of the '[`*Stream*`](#isStream())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)
`[get_collaborationOfCollaborationRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()), [get_lifelineOfRepresents](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()), [get_structuredClassifierOfRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()), [getEnd](../../compositestructures/mdinternalstructures/ConnectableElement.html#getEnd()), [getTemplateParameter](../../compositestructures/mdinternalstructures/ConnectableElement.html#getTemplateParameter()), [has_collaborationOfCollaborationRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()), [has_lifelineOfRepresents](../../compositestructures/mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()), [has_structuredClassifierOfRole](../../compositestructures/mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()), [hasEnd](../../compositestructures/mdinternalstructures/ConnectableElement.html#hasEnd()), [setTemplateParameter](../../compositestructures/mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
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
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](TypedElement.html)
`[getType](TypedElement.html#getType()), [setType](TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
getParameterSet
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)> getParameterSet()
Returns the value of the '***Parameter Set***' reference list.
 The list contents are of type [`ParameterSet`](../../activities/mdcompleteactivities/ParameterSet.html).
 It is bidirectional and its opposite is '[`*Parameter*`](../../activities/mdcompleteactivities/ParameterSet.html#getParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterSets containing the parameter. See ParameterSet.
 end-model-doc
Returns:
the value of the '*Parameter Set*' reference list.
See Also:
[`UMLPackage.getParameter_ParameterSet()`](../../metadata/UMLPackage.html#getParameter_ParameterSet())
[`ParameterSet.getParameter()`](../../activities/mdcompleteactivities/ParameterSet.html#getParameter())
Model:
opposite="parameter" ordered="false"
Generated:
get_behaviorOfOwnedParameter
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) get_behaviorOfOwnedParameter()
Returns the value of the '***behavior Of Owned Parameter***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Parameter*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameter())'.
 begin-user-doc 
If the meaning of the '*behavior Of Owned Parameter*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behavior Of Owned Parameter*' container reference.
See Also:
[`set_behaviorOfOwnedParameter(Behavior)`](#set_behaviorOfOwnedParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getParameter__behaviorOfOwnedParameter()`](../../metadata/UMLPackage.html#getParameter__behaviorOfOwnedParameter())
[`Behavior.getOwnedParameter()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameter())
Model:
opposite="ownedParameter" transient="false" ordered="false"
Generated:
set_behaviorOfOwnedParameter
void set_behaviorOfOwnedParameter(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*behavior Of Owned Parameter*`](#get_behaviorOfOwnedParameter())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*behavior Of Owned Parameter*' container reference.
See Also:
[`get_behaviorOfOwnedParameter()`](#get_behaviorOfOwnedParameter())
Generated:
get_activityParameterNodeOfParameter
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityParameterNode](../../activities/mdbasicactivities/ActivityParameterNode.html)> get_activityParameterNodeOfParameter()
Returns the value of the '***activity Parameter Node Of Parameter***' reference list.
 The list contents are of type [`ActivityParameterNode`](../../activities/mdbasicactivities/ActivityParameterNode.html).
 It is bidirectional and its opposite is
 '[`*Parameter*`](../../activities/mdbasicactivities/ActivityParameterNode.html#getParameter())'.
 begin-user-doc 
If the meaning of the '*activity Parameter Node Of Parameter*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*activity Parameter Node Of Parameter*' reference list.
See Also:
[`UMLPackage.getParameter__activityParameterNodeOfParameter()`](../../metadata/UMLPackage.html#getParameter__activityParameterNodeOfParameter())
[`ActivityParameterNode.getParameter()`](../../activities/mdbasicactivities/ActivityParameterNode.html#getParameter())
Model:
opposite="parameter" ordered="false"
Generated:
getDirection
@CheckForNull[ParameterDirectionKind](ParameterDirectionKind.html) getDirection()
Returns the value of the '***Direction***' attribute.
 The default value is `"in"`.
 The literals are from the enumeration [`ParameterDirectionKind`](ParameterDirectionKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates whether a parameter is being sent into or out of a behavioral element.
 end-model-doc
Returns:
the value of the '*Direction*' attribute.
See Also:
[`ParameterDirectionKind`](ParameterDirectionKind.html)
[`setDirection(ParameterDirectionKind)`](#setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind))
[`UMLPackage.getParameter_Direction()`](../../metadata/UMLPackage.html#getParameter_Direction())
Model:
default="in" required="true" ordered="false"
Generated:
setDirection
void setDirection(@CheckForNull
 [ParameterDirectionKind](ParameterDirectionKind.html) value)
Sets the value of the '[`*Direction*`](#getDirection())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Direction*' attribute.
See Also:
[`ParameterDirectionKind`](ParameterDirectionKind.html)
[`getDirection()`](#getDirection())
Generated:
getDefault
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDefault()
Returns the value of the '***Default***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A String that represents a value to be used when no argument is supplied for the Parameter.
 end-model-doc
Returns:
the value of the '*Default*' attribute.
See Also:
[`UMLPackage.getParameter_Default()`](../../metadata/UMLPackage.html#getParameter_Default())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getDefaultValue
@CheckForNull[ValueSpecification](ValueSpecification.html) getDefaultValue()
Returns the value of the '***Default Value***' containment reference.
 It is bidirectional and its opposite is '[`*Owning Parameter*`](ValueSpecification.html#getOwningParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies a ValueSpecification that represents a value to be used when no argument is supplied for the Parameter.
 end-model-doc
Returns:
the value of the '*Default Value*' containment reference.
See Also:
[`setDefaultValue(ValueSpecification)`](#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getParameter_DefaultValue()`](../../metadata/UMLPackage.html#getParameter_DefaultValue())
[`ValueSpecification.getOwningParameter()`](ValueSpecification.html#getOwningParameter())
Model:
opposite="owningParameter" containment="true" resolveProxies="true" ordered="false"
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
getOperation
@CheckForNull[Operation](Operation.html) getOperation()
Returns the value of the '***Operation***' container reference.
 It is bidirectional and its opposite is '[`*Owned Parameter*`](Operation.html#getOwnedParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Operation owning this parameter.
 end-model-doc
Returns:
the value of the '*Operation*' container reference.
See Also:
[`setOperation(Operation)`](#setOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))
[`UMLPackage.getParameter_Operation()`](../../metadata/UMLPackage.html#getParameter_Operation())
[`Operation.getOwnedParameter()`](Operation.html#getOwnedParameter())
Model:
opposite="ownedParameter" volatile="true" ordered="false"
Generated:
setOperation
void setOperation(@CheckForNull
 [Operation](Operation.html) value)
Sets the value of the '[`*Operation*`](#getOperation())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Operation*' container reference.
See Also:
[`getOperation()`](#getOperation())
Generated:
getEffect
@CheckForNull[ParameterEffectKind](../../activities/mdcompleteactivities/ParameterEffectKind.html) getEffect()
Returns the value of the '***Effect***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the effect that executions of the owner of the Parameter have on objects passed in or out of the parameter.
 end-model-doc
Returns:
the value of the '*Effect*' attribute.
See Also:
[`setEffect(ParameterEffectKind)`](#setEffect(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind))
[`UMLPackage.getParameter_Effect()`](../../metadata/UMLPackage.html#getParameter_Effect())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.ParameterParameterEffectKind" ordered="false"
Generated:
setEffect
void setEffect(@CheckForNull
 [ParameterEffectKind](../../activities/mdcompleteactivities/ParameterEffectKind.html) value)
Sets the value of the '[`*Effect*`](#getEffect())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Effect*' attribute.
See Also:
[`getEffect()`](#getEffect())
Generated:
isException
boolean isException()
Returns the value of the '***Exception***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Tells whether an output parameter may emit a value to the exclusion of the other outputs.
 end-model-doc
Returns:
the value of the '*Exception*' attribute.
See Also:
[`setException(boolean)`](#setException(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getParameter_Exception()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setException
void setException(boolean value)
Sets the value of the '[`*Exception*`](#isException())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Exception*' attribute.
See Also:
[`isException()`](#isException())
Generated:
isStream
boolean isStream()
Returns the value of the '***Stream***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Tells whether an input parameter may accept values while its behavior is executing, or whether an output parameter may post values while the behavior is
 executing.
 end-model-doc
Returns:
the value of the '*Stream*' attribute.
See Also:
[`setStream(boolean)`](#setStream(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getParameter_Stream()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setStream
void setStream(boolean value)
Sets the value of the '[`*Stream*`](#isStream())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Stream*' attribute.
See Also:
[`isStream()`](#isStream())
Generated:
getOwnerFormalParam
@CheckForNull[BehavioralFeature](BehavioralFeature.html) getOwnerFormalParam()
Returns the value of the '***Owner Formal Param***' container reference.
 It is bidirectional and its opposite is '[`*Owned Parameter*`](BehavioralFeature.html#getOwnedParameter())'.
 begin-user-doc 
If the meaning of the '*Owner Formal Param*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owner Formal Param*' container reference.
See Also:
[`setOwnerFormalParam(BehavioralFeature)`](#setOwnerFormalParam(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))
[`UMLPackage.getParameter_OwnerFormalParam()`](../../metadata/UMLPackage.html#getParameter_OwnerFormalParam())
[`BehavioralFeature.getOwnedParameter()`](BehavioralFeature.html#getOwnedParameter())
Model:
opposite="ownedParameter" transient="false" ordered="false"
Generated:
setOwnerFormalParam
void setOwnerFormalParam(@CheckForNull
 [BehavioralFeature](BehavioralFeature.html) value)
Sets the value of the '[`*Owner Formal Param*`](#getOwnerFormalParam())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owner Formal Param*' container reference.
See Also:
[`getOwnerFormalParam()`](#getOwnerFormalParam())
Generated:
hasParameterSet
boolean hasParameterSet()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_activityParameterNodeOfParameter
boolean has_activityParameterNodeOfParameter()
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
<h1 class="title" title="Interface Parameter">Interface Parameter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Parameter</span><span class="extends-implements">
extends <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a>, <a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Parameter</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Parameter is a specification of an argument used to pass information into or out of an invocation of a BehavioralFeature.  Parameters can be treated as
 ConnectableElements within Collaborations.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getOwnerFormalParam()"><code><em>Owner Formal Param</em></code></a></li>
<li><a href="#getParameterSet()"><code><em>Parameter Set</em></code></a></li>
<li><a href="#getOperation()"><code><em>Operation</em></code></a></li>
<li><a href="#getDefaultValue()"><code><em>Default Value</em></code></a></li>
<li><a href="#getDefault()"><code><em>Default</em></code></a></li>
<li><a href="#getDirection()"><code><em>Direction</em></code></a></li>
<li><a href="#getEffect()"><code><em>Effect</em></code></a></li>
<li><a href="#isException()"><code><em>Exception</em></code></a></li>
<li><a href="#isStream()"><code><em>Stream</em></code></a></li>
<li><a href="#get_activityParameterNodeOfParameter()"><code><em>activity Parameter Node Of Parameter</em></code></a></li>
<li><a href="#get_behaviorOfOwnedParameter()"><code><em>behavior Of Owned Parameter</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getParameter()"><code>UMLPackage.getParameter()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_activityParameterNodeOfParameter()">get_activityParameterNodeOfParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>activity Parameter Node Of Parameter</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behaviorOfOwnedParameter()">get_behaviorOfOwnedParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behavior Of Owned Parameter</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefault()">getDefault</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Default</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultValue()">getDefaultValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Default Value</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDirection()">getDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Direction</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdcompleteactivities/ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEffect()">getEffect</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Effect</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOperation()">getOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Operation</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnerFormalParam()">getOwnerFormalParam</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owner Formal Param</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParameterSet()">getParameterSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Parameter Set</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_activityParameterNodeOfParameter()">has_activityParameterNodeOfParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasParameterSet()">hasParameterSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isException()">isException</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Exception</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isStream()">isStream</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Stream</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_behaviorOfOwnedParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">set_behaviorOfOwnedParameter</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_behaviorOfOwnedParameter()"><code><em>behavior Of Owned Parameter</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setDefaultValue</a><wbr/>(<a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDefaultValue()"><code><em>Default Value</em></code></a>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind)">setDirection</a><wbr/>(<a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDirection()"><code><em>Direction</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEffect(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind)">setEffect</a><wbr/>(<a href="../../activities/mdcompleteactivities/ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getEffect()"><code><em>Effect</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setException(boolean)">setException</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isException()"><code><em>Exception</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">setOperation</a><wbr/>(<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOperation()"><code><em>Operation</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnerFormalParam(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">setOwnerFormalParam</a><wbr/>(<a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwnerFormalParam()"><code><em>Owner Formal Param</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setStream(boolean)">setStream</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isStream()"><code><em>Stream</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></h3>
<code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_collaborationOfCollaborationRole()">get_collaborationOfCollaborationRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()">get_lifelineOfRepresents</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_structuredClassifierOfRole()">get_structuredClassifierOfRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#getEnd()">getEnd</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#has_collaborationOfCollaborationRole()">has_collaborationOfCollaborationRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#has_lifelineOfRepresents()">has_lifelineOfRepresents</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#has_structuredClassifierOfRole()">has_structuredClassifierOfRole</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#hasEnd()">hasEnd</a>, <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ConnectableElementTemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
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
<section class="detail" id="getParameterSet()">
<h3>getParameterSet</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a>&gt;</span> <span class="element-name">getParameterSet</span>()</div>
<div class="block">Returns the value of the '<em><b>Parameter Set</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdcompleteactivities/ParameterSet.html#getParameter()"><code><em>Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterSets containing the parameter. See ParameterSet.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Parameter Set</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getParameter_ParameterSet()"><code>UMLPackage.getParameter_ParameterSet()</code></a></li>
<li><a href="../../activities/mdcompleteactivities/ParameterSet.html#getParameter()"><code>ParameterSet.getParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameter" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behaviorOfOwnedParameter()">
<h3>get_behaviorOfOwnedParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">get_behaviorOfOwnedParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>behavior Of Owned Parameter</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameter()"><code><em>Owned Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behavior Of Owned Parameter</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behavior Of Owned Parameter</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_behaviorOfOwnedParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>set_behaviorOfOwnedParameter(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameter__behaviorOfOwnedParameter()"><code>UMLPackage.getParameter__behaviorOfOwnedParameter()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameter()"><code>Behavior.getOwnedParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedParameter" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_behaviorOfOwnedParameter(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>set_behaviorOfOwnedParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_behaviorOfOwnedParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_behaviorOfOwnedParameter()"><code><em>behavior Of Owned Parameter</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>behavior Of Owned Parameter</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_behaviorOfOwnedParameter()"><code>get_behaviorOfOwnedParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_activityParameterNodeOfParameter()">
<h3>get_activityParameterNodeOfParameter</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a>&gt;</span> <span class="element-name">get_activityParameterNodeOfParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>activity Parameter Node Of Parameter</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityParameterNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdbasicactivities/ActivityParameterNode.html#getParameter()"><code><em>Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>activity Parameter Node Of Parameter</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>activity Parameter Node Of Parameter</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getParameter__activityParameterNodeOfParameter()"><code>UMLPackage.getParameter__activityParameterNodeOfParameter()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ActivityParameterNode.html#getParameter()"><code>ActivityParameterNode.getParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameter" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirection()">
<h3>getDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a></span> <span class="element-name">getDirection</span>()</div>
<div class="block">Returns the value of the '<em><b>Direction</b></em>' attribute.
 The default value is <code>"in"</code>.
 The literals are from the enumeration <a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ParameterDirectionKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates whether a parameter is being sent into or out of a behavioral element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Direction</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ParameterDirectionKind</code></a></li>
<li><a href="#setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind)"><code>setDirection(ParameterDirectionKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameter_Direction()"><code>UMLPackage.getParameter_Direction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="in" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind)">
<h3>setDirection</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDirection()"><code><em>Direction</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Direction</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ParameterDirectionKind</code></a></li>
<li><a href="#getDirection()"><code>getDirection()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefault()">
<h3>getDefault</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefault</span>()</div>
<div class="block">Returns the value of the '<em><b>Default</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A String that represents a value to be used when no argument is supplied for the Parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Default</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getParameter_Default()"><code>UMLPackage.getParameter_Default()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
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
 It is bidirectional and its opposite is '<a href="ValueSpecification.html#getOwningParameter()"><code><em>Owning Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies a ValueSpecification that represents a value to be used when no argument is supplied for the Parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Default Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDefaultValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setDefaultValue(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameter_DefaultValue()"><code>UMLPackage.getParameter_DefaultValue()</code></a></li>
<li><a href="ValueSpecification.html#getOwningParameter()"><code>ValueSpecification.getOwningParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningParameter" containment="true" resolveProxies="true" ordered="false"</dd>
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
<ul class="tag-list">
<li><a href="#getDefaultValue()"><code>getDefaultValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperation()">
<h3>getOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>Operation</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Operation.html#getOwnedParameter()"><code><em>Owned Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Operation owning this parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Operation</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)"><code>setOperation(Operation)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameter_Operation()"><code>UMLPackage.getParameter_Operation()</code></a></li>
<li><a href="Operation.html#getOwnedParameter()"><code>Operation.getOwnedParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedParameter" volatile="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOperation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>setOperation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOperation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOperation()"><code><em>Operation</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Operation</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getOperation()"><code>getOperation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEffect()">
<h3>getEffect</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdcompleteactivities/ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a></span> <span class="element-name">getEffect</span>()</div>
<div class="block">Returns the value of the '<em><b>Effect</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the effect that executions of the owner of the Parameter have on objects passed in or out of the parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Effect</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setEffect(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind)"><code>setEffect(ParameterEffectKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameter_Effect()"><code>UMLPackage.getParameter_Effect()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.ParameterParameterEffectKind" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEffect(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind)">
<h3>setEffect</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEffect</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdcompleteactivities/ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getEffect()"><code><em>Effect</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Effect</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getEffect()"><code>getEffect()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isException()">
<h3>isException</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isException</span>()</div>
<div class="block">Returns the value of the '<em><b>Exception</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Tells whether an output parameter may emit a value to the exclusion of the other outputs.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Exception</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setException(boolean)"><code>setException(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getParameter_Exception()</code></pre>
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
<section class="detail" id="setException(boolean)">
<h3>setException</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setException</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isException()"><code><em>Exception</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Exception</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isException()"><code>isException()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStream()">
<h3>isStream</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isStream</span>()</div>
<div class="block">Returns the value of the '<em><b>Stream</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Tells whether an input parameter may accept values while its behavior is executing, or whether an output parameter may post values while the behavior is
 executing.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Stream</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setStream(boolean)"><code>setStream(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getParameter_Stream()</code></pre>
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
<section class="detail" id="setStream(boolean)">
<h3>setStream</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setStream</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isStream()"><code><em>Stream</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Stream</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isStream()"><code>isStream()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnerFormalParam()">
<h3>getOwnerFormalParam</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></span> <span class="element-name">getOwnerFormalParam</span>()</div>
<div class="block">Returns the value of the '<em><b>Owner Formal Param</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="BehavioralFeature.html#getOwnedParameter()"><code><em>Owned Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owner Formal Param</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owner Formal Param</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setOwnerFormalParam(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)"><code>setOwnerFormalParam(BehavioralFeature)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameter_OwnerFormalParam()"><code>UMLPackage.getParameter_OwnerFormalParam()</code></a></li>
<li><a href="BehavioralFeature.html#getOwnedParameter()"><code>BehavioralFeature.getOwnedParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedParameter" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnerFormalParam(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>setOwnerFormalParam</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnerFormalParam</span><wbr/><span class="parameters">(@CheckForNull
 <a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwnerFormalParam()"><code><em>Owner Formal Param</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owner Formal Param</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getOwnerFormalParam()"><code>getOwnerFormalParam()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasParameterSet()">
<h3>hasParameterSet</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasParameterSet</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_activityParameterNodeOfParameter()">
<h3>has_activityParameterNodeOfParameter</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_activityParameterNodeOfParameter</span>()
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
