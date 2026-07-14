# JAVA OPENAPI: Region (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html
- source_path: `com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Region.html`
- source_sha256: `cb747efb8a729853aee959834dac4ee7c86cfb3a08b49bb3ac013d5d306340a2`
- captured_utc: `2026-07-14T16:53:13.848646+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines](package-summary.html)

## Interface Region

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceRegionextends [Namespace](../../classes/mdkernel/Namespace.html), [RedefinableElement](../../classes/mdkernel/RedefinableElement.html)

begin-user-doc 
 A representation of the model object '***Region***'.
 end-user-doc 
begin-model-doc 
 A Region is a top-level part of a StateMachine or a composite State, that serves as a container for the Vertices and Transitions of the StateMachine. A StateMachine
 or composite State may contain multiple Regions representing behaviors that may occur in parallel.
 end-model-doc 
The following features are supported:
 [`*Extended Region*`](#getExtendedRegion())
[`*region Of Extended Region*`](#get_regionOfExtendedRegion())
[`*State*`](#getState())
[`*State Machine*`](#getStateMachine())
[`*Transition*`](#getTransition())
[`*Subvertex*`](#getSubvertex())

See Also:
[`UMLPackage.getRegion()`](../../metadata/UMLPackage.html#getRegion())
Model:
annotation="MOF package='statemachines.mdbehaviorstatemachines'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Region](Region.html)>`
`[get_regionOfExtendedRegion](#get_regionOfExtendedRegion())()`
Returns the value of the '***region Of Extended Region***' reference list.
`[Region](Region.html)`
`[getExtendedRegion](#getExtendedRegion())()`
Returns the value of the '***Extended Region***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../classes/mdkernel/Classifier.html)>`
`[getRedefinitionContext](#getRedefinitionContext())()`
Returns the value of the '***Redefinition Context***' reference list.
`[State](State.html)`
`[getState](#getState())()`
Returns the value of the '***State***' container reference.
`[StateMachine](StateMachine.html)`
`[getStateMachine](#getStateMachine())()`
Returns the value of the '***State Machine***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Vertex](Vertex.html)>`
`[getSubvertex](#getSubvertex())()`
Returns the value of the '***Subvertex***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Transition](Transition.html)>`
`[getTransition](#getTransition())()`
Returns the value of the '***Transition***' containment reference list.
`boolean`
`[has_regionOfExtendedRegion](#has_regionOfExtendedRegion())()`

`boolean`
`[hasSubvertex](#hasSubvertex())()`

`boolean`
`[hasTransition](#hasTransition())()`

`void`
`[setExtendedRegion](#setExtendedRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region))([Region](Region.html) value)`
Sets the value of the '[`*Extended Region*`](#getExtendedRegion())' reference.
`void`
`[setState](#setState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](State.html) value)`
Sets the value of the '[`*State*`](#getState())' container reference.
`void`
`[setStateMachine](#setStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine))([StateMachine](StateMachine.html) value)`
Sets the value of the '[`*State Machine*`](#getStateMachine())' container
 reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getSubvertex
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Vertex](Vertex.html)> getSubvertex()
Returns the value of the '***Subvertex***' containment reference list.
 The list contents are of type [`Vertex`](Vertex.html).
 It is bidirectional and its opposite is '[`*Container*`](Vertex.html#getContainer())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of Vertices that are owned by this Region.
 end-model-doc
Returns:
the value of the '*Subvertex*' containment reference list.
See Also:
[`UMLPackage.getRegion_Subvertex()`](../../metadata/UMLPackage.html#getRegion_Subvertex())
[`Vertex.getContainer()`](Vertex.html#getContainer())
Model:
opposite="container" containment="true" resolveProxies="true" ordered="false"
Generated:
getTransition
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Transition](Transition.html)> getTransition()
Returns the value of the '***Transition***' containment reference list.
 The list contents are of type [`Transition`](Transition.html).
 It is bidirectional and its opposite is '[`*Container*`](Transition.html#getContainer())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of Transitions owned by the Region.
 end-model-doc
Returns:
the value of the '*Transition*' containment reference list.
See Also:
[`UMLPackage.getRegion_Transition()`](../../metadata/UMLPackage.html#getRegion_Transition())
[`Transition.getContainer()`](Transition.html#getContainer())
Model:
opposite="container" containment="true" resolveProxies="true" ordered="false"
Generated:
getStateMachine
@CheckForNull[StateMachine](StateMachine.html) getStateMachine()
Returns the value of the '***State Machine***' container reference.
 It is bidirectional and its opposite is '[`*Region*`](StateMachine.html#getRegion())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The StateMachine that owns the Region. If a Region is owned by a StateMachine, then it cannot also be owned by a State.
 end-model-doc
Returns:
the value of the '*State Machine*' container reference.
See Also:
[`setStateMachine(StateMachine)`](#setStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine))
[`UMLPackage.getRegion_StateMachine()`](../../metadata/UMLPackage.html#getRegion_StateMachine())
[`StateMachine.getRegion()`](StateMachine.html#getRegion())
Model:
opposite="region" transient="false" ordered="false"
Generated:
setStateMachine
void setStateMachine(@CheckForNull
 [StateMachine](StateMachine.html) value)
Sets the value of the '[`*State Machine*`](#getStateMachine())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*State Machine*' container reference.
See Also:
[`getStateMachine()`](#getStateMachine())
Generated:
getState
@CheckForNull[State](State.html) getState()
Returns the value of the '***State***' container reference.
 It is bidirectional and its opposite is '[`*Region*`](State.html#getRegion())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The State that owns the Region. If a Region is owned by a State, then it cannot also be owned by a StateMachine.
 end-model-doc
Returns:
the value of the '*State*' container reference.
See Also:
[`setState(State)`](#setState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))
[`UMLPackage.getRegion_State()`](../../metadata/UMLPackage.html#getRegion_State())
[`State.getRegion()`](State.html#getRegion())
Model:
opposite="region" transient="false" ordered="false"
Generated:
setState
void setState(@CheckForNull
 [State](State.html) value)
Sets the value of the '[`*State*`](#getState())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*State*' container reference.
See Also:
[`getState()`](#getState())
Generated:
getExtendedRegion
@CheckForNull[Region](Region.html) getExtendedRegion()
Returns the value of the '***Extended Region***' reference.
 It is bidirectional and its opposite is
 '[`*region Of Extended Region*`](#get_regionOfExtendedRegion())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The region of which this region is an extension.
 end-model-doc
Returns:
the value of the '*Extended Region*' reference.
See Also:
[`setExtendedRegion(Region)`](#setExtendedRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region))
[`UMLPackage.getRegion_ExtendedRegion()`](../../metadata/UMLPackage.html#getRegion_ExtendedRegion())
[`get_regionOfExtendedRegion()`](#get_regionOfExtendedRegion())
Model:
opposite="_regionOfExtendedRegion" ordered="false"
Generated:
setExtendedRegion
void setExtendedRegion(@CheckForNull
 [Region](Region.html) value)
Sets the value of the '[`*Extended Region*`](#getExtendedRegion())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Extended Region*' reference.
See Also:
[`getExtendedRegion()`](#getExtendedRegion())
Generated:
get_regionOfExtendedRegion
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Region](Region.html)> get_regionOfExtendedRegion()
Returns the value of the '***region Of Extended Region***' reference list.
 The list contents are of type [`Region`](Region.html).
 It is bidirectional and its opposite is
 '[`*Extended Region*`](#getExtendedRegion())'.
 begin-user-doc 
If the meaning of the '*region Of Extended Region*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*region Of Extended Region*' reference list.
See Also:
[`UMLPackage.getRegion__regionOfExtendedRegion()`](../../metadata/UMLPackage.html#getRegion__regionOfExtendedRegion())
[`getExtendedRegion()`](#getExtendedRegion())
Model:
opposite="extendedRegion" ordered="false"
Generated:
getRedefinitionContext
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../classes/mdkernel/Classifier.html)> getRedefinitionContext()
Returns the value of the '***Redefinition Context***' reference list.
 The list contents are of type [`Classifier`](../../classes/mdkernel/Classifier.html).
 It is bidirectional and its opposite is
 '`*region Of Redefinition Context*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Classifier in which context this element may be redefined.
 end-model-doc
Specified by:
`[getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext())` in interface `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`
Returns:
the value of the '*Redefinition Context*' reference list.
See Also:
[`UMLPackage.getRegion_RedefinitionContext()`](../../metadata/UMLPackage.html#getRegion_RedefinitionContext())
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_regionOfRedefinitionContext`
Model:
opposite="_regionOfRedefinitionContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
has_regionOfExtendedRegion
boolean has_regionOfExtendedRegion()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasSubvertex
boolean hasSubvertex()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasTransition
boolean hasTransition()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines</a></div>
<h1 class="title" title="Interface Region">Interface Region</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Region</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>, <a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Region</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Region is a top-level part of a StateMachine or a composite State, that serves as a container for the Vertices and Transitions of the StateMachine. A StateMachine
 or composite State may contain multiple Regions representing behaviors that may occur in parallel.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getExtendedRegion()"><code><em>Extended Region</em></code></a></li>
<li><a href="#get_regionOfExtendedRegion()"><code><em>region Of Extended Region</em></code></a></li>
<li><a href="#getState()"><code><em>State</em></code></a></li>
<li><a href="#getStateMachine()"><code><em>State Machine</em></code></a></li>
<li><a href="#getTransition()"><code><em>Transition</em></code></a></li>
<li><a href="#getSubvertex()"><code><em>Subvertex</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getRegion()"><code>UMLPackage.getRegion()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='statemachines.mdbehaviorstatemachines'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_regionOfExtendedRegion()">get_regionOfExtendedRegion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>region Of Extended Region</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtendedRegion()">getExtendedRegion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Extended Region</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinitionContext()">getRedefinitionContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefinition Context</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getState()">getState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>State</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStateMachine()">getStateMachine</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>State Machine</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSubvertex()">getSubvertex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Subvertex</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTransition()">getTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Transition</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_regionOfExtendedRegion()">has_regionOfExtendedRegion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSubvertex()">hasSubvertex</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasTransition()">hasTransition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExtendedRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">setExtendedRegion</a><wbr/>(<a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getExtendedRegion()"><code><em>Extended Region</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">setState</a><wbr/>(<a href="State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getState()"><code><em>State</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">setStateMachine</a><wbr/>(<a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getStateMachine()"><code><em>State Machine</em></code></a>' container
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<section class="detail" id="getSubvertex()">
<h3>getSubvertex</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a>&gt;</span> <span class="element-name">getSubvertex</span>()</div>
<div class="block">Returns the value of the '<em><b>Subvertex</b></em>' containment reference list.
 The list contents are of type <a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Vertex</code></a>.
 It is bidirectional and its opposite is '<a href="Vertex.html#getContainer()"><code><em>Container</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of Vertices that are owned by this Region.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Subvertex</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getRegion_Subvertex()"><code>UMLPackage.getRegion_Subvertex()</code></a></li>
<li><a href="Vertex.html#getContainer()"><code>Vertex.getContainer()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="container" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransition()">
<h3>getTransition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a>&gt;</span> <span class="element-name">getTransition</span>()</div>
<div class="block">Returns the value of the '<em><b>Transition</b></em>' containment reference list.
 The list contents are of type <a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>.
 It is bidirectional and its opposite is '<a href="Transition.html#getContainer()"><code><em>Container</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of Transitions owned by the Region.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Transition</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getRegion_Transition()"><code>UMLPackage.getRegion_Transition()</code></a></li>
<li><a href="Transition.html#getContainer()"><code>Transition.getContainer()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="container" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateMachine()">
<h3>getStateMachine</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></span> <span class="element-name">getStateMachine</span>()</div>
<div class="block">Returns the value of the '<em><b>State Machine</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="StateMachine.html#getRegion()"><code><em>Region</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The StateMachine that owns the Region. If a Region is owned by a StateMachine, then it cannot also be owned by a State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>State Machine</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)"><code>setStateMachine(StateMachine)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getRegion_StateMachine()"><code>UMLPackage.getRegion_StateMachine()</code></a></li>
<li><a href="StateMachine.html#getRegion()"><code>StateMachine.getRegion()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="region" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStateMachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">
<h3>setStateMachine</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setStateMachine</span><wbr/><span class="parameters">(@CheckForNull
 <a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getStateMachine()"><code><em>State Machine</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>State Machine</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getStateMachine()"><code>getStateMachine()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getState()">
<h3>getState</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">getState</span>()</div>
<div class="block">Returns the value of the '<em><b>State</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="State.html#getRegion()"><code><em>Region</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The State that owns the Region. If a Region is owned by a State, then it cannot also be owned by a StateMachine.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>State</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)"><code>setState(State)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getRegion_State()"><code>UMLPackage.getRegion_State()</code></a></li>
<li><a href="State.html#getRegion()"><code>State.getRegion()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="region" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>setState</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setState</span><wbr/><span class="parameters">(@CheckForNull
 <a href="State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getState()"><code><em>State</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>State</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getState()"><code>getState()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtendedRegion()">
<h3>getExtendedRegion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></span> <span class="element-name">getExtendedRegion</span>()</div>
<div class="block">Returns the value of the '<em><b>Extended Region</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="#get_regionOfExtendedRegion()"><code><em>region Of Extended Region</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The region of which this region is an extension.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Extended Region</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setExtendedRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)"><code>setExtendedRegion(Region)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getRegion_ExtendedRegion()"><code>UMLPackage.getRegion_ExtendedRegion()</code></a></li>
<li><a href="#get_regionOfExtendedRegion()"><code>get_regionOfExtendedRegion()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_regionOfExtendedRegion" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExtendedRegion(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">
<h3>setExtendedRegion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExtendedRegion</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getExtendedRegion()"><code><em>Extended Region</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Extended Region</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getExtendedRegion()"><code>getExtendedRegion()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_regionOfExtendedRegion()">
<h3>get_regionOfExtendedRegion</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a>&gt;</span> <span class="element-name">get_regionOfExtendedRegion</span>()</div>
<div class="block">Returns the value of the '<em><b>region Of Extended Region</b></em>' reference list.
 The list contents are of type <a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getExtendedRegion()"><code><em>Extended Region</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>region Of Extended Region</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>region Of Extended Region</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getRegion__regionOfExtendedRegion()"><code>UMLPackage.getRegion__regionOfExtendedRegion()</code></a></li>
<li><a href="#getExtendedRegion()"><code>getExtendedRegion()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="extendedRegion" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinitionContext()">
<h3>getRedefinitionContext</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getRedefinitionContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefinition Context</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is
 '<code><em>region Of Redefinition Context</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Classifier in which context this element may be redefined.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a></code> in interface <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Redefinition Context</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getRegion_RedefinitionContext()"><code>UMLPackage.getRegion_RedefinitionContext()</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_regionOfRedefinitionContext</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_regionOfRedefinitionContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_regionOfExtendedRegion()">
<h3>has_regionOfExtendedRegion</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_regionOfExtendedRegion</span>()
                            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSubvertex()">
<h3>hasSubvertex</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSubvertex</span>()
              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasTransition()">
<h3>hasTransition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasTransition</span>()
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
