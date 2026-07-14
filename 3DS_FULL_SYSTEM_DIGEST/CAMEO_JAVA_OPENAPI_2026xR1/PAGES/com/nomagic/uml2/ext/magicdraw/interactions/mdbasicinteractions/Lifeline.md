# JAVA OPENAPI: Lifeline (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html
- source_path: `com/nomagic/uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html`
- source_sha256: `adf33fd8d215dbedf5f3e21245ed1e94ac3c312d0ea11489450f958891ccd69b`
- captured_utc: `2026-07-14T16:46:32.673234+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions](package-summary.html)

## Interface Lifeline

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceLifelineextends [NamedElement](../../classes/mdkernel/NamedElement.html)

begin-user-doc 
 A representation of the model object '***Lifeline***'.
 end-user-doc 
begin-model-doc 
 A Lifeline represents an individual participant in the Interaction. While parts and structural features may have multiplicity greater than 1, Lifelines represent
 only one interacting entity.
 end-model-doc 
The following features are supported:
 [`*Covered By*`](#getCoveredBy())
[`*state Invariant Of Covered*`](#get_stateInvariantOfCovered())
[`*occurrence Specification Of Covered*`](#get_occurrenceSpecificationOfCovered())
[`*Interaction*`](#getInteraction())
[`*Decomposed As*`](#getDecomposedAs())
[`*Represents*`](#getRepresents())
[`*Selector*`](#getSelector())

See Also:
[`UMLPackage.getLifeline()`](../../metadata/UMLPackage.html#getLifeline())
Model:
annotation="MOF package='interactions.mdbasicinteractions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OccurrenceSpecification](OccurrenceSpecification.html)>`
`[get_occurrenceSpecificationOfCovered](#get_occurrenceSpecificationOfCovered())()`
Returns the value of the '***occurrence Specification Of Covered***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[StateInvariant](StateInvariant.html)>`
`[get_stateInvariantOfCovered](#get_stateInvariantOfCovered())()`
Returns the value of the '***state Invariant Of Covered***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](InteractionFragment.html)>`
`[getCoveredBy](#getCoveredBy())()`
Returns the value of the '***Covered By***' reference list.
`[PartDecomposition](../mdfragments/PartDecomposition.html)`
`[getDecomposedAs](#getDecomposedAs())()`
Returns the value of the '***Decomposed As***' reference.
`[Interaction](Interaction.html)`
`[getInteraction](#getInteraction())()`
Returns the value of the '***Interaction***' container reference.
`[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)`
`[getRepresents](#getRepresents())()`
Returns the value of the '***Represents***' reference.
`[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`
`[getSelector](#getSelector())()`
Returns the value of the '***Selector***' containment reference.
`boolean`
`[has_occurrenceSpecificationOfCovered](#has_occurrenceSpecificationOfCovered())()`

`boolean`
`[has_stateInvariantOfCovered](#has_stateInvariantOfCovered())()`

`boolean`
`[hasCoveredBy](#hasCoveredBy())()`

`void`
`[setDecomposedAs](#setDecomposedAs(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition))([PartDecomposition](../mdfragments/PartDecomposition.html) value)`
Sets the value of the '[`*Decomposed As*`](#getDecomposedAs())' reference.
`void`
`[setInteraction](#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))([Interaction](Interaction.html) value)`
Sets the value of the '[`*Interaction*`](#getInteraction())' container reference.
`void`
`[setRepresents](#setRepresents(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement))([ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html) value)`
Sets the value of the '[`*Represents*`](#getRepresents())' reference.
`void`
`[setSelector](#setSelector(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)`
Sets the value of the '[`*Selector*`](#getSelector())' containment reference.
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
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
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
getRepresents
@CheckForNull[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html) getRepresents()
Returns the value of the '***Represents***' reference.
 It is bidirectional and its opposite is '
invalid reference
`.compositestructures.mdinternalstructures.ConnectableElement#get_lifelineOfRepresents *lifeline Of Represents*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the ConnectableElement within the classifier that contains the enclosing interaction.
 end-model-doc
Returns:
the value of the '*Represents*' reference.
See Also:
[`setRepresents(ConnectableElement)`](#setRepresents(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement))
[`UMLPackage.getLifeline_Represents()`](../../metadata/UMLPackage.html#getLifeline_Represents())
[`ConnectableElement.get_lifelineOfRepresents()`](../../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents())
Model:
opposite="_lifelineOfRepresents" ordered="false"
Generated:
setRepresents
void setRepresents(@CheckForNull
 [ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html) value)
Sets the value of the '[`*Represents*`](#getRepresents())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Represents*' reference.
See Also:
[`getRepresents()`](#getRepresents())
Generated:
getInteraction
@CheckForNull[Interaction](Interaction.html) getInteraction()
Returns the value of the '***Interaction***' container reference.
 It is bidirectional and its opposite is '[`*Lifeline*`](Interaction.html#getLifeline())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Interaction enclosing this Lifeline.
 end-model-doc
Returns:
the value of the '*Interaction*' container reference.
See Also:
[`setInteraction(Interaction)`](#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))
[`UMLPackage.getLifeline_Interaction()`](../../metadata/UMLPackage.html#getLifeline_Interaction())
[`Interaction.getLifeline()`](Interaction.html#getLifeline())
Model:
opposite="lifeline" required="true" transient="false" ordered="false"
Generated:
setInteraction
void setInteraction(@CheckForNull
 [Interaction](Interaction.html) value)
Sets the value of the '[`*Interaction*`](#getInteraction())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Interaction*' container reference.
See Also:
[`getInteraction()`](#getInteraction())
Generated:
getSelector
@CheckForNull[ValueSpecification](../../classes/mdkernel/ValueSpecification.html) getSelector()
Returns the value of the '***Selector***' containment reference.
 It is bidirectional and its opposite is
 '[`*lifeline Of Selector*`](../../classes/mdkernel/ValueSpecification.html#get_lifelineOfSelector())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If the referenced ConnectableElement is multivalued, then this specifies the specific individual part within that set.
 end-model-doc
Returns:
the value of the '*Selector*' containment reference.
See Also:
[`setSelector(ValueSpecification)`](#setSelector(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getLifeline_Selector()`](../../metadata/UMLPackage.html#getLifeline_Selector())
[`ValueSpecification.get_lifelineOfSelector()`](../../classes/mdkernel/ValueSpecification.html#get_lifelineOfSelector())
Model:
opposite="_lifelineOfSelector" containment="true" resolveProxies="true" ordered="false"
Generated:
setSelector
void setSelector(@CheckForNull
 [ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)
Sets the value of the '[`*Selector*`](#getSelector())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Selector*' containment reference.
See Also:
[`getSelector()`](#getSelector())
Generated:
get_occurrenceSpecificationOfCovered
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OccurrenceSpecification](OccurrenceSpecification.html)> get_occurrenceSpecificationOfCovered()
Returns the value of the '***occurrence Specification Of Covered***' reference list.
 The list contents are of type [`OccurrenceSpecification`](OccurrenceSpecification.html).
 It is bidirectional and its opposite is
 '[`*Covered*`](OccurrenceSpecification.html#getCovered())'.
 begin-user-doc 
If the meaning of the '*occurrence Specification Of Covered*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*occurrence Specification Of Covered*' reference list.
See Also:
[`UMLPackage.getLifeline__occurrenceSpecificationOfCovered()`](../../metadata/UMLPackage.html#getLifeline__occurrenceSpecificationOfCovered())
[`OccurrenceSpecification.getCovered()`](OccurrenceSpecification.html#getCovered())
Model:
opposite="covered" volatile="true"
Generated:
get_stateInvariantOfCovered
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[StateInvariant](StateInvariant.html)> get_stateInvariantOfCovered()
Returns the value of the '***state Invariant Of Covered***' reference list.
 The list contents are of type [`StateInvariant`](StateInvariant.html).
 It is bidirectional and its opposite is '[`*Covered*`](StateInvariant.html#getCovered())'.
 begin-user-doc 
If the meaning of the '*state Invariant Of Covered*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*state Invariant Of Covered*' reference list.
See Also:
[`UMLPackage.getLifeline__stateInvariantOfCovered()`](../../metadata/UMLPackage.html#getLifeline__stateInvariantOfCovered())
[`StateInvariant.getCovered()`](StateInvariant.html#getCovered())
Model:
opposite="covered" volatile="true" ordered="false"
Generated:
getDecomposedAs
@CheckForNull[PartDecomposition](../mdfragments/PartDecomposition.html) getDecomposedAs()
Returns the value of the '***Decomposed As***' reference.
 It is bidirectional and its opposite is
 '[`*lifeline Of Decomposed As*`](../mdfragments/PartDecomposition.html#get_lifelineOfDecomposedAs())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Interaction that represents the decomposition.
 end-model-doc
Returns:
the value of the '*Decomposed As*' reference.
See Also:
[`setDecomposedAs(PartDecomposition)`](#setDecomposedAs(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition))
[`UMLPackage.getLifeline_DecomposedAs()`](../../metadata/UMLPackage.html#getLifeline_DecomposedAs())
[`PartDecomposition.get_lifelineOfDecomposedAs()`](../mdfragments/PartDecomposition.html#get_lifelineOfDecomposedAs())
Model:
opposite="_lifelineOfDecomposedAs" ordered="false"
Generated:
setDecomposedAs
void setDecomposedAs(@CheckForNull
 [PartDecomposition](../mdfragments/PartDecomposition.html) value)
Sets the value of the '[`*Decomposed As*`](#getDecomposedAs())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Decomposed As*' reference.
See Also:
[`getDecomposedAs()`](#getDecomposedAs())
Generated:
getCoveredBy
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InteractionFragment](InteractionFragment.html)> getCoveredBy()
Returns the value of the '***Covered By***' reference list.
 The list contents are of type [`InteractionFragment`](InteractionFragment.html).
 It is bidirectional and its opposite is '[`*Covered*`](InteractionFragment.html#getCovered())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the InteractionFragments in which this Lifeline takes part.
 end-model-doc
Returns:
the value of the '*Covered By*' reference list.
See Also:
[`UMLPackage.getLifeline_CoveredBy()`](../../metadata/UMLPackage.html#getLifeline_CoveredBy())
[`InteractionFragment.getCovered()`](InteractionFragment.html#getCovered())
Model:
opposite="covered" ordered="false"
Generated:
has_occurrenceSpecificationOfCovered
boolean has_occurrenceSpecificationOfCovered()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_stateInvariantOfCovered
boolean has_stateInvariantOfCovered()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasCoveredBy
boolean hasCoveredBy()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions</a></div>
<h1 class="title" title="Interface Lifeline">Interface Lifeline</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Lifeline</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Lifeline</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Lifeline represents an individual participant in the Interaction. While parts and structural features may have multiplicity greater than 1, Lifelines represent
 only one interacting entity.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getCoveredBy()"><code><em>Covered By</em></code></a></li>
<li><a href="#get_stateInvariantOfCovered()"><code><em>state Invariant Of Covered</em></code></a></li>
<li><a href="#get_occurrenceSpecificationOfCovered()"><code><em>occurrence Specification Of Covered</em></code></a></li>
<li><a href="#getInteraction()"><code><em>Interaction</em></code></a></li>
<li><a href="#getDecomposedAs()"><code><em>Decomposed As</em></code></a></li>
<li><a href="#getRepresents()"><code><em>Represents</em></code></a></li>
<li><a href="#getSelector()"><code><em>Selector</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getLifeline()"><code>UMLPackage.getLifeline()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='interactions.mdbasicinteractions'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_occurrenceSpecificationOfCovered()">get_occurrenceSpecificationOfCovered</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>occurrence Specification Of Covered</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stateInvariantOfCovered()">get_stateInvariantOfCovered</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>state Invariant Of Covered</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCoveredBy()">getCoveredBy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Covered By</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDecomposedAs()">getDecomposedAs</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Decomposed As</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInteraction()">getInteraction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Interaction</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresents()">getRepresents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Represents</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSelector()">getSelector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Selector</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_occurrenceSpecificationOfCovered()">has_occurrenceSpecificationOfCovered</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_stateInvariantOfCovered()">has_stateInvariantOfCovered</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasCoveredBy()">hasCoveredBy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDecomposedAs(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition)">setDecomposedAs</a><wbr/>(<a href="../mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDecomposedAs()"><code><em>Decomposed As</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">setInteraction</a><wbr/>(<a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInteraction()"><code><em>Interaction</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRepresents(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement)">setRepresents</a><wbr/>(<a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getRepresents()"><code><em>Represents</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSelector(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setSelector</a><wbr/>(<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSelector()"><code><em>Selector</em></code></a>' containment reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<section class="detail" id="getRepresents()">
<h3>getRepresents</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></span> <span class="element-name">getRepresents</span>()</div>
<div class="block">Returns the value of the '<em><b>Represents</b></em>' reference.
 It is bidirectional and its opposite is '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>.compositestructures.mdinternalstructures.ConnectableElement#get_lifelineOfRepresents <em>lifeline Of Represents</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the ConnectableElement within the classifier that contains the enclosing interaction.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Represents</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setRepresents(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement)"><code>setRepresents(ConnectableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLifeline_Represents()"><code>UMLPackage.getLifeline_Represents()</code></a></li>
<li><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html#get_lifelineOfRepresents()"><code>ConnectableElement.get_lifelineOfRepresents()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_lifelineOfRepresents" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRepresents(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.ConnectableElement)">
<h3>setRepresents</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRepresents</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a> value)</span></div>
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
<section class="detail" id="getInteraction()">
<h3>getInteraction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">getInteraction</span>()</div>
<div class="block">Returns the value of the '<em><b>Interaction</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Interaction.html#getLifeline()"><code><em>Lifeline</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Interaction enclosing this Lifeline.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Interaction</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)"><code>setInteraction(Interaction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLifeline_Interaction()"><code>UMLPackage.getLifeline_Interaction()</code></a></li>
<li><a href="Interaction.html#getLifeline()"><code>Interaction.getLifeline()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="lifeline" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">
<h3>setInteraction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInteraction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInteraction()"><code><em>Interaction</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Interaction</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getInteraction()"><code>getInteraction()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelector()">
<h3>getSelector</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getSelector</span>()</div>
<div class="block">Returns the value of the '<em><b>Selector</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/ValueSpecification.html#get_lifelineOfSelector()"><code><em>lifeline Of Selector</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If the referenced ConnectableElement is multivalued, then this specifies the specific individual part within that set.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Selector</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSelector(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setSelector(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLifeline_Selector()"><code>UMLPackage.getLifeline_Selector()</code></a></li>
<li><a href="../../classes/mdkernel/ValueSpecification.html#get_lifelineOfSelector()"><code>ValueSpecification.get_lifelineOfSelector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_lifelineOfSelector" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelector(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setSelector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSelector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSelector()"><code><em>Selector</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Selector</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSelector()"><code>getSelector()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_occurrenceSpecificationOfCovered()">
<h3>get_occurrenceSpecificationOfCovered</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">OccurrenceSpecification</a>&gt;</span> <span class="element-name">get_occurrenceSpecificationOfCovered</span>()</div>
<div class="block">Returns the value of the '<em><b>occurrence Specification Of Covered</b></em>' reference list.
 The list contents are of type <a href="OccurrenceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>OccurrenceSpecification</code></a>.
 It is bidirectional and its opposite is
 '<a href="OccurrenceSpecification.html#getCovered()"><code><em>Covered</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>occurrence Specification Of Covered</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>occurrence Specification Of Covered</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getLifeline__occurrenceSpecificationOfCovered()"><code>UMLPackage.getLifeline__occurrenceSpecificationOfCovered()</code></a></li>
<li><a href="OccurrenceSpecification.html#getCovered()"><code>OccurrenceSpecification.getCovered()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="covered" volatile="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stateInvariantOfCovered()">
<h3>get_stateInvariantOfCovered</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a>&gt;</span> <span class="element-name">get_stateInvariantOfCovered</span>()</div>
<div class="block">Returns the value of the '<em><b>state Invariant Of Covered</b></em>' reference list.
 The list contents are of type <a href="StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>StateInvariant</code></a>.
 It is bidirectional and its opposite is '<a href="StateInvariant.html#getCovered()"><code><em>Covered</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>state Invariant Of Covered</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>state Invariant Of Covered</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getLifeline__stateInvariantOfCovered()"><code>UMLPackage.getLifeline__stateInvariantOfCovered()</code></a></li>
<li><a href="StateInvariant.html#getCovered()"><code>StateInvariant.getCovered()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="covered" volatile="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDecomposedAs()">
<h3>getDecomposedAs</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a></span> <span class="element-name">getDecomposedAs</span>()</div>
<div class="block">Returns the value of the '<em><b>Decomposed As</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../mdfragments/PartDecomposition.html#get_lifelineOfDecomposedAs()"><code><em>lifeline Of Decomposed As</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Interaction that represents the decomposition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Decomposed As</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDecomposedAs(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition)"><code>setDecomposedAs(PartDecomposition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLifeline_DecomposedAs()"><code>UMLPackage.getLifeline_DecomposedAs()</code></a></li>
<li><a href="../mdfragments/PartDecomposition.html#get_lifelineOfDecomposedAs()"><code>PartDecomposition.get_lifelineOfDecomposedAs()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_lifelineOfDecomposedAs" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDecomposedAs(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.PartDecomposition)">
<h3>setDecomposedAs</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDecomposedAs</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdfragments/PartDecomposition.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">PartDecomposition</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDecomposedAs()"><code><em>Decomposed As</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Decomposed As</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getDecomposedAs()"><code>getDecomposedAs()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCoveredBy()">
<h3>getCoveredBy</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt;</span> <span class="element-name">getCoveredBy</span>()</div>
<div class="block">Returns the value of the '<em><b>Covered By</b></em>' reference list.
 The list contents are of type <a href="InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a>.
 It is bidirectional and its opposite is '<a href="InteractionFragment.html#getCovered()"><code><em>Covered</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the InteractionFragments in which this Lifeline takes part.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Covered By</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getLifeline_CoveredBy()"><code>UMLPackage.getLifeline_CoveredBy()</code></a></li>
<li><a href="InteractionFragment.html#getCovered()"><code>InteractionFragment.getCovered()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="covered" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_occurrenceSpecificationOfCovered()">
<h3>has_occurrenceSpecificationOfCovered</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_occurrenceSpecificationOfCovered</span>()
                                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_stateInvariantOfCovered()">
<h3>has_stateInvariantOfCovered</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_stateInvariantOfCovered</span>()
                             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasCoveredBy()">
<h3>hasCoveredBy</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasCoveredBy</span>()
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
