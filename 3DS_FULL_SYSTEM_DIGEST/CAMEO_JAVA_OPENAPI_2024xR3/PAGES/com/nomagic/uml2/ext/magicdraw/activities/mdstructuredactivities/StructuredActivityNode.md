# JAVA OPENAPI: StructuredActivityNode (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html`
- source_sha256: `393fe4af2b2e6d5e933a1bb5b17cdacce950eae303951610c4d3d1f7f9899979`
- captured_utc: `2026-07-14T16:56:20.136734+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities](package-summary.html)

## Interface StructuredActivityNode

All Superinterfaces:
`[Action](../../actions/mdbasicactions/Action.html)`, `[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)`, `[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ExecutableNode](ExecutableNode.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[ConditionalNode](ConditionalNode.html)`, `[ExpansionRegion](../mdextrastructuredactivities/ExpansionRegion.html)`, `[LoopNode](LoopNode.html)`, `[SequenceNode](SequenceNode.html)`

public interfaceStructuredActivityNodeextends [Action](../../actions/mdbasicactions/Action.html), [Namespace](../../classes/mdkernel/Namespace.html), [ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)

begin-user-doc 
 A representation of the model object '***Structured Activity Node***'.
 end-user-doc 
begin-model-doc 
 A StructuredActivityNode is an Action that is also an ActivityGroup and whose behavior is specified by the ActivityNodes and ActivityEdges it so contains. Unlike
 other kinds of ActivityGroup, a StructuredActivityNode owns the ActivityNodes and ActivityEdges it contains, and so a node or edge can only be directly contained in
 one StructuredActivityNode, though StructuredActivityNodes may be nested.
 end-model-doc 
The following features are supported:
 [`*Must Isolate*`](#isMustIsolate())
[`*Node*`](#getNode())
[`*Structured Node Input*`](#getStructuredNodeInput())
[`*Structured Node Output*`](#getStructuredNodeOutput())
[`*Variable*`](#getVariable())
[`*Edge*`](#getEdge())

See Also:
[`UMLPackage.getStructuredActivityNode()`](../../metadata/UMLPackage.html#getStructuredActivityNode())
Model:
annotation="MOF package='activities.mdstructuredactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Activity](../mdfundamentalactivities/Activity.html)`
`[getActivity](#getActivity())()`
Returns the value of the '***Activity***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](../mdbasicactivities/ActivityEdge.html)>`
`[getEdge](#getEdge())()`
Returns the value of the '***Edge***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityNode](../mdfundamentalactivities/ActivityNode.html)>`
`[getNode](#getNode())()`
Returns the value of the '***Node***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InputPin](../../actions/mdbasicactions/InputPin.html)>`
`[getStructuredNodeInput](#getStructuredNodeInput())()`
Returns the value of the '***Structured Node Input***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[OutputPin](../../actions/mdbasicactions/OutputPin.html)>`
`[getStructuredNodeOutput](#getStructuredNodeOutput())()`
Returns the value of the '***Structured Node Output***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Variable](Variable.html)>`
`[getVariable](#getVariable())()`
Returns the value of the '***Variable***' containment reference list.
`boolean`
`[hasEdge](#hasEdge())()`

`boolean`
`[hasNode](#hasNode())()`

`boolean`
`[hasStructuredNodeInput](#hasStructuredNodeInput())()`

`boolean`
`[hasStructuredNodeOutput](#hasStructuredNodeOutput())()`

`boolean`
`[hasVariable](#hasVariable())()`

`boolean`
`[isMustIsolate](#isMustIsolate())()`
Returns the value of the '***Must Isolate***' attribute.
`void`
`[setActivity](#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))([Activity](../mdfundamentalactivities/Activity.html) value)`
Sets the value of the '[`*Activity*`](#getActivity())' reference.
`void`
`[setMustIsolate](#setMustIsolate(boolean))(boolean value)`
Sets the value of the '[`*Must Isolate*`](#isMustIsolate())'
 attribute.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.[Action](../../actions/mdbasicactions/Action.html)
`[get_actionExecutionSpecificationOfAction](../../actions/mdbasicactions/Action.html#get_actionExecutionSpecificationOfAction()), [get_actionInputPinOfFromAction](../../actions/mdbasicactions/Action.html#get_actionInputPinOfFromAction()), [get_interactionOfAction](../../actions/mdbasicactions/Action.html#get_interactionOfAction()), [getContext](../../actions/mdbasicactions/Action.html#getContext()), [getInput](../../actions/mdbasicactions/Action.html#getInput()), [getLocalPostcondition](../../actions/mdbasicactions/Action.html#getLocalPostcondition()), [getLocalPrecondition](../../actions/mdbasicactions/Action.html#getLocalPrecondition()), [getOutput](../../actions/mdbasicactions/Action.html#getOutput()), [has_actionExecutionSpecificationOfAction](../../actions/mdbasicactions/Action.html#has_actionExecutionSpecificationOfAction()), [hasInput](../../actions/mdbasicactions/Action.html#hasInput()), [hasLocalPostcondition](../../actions/mdbasicactions/Action.html#hasLocalPostcondition()), [hasLocalPrecondition](../../actions/mdbasicactions/Action.html#hasLocalPrecondition()), [hasOutput](../../actions/mdbasicactions/Action.html#hasOutput()), [isLocallyReentrant](../../actions/mdbasicactions/Action.html#isLocallyReentrant()), [set_actionInputPinOfFromAction](../../actions/mdbasicactions/Action.html#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)), [set_interactionOfAction](../../actions/mdbasicactions/Action.html#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)), [setLocallyReentrant](../../actions/mdbasicactions/Action.html#setLocallyReentrant(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)
`[getContainedEdge](../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()), [getContainedNode](../mdfundamentalactivities/ActivityGroup.html#getContainedNode()), [getInActivity](../mdfundamentalactivities/ActivityGroup.html#getInActivity()), [getSubgroup](../mdfundamentalactivities/ActivityGroup.html#getSubgroup()), [getSuperGroup](../mdfundamentalactivities/ActivityGroup.html#getSuperGroup()), [hasContainedEdge](../mdfundamentalactivities/ActivityGroup.html#hasContainedEdge()), [hasContainedNode](../mdfundamentalactivities/ActivityGroup.html#hasContainedNode()), [hasSubgroup](../mdfundamentalactivities/ActivityGroup.html#hasSubgroup()), [setInActivity](../mdfundamentalactivities/ActivityGroup.html#setInActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setSuperGroup](../mdfundamentalactivities/ActivityGroup.html#setSuperGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityNode](../mdfundamentalactivities/ActivityNode.html)
`[get_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()), [getIncoming](../mdfundamentalactivities/ActivityNode.html#getIncoming()), [getInGroup](../mdfundamentalactivities/ActivityNode.html#getInGroup()), [getInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()), [getInPartition](../mdfundamentalactivities/ActivityNode.html#getInPartition()), [getInStructuredNode](../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()), [getOutgoing](../mdfundamentalactivities/ActivityNode.html#getOutgoing()), [getRedefinedNode](../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()), [has_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()), [hasIncoming](../mdfundamentalactivities/ActivityNode.html#hasIncoming()), [hasInGroup](../mdfundamentalactivities/ActivityNode.html#hasInGroup()), [hasInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()), [hasInPartition](../mdfundamentalactivities/ActivityNode.html#hasInPartition()), [hasOutgoing](../mdfundamentalactivities/ActivityNode.html#hasOutgoing()), [hasRedefinedNode](../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()), [setInStructuredNode](../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.[ExecutableNode](ExecutableNode.html)
`[get_clauseOfBody](ExecutableNode.html#get_clauseOfBody()), [get_clauseOfTest](ExecutableNode.html#get_clauseOfTest()), [get_exceptionHandlerOfHandlerBody](ExecutableNode.html#get_exceptionHandlerOfHandlerBody()), [get_loopNodeOfBodyPart](ExecutableNode.html#get_loopNodeOfBodyPart()), [get_loopNodeOfSetupPart](ExecutableNode.html#get_loopNodeOfSetupPart()), [get_loopNodeOfTest](ExecutableNode.html#get_loopNodeOfTest()), [get_sequenceNodeOfExecutableNode](ExecutableNode.html#get_sequenceNodeOfExecutableNode()), [getHandler](ExecutableNode.html#getHandler()), [has_exceptionHandlerOfHandlerBody](ExecutableNode.html#has_exceptionHandlerOfHandlerBody()), [hasHandler](ExecutableNode.html#hasHandler()), [set_clauseOfBody](ExecutableNode.html#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)), [set_clauseOfTest](ExecutableNode.html#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)), [set_loopNodeOfBodyPart](ExecutableNode.html#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_loopNodeOfSetupPart](ExecutableNode.html#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_loopNodeOfTest](ExecutableNode.html#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_sequenceNodeOfExecutableNode](ExecutableNode.html#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
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
getVariable
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Variable](Variable.html)> getVariable()
Returns the value of the '***Variable***' containment reference list.
 The list contents are of type [`Variable`](Variable.html).
 It is bidirectional and its opposite is '[`*Scope*`](Variable.html#getScope())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Variables defined in the scope of the StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*Variable*' containment reference list.
See Also:
[`UMLPackage.getStructuredActivityNode_Variable()`](../../metadata/UMLPackage.html#getStructuredActivityNode_Variable())
[`Variable.getScope()`](Variable.html#getScope())
Model:
opposite="scope" containment="true" resolveProxies="true" ordered="false"
Generated:
getStructuredNodeOutput
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[OutputPin](../../actions/mdbasicactions/OutputPin.html)> getStructuredNodeOutput()
Returns the value of the '***Structured Node Output***' containment reference list.
 The list contents are of type [`OutputPin`](../../actions/mdbasicactions/OutputPin.html).
 It is bidirectional and its opposite is '[`*structured Activity Node Of Structured Node Output*`](../../actions/mdbasicactions/OutputPin.html#get_structuredActivityNodeOfStructuredNodeOutput())'.
 begin-user-doc 
If the meaning of the '*Structured Node Output*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc 
 begin-model-doc 
 The OutputPins owned by the StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*Structured Node Output*' containment reference list.
See Also:
[`UMLPackage.getStructuredActivityNode_StructuredNodeOutput()`](../../metadata/UMLPackage.html#getStructuredActivityNode_StructuredNodeOutput())
[`OutputPin.get_structuredActivityNodeOfStructuredNodeOutput()`](../../actions/mdbasicactions/OutputPin.html#get_structuredActivityNodeOfStructuredNodeOutput())
Model:
opposite="_structuredActivityNodeOfStructuredNodeOutput" containment="true" resolveProxies="true" ordered="false"
Generated:
getNode
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityNode](../mdfundamentalactivities/ActivityNode.html)> getNode()
Returns the value of the '***Node***' containment reference list.
 The list contents are of type [`ActivityNode`](../mdfundamentalactivities/ActivityNode.html).
 It is bidirectional and its opposite is
 '[`*In Structured Node*`](../mdfundamentalactivities/ActivityNode.html#getInStructuredNode())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ActivityNodes immediately contained in the StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*Node*' containment reference list.
See Also:
[`UMLPackage.getStructuredActivityNode_Node()`](../../metadata/UMLPackage.html#getStructuredActivityNode_Node())
[`ActivityNode.getInStructuredNode()`](../mdfundamentalactivities/ActivityNode.html#getInStructuredNode())
Model:
opposite="inStructuredNode" containment="true" resolveProxies="true" ordered="false"
Generated:
getStructuredNodeInput
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InputPin](../../actions/mdbasicactions/InputPin.html)> getStructuredNodeInput()
Returns the value of the '***Structured Node Input***' containment reference list.
 The list contents are of type [`InputPin`](../../actions/mdbasicactions/InputPin.html).
 It is bidirectional and its opposite is '[`*structured Activity Node Of Structured Node Input*`](../../actions/mdbasicactions/InputPin.html#get_structuredActivityNodeOfStructuredNodeInput())'.
 begin-user-doc 
If the meaning of the '*Structured Node Input*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc 
 begin-model-doc 
 The InputPins owned by the StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*Structured Node Input*' containment reference list.
See Also:
[`UMLPackage.getStructuredActivityNode_StructuredNodeInput()`](../../metadata/UMLPackage.html#getStructuredActivityNode_StructuredNodeInput())
[`InputPin.get_structuredActivityNodeOfStructuredNodeInput()`](../../actions/mdbasicactions/InputPin.html#get_structuredActivityNodeOfStructuredNodeInput())
Model:
opposite="_structuredActivityNodeOfStructuredNodeInput" containment="true" resolveProxies="true" ordered="false"
Generated:
getEdge
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](../mdbasicactivities/ActivityEdge.html)> getEdge()
Returns the value of the '***Edge***' containment reference list.
 The list contents are of type [`ActivityEdge`](../mdbasicactivities/ActivityEdge.html).
 It is bidirectional and its opposite is
 '[`*In Structured Node*`](../mdbasicactivities/ActivityEdge.html#getInStructuredNode())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ActivityEdges immediately contained in the StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*Edge*' containment reference list.
See Also:
[`UMLPackage.getStructuredActivityNode_Edge()`](../../metadata/UMLPackage.html#getStructuredActivityNode_Edge())
[`ActivityEdge.getInStructuredNode()`](../mdbasicactivities/ActivityEdge.html#getInStructuredNode())
Model:
opposite="inStructuredNode" containment="true" resolveProxies="true" ordered="false"
Generated:
isMustIsolate
boolean isMustIsolate()
Returns the value of the '***Must Isolate***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, then any object used by an Action within the StructuredActivityNode cannot be accessed by any Action outside the node until the StructuredActivityNode
 as a whole completes. Any concurrent Actions that would result in accessing such objects are required to have their execution deferred until the completion of
 the StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*Must Isolate*' attribute.
See Also:
[`setMustIsolate(boolean)`](#setMustIsolate(boolean))
[`UMLPackage.getStructuredActivityNode_MustIsolate()`](../../metadata/UMLPackage.html#getStructuredActivityNode_MustIsolate())
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setMustIsolate
void setMustIsolate(boolean value)
Sets the value of the '[`*Must Isolate*`](#isMustIsolate())'
 attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Must Isolate*' attribute.
See Also:
[`isMustIsolate()`](#isMustIsolate())
Generated:
getActivity
@CheckForNull[Activity](../mdfundamentalactivities/Activity.html) getActivity()
Returns the value of the '***Activity***' reference.
 It is bidirectional and its opposite is
 '[`*Structured Node*`](../mdfundamentalactivities/Activity.html#getStructuredNode())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Activity immediately containing the StructuredActivityNode, if it is not contained in another StructuredActivityNode.
 end-model-doc
Specified by:
`[getActivity](../mdfundamentalactivities/ActivityNode.html#getActivity())` in interface `[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`
Returns:
the value of the '*Activity*' reference.
See Also:
[`setActivity(Activity)`](#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))
[`UMLPackage.getStructuredActivityNode_Activity()`](../../metadata/UMLPackage.html#getStructuredActivityNode_Activity())
[`Activity.getStructuredNode()`](../mdfundamentalactivities/Activity.html#getStructuredNode())
Model:
opposite="structuredNode" transient="true" volatile="true" derived="true" ordered="false"
Generated:
setActivity
void setActivity(@CheckForNull
 [Activity](../mdfundamentalactivities/Activity.html) value)
Sets the value of the '[`*Activity*`](#getActivity())' reference.
 begin-user-doc 
 end-user-doc
Specified by:
`[setActivity](../mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))` in interface `[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`
Parameters:
`value` - the new value of the '*Activity*' reference.
See Also:
[`getActivity()`](#getActivity())
Generated:
hasVariable
boolean hasVariable()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasStructuredNodeOutput
boolean hasStructuredNodeOutput()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasNode
boolean hasNode()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasStructuredNodeInput
boolean hasStructuredNodeInput()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities</a></div>
<h1 class="title" title="Interface StructuredActivityNode">Interface StructuredActivityNode</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></code>, <code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">StructuredActivityNode</span><span class="extends-implements">
extends <a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a>, <a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>, <a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Structured Activity Node</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A StructuredActivityNode is an Action that is also an ActivityGroup and whose behavior is specified by the ActivityNodes and ActivityEdges it so contains. Unlike
 other kinds of ActivityGroup, a StructuredActivityNode owns the ActivityNodes and ActivityEdges it contains, and so a node or edge can only be directly contained in
 one StructuredActivityNode, though StructuredActivityNodes may be nested.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isMustIsolate()"><code><em>Must Isolate</em></code></a></li>
<li><a href="#getNode()"><code><em>Node</em></code></a></li>
<li><a href="#getStructuredNodeInput()"><code><em>Structured Node Input</em></code></a></li>
<li><a href="#getStructuredNodeOutput()"><code><em>Structured Node Output</em></code></a></li>
<li><a href="#getVariable()"><code><em>Variable</em></code></a></li>
<li><a href="#getEdge()"><code><em>Edge</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode()"><code>UMLPackage.getStructuredActivityNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='activities.mdstructuredactivities'"</dd>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getActivity()">getActivity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Activity</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEdge()">getEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Edge</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNode()">getNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Node</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStructuredNodeInput()">getStructuredNodeInput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Structured Node Input</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStructuredNodeOutput()">getStructuredNodeOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Structured Node Output</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariable()">getVariable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Variable</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEdge()">hasEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasNode()">hasNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasStructuredNodeInput()">hasStructuredNodeInput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasStructuredNodeOutput()">hasStructuredNodeOutput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasVariable()">hasVariable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isMustIsolate()">isMustIsolate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Must Isolate</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a><wbr/>(<a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getActivity()"><code><em>Activity</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMustIsolate(boolean)">setMustIsolate</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isMustIsolate()"><code><em>Must Isolate</em></code></a>'
 attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.<a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></h3>
<code><a href="../../actions/mdbasicactions/Action.html#get_actionExecutionSpecificationOfAction()">get_actionExecutionSpecificationOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#get_actionInputPinOfFromAction()">get_actionInputPinOfFromAction</a>, <a href="../../actions/mdbasicactions/Action.html#get_interactionOfAction()">get_interactionOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#getContext()">getContext</a>, <a href="../../actions/mdbasicactions/Action.html#getInput()">getInput</a>, <a href="../../actions/mdbasicactions/Action.html#getLocalPostcondition()">getLocalPostcondition</a>, <a href="../../actions/mdbasicactions/Action.html#getLocalPrecondition()">getLocalPrecondition</a>, <a href="../../actions/mdbasicactions/Action.html#getOutput()">getOutput</a>, <a href="../../actions/mdbasicactions/Action.html#has_actionExecutionSpecificationOfAction()">has_actionExecutionSpecificationOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#hasInput()">hasInput</a>, <a href="../../actions/mdbasicactions/Action.html#hasLocalPostcondition()">hasLocalPostcondition</a>, <a href="../../actions/mdbasicactions/Action.html#hasLocalPrecondition()">hasLocalPrecondition</a>, <a href="../../actions/mdbasicactions/Action.html#hasOutput()">hasOutput</a>, <a href="../../actions/mdbasicactions/Action.html#isLocallyReentrant()">isLocallyReentrant</a>, <a href="../../actions/mdbasicactions/Action.html#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">set_actionInputPinOfFromAction</a>, <a href="../../actions/mdbasicactions/Action.html#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">set_interactionOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#setLocallyReentrant(boolean)">setLocallyReentrant</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></h3>
<code><a href="../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()">getContainedEdge</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getContainedNode()">getContainedNode</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getInActivity()">getInActivity</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getSubgroup()">getSubgroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getSuperGroup()">getSuperGroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasContainedEdge()">hasContainedEdge</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasContainedNode()">hasContainedNode</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasSubgroup()">hasSubgroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#setInActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setInActivity</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#setSuperGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup)">setSuperGroup</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></h3>
<code><a href="../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()">get_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getIncoming()">getIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInGroup()">getInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()">getInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInPartition()">getInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()">getInStructuredNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getOutgoing()">getOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()">getRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()">has_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasIncoming()">hasIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInGroup()">hasInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()">hasInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInPartition()">hasInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasOutgoing()">hasOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()">hasRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></h3>
<code><a href="ExecutableNode.html#get_clauseOfBody()">get_clauseOfBody</a>, <a href="ExecutableNode.html#get_clauseOfTest()">get_clauseOfTest</a>, <a href="ExecutableNode.html#get_exceptionHandlerOfHandlerBody()">get_exceptionHandlerOfHandlerBody</a>, <a href="ExecutableNode.html#get_loopNodeOfBodyPart()">get_loopNodeOfBodyPart</a>, <a href="ExecutableNode.html#get_loopNodeOfSetupPart()">get_loopNodeOfSetupPart</a>, <a href="ExecutableNode.html#get_loopNodeOfTest()">get_loopNodeOfTest</a>, <a href="ExecutableNode.html#get_sequenceNodeOfExecutableNode()">get_sequenceNodeOfExecutableNode</a>, <a href="ExecutableNode.html#getHandler()">getHandler</a>, <a href="ExecutableNode.html#has_exceptionHandlerOfHandlerBody()">has_exceptionHandlerOfHandlerBody</a>, <a href="ExecutableNode.html#hasHandler()">hasHandler</a>, <a href="ExecutableNode.html#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfBody</a>, <a href="ExecutableNode.html#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfTest</a>, <a href="ExecutableNode.html#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfBodyPart</a>, <a href="ExecutableNode.html#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfSetupPart</a>, <a href="ExecutableNode.html#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfTest</a>, <a href="ExecutableNode.html#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">set_sequenceNodeOfExecutableNode</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
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
<section class="detail" id="getVariable()">
<h3>getVariable</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a>&gt;</span> <span class="element-name">getVariable</span>()</div>
<div class="block">Returns the value of the '<em><b>Variable</b></em>' containment reference list.
 The list contents are of type <a href="Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a>.
 It is bidirectional and its opposite is '<a href="Variable.html#getScope()"><code><em>Scope</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Variables defined in the scope of the StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Variable</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_Variable()"><code>UMLPackage.getStructuredActivityNode_Variable()</code></a></li>
<li><a href="Variable.html#getScope()"><code>Variable.getScope()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="scope" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuredNodeOutput()">
<h3>getStructuredNodeOutput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a>&gt;</span> <span class="element-name">getStructuredNodeOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>Structured Node Output</b></em>' containment reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/OutputPin.html#get_structuredActivityNodeOfStructuredNodeOutput()"><code><em>structured Activity Node Of Structured Node Output</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Structured Node Output</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The OutputPins owned by the StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Structured Node Output</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_StructuredNodeOutput()"><code>UMLPackage.getStructuredActivityNode_StructuredNodeOutput()</code></a></li>
<li><a href="../../actions/mdbasicactions/OutputPin.html#get_structuredActivityNodeOfStructuredNodeOutput()"><code>OutputPin.get_structuredActivityNodeOfStructuredNodeOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_structuredActivityNodeOfStructuredNodeOutput" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNode()">
<h3>getNode</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>&gt;</span> <span class="element-name">getNode</span>()</div>
<div class="block">Returns the value of the '<em><b>Node</b></em>' containment reference list.
 The list contents are of type <a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()"><code><em>In Structured Node</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ActivityNodes immediately contained in the StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Node</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_Node()"><code>UMLPackage.getStructuredActivityNode_Node()</code></a></li>
<li><a href="../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()"><code>ActivityNode.getInStructuredNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inStructuredNode" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuredNodeInput()">
<h3>getStructuredNodeInput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a>&gt;</span> <span class="element-name">getStructuredNodeInput</span>()</div>
<div class="block">Returns the value of the '<em><b>Structured Node Input</b></em>' containment reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/InputPin.html#get_structuredActivityNodeOfStructuredNodeInput()"><code><em>structured Activity Node Of Structured Node Input</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Structured Node Input</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The InputPins owned by the StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Structured Node Input</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_StructuredNodeInput()"><code>UMLPackage.getStructuredActivityNode_StructuredNodeInput()</code></a></li>
<li><a href="../../actions/mdbasicactions/InputPin.html#get_structuredActivityNodeOfStructuredNodeInput()"><code>InputPin.get_structuredActivityNodeOfStructuredNodeInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_structuredActivityNodeOfStructuredNodeInput" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEdge()">
<h3>getEdge</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</span> <span class="element-name">getEdge</span>()</div>
<div class="block">Returns the value of the '<em><b>Edge</b></em>' containment reference list.
 The list contents are of type <a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdbasicactivities/ActivityEdge.html#getInStructuredNode()"><code><em>In Structured Node</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ActivityEdges immediately contained in the StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Edge</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_Edge()"><code>UMLPackage.getStructuredActivityNode_Edge()</code></a></li>
<li><a href="../mdbasicactivities/ActivityEdge.html#getInStructuredNode()"><code>ActivityEdge.getInStructuredNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inStructuredNode" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMustIsolate()">
<h3>isMustIsolate</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isMustIsolate</span>()</div>
<div class="block">Returns the value of the '<em><b>Must Isolate</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, then any object used by an Action within the StructuredActivityNode cannot be accessed by any Action outside the node until the StructuredActivityNode
 as a whole completes. Any concurrent Actions that would result in accessing such objects are required to have their execution deferred until the completion of
 the StructuredActivityNode.
 <p>
<!-- end-model-doc --></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Must Isolate</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setMustIsolate(boolean)"><code>setMustIsolate(boolean)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_MustIsolate()"><code>UMLPackage.getStructuredActivityNode_MustIsolate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMustIsolate(boolean)">
<h3>setMustIsolate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMustIsolate</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isMustIsolate()"><code><em>Must Isolate</em></code></a>'
 attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Must Isolate</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isMustIsolate()"><code>isMustIsolate()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivity()">
<h3>getActivity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">getActivity</span>()</div>
<div class="block">Returns the value of the '<em><b>Activity</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../mdfundamentalactivities/Activity.html#getStructuredNode()"><code><em>Structured Node</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Activity immediately containing the StructuredActivityNode, if it is not contained in another StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../mdfundamentalactivities/ActivityNode.html#getActivity()">getActivity</a></code> in interface <code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Activity</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)"><code>setActivity(Activity)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getStructuredActivityNode_Activity()"><code>UMLPackage.getStructuredActivityNode_Activity()</code></a></li>
<li><a href="../mdfundamentalactivities/Activity.html#getStructuredNode()"><code>Activity.getStructuredNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="structuredNode" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">
<h3>setActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setActivity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getActivity()"><code><em>Activity</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a></code> in interface <code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Activity</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getActivity()"><code>getActivity()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasVariable()">
<h3>hasVariable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasVariable</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStructuredNodeOutput()">
<h3>hasStructuredNodeOutput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasStructuredNodeOutput</span>()
                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
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
<section class="detail" id="hasStructuredNodeInput()">
<h3>hasStructuredNodeInput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasStructuredNodeInput</span>()
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
