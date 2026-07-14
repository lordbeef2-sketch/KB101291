# JAVA OPENAPI: ActivityPartition (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html`
- source_sha256: `494611158b4ebdd5249a33fead21c75f49b208a55d6620b5f8788e54eed37413`
- captured_utc: `2026-07-14T16:58:51.466442+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities](package-summary.html)

## Interface ActivityPartition

All Superinterfaces:
`[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceActivityPartitionextends [ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)

begin-user-doc 
 A representation of the model object '***Activity Partition***'.
 end-user-doc 
begin-model-doc 
 An ActivityPartition is a kind of ActivityGroup for identifying ActivityNodes that have some characteristic in common.
 end-model-doc 
The following features are supported:
 [`*Dimension*`](#isDimension())
[`*External*`](#isExternal())
[`*Node*`](#getNode())
[`*Represents*`](#getRepresents())
[`*Subpartition*`](#getSubpartition())
[`*Super Partition*`](#getSuperPartition())
[`*activity Of Partition*`](#get_activityOfPartition())
[`*Edge*`](#getEdge())

See Also:
[`UMLPackage.getActivityPartition()`](../../metadata/UMLPackage.html#getActivityPartition())
Model:
annotation="MOF package='activities.mdintermediateactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Activity](../mdfundamentalactivities/Activity.html)`
`[get_activityOfPartition](#get_activityOfPartition())()`
Returns the value of the '***activity Of Partition***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](../mdbasicactivities/ActivityEdge.html)>`
`[getEdge](#getEdge())()`
Returns the value of the '***Edge***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityNode](../mdfundamentalactivities/ActivityNode.html)>`
`[getNode](#getNode())()`
Returns the value of the '***Node***' reference list.
`[Element](../../classes/mdkernel/Element.html)`
`[getRepresents](#getRepresents())()`
Returns the value of the '***Represents***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](ActivityPartition.html)>`
`[getSubpartition](#getSubpartition())()`
Returns the value of the '***Subpartition***' containment reference list.
`[ActivityPartition](ActivityPartition.html)`
`[getSuperPartition](#getSuperPartition())()`
Returns the value of the '***Super Partition***' container reference.
`boolean`
`[hasEdge](#hasEdge())()`

`boolean`
`[hasNode](#hasNode())()`

`boolean`
`[hasSubpartition](#hasSubpartition())()`

`boolean`
`[isDimension](#isDimension())()`
Returns the value of the '***Dimension***' attribute.
`boolean`
`[isExternal](#isExternal())()`
Returns the value of the '***External***' attribute.
`void`
`[set_activityOfPartition](#set_activityOfPartition(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))([Activity](../mdfundamentalactivities/Activity.html) value)`
Sets the value of the
 '[`*activity Of Partition*`](#get_activityOfPartition())' reference.
`void`
`[setDimension](#setDimension(boolean))(boolean value)`
Sets the value of the '[`*Dimension*`](#isDimension())' attribute.
`void`
`[setExternal](#setExternal(boolean))(boolean value)`
Sets the value of the '[`*External*`](#isExternal())' attribute.
`void`
`[setRepresents](#setRepresents(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../classes/mdkernel/Element.html) value)`
Sets the value of the '[`*Represents*`](#getRepresents())' reference.
`void`
`[setSuperPartition](#setSuperPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition))([ActivityPartition](ActivityPartition.html) value)`
Sets the value of the '[`*Super Partition*`](#getSuperPartition())'
 container reference.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)
`[getContainedEdge](../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()), [getContainedNode](../mdfundamentalactivities/ActivityGroup.html#getContainedNode()), [getInActivity](../mdfundamentalactivities/ActivityGroup.html#getInActivity()), [getSubgroup](../mdfundamentalactivities/ActivityGroup.html#getSubgroup()), [getSuperGroup](../mdfundamentalactivities/ActivityGroup.html#getSuperGroup()), [hasContainedEdge](../mdfundamentalactivities/ActivityGroup.html#hasContainedEdge()), [hasContainedNode](../mdfundamentalactivities/ActivityGroup.html#hasContainedNode()), [hasSubgroup](../mdfundamentalactivities/ActivityGroup.html#hasSubgroup()), [setInActivity](../mdfundamentalactivities/ActivityGroup.html#setInActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setSuperGroup](../mdfundamentalactivities/ActivityGroup.html#setSuperGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
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
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getNode
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityNode](../mdfundamentalactivities/ActivityNode.html)> getNode()
Returns the value of the '***Node***' reference list.
 The list contents are of type [`ActivityNode`](../mdfundamentalactivities/ActivityNode.html).
 It is bidirectional and its opposite is
 '[`*In Partition*`](../mdfundamentalactivities/ActivityNode.html#getInPartition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityNodes immediately contained in the ActivityPartition.
 end-model-doc
Returns:
the value of the '*Node*' reference list.
See Also:
[`UMLPackage.getActivityPartition_Node()`](../../metadata/UMLPackage.html#getActivityPartition_Node())
[`ActivityNode.getInPartition()`](../mdfundamentalactivities/ActivityNode.html#getInPartition())
Model:
opposite="inPartition" ordered="false"
Generated:
getSubpartition
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](ActivityPartition.html)> getSubpartition()
Returns the value of the '***Subpartition***' containment reference list.
 The list contents are of type [`ActivityPartition`](ActivityPartition.html).
 It is bidirectional and its opposite is
 '[`*Super Partition*`](#getSuperPartition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Other ActivityPartitions immediately contained in this ActivityPartition (as its subgroups).
 end-model-doc
Returns:
the value of the '*Subpartition*' containment reference list.
See Also:
[`UMLPackage.getActivityPartition_Subpartition()`](../../metadata/UMLPackage.html#getActivityPartition_Subpartition())
[`getSuperPartition()`](#getSuperPartition())
Model:
opposite="superPartition" containment="true" resolveProxies="true" ordered="false"
Generated:
getSuperPartition
@CheckForNull[ActivityPartition](ActivityPartition.html) getSuperPartition()
Returns the value of the '***Super Partition***' container reference.
 It is bidirectional and its opposite is
 '[`*Subpartition*`](#getSubpartition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Other ActivityPartitions immediately containing this ActivityPartition (as its superGroups).
 end-model-doc
Returns:
the value of the '*Super Partition*' container reference.
See Also:
[`setSuperPartition(ActivityPartition)`](#setSuperPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition))
[`UMLPackage.getActivityPartition_SuperPartition()`](../../metadata/UMLPackage.html#getActivityPartition_SuperPartition())
[`getSubpartition()`](#getSubpartition())
Model:
opposite="subpartition" transient="false" ordered="false"
Generated:
setSuperPartition
void setSuperPartition(@CheckForNull
 [ActivityPartition](ActivityPartition.html) value)
Sets the value of the '[`*Super Partition*`](#getSuperPartition())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Super Partition*' container reference.
See Also:
[`getSuperPartition()`](#getSuperPartition())
Generated:
getRepresents
@CheckForNull[Element](../../classes/mdkernel/Element.html) getRepresents()
Returns the value of the '***Represents***' reference.
 It is bidirectional and its opposite is
 '[`*activity Partition Of Represents*`](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An Element represented by the functionality modeled within the ActivityPartition.
 end-model-doc
Returns:
the value of the '*Represents*' reference.
See Also:
[`setRepresents(Element)`](#setRepresents(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`UMLPackage.getActivityPartition_Represents()`](../../metadata/UMLPackage.html#getActivityPartition_Represents())
[`Element.get_activityPartitionOfRepresents()`](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents())
Model:
opposite="_activityPartitionOfRepresents" ordered="false"
Generated:
setRepresents
void setRepresents(@CheckForNull
 [Element](../../classes/mdkernel/Element.html) value)
Sets the value of the '[`*Represents*`](#getRepresents())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Represents*' reference.
See Also:
[`getRepresents()`](#getRepresents())
Generated:
get_activityOfPartition
@CheckForNull[Activity](../mdfundamentalactivities/Activity.html) get_activityOfPartition()
Returns the value of the '***activity Of Partition***' reference.
 It is bidirectional and its opposite is '[`*Partition*`](../mdfundamentalactivities/Activity.html#getPartition())'.
 begin-user-doc 
If the meaning of the '*activity Of Partition*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*activity Of Partition*' reference.
See Also:
[`set_activityOfPartition(Activity)`](#set_activityOfPartition(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))
[`UMLPackage.getActivityPartition__activityOfPartition()`](../../metadata/UMLPackage.html#getActivityPartition__activityOfPartition())
[`Activity.getPartition()`](../mdfundamentalactivities/Activity.html#getPartition())
Model:
opposite="partition" ordered="false"
Generated:
set_activityOfPartition
void set_activityOfPartition(@CheckForNull
 [Activity](../mdfundamentalactivities/Activity.html) value)
Sets the value of the
 '[`*activity Of Partition*`](#get_activityOfPartition())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*activity Of Partition*' reference.
See Also:
[`get_activityOfPartition()`](#get_activityOfPartition())
Generated:
getEdge
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](../mdbasicactivities/ActivityEdge.html)> getEdge()
Returns the value of the '***Edge***' reference list.
 The list contents are of type [`ActivityEdge`](../mdbasicactivities/ActivityEdge.html).
 It is bidirectional and its opposite is '[`*In Partition*`](../mdbasicactivities/ActivityEdge.html#getInPartition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityEdges immediately contained in the ActivityPartition.
 end-model-doc
Returns:
the value of the '*Edge*' reference list.
See Also:
[`UMLPackage.getActivityPartition_Edge()`](../../metadata/UMLPackage.html#getActivityPartition_Edge())
[`ActivityEdge.getInPartition()`](../mdbasicactivities/ActivityEdge.html#getInPartition())
Model:
opposite="inPartition" ordered="false"
Generated:
isDimension
boolean isDimension()
Returns the value of the '***Dimension***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates whether the ActivityPartition groups other ActivityPartitions along a dimension.
 end-model-doc
Returns:
the value of the '*Dimension*' attribute.
See Also:
[`setDimension(boolean)`](#setDimension(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivityPartition_Dimension()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setDimension
void setDimension(boolean value)
Sets the value of the '[`*Dimension*`](#isDimension())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Dimension*' attribute.
See Also:
[`isDimension()`](#isDimension())
Generated:
isExternal
boolean isExternal()
Returns the value of the '***External***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates whether the ActivityPartition represents an entity to which the partitioning structure does not apply.
 end-model-doc
Returns:
the value of the '*External*' attribute.
See Also:
[`setExternal(boolean)`](#setExternal(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivityPartition_External()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setExternal
void setExternal(boolean value)
Sets the value of the '[`*External*`](#isExternal())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*External*' attribute.
See Also:
[`isExternal()`](#isExternal())
Generated:
hasNode
boolean hasNode()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasSubpartition
boolean hasSubpartition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasEdge
boolean hasEdge()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities</a></div>
<h1 class="title" title="Interface ActivityPartition">Interface ActivityPartition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ActivityPartition</span><span class="extends-implements">
extends <a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Activity Partition</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An ActivityPartition is a kind of ActivityGroup for identifying ActivityNodes that have some characteristic in common.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isDimension()"><code><em>Dimension</em></code></a></li>
<li><a href="#isExternal()"><code><em>External</em></code></a></li>
<li><a href="#getNode()"><code><em>Node</em></code></a></li>
<li><a href="#getRepresents()"><code><em>Represents</em></code></a></li>
<li><a href="#getSubpartition()"><code><em>Subpartition</em></code></a></li>
<li><a href="#getSuperPartition()"><code><em>Super Partition</em></code></a></li>
<li><a href="#get_activityOfPartition()"><code><em>activity Of Partition</em></code></a></li>
<li><a href="#getEdge()"><code><em>Edge</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityPartition()"><code>UMLPackage.getActivityPartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='activities.mdintermediateactivities'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_activityOfPartition()">get_activityOfPartition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>activity Of Partition</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEdge()">getEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Edge</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNode()">getNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Node</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresents()">getRepresents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Represents</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSubpartition()">getSubpartition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Subpartition</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSuperPartition()">getSuperPartition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Super Partition</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEdge()">hasEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasNode()">hasNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSubpartition()">hasSubpartition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDimension()">isDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Dimension</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isExternal()">isExternal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>External</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_activityOfPartition(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">set_activityOfPartition</a><wbr/>(<a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_activityOfPartition()"><code><em>activity Of Partition</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDimension(boolean)">setDimension</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isDimension()"><code><em>Dimension</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExternal(boolean)">setExternal</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isExternal()"><code><em>External</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRepresents(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setRepresents</a><wbr/>(<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getRepresents()"><code><em>Represents</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSuperPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition)">setSuperPartition</a><wbr/>(<a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSuperPartition()"><code><em>Super Partition</em></code></a>'
 container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></h3>
<code><a href="../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()">getContainedEdge</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getContainedNode()">getContainedNode</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getInActivity()">getInActivity</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getSubgroup()">getSubgroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getSuperGroup()">getSuperGroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasContainedEdge()">hasContainedEdge</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasContainedNode()">hasContainedNode</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasSubgroup()">hasSubgroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#setInActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setInActivity</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#setSuperGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup)">setSuperGroup</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
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
<section class="detail" id="getNode()">
<h3>getNode</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>&gt;</span> <span class="element-name">getNode</span>()</div>
<div class="block">Returns the value of the '<em><b>Node</b></em>' reference list.
 The list contents are of type <a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdfundamentalactivities/ActivityNode.html#getInPartition()"><code><em>In Partition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityNodes immediately contained in the ActivityPartition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Node</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityPartition_Node()"><code>UMLPackage.getActivityPartition_Node()</code></a></li>
<li><a href="../mdfundamentalactivities/ActivityNode.html#getInPartition()"><code>ActivityNode.getInPartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inPartition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubpartition()">
<h3>getSubpartition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</span> <span class="element-name">getSubpartition</span>()</div>
<div class="block">Returns the value of the '<em><b>Subpartition</b></em>' containment reference list.
 The list contents are of type <a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getSuperPartition()"><code><em>Super Partition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Other ActivityPartitions immediately contained in this ActivityPartition (as its subgroups).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Subpartition</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityPartition_Subpartition()"><code>UMLPackage.getActivityPartition_Subpartition()</code></a></li>
<li><a href="#getSuperPartition()"><code>getSuperPartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="superPartition" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuperPartition()">
<h3>getSuperPartition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a></span> <span class="element-name">getSuperPartition</span>()</div>
<div class="block">Returns the value of the '<em><b>Super Partition</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="#getSubpartition()"><code><em>Subpartition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Other ActivityPartitions immediately containing this ActivityPartition (as its superGroups).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Super Partition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSuperPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition)"><code>setSuperPartition(ActivityPartition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityPartition_SuperPartition()"><code>UMLPackage.getActivityPartition_SuperPartition()</code></a></li>
<li><a href="#getSubpartition()"><code>getSubpartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="subpartition" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSuperPartition(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.ActivityPartition)">
<h3>setSuperPartition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSuperPartition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSuperPartition()"><code><em>Super Partition</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Super Partition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSuperPartition()"><code>getSuperPartition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresents()">
<h3>getRepresents</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getRepresents</span>()</div>
<div class="block">Returns the value of the '<em><b>Represents</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()"><code><em>activity Partition Of Represents</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An Element represented by the functionality modeled within the ActivityPartition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Represents</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setRepresents(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>setRepresents(Element)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityPartition_Represents()"><code>UMLPackage.getActivityPartition_Represents()</code></a></li>
<li><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()"><code>Element.get_activityPartitionOfRepresents()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_activityPartitionOfRepresents" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRepresents(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setRepresents</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRepresents</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getRepresents()"><code><em>Represents</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Represents</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getRepresents()"><code>getRepresents()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_activityOfPartition()">
<h3>get_activityOfPartition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">get_activityOfPartition</span>()</div>
<div class="block">Returns the value of the '<em><b>activity Of Partition</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../mdfundamentalactivities/Activity.html#getPartition()"><code><em>Partition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>activity Of Partition</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>activity Of Partition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_activityOfPartition(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)"><code>set_activityOfPartition(Activity)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityPartition__activityOfPartition()"><code>UMLPackage.getActivityPartition__activityOfPartition()</code></a></li>
<li><a href="../mdfundamentalactivities/Activity.html#getPartition()"><code>Activity.getPartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="partition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_activityOfPartition(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">
<h3>set_activityOfPartition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_activityOfPartition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_activityOfPartition()"><code><em>activity Of Partition</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>activity Of Partition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_activityOfPartition()"><code>get_activityOfPartition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEdge()">
<h3>getEdge</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</span> <span class="element-name">getEdge</span>()</div>
<div class="block">Returns the value of the '<em><b>Edge</b></em>' reference list.
 The list contents are of type <a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.
 It is bidirectional and its opposite is '<a href="../mdbasicactivities/ActivityEdge.html#getInPartition()"><code><em>In Partition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityEdges immediately contained in the ActivityPartition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Edge</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityPartition_Edge()"><code>UMLPackage.getActivityPartition_Edge()</code></a></li>
<li><a href="../mdbasicactivities/ActivityEdge.html#getInPartition()"><code>ActivityEdge.getInPartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inPartition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDimension()">
<h3>isDimension</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDimension</span>()</div>
<div class="block">Returns the value of the '<em><b>Dimension</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates whether the ActivityPartition groups other ActivityPartitions along a dimension.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Dimension</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDimension(boolean)"><code>setDimension(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivityPartition_Dimension()</code></pre>
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
<section class="detail" id="setDimension(boolean)">
<h3>setDimension</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDimension</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isDimension()"><code><em>Dimension</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Dimension</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isDimension()"><code>isDimension()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExternal()">
<h3>isExternal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isExternal</span>()</div>
<div class="block">Returns the value of the '<em><b>External</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates whether the ActivityPartition represents an entity to which the partitioning structure does not apply.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>External</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setExternal(boolean)"><code>setExternal(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivityPartition_External()</code></pre>
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
<section class="detail" id="setExternal(boolean)">
<h3>setExternal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExternal</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isExternal()"><code><em>External</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>External</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isExternal()"><code>isExternal()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNode()">
<h3>hasNode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasNode</span>()
         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSubpartition()">
<h3>hasSubpartition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSubpartition</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasEdge()">
<h3>hasEdge</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasEdge</span>()
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
